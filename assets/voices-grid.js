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

  /* Homepage Option 15 masthead and language dropdown. */
  if(document.body.classList.contains('desktop-search-context')){
    if(!document.querySelector('link[data-home-nav-option15]')){
      var css=document.createElement('link');css.rel='stylesheet';css.href='assets/homepage-nav-option15.css?v=20260820a';css.dataset.homeNavOption15='1';document.head.appendChild(css);
    }
    var tools=document.querySelector('.masthead .tools'),menu=tools&&tools.querySelector('.menu-toggle');
    if(tools&&menu&&!tools.querySelector('.home-language')){
      var language=document.createElement('div');language.className='home-language';
      language.innerHTML='<button class="home-language-toggle" type="button" aria-label="Choose language" aria-expanded="false"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4a13 13 0 0 1 0 16M12 4a13 13 0 0 0 0 16"/></svg><span>EN</span><i aria-hidden="true"></i></button><div class="home-language-menu" role="menu"><button type="button" data-code="EN" lang="en" aria-current="true">English <span>EN</span></button><button type="button" data-code="HI" lang="hi">हिन्दी <span>HI</span></button><button type="button" data-code="AR" lang="ar">العربية <span>AR</span></button><button type="button" data-code="FR" lang="fr">Français <span>FR</span></button></div>';
      tools.insertBefore(language,menu);
      var toggle=language.querySelector('.home-language-toggle'),label=toggle.querySelector('span');
      function setOpen(open){language.classList.toggle('open',open);toggle.setAttribute('aria-expanded',String(open))}
      toggle.addEventListener('click',function(event){event.stopPropagation();setOpen(!language.classList.contains('open'))});
      language.querySelectorAll('.home-language-menu button').forEach(function(button){button.addEventListener('click',function(){language.querySelectorAll('[aria-current]').forEach(function(item){item.removeAttribute('aria-current')});button.setAttribute('aria-current','true');label.textContent=button.dataset.code;document.documentElement.lang=button.lang;setOpen(false)})});
      document.addEventListener('click',function(event){if(!event.target.closest('.home-language'))setOpen(false)});
      document.addEventListener('keydown',function(event){if(event.key==='Escape')setOpen(false)});
    }
  }
})();
