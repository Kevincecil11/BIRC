from pathlib import Path

TAG = '<script src="assets/birc-layout-editor.js" defer></script>'
pages = [p for p in Path('.').glob('desktop*.html') if p.is_file()]
for page in pages:
    html = page.read_text()
    if TAG not in html:
        if '</body>' not in html:
            raise RuntimeError(f'{page}: missing </body>')
        page.write_text(html.replace('</body>', TAG + '</body>', 1))

context = Path('context.md')
text = context.read_text()
if '### Private desktop layout editor' not in text:
    marker = '### Left alignment is a standing rule'
    note = '''### Private desktop layout editor

All desktop pages load `assets/birc-layout-editor.js`. The editor stays dormant unless `?editor=1` is added to a desktop URL; activation is remembered only in that browser. It previews direct drag, resize, spacing, text, duplicate, hide, delete, and section reorder changes immediately and stores drafts in browser `localStorage`. It never commits to GitHub. `Export changes` downloads a page-specific JSON manifest for review and permanent implementation. Use `?editor=0` or Hide editor to disable it. Mobile files never load it.

'''
    if marker not in text:
        raise RuntimeError('context marker missing')
    context.write_text(text.replace(marker, note + marker, 1))

print(f'Installed editor on {len(pages)} desktop pages')
