from pathlib import Path
p=Path('desktop.html')
h=p.read_text()
old='<p class="reveal purpose-statement">India at the centre.<br>Every rice market in the room.<br>One place where the industry decides what comes next.</p>'
new='<p class="reveal purpose-statement"><span>India at the centre. Every rice</span><span>market in the room. One place where</span><span>the industry decides what comes next.</span></p>'
assert old in h
h=h.replace(old,new,1)
old_css='.purpose .purpose-statement{width:100%;max-width:none;font-size:clamp(36px,2.85vw,50px);line-height:1.16;white-space:nowrap}\n@media(max-width:1280px){.purpose .purpose-statement{font-size:36px;white-space:nowrap}}'
new_css='''.purpose.section{padding:112px 0 104px}.purpose .shell{grid-template-columns:240px minmax(0,1fr);gap:88px;align-items:start}.purpose .eyebrow{padding-top:12px}.purpose .purpose-statement{width:100%;max-width:23ch;font:500 clamp(52px,4vw,66px)/1.03 Poppins,sans-serif;letter-spacing:-.052em}.purpose .purpose-statement span{display:block;white-space:nowrap}.purpose footer{margin-top:44px;padding-top:20px}@media(max-width:1400px){.purpose .shell{grid-template-columns:190px minmax(0,1fr);gap:56px}.purpose .purpose-statement{font-size:clamp(46px,3.8vw,56px)}}@media(max-width:1180px){.purpose.section{padding:96px 0}.purpose .shell{grid-template-columns:160px minmax(0,1fr);gap:40px}.purpose .purpose-statement{font-size:42px;max-width:none}}'''
assert old_css in h
h=h.replace(old_css,new_css,1)
p.write_text(h)

p=Path('context.md');text=p.read_text()
text=text.replace('The Purpose statement uses a restrained 36-50px scale and explicit line breaks to guarantee exactly three lines on desktop.','The Purpose section uses a compact editorial rhythm with balanced 3-line copy, 52-66px on wide desktop, reduced section padding, and aligned label/content columns.',1)
p.write_text(text)
