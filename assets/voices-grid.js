(function(){
  var track=document.querySelector('.voices-track');
  if(!track)return;
  track.addEventListener('focusin',function(){track.style.animationPlayState='paused'});
  track.addEventListener('focusout',function(){track.style.animationPlayState='running'});
})();
