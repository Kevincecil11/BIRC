import os, re, traceback

log = []

MASTER2 = """
@media (min-width:900px){
main.page > section.masterchef{padding:0!important;margin:0!important;max-width:none!important;width:auto!important;background:transparent!important;border:0!important}
main.page > section.masterchef > section{padding-left:max(60px,calc((100% - 1320px)/2))!important;padding-right:max(60px,calc((100% - 1320px)/2))!important}
main.page .master-hero .title,main.page .master-hero h2{color:#faf0e6!important}
main.page .master-hero .lead{color:#aba49c!important}
main.page .master-hero .eye{color:#ebb341!important}
main.page .master-stat strong{color:#ebb341!important}
main.page .master-stat small{color:#aba49c!important}
main.page .master-apply .section-title{color:#0d0d0b!important}
main.page .master-apply .eye{color:#7a5405!important}
main.page .master-apply .form label{color:#4a453e!important}
main.page .master-apply .form input,main.page .master-apply .form select,main.page .master-apply .form textarea{background:#fffaf2!important;border:1px solid #d8cec3!important;color:#0d0d0b!important}
main.page .master-apply .form .submit{background:#0d0d0b!important;color:#faf0e6!important}
main.page .master-apply .doc-note{color:#4a453e!important}
}
"""


def inject(path, css, marker):
    raw = open(path, encoding='utf-8').read()
    tag = '<style id="%s">%s</style>' % (marker, css)
    if 'id="%s"' % marker in raw:
        raw = re.sub(r'<style id="%s">.*?</style>' % marker, lambda m: tag, raw, flags=re.S)
    else:
        raw = raw.replace('</head>', tag + '\n</head>', 1)
    open(path, 'w', encoding='utf-8').write(raw)
    log.append('injected %s into %s' % (marker, path))


try:
    if os.path.exists('desktop-rice-masterchef.html'):
        inject('desktop-rice-masterchef.html', MASTER2, 'dt-polish2')
except Exception:
    log.append(traceback.format_exc())

os.makedirs('_inspect', exist_ok=True)
open('_inspect/polish2-log.txt', 'w', encoding='utf-8').write('\n'.join(log))
