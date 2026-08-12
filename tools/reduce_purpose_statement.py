from pathlib import Path
p=Path('desktop.html')
h=p.read_text()
old='.purpose .purpose-statement{max-width:24ch;font-size:clamp(46px,3.75vw,65px);line-height:1.12}\n.purpose .purpose-statement span{display:block}\n@media(max-width:1280px){.purpose .purpose-statement{font-size:46px;max-width:22ch}}'
new='.purpose .purpose-statement{max-width:26ch;font-size:clamp(40px,3.2vw,56px);line-height:1.14}\n.purpose .purpose-statement span{display:block}\n@media(max-width:1280px){.purpose .purpose-statement{font-size:40px;max-width:24ch}}'
assert old in h
p.write_text(h.replace(old,new,1))

p=Path('context.md');text=p.read_text()
text=text.replace('The Purpose statement keeps the increased 46-65px scale and is deliberately composed as three lines on wide desktop so it stays inside the frame.','The Purpose statement uses a restrained 40-56px scale and is deliberately composed as three lines on wide desktop so it stays inside the frame.',1)
p.write_text(text)
