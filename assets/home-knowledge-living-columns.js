(function(){
'use strict';
var section=document.getElementById('knowledge-sessions');
if(!section||section.dataset.livingColumns==='1')return;
var sessions=[
['01','Crop Survey & Price Forecasting','Global Demand & Supply Outlook, 2027: Price Crash or New Bull Run?','desktop-knowledge-global-rice-demand-supply-outlook.html'],
['02','New Market Opportunities','Top 10 Rice Markets to Watch in 2027 and Entry Strategy','desktop-knowledge-top-rice-markets-entry-strategy.html'],
['03','Documentation, Insurance & Credit','Protecting Export Payments: Cut Risk by 80% and Prevent Disputes.','desktop-knowledge-protecting-rice-export-payments.html'],
['04','Shipping, Bulk & Containers','Bulk & Container Shipping 2026: Protect Margins and Mitigate Disputes','desktop-knowledge-rice-shipping-bulk-containers.html'],
['05','Quality & Certification','Why Buyers Reject Rice Shipments: How Exporters Can Prevent It','desktop-knowledge-rice-quality-certification-compliance.html'],
['06','Trade Schemes & Incentives','Policy Shifts 2026: Trade Schemes, Incentives and Export Opportunities','desktop-knowledge-rice-trade-schemes-incentives.html'],
['07','Sustainability & Carbon Credits','Sustainability Initiatives & Carbon Credits in Rice: Can Your Business Profit?','desktop-knowledge-rice-sustainability-carbon-credits.html'],
['08','Rice Milling','Profitable Rice Milling: Costs, Planning and Margin Improvement','desktop-knowledge-profitable-rice-milling.html'],
['09','Value-Added Products','Cleaning, sorting and branded value-added rice products.','desktop-knowledge-rice-value-added-products.html']
];
function row(s,clone){return '<a class="home-k08-session'+(clone?' is-clone':'')+'" href="'+s[3]+'"'+(clone?' aria-hidden="true" tabindex="-1"':'')+'><span class="home-k08-num">'+s[0]+'</span><span><span class="home-k08-topic">'+s[1]+'</span><strong class="home-k08-title">'+s[2]+'</strong></span><span class="home-k08-read">Read more <i aria-hidden="true">↗</i></span></a>'}
function track(items){return '<div class="home-k08-track">'+items.map(function(s){return row(s,false)}).join('')+items.map(function(s){return row(s,true)}).join('')+'</div>'}
section.dataset.livingColumns='1';section.className='home-k08';
section.innerHTML='<div class="shell"><header class="home-k08-head"><span class="eyebrow">Knowledge Sessions</span><h2>The 9 Knowledge Sessions.</h2><p>Nine working sessions across two days, built around the decisions rice businesses make every week.</p></header><div class="home-k08-cols" aria-label="Knowledge Sessions"><div class="home-k08-col">'+track(sessions.slice(0,5))+'</div><div class="home-k08-col">'+track(sessions.slice(5))+'</div><i class="home-k08-fade top" aria-hidden="true"></i><i class="home-k08-fade bottom" aria-hidden="true"></i></div></div>';
})();
