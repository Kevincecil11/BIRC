(()=>{
'use strict';
function ready(fn){document.readyState==='loading'?document.addEventListener('DOMContentLoaded',fn):fn()}
ready(()=>{
  const root=document.getElementById('bircEditorRoot');
  if(!root)return;
  const panel=document.getElementById('bePanel'),head=panel?.querySelector('.be-head'),launch=document.getElementById('beLaunch'),hide=document.getElementById('beDisable'),tools=panel?.querySelector('.be-tools');
  if(!panel||!head||!launch||!hide||!tools)return;
  const style=document.createElement('style');
  style.id='bircEditorUpgradeStyle';
  style.textContent=`
  #bePanel{inset:auto 18px auto auto!important;top:82px!important;width:350px!important;height:min(760px,calc(100vh - 104px))!important;border:1px solid var(--be-line)!important;resize:both!important;overflow:hidden!important;box-shadow:0 22px 60px #0009!important}
  #bePanel.open{opacity:1!important}.be-head{cursor:move!important;user-select:none!important}
  #bePrecisionGrid{position:fixed;z-index:2147483500;inset:0;pointer-events:none;display:none;--cols:12;background-image:linear-gradient(to right,rgba(235,179,65,.22) 1px,transparent 1px),repeating-linear-gradient(to bottom,rgba(235,179,65,.1) 0 1px,transparent 1px 8px);background-size:calc((100vw - 64px)/var(--cols)) 100%,100% 8px;background-position:32px 0,0 0;clip-path:inset(0 32px)}
  #bePrecisionGrid.on{display:block}.be-grid-tools{display:grid;grid-template-columns:auto repeat(3,1fr);gap:4px}.be-grid-tools button{height:30px;border:1px solid var(--be-line);background:var(--be-panel);color:var(--be-muted);font:700 10px Inter,sans-serif;cursor:pointer}.be-grid-tools button.on{border-color:var(--be-gold);color:var(--be-gold)}
  `;
  document.head.appendChild(style);
  const grid=document.createElement('div');grid.id='bePrecisionGrid';grid.className='on';document.body.appendChild(grid);
  const controls=document.createElement('div');controls.className='be-grid-tools';controls.innerHTML='<button id="beGridToggle" class="on">Grid</button><button data-grid-cols="8">8 col</button><button data-grid-cols="12" class="on">12 col</button><button data-grid-cols="16">16 col</button>';
  tools.insertBefore(controls,tools.lastElementChild);
  hide.textContent='Minimize';
  hide.onclick=e=>{e.preventDefault();e.stopImmediatePropagation();panel.classList.remove('open')};
  launch.onclick=()=>panel.classList.add('open');
  document.getElementById('beClose').onclick=()=>panel.classList.remove('open');
  let drag=null;
  head.addEventListener('pointerdown',e=>{
    if(e.target.closest('button'))return;
    e.preventDefault();const r=panel.getBoundingClientRect();drag={x:e.clientX,y:e.clientY,left:r.left,top:r.top};panel.style.right='auto';
    const move=ev=>{panel.style.left=Math.max(0,Math.min(innerWidth-panel.offsetWidth,drag.left+ev.clientX-drag.x))+'px';panel.style.top=Math.max(0,Math.min(innerHeight-panel.offsetHeight,drag.top+ev.clientY-drag.y))+'px'};
    const up=()=>{removeEventListener('pointermove',move);removeEventListener('pointerup',up)};
    addEventListener('pointermove',move);addEventListener('pointerup',up);
  });
  document.getElementById('beGridToggle').onclick=e=>{e.currentTarget.classList.toggle('on');grid.classList.toggle('on')};
  controls.querySelectorAll('[data-grid-cols]').forEach(b=>b.onclick=()=>{grid.style.setProperty('--cols',b.dataset.gridCols);controls.querySelectorAll('[data-grid-cols]').forEach(x=>x.classList.toggle('on',x===b))});
});
})();
