import os, traceback
from playwright.sync_api import sync_playwright

out = []

JS = r"""
(sels) => {
  const res = {};
  for (const s of sels) {
    const els = [...document.querySelectorAll(s)];
    res[s] = els.slice(0, 12).map(el => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return { l: Math.round(r.left), t: Math.round(r.top + window.scrollY), w: Math.round(r.width), h: Math.round(r.height), align: cs.textAlign, bg: cs.backgroundColor, display: cs.display, cols: cs.gridTemplateColumns };
    });
  }
  return res;
}
"""

TARGETS = {
    'desktop-partnership.html': ['main.dv-card', 'main.dv-card > div', '.wf-h', '.img-slot', 'details.wf-tier-card', 'details.wf-opp-card'],
    'desktop-contact.html': ['section.form-section', 'section.form-section .form', 'section.form-section .field', 'section.form-section .submit', '.routes', '.contact-stack'],
    'contact.html': ['section.form-section', 'section.form-section .form', 'section.form-section .submit'],
    'desktop-plan-visit.html': ['.venue-grid', '.venue-row', '.travel-panel.active', '.map'],
    'desktop-rice-masterchef.html': ['.master-hero', '.passes', '.master-pass', '.master-apply', '.master-form'],
}

try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        for f, sels in TARGETS.items():
            if not os.path.exists(f):
                continue
            width = 1440 if f.startswith('desktop-') else 430
            pg = b.new_page(viewport={'width': width, 'height': 900})
            pg.goto('http://127.0.0.1:8000/%s' % f, wait_until='domcontentloaded', timeout=60000)
            pg.wait_for_timeout(2200)
            pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
            pg.wait_for_timeout(400)
            res = pg.evaluate(JS, sels)
            out.append('==== %s (%spx) ====' % (f, width))
            for s in sels:
                items = res.get(s, [])
                out.append('%s  (%d found)' % (s, len(items)))
                for it in items[:6]:
                    out.append('   l=%s t=%s w=%s h=%s align=%s bg=%s display=%s cols=%s' % (it['l'], it['t'], it['w'], it['h'], it['align'], it['bg'], it['display'], (it['cols'] or '')[:60]))
            out.append('')
            pg.close()
        b.close()
except Exception:
    out.append(traceback.format_exc())

os.makedirs('_inspect', exist_ok=True)
open('_inspect/layout-check.txt', 'w', encoding='utf-8').write('\n'.join(out))
