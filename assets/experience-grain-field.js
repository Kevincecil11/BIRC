(function(){
var zones=[
['The Rice Route Map','Illuminated export route map','Rice begins in India’s fields, then travels across continents to kitchens, markets and communities around the world.','https://ik.imagekit.io/18ab23oqaj/zone1.png'],
['Seed Cloud','Suspended capsules','A suspended network of seed forms, carrying the intelligence and diversity held inside every variety.','https://ik.imagekit.io/18ab23oqaj/zone2.png'],
['The Rice Archive','Living archive','More than 200 varieties preserved by colour, form, origin and the generations of hands behind them.','https://ik.imagekit.io/18ab23oqaj/zone3.png'],
['Rice Through Time','Timeline corridor','Ten thousand years of cultivation, exchange, innovation and human memory, walked end to end.','https://ik.imagekit.io/18ab23oqaj/zone4.png'],
['How the World Eats Rice','Forty metre table','One continuous table shows how rice changes across countries while staying a shared human language.','https://ik.imagekit.io/18ab23oqaj/zone5.png'],
['Hands of Rice','Sculptural hands','A tribute to every hand that grows, carries, cooks and serves the grain.','https://ik.imagekit.io/18ab23oqaj/zone6.png'],
['The World Within','Macro grain projection','Macro projection opens a single grain into landscapes, structures and unseen systems.','https://ik.imagekit.io/18ab23oqaj/zone7.png'],
['Rice Mirror','Mirror installation','Thousands of floating grains rebuild your silhouette, making every visitor part of the field.','https://ik.imagekit.io/18ab23oqaj/zone8.png'],
['Beyond the Bowl','Window installation','A final frame looking past food toward material, climate, design and possibility.','https://ik.imagekit.io/18ab23oqaj/zone9.png']
];
var main=document.querySelector('main');if(!main)return;
main.className='gf-main';main.removeAttribute('style');
document.querySelectorAll('body>footer,body>aside.quick,body>.progress,body>header.mast').forEach(function(el){el.remove()});
var stage='',tabs='';
zones.forEach(function(z,i){
  stage+='<img class="gf-stage-image'+(i===0?' on':'')+'" src="'+z[3]+'" alt="'+z[0]+', Experience Zone '+(i+1)+'" decoding="async">';
  tabs+='<button class="gf-pick" type="button" role="tab" aria-selected="'+(i===0?'true':'false')+'" data-zone="'+i+'"><span class="gf-thumb"><img src="'+z[3]+'" alt="" loading="lazy" decoding="async"></span><b>'+String(i+1).padStart(2,'0')+'</b><span class="gf-name">'+z[0]+'</span></button>';
});
main.innerHTML='<section class="gf-field"><div class="gf-stage">'+stage+'<span class="gf-mark">01</span></div><div class="gf-veil"></div><div class="gf-top"><span class="gf-eye">Experience Zones · BIRC 2026</span><p>Nine immersive worlds tracing rice from field to future.</p></div><div class="gf-copy"><small class="gf-count">'+zones[0][1]+'</small><h1>'+zones[0][0]+'</h1><p>'+zones[0][2]+'</p></div><div class="gf-bottom"><nav class="gf-picker" role="tablist" aria-label="Experience Zones">'+tabs+'</nav><div class="gf-hint">Nine worlds · one journey</div></div></section>';
var picker=main.querySelector('.gf-picker'),copy=main.querySelector('.gf-copy'),mark=main.querySelector('.gf-mark'),buttons=[].slice.call(main.querySelectorAll('.gf-pick')),stages=[].slice.call(main.querySelectorAll('.gf-stage-image')),active=0;
function select(i){if(i===active)return;active=i;buttons.forEach(function(b,k){b.setAttribute('aria-selected',k===i?'true':'false')});stages.forEach(function(s,k){s.classList.toggle('on',k===i)});mark.textContent=String(i+1).padStart(2,'0');copy.classList.add('swap');setTimeout(function(){copy.innerHTML='<small class="gf-count">'+zones[i][1]+'</small><h1>'+zones[i][0]+'</h1><p>'+zones[i][2]+'</p>';copy.classList.remove('swap')},140)}
picker.addEventListener('click',function(e){var b=e.target.closest('.gf-pick');if(b)select(Number(b.dataset.zone))});
picker.addEventListener('keydown',function(e){var i=buttons.indexOf(document.activeElement);if(i<0)return;var n=e.key==='ArrowRight'?i+1:e.key==='ArrowLeft'?i-1:-1;if(n<0||n>8)return;e.preventDefault();buttons[n].focus();select(n)});
})();
