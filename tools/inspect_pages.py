import os, re, traceback
os.makedirs('_inspect', exist_ok=True)


def run():
    from bs4 import BeautifulSoup

    def soup(p):
        return BeautifulSoup(open(p, encoding='utf-8').read(), 'html.parser')

    def outline(path, out):
        s = soup(path)
        lines = []

        def walk(node, depth):
            for ch in node.find_all(recursive=False):
                if ch.name in ('script', 'style'):
                    continue
                cls = '.'.join(ch.get('class') or [])
                idv = ch.get('id') or ''
                txt = ' '.join(ch.get_text(' ', strip=True).split())[:70]
                lines.append('%s<%s%s%s> %s' % ('  ' * depth, ch.name, ('#' + idv) if idv else '', ('.' + cls) if cls else '', txt))
                if depth < 4:
                    walk(ch, depth + 1)
        walk(s.body, 0)
        open(out, 'w', encoding='utf-8').write('\n'.join(lines))

    def content(path, out):
        s = soup(path)
        for t in s(['script', 'style']):
            t.decompose()
        lines = []
        for el in s.body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'li', 'a', 'button', 'label', 'option', 'td', 'th', 'summary']):
            if el.find(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'li']):
                continue
            txt = ' '.join(el.get_text(' ', strip=True).split())
            if not txt:
                continue
            lines.append('%s: %s' % (el.name.upper(), txt))
        dedup = []
        for l in lines:
            if not dedup or dedup[-1] != l:
                dedup.append(l)
        open(out, 'w', encoding='utf-8').write('\n'.join(dedup))

    def formmarkup(path, out):
        s = soup(path)
        chunks = []
        for f in s.find_all('form'):
            sec = f.find_parent('section') or f.parent
            chunks.append(str(sec)[:9000])
        open(out, 'w', encoding='utf-8').write('\n\n=====\n\n'.join(chunks) if chunks else 'NO FORM')

    def styleblock(path, out, keywords):
        raw = open(path, encoding='utf-8').read()
        keep = []
        for b in re.findall(r'<style[^>]*>(.*?)</style>', raw, re.S):
            for rule in re.findall(r'[^{}]+\{[^{}]*\}', b):
                if any(k in rule for k in keywords):
                    keep.append(' '.join(rule.split()))
        open(out, 'w', encoding='utf-8').write('\n'.join(keep))

    for f, o in {
        'desktop-creators.html': 'creators-desktop-outline.txt',
        'desktop-rice-masterchef.html': 'masterchef-desktop-outline.txt',
        'desktop-partnership.html': 'partnership-desktop-outline.txt',
        'desktop-plan-visit.html': 'planvisit-desktop-outline.txt',
        'desktop-contact.html': 'contact-desktop-outline.txt',
        'desktop-artists.html': 'artists-desktop-outline.txt',
    }.items():
        if os.path.exists(f):
            outline(f, '_inspect/' + o)

    for f, o in {
        'rice-masterchef.html': 'masterchef-content.txt',
        'partnership.html': 'partnership-content.txt',
        'plan-visit.html': 'planvisit-content.txt',
        'contact.html': 'contact-content.txt',
        'creators.html': 'creators-content.txt',
    }.items():
        if os.path.exists(f):
            content(f, '_inspect/' + o)

    formmarkup('desktop-creators.html', '_inspect/creators-form-markup.txt')
    formmarkup('desktop-artists.html', '_inspect/artists-form-markup.txt')
    styleblock('desktop-artists.html', '_inspect/artists-form-css.txt', ['input', 'label', 'textarea', 'select', 'form', 'field', 'submit'])
    styleblock('desktop-creators.html', '_inspect/creators-form-css.txt', ['input', 'label', 'textarea', 'select', 'form', 'field', 'submit'])

    sizes = []
    for f in sorted(os.listdir('.')):
        if f.endswith('.html'):
            sizes.append('%8d  %s' % (os.path.getsize(f), f))
    open('_inspect/sizes.txt', 'w', encoding='utf-8').write('\n'.join(sizes))


try:
    run()
    open('_inspect/error.txt', 'w').write('OK')
except Exception:
    open('_inspect/error.txt', 'w').write(traceback.format_exc())
