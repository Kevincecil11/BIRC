from pathlib import Path
import re

p=Path('desktop.html')
h=p.read_text()
if 'desktop-gallery-section' not in h:
    h,n=re.subn(r'<section class="section-tight">(\s*<div class="shell">\s*<header class="sechead")',r'<section class="section-tight desktop-gallery-section">\1',h,count=1)
    if n!=1: raise SystemExit('desktop gallery section not found')
css='''
/* desktop-only floating action collision fix */
.side-actions{right:14px;bottom:14px;gap:7px}
.side-action{width:158px;height:46px;padding:0 13px;gap:9px;font-size:8.5px;box-shadow:0 9px 24px #0007}
.side-action svg{width:18px;height:18px}.side-action.whatsapp svg{width:20px;height:20px}
/* BIRC in pictures as a full-page desktop chapter */
.desktop-gallery-section{min-height:100vh;padding:112px 0 96px;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.desktop-gallery-section .sechead{margin-bottom:48px!important}
.desktop-gallery-section .gallery{margin-top:0;overflow:visible}
.desktop-gallery-section .gallery-run{gap:10px;align-items:stretch}
.desktop-gallery-section .tile,.desktop-gallery-section .tile:nth-child(even){width:min(72vw,1120px);height:min(68vh,720px);flex:none}
.desktop-gallery-section .tile:after{left:22px;bottom:20px;font-size:11px}
@media(max-width:1400px){.side-actions{right:10px;bottom:10px}.side-action{width:148px;height:44px}.desktop-gallery-section .tile,.desktop-gallery-section .tile:nth-child(even){width:78vw;height:66vh}}
'''
if 'desktop-only floating action collision fix' not in h:
    h=h.replace('</style>',css+'</style>',1)
p.write_text(h)

p=Path('context.md')
text=p.read_text()
text=text.replace('Book your stand and the green WhatsApp action with its official mark are stacked at the bottom-right.','compact Book your stand and green WhatsApp actions are stacked at the bottom-right to minimize content overlap.')
if 'Desktop `BIRC in pictures` is a full-viewport chapter' not in text:
    marker='- Final CTA uses `assets/rice-world-map.png` full-bleed with a dark readability overlay.'
    text=text.replace(marker,'- Desktop `BIRC in pictures` is a full-viewport chapter with large 72vw by 68vh image panels. Mobile retains its approved compact gallery treatment.\n'+marker)
# Remove accidental mobile notes if present.
text=text.replace('- Mobile homepage floating controls use a compact 46px toggle and 40px actions, raised above the sticky countdown bar with reserved right-side space so controls never overlap.\n','')
text=text.replace('- Mobile `BIRC in pictures` is a full-viewport chapter with near-canvas-width, tall image placeholders (62svh, capped at 620px) rather than a short strip.\n','')
p.write_text(text)
