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
main.innerHTML='<section class="gf-field"><div class="gf-stage">'+stage+'</div><div class="gf-veil"></div><canvas class="gf-canvas" aria-hidden="true"></canvas><div class="gf-top"><span class="gf-eye">Live grain field</span><p>Move the cursor through the field. The grains part, then settle back into formation.</p></div><div class="gf-copy"><small class="gf-count">'+zones[0][1]+'</small><h1>'+zones[0][0]+'</h1><p>'+zones[0][2]+'</p></div><div class="gf-bottom"><nav class="gf-picker" role="tablist" aria-label="Experience Zones">'+tabs+'</nav><div class="gf-hint">Nine worlds · one grain field</div></div></section>';
var picker=main.querySelector('.gf-picker'),copy=main.querySelector('.gf-copy'),buttons=[].slice.call(main.querySelectorAll('.gf-pick')),stages=[].slice.call(main.querySelectorAll('.gf-stage-image')),field=main.querySelector('.gf-field');
var canvas=main.querySelector('.gf-canvas'),ctx=canvas.getContext('2d'),dpr=1,w=0,h=0,pts=[],target=[],active=0,mouse={x:-9999,y:-9999},gold='#ebb341',muted='#79705f';
function resize(){dpr=Math.min(devicePixelRatio||1,2);w=canvas.clientWidth;h=canvas.clientHeight;if(!w||!h)return;canvas.width=w*dpr;canvas.height=h*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);if(!pts.length)seed();shape(active)}
function seed(){var n=Math.min(2100,Math.max(1100,Math.floor(w*h/700)));for(var i=0;i<n;i++)pts.push({x:Math.random()*w,y:Math.random()*h,vx:0,vy:0,a:.32+Math.random()*.6,s:1.1+Math.random()*2.1,r:Math.random()*6.28,g:Math.random()<.27})}
function shape(num){var oh=Math.max(280,Math.floor(h*.44)),ow=Math.floor(oh*1.28),off=document.createElement('canvas');off.width=ow;off.height=oh;var o=off.getContext('2d');o.fillStyle='#fff';o.textAlign='center';o.textBaseline='middle';o.font='700 '+Math.floor(oh*.98)+'px Poppins, sans-serif';o.fillText(String(num+1).padStart(2,'0'),ow/2,oh*.52);var data=o.getImageData(0,0,ow,oh).data,samples=[],ox=w*.63-ow/2,oy=h*.44-oh/2;for(var y=0;y<oh;y+=3)for(var x=0;x<ow;x+=3)if(data[(y*ow+x)*4+3]>90)samples.push([x+ox,y+oy]);for(var i=samples.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),q=samples[i];samples[i]=samples[j];samples[j]=q}target=samples}
function select(i){if(i===active)return;active=i;buttons.forEach(function(b,k){b.setAttribute('aria-selected',k===i?'true':'false')});stages.forEach(function(s,k){s.classList.toggle('on',k===i)});copy.classList.add('swap');setTimeout(function(){copy.innerHTML='<small class="gf-count">'+zones[i][1]+'</small><h1>'+zones[i][0]+'</h1><p>'+zones[i][2]+'</p>';copy.classList.remove('swap')},140);shape(i)}
picker.addEventListener('click',function(e){var b=e.target.closest('.gf-pick');if(b)select(Number(b.dataset.zone))});
picker.addEventListener('keydown',function(e){var i=buttons.indexOf(document.activeElement);if(i<0)return;var n=e.key==='ArrowRight'?i+1:e.key==='ArrowLeft'?i-1:-1;if(n<0||n>8)return;e.preventDefault();buttons[n].focus();select(n)});
function frame(){if(w&&h){ctx.clearRect(0,0,w,h);var t=performance.now()*.00025;for(var i=0;i<pts.length;i++){var p=pts[i],q=target[i%Math.max(1,target.length)]||[w*.63,h*.44],dx=q[0]-p.x,dy=q[1]-p.y,mdx=p.x-mouse.x,mdy=p.y-mouse.y,dist=Math.sqrt(mdx*mdx+mdy*mdy);if(dist<130){var f=(130-dist)/130;p.vx+=mdx/(dist||1)*f*.7;p.vy+=mdy/(dist||1)*f*.7}p.vx+=dx*.0009;p.vy+=dy*.0009;p.vx*=.912;p.vy*=.912;p.x+=p.vx+Math.cos(t+i)*.04;p.y+=p.vy+Math.sin(t*1.3+i)*.04;p.r+=.01;ctx.save();ctx.translate(p.x,p.y);ctx.rotate(p.r);ctx.globalAlpha=p.a;ctx.fillStyle=p.g?gold:muted;ctx.beginPath();ctx.ellipse(0,0,p.s*.5,p.s*2.1,0,0,6.283);ctx.fill();ctx.restore()}}requestAnimationFrame(frame)}
field.addEventListener('pointermove',function(e){var r=canvas.getBoundingClientRect();mouse.x=e.clientX-r.left;mouse.y=e.clientY-r.top});
field.addEventListener('pointerleave',function(){mouse.x=-9999;mouse.y=-9999});
addEventListener('resize',resize);
function boot(){resize();frame()}
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(boot);else boot();
setTimeout(resize,400);
})();
