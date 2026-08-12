from pathlib import Path
import re

p = Path('desktop.html')
h = p.read_text()

floats = '''<aside class="side-actions" aria-label="Quick actions"><a class="side-action stand" href="desktop-space-rental.html"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V8l8-4 8 4v12M8 20v-7h8v7M4 9h16"/></svg><span>Book your stand</span></a><a class="side-action whatsapp" href="https://wa.me/" aria-label="Contact BIRC on WhatsApp"><svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16.04 3C8.85 3 3 8.72 3 15.76c0 2.48.74 4.9 2.13 6.95L3 29l6.49-2.08a13.25 13.25 0 0 0 6.54 1.71h.01C23.23 28.63 29 22.9 29 15.86 29 8.82 23.23 3 16.04 3Zm0 23.47h-.01a11.06 11.06 0 0 1-5.63-1.53l-.4-.23-3.85 1.23 1.26-3.72-.25-.39a10.51 10.51 0 0 1-1.75-5.79c0-5.96 4.77-10.82 10.64-10.82 5.87 0 10.64 4.86 10.64 10.82 0 5.96-4.78 10.43-10.65 10.43Zm5.83-7.82c-.32-.16-1.9-.92-2.2-1.02-.3-.1-.5-.16-.72.16-.21.31-.82 1.02-1 1.23-.19.21-.38.24-.7.08-.32-.16-1.35-.49-2.57-1.55a9.67 9.67 0 0 1-1.78-2.18c-.19-.31-.02-.48.14-.64.14-.14.32-.37.48-.55.16-.18.21-.31.32-.52.1-.21.05-.39-.03-.55-.08-.16-.72-1.7-.98-2.33-.26-.62-.53-.54-.72-.55h-.62c-.21 0-.56.08-.85.39-.3.31-1.12 1.08-1.12 2.63 0 1.55 1.15 3.05 1.31 3.26.16.21 2.27 3.4 5.49 4.76.77.33 1.37.52 1.84.67.77.24 1.47.21 2.03.13.62-.09 1.9-.76 2.17-1.5.27-.73.27-1.35.19-1.5-.08-.13-.3-.21-.62-.37Z"/></svg><span>WhatsApp</span></a></aside>'''
h, n = re.subn(r'<aside class="side-actions">.*?</aside>', floats, h, count=1, flags=re.S)
assert n == 1, 'side actions not found'

css = r'''
:root{--nav:88px}
.masthead{height:88px;background:#0d0d0bf8;border-bottom:1px solid var(--dl);backdrop-filter:none}
.masthead .shell{width:min(1760px,calc(100% - 48px));grid-template-columns:190px minmax(0,1fr) auto;gap:24px}
.brand{display:flex;align-items:center;min-width:0}
.brand img{width:170px;height:55px;object-fit:contain;object-position:left center}
.nav-utilities{min-width:0;justify-self:start;display:flex;align-items:center;border:1px solid var(--dl);background:var(--ink-3)}
.nav-search,.utility-link{height:44px;flex:none;border:0;background:transparent;color:var(--dm);transition:background .18s var(--e),color .18s var(--e)}
.nav-search{width:46px;display:grid;place-items:center;border-right:1px solid var(--dl);cursor:pointer}
.nav-search svg{width:17px;height:17px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round}
.utility-link{padding:0 14px;display:inline-flex;align-items:center;gap:9px;border-right:1px solid var(--dl);font:600 9px Poppins,sans-serif;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap}
.utility-link:last-child{border-right:0}
.utility-link:hover,.nav-search:hover{background:var(--grey);color:var(--linen)}
.utility-link svg{width:16px;height:16px;fill:none;stroke:var(--gold);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.tools{display:flex;align-items:center;gap:8px}
.nav-countdown{height:46px;min-width:158px;padding:6px 14px;display:flex;flex-direction:column;justify-content:center;border:1px solid var(--gold-deep);background:var(--ink-3)}
.nav-countdown small{color:var(--gold);font:600 8px Poppins,sans-serif;letter-spacing:.13em;text-transform:uppercase}
.nav-countdown strong{margin-top:2px;color:var(--linen);font:600 12px Poppins,sans-serif;font-variant-numeric:tabular-nums;letter-spacing:.02em}
.tools .ghost,.tools .solid,.menu-toggle{height:46px}
.tools .ghost{padding-inline:15px}
.tools .solid{padding-inline:18px}
.menu-toggle{order:99;width:46px;display:grid;place-content:center;gap:6px;border:1px solid var(--dl);background:var(--ink-3);color:var(--linen);cursor:pointer;transition:border-color .18s var(--e),background .18s var(--e)}
.menu-toggle:hover{border-color:var(--gold);background:var(--grey)}
.menu-toggle i{display:block;width:18px;height:1px;background:currentColor}
.float-time,.mobile-view-control{display:none!important}
.footer{padding-bottom:40px}
.side-actions{position:fixed;z-index:65;right:24px;bottom:24px;display:grid;gap:10px}
.side-action{width:190px;height:56px;padding:0 17px;display:flex;align-items:center;gap:12px;border:1px solid transparent;box-shadow:0 14px 34px #0008;font:600 10px Poppins,sans-serif;letter-spacing:.08em;text-transform:uppercase;transition:transform .18s var(--e),filter .18s var(--e),box-shadow .18s var(--e)}
.side-action:hover{transform:translateY(-2px);filter:brightness(1.04);box-shadow:0 18px 40px #0009}
.side-action svg{width:21px;height:21px;flex:none;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.side-action.stand{background:var(--gold);border-color:var(--gold);color:var(--ink)}
.side-action.whatsapp{background:#25d366;border-color:#25d366;color:#0d2b18}
.side-action.whatsapp svg{width:23px;height:23px;fill:currentColor;stroke:none}
.hero{padding-top:calc(var(--nav) + 48px);padding-bottom:56px;align-items:center}
.hero .shell{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:64px;align-items:stretch}
.hero-copy{min-height:620px;padding-right:24px;display:flex;flex-direction:column;justify-content:center}
.hero h1{font-size:clamp(62px,5vw,96px);max-width:11ch}
.hero .lede{max-width:52ch}
.scrollcue{margin-top:auto;padding-top:38px}
.dossier{width:100%;max-width:none;min-height:620px;align-self:stretch;display:grid;grid-template-rows:auto 1fr auto;background:#12120fe8}
.dossier-head{min-height:58px;padding:0 26px}
.spec{height:100%;grid-template-columns:160px minmax(0,1fr);grid-template-rows:repeat(5,1fr);gap:0;padding:0}
.spec dt,.spec dd{min-height:0;height:100%;display:flex;align-items:center;border-bottom:1px solid var(--dl)}
.spec dt{padding-left:26px}
.spec dd{justify-content:flex-end;padding-right:26px}
.countdown{min-height:96px}
.countdown div{display:grid;align-content:center;padding:16px 8px}
@media(max-width:1450px){
  .masthead .shell{width:calc(100% - 32px);grid-template-columns:184px minmax(0,1fr) auto;gap:16px}
  .utility-link{padding-inline:11px}
  .nav-countdown{min-width:144px;padding-inline:11px}
  .tools .ghost{display:none}
  .side-actions{right:18px;bottom:18px}
  .hero-copy,.dossier{min-height:570px}
}
@media(max-width:1260px){
  .nav-utilities{justify-self:end}
  .utility-link{width:44px;padding:0;justify-content:center}
  .utility-link span{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  .nav-countdown{min-width:136px}
  .tools .solid{padding-inline:14px}
}
'''
pattern = r'\n\.masthead\{height:78px.*?@media\(max-width:1450px\)\{.*?\}\}\n</style>'
h, n = re.subn(pattern, '\n' + css + '</style>', h, count=1, flags=re.S)
assert n == 1, 'final homepage CSS block not found'
p.write_text(h)

c = Path('context.md')
text = c.read_text()
text, n = re.subn(
    r'### Masthead\n\n.*?\n\n### Left alignment',
    '''### Masthead

Desktop homepage masthead is 88px high and uses the official logo at 170 x 55px, a 20% increase from the previous 142 x 46px treatment. The navigation is organized into three deliberate groups: the enlarged brand, a shared utility rail containing Search plus the EY report, Buyer facilitation, and 2026 agenda links, then the countdown, Login, Register, and sandwich menu at the extreme right. At narrower desktop widths the three document controls retain their icons while their labels collapse to keep the header breathable. The Mobile view control is removed from this homepage masthead. The previous full-width bottom action bar is removed; Book your stand and green WhatsApp actions are stacked at the bottom-right. Other desktop pages retain their current inline mastheads until navigation is intentionally synchronized.

### Left alignment''',
    text,
    count=1,
    flags=re.S,
)
assert n == 1, 'masthead context not found'
text = text.replace(
    '- Desktop homepage controls: countdown lives in the masthead; Book your stand and WhatsApp are stacked on the right edge. There is no full-width bottom bar and no desktop Mobile view control. Mobile controls remain unchanged.',
    '- Desktop homepage controls: countdown lives in the masthead; Book your stand and the green WhatsApp action with its official mark are stacked at the bottom-right. There is no full-width bottom bar and no desktop Mobile view control. Mobile controls remain unchanged.'
)
c.write_text(text)
