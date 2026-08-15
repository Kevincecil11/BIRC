(function(){
  'use strict';
  var track=document.querySelector('.voices-track');
  if(!track)return;
  document.querySelectorAll('.voices-grid-note').forEach(function(note){note.remove()});
  Array.from(document.querySelectorAll('*')).forEach(function(el){
    if(el.children.length===0&&el.textContent.trim().toLowerCase()==='04 principles')el.remove();
  });
  document.querySelectorAll('.voice-grid-card').forEach(function(card){
    var image=card.querySelector('.voice-grid-image');
    var quote=card.querySelector('blockquote');
    var person=card.querySelector('.voice-grid-person');
    if(!image||!quote||!person||card.querySelector('.voice-grid-inner'))return;
    var inner=document.createElement('div');inner.className='voice-grid-inner';
    var front=document.createElement('div');front.className='voice-grid-front';
    var back=document.createElement('div');back.className='voice-grid-back';
    front.appendChild(image.cloneNode(true));
    front.appendChild(person.cloneNode(true));
    var hint=document.createElement('span');hint.className='voice-grid-hint';hint.textContent='Click to read';front.appendChild(hint);
    back.appendChild(quote.cloneNode(true));back.appendChild(person.cloneNode(true));
    inner.appendChild(front);inner.appendChild(back);card.replaceChildren(inner);
    card.tabIndex=0;card.setAttribute('role','button');card.setAttribute('aria-expanded','false');card.setAttribute('aria-label','Open testimonial from '+(person.querySelector('b')?person.querySelector('b').textContent:'industry leader'));
    function toggle(){var open=card.classList.toggle('is-flipped');card.setAttribute('aria-expanded',String(open))}
    card.addEventListener('click',toggle);
    card.addEventListener('keydown',function(event){if(event.key==='Enter'||event.key===' '){event.preventDefault();toggle()}});
  });
})();
