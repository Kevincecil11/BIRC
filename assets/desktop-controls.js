(function(){
  'use strict';

  /* Final Influencer alignment layer. Inserted last so legacy page CSS cannot override it. */
  var role=document.body.dataset.mobile;
  if(role==='creators.html'||role==='rice-masterchef.html'||role==='artists.html'){
    var finalStyle=document.createElement('style');
    finalStyle.id='final-influencer-alignment';
    finalStyle.textContent=`
      /* ---- Shared gutters ---- */
      body[data-mobile="creators.html"] main.page>section,
      body[data-mobile="artists.html"] main.page>section{
        padding-left:max(32px,calc((100vw - 1680px)/2))!important;
        padding-right:max(32px,calc((100vw - 1680px)/2))!important;
      }

      /* ---- Rice Masterchef: the .masterchef element is only a wrapper, never a hero ---- */
      body[data-mobile="rice-masterchef.html"] main.page>section.masterchef{
        display:block!important;
        min-height:0!important;
        margin:0!important;
        padding:0!important;
        background:#faf0e6!important;
        background-color:#faf0e6!important;
        color:#0d0d0b!important;
        overflow:visible!important;
      }
      body[data-mobile="rice-masterchef.html"] main.page>section.masterchef:before{
        content:none!important;display:none!important;background:none!important;
      }
      body[data-mobile="rice-masterchef.html"] main.page>section.masterchef>section{
        padding-left:max(32px,calc((100vw - 1680px)/2))!important;
        padding-right:max(32px,calc((100vw - 1680px)/2))!important;
      }
      body[data-mobile="rice-masterchef.html"] main.page>section.masterchef>section.master-hero{
        min-height:100vh!important;
        padding-top:136px!important;
        padding-bottom:56px!important;
        background-color:#0d0d0b!important;
        color:#faf0e6!important;
        display:flex!important;
        flex-direction:column!important;
        justify-content:center!important;
      }
      body[data-mobile="rice-masterchef.html"] .master-hero .title{color:#faf0e6!important}
      body[data-mobile="rice-masterchef.html"] .master-hero .lead{color:#aba49c!important}
      body[data-mobile="rice-masterchef.html"] .master-hero .eye{color:#ebb341!important}
      body[data-mobile="rice-masterchef.html"] .moment,
      body[data-mobile="rice-masterchef.html"] .master-score,
      body[data-mobile="rice-masterchef.html"] .chef-process,
      body[data-mobile="rice-masterchef.html"] .faq-section{background:#faf0e6!important;color:#0d0d0b!important}
      body[data-mobile="rice-masterchef.html"] .winner,
      body[data-mobile="rice-masterchef.html"] .eligibility{background:#191916!important;color:#faf0e6!important}
      body[data-mobile="rice-masterchef.html"] .master-apply{background:#ebb341!important;color:#0d0d0b!important}
      body[data-mobile="rice-masterchef.html"] .winner{display:block!important}
      body[data-mobile="rice-masterchef.html"] .winner .winner-list{margin-top:46px!important}

      /* ---- Section heading stacks share one left edge ---- */
      body[data-mobile="creators.html"] main.page section:not(.hero)>.head,
      body[data-mobile="rice-masterchef.html"] main.page section.masterchef>section:not(.master-hero)>.head{
        display:block!important;width:100%!important;margin:0 0 48px!important;padding:0!important;text-align:left!important;
      }
      body[data-mobile="creators.html"] main.page section:not(.hero)>.head>.eye,
      body[data-mobile="rice-masterchef.html"] main.page section.masterchef>section:not(.master-hero)>.head>.eye,
      body[data-mobile="rice-masterchef.html"] main.page section.masterchef>section:not(.master-hero)>.eye{
        display:block!important;margin:0 0 18px!important;padding:0!important;text-align:left!important;
      }
      body[data-mobile="creators.html"] main.page section:not(.hero)>.head>.section-title,
      body[data-mobile="rice-masterchef.html"] main.page section.masterchef>section:not(.master-hero)>.head>.section-title,
      body[data-mobile="rice-masterchef.html"] main.page section.masterchef>section:not(.master-hero)>.section-title,
      body[data-mobile="rice-masterchef.html"] main.page section.masterchef>section:not(.master-hero)>h2{
        display:block!important;margin:0!important;padding:0!important;max-width:24ch!important;text-align:left!important;
      }
      body[data-mobile="creators.html"] main.page section:not(.hero)>.head>p,
      body[data-mobile="rice-masterchef.html"] main.page section.masterchef>section:not(.master-hero)>.head>p,
      body[data-mobile="rice-masterchef.html"] main.page section.masterchef>section:not(.master-hero)>p{
        margin:20px 0 0!important;max-width:62ch!important;text-align:left!important;
      }

      /* ---- Centered application forms ---- */
      body[data-mobile="creators.html"] section.apply form.form,
      body[data-mobile="rice-masterchef.html"] section.master-apply form.master-form,
      body[data-mobile="artists.html"] section#apply form.form{
        width:min(940px,100%)!important;max-width:940px!important;margin-left:auto!important;margin-right:auto!important;
      }

      /* ---- Q&A: gold eyebrow, black title, questions, all on one left edge ---- */
      body[data-mobile="creators.html"] main.page section.faq-section,
      body[data-mobile="rice-masterchef.html"] main.page section.faq-section{background:#faf0e6!important;color:#0d0d0b!important}
      body[data-mobile="creators.html"] main.page section.faq-section>.head,
      body[data-mobile="creators.html"] main.page section.faq-section>.faq-items,
      body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.head,
      body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.faq-items{
        display:block!important;width:min(1040px,100%)!important;max-width:1040px!important;
        margin-left:auto!important;margin-right:auto!important;padding-left:0!important;padding-right:0!important;text-align:left!important;
      }
      body[data-mobile="creators.html"] main.page section.faq-section>.head,
      body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.head{margin-top:0!important;margin-bottom:42px!important}
      body[data-mobile="creators.html"] main.page section.faq-section>.head>.eye,
      body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.head>.eye{
        display:block!important;color:#c98e25!important;margin:0 0 18px!important;padding:0!important;text-align:left!important;
      }
      body[data-mobile="creators.html"] main.page section.faq-section>.head>.section-title,
      body[data-mobile="rice-masterchef.html"] main.page section.faq-section>.head>.section-title{
        display:block!important;color:#0d0d0b!important;margin:0!important;padding:0!important;max-width:24ch!important;text-align:left!important;
      }
      body[data-mobile="creators.html"] main.page section.faq-section .faq-item,
      body[data-mobile="rice-masterchef.html"] main.page section.faq-section .faq-item{border-color:#d8cec3!important}
      body[data-mobile="creators.html"] main.page section.faq-section .faq-q,
      body[data-mobile="rice-masterchef.html"] main.page section.faq-section .faq-q{color:#0d0d0b!important}

      /* ---- Artists: removed image, full ivory Q&A, no centered title indent ---- */
      body[data-mobile="artists.html"] .source-visual{display:none!important}
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq{
        position:relative!important;left:50%!important;width:100vw!important;max-width:none!important;
        margin:88px 0 -130px -50vw!important;
        padding:120px max(32px,calc((100vw - 1680px)/2))!important;
        background:#faf0e6!important;color:#0d0d0b!important;
      }
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq>.eye,
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq>.section-title,
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq>.faq-items{
        display:block!important;width:min(1040px,100%)!important;max-width:1040px!important;
        margin-left:auto!important;margin-right:auto!important;padding-left:0!important;padding-right:0!important;text-align:left!important;
      }
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq>.eye{color:#c98e25!important;margin-top:0!important;margin-bottom:18px!important}
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq>.section-title{color:#0d0d0b!important;margin-top:0!important}
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq>.faq-items{margin-top:42px!important}
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq .faq-item{border-color:#d8cec3!important}
      body[data-mobile="artists.html"] main.page section#apply>section.artist-faq .faq-q{color:#0d0d0b!important}
    `;
    document.head.appendChild(finalStyle);
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

;(function(){if(!document.querySelector('script[data-canonical-nav]')){var s=document.createElement('script');s.src='assets/canonical-navigation.js?v=20260816';s.dataset.canonicalNav='1';document.head.appendChild(s)}})();
