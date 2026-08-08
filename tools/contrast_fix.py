import os, re, traceback
from playwright.sync_api import sync_playwright

PAGES = [
    'desktop-rice-masterchef.html',
    'desktop-artists.html',
    'desktop-partnership.html',
    'desktop-plan-visit.html',
    'desktop-contact.html',
    'contact.html',
]

JS = r"""
(threshold) => {
  const parse = (c) => {
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(',').map(x => parseFloat(x.trim()));
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const lum = (c) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
  };
  const ratio = (a, b) => { const l1 = lum(a), l2 = lum(b); const hi = Math.max(l1, l2), lo = Math.min(l1, l2); return (hi + 0.05) / (lo + 0.05); };
  const bgOf = (el) => {
    let n = el;
    while (n && n !== document.documentElement) {
      const c = parse(getComputedStyle(n).backgroundColor);
      if (c && c.a > 0.5) return c;
      n = n.parentElement;
    }
    return { r: 13, g: 13, b: 11, a: 1 };
  };
  const path = (el) => {
    const parts = [];
    let n = el;
    while (n && n.tagName && n.tagName.toLowerCase() !== 'body') {
      const p = n.parentElement;
      if (!p) break;
      const i = [...p.children].indexOf(n) + 1;
      parts.unshift(n.tagName.toLowerCase() + ':nth-child(' + i + ')');
      n = p;
    }
    return 'body > ' + parts.join(' > ');
  };
  const fixes = [];
  const els = [...document.querySelectorAll('main h1,main h2,main h3,main h4,main p,main li,main label,main small,main strong,main span,main summary,main address,main a,main button,main div')];
  for (const el of els) {
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 0);
    if (!own) continue;
    const fg = parse(cs.color);
    if (!fg || fg.a < 0.3) continue;
    const bg = bgOf(el);
    const cr = ratio(fg, bg);
    if (cr >= threshold) continue;
    const target = lum(bg) > 0.35 ? '#0d0d0b' : '#faf0e6';
    fixes.push({ sel: path(el), color: target, was: cs.color, ratio: Math.round(cr * 100) / 100, text: (el.textContent || '').trim().slice(0, 40) });
  }
  return fixes;
}
"""

log = []


def inject(path, css, marker):
    raw = open(path, encoding='utf-8').read()
    tag = '<style id="%s">%s</style>' % (marker, css)
    if 'id="%s"' % marker in raw:
        raw = re.sub(r'<style id="%s">.*?</style>' % marker, lambda m: tag, raw, flags=re.S)
    else:
        raw = raw.replace('</head>', tag + '\n</head>', 1)
    open(path, 'w', encoding='utf-8').write(raw)


try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        for f in PAGES:
            if not os.path.exists(f):
                continue
            width = 1440 if f.startswith('desktop-') else 430
            pg = b.new_page(viewport={'width': width, 'height': 900})
            pg.goto('http://127.0.0.1:8000/%s' % f, wait_until='domcontentloaded', timeout=60000)
            pg.wait_for_timeout(2500)
            pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
            pg.wait_for_timeout(500)
            fixes = pg.evaluate(JS, 1.9)
            seen = {}
            for fx in fixes:
                seen[fx['sel']] = fx['color']
            if seen:
                media = '@media (min-width:900px){' if f.startswith('desktop-') else ''
                close = '}' if media else ''
                rules = '\n'.join('%s{color:%s!important}' % (s, c) for s, c in seen.items())
                inject(f, '\n' + media + '\n' + rules + '\n' + close + '\n', 'dt-contrast')
            log.append('%s: %s fixes' % (f, len(seen)))
            for fx in fixes[:10]:
                log.append('   %.2f %s -> %s :: %s' % (fx['ratio'], fx['was'], seen[fx['sel']], fx['text']))
            pg.close()
        b.close()
except Exception:
    log.append(traceback.format_exc())

os.makedirs('_inspect', exist_ok=True)
open('_inspect/contrast-log.txt', 'w', encoding='utf-8').write('\n'.join(log))
