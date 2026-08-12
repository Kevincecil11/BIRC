from pathlib import Path
import re

p = Path('desktop.html')
h = p.read_text()

menu = '''<div class="desktop-menu-shade" id="desktopMenuShade"></div><aside class="desktop-menu" id="desktopMenu" aria-label="Site menu"><header class="desktop-menu-head"><img src="https://ik.imagekit.io/18ab23oqaj/BIRC%20Ivory%20logo%20dates.png" alt="BIRC"><button class="desktop-menu-close" id="desktopMenuClose" type="button" aria-label="Close site menu">×</button></header><div class="desktop-menu-grid"><nav class="menu-col"><a href="desktop.html">Home</a><a href="desktop-about.html">About</a><a href="desktop-conference.html">Conference</a><div class="menu-group"><span>Exhibition</span><div class="menu-sub"><a href="desktop-exhibition.html">Why exhibit <i>01</i></a><a href="desktop-exhibitor-profile.html">Exhibitor profile <i>02</i></a><a href="desktop-space-rental.html">Space rental <i>03</i></a></div></div><a href="desktop-experience.html">Experience</a><div class="menu-group"><span>Influencers</span><div class="menu-sub"><a href="desktop-creators.html">Content Creators <i>01</i></a><a href="desktop-rice-masterchef.html">Rice Masterchef <i>02</i></a><a href="desktop-artists.html">Artists <i>03</i></a></div></div><a href="desktop-partnership.html">Partnership</a><a href="desktop-plan-visit.html">Plan Visit</a><a href="desktop-contact.html">Contact</a></nav></div><footer class="desktop-menu-foot"><a href="index.html?view=mobile">Mobile view</a><a href="https://birc.in/login">Login</a></footer></aside>'''
h, n = re.subn(r'<div class="desktop-menu-shade".*?</aside>', menu, h, count=1, flags=re.S)
assert n == 1, 'desktop menu not found'

# Match document utility labels to Login/Register typography.
h, n = re.subn(
    r'(\.utility-link\{padding:0 14px;display:inline-flex;align-items:center;gap:9px;border-right:1px solid var\(--dl\);font:600 )9px( Poppins,sans-serif;letter-spacing:)\.08em',
    r'\g<1>11px\g<2>.1em',
    h,
    count=1,
)
assert n == 1, 'utility typography rule not found'

# Replace the drawer layout with a restrained single vertical stack.
drawer_css = '''
/* simple single-column desktop menu */
.desktop-menu{width:min(430px,38vw);padding:30px 36px 36px}
.desktop-menu-head{padding-bottom:24px}
.desktop-menu-head img{width:150px;height:48px}
.desktop-menu-grid{display:block;margin-top:18px}
.desktop-menu .menu-col{display:block}
.desktop-menu .menu-col>a,.desktop-menu .menu-group>span{min-height:48px;justify-content:flex-start;font:600 16px Poppins,sans-serif;letter-spacing:-.02em}
.desktop-menu .menu-group>span{color:var(--linen)}
.desktop-menu .menu-sub{padding:4px 0 12px 18px}
.desktop-menu .menu-sub a{padding:7px 0;font:500 12px Poppins,sans-serif}
.desktop-menu .menu-sub i{margin-left:auto}
.desktop-menu-foot{margin-top:24px;padding-top:20px}
'''
assert h.count('</style>') == 1
h = h.replace('</style>', drawer_css + '</style>', 1)
p.write_text(h)

c = Path('context.md')
text = c.read_text()
old = 'At narrower desktop widths the three document controls retain their icons while their labels collapse to keep the header breathable.'
new = 'The three document labels use the same 11px Poppins weight and tracking as Login and Register; at narrower desktop widths they retain their icons while their labels collapse to keep the header breathable.'
assert old in text
text = text.replace(old, new, 1)
old2 = 'The Mobile view control is removed from this homepage masthead.'
new2 = 'The sandwich drawer is a single, left-aligned vertical stack: primary links have no numbers, while submenu items retain their small sequence numbers. The Mobile view control is removed from this homepage masthead.'
assert old2 in text
text = text.replace(old2, new2, 1)
c.write_text(text)
