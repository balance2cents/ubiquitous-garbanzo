/* ===== Study tutor (shared across the subject apps) =====
   Needs window.TUTOR_CONFIG = {
     app, subject, course,            // names used in the prompt and header
     contextRoot: () => Element,      // what "what's on my screen" reads
     contextLabel: () => string,      // short label of that, e.g. "Chapter 4"
     addNote: (text) => void,         // append an explanation to the app's notes
     colors: {accent, onAccent, surface, surface2, ink, muted, line, bg}
   } */
(function(){
  const C=window.TUTOR_CONFIG; if(!C)return;
  const KEY='tutor-chat-'+C.app.toLowerCase().replace(/[^a-z0-9]+/g,'-');
  const css=`
  .tt-root{--tt-accent:${C.colors.accent};--tt-on:${C.colors.onAccent};--tt-surface:${C.colors.surface};--tt-surface2:${C.colors.surface2};--tt-ink:${C.colors.ink};--tt-muted:${C.colors.muted};--tt-line:${C.colors.line};--tt-bg:${C.colors.bg};font-size:14.5px;line-height:1.55}
  .tt-fab{position:fixed;right:18px;bottom:calc(18px + env(safe-area-inset-bottom,0px));z-index:60;display:inline-flex;align-items:center;gap:8px;border:0;border-radius:999px;padding:11px 18px 11px 14px;background:var(--tt-accent);color:var(--tt-on);font:inherit;font-weight:600;cursor:pointer;box-shadow:0 6px 20px rgba(0,0,0,.22)}
  .tt-fab:hover{filter:brightness(1.07)} .tt-fab:focus-visible{outline:3px solid var(--tt-ink);outline-offset:2px}
  .tt-fab svg{width:18px;height:18px;flex:none}
  .tt-panel{position:fixed;top:calc(12px + env(safe-area-inset-top,0px));right:12px;bottom:calc(12px + env(safe-area-inset-bottom,0px));width:min(440px,calc(100vw - 24px));z-index:70;display:flex;flex-direction:column;background:var(--tt-surface);color:var(--tt-ink);border:1px solid var(--tt-line);border-radius:14px;box-shadow:0 18px 50px rgba(0,0,0,.28);overflow:hidden}
  .tt-panel[hidden]{display:none!important}
  @media (max-width:640px){.tt-panel{top:auto;left:0;right:0;bottom:0;width:100%;height:88vh;border-radius:16px 16px 0 0;padding-bottom:env(safe-area-inset-bottom,0px)}}
  .tt-head{display:flex;align-items:center;gap:10px;padding:12px 14px;border-bottom:1px solid var(--tt-line)}
  .tt-title{font-weight:700;font-size:15.5px;line-height:1.2} .tt-sub{font-size:12px;color:var(--tt-muted)}
  .tt-head .tt-grow{flex:1;min-width:0}
  .tt-ibtn{border:1px solid var(--tt-line);background:var(--tt-surface);color:var(--tt-ink);border-radius:8px;padding:5px 10px;font:inherit;font-size:12.5px;cursor:pointer}
  .tt-ibtn:hover{background:var(--tt-surface2)}
  .tt-log{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:12px;background:var(--tt-bg)}
  .tt-msg{max-width:92%;padding:10px 13px;border-radius:12px;overflow-wrap:anywhere}
  .tt-msg.u{align-self:flex-end;background:var(--tt-accent);color:var(--tt-on);border-bottom-right-radius:4px;white-space:pre-wrap}
  .tt-msg.a{align-self:flex-start;background:var(--tt-surface);border:1px solid var(--tt-line);border-bottom-left-radius:4px}
  .tt-msg.a p{margin:0 0 8px} .tt-msg.a p:last-child{margin-bottom:0}
  .tt-msg.a ul,.tt-msg.a ol{margin:4px 0 8px;padding-left:20px} .tt-msg.a li{margin-bottom:3px}
  .tt-msg.a h4{margin:8px 0 4px;font-size:14.5px}
  .tt-msg.a code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.9em;background:var(--tt-surface2);padding:1px 5px;border-radius:4px}
  .tt-msg.think{color:var(--tt-muted);font-style:italic}
  .tt-acts{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
  .tt-acts button{border:1px solid var(--tt-line);background:var(--tt-surface2);color:var(--tt-ink);border-radius:7px;padding:4px 10px;font:inherit;font-size:12.5px;cursor:pointer}
  .tt-acts button:hover{border-color:var(--tt-accent)} .tt-acts button[disabled]{opacity:.7;cursor:default}
  .tt-err{align-self:stretch;font-size:13px;color:var(--tt-ink);background:var(--tt-surface2);border-left:3px solid var(--tt-accent);padding:8px 11px;border-radius:0 8px 8px 0}
  .tt-empty{color:var(--tt-muted);font-size:14px}
  .tt-empty b{color:var(--tt-ink)}
  .tt-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
  .tt-chips button{border:1px solid var(--tt-line);background:var(--tt-surface);color:var(--tt-ink);border-radius:999px;padding:5px 11px;font:inherit;font-size:12.5px;cursor:pointer;text-align:left}
  .tt-chips button:hover{border-color:var(--tt-accent)}
  .tt-ctx{display:flex;align-items:center;gap:8px;padding:8px 14px 0;font-size:12.5px;color:var(--tt-muted)}
  .tt-ctx input{accent-color:var(--tt-accent);margin:0}
  .tt-ctx span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .tt-comp{display:flex;gap:8px;align-items:flex-end;padding:8px 14px 12px}
  .tt-comp textarea{flex:1;min-width:0;resize:none;max-height:140px;min-height:42px;border:1px solid var(--tt-line);border-radius:10px;padding:10px 12px;font:inherit;background:var(--tt-bg);color:var(--tt-ink)}
  .tt-comp textarea:focus{outline:2px solid var(--tt-accent);outline-offset:0;border-color:transparent}
  .tt-send{border:0;border-radius:10px;padding:10px 15px;background:var(--tt-accent);color:var(--tt-on);font:inherit;font-weight:600;cursor:pointer}
  .tt-send[disabled]{opacity:.5;cursor:default}
  .tt-foot{font-size:11.5px;color:var(--tt-muted);padding:0 14px 10px}
  `;
  const style=document.createElement('style'); style.textContent=css; document.head.appendChild(style);
  const root=document.createElement('div'); root.className='tt-root';
  root.innerHTML=`<button class="tt-fab" type="button" hidden aria-haspopup="dialog"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.3 2.4c-.5.2-.8.6-.8 1.1v.5"/><path d="M12 16.5h.01"/></svg>Ask</button>
  <section class="tt-panel" hidden role="dialog" aria-label="Tutor">
    <div class="tt-head"><div class="tt-grow"><div class="tt-title">Tutor</div><div class="tt-sub">${esc(C.subject)} · ask anything, in your own words</div></div><button class="tt-ibtn" type="button" data-act="new">New chat</button><button class="tt-ibtn" type="button" data-act="close" aria-label="Close tutor">Close</button></div>
    <div class="tt-log" aria-live="polite"></div>
    <label class="tt-ctx"><input type="checkbox" checked><span></span></label>
    <div class="tt-comp"><textarea rows="1" placeholder="Ask about anything you don’t get…" aria-label="Your question"></textarea><button class="tt-send" type="button">Send</button></div>
    <div class="tt-foot">Uses your Claude account. The first question asks for permission. Check answers against your course notes.</div>
  </section>`;
  document.body.appendChild(root);
  const $=s=>root.querySelector(s), fab=$('.tt-fab'), panel=$('.tt-panel'), log=$('.tt-log'), box=$('textarea'), send=$('.tt-send'), ctxBox=$('.tt-ctx input'), ctxLbl=$('.tt-ctx span');
  function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
  function md(t){
    const lines=esc(t).split('\n'); let out='',list=null;
    const inline=s=>s.replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/(^|[\s(])\*([^*\n]+)\*(?=[\s).,;:!?]|$)/g,'$1<i>$2</i>');
    const close=()=>{if(list){out+=`</${list}>`;list=null;}};
    let para=[];
    const flush=()=>{if(para.length){out+=`<p>${inline(para.join('<br>'))}</p>`;para=[];}};
    for(const raw of lines){
      const l=raw.trimEnd(); let m;
      if(!l.trim()){flush();close();continue;}
      if((m=l.match(/^#{1,4}\s+(.*)/))){flush();close();out+=`<h4>${inline(m[1])}</h4>`;continue;}
      if((m=l.match(/^\s*[-*•]\s+(.*)/))){flush();if(list!=='ul'){close();out+='<ul>';list='ul';}out+=`<li>${inline(m[1])}</li>`;continue;}
      if((m=l.match(/^\s*\d+[.)]\s+(.*)/))){flush();if(list!=='ol'){close();out+='<ol>';list='ol';}out+=`<li>${inline(m[1])}</li>`;continue;}
      close(); para.push(l);
    }
    flush(); close(); return out;
  }
  const plain=t=>t.replace(/\*\*([^*]+)\*\*/g,'$1').replace(/`([^`]+)`/g,'$1').replace(/^#{1,4}\s+/gm,'');
  let turns=[]; try{turns=JSON.parse(localStorage.getItem(KEY)||'[]');if(!Array.isArray(turns))turns=[];}catch(e){turns=[];}
  const saveTurns=()=>{try{localStorage.setItem(KEY,JSON.stringify(turns.slice(-30)));}catch(e){}};
  let sample=null, busy=false, ctl=null, dead=false;
  const RULES=()=>`You are a patient, sharp tutor inside "${C.app}", a study app for the course "${C.subject}" (${C.course}) at the Lucerne University of Applied Sciences and Arts (HSLU), Bachelor in International Business Administration. The student is preparing for the written exam in January.
How to answer:
- Explain in plain American English, step by step, like a smart friend. Short sentences. Define any technical term the first time you use it.
- Use the course's own conventions and examples when the screen content below shows them; if your general knowledge differs from the course material, follow the course and say so.
- If the student asks about an exercise, guide them through the method first and check their reasoning; give the final number only if they ask for it or are clearly stuck.
- When it helps, give one short concrete example with real numbers.
- Keep answers under about 250 words unless the student asks for more. Use simple formatting only: short paragraphs, "- " bullets, numbered steps, **bold** for key terms. No tables, no LaTeX (write formulas inline like x̄ = Σx / n).
- If something is outside the course or you are unsure, say so honestly instead of guessing.`;
  function screen(){
    if(!ctxBox.checked)return '';
    let t=''; try{const el=C.contextRoot();t=el?el.innerText:'';}catch(e){}
    t=t.replace(/\n{3,}/g,'\n\n').trim();
    if(t.length>9000)t=t.slice(0,9000)+'\n[…]';
    return t?`\n\nWhat the student currently sees on screen (${C.contextLabel()}):\n"""\n${t}\n"""`:'';
  }
  function bubble(role,html,cls=''){const d=document.createElement('div');d.className=`tt-msg ${role} ${cls}`;d.innerHTML=html;log.appendChild(d);log.scrollTop=log.scrollHeight;return d;}
  function addActs(d,q,a){
    const acts=document.createElement('div'); acts.className='tt-acts';
    acts.innerHTML=`<button type="button">Add to my notes</button><button type="button">Copy</button>`;
    const [nb,cb]=acts.querySelectorAll('button');
    nb.onclick=()=>{try{C.addNote(`Q: ${q.trim()}\n${plain(a).trim()}`);nb.textContent='Added to notes ✓';nb.disabled=true;}catch(e){nb.textContent='Could not add';}};
    cb.onclick=()=>{try{navigator.clipboard.writeText(plain(a)).then(()=>{cb.textContent='Copied';},()=>{cb.textContent='Copy failed';});}catch(e){cb.textContent='Copy failed';}};
    d.appendChild(acts);
  }
  function renderLog(){
    log.innerHTML='';
    if(!turns.length){
      const sug=['Explain this page to me like I’m new to it','Give me a simple example with numbers','What are the typical exam mistakes here?','Quiz me with 3 questions on this'];
      log.innerHTML=`<div class="tt-empty"><b>Stuck on something?</b> Ask in your own words, even if it feels basic. Leave "Include what’s on my screen" on and I can see the chapter or exercise you’re looking at.<div class="tt-chips">${sug.map(s=>`<button type="button">${s}</button>`).join('')}</div></div>`;
      log.querySelectorAll('.tt-chips button').forEach(b=>b.onclick=()=>{box.value=b.textContent;ask();});
      return;
    }
    let lastQ='';
    turns.forEach(t=>{if(t.role==='user'){lastQ=t.content;bubble('u',esc(t.content));}else{const d=bubble('a',md(t.content));addActs(d,lastQ,t.content);}});
  }
  function setBusy(b){busy=b;send.textContent=b?'Stop':'Send';send.disabled=!b&&!box.value.trim();box.disabled=false;}
  const MSG={not_granted:'The tutor needs your permission to use Claude. Reload the page to be asked again.',sampling_disabled:'Claude isn’t available for this account right now.',not_declared:'The tutor isn’t enabled in this version of the app.',capability_disabled:'The tutor can’t run in this view.',capability_removed:'The tutor can’t run in this view.',rate_limited:'Too many questions at once, or your usage limit is reached. Wait a bit and send again.',session_expired:'You’ve been signed out. Sign in again and reload.',refused:'Claude declined that question. Try rephrasing it.',empty_completion:'No answer came back. Try asking it a bit differently.',prompt_too_large:'That was too much text at once. Untick "Include what’s on my screen" or ask a shorter question.',upstream_error:'The connection dropped. Send your question again.'};
  async function ask(){
    if(busy){ctl&&ctl.abort();return;}
    const q=box.value.trim(); if(!q||!sample||dead)return;
    if(!turns.length)log.innerHTML='';
    box.value=''; autosize();
    turns.push({role:'user',content:q}); saveTurns(); bubble('u',esc(q));
    const d=bubble('a','Thinking…','think'); setBusy(true);
    ctl=new AbortController();
    const hist=turns.slice(-16); while(hist.length&&hist[0].role!=='user')hist.shift();
    const input=[{role:'user',content:RULES()+screen()},...hist];
    try{
      const {text,truncated}=await sample(input,{cache:false,signal:ctl.signal,onText:({text})=>{d.classList.remove('think');d.innerHTML=md(text);log.scrollTop=log.scrollHeight;}});
      d.classList.remove('think'); d.innerHTML=md(text);
      turns.push({role:'assistant',content:text}); saveTurns(); addActs(d,q,text);
      if(truncated)bubble('err','The answer was cut short. Ask “continue” or ask for less at a time.','tt-err');
    }catch(e){
      const code=(e&&e.code)||'upstream_error';
      if(e&&e.text&&code!=='refused'){d.classList.remove('think');d.innerHTML=md(e.text);turns.push({role:'assistant',content:e.text});saveTurns();addActs(d,q,e.text);}
      else d.remove();
      if(code!=='cancelled'){const m=document.createElement('div');m.className='tt-err';m.textContent=MSG[code]||MSG.upstream_error;log.appendChild(m);}
      if(['not_granted','sampling_disabled','not_declared','capability_disabled','capability_removed','session_expired'].includes(code)){dead=true;send.disabled=true;box.disabled=true;}
    }finally{ctl=null;setBusy(false);log.scrollTop=log.scrollHeight;}
  }
  function autosize(){box.style.height='auto';box.style.height=Math.min(140,box.scrollHeight)+'px';if(!busy)send.disabled=!box.value.trim();}
  box.addEventListener('input',autosize);
  box.addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing){e.preventDefault();ask();}});
  send.onclick=ask;
  function open(prefill){
    panel.hidden=false; fab.hidden=true; ctxLbl.textContent='Include what’s on my screen: '+C.contextLabel(); renderLog();
    if(prefill){box.value=prefill;autosize();}
    setTimeout(()=>box.focus(),30);
  }
  function close(){panel.hidden=true;fab.hidden=!sample;ctl&&ctl.abort();fab.focus();}
  fab.onclick=()=>open();
  root.querySelector('[data-act=close]').onclick=close;
  root.querySelector('[data-act=new]').onclick=()=>{ctl&&ctl.abort();turns=[];saveTurns();renderLog();box.focus();};
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!panel.hidden)close();});
  window.Tutor={open:p=>{if(sample)open(p);},available:()=>!!sample};
  (async()=>{
    try{sample=window.claude&&typeof window.claude.use==='function'?await window.claude.use('sample'):null;}catch(e){sample=null;}
    if(sample){fab.hidden=!panel.hidden;document.dispatchEvent(new CustomEvent('tutor-ready'));}
  })();
})();
