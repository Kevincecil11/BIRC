from pathlib import Path
import re

p=Path('desktop.html');h=p.read_text()

# Experience heading begins exactly where the visual square begins.
# Date statement becomes three deliberate lines.
old='<p>Policy on Friday. Trade on Saturday. The future on Sunday.</p>'
new='<p class="date-statement"><span>Policy on Friday.</span><span>Trade on Saturday.</span><span>The future on Sunday.</span></p>'
assert old in h
h=h.replace(old,new,1)

# Replace quote stage and remove the four-name selector row.
old_section=re.search(r'<section class="voices light section" id="voices">.*?</section>',h,re.S)
assert old_section
new_section='''<section class="voices light section" id="voices"><div class="shell voices-layout"><header class="voices-intro"><span class="eyebrow">Voices of the industry</span><h2>What leaders say</h2><p>Four perspectives from across global trade, policy, and industry.</p><div class="voice-progress" aria-hidden="true"><i id="voiceProgress"></i></div></header><div class="voice-stage" id="voiceStage" aria-live="polite"><div class="voice-index" id="voiceIndex">01 / 04</div><div class="voice-quote"><div class="qmark" aria-hidden="true">&ldquo;</div><blockquote id="quoteText">BIRC redefined how we see global rice trade.</blockquote></div><aside class="voice-person"><div class="voice-portrait" id="voicePortrait" role="img" aria-label="Portrait placeholder for Priya Nair"><span>Portrait</span></div><b id="quoteName">Priya Nair</b><span id="quoteRole">Director, Global Grain Council</span></aside></div></div></section>'''
h=h[:old_section.start()]+new_section+h[old_section.end():]

# Replace old voice script with automatic rotation.
pattern=r'/\* voices \*/.*?/\* plan your visit \*/'
voice_js='''/* voices, automatic rotation */
  var voices=[
    ['BIRC redefined how we see global rice trade.','Priya Nair','Director, Global Grain Council'],
    ['The ecosystem here moves faster than any fair.','Marco van der Belt','CEO, EuroRice Partners'],
    ['Every session sharpened our market view.','Chen Wei','Head of Trade, Asia Foods'],
    ["A platform built for the industry's future.",'James Sterling','Founder, Sterling Commodities']
  ];
  var voiceCurrent=0,voiceTimer=null,voiceStage=document.getElementById('voiceStage'),qText=document.getElementById('quoteText'),qName=document.getElementById('quoteName'),qRole=document.getElementById('quoteRole'),voiceIndex=document.getElementById('voiceIndex'),voiceProgress=document.getElementById('voiceProgress'),voicePortrait=document.getElementById('voicePortrait');
  function setVoice(i){voiceCurrent=(i+voices.length)%voices.length;var v=voices[voiceCurrent];voiceStage.classList.remove('swap');void voiceStage.offsetWidth;voiceStage.classList.add('swap');qText.textContent=v[0];qName.textContent=v[1];qRole.textContent=v[2];voiceIndex.textContent=String(voiceCurrent+1).padStart(2,'0')+' / 04';voiceProgress.style.width=((voiceCurrent+1)/voices.length*100)+'%';voicePortrait.setAttribute('aria-label','Portrait placeholder for '+v[1])}
  function startVoices(){if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;clearInterval(voiceTimer);voiceTimer=setInterval(function(){setVoice(voiceCurrent+1)},5200)}
  setVoice(0);startVoices();

  /* plan your visit */'''
h,n=re.subn(pattern,voice_js,h,count=1,flags=re.S)
assert n==1

css='''
/* experience header aligns to visual stage */
.zones>.shell:first-child .sechead{grid-template-columns:320px minmax(0,1fr);gap:64px}
.zones>.shell:first-child .sechead>div{grid-column:2}
.zones>.shell:first-child .sechead>.eyebrow{grid-column:1}
.date-statement span{display:block}
/* automatic editorial leader stage */
.voices .voices-layout{grid-template-columns:300px minmax(0,1fr);grid-template-rows:1fr;gap:72px}
.voices-intro{grid-row:1;grid-column:1}
.voices .voice-stage{grid-column:2;min-height:460px;padding:44px 48px;display:grid;grid-template-columns:minmax(0,1fr) 220px;grid-template-rows:auto 1fr;gap:28px 48px;align-items:stretch}
.voice-index{grid-column:1/-1;grid-row:1;text-align:right}
.voice-quote{grid-column:1;grid-row:2;display:flex;flex-direction:column;justify-content:flex-end;min-width:0;position:relative;z-index:2}
.voice-quote .qmark{margin:0 0 34px}
.voice-quote blockquote{margin:0;font:500 clamp(38px,3.25vw,58px)/1.08 Poppins,sans-serif;letter-spacing:-.05em;max-width:14ch}
.voice-person{grid-column:2;grid-row:2;align-self:end;display:flex;flex-direction:column;align-items:flex-end;text-align:right;position:relative;z-index:2}
.voice-portrait{width:180px;aspect-ratio:3/4;margin-bottom:20px;display:grid;place-items:end start;padding:14px;background:repeating-linear-gradient(125deg,transparent 0 22px,#faf0e608 22px 23px),var(--ink-3);border:1px solid var(--dl);color:var(--lm)}
.voice-portrait span{font:600 8px Poppins,sans-serif;letter-spacing:.14em;text-transform:uppercase}
.voice-person b{font:600 16px Poppins,sans-serif;color:var(--linen)}
.voice-person>span{margin-top:5px;color:var(--dm);font-size:12px}
.voice-stage.swap .voice-quote,.voice-stage.swap .voice-person{animation:voiceSwap .55s var(--e)}
@keyframes voiceSwap{from{opacity:0;transform:translateY(12px)}}
.voices .voicelist{display:none!important}
@media(max-width:1400px){.zones>.shell:first-child .sechead{grid-template-columns:320px minmax(0,1fr);gap:64px}.voices .voices-layout{grid-template-columns:250px minmax(0,1fr);gap:48px}.voices .voice-stage{grid-template-columns:minmax(0,1fr) 190px;gap:24px 36px}.voice-portrait{width:160px}}
@media(max-width:1180px){.zones>.shell:first-child .sechead{grid-template-columns:280px minmax(0,1fr);gap:48px}.voices .voice-stage{grid-template-columns:minmax(0,1fr) 170px;padding:36px}.voice-portrait{width:145px}.voice-quote blockquote{font-size:38px}}
@media(prefers-reduced-motion:reduce){.voice-stage.swap .voice-quote,.voice-stage.swap .voice-person{animation:none}}
'''
h=h.replace('</style>',css+'</style>',1)
p.write_text(h)

p=Path('context.md');text=p.read_text()
needle='- Desktop homepage uses a wide 1680px shell with 32px minimum side gutters.'
addition='- Desktop Experience Zones heading aligns with the left edge of the visual stage, the three-day statement is set as three separate lines, and Voices uses an automatic four-quote rotation with a right-aligned portrait placeholder, name, and designation. The bottom four-name selector is removed.\n'
assert needle in text
p.write_text(text.replace(needle,addition+needle,1))
