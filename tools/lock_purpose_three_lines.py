from pathlib import Path
p=Path('desktop.html')
h=p.read_text()
old='<p class="reveal purpose-statement"><span>India at the centre.</span><span>Every rice market in the room.</span><span>One place where the industry decides what comes next.</span></p>'
new='<p class="reveal purpose-statement">India at the centre.<br>Every rice market in the room.<br>One place where the industry decides what comes next.</p>'
assert old in h
h=h.replace(old,new,1)
old_css='.purpose .purpose-statement{max-width:26ch;font-size:clamp(40px,3.2vw,56px);line-height:1.14}\n.purpose .purpose-statement span{display:block}\n@media(max-width:1280px){.purpose .purpose-statement{font-size:40px;max-width:24ch}}'
new_css='.purpose .purpose-statement{width:100%;max-width:none;font-size:clamp(36px,2.85vw,50px);line-height:1.16;white-space:nowrap}\n@media(max-width:1280px){.purpose .purpose-statement{font-size:36px;white-space:nowrap}}'
assert old_css in h
h=h.replace(old_css,new_css,1)
p.write_text(h)

p=Path('context.md');text=p.read_text()
text=text.replace('The Purpose statement uses a restrained 40-56px scale and is deliberately composed as three lines on wide desktop so it stays inside the frame.','The Purpose statement uses a restrained 36-50px scale and explicit line breaks to guarantee exactly three lines on desktop.',1)
p.write_text(text)
