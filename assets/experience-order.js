(function(){
  'use strict';
  /* Supplied BIRC document order. Seed Cloud is retained as the ninth approved zone. */
  var order=[
    'The Rice Archive',
    'Hands of Rice',
    'How the World Eats Rice',
    'Beyond the Bowl',
    'The World Within',
    'Rice Mirror',
    'The Rice Route Map',
    'Rice Through Time',
    'Seed Cloud'
  ];
  function titleOf(node){
    return (node.getAttribute('data-zone-card')||(node.querySelector('h2,h3')||{}).textContent||'').trim();
  }
  function reorder(container,nodes){
    var map={};nodes.forEach(function(node){map[titleOf(node)]=node});
    order.forEach(function(title,index){
      var node=map[title];if(!node)return;
      container.appendChild(node);
      var top=node.querySelector('.zone-card-top span:first-child');
      var idx=node.querySelector('.index');
      if(top)top.textContent=String(index+1).padStart(2,'0')+' / 09';
      if(idx)idx.textContent=String(index+1).padStart(2,'0')+' / 09';
    });
  }
  var atlas=document.querySelector('.zone-atlas-grid');
  if(atlas)reorder(atlas,Array.from(atlas.querySelectorAll(':scope > .zone-card')));
  var experience=document.querySelector('main .zones');
  if(experience)reorder(experience,Array.from(experience.querySelectorAll(':scope > .zone')));
  var mobileMain=document.querySelector('main.page');
  if(mobileMain){
    var zones=Array.from(mobileMain.querySelectorAll(':scope > section.zone'));
    if(zones.length){
      var anchor=zones[0];
      var map={};zones.forEach(function(node){map[titleOf(node)]=node});
      order.forEach(function(title){if(map[title])mobileMain.insertBefore(map[title],anchor)});
    }
  }
})();
