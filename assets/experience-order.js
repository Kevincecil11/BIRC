(function(){
'use strict';
var zones=[
 {title:'The Rice Archive',kicker:'Living archive',copy:'200+ varieties. One living archive.',image:'https://ik.imagekit.io/18ab23oqaj/zone1-archive.png'},
 {title:'Hands of Rice',kicker:'Sculptural hands',copy:'From seed to serving hands.',image:'https://ik.imagekit.io/18ab23oqaj/zone2-hands.png'},
 {title:'How the World Eats Rice',kicker:'Forty metre table',copy:'Forty metres of tables.',image:'https://ik.imagekit.io/18ab23oqaj/zone3-what%20people%20eat.png'},
 {title:'Beyond the Bowl',kicker:'Window installation',copy:'A window you cannot pass.',image:'https://ik.imagekit.io/18ab23oqaj/zone4-beyond.png'},
 {title:'The World Within',kicker:'Macro grain projection',copy:'A grain becomes a universe.',image:'https://ik.imagekit.io/18ab23oqaj/zone5-within.png'},
 {title:'The Rice Route Map',kicker:'Illuminated export route map',copy:'From Indian fields to the world’s plates.',image:'https://ik.imagekit.io/18ab23oqaj/zone6-route.png'},
 {title:'Rice Through Time',kicker:'Timeline corridor',copy:'Ancient grain, future harvest.',image:'https://ik.imagekit.io/18ab23oqaj/zone7-time.png'},
 {title:'Rice Mirror',kicker:'Mirror installation',copy:'The grains know your face.',image:'https://ik.imagekit.io/18ab23oqaj/zone8-mirror.png'},
 {title:'Seed Cloud',kicker:'Suspended capsules',copy:'A cloud of capsules. A network of intelligence.',image:'https://ik.imagekit.io/18ab23oqaj/zone9-seedcloud.png'}
];
function titleOf(node){var h=node.querySelector('h2,h3');return (node.getAttribute('data-zone-card')||(h&&h.textContent)||'').trim()}
function decorate(node,z,index){
 var h=node.querySelector('h2,h3');if(h)h.textContent=z.title;
 var p=node.querySelector('.zone-copy p,.zone-card-copy p');if(p)p.textContent=z.copy;
 var k=node.querySelector('.zone-kicker,.zone-cap');if(k)k.textContent=z.kicker;
 var top=node.querySelector('.zone-card-top span:first-child,.zone-no');if(top)top.textContent=String(index+1).padStart(2,'0')+' / 09';
 var visual=node.querySelector('.visual,.zone-card-art,.zone-vis');if(visual){visual.innerHTML='<img class="canonical-zone-image" src="'+z.image+'" alt="'+z.title+' Experience Zone" loading="lazy" decoding="async">'}
}
function reorder(container,nodes){var map={};nodes.forEach(function(n){map[titleOf(n)]=n});zones.forEach(function(z,i){var n=map[z.title];if(!n)return;decorate(n,z,i);container.appendChild(n)})}
var atlas=document.querySelector('.zone-atlas-grid');if(atlas)reorder(atlas,Array.from(atlas.querySelectorAll(':scope > .zone-card')));
var mobileHome=document.querySelector('#tourTrack');if(mobileHome)reorder(mobileHome,Array.from(mobileHome.querySelectorAll(':scope > .zone')));
var mobileMain=document.querySelector('main.page');if(mobileMain&&!mobileHome){var list=Array.from(mobileMain.querySelectorAll(':scope > section.zone'));if(list.length){var marker=document.createComment('canonical-zone-order');mobileMain.insertBefore(marker,list[0]);var map={};list.forEach(function(n){map[titleOf(n)]=n});zones.forEach(function(z,i){var n=map[z.title];if(!n)return;decorate(n,z,i);mobileMain.insertBefore(n,marker)});marker.remove()}}
var desktopMain=document.querySelector('section.zones');if(desktopMain&&!atlas&&!mobileMain){var desktopList=Array.from(desktopMain.querySelectorAll(':scope > article.zone'));if(desktopList.length)reorder(desktopMain,desktopList)}
if(!document.getElementById('canonical-zone-image-style')){var style=document.createElement('style');style.id='canonical-zone-image-style';style.textContent='.canonical-zone-image{position:absolute!important;inset:0!important;width:100%!important;height:100%!important;object-fit:cover!important;object-position:center!important;display:block!important}.zone-card-art,.visual,.zone-vis{position:relative!important;overflow:hidden!important}';document.head.appendChild(style)}
})();
