from pathlib import Path
import re

p=Path('desktop.html')
h=p.read_text()

# Raise the shared desktop eyebrow title size by exactly 20%: 11px to 13.2px.
h,n=re.subn(r'(\.eyebrow\{display:block;font:600 )11px(/1 Poppins,sans-serif;)',r'\g<1>13.2px\g<2>',h,count=1)
assert n==1, 'shared eyebrow rule not found'

# Keep the purpose statement as two deliberate editorial lines on desktop.
old='<p class="reveal">India at the centre. Every rice market in the room. One place where the industry decides what comes next.</p>'
new='<p class="reveal purpose-statement"><span>India at the centre. Every rice market in the room.</span><span>One place where the industry decides what comes next.</span></p>'
assert old in h
h=h.replace(old,new,1)

css='''
.purpose .purpose-statement{max-width:none;font-size:clamp(46px,3.75vw,65px);line-height:1.12}
.purpose .purpose-statement span{display:block;white-space:nowrap}
@media(max-width:1280px){.purpose .purpose-statement{font-size:46px}.purpose .purpose-statement span{white-space:normal}}
'''
h=h.replace('</style>',css+'</style>',1)
p.write_text(h)

p=Path('context.md')
text=p.read_text()
needle='### Left alignment is a standing rule'
addition='Desktop homepage eyebrow titles use 13.2px Poppins, a 20% increase from the previous 11px shared size. The Purpose statement is deliberately composed as two lines on wide desktop.\n\n'
assert needle in text
text=text.replace(needle,addition+needle,1)
p.write_text(text)
