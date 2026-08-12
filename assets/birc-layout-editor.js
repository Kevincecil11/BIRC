(()=>{
'use strict';
const KEY='birc-layout-editor:', ENABLE='bircEditorEnabled';
const page=location.pathname.split('/').pop()||'desktop.html';
const allowed=/^desktop(?:-[a-z-]+)?\.html$/.test(page);
if(!allowed)return;
const qs=new URLSearchParams(location.search);
if(qs.get('editor')==='1')localStorage.setItem(ENABLE,'1');
if(qs.get('editor')==='0'){localStorage.removeItem(ENABLE);localStorage.removeItem(KEY+page);return;}
if(localStorage.getItem(ENABLE)!=='1')return;

const state={open:false,mode:'select',selected:null,drag:null,history:[],ops:[],applying:false};
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const snap=n=>Math.round(n/4)*4;
const esc=s=>CSS.escape(s);
function path(el){
  if(!el||el===document.body)return 'body';
  if(el.id)return '#'+esc(el.id);
  const bits=[];let n=el;
  while(n&&n!==document.body){
    let bit=n.tagName.toLowerCase();
    const cls=[...n.classList].filter(x=>!x.startsWith('be-')).slice(0,2);
    if(cls.length)bit+='.'+cls.map(esc).join('.');
    const sib=[...n.parentElement.children].filter(x=>x.tagName===n.tagName);
    if(sib.length>1)bit+=`:nth-of-type(${sib.indexOf(n)+1})`;
    bits.unshift(bit);n=n.parentElement;
  }
  return 'body > '+bits.join(' > ');
}
function record(op){if(state.applying)return;state.ops.push({...op,at:new Date().toISOString()});save();}
function save(){localStorage.setItem(KEY+page,JSON.stringify({version:1,page,updatedAt:new Date().toISOString(),operations:state.ops}));updateStatus();}
function load(){try{return JSON.parse(localStorage.getItem(KEY+page)||'null')}catch{return null}}
function target(sel){try{return document.querySelector(sel)}catch{return null}}
function applyOp(op){
  const el=target(op.selector);if(!el)return;
  if(op.type==='style')Object.assign(el.style,op.styles);
  if(op.type==='text')el.textContent=op.value;
  if(op.type==='hide')el.style.display=op.value?'none':'';
  if(op.type==='delete')el.remove();
  if(op.type==='duplicate'){const copy=el.cloneNode(true);el.after(copy)}
  if(op.type==='move'){const parent=target(op.parent),before=op.before?target(op.before):null;if(parent)parent.insertBefore(el,before)}
}
function replay(){const data=load();if(!data?.operations)return;state.applying=true;data.operations.forEach(applyOp);state.ops=data.operations;state.applying=false;}
function htmlClean(){
  const clone=document.documentElement.cloneNode(true);
  clone.querySelector('#bircEditorRoot')?.remove();clone.querySelector('#bircEditorStyle')?.remove();
  clone.querySelector('script[src$="birc-layout-editor.js"]')?.remove();
  clone.querySelectorAll('[data-be-selected],[data-be-hover]').forEach(x=>{x.removeAttribute('data-be-selected');x.removeAttribute('data-be-hover')});
  return '<!doctype html>\n'+clone.outerHTML;
}
function checkpoint(){state.history.push(JSON.stringify(state.ops));if(state.history.length>50)state.history.shift();$('#beUndo').disabled=false;}
function undo(){if(!state.history.length)return;localStorage.setItem(KEY+page,JSON.stringify({version:1,page,operations:JSON.parse(state.history.pop())}));location.reload();}
function updateStatus(){const n=state.ops.length;$('#beStatus').textContent=n?`${n} local change${n===1?'':'s'}`:'No local changes';}
function toast(msg){const t=$('#beToast');t.textContent=msg;t.classList.add('on');setTimeout(()=>t.classList.remove('on'),2200)}

const css=`
#bircEditorRoot{--be-bg:#171714;--be-panel:#20201c;--be-line:#39362f;--be-text:#faf0e6;--be-muted:#aaa39a;--be-gold:#ebb341;position:fixed;z-index:2147483600;inset:0;pointer-events:none;font:13px/1.4 Inter,system-ui,sans-serif;color:var(--be-text)}
#beLaunch{pointer-events:auto;position:fixed;right:18px;top:92px;height:42px;padding:0 16px;border:1px solid var(--be-gold);background:var(--be-bg);color:var(--be-gold);font:700 11px Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;box-shadow:0 12px 30px #0008}
#bePanel{pointer-events:auto;position:fixed;inset:0 0 0 auto;width:330px;background:var(--be-bg);border-left:1px solid var(--be-line);transform:translateX(102%);transition:transform .35s cubic-bezier(.16,1,.3,1);display:grid;grid-template-rows:58px auto 1fr auto;box-shadow:-22px 0 60px #0008}
#bePanel.open{transform:none}.be-head{display:flex;align-items:center;justify-content:space-between;padding:0 14px;border-bottom:1px solid var(--be-line)}.be-head b{font-size:14px}.be-icon{width:34px;height:34px;border:1px solid var(--be-line);background:var(--be-panel);color:var(--be-text);cursor:pointer}.be-tools{padding:12px 14px;border-bottom:1px solid var(--be-line);display:grid;gap:9px}.be-modes{display:grid;grid-template-columns:repeat(3,1fr);gap:4px}.be-modes button,.be-btn{min-height:36px;border:1px solid var(--be-line);background:var(--be-panel);color:var(--be-text);font:700 11px Inter,sans-serif;cursor:pointer}.be-modes button.on{border-color:var(--be-gold);color:var(--be-gold)}.be-status{display:flex;justify-content:space-between;color:var(--be-muted);font-size:11px}.be-body{min-height:0;overflow:auto}.be-block{padding:14px;border-bottom:1px solid var(--be-line)}.be-label{display:block;margin-bottom:8px;color:var(--be-muted);font-size:9px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}.be-selected{font-weight:750;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.be-tag{margin-top:3px;color:var(--be-gold);font:10px ui-monospace,monospace}.be-control{margin-top:12px}.be-control header{display:flex;justify-content:space-between;color:var(--be-muted);font-size:11px}.be-control output{color:var(--be-text);font-variant-numeric:tabular-nums}.be-control input{width:100%;accent-color:var(--be-gold)}.be-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px}.be-sections{display:grid;gap:5px}.be-section{min-height:38px;padding:0 9px;display:grid;grid-template-columns:18px 1fr;gap:7px;align-items:center;border:1px solid var(--be-line);background:var(--be-panel);color:var(--be-muted);text-align:left;cursor:grab}.be-section:hover{border-color:var(--be-gold);color:var(--be-text)}.be-section.dragging{opacity:.45}.be-section span:last-child{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.be-foot{padding:12px 14px;border-top:1px solid var(--be-line);display:grid;grid-template-columns:1fr 1fr;gap:6px}.be-btn.gold{background:var(--be-gold);border-color:var(--be-gold);color:#151512}.be-btn.danger{color:#ff9c90}.be-btn:disabled{opacity:.35;cursor:not-allowed}#beBox{position:absolute;z-index:2147483599;border:2px solid #ebb341;pointer-events:none}#beBox[hidden]{display:none}.be-handle{position:absolute;width:14px;height:14px;border:2px solid #151512;background:#ebb341;pointer-events:auto}.be-nw{left:-8px;top:-8px;cursor:nwse-resize}.be-ne{right:-8px;top:-8px;cursor:nesw-resize}.be-sw{left:-8px;bottom:-8px;cursor:nesw-resize}.be-se{right:-8px;bottom:-8px;cursor:nwse-resize}.be-drag{position:absolute;left:50%;top:-31px;transform:translateX(-50%);height:27px;padding:0 10px;border:0;background:#ebb341;color:#151512;font:800 10px Inter,sans-serif;pointer-events:auto;cursor:move;white-space:nowrap}#beToast{position:fixed;right:350px;bottom:20px;padding:11px 14px;border:1px solid var(--be-line);background:var(--be-panel);opacity:0;transform:translateY(10px);transition:.2s}#beToast.on{opacity:1;transform:none}[data-be-selected]{outline:3px solid #ebb341!important;outline-offset:-3px!important}[data-be-hover]{outline:1px dashed #c98e25!important;outline-offset:-1px!important}
`;
const st=document.createElement('style');st.id='bircEditorStyle';st.textContent=css;document.head.appendChild(st);
const root=document.createElement('div');root.id='bircEditorRoot';root.innerHTML=`
<button id="beLaunch">Edit layout</button><aside id="bePanel"><header class="be-head"><div><b>BIRC layout editor</b><div id="beStatus" style="color:#aaa39a;font-size:10px"></div></div><button class="be-icon" id="beClose">×</button></header>
<div class="be-tools"><div class="be-modes"><button data-mode="select" class="on">Select</button><button data-mode="move">Move</button><button data-mode="resize">Resize</button></div><div class="be-status"><span>Live preview</span><span>Saved locally</span></div></div>
<div class="be-body"><section class="be-block"><span class="be-label">Selection</span><div class="be-selected" id="beSelected">Nothing selected</div><div class="be-tag" id="beTag">Click an element</div></section>
<section class="be-block" id="beInspector" hidden><span class="be-label">Geometry</span><div class="be-control"><header><span>Width</span><output id="beWidthOut"></output></header><input id="beWidth" type="range" min="24" max="1800" step="4"></div><div class="be-control"><header><span>Minimum height</span><output id="beHeightOut"></output></header><input id="beHeight" type="range" min="16" max="1400" step="4"></div><div class="be-control"><header><span>Font size</span><output id="beFontOut"></output></header><input id="beFont" type="range" min="8" max="160"></div><div class="be-control"><header><span>Padding X</span><output id="bePxOut"></output></header><input id="bePx" type="range" min="0" max="260" step="4"></div><div class="be-control"><header><span>Padding Y</span><output id="bePyOut"></output></header><input id="bePy" type="range" min="0" max="260" step="4"></div><div class="be-control"><header><span>Gap</span><output id="beGapOut"></output></header><input id="beGap" type="range" min="0" max="180" step="4"></div><div class="be-grid" style="margin-top:12px"><button class="be-btn" id="beCenter">Center</button><button class="be-btn" id="beResetMove">Reset move</button><button class="be-btn" id="beText">Edit text</button><button class="be-btn" id="beDuplicate">Duplicate</button><button class="be-btn" id="beHide">Hide</button><button class="be-btn danger" id="beDelete">Delete</button></div></section>
<section class="be-block"><span class="be-label">Sections, drag to reorder</span><div class="be-sections" id="beSections"></div></section></div>
<footer class="be-foot"><button class="be-btn" id="beUndo" disabled>Undo</button><button class="be-btn" id="beReset">Reset page</button><button class="be-btn gold" id="beExport">Export changes</button><button class="be-btn" id="beDisable">Hide editor</button></footer></aside><div id="beBox" hidden><button class="be-drag">Drag</button><i class="be-handle be-nw" data-corner="nw"></i><i class="be-handle be-ne" data-corner="ne"></i><i class="be-handle be-sw" data-corner="sw"></i><i class="be-handle be-se" data-corner="se"></i></div><div id="beToast"></div>`;
document.body.appendChild(root);
const panel=$('#bePanel'), box=$('#beBox');
function setOpen(v){state.open=v;panel.classList.toggle('open',v)}
$('#beLaunch').onclick=()=>setOpen(true);$('#beClose').onclick=()=>setOpen(false);
$('#beDisable').onclick=()=>{localStorage.removeItem(ENABLE);root.remove();st.remove()};
function select(el){
  $$('[data-be-selected]').forEach(x=>x.removeAttribute('data-be-selected'));state.selected=el;
  $('#beInspector').hidden=!el;$('#beSelected').textContent=el?(el.id||[...el.classList].join('.')||el.tagName):'Nothing selected';$('#beTag').textContent=el?'<'+el.tagName.toLowerCase()+'>':'Click an element';
  if(!el){box.hidden=true;renderSections();return}el.setAttribute('data-be-selected','');sync();place();renderSections();
}
function place(){if(!state.selected)return;const r=state.selected.getBoundingClientRect();box.style.left=(r.left+scrollX)+'px';box.style.top=(r.top+scrollY)+'px';box.style.width=r.width+'px';box.style.height=r.height+'px';box.hidden=false;$$('.be-handle',box).forEach(x=>x.style.display=state.mode==='resize'?'block':'none');$('.be-drag',box).style.display=state.mode==='move'?'block':'none'}
function sync(){const el=state.selected;if(!el)return;const c=getComputedStyle(el),r=el.getBoundingClientRect(),v={Width:r.width,Height:r.height,Font:parseFloat(c.fontSize),Px:parseFloat(c.paddingLeft),Py:parseFloat(c.paddingTop),Gap:parseFloat(c.gap)||0};Object.entries(v).forEach(([k,n])=>{const i=$('#be'+k),o=$('#be'+k+'Out');i.value=Math.min(+i.max,Math.max(+i.min,Math.round(n)));o.textContent=Math.round(n)+'px'})}
function start(type,e,corner='se'){if(!state.selected)return;e.preventDefault();e.stopPropagation();checkpoint();const el=state.selected,r=el.getBoundingClientRect(),c=getComputedStyle(el),m=new DOMMatrix(c.transform==='none'?'matrix(1,0,0,1,0,0)':c.transform);state.drag={type,corner,x:e.clientX,y:e.clientY,w:r.width,h:r.height,tx:m.m41,ty:m.m42,selector:path(el)};const move=ev=>{const dx=ev.clientX-state.drag.x,dy=ev.clientY-state.drag.y;if(type==='move'){const tx=snap(state.drag.tx+dx),ty=snap(state.drag.ty+dy);el.style.transform=`translate(${tx}px,${ty}px)`;replaceStyleOp(state.drag.selector,{transform:el.style.transform})}else{const w=Math.max(24,snap(state.drag.w+(corner.includes('e')?dx:-dx))),h=Math.max(16,snap(state.drag.h+(corner.includes('s')?dy:-dy)));el.style.width=w+'px';el.style.minHeight=h+'px';replaceStyleOp(state.drag.selector,{width:el.style.width,minHeight:el.style.minHeight})}sync();place()};const up=()=>{removeEventListener('pointermove',move);removeEventListener('pointerup',up);save()};addEventListener('pointermove',move);addEventListener('pointerup',up)}
$('.be-drag',box).onpointerdown=e=>start('move',e);$$('.be-handle',box).forEach(h=>h.onpointerdown=e=>start('resize',e,h.dataset.corner));
function replaceStyleOp(selector,styles){let op=[...state.ops].reverse().find(x=>x.type==='style'&&x.selector===selector);if(op)Object.assign(op.styles,styles);else state.ops.push({type:'style',selector,styles:{...styles},at:new Date().toISOString()});updateStatus()}
function live(id,prop,unit='px'){const input=$(id);input.onpointerdown=checkpoint;input.oninput=()=>{if(!state.selected)return;const value=input.value+unit;state.selected.style[prop]=value;$(id+'Out').textContent=value;replaceStyleOp(path(state.selected),{[prop]:value});save();place()}}
live('#beWidth','width');live('#beHeight','minHeight');live('#beFont','fontSize');
function dual(id,a,b){const i=$(id);i.onpointerdown=checkpoint;i.oninput=()=>{if(!state.selected)return;const v=i.value+'px';state.selected.style[a]=v;state.selected.style[b]=v;$(id+'Out').textContent=v;replaceStyleOp(path(state.selected),{[a]:v,[b]:v});save();place()}}
dual('#bePx','paddingLeft','paddingRight');dual('#bePy','paddingTop','paddingBottom');live('#beGap','gap');
$('#beCenter').onclick=()=>{if(!state.selected)return;checkpoint();state.selected.style.marginInline='auto';replaceStyleOp(path(state.selected),{marginInline:'auto'});save();place()};
$('#beResetMove').onclick=()=>{if(!state.selected)return;checkpoint();state.selected.style.transform='';replaceStyleOp(path(state.selected),{transform:''});save();place()};
$('#beText').onclick=()=>{if(!state.selected)return;const v=prompt('Text content',state.selected.textContent);if(v===null)return;checkpoint();const sel=path(state.selected);state.selected.textContent=v;record({type:'text',selector:sel,value:v});select(state.selected)};
$('#beDuplicate').onclick=()=>{if(!state.selected)return;checkpoint();const sel=path(state.selected),c=state.selected.cloneNode(true);c.removeAttribute('data-be-selected');state.selected.after(c);record({type:'duplicate',selector:sel});select(c)};
$('#beHide').onclick=()=>{if(!state.selected)return;checkpoint();const sel=path(state.selected),v=state.selected.style.display!=='none';state.selected.style.display=v?'none':'';record({type:'hide',selector:sel,value:v});select(null)};
$('#beDelete').onclick=()=>{if(!state.selected||!confirm('Delete this element from your local draft?'))return;checkpoint();const sel=path(state.selected);state.selected.remove();record({type:'delete',selector:sel});select(null)};
function renderSections(){const wrap=$('#beSections');wrap.innerHTML='';$$('main > section').forEach((s,i)=>{const b=document.createElement('button');b.className='be-section';b.draggable=true;b.dataset.i=i;b.innerHTML='<span>⠿</span><span></span>';b.lastChild.textContent=s.querySelector('h1,h2,h3')?.textContent.trim().replace(/\s+/g,' ').slice(0,38)||s.id||`Section ${i+1}`;b.onclick=()=>{select(s);s.scrollIntoView({block:'center'})};b.ondragstart=()=>b.classList.add('dragging');b.ondragend=()=>b.classList.remove('dragging');b.ondragover=e=>e.preventDefault();b.ondrop=e=>{e.preventDefault();const moving=$('.be-section.dragging'),from=+moving?.dataset.i,to=i;if(Number.isNaN(from)||from===to)return;checkpoint();const arr=$$('main > section'),el=arr[from],dest=arr[to],parent=dest.parentElement,before=from<to?dest.nextElementSibling:dest;parent.insertBefore(el,before);record({type:'move',selector:path(el),parent:path(parent),before:before?path(before):null});renderSections()};wrap.appendChild(b)})}
$$('[data-mode]').forEach(b=>b.onclick=()=>{state.mode=b.dataset.mode;$$('[data-mode]').forEach(x=>x.classList.toggle('on',x===b));place()});
document.addEventListener('mouseover',e=>{if(e.target.closest('#bircEditorRoot,script,style'))return;e.target.setAttribute('data-be-hover','')});document.addEventListener('mouseout',e=>e.target.removeAttribute('data-be-hover'));document.addEventListener('click',e=>{if(e.target.closest('#bircEditorRoot')||!state.open)return;e.preventDefault();e.stopPropagation();select(e.target)},true);addEventListener('scroll',place,{passive:true});addEventListener('resize',place);
$('#beUndo').onclick=undo;$('#beReset').onclick=()=>{if(confirm('Clear every local edit for this page?')){localStorage.removeItem(KEY+page);location.reload()}};
$('#beExport').onclick=()=>{const payload={schema:'birc-layout-changes/v1',page,sourceUrl:location.href,exportedAt:new Date().toISOString(),operations:state.ops,notes:'Send this JSON to ClickUp Brain for review and permanent implementation.'};const blob=new Blob([JSON.stringify(payload,null,2)],{type:'application/json'}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=page.replace('.html','')+'-layout-changes.json';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(a.href),1000);toast('Changes exported')};
replay();renderSections();updateStatus();
})();