from pathlib import Path
p=Path('desktop.html')
h=p.read_text()
css='''
/* unified editorial alignment */
:root{--editorial-rail:240px;--editorial-gap:88px}
.purpose .shell,.sechead,.datelead,.why-head{grid-template-columns:var(--editorial-rail) minmax(0,1fr);gap:var(--editorial-gap)}
.sechead .eyebrow,.datelead .eyebrow,.why-head .eyebrow{padding-top:12px}
.purpose footer{display:grid;grid-template-columns:160px 110px minmax(0,1fr);gap:20px;align-items:center;width:100%}
.purpose footer span{margin:0;text-align:left;white-space:nowrap}
@media(max-width:1400px){:root{--editorial-rail:190px;--editorial-gap:56px}.purpose footer{grid-template-columns:140px 90px minmax(0,1fr);gap:16px}}
@media(max-width:1180px){:root{--editorial-rail:160px;--editorial-gap:40px}.purpose footer{grid-template-columns:130px 80px minmax(0,1fr);gap:14px}}
'''
h=h.replace('</style>',css+'</style>',1)
p.write_text(h)

p=Path('context.md');text=p.read_text()
needle='### Left alignment is a standing rule\n\n'
addition='Desktop homepage section introductions share one editorial grid token: a 240px label rail and 88px content gap on wide screens, scaling to 190/56 and 160/40 at narrower desktop widths. Purpose metadata uses an explicit aligned three-column grid beneath the statement.\n\n'
assert needle in text
p.write_text(text.replace(needle,needle+addition,1))
