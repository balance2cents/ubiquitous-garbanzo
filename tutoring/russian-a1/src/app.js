// ============================================================
// Пятёрка: app logic
// Data: VOCAB (per lesson [ru, en, de, extra]), LESSONS, READINGS, ... from content.js
// Two shared db docs: p5/student (her progress, she writes) and p5/tutor (plan, notes, feedback, tutor writes).
// ============================================================
const $ = (s, r=document) => r.querySelector(s);
const $$ = (s, r=document) => [...r.querySelectorAll(s)];
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const STRESS = /́/g;
const norm = s => String(s||'').replace(STRESS,'').toLowerCase().replace(/ё/g,'е').replace(/[.,!?…:;"«»()]/g,' ').replace(/\s+/g,' ').trim();
const answers = a => Array.isArray(a) ? a : [a];
const isRight = (given, a) => answers(a).some(x => norm(x) === norm(given));
const uid = () => Math.random().toString(36).slice(2,9);
const todayStr = () => { const d=new Date(); return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'); };
const dayNum = (s=todayStr()) => Math.round(Date.parse(s+'T00:00:00Z')/864e5);
const fmtDate = s => new Date(s+'T12:00:00').toLocaleDateString('en-US',{weekday:'short', month:'short', day:'numeric'});
const pct = x => Math.round((x||0)*100);
const shuffle = a => { a=[...a]; for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]];} return a; };

// ---------- words ----------
const WORDS = [];
Object.keys(VOCAB).forEach(L => VOCAB[L].forEach((w,i) => WORDS.push({id:L+'-'+i, L:+L, ru:w[0], en:w[1], de:w[2], x:w[3]})));
// Accepted typed answers for a headword: "Как вас / тебя зовут?" → both variants; "мой, моя" → each part.
function ruAnswers(ru){
  const base = ru.replace(/…/g,'').trim(); const out=[base];
  if(/ \/ /.test(base)){ const m=base.match(/(\S+) \/ (\S+)/); out.push(base.replace(m[0],m[1]), base.replace(m[0],m[2])); }
  if(base.includes(',')) out.push(...base.split(',').map(x=>x.trim()));
  return out;
}
const WORD = Object.fromEntries(WORDS.map(w => [w.id, w]));
const SRS_DAYS = [0, 1, 3, 7, 14, 30]; // interval after reaching box n

// ---------- state ----------
const DEF_STUDENT = () => ({ srs:{}, newLog:{}, quiz:{}, drill:{}, mistakes:[], writing:{}, mocks:[], hw:{}, read:{}, streak:{last:'', n:0}, _v:0 });
const DEF_TUTOR = () => ({ scope:[1,2,3,4,5,6,7,8,9], classAt:1, newPerDay:15, note:'', noteTs:0, weeks:DEFAULT_WEEKS.map(([d,f])=>({d,f})), homework:[], fb:{}, _v:0 });
const loadLocal = (k, def) => { try { const v = JSON.parse(localStorage.getItem(k)||'null'); return v ? Object.assign(def(), v) : def(); } catch(e){ return def(); } };
const saveLocal = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch(e){} };
const S = { student: loadLocal('p5-student', DEF_STUDENT), tutor: loadLocal('p5-tutor', DEF_TUTOR), scratch: DEF_STUDENT() };
let role = 'student';          // becomes 'tutor' for the artifact owner
let preview = false;           // tutor looking at the student pages
const ui = (() => { try { return JSON.parse(localStorage.getItem('p5-ui')||'{}'); } catch(e){ return {}; } })();
const saveUi = () => { try { localStorage.setItem('p5-ui', JSON.stringify(ui)); } catch(e){} };
// Where practice gets recorded: her record for her, a throwaway scratch record for the tutor.
const P = () => role === 'tutor' ? S.scratch : S.student;
const T = () => S.tutor;
const inScope = L => T().scope.includes(L);

// ---------- sync (db capability, with localStorage as the always-on cache) ----------
const refs = {}; const timers = {}; const lastJSON = {};
let dbOK = false;
function setSync(t, cls){ const el=$('#sync'); el.className='sync '+cls; $('#sync-t').textContent=t; }
function save(which){
  if(which==='student' && role==='tutor') return; // tutor's own practice stays in scratch
  if(which==='tutor' && role!=='tutor') return;
  const obj = S[which]; obj._v = (obj._v||0)+1;
  saveLocal('p5-'+which, obj);
  if(!refs[which]) return;
  setSync('Saving…','ok busy');
  clearTimeout(timers[which]);
  timers[which] = setTimeout(async () => {
    const json = JSON.stringify(obj);
    if(json === lastJSON[which]) { setSync('Synced','ok'); return; }
    try { await refs[which].set(JSON.parse(json)); lastJSON[which]=json; setSync('Synced','ok'); }
    catch(e){ setSync('Saved on this device only','local'); }
  }, 700);
}
function adopt(which, data){
  if(!data) return false;
  if((data._v||0) <= (S[which]._v||0)) return false;
  const def = which==='student' ? DEF_STUDENT() : DEF_TUTOR();
  S[which] = Object.assign(def, data);
  lastJSON[which] = JSON.stringify(S[which]);
  saveLocal('p5-'+which, S[which]);
  return true;
}
async function initSync(){
  let db=null, user=null;
  try { if(window.claude && typeof window.claude.use==='function'){ [db, user] = await Promise.all([window.claude.use('db'), window.claude.use('user')]); } } catch(e){}
  try { if(user && await user.isOwner()) { role='tutor'; if(!location.hash) route='tutor'; } } catch(e){}
  if(!db){ setSync('Saved on this device only','local'); render(); return; }
  refs.student = db.doc('p5/student'); refs.tutor = db.doc('p5/tutor');
  try {
    for(const w of ['student','tutor']){
      const snap = await refs[w].get();
      const mine = (w==='student' && role!=='tutor') || (w==='tutor' && role==='tutor');
      if(snap.exists){
        const remote = snap.data();
        if(!adopt(w, remote) && mine && (S[w]._v||0) > (remote._v||0)) { await refs[w].set(S[w]); lastJSON[w]=JSON.stringify(S[w]); }
      } else if(mine && S[w]._v > 0){ await refs[w].set(S[w]); lastJSON[w]=JSON.stringify(S[w]); }
    }
    dbOK = true; setSync(role==='tutor' ? 'Synced · tutor view' : 'Synced','ok');
  } catch(e){ setSync('Saved on this device only','local'); render(); return; }
  for(const w of ['student','tutor']){
    refs[w].onSnapshot(snap => { if(snap.exists && adopt(w, snap.data())) softRender(); }, () => setSync('Saved on this device only','local'));
  }
  render();
}
// Never re-render under someone's cursor: wait until they leave the field.
let pendingRender=false;
function softRender(){
  const a=document.activeElement;
  if(a && (a.tagName==='INPUT'||a.tagName==='TEXTAREA'||a.tagName==='SELECT') && $('#main').contains(a)){ pendingRender=true; return; }
  render();
}
document.addEventListener('focusout', () => setTimeout(() => { if(pendingRender && !$('#main').contains(document.activeElement)){ pendingRender=false; render(); } }, 50));

// ---------- speech ----------
let ruVoice=null;
function loadVoices(){ try { const vs=speechSynthesis.getVoices(); ruVoice = vs.find(v=>/^ru/i.test(v.lang)) || null; } catch(e){} }
if('speechSynthesis' in window){ loadVoices(); speechSynthesis.onvoiceschanged = loadVoices; }
let warnedVoice=false;
function speak(t){
  if(!('speechSynthesis' in window)) return toast('This browser can\'t read aloud.');
  const u = new SpeechSynthesisUtterance(String(t).replace(STRESS,'').replace(/…/g,''));
  u.lang='ru-RU'; u.rate=.85; if(ruVoice) u.voice=ruVoice;
  speechSynthesis.cancel(); speechSynthesis.speak(u);
  if(!ruVoice && !warnedVoice){ warnedVoice=true; setTimeout(()=>{ loadVoices(); if(!ruVoice) toast('No Russian voice found on this device. Add one in your system language settings for real pronunciation.'); }, 600); }
}
const SPK = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/><path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg>';
const spkBtn = t => `<button class="spk" data-say="${esc(t)}" aria-label="Hear it">${SPK}</button>`;

function toast(msg){ const t=document.createElement('div'); t.className='toast'; t.textContent=msg; document.body.appendChild(t); setTimeout(()=>t.remove(), 3200); }

// ---------- progress maths ----------
function mastery(L){ const ws=WORDS.filter(w=>w.L===L); if(!ws.length) return 0; const r=P().srs; return ws.filter(w => r[w.id] && r[w.id][0]>=3).length / ws.length; }
function seenShare(L){ const ws=WORDS.filter(w=>w.L===L); const r=P().srs; return ws.filter(w=>r[w.id]).length/ws.length; }
function lessonReady(L, rec=P()){
  const q=rec.quiz[L]?.best||0, d=rec.drill[L]?.best||0;
  const ws=WORDS.filter(w=>w.L===L); const m = ws.filter(w => rec.srs[w.id] && rec.srs[w.id][0]>=3).length/ws.length;
  return .4*q + .3*d + .3*m;
}
function overall(rec=P()){ const sc=T().scope; if(!sc.length) return 0; return sc.reduce((a,L)=>a+lessonReady(L,rec),0)/sc.length; }
function gradeFor(x){ return x>=.9?['5','A']:x>=.75?['4','B']:x>=.6?['3','C']:['2','not yet']; }
function dueCards(){
  const r=P().srs, today=dayNum();
  return WORDS.filter(w => inScope(w.L) && r[w.id] && r[w.id][1] <= today);
}
function newCards(onlyL){
  const r=P().srs, t=todayStr();
  const left = Math.max(0, (T().newPerDay||15) - (P().newLog[t]||0));
  return WORDS.filter(w => (onlyL ? w.L===onlyL : inScope(w.L)) && !r[w.id]).slice(0, onlyL ? 20 : left);
}
function daysLeft(){ return dayNum(EXAM_DATE) - dayNum(); }
function thisWeek(){ const t=todayStr(); const ws=[...T().weeks].sort((a,b)=>a.d<b.d?-1:1); let cur=null; for(const w of ws){ if(w.d<=t) cur=w; } return cur || ws[0] || {d:todayStr(), f:'No plan set yet'}; }
function touchStreak(){
  const rec=P(), t=todayStr(); if(rec.streak.last===t) return;
  const y = new Date(Date.now()-864e5); const ys = y.getFullYear()+'-'+String(y.getMonth()+1).padStart(2,'0')+'-'+String(y.getDate()).padStart(2,'0');
  rec.streak = {last:t, n: rec.streak.last===ys ? rec.streak.n+1 : 1};
}
function logMistake(src, q, given, right){
  const rec=P();
  const key = norm(q).slice(0,80);
  const ex = rec.mistakes.find(m => m.key===key);
  if(ex){ ex.n=(ex.n||1)+1; ex.given=given; ex.ts=Date.now(); }
  else rec.mistakes.unshift({key, src, q, given, right, ts:Date.now(), n:1});
  rec.mistakes = rec.mistakes.slice(0,150);
}

// ---------- routing ----------
let route = (location.hash||'#home').slice(1) || 'home';
let lessonTab = ui.lessonTab || 'grammar';
function go(r){ route=r; if(location.hash.slice(1)!==r) history.replaceState(null,'','#'+r); render(); $('#main').focus({preventScroll:true}); window.scrollTo({top:0}); }
window.addEventListener('hashchange', () => { const r=location.hash.slice(1)||'home'; if(r!==route){ route=r; render(); } });

// ---------- nav ----------
function renderNav(){
  const rec=P(); const due=dueCards().length;
  const item = (r, n, t, meta, extra='') => `<button class="nav ${route===r||route.startsWith(r+':')?'on':''} ${extra}" data-go="${r}">${n}<span class="nav-body"><span class="nav-t">${t}</span>${meta?`<span class="nav-meta">${meta}</span>`:''}</span></button>`;
  let h='';
  if(role==='tutor'){
    h += `<div class="nav-label">Tutor</div>`;
    h += item('tutor','<span class="nav-n">T</span>','Tutor desk', subsCount()? subsCount()+' to grade':'plan · progress · feedback');
    h += `<button class="nav" data-act="preview"><span class="nav-n">${preview?'✓':'S'}</span><span class="nav-body"><span class="nav-t">${preview?'Hide student pages':'Student pages'}</span><span class="nav-meta">your practice here isn't saved</span></span></button>`;
    if(!preview){ $('#nav').innerHTML=h; return; }
  }
  h += `<div class="nav-label">Today</div>`;
  h += item('home','<span class="nav-n">★</span>','Home', daysLeft()+' days to the exam');
  h += item('cards','<span class="nav-n">✦</span>','Flashcards', due? due+' due now':'up to date');
  h += `<div class="nav-label">Lektionen</div>`;
  LESSONS.forEach(l => {
    const r = lessonReady(l.n); const done = r>=.85;
    h += item('l'+l.n, `<span class="nav-n ${done?'done':''}">${l.n}</span>`, l.ru, inScope(l.n)? (pct(r)+'% ready') : 'not on the exam', inScope(l.n)?'':'out');
  });
  h += `<div class="nav-label">Exam</div>`;
  h += item('mock','<span class="nav-n">✎</span>','Mock exam', rec.mocks.length? 'best '+pct(Math.max(...rec.mocks.map(m=>m.score/m.max)))+'%':'timed, like the real thing');
  h += item('mistakes','<span class="nav-n">!</span>','Mistake log', rec.mistakes.length? rec.mistakes.length+' to fix':'empty');
  h += item('abc','<span class="nav-n">А</span>','Alphabet','33 letters, sounds, traps');
  h += item('german','<span class="nav-n">DE</span>','Exam German','instructions + grammar terms');
  $('#nav').innerHTML = h;
}
function subsCount(){ const st=S.student, fb=T().fb; return Object.keys(st.writing||{}).filter(k => !fb[k] || fb[k].ts < st.writing[k].ts).length; }

// ---------- views ----------
function render(){
  renderNav();
  const m = $('#main');
  if(role==='tutor' && !preview && route!=='tutor') route='tutor';
  let h='';
  if(route==='tutor' && role==='tutor') h=vTutor();
  else if(route==='home') h=vHome();
  else if(route==='cards') h=vCards();
  else if(/^l\d/.test(route)) h=vLesson(+route[1]);
  else if(route==='mock') h=vMock();
  else if(route==='mistakes') h=vMistakes();
  else if(route==='abc') h=vAbc();
  else if(route==='german') h=vGerman();
  else { route='home'; h=vHome(); }
  const banner = role==='tutor' && route!=='tutor' ? `<div class="chip a" style="margin-bottom:14px">Student preview · your answers here aren't saved to her record</div>` : '';
  m.innerHTML = banner + h;
  afterRender();
}
function afterRender(){
  if(route==='cards') mountCard();
  if(route==='mock' && mock.on) tickTimer();
}

// ----- home -----
function vHome(){
  const rec=P(), T_=T(), dl=daysLeft(), wk=thisWeek(), due=dueCards().length, nw=newCards().length;
  const ov=overall(), [g,letter]=gradeFor(ov);
  const next = LESSONS.find(l => inScope(l.n) && lessonReady(l.n) < .85);
  const hw = T_.homework.filter(x=>!rec.hw[x.id]);
  let h = '';
  if(!ui.introSeen && role!=='tutor') h += `<div class="card" style="margin-bottom:16px"><h3>Привет! This is your Russian platform.</h3>
    <p class="muted">It follows your course book, <b>Jasno! neu</b>, Lektion 1–9. Every lesson has the grammar in plain English (with the German terms your class uses), the book's vocabulary with stress marks, the workbook self-test, and typing drills. Click any <i class="ru">blue Russian</i> to hear it. Your progress syncs, so your tutor can see what to work on with you.</p>
    <button class="btn sm" data-act="intro-ok">Got it</button></div>`;
  h += `<div class="hero">
    <div class="count num">${Math.max(dl,0)}<small>${dl>0?'days until the A1 exam':'exam day has passed'}<br><b>Wed 16 Dec 2026</b></small></div>
    <div class="stack" style="gap:8px">
      <div class="eyebrow">This week · from ${fmtDate(wk.d)}</div>
      <div class="week">${esc(wk.f)}</div>
      <div class="row" style="margin-top:6px">
        <span class="chip ${ov>=.75?'g':ov>=.5?'a':'r'}">Readiness ${pct(ov)}%</span>
        <span class="chip">${ov>=.6?`on track for a ${g} (${letter})`:'keep going: the grade estimate starts at 60%'}</span>
        ${rec.streak.n>1?`<span class="chip b">${rec.streak.n}-day streak</span>`:''}
      </div>
    </div></div>`;
  h += `<div class="grid2" style="margin-top:16px">`;
  h += `<div class="card"><h3>Today</h3><div class="todo">
    <div class="todo-i"><div class="t"><b>${due}</b> flashcards due${nw?` · <b>${nw}</b> new`:''}<div class="faint" style="font-size:13px">10 minutes a day beats 2 hours on Sunday.</div></div><button class="btn sm" data-go="cards" ${due+nw?'':'disabled'}>${due+nw?'Start':'Done ✓'}</button></div>
    ${next?`<div class="todo-i"><div class="t">Next up: <b>Lektion ${next.n}</b> · ${esc(next.en)}<div class="faint" style="font-size:13px">${pct(lessonReady(next.n))}% ready · ${nextStep(next.n)}</div></div><button class="btn sm ghost" data-go="l${next.n}">Open</button></div>`:''}
    ${rec.mistakes.length?`<div class="todo-i"><div class="t"><b>${rec.mistakes.length}</b> ${rec.mistakes.length===1?'mistake':'mistakes'} waiting in your log</div><button class="btn sm ghost" data-go="mistakes">Fix</button></div>`:''}
    ${hw.map(x=>`<div class="todo-i"><div class="t"><span class="chip r">Homework</span> ${esc(x.text)}${x.due?`<div class="faint" style="font-size:13px">due ${fmtDate(x.due)}</div>`:''}</div><button class="btn sm ghost" data-act="hw-done" data-id="${x.id}">Done</button></div>`).join('')}
  </div></div>`;
  h += `<div class="stack">`;
  if(T_.note) h += `<div class="note"><div class="eyebrow" style="color:var(--red)">From your tutor</div><div class="hand">${esc(T_.note)}</div></div>`;
  const fbNew = Object.entries(T_.fb).filter(([k,f]) => f.ts > (ui.fbSeen||0));
  if(fbNew.length) h += `<div class="card"><h3>New feedback on your writing</h3>${fbNew.map(([k,f])=>`<div class="row" style="margin-bottom:6px"><span class="grade" style="width:34px;height:34px;font-size:24px">${esc(f.grade||'✓')}</span><span>${esc(writingTitle(k))}</span><button class="btn sm ghost" data-go="${writingRoute(k)}">Read</button></div>`).join('')}</div>`;
  h += `<div class="card"><h3>Lessons on the exam</h3><div class="ready">${LESSONS.map(l=>{const r=lessonReady(l.n);return `<button class="rl ${inScope(l.n)?'':'out'}" data-go="l${l.n}"><div class="n">L${l.n}</div><div class="p num" style="color:${r>=.85?'var(--green)':r>=.5?'var(--ink)':'var(--ink-faint)'}">${pct(r)}%</div><div class="bar"><i style="width:${pct(r)}%;background:${r>=.85?'var(--green)':'var(--blue)'}"></i></div></button>`}).join('')}</div>
    <p class="faint" style="font-size:13px;margin:10px 0 0">Readiness = 40% self-test + 30% drills + 30% words you know solidly.${T_.classAt?` Your class is at Lektion ${T_.classAt}.`:''}</p></div>`;
  h += `</div></div>`;
  return h;
}
function nextStep(L){ const rec=P(); if(!rec.read[L]) return 'start with the grammar'; if(!rec.quiz[L]) return 'take the self-test'; if(!rec.drill[L]) return 'do the drill'; if(mastery(L)<.6) return 'learn the words'; return 'retake what\'s weakest'; }
function writingTitle(k){ if(k.startsWith('mock-')) return 'Mock exam writing, '+new Date(+k.slice(5)).toLocaleDateString('en-US',{month:'short',day:'numeric'}); const l=LESSONS.find(l=>l.write&&l.write.id===k); return l?`Lektion ${l.n} writing task`:k; }
function writingRoute(k){ if(k.startsWith('mock-')) return 'mock'; const l=LESSONS.find(l=>l.write&&l.write.id===k); return l?'l'+l.n+':write':'home'; }

// ----- lesson -----
function vLesson(n){
  const l = LESSONS.find(x=>x.n===n); const rec=P();
  if(route.includes(':')) { lessonTab = route.split(':')[1]; route='l'+n; }
  const tabs = [['grammar','Grammar'],['words','Words'],['quiz','Self-test'],['drill','Drill']].concat(l.write?[['write','Writing']]:[]);
  if(!tabs.some(t=>t[0]===lessonTab)) lessonTab='grammar';
  const q=rec.quiz[n], d=rec.drill[n];
  let h = `<div class="ph"><div><div class="eyebrow">Lektion ${n} · ${esc(l.kb)}${inScope(n)?'':' · not on the exam'}</div>
    <h1 class="title"><i class="ru" style="color:inherit">${esc(l.ru)}</i></h1><div class="title-en">${esc(l.en)}</div></div>
    <div class="tabs" role="tablist">${tabs.map(([k,t])=>`<button class="tab ${lessonTab===k?'on':''}" data-tab="${k}" role="tab" aria-selected="${lessonTab===k}">${t}</button>`).join('')}</div></div>
  <div class="row" style="margin:-8px 0 18px">
    <span class="chip ${rec.read[n]?'g':''}">${rec.read[n]?'Grammar read ✓':'Grammar not read'}</span>
    <span class="chip ${q?(q.best>=.85?'g':'a'):''}">Self-test ${q?pct(q.best)+'%':'—'}</span>
    <span class="chip ${d?(d.best>=.85?'g':'a'):''}">Drill ${d?pct(d.best)+'%':'—'}</span>
    <span class="chip ${mastery(n)>=.85?'g':''}">Words ${pct(mastery(n))}% solid</span>
  </div>`;
  if(lessonTab==='grammar') h += `<div class="sheet"><div class="eyebrow">By the end you can</div><ul class="cando">${l.can.map(c=>`<li>${esc(c)}</li>`).join('')}</ul><hr style="border:0;border-top:1px solid var(--line);margin:18px 0"><div class="gram">${wrapTables(l.grammar)}</div>
    <div class="row" style="justify-content:flex-end;margin-top:20px">${rec.read[n]?'<span class="chip g">Read ✓</span>':''}<button class="btn" data-act="read" data-l="${n}">${rec.read[n]?'Next: self-test →':'I\'ve read it → self-test'}</button></div></div>`;
  if(lessonTab==='words') h += vWords(n);
  if(lessonTab==='quiz') h += vQuiz(l);
  if(lessonTab==='drill') h += vDrill(l);
  if(lessonTab==='write') h += vWrite(l.write, `Lektion ${n}`);
  return h;
}
const wrapTables = html => html.replace(/<table class="gt">/g,'<div class="tbl-wrap"><table class="gt">').replace(/<\/table>/g,'</table></div>');
function vWords(n){
  const ws=WORDS.filter(w=>w.L===n), r=P().srs;
  return `<div class="sheet"><div class="row" style="justify-content:space-between;margin-bottom:12px"><p class="muted" style="margin:0">${ws.length} words the book marks as <b>Lernwortschatz</b> (to learn). The accent shows the stressed vowel. Dots = how solid you know it.</p>
    <button class="btn" data-act="study-lesson" data-l="${n}">Study these as flashcards</button></div>
    <div class="tbl-wrap"><table class="words"><thead><tr><th>Russian</th><th>English</th><th>German</th><th>Notes</th><th></th></tr></thead><tbody>
    ${ws.map(w=>{const b=r[w.id]?r[w.id][0]:0; return `<tr><td class="w"><i class="ru" data-say="${esc(w.ru)}">${esc(w.ru)}</i></td><td>${esc(w.en)}</td><td class="faint">${esc(w.de)}</td><td class="faint" style="font-size:13.5px">${esc(w.x)}</td><td><span class="box-dots" title="level ${b} of 5">${[1,2,3,4,5].map(i=>`<i class="${b>=i?'on':''}"></i>`).join('')}</span></td></tr>`}).join('')}
    </tbody></table></div></div>`;
}

// quiz: answers are kept in memory until the whole test is done
const quizRun = {};
function vQuiz(l){
  const run = quizRun[l.n] || (quizRun[l.n] = {ans:{}});
  const done = Object.keys(run.ans).length, total=l.quiz.length;
  let h = `<div class="sheet"><p class="muted">From the workbook (<b>Что правильно?</b>, end of the lesson). Pick the right form. You get the reason right after each answer.</p>
    <div class="row" style="margin-bottom:14px"><div class="bar" style="flex:1"><i style="width:${done/total*100}%"></i></div><span class="num faint">${done} / ${total}</span></div>`;
  h += l.quiz.map((q,i)=>{
    const a = run.ans[i];
    return `<div class="q"><div class="q-n">${i+1}</div><div class="q-p">${ruify(q[0])}</div><div class="opts">${q[1].map((o,j)=>{
      let c=''; if(a!==undefined){ if(j===q[2]) c='ok'; else if(j===a) c='bad'; }
      return `<button class="opt ${c}" data-act="qa" data-l="${l.n}" data-i="${i}" data-j="${j}" ${a!==undefined?'disabled':''}>${esc(o)}</button>`;}).join('')}</div>
      ${a!==undefined?`<div class="why">${a===q[2]?'<b style="color:var(--green)">Right.</b>':'<b style="color:var(--red)">Not quite.</b>'} ${esc(q[3])}</div>`:''}</div>`;
  }).join('');
  if(done===total){
    const sc = l.quiz.filter((q,i)=>run.ans[i]===q[2]).length;
    h += `<div class="score"><span class="big num">${sc}/${total}</span><span class="grade">${gradeFor(sc/total)[0]}</span><span class="muted">${sc===total?'Perfect. Move on to the drill.':sc/total>=.85?'Solid. Check the red ones, then the drill.':'Re-read the grammar box for the ones you missed, then retake.'}</span><button class="btn ghost" data-act="q-reset" data-l="${l.n}">Retake</button></div>`;
  }
  return h+'</div>';
}
function ruify(s){ // wrap Cyrillic runs so they are clickable/speakable, keep existing tags
  if(/<i class="ru">/.test(s)) return s;
  return s.split(/(<[^>]+>)/).map(p => p.startsWith('<') ? p : p.replace(/([А-Яа-яЁё][А-Яа-яЁё́\- ,…!?–—.]*[А-Яа-яЁё.!?…])/g, m=>`<i class="ru">${m}</i>`)).join('');
}

// drill
const drillRun = {};
function vDrill(l){
  const run = drillRun[l.n] || (drillRun[l.n] = {val:{}, checked:false});
  let h = `<div class="sheet"><p class="muted">Type the answer in Cyrillic. Stress marks don't matter, ё = е is fine. No Russian keyboard? Use the <b>АБВ keyboard</b> button at the bottom right.</p>`;
  h += l.drill.map((d,i)=>{
    const v = run.val[i]||''; const ok = run.checked && isRight(v, d[1]);
    return `<div class="dr"><div>${ruify(esc(d[0]))}</div><input class="input" lang="ru" autocomplete="off" autocapitalize="off" spellcheck="false" id="dr-${l.n}-${i}" data-drill="${l.n}" data-i="${i}" value="${esc(v)}" ${run.checked?'readonly':''}>
      <span class="mark ${run.checked?(ok?'ok':'bad'):''}">${run.checked?(ok?'✓':'✗'):''}</span>
      ${run.checked&&!ok?`<div class="fix">→ ${esc(answers(d[1])[0])}</div>`:''}</div>`;
  }).join('');
  if(!run.checked) h += `<div class="row" style="justify-content:flex-end;margin-top:16px"><button class="btn" data-act="d-check" data-l="${l.n}">Check answers</button></div>`;
  else { const sc=l.drill.filter((d,i)=>isRight(run.val[i]||'',d[1])).length;
    h += `<div class="score"><span class="big num">${sc}/${l.drill.length}</span><span class="grade">${gradeFor(sc/l.drill.length)[0]}</span><span class="muted">Wrong answers went to your mistake log.</span><button class="btn ghost" data-act="d-reset" data-l="${l.n}">Try again</button></div>`; }
  return h+'</div>';
}

// writing (lesson tasks and mock exam)
function vWrite(w, label){
  const rec=S.student, sub=rec.writing[w.id], fb=T().fb[w.id];
  const draftKey='p5-draft-'+w.id; let draft=''; try{ draft=localStorage.getItem(draftKey)||''; }catch(e){}
  const text = draft || (sub?sub.text:'');
  const words = text.trim()? text.trim().split(/\s+/).length : 0;
  let h = `<div class="sheet"><div class="eyebrow">${esc(label)} · writing task</div><p style="font-size:17px">${esc(w.prompt)}</p>
   <p class="faint" style="font-size:14px">Aim for about ${w.words} words. The exam will have a task like this. Write in Russian; your tutor corrects it in red.</p>
   <textarea class="ta" id="wr-${w.id}" data-write="${w.id}" lang="ru" placeholder="Пишите здесь…">${esc(text)}</textarea>
   <div class="row" style="justify-content:space-between;margin-top:10px"><span class="faint num" id="wc-${w.id}">${words} words</span>
   <button class="btn" data-act="submit-write" data-id="${w.id}" ${role==='tutor'?'disabled title="Only the student submits"':''}>${sub?'Resubmit to tutor':'Submit to tutor'}</button></div>`;
  if(sub) h += `<p class="faint" style="font-size:13px;margin-top:8px">Submitted ${new Date(sub.ts).toLocaleString('en-US',{month:'short',day:'numeric',hour:'numeric',minute:'2-digit'})}.</p>`;
  if(fb){ h += `<div class="fb"><div class="row"><span class="grade">${esc(fb.grade||'✓')}</span><div class="eyebrow" style="color:var(--red);margin:0">Tutor's corrections</div></div><div class="hand" style="font-size:23px;white-space:pre-wrap;margin-top:8px">${esc(fb.text)}</div></div>`;
    if(fb.ts > (ui.fbSeen||0)){ ui.fbSeen=Date.now(); saveUi(); } }
  return h+'</div>';
}

// ----- flashcards -----
let deck=null; // {cards:[id], i, mode, reveal, stats, lesson}
function buildDeck(lesson){
  const due = lesson ? WORDS.filter(w=>w.L===lesson && P().srs[w.id] && P().srs[w.id][1]<=dayNum()) : dueCards();
  const fresh = newCards(lesson);
  deck = {cards: shuffle(due.map(w=>w.id)).concat(fresh.map(w=>w.id)), i:0, reveal:false, stats:{ok:0,bad:0}, lesson, mode: ui.cardMode||'rec'};
}
function vCards(){
  if(!deck) buildDeck(null);
  const total=deck.cards.length;
  let h = `<div class="ph"><div><div class="eyebrow">Spaced repetition${deck.lesson?` · Lektion ${deck.lesson}`:' · all lessons on the exam'}</div><h1 class="title">Flashcards</h1></div>
    <div class="tabs"><button class="tab ${deck.mode==='rec'?'on':''}" data-act="cmode" data-m="rec">Russian → English</button><button class="tab ${deck.mode==='pro'?'on':''}" data-act="cmode" data-m="pro">English → Russian (type)</button></div></div>`;
  h += `<div class="fc-wrap"><div class="stat-row"><span class="chip">${Math.min(deck.i,total)} / ${total}</span><span class="chip g">${deck.stats.ok} knew</span><span class="chip r">${deck.stats.bad} again</span></div><div id="fc"></div>
    <p class="faint" style="font-size:13px;text-align:center;margin-top:14px">Cards you know come back after 1, 3, 7, 14, then 30 days. Cards you miss come back in this session. ${T().newPerDay} new cards a day.</p></div>`;
  return h;
}
function mountCard(){
  const el=$('#fc'); if(!el) return;
  if(deck.i>=deck.cards.length){
    el.innerHTML = `<div class="fc"><div class="front en">${deck.cards.length?'Done for now.':'Nothing due right now.'}</div><div class="meta">${deck.cards.length?`${deck.stats.ok} right, ${deck.stats.bad} to repeat. Come back tomorrow.`:'New cards unlock each day. You can also study a single lesson from its Words tab.'}</div>
    <div class="fc-actions"><button class="btn ghost" data-go="home">Home</button>${deck.lesson?'':`<button class="btn ghost" data-act="deck-more">Practice any 20 words</button>`}</div></div>`;
    return;
  }
  const w = WORD[deck.cards[deck.i]]; const isNew = !P().srs[w.id];
  const tag = `<span class="lesson-tag">L${w.L}${isNew?' · new':''}</span>`;
  if(deck.mode==='rec'){
    el.innerHTML = `<div class="fc">${tag}<div class="front"><i class="ru" data-say="${esc(w.ru)}" style="color:inherit">${esc(w.ru)}</i> ${spkBtn(w.ru)}</div>
      ${deck.reveal?`<div class="back"><div class="a">${esc(w.en)}</div><div class="meta">${esc(w.de)}${w.x?' · '+esc(w.x):''}</div></div>`:''}</div>
      <div class="fc-actions">${deck.reveal?`<button class="btn red" data-act="card" data-ok="0">Again</button><button class="btn" data-act="card" data-ok="1" style="background:var(--green)">I knew it</button>`:`<button class="btn" data-act="reveal" id="reveal-btn">Show answer</button>`}</div>`;
    if(!deck.reveal && ui.autoSay) speak(w.ru);
  } else {
    el.innerHTML = `<div class="fc">${tag}<div class="front en">${esc(w.en)}</div><div class="meta">${w.x&&!/[а-яё]/i.test(w.x)?esc(w.x):''}</div>
      ${deck.reveal?`<div class="back"><div class="a"><i class="ru" data-say="${esc(w.ru)}">${esc(w.ru)}</i></div><div class="meta">${deck.last?'<span style="color:var(--green);font-weight:700">Correct</span>':`<span style="color:var(--red);font-weight:700">You wrote: ${esc(deck.typed||'(nothing)')}</span>`}</div></div>`
      :`<input class="input" id="fc-in" lang="ru" autocomplete="off" autocapitalize="off" spellcheck="false" style="text-align:center;font-size:22px;margin-top:8px" placeholder="по-русски…">`}</div>
      <div class="fc-actions">${deck.reveal?`<button class="btn" data-act="next-card" id="next-btn">Next</button>`:`<button class="btn ghost" data-act="pro-check" data-skip="1">I don't know</button><button class="btn" data-act="pro-check">Check</button>`}</div>`;
    const inp=$('#fc-in'); if(inp) inp.focus();
    else $('#next-btn')?.focus();
  }
}
function grade(ok){
  const w = WORD[deck.cards[deck.i]], rec=P(), cur=rec.srs[w.id];
  if(!cur){ const t=todayStr(); rec.newLog = {[t]:(rec.newLog[t]||0)+1}; }
  if(ok){ const b=Math.min(5,(cur?cur[0]:0)+1); rec.srs[w.id]=[b, dayNum()+SRS_DAYS[b]]; deck.stats.ok++; }
  else { rec.srs[w.id]=[1, dayNum()]; deck.stats.bad++; deck.cards.push(w.id); if(deck.mode==='pro') logMistake('Flashcards', w.en, deck.typed||'', w.ru); }
  touchStreak(); save('student');
}

// ----- mock exam -----
const mock = {on:false};
function buildMock(){
  const sc=T().scope, maxL=Math.max(...sc);
  const readings = READINGS.filter(r => r.lessons.every(L=>L<=maxL) && r.lessons.some(L=>sc.includes(L)));
  const qpool = shuffle(LESSONS.filter(l=>sc.includes(l.n)).flatMap(l=>l.quiz.map(q=>({L:l.n,q})))).slice(0,15);
  const dpool = shuffle(LESSONS.filter(l=>sc.includes(l.n)).flatMap(l=>l.drill.map(d=>({L:l.n,d})))).slice(0,10);
  const wpool = LESSONS.filter(l=>sc.includes(l.n) && l.write).map(l=>l.write);
  const w = wpool.length ? wpool[Math.floor(Math.random()*wpool.length)] : null;
  Object.assign(mock, {on:true, start:Date.now(), mins:60, readings:shuffle(readings).slice(0,2), qpool, dpool, w, ra:{}, qa:{}, da:{}, wtext:'', done:false});
}
function vMock(){
  const rec=P();
  if(!mock.on){
    let h = `<div class="ph"><div><div class="eyebrow">Practice under exam conditions</div><h1 class="title">Mock exam</h1></div></div>
    <div class="sheet"><p style="font-size:17px">60 minutes, closed book, no dictionary. Four parts, drawn fresh each time from the lessons on the exam (${T().scope.length? 'Lektion '+T().scope.join(', '):'none selected'}):</p>
    <ol class="cando" style="font-size:16px"><li><b>Reading</b>: short texts, richtig oder falsch</li><li><b>Grammar</b>: 15 multiple-choice gaps</li><li><b>Forms</b>: 10 typed answers</li><li><b>Writing</b>: one short text, graded by your tutor</li></ol>
    <p class="muted" style="margin-top:10px">Parts 1–3 are scored instantly. Do the first one around Lektion 6, then one every week in December.</p>
    <button class="btn" data-act="mock-start" ${T().scope.length?'':'disabled'}>Start the 60-minute mock</button></div>`;
    if(rec.mocks.some(m=>(T().fb['mock-'+m.ts]?.ts||0)>(ui.fbSeen||0))){ ui.fbSeen=Date.now(); saveUi(); }
    if(rec.mocks.length) h += `<div class="card" style="margin-top:16px"><h3>Past attempts</h3><table class="stats"><thead><tr><th>Date</th><th>Score</th><th>Grade</th><th>Writing</th></tr></thead><tbody>${rec.mocks.slice().reverse().map(m=>{const f=T().fb['mock-'+m.ts];return `<tr><td>${new Date(m.ts).toLocaleDateString('en-US',{month:'short',day:'numeric'})}</td><td class="num">${m.score}/${m.max} (${pct(m.score/m.max)}%)</td><td><span class="chip ${m.score/m.max>=.75?'g':'a'}">${gradeFor(m.score/m.max)[0]}</span></td><td>${f?`<span class="hand" style="font-size:20px">${esc(f.grade||'✓')}</span> ${esc(f.text).slice(0,80)}${f.text.length>80?'…':''}`:(S.student.writing['mock-'+m.ts]?'<span class="faint">waiting for tutor</span>':'—')}</td></tr>`}).join('')}</tbody></table></div>`;
    return h;
  }
  let h = `<div class="ph"><div><div class="eyebrow">Mock exam · Lektion ${T().scope.join(', ')}</div><h1 class="title">Контрольная работа</h1></div><div class="timer num" id="timer"></div></div><div class="sheet">`;
  if(mock.readings.length){ h+=`<div class="part-h">Teil 1 · Lesen Sie den Text. Richtig oder falsch?</div>`;
    mock.readings.forEach(r=>{ h+=`<div class="reading">${ruify(esc(r.text))}</div>` + r.items.map((it,i)=>{const k=r.id+i, a=mock.ra[k];
      const cls = v => mock.done ? (v===it[1]?'ok':(a===v?'bad':'')) : (a===v?'ok':'');
      return `<div class="tf"><span class="t">${esc(it[0])}</span><button class="opt ${cls(true)}" data-act="m-r" data-k="${k}" data-v="1" ${mock.done?'disabled':''}>richtig</button><button class="opt ${cls(false)}" data-act="m-r" data-k="${k}" data-v="0" ${mock.done?'disabled':''}>falsch</button></div>`}).join(''); }); }
  h += `<div class="part-h">Teil 2 · Wählen Sie die richtige Antwort.</div>`;
  h += mock.qpool.map(({L,q},i)=>{const a=mock.qa[i]; return `<div class="q"><div class="q-n">${i+1} · L${L}</div><div class="q-p">${ruify(q[0])}</div><div class="opts">${q[1].map((o,j)=>{let c=''; if(mock.done){ if(j===q[2]) c='ok'; else if(j===a) c='bad'; } else if(a===j) c='ok'; return `<button class="opt ${c}" data-act="m-q" data-i="${i}" data-j="${j}" ${mock.done?'disabled':''}>${esc(o)}</button>`}).join('')}</div>${mock.done&&a!==q[2]?`<div class="why">${esc(q[3])}</div>`:''}</div>`}).join('');
  h += `<div class="part-h">Teil 3 · Setzen Sie die richtige Form ein.</div>`;
  h += mock.dpool.map(({L,d},i)=>{const v=mock.da[i]||'', ok=isRight(v,d[1]); return `<div class="dr"><div>${ruify(esc(d[0]))}</div><input class="input" id="md-${i}" data-mdrill="${i}" lang="ru" autocomplete="off" autocapitalize="off" spellcheck="false" value="${esc(v)}" ${mock.done?'readonly':''}><span class="mark ${mock.done?(ok?'ok':'bad'):''}">${mock.done?(ok?'✓':'✗'):''}</span>${mock.done&&!ok?`<div class="fix">→ ${esc(answers(d[1])[0])}</div>`:''}</div>`}).join('');
  if(mock.w){ h += `<div class="part-h">Teil 4 · Schreiben Sie einen Text.</div><p style="font-size:16.5px">${esc(mock.w.prompt)}</p><textarea class="ta" id="m-write" data-mwrite="1" lang="ru" ${mock.done?'readonly':''}>${esc(mock.wtext)}</textarea>`; }
  if(!mock.done) h += `<div class="row" style="justify-content:space-between;margin-top:18px"><button class="btn ghost" data-act="mock-quit">Abandon</button><button class="btn" data-act="mock-submit">Hand in</button></div>`;
  else { const r=mock.result; h += `<div class="score"><span class="big num">${r.score}/${r.max}</span><span class="grade">${gradeFor(r.score/r.max)[0]}</span><span class="muted">Parts 1–3 (${pct(r.score/r.max)}%). ${mock.w?'Your writing went to your tutor.':''} Weakest: ${r.weak||'—'}</span><button class="btn ghost" data-act="mock-close">Close</button></div>`; }
  return h+'</div>';
}
let timerInt=null;
function tickTimer(){
  clearInterval(timerInt);
  const upd=()=>{ const el=$('#timer'); if(!el||!mock.on||mock.done){ clearInterval(timerInt); if(el&&mock.done) el.textContent=''; return; } const left=mock.start+mock.mins*6e4-Date.now(); const m=Math.max(0,Math.floor(left/6e4)), s=Math.max(0,Math.floor(left/1e3)%60); el.textContent=`${m}:${String(s).padStart(2,'0')} left`; el.style.color=left<5*6e4?'var(--red)':''; };
  upd(); timerInt=setInterval(upd,1000);
}
function submitMock(){
  let score=0, max=0; const byL={};
  const add=(L,ok)=>{ byL[L]=byL[L]||[0,0]; byL[L][1]++; if(ok) byL[L][0]++; };
  mock.readings.forEach(r=>r.items.forEach((it,i)=>{ max++; const ok=mock.ra[r.id+i]===it[1]; if(ok) score++; add(Math.max(...r.lessons),ok); }));
  mock.qpool.forEach(({L,q},i)=>{ max++; const ok=mock.qa[i]===q[2]; if(ok) score++; else logMistake('Mock · L'+L, q[0].replace(/<[^>]+>/g,' '), q[1][mock.qa[i]]??'(blank)', q[1][q[2]]); add(L,ok); });
  mock.dpool.forEach(({L,d},i)=>{ max++; const ok=isRight(mock.da[i]||'',d[1]); if(ok) score++; else logMistake('Mock · L'+L, d[0], mock.da[i]||'(blank)', answers(d[1])[0]); add(L,ok); });
  const weak = Object.entries(byL).filter(([L,[a,b]])=>a/b<.7).map(([L])=>'Lektion '+L).join(', ');
  const ts=Date.now();
  const rec=P(); rec.mocks.push({ts, score, max, byL}); rec.mocks=rec.mocks.slice(-20);
  if(mock.w && mock.wtext.trim() && role!=='tutor') rec.writing['mock-'+ts]={text:mock.wtext, ts, prompt:mock.w.prompt};
  touchStreak(); save('student');
  mock.done=true; mock.result={score,max,weak};
}

// ----- mistakes -----
function vMistakes(){
  const rec=P();
  let h = `<div class="ph"><div><div class="eyebrow">Everything you got wrong, most recent first</div><h1 class="title">Mistake log</h1></div></div>`;
  if(!rec.mistakes.length) return h+`<div class="sheet"><p class="muted">Nothing here. Wrong answers from self-tests, drills, typed flashcards and mock exams collect here automatically.</p></div>`;
  h += `<div class="sheet"><p class="muted">Say the right answer out loud before you reveal it. Clear a mistake once you'd get it right tomorrow.</p>`;
  h += rec.mistakes.map((m,i)=>`<div class="q"><div class="q-n">${esc(m.src)}${m.n>1?` · missed ${m.n}×`:''}</div><div class="q-p">${ruify(esc(m.q))}</div>
    <div class="row"><span class="faint">You: <s style="color:var(--red)">${esc(m.given)}</s></span>
    <details><summary class="btn sm ghost" style="list-style:none;display:inline-block">Show answer</summary><div style="margin-top:6px;font-size:17px"><i class="ru" data-say="${esc(m.right)}">${esc(m.right)}</i></div></details>
    <button class="btn sm" data-act="mis-clear" data-i="${i}" style="margin-left:auto;background:var(--green)">Got it now</button></div></div>`).join('');
  return h+'</div>';
}

// ----- alphabet -----
const COGNATES = [['ресторан','restaurant'],['метро','metro'],['торт','cake'],['кафе','café'],['туалет','toilet'],['кофе','coffee'],['телефон','telephone'],['автобус','bus'],['шоколад','chocolate'],['музыка','music'],['компьютер','computer'],['менеджер','manager'],['журналист','journalist'],['инженер','engineer'],['футбол','soccer'],['спорт','sport'],['суши','sushi'],['сувенир','souvenir'],['теннис','tennis'],['лимон','lemon'],['банан','banana'],['велосипед','bicycle'],['машина','car'],['баскетбол','basketball'],['театр','theater'],['актёр','actor'],['секретарь','secretary'],['студент','student'],['банк','bank'],['музей','museum']];
let abcQ=null;
function newAbcQ(){ const [ru,en]=COGNATES[Math.floor(Math.random()*COGNATES.length)]; const opts=shuffle([en,...shuffle(COGNATES.filter(c=>c[1]!==en)).slice(0,3).map(c=>c[1])]); abcQ={ru,en,opts,a:null}; }
function vAbc(){
  if(!abcQ) newAbcQ();
  let h = `<div class="ph"><div><div class="eyebrow">Lektion 1–2 · 33 letters</div><h1 class="title">Alphabet</h1></div></div>
  <div class="stack"><div class="card"><h3>Read it: which word is this?</h3><div class="row" style="gap:16px"><span style="font-size:32px;font-weight:700"><i class="ru" data-say="${abcQ.ru}" style="color:inherit">${abcQ.ru}</i></span>${spkBtn(abcQ.ru)}</div>
  <div class="opts" style="margin-top:10px">${abcQ.opts.map(o=>{let c=''; if(abcQ.a){ if(o===abcQ.en) c='ok'; else if(o===abcQ.a) c='bad'; } return `<button class="opt ${c}" data-act="abc" data-v="${esc(o)}" ${abcQ.a?'disabled':''}>${esc(o)}</button>`}).join('')}</div>
  ${abcQ.a?`<div class="row" style="margin-top:10px"><span class="muted">${abcQ.a===abcQ.en?'Right!':'It\'s '+abcQ.en+'.'}</span><button class="btn sm" data-act="abc-next">Next word</button></div>`:''}</div>
  <p class="muted" style="margin:0">Red tiles are traps: letters that look like Latin letters but sound different. Tap a tile to hear the example.</p>
  <div class="abc">${ALPHABET.map(a=>`<button class="lt ${a[3]&&/Looks like|No English/.test(a[3])?'trap':''}" data-say="${esc(a[2])}"><div class="L">${a[0]}</div><div class="s">${esc(a[1])}</div><div class="x">${esc(a[2])}</div>${a[3]?`<div class="tr">${esc(a[3])}</div>`:''}</button>`).join('')}</div>
  <div class="card"><h3>Handwriting</h3><p class="muted" style="margin:0">Your workbook asks for answers <b>in Schreibschrift</b> (Russian cursive). Several cursive letters look nothing like print: <b>т</b> is written like an m, <b>д</b> like a g, <b>и</b> like a u. Practice the ÜB pages for Lektion 1–2 by hand. Typing here won't train that.</p></div></div>`;
  return h;
}

// ----- exam german -----
function vGerman(){
  return `<div class="ph"><div><div class="eyebrow">The exam paper is in German</div><h1 class="title">Exam German</h1></div></div>
  <div class="stack"><div class="sheet"><p class="muted">Misreading an instruction costs points even when your Russian is right. Here are the task instructions from your Kursbuch (p. 10) and the workbook, with English and the Russian version your teacher may say aloud.</p>
  <div class="tbl-wrap"><table class="words"><thead><tr><th>On the paper</th><th>Means</th><th>Russian</th></tr></thead><tbody>${EXAM_GERMAN.map(r=>`<tr><td><b>${esc(r[0])}</b></td><td>${esc(r[1])}</td><td><i class="ru">${esc(r[2])}</i></td></tr>`).join('')}</tbody></table></div></div>
  <div class="sheet"><h3 style="font-family:var(--f-display);font-size:16px;margin-bottom:10px">Grammar terms your teacher uses</h3>
  <div class="tbl-wrap"><table class="words"><tbody>${GERMAN_TERMS.map(r=>`<tr><td><b>${esc(r[0])}</b></td><td>${esc(r[1])}</td></tr>`).join('')}</tbody></table></div></div></div>`;
}

// ----- tutor desk -----
function vTutor(){
  const st=S.student, T_=T();
  const ov=overall(st);
  let h = `<div class="ph"><div><div class="eyebrow">Only you see this page</div><h1 class="title">Tutor desk</h1><div class="title-en">${daysLeft()} days to the exam · her readiness ${pct(ov)}% · streak ${st.streak.n||0} days</div></div></div>`;
  h += `<div class="grid2">`;
  // progress table
  h += `<div class="card" style="grid-column:1/-1"><h3>Her progress by lesson</h3><div class="tbl-wrap"><table class="stats"><thead><tr><th>Lektion</th><th>Grammar</th><th>Self-test</th><th>Drill</th><th>Words solid</th><th>Readiness</th></tr></thead><tbody>
    ${LESSONS.map(l=>{const q=st.quiz[l.n], d=st.drill[l.n]; const ws=WORDS.filter(w=>w.L===l.n); const m=ws.filter(w=>st.srs[w.id]&&st.srs[w.id][0]>=3).length/ws.length; const r=lessonReady(l.n,st);
      return `<tr style="${inScope(l.n)?'':'opacity:.45'}"><td><b>${l.n}</b> ${esc(l.ru)}</td><td>${st.read[l.n]?'✓':'—'}</td><td class="num">${q?pct(q.best)+'%'+(q.n>1?` <span class="faint">(${q.n}×)</span>`:''):'—'}</td><td class="num">${d?pct(d.best)+'%':'—'}</td><td class="num">${pct(m)}%</td><td><span class="chip ${r>=.85?'g':r>=.5?'a':'r'}">${pct(r)}%</span></td></tr>`}).join('')}
  </tbody></table></div>
  ${st.mocks.length?`<p style="margin:12px 0 0"><b>Mock exams:</b> ${st.mocks.map(m=>`${new Date(m.ts).toLocaleDateString('en-US',{month:'short',day:'numeric'})} <b>${pct(m.score/m.max)}%</b>`).join(' · ')}</p>`:'<p class="faint" style="margin:12px 0 0">No mock exams yet.</p>'}</div>`;
  // writing inbox
  const subs = Object.entries(st.writing||{}).sort((a,b)=>b[1].ts-a[1].ts);
  h += `<div class="card" style="grid-column:1/-1"><h3>Writing inbox</h3>${subs.length?subs.map(([k,s])=>{const f=T_.fb[k]; const fresh=!f||f.ts<s.ts;
    return `<div class="q"><div class="row" style="justify-content:space-between"><b>${esc(writingTitle(k))}</b>${fresh?'<span class="chip r">needs grading</span>':'<span class="chip g">graded</span>'}</div>
    ${s.prompt?`<p class="faint" style="font-size:14px;margin:6px 0">${esc(s.prompt)}</p>`:''}<div class="sub" style="margin-top:8px">${esc(s.text)}</div>
    <div class="fb"><div class="row" style="margin-bottom:8px"><span class="muted">Grade:</span>${['5','4','3','2','✓'].map(g=>`<button class="pill-btn ${(f?.grade||'')===g?'on':''}" data-act="fb-grade" data-k="${k}" data-g="${g}">${g}</button>`).join('')}<span class="faint" style="font-size:13px">5 = A · 4 = B · 3 = C · 2 = not yet</span></div>
    <textarea class="ta" style="min-height:90px" id="fb-${k}" data-fb="${k}" placeholder="Corrections and comments. Show up for her in red pen.">${esc(f?.text||'')}</textarea>
    <div class="row" style="justify-content:flex-end;margin-top:8px"><button class="btn red sm" data-act="fb-save" data-k="${k}">Send feedback</button></div></div></div>`}).join(''):'<p class="faint">Nothing submitted yet. Each lesson (2–9) has a writing task, and every mock exam ends with one.</p>'}</div>`;
  // note + homework
  h += `<div class="card"><h3>Note on her home page</h3><textarea class="ta" style="min-height:110px;font-family:var(--f-hand);font-size:22px;color:var(--red)" id="t-note" data-tnote="1" placeholder="Молодец! This week: у меня есть / нет…">${esc(T_.note)}</textarea><div class="row" style="justify-content:flex-end;margin-top:8px"><button class="btn red sm" data-act="note-save">Pin note</button></div></div>`;
  h += `<div class="card"><h3>Homework</h3><div class="todo">${T_.homework.map(x=>`<div class="todo-i"><div class="t">${esc(x.text)}${x.due?`<div class="faint" style="font-size:13px">due ${fmtDate(x.due)}</div>`:''}</div>${st.hw[x.id]?'<span class="chip g">done</span>':'<span class="chip">open</span>'}<button class="btn sm ghost" data-act="hw-del" data-id="${x.id}" aria-label="Remove">✕</button></div>`).join('')||'<p class="faint" style="margin:0">None assigned.</p>'}</div>
    <div class="row" style="margin-top:10px"><input class="input" id="hw-text" placeholder="e.g. Lektion 4 drill until 100%" style="flex:1"><input class="input" type="date" id="hw-due"><button class="btn sm" data-act="hw-add">Assign</button></div></div>`;
  // settings
  h += `<div class="card"><h3>Exam scope and pace</h3><p class="muted" style="font-size:14.5px">Tick the Lektionen her teacher says are on the 16 Dec exam. Flashcards, readiness and mock exams follow this.</p>
    <div class="row">${LESSONS.map(l=>`<label class="chip ${inScope(l.n)?'b':''}" style="cursor:pointer"><input type="checkbox" data-scope="${l.n}" ${inScope(l.n)?'checked':''} style="margin:0 4px 0 0">L${l.n}</label>`).join('')}</div>
    <div class="row" style="margin-top:12px"><label>Her class is at Lektion <select class="input" id="t-class" data-tset="classAt">${LESSONS.map(l=>`<option ${T_.classAt===l.n?'selected':''}>${l.n}</option>`).join('')}</select></label>
    <label>New cards / day <input class="input" type="number" min="0" max="60" style="width:80px" id="t-new" data-tset="newPerDay" value="${T_.newPerDay}"></label></div></div>`;
  // plan
  h += `<div class="card"><h3>Week plan</h3><div class="stack" style="gap:6px">${T_.weeks.map((w,i)=>`<div class="row" style="flex-wrap:nowrap"><span class="num faint" style="width:92px;flex:none;font-size:13.5px">${fmtDate(w.d)}</span><input class="input" style="flex:1" id="wk-${i}" data-week="${i}" value="${esc(w.f)}"></div>`).join('')}</div></div>`;
  // mistakes
  const top = st.mistakes.slice().sort((a,b)=>(b.n||1)-(a.n||1)).slice(0,10);
  h += `<div class="card"><h3>Her repeat mistakes</h3>${top.length?`<table class="stats"><tbody>${top.map(m=>`<tr><td style="font-size:14px">${ruify(esc(m.q))}</td><td><s style="color:var(--red)">${esc(m.given)}</s> → <b>${esc(m.right)}</b></td><td class="num faint">${m.n}×</td></tr>`).join('')}</tbody></table>`:'<p class="faint" style="margin:0">None yet.</p>'}</div>`;
  h += `<div class="card"><h3>Teaching with this</h3><ul class="cando" style="font-size:14.5px"><li>Before each session, check the table: red readiness = what you teach that day.</li><li>Use "Student pages" to walk through a lesson together on screen. Your clicks there don't touch her record.</li><li>Grade her writing here; she sees it in red on her home page.</li><li>From Lektion 6 on, have her do one mock exam a week.</li></ul></div>`;
  h += `</div>`;
  return h;
}

// ---------- events ----------
document.addEventListener('click', e => {
  const say = e.target.closest('[data-say]'); if(say && !e.target.closest('[data-act]')) { speak(say.dataset.say); if(say.classList.contains('spk')||say.classList.contains('lt')||say.tagName==='I') return; }
  const ru = e.target.closest('i.ru'); if(ru && !ru.dataset.say && !e.target.closest('button')) { speak(ru.textContent); return; }
  const g = e.target.closest('[data-go]'); if(g){ if(g.dataset.go==='cards' && (!deck || deck.i>=deck.cards.length || deck.lesson)) buildDeck(null); go(g.dataset.go); return; }
  const t = e.target.closest('[data-tab]'); if(t){ lessonTab=t.dataset.tab; ui.lessonTab=lessonTab; saveUi(); render(); return; }
  const a = e.target.closest('[data-act]'); if(!a) return;
  const act=a.dataset.act, rec=P();
  switch(act){
    case 'intro-ok': ui.introSeen=1; saveUi(); render(); break;
    case 'preview': preview=!preview; go(preview?'home':'tutor'); break;
    case 'read': { const L=+a.dataset.l; if(!rec.read[L]){ rec.read[L]=true; touchStreak(); save('student'); } lessonTab='quiz'; render(); window.scrollTo({top:0}); break; }
    case 'qa': { const L=+a.dataset.l, i=+a.dataset.i, j=+a.dataset.j, l=LESSONS.find(x=>x.n===L), run=quizRun[L];
      run.ans[i]=j; const q=l.quiz[i]; if(j!==q[2]) logMistake('Self-test · L'+L, q[0].replace(/<[^>]+>/g,' '), q[1][j], q[1][q[2]]);
      if(Object.keys(run.ans).length===l.quiz.length){ const sc=l.quiz.filter((q,k)=>run.ans[k]===q[2]).length/l.quiz.length; const prev=rec.quiz[L]||{best:0,n:0}; rec.quiz[L]={best:Math.max(prev.best,sc), last:sc, n:prev.n+1, ts:Date.now()}; touchStreak(); }
      save('student'); const y=window.scrollY; render(); window.scrollTo({top:y}); break; }
    case 'q-reset': delete quizRun[+a.dataset.l]; render(); window.scrollTo({top:0}); break;
    case 'd-check': { const L=+a.dataset.l, l=LESSONS.find(x=>x.n===L), run=drillRun[L];
      $$(`[data-drill="${L}"]`).forEach(inp=>run.val[+inp.dataset.i]=inp.value);
      run.checked=true; const sc=l.drill.filter((d,i)=>isRight(run.val[i]||'',d[1])).length/l.drill.length;
      l.drill.forEach((d,i)=>{ if(!isRight(run.val[i]||'',d[1])) logMistake('Drill · L'+L, d[0], run.val[i]||'(blank)', answers(d[1])[0]); });
      const prev=rec.drill[L]||{best:0,n:0}; rec.drill[L]={best:Math.max(prev.best,sc), last:sc, n:prev.n+1, ts:Date.now()}; touchStreak(); save('student'); const y=window.scrollY; render(); window.scrollTo({top:y}); break; }
    case 'd-reset': delete drillRun[+a.dataset.l]; render(); break;
    case 'submit-write': { const id=a.dataset.id, ta=$('#wr-'+id); if(!ta.value.trim()) return toast('Write something first.');
      const l=LESSONS.find(l=>l.write&&l.write.id===id);
      S.student.writing[id]={text:ta.value, ts:Date.now(), prompt:l?l.write.prompt:''}; touchStreak(); save('student'); try{localStorage.removeItem('p5-draft-'+id);}catch(e){} toast('Sent to your tutor.'); render(); break; }
    case 'study-lesson': buildDeck(+a.dataset.l); go('cards'); break;
    case 'cmode': deck.mode=a.dataset.m; ui.cardMode=deck.mode; saveUi(); deck.reveal=false; render(); break;
    case 'reveal': deck.reveal=true; mountCard(); break;
    case 'card': grade(a.dataset.ok==='1'); deck.i++; deck.reveal=false; renderNav(); render(); break;
    case 'pro-check': { const inp=$('#fc-in'); const w=WORD[deck.cards[deck.i]]; deck.typed = a.dataset.skip? '' : (inp?inp.value:''); deck.last = !a.dataset.skip && isRight(deck.typed, ruAnswers(w.ru)); deck.reveal=true; grade(deck.last); mountCard(); speak(w.ru); break; }
    case 'next-card': deck.i++; deck.reveal=false; render(); break;
    case 'deck-more': { const pool=shuffle(WORDS.filter(w=>inScope(w.L)&&P().srs[w.id])).slice(0,20); deck={cards:pool.map(w=>w.id), i:0, reveal:false, stats:{ok:0,bad:0}, lesson:null, mode:deck.mode}; if(!pool.length) toast('Learn some new words first.'); render(); break; }
    case 'mock-start': buildMock(); render(); break;
    case 'm-r': mock.ra[a.dataset.k]=a.dataset.v==='1'; { const y=window.scrollY; render(); window.scrollTo({top:y}); } break;
    case 'm-q': mock.qa[+a.dataset.i]=+a.dataset.j; { const y=window.scrollY; render(); window.scrollTo({top:y}); } break;
    case 'mock-submit': $$('[data-mdrill]').forEach(i=>mock.da[+i.dataset.mdrill]=i.value); { const w=$('#m-write'); if(w) mock.wtext=w.value; } submitMock(); render(); window.scrollTo({top:0}); break;
    case 'mock-quit': mock.on=false; render(); break;
    case 'mock-close': mock.on=false; render(); break;
    case 'mis-clear': rec.mistakes.splice(+a.dataset.i,1); save('student'); render(); break;
    case 'hw-done': rec.hw[a.dataset.id]=true; touchStreak(); save('student'); render(); break;
    case 'abc': abcQ.a=a.dataset.v; render(); break;
    case 'abc-next': newAbcQ(); render(); break;
    // tutor
    case 'note-save': T().note=$('#t-note').value; T().noteTs=Date.now(); save('tutor'); toast('Pinned to her home page.'); break;
    case 'hw-add': { const tx=$('#hw-text').value.trim(); if(!tx) return; T().homework.push({id:uid(), text:tx, due:$('#hw-due').value||''}); save('tutor'); render(); break; }
    case 'hw-del': T().homework=T().homework.filter(x=>x.id!==a.dataset.id); save('tutor'); render(); break;
    case 'fb-grade': { const k=a.dataset.k; const ta=$('#fb-'+k); T().fb[k]=Object.assign({text:'',ts:0}, T().fb[k], {grade:a.dataset.g, text:ta?ta.value:(T().fb[k]?.text||'')}); render(); break; }
    case 'fb-save': { const k=a.dataset.k; T().fb[k]=Object.assign({}, T().fb[k], {text:$('#fb-'+k).value, ts:Date.now()}); save('tutor'); toast('Feedback sent.'); render(); break; }
  }
});
document.addEventListener('input', e => {
  const t=e.target;
  if(t.dataset.write){ try{ localStorage.setItem('p5-draft-'+t.dataset.write, t.value); }catch(err){} const c=$('#wc-'+t.dataset.write); if(c) c.textContent=(t.value.trim()?t.value.trim().split(/\s+/).length:0)+' words'; }
  if(t.dataset.drill){ const run=drillRun[+t.dataset.drill]; if(run) run.val[+t.dataset.i]=t.value; }
  if(t.dataset.mdrill) mock.da[+t.dataset.mdrill]=t.value;
  if(t.dataset.mwrite) mock.wtext=t.value;
});
document.addEventListener('change', e => {
  const t=e.target;
  if(t.dataset.scope){ const L=+t.dataset.scope; let sc=T().scope.filter(x=>x!==L); if(t.checked) sc.push(L); T().scope=sc.sort((a,b)=>a-b); save('tutor'); render(); }
  if(t.dataset.tset){ T()[t.dataset.tset]=+t.value; save('tutor'); renderNav(); }
  if(t.dataset.week!==undefined){ T().weeks[+t.dataset.week].f=t.value; save('tutor'); }
});
document.addEventListener('keydown', e => {
  if(e.key!=='Enter' || e.shiftKey) return;
  const t=e.target;
  if(t.id==='fc-in'){ e.preventDefault(); $('[data-act="pro-check"]:not([data-skip])')?.click(); return; }
  if(route==='cards' && deck && deck.reveal && t.tagName!=='INPUT' && t.tagName!=='TEXTAREA'){ const n=$('#next-btn'); if(n){ e.preventDefault(); n.click(); } return; }
  if(t.dataset.drill!==undefined){ e.preventDefault(); const nx=$(`#dr-${t.dataset.drill}-${+t.dataset.i+1}`); if(nx) nx.focus(); else $(`[data-act="d-check"][data-l="${t.dataset.drill}"]`)?.click(); }
  if(t.dataset.mdrill!==undefined){ e.preventDefault(); $(`#md-${+t.dataset.mdrill+1}`)?.focus(); }
  if(t.id==='hw-text'){ e.preventDefault(); $('[data-act="hw-add"]').click(); }
});
document.addEventListener('keydown', e => { // space reveals a flashcard
  if(route==='cards' && deck && deck.mode==='rec' && !deck.reveal && e.key===' ' && document.activeElement.tagName!=='INPUT'){ e.preventDefault(); deck.reveal=true; mountCard(); }
});

// ---------- on-screen Cyrillic keyboard ----------
const KROWS = ['йцукенгшщзхъ','фывапролджэ','ячсмитьбюё'];
let kTarget=null, kShift=false, kOpen=false;
function drawKbd(){
  const up = s => kShift ? s.toUpperCase() : s;
  $('#kbd').innerHTML = `<div class="kbd-rows">${KROWS.map(r=>`<div class="kbd-row">${[...r].map(c=>`<button class="key" data-k="${up(c)}" tabindex="-1">${up(c)}</button>`).join('')}</div>`).join('')}
   <div class="kbd-row"><button class="key w ${kShift?'on':''}" data-k="SHIFT" tabindex="-1">Shift</button><button class="key w" data-k=" " tabindex="-1" style="max-width:260px">space</button><button class="key w" data-k="BK" tabindex="-1">⌫</button><button class="key w" data-k="HIDE" tabindex="-1">Hide</button></div></div>`;
}
document.addEventListener('focusin', e => {
  const t=e.target;
  if((t.tagName==='INPUT' && t.getAttribute('lang')==='ru') || (t.tagName==='TEXTAREA' && t.getAttribute('lang')==='ru')){ kTarget=t; $('#kbd-toggle').hidden = kOpen; }
});
$('#kbd-toggle').addEventListener('mousedown', e=>e.preventDefault());
$('#kbd-toggle').addEventListener('click', () => { kOpen=true; drawKbd(); $('#kbd').hidden=false; $('#kbd-toggle').hidden=true; kTarget?.focus(); });
$('#kbd').addEventListener('mousedown', e => e.preventDefault()); // keep focus in the field
$('#kbd').addEventListener('click', e => {
  const k=e.target.closest('[data-k]'); if(!k) return; const v=k.dataset.k;
  if(v==='HIDE'){ kOpen=false; $('#kbd').hidden=true; $('#kbd-toggle').hidden=false; return; }
  if(v==='SHIFT'){ kShift=!kShift; drawKbd(); return; }
  if(!kTarget || !document.body.contains(kTarget) || kTarget.readOnly) return;
  const s=kTarget.selectionStart ?? kTarget.value.length, en=kTarget.selectionEnd ?? s, val=kTarget.value;
  if(v==='BK'){ const from = s===en ? Math.max(0,s-1) : s; kTarget.value = val.slice(0,from)+val.slice(en); kTarget.setSelectionRange(from,from); }
  else { kTarget.value = val.slice(0,s)+v+val.slice(en); kTarget.setSelectionRange(s+v.length,s+v.length); if(kShift){ kShift=false; drawKbd(); } }
  kTarget.dispatchEvent(new Event('input',{bubbles:true}));
  kTarget.focus();
});

// ---------- boot ----------
render();
initSync();
