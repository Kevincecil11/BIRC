from pathlib import Path
p=Path('desktop.html');h=p.read_text()
css='''
/* final stage-heading positions */
.zones>.shell:first-child .sechead>div{padding-left:64px}
.dates .datelead{position:relative;display:block;margin-bottom:36px;text-align:center}
.dates .datelead .eyebrow{position:absolute;left:0;top:12px;text-align:left}
.dates .datelead .date-statement{display:inline-block;width:auto;max-width:none;margin:0 auto;text-align:center;font-size:clamp(36px,3vw,48px);line-height:1.08}
.dates .datelock{margin-left:0;width:100%;text-align:center}
@media(max-width:1400px){.zones>.shell:first-child .sechead>div{padding-left:64px}}
@media(max-width:1180px){.zones>.shell:first-child .sechead>div{padding-left:48px}.dates .datelead .date-statement{font-size:34px}}
'''
h=h.replace('</style>',css+'</style>',1)
p.write_text(h)

p=Path('context.md');text=p.read_text()
old='Desktop Experience Zones heading sits directly above and aligns with the large visual stage. The three-day statement sits directly above the October/date composition in the same right-hand column and remains three separate lines.'
new='Desktop Experience Zones heading sits directly above the large visual stage and aligns to the square’s inner content edge near its 01 marker. The complete three-day statement and October/date composition are centered across the page, while the `Three days` eyebrow remains on the left editorial rail.'
assert old in text
p.write_text(text.replace(old,new,1))
