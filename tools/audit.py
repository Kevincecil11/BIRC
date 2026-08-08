import os, json, traceback
from playwright.sync_api import sync_playwright

PAGES = [
    'desktop-creators.html',
    'desktop-rice-masterchef.html',
    'desktop-artists.html',
    'desktop-partnership.html',
    'desktop-plan-visit.html',
    'desktop-contact.html',
]

JS = r"""
() => {
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
  const out = { contrast: [], overflow: [], centered: [], edges: {} };
  const els = [...document.querySelectorAll('main h1,main h2,main h3,main h4,main p,main li,main label,main small,main strong,main span,main summary,main address,main button,main a')];
  for (const el of els) {
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) < 0.2) continue;
    const txt = (el.textContent || '').trim();
    if (!txt) continue;
    const fg = parse(cs.color);
    if (fg && fg.a > 0.3) {
      const cr = ratio(fg, bgOf(el));
      if (cr < 3.0) out.contrast.push({ tag: el.tagName, cls: el.className.toString().slice(0, 40), ratio: Math.round(cr * 100) / 100, color: cs.color, text: txt.slice(0, 48) });
    }
    if (r.right > window.innerWidth + 2 || r.left < -2) out.overflow.push({ tag: el.tagName, cls: el.className.toString().slice(0, 40), left: Math.round(r.left), right: Math.round(r.right), text: txt.slice(0, 40) });
    if (['H1','H2','H3','P'].includes(el.tagName) && cs.textAlign === 'center') out.centered.push({ tag: el.tagName, cls: el.className.toString().slice(0, 40), text: txt.slice(0, 40) });
    if (['H1','H2','H3'].includes(el.tagName)) {
      const k = String(Math.round(r.left));
      out.edges[k] = (out.edges[k] || 0) + 1;
    }
  }
  out.docWidth = document.documentElement.scrollWidth;
  out.viewport = window.innerWidth;
  return out;
}
"""

lines = []
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1440, 'height': 900})
        for f in PAGES:
            if not os.path.exists(f):
                continue
            pg.goto('http://127.0.0.1:8000/%s' % f, wait_until='load')
            pg.wait_for_timeout(2000)
            pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
            pg.wait_for_timeout(600)
            res = pg.evaluate(JS)
            lines.append('==== %s ====' % f)
            lines.append('docWidth %s / viewport %s' % (res['docWidth'], res['viewport']))
            edges = sorted(res['edges'].items(), key=lambda kv: -kv[1])[:6]
            lines.append('heading left edges (px:count): %s' % edges)
            lines.append('centered headings/paras: %s' % len(res['centered']))
            for c in res['centered'][:12]:
                lines.append('  CENTER %s.%s %s' % (c['tag'], c['cls'], c['text']))
            lines.append('low contrast items: %s' % len(res['contrast']))
            seen = set()
            for c in res['contrast']:
                key = (c['tag'], c['cls'], c['color'])
                if key in seen:
                    continue
                seen.add(key)
                lines.append('  CONTRAST %.2f %s.%s color=%s :: %s' % (c['ratio'], c['tag'], c['cls'], c['color'], c['text']))
                if len(seen) > 14:
                    break
            lines.append('overflow items: %s' % len(res['overflow']))
            for c in res['overflow'][:8]:
                lines.append('  OVERFLOW %s.%s l=%s r=%s %s' % (c['tag'], c['cls'], c['left'], c['right'], c['text']))
            lines.append('')
        b.close()
except Exception:
    lines.append(traceback.format_exc())

os.makedirs('_inspect', exist_ok=True)
open('_inspect/audit.txt', 'w', encoding='utf-8').write('\n'.join(lines))
