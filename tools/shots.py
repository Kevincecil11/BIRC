import os, traceback
from playwright.sync_api import sync_playwright
from PIL import Image

PAGES = [
    'desktop-creators.html',
    'desktop-rice-masterchef.html',
    'desktop-artists.html',
    'desktop-partnership.html',
    'desktop-plan-visit.html',
    'desktop-contact.html',
]

os.makedirs('_shots', exist_ok=True)
log = []

try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1440, 'height': 900})
        for f in PAGES:
            if not os.path.exists(f):
                log.append('missing %s' % f)
                continue
            pg.goto('http://127.0.0.1:8000/%s' % f, wait_until='load')
            pg.wait_for_timeout(2500)
            pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            pg.wait_for_timeout(1500)
            pg.evaluate("window.scrollTo(0, 0)")
            pg.wait_for_timeout(800)
            tmp = '/tmp/%s.png' % f.replace('.html', '')
            pg.screenshot(path=tmp, full_page=True)
            im = Image.open(tmp).convert('RGB')
            w, h = im.size
            scale = 820.0 / w
            im = im.resize((820, int(h * scale)))
            maxh = 5600
            if im.size[1] > maxh:
                im = im.crop((0, 0, 820, maxh))
            out = '_shots/%s.jpg' % f.replace('.html', '')
            im.save(out, 'JPEG', quality=62, optimize=True)
            log.append('%s -> %s %s' % (f, out, im.size))
        b.close()
except Exception:
    log.append(traceback.format_exc())

open('_shots/log.txt', 'w', encoding='utf-8').write('\n'.join(log))
