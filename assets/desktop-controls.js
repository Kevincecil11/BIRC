(function(){
  'use strict';
  var target=new Date('2026-10-23T10:00:00+05:30').getTime();
  function pad(n){return String(Math.max(0,n)).padStart(2,'0')}
  function updateCountdown(){
    var delta=Math.max(0,target-Date.now());
    var days=Math.floor(delta/86400000),hours=Math.floor(delta/3600000)%24,minutes=Math.floor(delta/60000)%60,seconds=Math.floor(delta/1000)%60;
    document.querySelectorAll('[data-shared-clock],[data-clock],#navClock').forEach(function(el){el.textContent=days+'d '+pad(hours)+'h '+pad(minutes)+'m'});
    document.querySelectorAll('#cd').forEach(function(el){el.textContent=pad(days)});
    document.querySelectorAll('#ch').forEach(function(el){el.textContent=pad(hours)});
    document.querySelectorAll('#cm').forEach(function(el){el.textContent=pad(minutes)});
    document.querySelectorAll('#cs').forEach(function(el){el.textContent=pad(seconds)});
    document.querySelectorAll('.final .clockrow,.final .clock').forEach(function(clock){
      var values=[pad(days),pad(hours),pad(minutes),pad(seconds)];
      clock.querySelectorAll('strong').forEach(function(el,index){if(index<4)el.textContent=values[index]});
    });
  }
  updateCountdown();
  setInterval(updateCountdown,1000);
  document.addEventListener('visibilitychange',function(){if(!document.hidden)updateCountdown()});
  var dialog=document.getElementById('desktopRegistrationChooser');
  if(!dialog){
    dialog=document.createElement('dialog');dialog.id='desktopRegistrationChooser';dialog.className='desktop-reg-dialog';dialog.setAttribute('aria-labelledby','desktopRegTitle');
    dialog.innerHTML='<header class="desktop-reg-head"><button class="desktop-reg-close" type="button" aria-label="Close registration options">×</button><small>BIRC 2026 Registration</small><h2 id="desktopRegTitle">Choose how you are joining.</h2><p>Visitor, Exhibitor or Buyer. Pick one to open the correct registration form.</p></header><div class="desktop-reg-roles"><a class="desktop-reg-role" href="register.html?type=visitor"><span class="role-number">01</span><h3>Visitor</h3><p>Attend sessions, explore the exhibition and meet industry leaders.</p><b>Continue as Visitor →</b></a><a class="desktop-reg-role" href="register.html?type=exhibitor"><span class="role-number">02</span><h3>Exhibitor</h3><p>Showcase products, services and solutions across the BIRC floor.</p><b>Continue as Exhibitor →</b></a><a class="desktop-reg-role" href="register.html?type=buyer"><span class="role-number">03</span><h3>Buyer</h3><p>Connect directly with exporters, millers and manufacturers.</p><b>Continue as Buyer →</b></a></div>';
    document.body.appendChild(dialog);
  }
  function openChooser(event){if(event){event.preventDefault();event.stopImmediatePropagation()}if(typeof dialog.showModal==='function'){if(!dialog.open)dialog.showModal()}else dialog.setAttribute('open','');document.body.classList.add('desktop-reg-open')}
  function closeChooser(){if(typeof dialog.close==='function'&&dialog.open)dialog.close();else dialog.removeAttribute('open');document.body.classList.remove('desktop-reg-open')}
  document.addEventListener('click',function(event){var trigger=event.target.closest('[data-register],.shared-register,.solid,.navbtn.gold,a[href="register.html?type=visitor"]');if(!trigger||dialog.contains(trigger))return;openChooser(event)},true);
  var close=dialog.querySelector('.desktop-reg-close');if(close)close.addEventListener('click',closeChooser);
  dialog.addEventListener('cancel',function(event){event.preventDefault();closeChooser()});dialog.addEventListener('close',function(){document.body.classList.remove('desktop-reg-open')});
  dialog.addEventListener('click',function(event){if(event.target!==dialog)return;var box=dialog.getBoundingClientRect();if(event.clientX<box.left||event.clientX>box.right||event.clientY<box.top||event.clientY>box.bottom)closeChooser()});
})();
