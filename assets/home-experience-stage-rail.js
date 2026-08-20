(function(){
'use strict';
var section=document.getElementById('zones');
if(!section||section.dataset.stageRail==='1')return;
var fallback=[
['The Rice Archive','Living archive','200+ varieties. One living archive.','https://ik.imagekit.io/18ab23oqaj/zone3.png'],
['Hands of Rice','Sculptural hands','From seed to serving hands.','https://ik.imagekit.io/18ab23oqaj/zone6.png'],
['How the World Eats Rice','Forty metre table','Forty metres of tables.','https://ik.imagekit.io/18ab23oqaj/zone5.png'],
['Beyond the Bowl','Window installation','A window you cannot pass.','https://ik.imagekit.io/18ab23oqaj/zone9.png'],
['The World Within','Macro grain projection','A grain becomes a universe.','https://ik.imagekit.io/18ab23oqaj/zone7.png'],
['Rice Mirror','Mirror installation','The grains know your face.','https://ik.imagekit.io/18ab23oqaj/zone8.png'],
['The Rice Route Map','Illuminated export route map','From Indian fields to the world’s plates.','https://ik.imagekit.io/18ab23oqaj/zone1.png'],
['Rice Through Time','Timeline corridor','Ancient grain, future harvest.','https://ik.imagekit.io/18ab23oqaj/zone4.png'],
['Seed Cloud','Suspended capsules','A cloud of capsules. A network of intelligence.','https://ik.imagekit.io/18ab23oqaj/zone2.png']
];
var zones=fallback.map(function(z){return {title:z[0],label:z[1],copy:z[2],image:z[3],href:'desktop-experience.html'}});
section.dataset.stageRail='1';section.className='home-xc';
section.innerHTML='<div class="shell"><header class="home-xc-head"><span class="eyebrow">Inside the summit</span><h2>9 Zones.<br>Endless possibilities.</h2><p>Nine immersive worlds tracing rice from field to future, designed to be walked, touched, and remembered.</p></header><div class="home-xc-stage"><div class="home-xc-rail" role="tablist" aria-label="Experience Zones"></div><article class="home-xc-view" role="tabpanel"><img class="home-xc-image" alt=""><div class="home-xc-meta"><span></span><span></span></div><div class="home-xc-copy"><h3></h3><p></p><a class="home-xc-link" href="desktop-experience.html">Explore this zone <span aria-hidden="true">↗</span></a></div><div class="home-xc-progress" aria-hidden="true"><i></i></div></article></div></div>';
var rail=section.querySelector('.home-xc-rail'),view=section.querySelector('.home-xc-view'),image=view.querySelector('.home-xc-image'),meta=view.querySelector('.home-xc-meta'),title=view.querySelector('h3'),copy=view.querySelector('p'),link=view.querySelector('.home-xc-link'),progress=view.querySelector('.home-xc-progress i'),index=-1;
zones.forEach(function(zone,i){var button=document.createElement('button');button.type='button';button.className='home-xc-tab';button.setAttribute('role','tab');button.setAttribute('aria-selected','false');button.innerHTML='<span>'+String(i+1).padStart(2,'0')+'</span><strong>'+zone.title+'</strong><i aria-hidden="true"></i>';button.addEventListener('click',function(){select(i)});rail.appendChild(button)});
function render(i){var z=zones[i];rail.querySelectorAll('.home-xc-tab').forEach(function(b,n){b.setAttribute('aria-selected',String(n===i))});meta.children[0].textContent=String(i+1).padStart(2,'0')+' / 09';meta.children[1].textContent=z.label;title.textContent=z.title;copy.textContent=z.copy;link.href=z.href;image.src=z.image;image.alt=z.title+' Experience Zone';progress.style.width=((i+1)/zones.length*100)+'%'}
function select(i){if(i===index)return;index=i;view.classList.add('is-changing');setTimeout(function(){render(index);view.classList.remove('is-changing')},180)}
render(0);index=0;
})();
