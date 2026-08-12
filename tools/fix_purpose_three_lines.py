from pathlib import Path

p=Path('desktop.html')
h=p.read_text()
old='<p class="reveal purpose-statement"><span>India at the centre. Every rice market in the room.</span><span>One place where the industry decides what comes next.</span></p>'
new='<p class="reveal purpose-statement"><span>India at the centre.</span><span>Every rice market in the room.</span><span>One place where the industry decides what comes next.</span></p>'
assert old in h
h=h.replace(old,new,1)
old_css='.purpose .purpose-statement{max-width:none;font-size:clamp(46px,3.75vw,65px);line-height:1.12}\n.purpose .purpose-statement span{display:block;white-space:nowrap}\n@media(max-width:1280px){.purpose .purpose-statement{font-size:46px}.purpose .purpose-statement span{white-space:normal}}'
new_css='.purpose .purpose-statement{max-width:24ch;font-size:clamp(46px,3.75vw,65px);line-height:1.12}\n.purpose .purpose-statement span{display:block}\n@media(max-width:1280px){.purpose .purpose-statement{font-size:46px;max-width:22ch}}'
assert old_css in h
h=h.replace(old_css,new_css,1)
p.write_text(h)

p=Path('context.md')
text=p.read_text()
text=text.replace('The Purpose statement is deliberately composed as two lines on wide desktop.','The Purpose statement keeps the increased 46-65px scale and is deliberately composed as three lines on wide desktop so it stays inside the frame.',1)
p.write_text(text)
