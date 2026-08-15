(function(){
  'use strict';
  var track=document.querySelector('.voices-track');
  if(!track)return;
  document.querySelectorAll('.voices-grid-note').forEach(function(note){note.remove()});
  document.querySelectorAll('.voice-grid-card').forEach(function(card){
    var image=card.querySelector('.voice-grid-image');
    var quote=card.querySelector('blockquote');
    var person=card.querySelector('.voice-grid-person');
    if(!image||!quote||!person)return;
    var inner=document.createElement('div'),front=document.createElement('div'),back=document.createElement('div');
    inner.className='voice-grid-inner';front.className='voice-grid-front';back.className='voice-grid-back';
    front.appendChild(image.cloneNode(true));front.appendChild(person.cloneNode(true));
    var hint=document.createElement('span');hint.className='voice-grid-hint';hint.textContent='Click to read';front.appendChild(hint);
    back.appendChild(quote.cloneNode(true));back.appendChild(person.cloneNode(true));
    inner.appendChild(front);inner.appendChild(back);card.replaceChildren(inner);
    card.tabIndex=0;card.setAttribute('role','button');card.setAttribute('aria-expanded','false');
    function setOpen(open){document.querySelectorAll('.voice-grid-card.is-flipped').forEach(function(other){if(other!==card){other.classList.remove('is-flipped');other.setAttribute('aria-expanded','false')}});card.classList.toggle('is-flipped',open);card.setAttribute('aria-expanded',String(open));track.classList.toggle('is-reading',open)}
    card.addEventListener('click',function(){setOpen(!card.classList.contains('is-flipped'))});
    card.addEventListener('keydown',function(event){if(event.key==='Enter'||event.key===' '){event.preventDefault();setOpen(!card.classList.contains('is-flipped'))}});
  });
  document.addEventListener('keydown',function(event){if(event.key==='Escape'){document.querySelectorAll('.voice-grid-card.is-flipped').forEach(function(card){card.classList.remove('is-flipped');card.setAttribute('aria-expanded','false')});track.classList.remove('is-reading')}});
})();
