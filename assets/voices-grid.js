(function(){
  'use strict';
  document.querySelectorAll('.voices-grid-note').forEach(function(note){note.remove()});
  document.querySelectorAll('.zone-card').forEach(function(card){
    if(card.dataset.fullCardFlip==='true')return;
    card.dataset.fullCardFlip='true';card.tabIndex=0;card.setAttribute('role','button');
    function flip(){var button=card.querySelector('.zone-read'),open=card.classList.toggle('is-flipped');if(button)button.setAttribute('aria-expanded',String(open))}
    card.addEventListener('click',function(event){if(event.target.closest('button'))return;flip()});
    card.addEventListener('keydown',function(event){if((event.key==='Enter'||event.key===' ')&&!event.target.closest('button')){event.preventDefault();flip()}});
  });
})();
