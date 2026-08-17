(function(){
'use strict';
var drawer=document.getElementById('drawer'),open=document.getElementById('openMenu'),close=document.getElementById('closeMenu'),docs=document.getElementById('mobileDocs');
if(!drawer||!open||!close)return;
function setMenu(on){drawer.classList.toggle('open',on);document.body.classList.toggle('lock',on);open.setAttribute('aria-expanded',String(on));drawer.setAttribute('aria-hidden',String(!on));if(on&&docs)docs.classList.remove('open')}
open.setAttribute('aria-expanded','false');drawer.setAttribute('aria-hidden','true');
open.onclick=function(e){e.preventDefault();e.stopPropagation();setMenu(true)};
close.onclick=function(e){e.preventDefault();setMenu(false)};
drawer.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});
window.addEventListener('pageshow',function(){setMenu(false)});
})();
