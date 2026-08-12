from pathlib import Path

BASE = '<script src="assets/birc-layout-editor.js" defer></script>'
UPGRADE = '<script src="assets/birc-layout-editor-upgrade.js" defer></script>'
pages = [p for p in Path('.').glob('desktop*.html') if p.is_file()]
for page in pages:
    html = page.read_text()
    if BASE not in html:
        html = html.replace('</body>', BASE + '</body>', 1)
    if UPGRADE not in html:
        html = html.replace('</body>', UPGRADE + '</body>', 1)
    page.write_text(html)

context = Path('context.md')
text = context.read_text()
old = 'It previews direct drag, resize, spacing, text, duplicate, hide, delete, and section reorder changes immediately and stores drafts in browser `localStorage`.'
new = 'It previews direct drag, resize, spacing, text, duplicate, hide, delete, and section reorder changes immediately and stores drafts in browser `localStorage`. The panel is draggable and resizable, Minimize always leaves the Edit layout launcher available, and an 8px baseline with selectable 8/12/16-column overlays supports precise alignment.'
if old in text:
    text = text.replace(old, new, 1)
context.write_text(text)
print(f'Installed editor upgrade on {len(pages)} desktop pages')
