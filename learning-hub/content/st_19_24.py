from _dsl import L

LECTURES = [

L(19, "Leverage Cognitive Psychology for Better Strategy",
  "Your brain filters reality before you ever 'decide.' Know the filters, and break the mind rut on purpose.",
  [
   ("Bounded rationality", """
<p>We think we're rational, but we rarely think about thinking. Perception, memory and how we blend it with new information all run without conscious direction; we see only the results. The classic model said we weigh options and maximize utility. <b>Herbert Simon</b> corrected it with <b>bounded rationality</b>: limits of information, cognition and time. The brain pre-filters input using experience, education and culture, builds a <b>simplified mental model</b>, and we act rationally only within that model, which can be badly off in high-stress, high-stakes moments.</p>
"""),
   ("Mindsets and the expert's blind spot", """
<p>CIA veteran <b>Richards Heuer</b>: an experienced specialist may be among the last to see what's really happening when events turn; "analysts who know the most about a subject have the most to unlearn." In 1989 to 1990 CIA specialists were slow to grasp the speed of German reunification; generalists saw it. A <b>mindset</b> is a set of assumptions and methods; entrenched across a group, it becomes groupthink. Example: the Cold War mindset that led the U.S. to ally with unsavory regimes.</p>
"""),
   ("Three barriers to clear perception", """
<ol>
<li><b>Mindsets form quickly but resist change.</b> The "mind rut": a sequence of gradually distorted images hides that the last one is a different subject.</li>
<li><b>We perceive what we expect to perceive.</b> The Luftwaffe chief denied the Allies had a long-range fighter even after one was shot down; Stalin refused reports of the 1941 German invasion.</li>
<li><b>New information is assimilated to existing images.</b> Before the 1973 Arab-Israeli war, analysts updated each day's story incrementally, an "assembly line" narrative instead of the big picture.</li>
</ol>
"""),
   ("Groupthink (Irving Janis)", """
<p>Concern for solidarity and consensus degrades decisions (Bay of Pigs, the Watergate cover-up). Eight symptoms in three clusters (overestimating the group's power and morality; closed-mindedness; pressure to conform):</p>
<ul>
<li>Illusion of invulnerability (excess optimism, risk taking)</li>
<li>Unquestioned belief in the group's morality</li>
<li>Rationalizing away warnings</li>
<li>Stereotyping opponents as weak, evil or stupid</li>
<li>Self-censorship of dissent</li>
<li>Illusion of unanimity</li>
<li>Direct pressure on dissenters, framed as "disloyalty"</li>
<li>Self-appointed "mind guards" shielding the group from dissenting information</li>
</ul>
<p>Results: incomplete survey of alternatives, unexamined risks, rejected options never revisited, poor and biased information search, no contingency plans.</p>
"""),
   ("An analytical process model", """
<ol>
<li><b>Define the problem</b> so the answer makes a difference.</li>
<li><b>Suspend judgment</b>; list all plausible hypotheses, then trim to a workable set.</li>
<li><b>Collect information</b> on all of them, including alternatives you haven't seriously considered.</li>
<li><b>Argue against the hypotheses</b>: try to reject rather than confirm; evidence that fits your favorite may fit others too.</li>
<li><b>Monitor for surprises</b>: conclusions are tentative; name critical indicators to watch.</li>
</ol>
<p>To generate hypotheses outside your mind rut, use: <b>situational logic</b> (inductive; treat this case as unique), <b>application of theory</b> (deductive; general to specific), <b>comparison with historical situations</b> (case studies), and <b>data immersion</b> (soak in data, suppress preconceptions, test emerging patterns).</p>
"""),
  ],
  ["Bounded rationality: we decide inside a simplified mental model.",
   "Experts have the most to unlearn (Heuer).",
   "Barriers: sticky mindsets, seeing what we expect, assimilating new info to old images.",
   "Janis's groupthink: eight symptoms around invulnerability, closed minds, conformity.",
   "Analytical model: define, hypothesize widely, collect, try to reject, monitor."],
  [("Bounded rationality", "Simon's idea that decisions are rational only within limits of information, cognition and time.", "concept"),
   ("Mindset", "A collection of assumptions and methods that shapes what a person or group sees.", "concept"),
   ("Mind rut", "Being locked into a pattern so that genuinely new information looks like a variation of the old.", "concept"),
   ("Mind guards", "Self-appointed group members who shield the group from dissenting information (a groupthink symptom).", "concept"),
   ("Situational logic", "Inductive analysis treating a situation as unique rather than as one of a class.", "concept"),
   ("Data immersion", "Soaking in data while suppressing preconceptions so patterns can emerge and be tested.", "concept"),
   ("Herbert Simon", "Social scientist who introduced bounded rationality.", "person"),
   ("Richards Heuer", "CIA veteran; Psychology of Intelligence Analysis.", "person"),
   ("Irving Janis", "Psychologist who identified and named groupthink.", "person")],
  [("mc", "Heuer warns that during a paradigm shift, who has the most to unlearn?",
    ["Generalists", "Analysts who know the most about the subject", "New hires", "Politicians"], 1,
    "Specialists were slower than generalists to see German reunification coming."),
   ("mc", "Stalin refusing reports of the 1941 invasion illustrates which barrier?",
    ["We perceive what we expect to perceive", "Data immersion", "Bounded rationality only", "Mind guards"], 0,
    "His belief in the nonaggression paradigm overrode the evidence."),
   ("tf", "In the analytical process model you should try to confirm your favorite hypothesis.", False,
    "Try to reject hypotheses rather than confirm them."),
   ("mc", "The 'assembly line' narrative before the 1973 war shows:",
    ["New information assimilated to existing images", "Too little information", "Mirror-imaging", "Free riding"], 0,
    "Daily incremental updates prevented a coherent big picture."),
   ("mc", "Which is a symptom of groupthink?",
    ["Inviting outside critics", "Illusion of unanimity", "Reconsidering rejected options", "Contingency planning"], 1,
    "Others: invulnerability, self-censorship, mind guards, pressure on dissenters."),
   ("tf", "Application of theory is a deductive approach reasoning from the general to the specific.", True,
    "Situational logic is the inductive counterpart."),
  ],
  ("The confident launch team",
   """A marketing team of five has worked together for years and has never had a failed campaign. For a new market, they agree within ten minutes on the same campaign that worked at home. One junior member mentions that local focus groups found the humor offensive; the team lead says, "They just don't get it yet. We always win." Nobody raises it again, and there's no backup plan.""",
   [("Identify the groupthink symptoms and perception barriers at work.",
     """Illusion of invulnerability ('we always win'), rationalizing warnings (focus group dismissed), stereotyping the audience ('they don't get it'), self-censorship (nobody raises it again), illusion of unanimity (ten-minute agreement), direct pressure on the dissenter. Perception barriers: they see what they expect (home success), assimilating new market data to the old image. No contingency plan is a typical groupthink output."""),
    ("Apply the analytical process model to fix the decision.",
     """Define the problem: what campaign will work in THIS market? List several hypotheses (adapt the humor, a different tone, a local partner). Collect information for each, including the focus group. Try to reject the favored home campaign: does any evidence contradict it? Set indicators to monitor (early engagement, complaints) and a backup campaign. Assign someone as devil's advocate.""")]),
  ["Is there a consensus 'groupthink' on some public issue you follow? Where did it come from?",
   "Do you feel pressure to conform in your team? Who decides the central ideas?",
   "How do you define problems in group settings? Is the definition rigged toward the answer you want?",
   "Which cognitive trap affects you most, and how will you guard against it?"]),

L(20, "Strategic Intuition and Creative Insight",
  "Coup d'oeil is not magic. It's pattern memory plus courage, and it can be trained.",
  [
   ("Coup d'oeil and intelligent memory", """
<p>Clausewitz's "stroke of the eye" is the flash of insight behind great strategy, obvious in hindsight. Scientists no longer see analysis and intuition as separate; a single mode of thought, <b>intelligent memory</b>, combines them. Research suggests we can cultivate insight by creating the conditions that produce it.</p>
"""),
   ("How decisions really get made", """
<p>The textbook model has four steps: analyze the problem, list options, weight criteria and evaluate, add up the score. <b>William Duggan</b>: decision makers use that only when procedures force them; left alone, they use <b>strategic intuition</b>. Military research separates <b>analytical</b> decisions (when there's time) from <b>intuitive</b> ones (when time is short), but intuition is weak with inexperienced leaders, very complex situations, or competing courses of action.</p>
<p><b>Gary Klein</b>: experts don't generate many options and pick one. Problem and solution come to them together; they mentally simulate the course of action and commit or reject it.</p>
<p>Duggan's definition: strategic intuition is the "<b>selective projection of past elements into the future in a new combination</b>," with personal commitment to follow through and work out details along the way. That matches Porter's "doing things differently."</p>
"""),
   ("Chancellorsville as a natural experiment", """
<p>If everyone follows the same best practices, the efficiency frontier moves and nobody gains lasting advantage. The Civil War was close to a controlled experiment: officers from the same academy, same teachers, same prior war. The North had overwhelming material superiority, yet the war lasted four years. At <b>Chancellorsville</b> (May 1863), Lee faced Hooker's army twice his size, entrenched and better supplied, and won the most lopsided contest of the war by violating a bedrock rule: <b>never divide your army in the face of a superior foe</b>. Two divisions held Hooker while Jackson marched around the Union right.</p>
"""),
   ("Firefighters and patterns", """
<p>Klein found experienced firefighters don't compare options; they act. Intuition is the gradual build-up of a <b>large repertoire of patterns</b> over years of practice. Without it, decision makers freeze. Formal analysis supplements intuition but can't replace it. Klein's balance: let intuition <b>recognize and decide</b>, and use analysis to <b>verify</b>.</p>
"""),
   ("Seven steps to develop intuitive insight", """
<ol>
<li>Your <b>first option is probably the best</b>: note it, then mentally simulate how it would play out and what could go wrong.</li>
<li>Make sure you <b>understand the problem</b>.</li>
<li><b>Override intuition when it misleads</b>: ask what evidence would change your mind. If nothing could, you've built a cocoon.</li>
<li>Use intuition to <b>think ahead of the curve</b>: connect dots, flag inconsistencies.</li>
<li><b>Accept uncertainty</b>; know when you have enough to act.</li>
<li>Use the <b>right strategy</b>: if it's complicated and nobody has good intuitions, analyze.</li>
<li><b>Watch out for naysayers</b>: managers who discount experience, demand blind compliance, can't tolerate uncertainty.</li>
</ol>
<p>Insight isn't reserved for Napoleon or Steve Jobs; recombining what you know in new ways is a learnable skill.</p>
"""),
  ],
  ["Analysis and intuition merge in 'intelligent memory.'",
   "Experts recognize problem and solution together (Klein), then mentally simulate.",
   "Strategic intuition = new combinations of past elements projected forward (Duggan).",
   "Lee at Chancellorsville: insight beat textbook rules and superior resources.",
   "Intuition decides, analysis verifies; build patterns through deliberate experience."],
  [("Intelligent memory", "Model in which analysis and intuition are one mode of thought drawing on stored experience.", "concept"),
   ("Strategic intuition", "Duggan: selectively projecting past elements into the future in a new combination, with commitment to follow through.", "concept"),
   ("Recognition-primed decision", "Klein's finding that experts recognize a situation and a workable action together, then mentally test it.", "concept"),
   ("William Duggan", "Columbia strategist; Strategic Intuition and Napoleon's Glance.", "person"),
   ("Gary Klein", "Research psychologist who studied firefighters' intuition; The Power of Intuition.", "person")],
  [("mc", "Klein found that expert firefighters typically:",
    ["Compare several options systematically", "Act on a recognized pattern without comparing options", "Wait for orders", "Use a weighted scorecard"], 1,
    "Problem and solution come to them together."),
   ("mc", "What rule did Lee break at Chancellorsville?",
    ["Never attack at night", "Never divide your army in the face of a superior foe", "Always hold the high ground", "Never use cavalry"], 1,
    "He split his army and won the most lopsided battle of the war."),
   ("tf", "Duggan says decision makers prefer the four-step analytical method even when not required.", False,
    "They use it only when procedures force them; otherwise they use strategic intuition."),
   ("mc", "Intuitive decision-making works poorly when:",
    ["Time is short", "Leaders are inexperienced or the situation is very complex", "The problem is familiar", "The expert has seen similar cases"], 1,
    "Also when there are competing courses of action."),
   ("mc", "Klein's recommended balance is:",
    ["Analysis decides, intuition verifies", "Intuition recognizes and decides, analysis verifies", "Only analysis", "Only intuition"], 1,
    "Combine them, with intuition first."),
   ("tf", "Per the lecture, if no evidence could change your mind, you've built a cocoon around your beliefs.", True,
    "Step 3: override intuition when it misleads."),
  ],
  ("The overanalyzed hire",
   """A team lead with 12 years of hiring experience meets a candidate and immediately feels 'this person is right,' though the candidate's CV is unusual. HR insists on a 20-criteria weighted scorecard; the candidate scores slightly below another applicant. The lead is also known for occasionally falling for charismatic interviewees.""",
   [("When should the lead trust this intuition, according to Klein and the seven steps?",
     """The lead has a big repertoire of patterns from 12 years, so the first impression deserves to be recorded and taken seriously (step 1). But they should mentally simulate the hire (first 90 days, where it could fail) and ask what evidence would change their mind (step 3), especially given the known charisma bias. Intuition recognizes; analysis verifies."""),
    ("Propose a process that combines intuition and analysis instead of choosing one.",
     """Let intuition name the hypothesis ('this candidate will outperform'), then verify with targeted analysis: a work-sample task, reference calls aimed at the charisma risk, and a check of the two or three criteria that really predict success rather than all 20. If verification holds, hire despite the scorecard; if it exposes the known bias, override the gut.""")]),
  ["Do you dismiss intuition as unworthy? How could you listen more to your voice of experience?",
   "Where do you simply 'know' the answer within your expertise? How could coup d'oeil help you act on it?",
   "Compare the strengths and limits of analytical and intuitive decision-making in one decision you face now."]),

L(21, "From Systemic Problems to Systemic Solutions",
  "If it's the same problem as last year, it's a system problem. Fix the system, not the symptom.",
  [
   ("Recurring crises", """
<p>Drucker called them "recurring crises." John Foster Dulles: "The measure of success is not whether you have a tough problem to deal with, but whether it is the same problem you had last year." A <b>system</b> is a collection of people, processes and things that interact as an integrated whole, with structure, behavior, interdependence and usually output. Garbage collection, power grids, legal systems: we use them without seeing them, holding only expectations. It pays to look.</p>
"""),
   ("Warden's five rings", """
<p>John A. Warden III argued all systems share five components, drawn as concentric circles from the center out:</p>
<ol>
<li><b>Leader</b></li>
<li><b>Conversion process</b> (food or energy that keeps it running)</li>
<li><b>Infrastructure</b> (blood vessels, roads, transmission lines)</li>
<li><b>Population</b></li>
<li><b>Action units</b> (antibodies, police, maintenance crews)</li>
</ol>
<p>It works for a body, a state or a drug cartel, and lets you ask: what is the system's purpose, and does it deliver it?</p>
"""),
   ("IBM: the incentive problem", """
<p>In 1999 Lou Gerstner saw IBM winning more U.S. patents than anyone (1993 to 1999) but not turning them into businesses. His task force found that the short-term profit focus created <b>strategic myopia</b>; managers weren't rewarded for spotting growth; demands for fact-based analysis and detailed forecasts created a climate of fear; new ventures were held to legacy-business earnings targets and had their budgets cut. The system was designed to deliver stability, not new businesses. The <b>Emerging Business Opportunities</b> program changed incentives; 22 successful businesses launched in its first five years.</p>
"""),
   ("Best Buy: the information problem", """
<p>Jeff Severts saw that sales forecasts were tangled with budgeting, performance measurement, compensation and purchasing, each with an agenda that skewed the numbers. Borrowing James Surowiecki's wisdom-of-crowds idea, he asked 190 employees for estimates: off by less than 0.5%; a later test was 99.9% accurate. The system's incentives, not bad luck, had produced bad forecasts.</p>
"""),
   ("India: health problems solved upstream", """
<p>In the village of Sujala, the Byrraju Foundation fought disease not with more doctors or medicine but by installing <b>water purification</b>, and disease plummeted. Hindustan Unilever paired cheaper soap with hand-washing education and developed a more resilient iodine to fortify salt against widespread deficiency, earning profits while solving systemic problems.</p>
"""),
   ("Finding the root", """
<p>Sources of systemic problems include health, information, incentives and morale. Test with the <b>five whys</b>: ask "why?" at least five times until you reach the real cause; then find creative ways to solve or avoid it. Without understanding the roots, any solution is misdirected.</p>
"""),
  ],
  ["Same problem as last year = systemic problem.",
   "Warden's rings: leader, conversion process, infrastructure, population, action units.",
   "IBM: incentives produced stability, not innovation; change the incentives.",
   "Best Buy: biased information systems; diverse crowds forecast better.",
   "Ask 'why?' five times to reach the systemic root."],
  [("System", "People, processes and things interacting as an integrated whole with structure, behavior and output.", "concept"),
   ("Systemic problem", "A problem produced by how a system is designed, so it keeps recurring until the system changes.", "concept"),
   ("Five whys", "Asking 'why?' at least five times to trace a problem to its systemic root cause.", "concept"),
   ("Warden's five rings", "Leader, conversion process, infrastructure, population and action units, from center outward.", "concept"),
   ("Wisdom of crowds", "Surowiecki's finding that diverse, nominally informed groups often predict better than a few experts.", "concept"),
   ("John A. Warden III", "U.S. Air Force strategist who revolutionized thinking about air power with a systems approach.", "person"),
   ("Lou Gerstner", "IBM chairman who diagnosed the incentive problem behind missed growth opportunities.", "person")],
  [("mc", "What was IBM's systemic problem?",
    ["Too few patents", "Incentives rewarding short-term profit over new businesses", "Bad forecasting", "Impure water"], 1,
    "The system was designed to deliver stability and sobriety."),
   ("mc", "Which is the innermost of Warden's five rings?",
    ["Population", "Infrastructure", "Leader", "Action units"], 2,
    "Leader, then conversion process, infrastructure, population, action units."),
   ("tf", "Best Buy's employee crowd forecast was less accurate than the official forecast.", False,
    "It was off by less than 0.5%, later 99.9% accurate."),
   ("mc", "In Sujala, disease fell mainly because of:",
    ["More doctors", "New medicines", "Water purification", "A new hospital"], 2,
    "Fixing the systemic cause: impure drinking water."),
   ("mc", "Dulles's test of success is whether:",
    ["You have no problems", "You face the same problem as last year", "Your budget grew", "Your team is happy"], 1,
    "Facing the same problem means you treated symptoms."),
   ("tf", "The five whys technique aims to find the truly systemic cause.", True,
    "Keep asking until you reach the root."),
  ],
  ("The team that always misses the deadline",
   """Every quarter, a product team pulls all-nighters the week before a release. Management responds each time with pizza, overtime pay and a 'lessons learned' meeting. Features are added to the release until two weeks before the deadline. Sales promises customers dates before engineering estimates the work, and the sales team's bonus depends on signed deals, not on delivered features.""",
   [("Run the five whys and identify the systemic problem.",
     """Why the all-nighters? Too much work at the end. Why? Features keep being added late. Why? Customers were promised features and dates. Why? Sales commits before engineering estimates. Why? Sales bonuses reward signed deals, not delivery. The root is an incentive and process system (like IBM's), not laziness or bad luck. Pizza and lessons-learned meetings treat the symptom."""),
    ("Design a systemic solution.",
     """Change incentives and process: part of the sales bonus tied to delivered and accepted features; no customer date without an engineering estimate; a feature freeze four weeks before release, with exceptions approved by one owner. Measure 'crunch hours' as a tracked metric so recurrence is visible.""")]),
  ["Do the systems in your life (like the nail by the door for your keys) actually produce the results you think?",
   "List the systems you depend on to simply get through a day.",
   "Does your workplace have a recurring 'crunch time'? What system produces it?"]),

L(22, "Seize the Future with Scenario Analysis",
  "You can't predict the future, but you can rehearse several of them and pick moves that survive all.",
  [
   ("The paradox and the President's Daily Brief", """
<p>Sound decisions require knowing the future, yet it's unknowable. The <b>President's Daily Brief</b> gives the intelligence community's best estimate of the next 24 hours, to reduce uncertainty. In business, uncertainty means risk, and risk costs money. Chess shows the scale: one move ahead means 1,600 possible positions; two moves, 2.5 million. Scenario analysis is a mid-range answer: a menu of alternative futures built by asking "<b>What if?</b>" about key drivers and assembling the answers into plausible stories.</p>
"""),
   ("Rehearsing the future", """
<p>We already do this as training, rehearsal, standard operating procedures and contingency plans. Military, police and sports teams rehearse under conditions close to the real event: game-like practice, live-ammunition exercises, days-long stress evaluations. Businesses run <b>war games</b> to simulate crisis decisions, which also get leaders out of the boardroom where some options are taboo.</p>
"""),
   ("Origins: Kahn and Wack", """
<p><b>Herman Kahn</b> developed scenarios about nuclear war at RAND in the 1950s. In the late 1960s <b>Pierre Wack</b> brought scenario planning to <b>Royal Dutch Shell</b>. If the future were 100% unknowable, planning would be useless, so separate the <b>predetermineds</b> (appear the same in every scenario) from the <b>uncertainties</b> (play out differently as the horizon extends).</p>
"""),
   ("Three objectives", """
<ol>
<li>Projects and decisions that are <b>robust</b> across different futures: measured against all scenarios, not the best one, and built to meet minimum expectations in each.</li>
<li>Better thinking about the future: no single "official future."</li>
<li>Richer interpretation of information than competitors have.</li>
</ol>
"""),
   ("The eight-step process", """
<ol>
<li>Identify the <b>focal issue</b> or decision (from your mission and objectives).</li>
<li>Identify <b>key factors</b> in the local environment (customers, suppliers, competitors, success indicators).</li>
<li>Identify <b>driving forces</b> in the macro environment (demographics, technology, industry growth).</li>
<li><b>Rank</b> factors and forces by impact and uncertainty to find the critical uncertainties.</li>
<li>Select <b>scenario logics</b>: a two-by-two matrix of the main uncertainties, giving four possible worlds.</li>
<li><b>Flesh out</b> each scenario into a narrative, a story about the future.</li>
<li>Determine each scenario's <b>implications</b> for the focal issue.</li>
<li>Select <b>leading indicators</b> that reveal which future is unfolding.</li>
</ol>
<p>Give each scenario a vivid name ("Crisis Mode," "Open-Market Dynamic").</p>
"""),
   ("Shell and the 1973 oil shock", """
<p>Until 1965 Shell used "predict and control": a single-line forecast. Its scenarios first carried probabilities; the new approach made them equally plausible and focused on <b>causality, not probability</b>, to stretch executives' thinking. Of six oil-price scenarios in the early 1970s, the counterintuitive <b>Crisis Scenario</b> anticipated the 1973 embargo. Shell was better prepared than any competitor and later called tanker overcapacity and European petrochemicals correctly.</p>
<p>Personally: rehearse job interviews; for a speech, the predetermineds are the text and venue, the uncertainties are Q&amp;A, the room and the equipment, so practice with a friend asking questions. Where uncertainty is unpredictable, prepare standard responses that work almost anywhere.</p>
"""),
  ],
  ["Scenario analysis = several plausible stories about the future built from 'what if?'",
   "Separate predetermineds from critical uncertainties (Wack).",
   "Judge decisions by robustness across all scenarios, not the preferred one.",
   "Process: focal issue, key factors, drivers, rank, 2x2 logics, narratives, implications, indicators.",
   "Shell's Crisis Scenario prepared it for 1973."],
  [("Scenario analysis", "Building several plausible stories about the future by asking 'what if?' about key drivers.", "concept"),
   ("Predetermineds", "Elements expected to appear the same in every scenario.", "concept"),
   ("Critical uncertainties", "High-impact, highly uncertain forces that define how scenarios differ.", "concept"),
   ("Robust decision", "A decision that performs acceptably in all scenarios, not just the preferred one.", "concept"),
   ("Leading indicator", "A signal that shows which scenario the world is actually moving toward.", "concept"),
   ("War game", "A business or military simulation of crisis decisions against likely competitor moves.", "concept"),
   ("Herman Kahn", "RAND strategist who pioneered scenarios about nuclear war.", "person"),
   ("Pierre Wack", "Introduced scenario planning at Royal Dutch Shell.", "person")],
  [("mc", "What made Shell's revised scenario approach different?",
    ["Assigning precise probabilities", "Equally plausible scenarios focused on causality", "A single official forecast", "Ignoring uncertainty"], 1,
    "Causality, not probability, to stretch executives' thinking."),
   ("mc", "In Wack's terms, elements that appear the same in every scenario are:",
    ["Uncertainties", "Predetermineds", "Indicators", "Drivers"], 1,
    "Uncertainties are what differ."),
   ("tf", "A robust project is measured against the best possible scenario.", False,
    "It's measured against all scenarios and should meet minimum expectations in each."),
   ("mc", "The 2x2 matrix in step 5 typically yields how many scenarios?",
    ["Two", "Three", "Four", "Six"], 2,
    "Four possible worlds from two main uncertainties."),
   ("mc", "What is the last step of the process?",
    ["Name the scenarios", "Select leading indicators", "Identify the focal issue", "Rank factors"], 1,
    "Indicators tell you which direction history is taking."),
   ("tf", "Shell's Crisis Scenario anticipated the 1973 oil shock.", True,
    "Shell was better prepared than its competitors."),
  ],
  ("Choosing where to live after graduation",
   """Ana is graduating and deciding whether to sign a three-year apartment lease in Zurich. Two big uncertainties: whether she lands a job in Zurich or in another city, and whether remote work stays common in her field or fades. Predetermineds: she'll finish her degree in June, Zurich rents are high, and she wants to keep learning German.""",
   [("Build a 2x2 scenario matrix with named scenarios.",
     """Axes: job location (Zurich vs. elsewhere) and remote work (stays common vs. fades). 1) 'Home Base': Zurich job, remote common. 2) 'Daily Commuter': Zurich job, remote fades. 3) 'Remote Expat': job elsewhere, remote common, so she could live in Zurich anyway. 4) 'Forced Move': job elsewhere, remote fades, so she must relocate."""),
    ("What's a robust decision, and what leading indicators should she watch?",
     """A three-year lease performs badly in 'Forced Move.' Robust choice: a one-year lease or a sublet with an exit clause that works acceptably in all four. Leading indicators: where her interviews and offers come from, employer return-to-office announcements in her field, and job ads mentioning remote or hybrid.""")]),
  ["Pick a major decision and visualize how several alternative futures could unfold from it.",
   "For a recent decision, ask 'if I do this, what will the other player do?' How did you actually decide?",
   "Name three likely futures for yourself and a response that would hold up in all three."]),

L(23, "The Correlation of Forces, Luck, and Culture",
  "Big impersonal forces push on you. Lucky people ride them; strategists also read culture.",
  [
   ("Correlation of forces", """
<p>A Soviet Cold War term for calculating world power across military, political, economic, social, moral and revolutionary factors: a philosophy, a measuring method and a guide to action. The Soviets read the large impersonal forces, rode them, and tried to tilt them, which let a backward economy score notable successes against a richer U.S. For us it means the long-term environmental factors acting on a contest. We aren't at their mercy: like <b>aikidō</b>, we can position ourselves to redirect them. It combines all our environmental scans into a holistic, long-term view, so we can plan our response to curveballs in advance.</p>
"""),
   ("Luck as behavior", """
<p>"Good luck" is largely a consistent behavior pattern that rides the correlation of forces; fighting it with brute or intellectual force tends to produce "bad luck." Max Gunther's five behaviors of lucky people:</p>
<ol>
<li><b>Many friendly contacts</b> (networking).</li>
<li><b>Attending to hunches</b>: conclusions from real, if unconscious, data.</li>
<li><b>Acting boldly</b> (audentes fortuna juvat, "fortune favors the bold"): ready to accept opportunity, distinguishing boldness from rashness, not demanding certainty.</li>
<li><b>The ratchet effect</b>: getting out of bad situations fast. "If you are losing a tug-of-war with a tiger, give him the rope before he gets to your arm."</li>
<li><b>The pessimism paradox</b>: respecting Murphy's law and Mitchell's law ("Life is as slippery as a piece of soap..."); never surprised by the worst case.</li>
</ol>
<p>These are positioning by principle: they don't guarantee victory but improve the odds.</p>
"""),
   ("Hofstede's dimensions of culture", """
<p>Culture is a major current. <b>Geert Hofstede</b> (early 1970s) defined it as "the collective programming of the mind that distinguishes the members of one group or category of people from another." Its visible practices are <b>symbols, heroes and rituals</b>, which only become noticeable when you deal with another culture. Knowing cultural scores helps predict behavior, institutions and politics, and guards against stereotypes and <b>mirror-imaging</b>.</p>
<ul>
<li><b>Power distance</b>: how inequality in prestige, wealth and power is handled; shapes hierarchy. Russia 93, U.S. 40.</li>
<li><b>Uncertainty avoidance</b>: how threatened people feel by the unknown; higher means more rule-driven. Greece 112, U.K. 35.</li>
<li><b>Individualism</b> (vs. collectivism): individual or group rewards. Australia 90, Guatemala 6.</li>
<li><b>Masculinity</b> (ego goals vs. social goals): Slovakia 110, Sweden 5.</li>
</ul>
<p>No single dimension decides behavior; they combine into patterns of expectation. Firms often ignore culture because it's hard to quantify, which is exactly why understanding it is an advantage.</p>
"""),
  ],
  ["Correlation of forces: read the big impersonal currents and ride or tilt them.",
   "Luck is behavior: networking, hunches, boldness, ratchet effect, pessimism paradox.",
   "Hofstede: culture as collective mental programming, shown in symbols, heroes and rituals.",
   "Four dimensions: power distance, uncertainty avoidance, individualism, masculinity.",
   "Understanding culture beats mirror-imaging, and few competitors bother."],
  [("Correlation of forces", "Soviet concept for assessing the combined military, political, economic and social forces shaping a contest.", "concept"),
   ("Ratchet effect", "Gunther's lucky behavior of getting out of bad situations quickly.", "concept"),
   ("Pessimism paradox", "Gunther: lucky people expect things can go wrong, so they're never blindsided by the worst case.", "concept"),
   ("Power distance", "Hofstede dimension: how a culture handles inequality and hierarchy.", "concept"),
   ("Uncertainty avoidance", "Hofstede dimension: how threatened a culture feels by the unknown; high means more rules.", "concept"),
   ("Individualism vs. collectivism", "Hofstede dimension: whether people are motivated by individual or group rewards.", "concept"),
   ("Masculinity vs. femininity (Hofstede)", "Dimension contrasting ego/achievement goals with social/nurturing goals.", "concept"),
   ("Geert Hofstede", "Dutch researcher who created the dimensions of culture model.", "person"),
   ("Max Gunther", "Writer who identified five behaviors of lucky people (The Luck Factor).", "person")],
  [("mc", "Which Hofstede dimension measures sensitivity to the unknown?",
    ["Power distance", "Uncertainty avoidance", "Individualism", "Masculinity"], 1,
    "Higher scores mean more rule-driven societies (Greece 112)."),
   ("mc", "'Give the tiger the rope before he gets to your arm' illustrates:",
    ["The pessimism paradox", "The ratchet effect", "Acting boldly", "Networking"], 1,
    "Getting out of bad situations quickly."),
   ("tf", "In the lecture, Russia's power distance score (93) is higher than the U.S. score (40).", True,
    "High scores mean entrenched hierarchical roles."),
   ("mc", "Hofstede's visible practices of culture are:",
    ["Laws, taxes and borders", "Symbols, heroes and rituals", "Food, music and dress", "Rules, roles and rewards"], 1,
    "Culture provides the matrix to decode them."),
   ("mc", "Which country is cited as among the highest for social (feminine) goals?",
    ["Slovakia", "Sweden", "Australia", "Greece"], 1,
    "Sweden scores 5; Slovakia 110 on ego goals."),
   ("tf", "According to the lecture, luck is mostly random and can't be influenced by behavior.", False,
    "It's largely the result of consistent behaviors that ride the correlation of forces."),
  ],
  ("Leading a team across cultures",
   """You're a project lead from a low power distance, individualist culture. You've just taken over a team in a country with high power distance, high uncertainty avoidance and strong collectivism. In your first week you invited 'everyone to challenge my ideas openly,' announced individual performance awards, and said the plan would be 'figured out as we go.' Engagement is low and nobody speaks in meetings.""",
   [("Explain the reaction using Hofstede's dimensions and the idea of mirror-imaging.",
     """You mirror-imaged your own culture. High power distance: openly challenging the boss feels inappropriate, so silence is expected. High uncertainty avoidance: 'figure it out as we go' creates anxiety; people want clear rules and plans. Collectivism: individual awards can embarrass people and hurt group harmony. Your behavior clashed on all three dimensions."""),
    ("What would you change, and which lucky behavior helps here?",
     """Give a clear plan and roles up front (uncertainty avoidance), collect input privately or through senior team members (power distance), and reward team achievements (collectivism). Gunther's behaviors: build many friendly contacts one-on-one (networking) and use the ratchet effect, dropping the failing approach quickly instead of insisting.""")]),
  ["Draw a 'correlation of forces' map of the macro-forces pushing on you and on your organization.",
   "Pick two or three of Gunther's luck behaviors and start practicing them this week.",
   "How would your expectations differ doing business in Puerto Rico, Russia and Malaysia?"]),

L(24, "Strategic Thinking as a Way of Life",
  "Franklin, Churchill, Jobs and Winfrey: the strategic personality is curiosity, intent, boldness and follow-through.",
  [
   ("Prepare, don't predict", """
<p>Uncertainty is everywhere. Success isn't predicting the future but <b>preparing for it prudently</b>, combining the course's tools and taking an active role in shaping your circumstances.</p>
"""),
   ("Benjamin Franklin", """
<p>Franklin both visualized the future and crafted it, seizing and creating opportunities. At 21 he formed a discussion group that became the American Philosophical Society; he co-founded America's first public library and helped found what became the University of Pennsylvania. Curiosity plus a lust for life gave him legacies in science, politics, education, literature, military affairs and finance. His <b>13 principles</b> were a blueprint; four of them (<b>order, resolution, frugality, industry</b>) suggest that you tackle uncertainty by building an <b>island of certitude</b>.</p>
"""),
   ("Winston Churchill", """
<p>Expecting to die young like his father, Churchill moved with urgency: war correspondent at 21, riskiest military assignments, captured by the Boers, escaped. As First Lord of the Admiralty he fell after the Dardanelles failure in WWI and drew <b>five truths</b> for any operation:</p>
<ol>
<li>One must have <b>full authority</b> (the one he held most fiercely: never accept responsibility without power to act).</li>
<li>A <b>reasonable prospect of success</b>.</li>
<li><b>Greater interests</b> are not compromised.</li>
<li>All possible <b>care and forethought</b> in preparation.</li>
<li>All <b>vigor and determination</b> in execution.</li>
</ol>
<p>He spent the 1930s on the political periphery preparing a comeback, became prime minister on May 10, 1940, and led with a love of surprise and deception. He valued history as the guide to the future, and knew a good idea needs boldness, decisiveness and relentless follow-through.</p>
"""),
   ("Steve Jobs", """
<p>Jobs exercised coup d'oeil relentlessly and reshaped six industries: personal computers, animated movies, music, phones, tablets and digital publishing. "<b>Think Different</b>" works as a mission statement for any strategy. Forced out of Apple in 1985, he bought Pixar and built NeXT. Back at Apple in the late 1990s, he refocused the company in a single meeting on <b>four products</b> (consumer and pro desktops and portables), then made Apple the hub for iPod, iTunes, iPhone and iPad. His traits: focus, strategic intent, drive, insight at the crucial moment, coordinated surprise, precise execution, detailed follow-through.</p>
"""),
   ("Oprah Winfrey, and you", """
<p>Winfrey turned curiosity and personal details into an enduring brand (like Franklin), voiced strategic intent in everyday battles (like Churchill), and shaped national tastes in books, health and politics (like Jobs). A strategic personality can thrive in any field, and the distance between us and the greatest strategists is rarely as big as we think.</p>
<p>Robert J. Hastings: "Regret and fear are twin thieves who would rob us of today." The strategic thinker mines the past for insight, lets the five-year goal shape today's moves, welcomes uncertainty and bends it, and refuses to be merely buffeted by events.</p>
"""),
  ],
  ["Measure success by preparation, not prediction.",
   "Franklin: create an island of certitude (order, resolution, frugality, industry).",
   "Churchill's five truths: authority, prospect of success, greater interests, preparation, vigor.",
   "Jobs: radical focus (four products) and relentless execution.",
   "Strategic thinking is a habit: one lecture's principle per week, practiced deliberately."],
  [("Island of certitude", "A zone of order and discipline (Franklin's order, resolution, frugality, industry) for facing uncertainty.", "concept"),
   ("Churchill's five truths", "Full authority, reasonable prospect of success, greater interests safe, careful preparation, vigorous execution.", "concept"),
   ("Benjamin Franklin", "Founding father and Enlightenment polymath who lived by 13 principles.", "person"),
   ("Winston Churchill", "British prime minister in WWII; learned his five truths from the Dardanelles failure.", "person"),
   ("Steve Jobs", "Apple co-founder who refocused the company on four products and revolutionized six industries.", "person"),
   ("Oprah Winfrey", "Media strategist who built a personal brand and self-improvement mission.", "person")],
  [("mc", "Which of Churchill's five truths did he hold most fervently?",
    ["Reasonable prospect of success", "Full authority", "Vigor in execution", "Greater interests not compromised"], 1,
    "Never accept responsibility without the power to act."),
   ("mc", "Franklin's four principles that build an 'island of certitude' are:",
    ["Order, resolution, frugality, industry", "Silence, sincerity, justice, humility", "Mass, maneuver, surprise, security", "Mission, objective, control, implementation"], 0,
    "A key to tackling uncertainty."),
   ("tf", "On returning to Apple, Jobs expanded the product line to dozens of products.", False,
    "He cut it to four: consumer and professional desktops and portables."),
   ("mc", "Churchill drew his five truths from:",
    ["The Battle of Britain", "The Dardanelles failure in WWI", "The Boer War escape", "D-Day"], 1,
    "His political star fell after it."),
   ("mc", "The lecture's main measure of strategic success is:",
    ["Predicting the future accurately", "Preparing prudently for an uncertain future", "Avoiding all risk", "Copying great strategists"], 1,
    "Preparation, not prediction."),
   ("tf", "Ridgley argues the gap between us and the greatest strategic minds is rarely as vast as we suppose.", True,
    "Those bold enough always find new realms for strategic endeavor."),
  ],
  ("Your one-year strategic plan",
   """This is a capstone case about you. Choose one real goal you want to reach in the next 12 months (career, study, health, a project). Use the course's tools to plan it.""",
   [("State your mission and strategic intent for this goal, then list two measurable objectives.",
     """A strong answer has: a one-sentence mission (why this matters to you), a concrete, stretching strategic intent (Lecture 6), and two objectives that are clear, achievable and measurable with dates (Lecture 7). Weak answers are vague ('be better at X') or have no numbers or deadlines."""),
    ("Do a quick SWOT and name one scenario risk and one Churchill truth you'll apply.",
     """A strong answer lists honest internal strengths and weaknesses and specific external opportunities and threats (Lecture 10), names a critical uncertainty with a robust response (Lecture 22), and applies one of Churchill's truths concretely, e.g. 'I'll only commit if I have full authority over my schedule, so I'll negotiate fixed study blocks with my employer first' (Lecture 24). It closes options: it says what you'll stop doing.""")]),
  ["Which traits do Franklin, Churchill, Jobs and Winfrey share with people you admire?",
   "Pick one lecture per week and enact its principle deliberately in a real situation.",
   "Where do you want to be in one year and in five? Sketch the six-step plan and choose the tools you'll use first."]),
]
