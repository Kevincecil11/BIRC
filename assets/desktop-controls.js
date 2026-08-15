(function(){
  'use strict';

  /* Rice Masterchef uses the exact Content Creators alignment vocabulary. */
  if(document.body.dataset.mobile==='rice-masterchef.html'){
    var alignment=document.createElement('style');
    alignment.id='masterchef-creator-alignment';
    alignment.textContent='\
body[data-mobile="rice-masterchef.html"] main.page>section.masterchef>section{padding-left:max(32px,calc((100vw - 1680px)/2))!important;padding-right:max(32px,calc((100vw - 1680px)/2))!important}\
body[data-mobile="rice-masterchef.html"] main.page>section.masterchef>section:not(.master-hero)>.eye{display:block!important;margin:0 0 18px!important;padding:0!important;text-align:left!important}\
body[data-mobile="rice-masterchef.html"] main.page>section.masterchef>section:not(.master-hero)>.section-title,body[data-mobile="rice-masterchef.html"] main.page>section.masterchef>section:not(.master-hero)>h2{display:block!important;margin:0!important;max-width:24ch!important;text-align:left!important}\
body[data-mobile="rice-masterchef.html"] main.page>section.masterchef>section:not(.master-hero)>p{margin:20px 0 0!important;max-width:62ch!important;text-align:left!important}\
body[data-mobile="rice-masterchef.html"] .master-apply form.master-form{width:min(940px,100%)!important;max-width:940px!important;margin-left:auto!important;margin-right:auto!important}\
body[data-mobile="rice-masterchef.html"] main.page section.faq-section{background:#faf0e6!important;color:#0d0d0b!important}\
body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.head{display:block!important;width:min(1040px,100%)!important;max-width:1040px!important;margin:0 auto 42px!important;text-align:left!important}\
body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.head>.eye{display:block!important;margin:0 0 18px!important;padding:0!important}\
body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.head>.section-title{display:block!important;margin:0!important;max-width:24ch!important}\
body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.faq-items{width:min(1040px,100%)!important;max-width:1040px!important;margin-left:auto!important;margin-right:auto!important}\
body[data-mobile="rice-masterchef.html"] main.page section.faq-section .faq-item{border-color:#d8cec3!important}\
body[data-mobile="rice-masterchef.html"] main.page section.faq-section .faq-q{color:#0d0d0b!important}\
body[data-mobile="rice-masterchef.html"] main.page section.faq-section .faq-a p{color:#6d6862!important}';
    document.head.appendChild(alignment);
  }

  var target=Date.parse('2026-10-23T10:00:00+05:30');
  function pad(n){return String(Math.max(0,n)).padStart(2,'0')}
  function updateCountdown(){
    var delta=Math.max(0,target-Date.now());
    var values={days:Math.floor(delta/86400000),hours:Math.floor(delta/3600000)%24,minutes:Math.floor(delta/60000)%60,seconds:Math.floor(delta/1000)%60};
    document.querySelectorAll('[data-shared-clock],[data-clock],#navClock').forEach(function(el){el.textContent=values.days+'d '+pad(values.hours)+'h '+pad(values.minutes)+'m'});
    var ordered=[pad(values.days),pad(values.hours),pad(values.minutes),pad(values.seconds)];
    document.querySelectorAll('.countdown,.clockrow,.final .clock').forEach(function(clock){clock.querySelectorAll('strong').forEach(function(el,index){if(index<4)el.textContent=ordered[index]})});
    [['cd',0],['ch',1],['cm',2],['cs',3]].forEach(function(pair){document.querySelectorAll('#'+pair[0]).forEach(function(el){el.textContent=ordered[pair[1]]})});
  }
  updateCountdown();setInterval(updateCountdown,1000);addEventListener('pageshow',updateCountdown);document.addEventListener('visibilitychange',function(){if(!document.hidden)updateCountdown()});
  var dialog=document.getElementById('desktopRegistrationChooser');
  if(!dialog){dialog=document.createElement('dialog');dialog.id='desktopRegistrationChooser';dialog.className='desktop-reg-dialog';dialog.setAttribute('aria-labelledby','desktopRegTitle');dialog.innerHTML='<header class="desktop-reg-head"><button class="desktop-reg-close" type="button" aria-label="Close registration options">×</button><small>BIRC 2026 Registration</small><h2 id="desktopRegTitle">Choose how you are joining.</h2><p>Visitor, Exhibitor or Buyer. Pick one to open the correct registration form.</p></header><div class="desktop-reg-roles"><a class="desktop-reg-role" href="register.html?type=visitor"><span class="role-number">01</span><h3>Visitor</h3><p>Attend sessions, explore the exhibition and meet industry leaders.</p><b>Continue as Visitor →</b></a><a class="desktop-reg-role" href="register.html?type=exhibitor"><span class="role-number">02</span><h3>Exhibitor</h3><p>Showcase products, services and solutions across the BIRC floor.</p><b>Continue as Exhibitor →</b></a><a class="desktop-reg-role" href="register.html?type=buyer"><span class="role-number">03</span><h3>Buyer</h3><p>Connect directly with exporters, millers and manufacturers.</p><b>Continue as Buyer →</b></a></div>';document.body.appendChild(dialog)}
  function openChooser(event){if(event){event.preventDefault();event.stopImmediatePropagation()}if(typeof dialog.showModal==='function'){if(!dialog.open)dialog.showModal()}else dialog.setAttribute('open','');document.body.classList.add('desktop-reg-open')}
  function closeChooser(){if(typeof dialog.close==='function'&&dialog.open)dialog.close();else dialog.removeAttribute('open');document.body.classList.remove('desktop-reg-open')}
  document.addEventListener('click',function(event){var trigger=event.target.closest('[data-register],.shared-register,.solid,.navbtn.gold,a[href="register.html?type=visitor"]');if(!trigger||dialog.contains(trigger))return;openChooser(event)},true);
  var close=dialog.querySelector('.desktop-reg-close');if(close)close.addEventListener('click',closeChooser);dialog.addEventListener('cancel',function(event){event.preventDefault();closeChooser()});dialog.addEventListener('close',function(){document.body.classList.remove('desktop-reg-open')});dialog.addEventListener('click',function(event){if(event.target!==dialog)return;var box=dialog.getBoundingClientRect();if(event.clientX<box.left||event.clientX>box.right||event.clientY<box.top||event.clientY>box.bottom)closeChooser()});
})();
