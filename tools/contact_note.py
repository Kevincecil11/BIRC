import re, os

NOTE = '<p class="doc-note">No login. No OTP. Your enquiry goes straight to the BIRC team and is routed to the right desk.</p>'
log = []

for path in ['contact.html', 'desktop-contact.html']:
    if not os.path.exists(path):
        continue
    raw = open(path, encoding='utf-8').read()
    if 'doc-note' in raw:
        log.append('%s already has note' % path)
        continue
    m = re.search(r'<div[^>]*id="formStatus"[^>]*>', raw)
    if not m:
        m = re.search(r'</button>\s*</form>', raw)
        if m:
            raw = raw[:m.start() + len('</button>')] + NOTE + raw[m.start() + len('</button>'):]
            open(path, 'w', encoding='utf-8').write(raw)
            log.append('%s note added before </form>' % path)
        else:
            log.append('%s no anchor found' % path)
        continue
    raw = raw[:m.start()] + NOTE + raw[m.start():]
    open(path, 'w', encoding='utf-8').write(raw)
    log.append('%s note added before status' % path)

os.makedirs('_inspect', exist_ok=True)
open('_inspect/contact-note-log.txt', 'w', encoding='utf-8').write('\n'.join(log))
