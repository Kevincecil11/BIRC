from pathlib import Path
p=Path('desktop.html');h=p.read_text()
css='''
/* stage-aligned section headings */
.zones>.shell:first-child .sechead{grid-template-columns:320px minmax(0,1fr);gap:52px;margin-bottom:48px}
.zones>.shell:first-child .sechead>div{grid-column:2;padding-left:0}
.dates .datelead{grid-template-columns:320px minmax(0,1fr);gap:52px;align-items:start;margin-bottom:36px}
.dates .datelead .date-statement{grid-column:2;text-align:center;justify-self:stretch;max-width:none;margin:0;font-size:clamp(36px,3vw,48px);line-height:1.08}
.dates .datelead .eyebrow{grid-column:1;text-align:left}
.dates .datelock{margin-left:372px;width:calc(100% - 372px);padding-top:56px}
@media(max-width:1400px){.zones>.shell:first-child .sechead,.dates .datelead{grid-template-columns:320px minmax(0,1fr);gap:48px}.dates .datelock{margin-left:368px;width:calc(100% - 368px)}}
@media(max-width:1180px){.zones>.shell:first-child .sechead,.dates .datelead{grid-template-columns:280px minmax(0,1fr);gap:48px}.dates .datelock{margin-left:328px;width:calc(100% - 328px)}.dates .datelead .date-statement{font-size:34px}}
'''
h=h.replace('</style>',css+'</style>',1)
p.write_text(h)

p=Path('context.md');text=p.read_text()
old='Desktop Experience Zones heading aligns with the left edge of the visual stage, the three-day statement is set as three separate lines, and Voices uses an automatic four-quote rotation with a right-aligned portrait placeholder, name, and designation.'
new='Desktop Experience Zones heading sits directly above and aligns with the large visual stage. The three-day statement sits directly above the October/date composition in the same right-hand column and remains three separate lines. Voices uses an automatic four-quote rotation with a right-aligned portrait placeholder, name, and designation.'
assert old in text
p.write_text(text.replace(old,new,1))
