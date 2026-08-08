import os, re, traceback

LOG = []

ALIGN = """
@media (min-width:900px){
main.page section,main.page section > header,main.page .head,main.page .eye,main.page h1,main.page h2,main.page h3,main.page h4,main.page p,main.page ul,main.page li,main.page address{text-align:left!important}
main.page .section-title,main.page h1.title,main.page h2.title{max-width:26ch;margin-left:0;margin-right:0}
main.page p.lead{max-width:70ch;margin-left:0;margin-right:0}
main.page .head{margin-left:0;margin-right:0}
main.page .btn{margin-left:0}
}
"""

MASTER = """
@media (min-width:900px){
main.page > section.masterchef{max-width:none;width:auto;margin:0;padding:0;background:transparent;border:0}
.prize{display:flex;align-items:baseline;gap:20px;flex-wrap:wrap;border:1px solid #35332e;padding:26px 30px;margin:34px 0 0}
.prize small{font-family:Poppins,sans-serif;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#aba49c}
.prize strong{font-family:Poppins,sans-serif;font-size:46px;line-height:1;color:#ebb341}
.prize span{font-size:14px;color:#aba49c}
}
"""

ARTISTS = """
#apply.apply{background:#ebb341!important}
#apply .eye{color:#7a5405!important}
#apply > p{color:#2b2b27!important}
#apply .section-title{color:#0d0d0b!important}
#apply .form{background:#faf0e6!important;border:1px solid #d8cec3!important;padding:34px!important}
#apply .form label{color:#4a453e!important}
#apply .form input,#apply .form select,#apply .form textarea{background:#fffaf2!important;border:1px solid #d8cec3!important;color:#0d0d0b!important}
#apply .form input::placeholder,#apply .form textarea::placeholder{color:#8a837a!important}
#apply .form .submit{background:#0d0d0b!important;color:#faf0e6!important}
#apply .doc-note{color:#4a453e!important}
#apply .status{color:#2b2b27!important}
#apply .artist-faq .faq-item{border-color:#cfa64a!important}
#apply .artist-faq .faq-q{color:#0d0d0b!important}
#apply .artist-faq .faq-a,#apply .artist-faq .faq-a p{color:#2b2b27!important}
@media (min-width:900px){
#apply .form{max-width:940px;display:grid;grid-template-columns:1fr 1fr;gap:0 26px}
#apply .form .field:nth-child(8){grid-column:1/-1}
#apply .form > label,#apply .form .submit,#apply .form .doc-note,#apply .form .status{grid-column:1/-1}
#apply .form .submit{width:auto;justify-self:start;padding:18px 36px!important}
}
"""

PLANVISIT = """
@media (min-width:900px){
.venue-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:36px}
.venue-row{display:flex;align-items:baseline;justify-content:space-between;gap:28px;border:1px solid #35332e;padding:26px 30px;margin:0}
.venue-row strong{font-family:Poppins,sans-serif;font-size:36px;line-height:1;color:#ebb341}
.map{height:420px;margin-top:40px;border:1px solid #35332e}
.hotel-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:32px}
.hotel{display:flex;align-items:baseline;justify-content:space-between;gap:18px;border:1px solid #35332e;padding:24px 26px;margin:0}
.travel-tabs{display:flex;flex-wrap:wrap;gap:10px;margin-top:34px}
.travel-tab{padding:13px 22px;font-family:Poppins,sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase}
.travel-panel.active{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 36px;align-items:start;margin-top:34px}
.travel-panel.active > h3,.travel-panel.active > .group{grid-column:1/-1}
.travel-panel.active > .group{margin-top:22px}
.travel-panel .route{margin:0;border:1px solid #35332e;padding:22px 24px}
.travel-panel .tip{margin:0}
#faqs .faq{max-width:940px}
}
"""

CONTACT = """
section.form-section{background:#ebb341}
section.form-section .eye{color:#7a5405!important}
section.form-section .section-title{color:#0d0d0b!important}
section.form-section .lead,section.form-section > p{color:#2b2b27!important}
section.form-section .form{background:#faf0e6;border:1px solid #d8cec3;padding:28px;margin-top:30px}
section.form-section .field{margin-bottom:22px}
section.form-section .form label{display:block;font-family:Poppins,sans-serif;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#4a453e;margin-bottom:10px}
section.form-section .form input,section.form-section .form select,section.form-section .form textarea{width:100%;background:#fffaf2;border:1px solid #d8cec3;border-radius:0;padding:14px 15px;font-family:Inter,sans-serif;font-size:15px;color:#0d0d0b}
section.form-section .form textarea{min-height:150px;resize:vertical}
section.form-section .form input:focus,section.form-section .form select:focus,section.form-section .form textarea:focus{outline:2px solid #c98e25;outline-offset:2px;border-color:#c98e25}
section.form-section .form input::placeholder,section.form-section .form textarea::placeholder{color:#8a837a}
section.form-section .submit{width:100%;background:#0d0d0b;color:#faf0e6;border:0;border-radius:0;padding:18px;font-family:Poppins,sans-serif;font-size:13px;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;transition:background .2s cubic-bezier(.22,1,.36,1)}
section.form-section .submit:hover{background:#191916}
section.form-section .doc-note{font-size:12px;line-height:1.6;color:#4a453e;margin-top:16px}
section.form-section .status{margin-top:12px;font-size:13px;color:#2b2b27}
@media (min-width:900px){
section.form-section .form{max-width:900px;padding:44px;display:grid;grid-template-columns:1fr 1fr;gap:0 28px}
section.form-section .form .field:nth-child(5){grid-column:1/-1}
section.form-section .submit,section.form-section .doc-note,section.form-section .status{grid-column:1/-1}
section.form-section .submit{width:auto;justify-self:start;padding:18px 38px}
}
"""

PARTNERSHIP = """
@media (min-width:900px){
main.dv-card{max-width:none!important;width:100%!important;margin:0!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:76px 0 0!important;text-align:left!important}
main.dv-card > div{width:min(1320px,calc(100% - 112px));margin-left:auto;margin-right:auto;padding:70px 0;text-align:left!important}
main.dv-card .wf-h{font-family:Poppins,sans-serif;font-size:clamp(34px,3.2vw,50px);line-height:1.06;letter-spacing:-.01em;text-align:left!important;max-width:24ch}
main.dv-card p,main.dv-card > div > div{text-align:left!important}
.img-slot{height:440px;display:flex;align-items:flex-end}
.img-slot-cap{text-align:left!important}
main.dv-card > div:has(> details.wf-tier-card){display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px;align-items:start}
main.dv-card > div:has(> details.wf-tier-card) > div:first-child{grid-column:1/-1;margin-bottom:6px}
main.dv-card > div:has(> details.wf-tier-card) > details.wf-tier-card:nth-of-type(1){grid-column:1/-1}
main.dv-card details.wf-tier-card{margin:0}
main.dv-card details.wf-tier-card summary{padding:26px 28px}
main.dv-card div:has(> details.wf-opp-card){display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;align-items:start;margin-top:34px}
main.dv-card details.wf-opp-card{margin:0}
main.dv-card details[open].wf-tier-card,main.dv-card details[open].wf-opp-card{outline:1px solid #ebb341;outline-offset:-1px}
main.dv-card .wf-acc-body{padding:0 28px 28px}
main.dv-card .wf-marquee-track{margin-top:30px}
}
"""


def read(p):
    return open(p, encoding='utf-8').read()


def write(p, raw):
    open(p, 'w', encoding='utf-8').write(raw)


def inject(path, css, marker):
    raw = read(path)
    tag = '<style id="%s">%s</style>' % (marker, css)
    if 'id="%s"' % marker in raw:
        raw = re.sub(r'<style id="%s">.*?</style>' % marker, lambda m: tag, raw, flags=re.S)
    else:
        raw = raw.replace('</head>', tag + '\n</head>', 1)
    write(path, raw)
    LOG.append('injected %s into %s' % (marker, path))


def creators_layer():
    raw = read('desktop-creators.html')
    blocks = re.findall(r'<style[^>]*>(.*?)</style>', raw, re.S)
    return blocks[-1] if blocks else ''


ALIAS = {
    'master-hero': ['hero'],
    'master-stats': ['stats'],
    'master-stat': ['stat'],
    'moment': ['access', 'pad'],
    'moment-list': ['access-list'],
    'moment-row': ['access-row'],
    'winner': ['pad'],
    'winner-list': ['access-list'],
    'winner-row': ['access-row'],
    'master-score': ['score', 'pad'],
    'master-passes': ['passes'],
    'master-pass': ['pass'],
    'eligibility': ['criteria', 'pad'],
    'content-list': ['access-list'],
    'content-row': ['access-row'],
    'chef-process': ['process', 'pad'],
    'master-apply': ['apply', 'pad'],
    'master-form': ['form'],
}


def alias_masterchef():
    path = 'desktop-rice-masterchef.html'
    raw = read(path)

    def repl(m):
        toks = m.group(1).split()
        out = list(toks)
        for t in toks:
            for a in ALIAS.get(t, []):
                if a not in out:
                    out.append(a)
        if 'master-pass' in toks and 'vip' not in toks and 'day' not in out:
            out.append('day')
        return 'class="%s"' % ' '.join(out)

    raw = re.sub(r'class="([^"]*)"', repl, raw)
    write(path, raw)
    LOG.append('aliased masterchef classes')


NOTE = '<p class="doc-note">No login. No OTP. Your enquiry goes straight to the BIRC team and is routed to the right desk.</p>'


def contact_note(path):
    raw = read(path)
    if 'doc-note' in raw:
        LOG.append('note already present in %s' % path)
        return
    m = re.search(r'<div id="formStatus"', raw)
    if not m:
        LOG.append('formStatus not found in %s' % path)
        return
    raw = raw[:m.start()] + NOTE + raw[m.start():]
    write(path, raw)
    LOG.append('added form note to %s' % path)


def run():
    layer = creators_layer()

    if os.path.exists('desktop-rice-masterchef.html'):
        alias_masterchef()
        inject('desktop-rice-masterchef.html', layer, 'dt-creators-layer')
        inject('desktop-rice-masterchef.html', ALIGN + MASTER, 'dt-polish')

    if os.path.exists('desktop-artists.html'):
        inject('desktop-artists.html', ALIGN + ARTISTS, 'dt-polish')

    if os.path.exists('desktop-plan-visit.html'):
        inject('desktop-plan-visit.html', ALIGN + PLANVISIT, 'dt-polish')

    if os.path.exists('desktop-contact.html'):
        contact_note('desktop-contact.html')
        inject('desktop-contact.html', ALIGN + CONTACT, 'dt-polish')

    if os.path.exists('contact.html'):
        contact_note('contact.html')
        inject('contact.html', CONTACT, 'dt-polish')

    if os.path.exists('desktop-partnership.html'):
        inject('desktop-partnership.html', PARTNERSHIP, 'dt-polish')

    entry = '\n- 2026-08-08 desktop polish: Masterchef now runs on the Creators desktop system (class aliases + shared layer); Artists apply section and FAQ recoloured for the gold backdrop; Plan Visit venue/hotel/travel blocks gridded; Partnership unwrapped from the mobile card into a full-width desktop grid; Contact enquiry form rebuilt in the Creators form style on desktop-contact.html and mobile contact.html; all copy left-aligned on desktop.\n'
    if os.path.exists('context.md'):
        raw = read('context.md')
        if 'desktop polish' not in raw:
            open('context.md', 'a', encoding='utf-8').write(entry)
            LOG.append('context.md updated')


os.makedirs('_inspect', exist_ok=True)
try:
    run()
    open('_inspect/polish-log.txt', 'w', encoding='utf-8').write('OK\n' + '\n'.join(LOG))
except Exception:
    open('_inspect/polish-log.txt', 'w', encoding='utf-8').write('FAILED\n' + '\n'.join(LOG) + '\n' + traceback.format_exc())
