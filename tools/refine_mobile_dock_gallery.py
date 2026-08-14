from pathlib import Path

p=Path('index.html')
h=p.read_text()
old='<section class="dark pad" style="padding-left:0;padding-right:0"><header class="head" style="padding:0 var(--p)"><span class="eye">Impressions</span><h2 class="title">BIRC in pictures</h2></header>'
new='<section class="dark pad mobile-gallery-section"><header class="head mobile-gallery-head"><span class="eye">Impressions</span><h2 class="title">BIRC in pictures</h2></header>'
assert old in h
h=h.replace(old,new,1)
css='''
/* mobile-only dock collision fix */
.action-dock{right:max(12px,calc((100vw - 520px)/2 + 12px));bottom:82px;gap:6px}
.action-toggle{width:46px;height:46px;font-size:20px;box-shadow:0 8px 22px #0008}
.action-list{gap:6px}
.action-link{min-height:40px;padding:0 11px;gap:8px;font-size:8px;box-shadow:0 6px 18px #0006}
.action-link span{width:20px;height:20px;font-size:10px}
.sticky{padding-right:78px;min-height:66px}
.sticky .btn{min-width:104px;padding-inline:14px}
.view-switch{bottom:max(12px,env(safe-area-inset-bottom));min-height:38px;padding-inline:11px}
/* BIRC in pictures as a full-page mobile chapter */
.mobile-gallery-section{min-height:100svh;padding:92px 0 96px!important;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.mobile-gallery-head{padding:0 var(--p);margin-bottom:42px}
.mobile-gallery-section .gallery{margin-top:0;overflow:visible}
.mobile-gallery-section .gallery-run{gap:10px!important;align-items:stretch}
.mobile-gallery-section .gallery-img{width:calc(min(100vw,520px) - 44px)!important;height:clamp(460px,62svh,620px)!important;flex:none;border:1px solid var(--dl)}
.mobile-gallery-section .gallery-img:nth-child(even){width:calc(min(100vw,520px) - 44px)!important}
.mobile-gallery-section .gallery-img:after{left:18px;bottom:16px;font-size:9px;letter-spacing:.12em;text-transform:uppercase}
@media(max-width:360px){.sticky{padding-right:68px}.action-dock{right:10px}.action-toggle{width:44px;height:44px}.mobile-gallery-section .gallery-img{height:500px!important}}
@media(prefers-reduced-motion:reduce){.mobile-gallery-section .gallery-run{overflow-x:auto;width:auto;scroll-snap-type:x mandatory}.mobile-gallery-section .gallery-img{scroll-snap-align:center}}
'''
marker='</style><style id="view-switch-style">'
assert marker in h
h=h.replace(marker,css+'</style><style id="view-switch-style">',1)
p.write_text(h)

p=Path('context.md')
text=p.read_text()
old='- Gallery placeholders are intentionally 20% larger than the original gallery. Preserve.'
new='- Mobile homepage floating controls use a compact 46px toggle and 40px actions, raised above the sticky countdown bar with reserved right-side space so controls never overlap.\n- Mobile `BIRC in pictures` is a full-viewport chapter with near-canvas-width, tall image placeholders (62svh, capped at 620px) rather than a short strip.'
assert old in text
p.write_text(text.replace(old,new,1))
