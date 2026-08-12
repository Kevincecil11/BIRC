from pathlib import Path
import re

SEARCH_DIALOG = '''<dialog class="site-search" id="siteSearch" aria-labelledby="siteSearchTitle"><div class="search-head"><span class="search-kicker">BIRC 2026</span><h2 id="siteSearchTitle">Search the summit</h2><button class="search-close" type="button" data-search-close aria-label="Close search">×</button></div><form class="search-form" id="siteSearchForm" role="search"><label class="sr-only" for="siteSearchInput">Search BIRC 2026</label><input id="siteSearchInput" type="search" autocomplete="off" placeholder="Speakers, schedule, exhibitors, venue..."><button type="submit"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/></svg><span>Search</span></button></form><div class="search-status" id="siteSearchStatus">Popular searches</div><div class="search-results" id="siteSearchResults" aria-live="polite"></div><div class="search-popular" id="siteSearchPopular"><button type="button" data-query="Speakers">Speakers</button><button type="button" data-query="Schedule">Schedule</button><button type="button" data-query="Exhibitors">Exhibitors</button><button type="button" data-query="Registration">Registration</button><button type="button" data-query="Venue">Venue</button></div></dialog>'''

SEARCH_CSS = r'''
.sr-only{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}
.site-search{width:min(760px,calc(100% - 48px));max-height:min(760px,calc(100vh - 64px));padding:0;border:1px solid var(--dl);background:var(--linen);color:var(--ink);box-shadow:0 34px 100px #000b;overflow:auto}
.site-search::backdrop{background:#0d0d0be6}
.search-head{position:relative;padding:34px 38px 22px;border-top:3px solid var(--gold);border-bottom:1px solid var(--ll)}
.search-kicker{display:block;color:var(--gold-deep);font:600 9px Poppins,sans-serif;letter-spacing:.18em;text-transform:uppercase}
.search-head h2{margin-top:10px;font:600 32px/1 Poppins,sans-serif;letter-spacing:-.045em}
.search-close{position:absolute;right:22px;top:22px;width:44px;height:44px;border:1px solid var(--ll);background:transparent;color:var(--ink);font-size:23px;cursor:pointer}
.search-form{margin:28px 38px 0;display:grid;grid-template-columns:1fr auto;border:1px solid var(--ll);background:#fffaf2}
.search-form input{min-width:0;height:58px;padding:0 18px;border:0;background:transparent;color:var(--ink);font:400 16px Inter,sans-serif;outline:0}
.search-form button{min-width:146px;border:0;background:var(--gold);color:var(--ink);display:flex;align-items:center;justify-content:center;gap:10px;font:600 11px Poppins,sans-serif;letter-spacing:.1em;text-transform:uppercase;cursor:pointer}
.search-form svg{width:17px;height:17px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round}
.search-form:focus-within{outline:3px solid var(--gold-deep);outline-offset:2px}
.search-status{margin:24px 38px 0;color:var(--lm);font:600 9px Poppins,sans-serif;letter-spacing:.15em;text-transform:uppercase}
.search-results{margin:10px 38px 0;border-top:1px solid var(--ll)}
.search-result{display:grid;grid-template-columns:110px minmax(0,1fr) 24px;gap:18px;align-items:center;padding:16px 8px;border-bottom:1px solid var(--ll);transition:background .15s var(--e)}
.search-result:hover,.search-result:focus-visible{background:var(--linen-2)}
.search-result small{color:var(--gold-deep);font:600 8px Poppins,sans-serif;letter-spacing:.13em;text-transform:uppercase}
.search-result strong{display:block;font:600 15px Poppins,sans-serif}
.search-result p{margin-top:3px;color:var(--lm);font:400 12px/1.45 Inter,sans-serif}
.search-result>span{color:var(--gold-deep);font-size:18px}
.search-empty{padding:22px 8px;color:var(--lm);font-size:14px;border-bottom:1px solid var(--ll)}
.search-popular{padding:12px 38px 34px;display:flex;flex-wrap:wrap;gap:8px}
.search-popular button{min-height:40px;padding:0 14px;border:1px solid var(--ll);background:transparent;color:var(--lm);font:500 11px Poppins,sans-serif;cursor:pointer}
.search-popular button:hover{border-color:var(--gold-deep);color:var(--ink)}
body.search-open{overflow:hidden}
@media(max-width:640px){
 .site-search{width:calc(100% - 24px);max-height:calc(100svh - 24px)}
 .search-head{padding:26px 20px 18px}.search-head h2{font-size:25px}.search-close{right:12px;top:12px;width:40px;height:40px}
 .search-form{margin:20px 14px 0;grid-template-columns:minmax(0,1fr) 52px}.search-form input{height:54px;padding-inline:14px;font-size:15px}.search-form button{min-width:0}.search-form button span{display:none}
 .search-status{margin:20px 16px 0}.search-results{margin:8px 14px 0}.search-result{grid-template-columns:1fr 20px;gap:8px;padding:14px 6px}.search-result small{grid-column:1/-1}.search-result p{font-size:11px}.search-result>span{grid-column:2;grid-row:2}
 .search-popular{padding:10px 14px 24px;gap:6px}.search-popular button{min-height:38px;padding-inline:11px;font-size:10px}
}
'''

SEARCH_JS = r'''<script id="site-search-script">(function(){
var dialog=document.getElementById('siteSearch'),input=document.getElementById('siteSearchInput'),form=document.getElementById('siteSearchForm'),results=document.getElementById('siteSearchResults'),status=document.getElementById('siteSearchStatus'),popular=document.getElementById('siteSearchPopular');
if(!dialog||!input)return;
var desktop=document.body.classList.contains('desktop-search-context');
var prefix=desktop?'desktop-':'';
var items=[
 ['Programme','Schedule',prefix+'conference.html','Conference agenda, knowledge sessions and the three-day programme.','schedule agenda programme knowledge sessions workshops'],
 ['Conference','Speakers',prefix+'conference.html','Meet the speakers and industry leaders joining BIRC 2026.','speakers leaders conference'],
 ['Exhibition','Why exhibit',prefix+'exhibition.html','Why BIRC is built for exporters, millers, traders and technology providers.','exhibitors exhibition exporters millers traders'],
 ['Exhibition','Exhibitor profile',prefix+'exhibitor-profile.html','Explore exhibitor categories and participation profiles.','exhibitors profile categories'],
 ['Exhibition','Book exhibition space',prefix+'space-rental.html','Review stand formats and exhibition space options.','stand booth rental exhibitors registration'],
 ['Visit','Bharat Mandapam',prefix+'plan-visit.html#venue','Venue information for Halls 4 and 5, Pragati Maidan, New Delhi.','venue bharat mandapam halls gate new delhi'],
 ['Visit','Travel and hotels',prefix+'plan-visit.html#travel','Plan metro, airport, rail, road and hotel arrangements.','travel hotels metro airport railway'],
 ['Registration','Register for BIRC 2026',desktop?'register.html?type=visitor':'register.html?type=visitor','Choose visitor, exhibitor or buyer registration.','registration register visitor buyer exhibitor'],
 ['Experience','Experience Zones',prefix+'experience.html','Nine immersive worlds tracing rice from field to future.','experience zones rice route seed archive'],
 ['Partnership','Partnership opportunities',prefix+'partnership.html','Explore sponsorship tiers and special opportunities.','partnership sponsor sponsorship'],
 ['Influencers','Content Creators',prefix+'creators.html','Creator access, scoring, criteria and application details.','creators influencers content'],
 ['Influencers','Rice Masterchef',prefix+'rice-masterchef.html','Competition details, criteria and participation information.','masterchef chef competition'],
 ['Influencers','Artists',prefix+'artists.html','Artist programme, criteria and application details.','artists art programme'],
 ['About BIRC','About the summit',prefix+'about.html','Mission, story, values and industry overview.','about mission story organisers'],
 ['Support','Contact BIRC',prefix+'contact.html','Booking, visiting and general enquiry details.','contact booking email phone support']
];
function esc(s){return s.replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function render(q){q=q.trim().toLowerCase();results.innerHTML='';if(!q){status.textContent='Popular searches';popular.hidden=false;return}popular.hidden=false;var words=q.split(/\s+/);var found=items.map(function(x){var hay=x.join(' ').toLowerCase(),score=0;words.forEach(function(w){if(x[1].toLowerCase().includes(w))score+=4;if(x[0].toLowerCase().includes(w))score+=2;if(hay.includes(w))score+=1});return [score,x]}).filter(function(x){return x[0]>0}).sort(function(a,b){return b[0]-a[0]}).slice(0,7).map(function(x){return x[1]});status.textContent=found.length?found.length+' result'+(found.length===1?'':'s'):'No results';if(!found.length){results.innerHTML='<div class="search-empty">Try speakers, schedule, exhibitors, registration, or venue.</div>';return}results.innerHTML=found.map(function(x){return '<a class="search-result" href="'+esc(x[2])+'"><small>'+esc(x[0])+'</small><div><strong>'+esc(x[1])+'</strong><p>'+esc(x[3])+'</p></div><span aria-hidden="true">→</span></a>'}).join('')}
function openSearch(){if(typeof dialog.showModal==='function')dialog.showModal();else dialog.setAttribute('open','');document.body.classList.add('search-open');setTimeout(function(){input.focus()},80)}
function closeSearch(){if(dialog.open&&typeof dialog.close==='function')dialog.close();else dialog.removeAttribute('open');document.body.classList.remove('search-open')}
document.querySelectorAll('[data-search-open]').forEach(function(b){b.addEventListener('click',openSearch)});document.querySelectorAll('[data-search-close]').forEach(function(b){b.addEventListener('click',closeSearch)});form.addEventListener('submit',function(e){e.preventDefault();render(input.value)});input.addEventListener('input',function(){render(input.value)});popular.addEventListener('click',function(e){var b=e.target.closest('[data-query]');if(!b)return;input.value=b.dataset.query;render(input.value);input.focus()});dialog.addEventListener('close',function(){document.body.classList.remove('search-open')});dialog.addEventListener('click',function(e){var b=dialog.getBoundingClientRect();if(e.clientX<b.left||e.clientX>b.right||e.clientY<b.top||e.clientY>b.bottom)closeSearch()});document.addEventListener('keydown',function(e){if(e.key==='/'&&!/input|textarea/i.test(document.activeElement.tagName)){e.preventDefault();openSearch()}});render('');
})();</script>'''

# Desktop
p=Path('desktop.html'); h=p.read_text()
h=h.replace('<body>','<body class="desktop-search-context">',1)
h=h.replace('<button class="nav-search" type="button" aria-label="Search BIRC">','<button class="nav-search" type="button" aria-label="Search BIRC" data-search-open>',1)
assert h.count('</style>')==1
h=h.replace('</style>',SEARCH_CSS+'</style>',1)
h=h.replace('<dialog class="regdialog"',SEARCH_DIALOG+'<dialog class="regdialog"',1)
h=h.replace('</body>',SEARCH_JS+'</body>',1)
p.write_text(h)

# Mobile
p=Path('index.html'); h=p.read_text()
old='<header class="bar" id="bar"><a href="#top"><img class="logo" src="https://ik.imagekit.io/18ab23oqaj/BIRC%20Ivory%20logo%20dates.png" alt="BIRC"></a><button class="menu" id="openMenu" aria-label="Menu"><i></i><i></i></button></header>'
new='''<header class="bar" id="bar"><a href="#top"><img class="logo" src="https://ik.imagekit.io/18ab23oqaj/BIRC%20Ivory%20logo%20dates.png" alt="BIRC"></a><div class="mobile-head-tools"><button class="mobile-head-icon" type="button" data-search-open aria-label="Search BIRC"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/></svg></button><button class="mobile-head-icon" id="mobileDocsToggle" type="button" aria-label="Open BIRC documents" aria-expanded="false"><svg viewBox="0 0 24 24"><path d="M6 3h9l3 3v15H6zM15 3v4h4M9 11h6M9 15h6"/></svg></button><button class="menu" id="openMenu" aria-label="Menu"><i></i><i></i></button></div></header><aside class="mobile-docs" id="mobileDocs" aria-label="BIRC documents"><span>Documents</span><a href="https://api.birc.in/uploads/birc-1781162197449-632024568.pdf" target="_blank" rel="noopener">EY report <b>↗</b></a><a href="https://api.birc.in/uploads/birc-1784615646887-946540455.pdf" target="_blank" rel="noopener">Buyer facilitation <b>↗</b></a><a href="https://api.birc.in/uploads/birc-agenda-2026.pdf" target="_blank" rel="noopener">2026 agenda <b>↗</b></a></aside>'''
assert old in h
h=h.replace(old,new,1)
mobile_css=r'''
.mobile-head-tools{display:flex;align-items:center;gap:2px}.mobile-head-icon{width:38px;height:44px;padding:0;display:grid;place-items:center;border:0;background:transparent;color:var(--l)}.mobile-head-icon svg{width:17px;height:17px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}.bar .menu{width:40px}.bar .logo{width:136px;height:44px}.mobile-docs{position:fixed;z-index:79;top:72px;left:50%;width:min(calc(100% - 28px),492px);padding:10px 14px 14px;background:var(--j2);border:1px solid var(--dl);transform:translate(-50%,-10px);opacity:0;visibility:hidden;transition:opacity .2s var(--e),transform .25s var(--e),visibility .25s}.mobile-docs.open{opacity:1;visibility:visible;transform:translate(-50%,0)}.mobile-docs>span{display:block;padding:5px 2px 9px;color:var(--g);font:600 8px Poppins,sans-serif;letter-spacing:.16em;text-transform:uppercase}.mobile-docs a{min-height:44px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid var(--dl);font:600 11px Poppins,sans-serif;letter-spacing:.06em;text-transform:uppercase}.mobile-docs b{color:var(--g);font-weight:600}
'''
# Insert all CSS into final primary style before view-switch style.
marker='</style><style id="view-switch-style">'
assert marker in h
h=h.replace(marker,mobile_css+SEARCH_CSS+'</style><style id="view-switch-style">',1)
h=h.replace('<dialog class="registration-dialog"',SEARCH_DIALOG+'<dialog class="registration-dialog"',1)
mobile_js=r'''<script id="mobile-docs-script">(function(){var b=document.getElementById('mobileDocsToggle'),p=document.getElementById('mobileDocs');if(!b||!p)return;function set(o){p.classList.toggle('open',o);b.setAttribute('aria-expanded',String(o))}b.addEventListener('click',function(e){e.stopPropagation();set(!p.classList.contains('open'))});document.addEventListener('click',function(e){if(!e.target.closest('#mobileDocs')&&!e.target.closest('#mobileDocsToggle'))set(false)});document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false)});})();</script>'''
h=h.replace('</body>',mobile_js+SEARCH_JS+'</body>',1)
p.write_text(h)

# Context
p=Path('context.md'); text=p.read_text()
needle='- Mobile has one floating `+` dock revealing Book your stand, Register to visit, Login, WhatsApp. Login and WhatsApp URLs are still pending; do not invent them.'
replacement=needle+'\n- Desktop and mobile homepages share a native search dialog with live client-side results and popular queries. Desktop opens it from the navbar search control. Mobile adds Search and Documents icons beside the menu; Documents reveals the same EY report, Buyer facilitation, and 2026 agenda PDFs used on desktop.'
assert needle in text
p.write_text(text.replace(needle,replacement,1))
