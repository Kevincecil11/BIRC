from pathlib import Path
import re

for filename, target in [('desktop.html','desktop-media-coverage.html'),('index.html','media-coverage.html')]:
    p=Path(filename); h=p.read_text()
    h=h.replace('href="https://birc.in/#coverage" target="_blank" rel="noopener"','href="'+target+'"')
    h,n=re.subn(r'<div class="coverage-outlets">(.*?)</div>',lambda m:'<div class="coverage-outlets"><div class="coverage-track">'+m.group(1)+m.group(1)+'</div></div>',h,count=1,flags=re.S)
    assert n==1, filename+' coverage outlets not found'
    css='''.coverage-outlets{overflow:hidden!important}.coverage-track{display:flex;width:max-content;min-width:100%;animation:coverageMove 34s linear infinite}.coverage-track:hover{animation-play-state:paused}.coverage-track>a{flex:none}@keyframes coverageMove{to{transform:translateX(-50%)}}@media(prefers-reduced-motion:reduce){.coverage-track{animation:none;overflow-x:auto}}'''
    h=h.replace('</style>',css+'</style>',1)
    p.write_text(h)

p=Path('context.md'); text=p.read_text()
old='- The previous rotating facts ticker below the hero is replaced on desktop and mobile by a media coverage rail titled `Published across / 80`. It shows clickable publisher marks and ends with a `See the coverage` action; mobile uses horizontal scroll snapping.'
new='- The previous rotating facts ticker below the hero is replaced on desktop and mobile by a continuously moving media coverage rail titled `Published across / 80`. Every publisher mark is clickable, motion pauses on hover and respects reduced motion. `See the coverage` opens the dedicated local coverage page (`desktop-media-coverage.html` or `media-coverage.html`).'
assert old in text
text=text.replace(old,new,1)
text=text.replace('### Desktop pages (13)','### Desktop pages (14)',1)
text=text.replace('`desktop-contact.html`\n\n## 5.', '`desktop-contact.html`, `desktop-media-coverage.html`\n\n## 5.',1)
text=text.replace('### Mobile pages (12)','### Mobile pages (13)',1)
text=text.replace('`register.html`\n\nMobile canvas','`register.html`, `media-coverage.html`\n\nMobile canvas',1)
p.write_text(text)
