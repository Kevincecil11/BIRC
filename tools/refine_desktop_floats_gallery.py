from pathlib import Path

p=Path('desktop.html')
h=p.read_text()
old='<section class="section-tight">\n    <div class="shell">\n      <header class="sechead" style="margin-bottom:0">\n        <span class="eyebrow">Impressions</span>'
new='<section class="section-tight desktop-gallery-section">\n    <div class="shell">\n      <header class="sechead desktop-gallery-head" style="margin-bottom:0">\n        <span class="eyebrow">Impressions</span>'
assert old in h
h=h.replace(old,new,1)
css='''
/* desktop-only floating action collision fix */
.side-actions{right:14px;bottom:14px;gap:7px}
.side-action{width:158px;height:46px;padding:0 13px;gap:9px;font-size:8.5px;box-shadow:0 9px 24px #0007}
.side-action svg{width:18px;height:18px}.side-action.whatsapp svg{width:20px;height:20px}
/* BIRC in pictures as a full-page desktop chapter */
.desktop-gallery-section{min-height:100vh;padding:112px 0 96px;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.desktop-gallery-head{margin-bottom:48px!important}
.desktop-gallery-section .gallery{margin-top:0;overflow:visible}
.desktop-gallery-section .gallery-run{gap:10px;align-items:stretch}
.desktop-gallery-section .tile,.desktop-gallery-section .tile:nth-child(even){width:min(72vw,1120px);height:min(68vh,720px);flex:none}
.desktop-gallery-section .tile:after{left:22px;bottom:20px;font-size:11px}
@media(max-width:1400px){.side-actions{right:10px;bottom:10px}.side-action{width:148px;height:44px}.desktop-gallery-section .tile,.desktop-gallery-section .tile:nth-child(even){width:78vw;height:66vh}}
'''
h=h.replace('</style>',css+'</style>',1)
p.write_text(h)

p=Path('context.md')
text=p.read_text()
needle='- Desktop homepage controls: countdown lives in the masthead; Book your stand and the green WhatsApp action with its official mark are stacked at the bottom-right.'
replacement='- Desktop homepage controls: countdown lives in the masthead; compact Book your stand and green WhatsApp actions are stacked at the bottom-right at 158 x 46px to minimize content overlap.'
assert needle in text
text=text.replace(needle,replacement,1)
old='- Gallery placeholders are intentionally 20% larger than the original gallery. Preserve.'
new='- Desktop `BIRC in pictures` is a full-viewport chapter with large 72vw by 68vh image panels. Mobile retains its previously approved compact gallery treatment.'
if old in text:text=text.replace(old,new,1)
else:
    # Replace the accidental mobile-only notes if they survived the restore source.
    text=text.replace('- Mobile homepage floating controls use a compact 46px toggle and 40px actions, raised above the sticky countdown bar with reserved right-side space so controls never overlap.\n- Mobile `BIRC in pictures` is a full-viewport chapter with near-canvas-width, tall image placeholders (62svh, capped at 620px) rather than a short strip.',new,1)
p.write_text(text)
