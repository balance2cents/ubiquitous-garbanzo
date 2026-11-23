from _dsl import L

LECTURES = [

L(1, "The World of Strategic Thinking",
  "Strategy is the plan plus the ability to change the play in the seconds before the snap.",
  [
   ("The quarterback test", """
<p>Ridgley opens with American football. The huddle calls a play based on the situation: distance to a first down, downs left, distance to score. The defense reads the same situation and calls its own play. The interesting part happens in the 10 to 15 seconds between breaking the huddle and the snap: the quarterback reads the defense and may <b>change the play</b>.</p>
<p>That moment is the course's definition of real strategy: a plan, plus a live loop of action and reaction against an opponent who is also thinking. A plan that can't adapt is just a schedule.</p>
"""),
   ("Static thinking vs. strategic thinking", """
<p>Strategic thinking is a cultivated skill, not a talent you are born with. Most people default to <b>cognitive confinement</b>: running routines they never question and avoiding thinking about tomorrow. Einstein's line about insanity (doing the same thing and expecting different results) is the opposite of strategic thinking.</p>
<p>Strategic thinking is different from daydreaming about the future. It means setting goals, building long-range plans from careful analysis of the internal and external environment, and letting where you want to be in five years decide what you do today.</p>
<p>Peter Drucker split thinking into two kinds. <b>Thinking about objects</b> (static planning) is easy because the variables barely move. <b>Thinking about people</b> is hard because you have to anticipate the moves and countermoves of competitors.</p>
"""),
   ("The core vocabulary and its founders", """
<ul>
<li><b>Strategic intent</b>: the big idea a strategy serves (the career, the house, the market you want). It is what pulls your thinking toward the future.</li>
<li><b>Strategy</b>: more than a plan. A way of seeing the future with your goals in mind, responding to a changing environment and, where possible, changing that environment in your favor.</li>
<li><b>Sun Tzu</b> saw reality as fluid: the strategist must keep adapting.</li>
<li><b>Jomini</b> contributed interior lines of communication and the concentration of force.</li>
<li><b>Clausewitz</b> called uncertainty, chance and probability "friction," and answered it with <b>coup d'oeil</b>: a rapid, accurate stroke of intuition.</li>
<li><b>Liddell Hart</b> argued for the indirect approach: never grind against an entrenched enemy's front; find another route.</li>
<li><b>Michael Porter</b> brought it into business: strategy is "choosing a different set of activities to deliver a unique mix of value." In short, doing things differently. That one idea links Hannibal at Cannae (216 B.C.) and Apple in the 1980s.</li>
</ul>
"""),
   ("Strategy vs. tactics", """
<p>Strategy is the higher-level plan; tactics are how you execute it. If your strategy is to become a doctor, med school courses are part of the strategy, and how you study for them are tactics. Clausewitz: tactics is using forces in battle; strategy is using battles to win the war.</p>
<p>The trap is thinking strategy can be separated from tactics. Many great plans die in execution. Good strategy is <b>dynamic, adaptive and opportunistic</b>, and depends on swift, bold, decisive tactics.</p>
"""),
   ("Intelligence, surprise and a working definition", """
<p>Intelligence and analysis are the raw material for strategy. You want to learn what the other side is doing and mislead them about what you are doing, as the U.S. did with the feigned amphibious invasion of Kuwait in 1991. Ridgley previews the five types of surprise: <b>intention, time, place, strength and style</b>, and tools like SWOT.</p>
<p>His robust definition: strategy is a method or plan to bring about a desired future (a goal reached or a problem solved) that <b>assesses, acquires and allocates resources</b> to their most effective use, and that <b>anticipates competitor responses</b>.</p>
<p>Strategic thinking is goal-directed, structured, future-focused, analytical, ambitious and instrumental: a resource like money or time.</p>
"""),
  ],
  ["Real strategy = plan + live adaptation to an opponent who also adapts (the quarterback before the snap).",
   "Strategic thinking is a trained skill; the default human mode is unquestioned routine.",
   "Porter: strategy is doing things differently, choosing a different set of activities.",
   "Strategy and tactics can't be separated; execution is where most plans fail.",
   "A full definition covers the goal, resource allocation and anticipated competitor responses."],
  [("Strategic intent", "The big, motivating idea a strategy exists to serve; it pulls planning toward a desired future.", "concept"),
   ("Cognitive confinement", "Static thinking: living in routines you never question and refusing to think about tomorrow.", "concept"),
   ("Coup d'oeil", "Clausewitz's 'glance of the eye': a rapid, accurate intuitive judgment in the middle of uncertainty.", "concept"),
   ("Friction", "Clausewitz's name for the uncertainty, chance and probability that make up most of conflict.", "concept"),
   ("Michael Porter", "Harvard strategist; defined strategy as choosing a different set of activities to deliver a unique mix of value.", "person"),
   ("Peter Drucker", "Management thinker who contrasted easy thinking about objects with hard thinking about people.", "person")],
  [("mc", "In the quarterback example, what marks 'genuine strategy'?",
    ["Calling the perfect play in the huddle", "Changing the play after reading the defense", "Running the same play until it works", "Letting the coach decide"], 1,
    "The point is the action-reaction loop: the ability to change the plan based on what the opponent shows."),
   ("mc", "Porter's definition of strategy is best summarized as:",
    ["Doing the same things more efficiently", "Benchmarking the market leader", "Doing things differently", "Cutting costs below rivals"], 2,
    "Porter: choosing a different set of activities to deliver a unique mix of value."),
   ("tf", "According to the lecture, strategic thinking is mostly an inborn talent.", False,
    "It is a skill that must be cultivated and practiced."),
   ("mc", "Drucker said strategic thinking is harder than static thinking because it involves:",
    ["Larger budgets", "Thinking about people who react to you", "More spreadsheets", "Longer time horizons only"], 1,
    "Thinking about objects is easy; anticipating the actions and reactions of people is hard."),
   ("mc", "Which is NOT one of the five types of surprise?",
    ["Intention", "Place", "Price", "Style"], 2,
    "The five are intention, time, place, strength and style."),
   ("tf", "Clausewitz described strategy as the employment of battles to achieve the object of war.", True,
    "Tactics uses forces in battle; strategy uses battles toward the war's aim."),
  ],
  ("The gym that wants a 'strategy'",
   """A neighborhood gym owner tells you: "Our strategy for next year is to be more efficient. We'll install a new booking app, adopt the same class schedule as the big chain across the street, and run a 10% discount in January." A new boutique studio opened two blocks away last month, and the chain just cut its prices.""",
   [("Is what the owner described a strategy in the sense of this lecture? Explain using at least two ideas from the lecture.",
     """Mostly no. It is a list of efficiency moves and imitation, not strategy. Porter's test is doing things differently, but copying the chain's schedule is the opposite. There is no strategic intent (what is the gym for, for whom?), no allocation of resources toward a distinctive goal, and no anticipation of competitor responses: the chain can match a 10% discount instantly, and the boutique studio is ignored. It is static thinking about objects (an app, a schedule) rather than thinking about people who will react."""),
    ("Sketch what a 'quarterback' version would include: a plan plus how it adapts to competitors' moves.",
     """A clear intent (e.g. the gym for over-40 beginners who are intimidated by chains), a few activities the chain and boutique don't do, and planned reads: if the chain cuts prices again, don't follow (price war); if the boutique copies our niche classes, shift to coaching packages. Set signals to watch (membership churn, competitor promotions) and decide in advance when you will change the play.""")]),
  ["Name one program or process in your life or work that calls itself 'strategy' but is really an efficiency tool. What would genuine strategy look like instead?",
   "Watch the next sports match you see for the moment between play call and execution. Who adjusts, and based on what?"]),

L(2, "The Origins and Relevance of Ancient Strategy",
  "Six ancient minds, six portable lessons: power, innovation, fluid plans, knowing your opponent, reserves, and boldness.",
  [
   ("Thucydides: power as the arbiter", """
<p>Thucydides, an Athenian general (strategos) in the Peloponnesian War, wrote its history down to 411 B.C. The book founded international relations and the school of <b>political realism</b>. In the <b>Melian dialogue</b>, Athens tells the islanders of Melos that superior force is the only argument that matters, sweeping aside fairness, justice and the gods.</p>
<p>Lesson: some arenas really are governed by raw power (realpolitik). Recognize when you are in one, and ask how to use your advantages for an overwhelming win, or how to avoid being the Melians.</p>
"""),
   ("Pagondas at Delium: innovation tips an even fight", """
<p>At Delium (424 B.C.) the obscure Theban general Pagondas did several new things. He pursued the retreating Athenians rather than let them go, an early form of <b>forward defense and preemption</b> (striking a long-term threat, not just an immediate one). He held fresh cavalry <b>in reserve</b> and committed it at the decisive moment, the first recorded use of deliberate reserves joining an attack. He watched from a distance rather than fighting at the front, and modified his troop formation.</p>
<p>Delium counts as the birthplace of Western tactics. Lesson: <b>surprise innovations can turn an evenly matched struggle.</b></p>
"""),
   ("Sun Tzu: all plans are temporary", """
<p>The Art of War (5th century B.C., likely expanded later) rests on the fluid nature of reality. A plan can be obsolete the moment it is made. How you position yourself depends on two things: <b>objective conditions</b> in the physical environment and the <b>subjective beliefs</b> of competitors in it. The best plans emerge in the dynamic of action and response, guided by sound judgment and principles.</p>
"""),
   ("Hannibal at Cannae: outsmart the stronger side", """
<p>In 216 B.C. Hannibal, outnumbered in Rome's own territory, beat the Romans by turning their habits against them. The Romans formed a narrow, deep phalanx, which cancelled their numbers. Roman training told soldiers to chase a fleeing enemy, so when Hannibal's center appeared to give way, they pushed in and exposed their flanks. His cavalry drove off the Roman horse and, instead of chasing it, hit the Roman infantry from behind. Complete envelopment.</p>
<p>Lesson: against a stronger competitor, use what you know of their <b>habits and weaknesses</b>, especially when they feel most confident.</p>
"""),
   ("Vegetius and Machiavelli: preparation and fortune", """
<p><b>Vegetius</b> (late 4th century A.D.) wrote the Epitoma rei militaris, the most popular military handbook for over 1,000 years. It looks mundane (recruiting, training, discipline), but it links to high strategy: strategy has three elements, <b>intentions, capabilities and resources</b>, and preparation builds capability. He stressed <b>strategic reserves</b>.</p>
<p><b>Machiavelli</b> (The Prince; The Art of War) offers <b>virtu</b> (flexibility, foresight, energy, ability, political acumen: a developable skill) and <b>fortuna</b>, which he saw as malevolent and to be "beaten and mauled" into submission. Today we'd call that a <b>bias toward action</b>. Virtu meeting fortuna is an early version of <b>emergent strategy</b>.</p>
"""),
   ("The five lessons of the past", """
<ol>
<li>Any field, however mindless, can be transformed by tactics: use special forces at special times in special ways.</li>
<li>Plans must change; the best ones emerge from action and response.</li>
<li>Preparation is the heart of capability. <b>No reserves, no strategy.</b></li>
<li>Know your opponents: surprise plus superb execution can beat a force twice your size.</li>
<li>Be bold and seize your fortune; the hardest part is starting.</li>
</ol>
"""),
  ],
  ["Thucydides/Melian dialogue: some arenas run on raw power (realism).",
   "Pagondas: reserves and innovation decide even fights; first deliberate reserves at Delium.",
   "Sun Tzu: plans are temporary; position by terrain AND opponents' beliefs.",
   "Hannibal: exploit the stronger side's habits (Cannae envelopment).",
   "Vegetius: preparation builds capability; Machiavelli: virtu vs. fortuna, bias toward action."],
  [("Melian dialogue", "Passage in Thucydides where Athens tells Melos that superior force alone decides; the archetype of power politics.", "concept"),
   ("Political realism", "School of thought (rooted in Thucydides) that sees international outcomes as driven by configurations of power.", "concept"),
   ("Preemption", "Striking an enemy that poses a long-term threat before it becomes an immediate one.", "concept"),
   ("Strategic reserve", "Resources deliberately held back to be committed at a decisive moment.", "concept"),
   ("Virtu and fortuna", "Machiavelli's pair: developable qualities like foresight and energy (virtu) versus unpredictable, hostile fortune (fortuna).", "concept"),
   ("Pagondas", "Theban general at Delium (424 B.C.), credited with founding battlefield tactics, including the first deliberate use of reserves.", "person"),
   ("Hannibal", "Carthaginian general who enveloped a larger Roman army at Cannae in 216 B.C.", "person"),
   ("Vegetius", "Late Roman author of the Epitoma rei militaris, the handbook on training, discipline and reserves.", "person")],
  [("mc", "What tactical first is credited to Pagondas at Delium?",
    ["The phalanx", "Deliberate reserves joining an attack", "Siege engines", "Naval blockade"], 1,
    "He held fresh cavalry in reserve and committed it at the crucial moment."),
   ("mc", "Why did the Romans' own training help Hannibal at Cannae?",
    ["They were trained to retreat early", "They were trained to pursue a fleeing enemy", "They refused to use cavalry", "They fought only at night"], 1,
    "When his center seemed to withdraw, the Romans pressed forward and exposed their flanks."),
   ("tf", "Sun Tzu held that a well-made plan should be followed regardless of changing conditions.", False,
    "For Sun Tzu all plans are temporary; the best ones spring from action and response."),
   ("mc", "Vegetius ties his 'pedestrian' topics to strategy through which three elements?",
    ["Time, place, style", "Intentions, capabilities, resources", "Mission, objective, control", "Offense, mass, maneuver"], 1,
    "Preparation develops the capabilities that let intentions be achieved with available resources."),
   ("mc", "Machiavelli's advice to 'beat and maul' fortune is closest to:",
    ["Risk aversion", "A bias toward action", "Pure luck", "Waiting for better conditions"], 1,
    "He saw fortune as hostile and urged active, energetic response."),
   ("tf", "Ridgley's summary: 'If you have no reserves, you have no strategy.'", True,
    "Reserves make maneuver possible; they come from training, discipline and planning."),
  ],
  ("The small agency vs. the giant",
   """A 12-person design agency is pitching against a global agency with 20 times its staff for a regional bank's rebrand. Everyone knows the big agency's habit: it always sends its most senior partners to the first pitch, then hands the work to junior teams, and it reuses a standard 'brand discovery' template. The small agency has one founder who has personally led three bank rebrands and a modest cash buffer it has been saving.""",
   [("Which ancient lesson(s) apply here, and how would you use them?",
     """Hannibal's: exploit the stronger competitor's habits when it feels confident. Make the big agency's habit the issue: promise (in writing) that the people in the pitch room do the work, and show a discovery process built for this bank rather than a template. Pagondas/Vegetius on reserves: use the saved cash as a reserve committed at the decisive point, e.g. funding a free mini-prototype for the final round instead of spreading it thin."""),
    ("What is the risk of the Melian dialogue in this situation, and how do you avoid being the Melians?",
     """If the fight is purely about scale (global coverage, huge budgets), power decides and the small agency loses. Avoid fighting on that ground: don't argue you are 'just as big'; shift the decision criteria to things where size is a weakness (attention, senior involvement, speed).""")]),
  ["Where in your life is power the only real arbiter? What would you advise yourself if you were the Athenians, and if you were the Melians?",
   "List areas where you have uncommonly strong reserves (skills, money, contacts, time). How could you hold some back and commit them at a decisive moment?",
   "Think back to an unexpected situation that overwhelmed you. What virtu (trait) would have helped?"]),

L(3, "The Dawn of Modern Strategic Thinking",
  "Napoleon, Jomini and Clausewitz: why a checklist is the most dangerous thing a strategist can carry.",
  [
   ("From the Enlightenment to Napoleon", """
<p>The Enlightenment applied reason to everything, war included. Maurice de Saxe revived Vegetius; Frederick the Great mastered drilling large armies. With new ideas, new technology and growing populations, Napoleon (era roughly 1790 to 1815) arrived as a "perfect storm." He shows the <b>power of ideas over material resources</b>.</p>
"""),
   ("Napoleon: principles, not a system", """
<p>His Military Maxims remain a practical guide. Two warnings matter most. "<b>Unhappy the general who comes on the field of battle with a system.</b>" Treating strategy as a formula is the biggest danger for modern strategists. And: theory is fine for general principles, but applying them is always dangerous. The best plan can be overturned by its own implementation, so keep flexibility and respond to the opponent.</p>
"""),
   ("Two signature strategies", """
<ul>
<li><b>Central position</b> (when outnumbered): drive a wedge between allied enemy armies, leave a small masking force to hold one, and fight the other with superior local force. This is <b>concentration in time and space</b>: be stronger at the point of attack even if weaker overall.</li>
<li><b>Indirect approach</b> (when roughly equal and with room to maneuver): a small force feints at the enemy's front (a "demonstration") while the main force swings onto the flank or rear, onto the enemy's lines of communication and supply, forcing it to fight at a disadvantage or withdraw.</li>
</ul>
"""),
   ("Jomini vs. Clausewitz", """
<p><b>Jomini</b> (Swiss officer in Napoleon's army) was first to separate <b>strategy, tactics and logistics</b>. His master principle was <b>concentration at the decisive point</b>, in four parts: bring most forces to bear on decisive areas and enemy communications without exposing your own; maneuver your major forces against only parts of the enemy; tactically mass on the decisive area of the battlefield; and get those forces into action fast. He also defined 12 geometric orders of battle.</p>
<p><b>Clausewitz</b> (Prussian; On War, published posthumously by his widow Marie) placed war in a political context. War is a function of <b>violence, chance and political aims</b>. Chance matters most to us: the commander's courage and skill against uncertainty, resolved through coup d'oeil. Militaries now accept that intuitive decision-making can be taught.</p>
"""),
   ("What happened next", """
<p>Jomini dominated the 19th century. In the American Civil War, commanders treating him as a checklist launched massed frontal assaults into rifles and minié balls. The fault was the checklist mindset, not Jomini. Creative exceptions: <b>Stonewall Jackson</b> ("mystify, mislead, and surprise"; Shenandoah 1862) and <b>Nathan Bedford Forrest</b> ("Get there first with the most"; Brice's Crossroads 1864). Guderian's panzers in 1940 applied the same idea of overwhelming force at one point.</p>
<p>World War I generals tried to concentrate like Jomini but missed that technology had shifted the advantage to the defense. Liddell Hart responded with his indirect approach built around the tank. In the 1930s, <b>geopolitics</b> and geographical determinism appeared; Mackinder's 1904 formula: who rules Eastern Europe commands the Heartland; who rules the Heartland commands the World Island; who rules the World Island commands the World.</p>
<p>Keep two tools: the <b>indirect approach</b> and the <b>central position</b>. And notice the frontal assault is used far too often.</p>
"""),
  ],
  ["Napoleon: never bring a system to the battlefield; principles must flex in execution.",
   "Central position (outnumbered) = wedge + mask + local superiority; indirect approach (equal) = feint front, hit flank/rear.",
   "Jomini: strategy/tactics/logistics; concentration at the decisive point.",
   "Clausewitz: violence, chance, political aims; coup d'oeil beats chance.",
   "Checklist strategy produced the Civil War and WWI slaughters."],
  [("Central position", "Napoleon's move when outnumbered: split allied enemies, mask one, and defeat the other with local superiority.", "concept"),
   ("Indirect approach", "Feint at the enemy's front while the main force strikes its flank, rear or supply lines; avoid head-on attacks on strength.", "concept"),
   ("Concentration of force", "Massing superior strength at the decisive point and time, even when outnumbered overall.", "concept"),
   ("Geopolitics", "Systematic thinking about how geography shapes politics and conflict; criticized as geographic determinism.", "concept"),
   ("Antoine Jomini", "Swiss theorist who separated strategy, tactics and logistics and made concentration the core principle.", "person"),
   ("Carl von Clausewitz", "Prussian theorist (On War): war as violence, chance and politics; coup d'oeil.", "person"),
   ("Halford Mackinder", "Geographer whose 1904 Heartland formula founded geopolitics.", "person")],
  [("mc", "When outnumbered by two allied armies, Napoleon typically used:",
    ["The indirect approach", "The central position", "A frontal assault", "A siege"], 1,
    "He drove a wedge between them and fought one with local superiority while masking the other."),
   ("tf", "Napoleon said: 'Unhappy the general who comes on the field of battle with a system.'", True,
    "His warning against treating strategy as a formula."),
   ("mc", "Jomini is credited with being first to distinguish:",
    ["Strategy, tactics and logistics", "Offense and defense", "Land and sea power", "Virtu and fortuna"], 0,
    "His Art of War defined these as three distinct realms."),
   ("mc", "Clausewitz's three variables of conflict are:",
    ["Mass, maneuver, surprise", "Violence, chance, political aims", "Time, place, strength", "Mission, enemy, terrain"], 1,
    "The strategist balances violence, chance and political aims."),
   ("mc", "Why did massed frontal assaults fail so badly in the Civil War and WWI?",
    ["Jomini forbade them", "Technology had shifted the advantage to the defense", "Armies lacked numbers", "Cavalry was banned"], 1,
    "Rifles, minié balls and later machine guns made frontal attacks nearly suicidal; commanders followed checklists."),
   ("tf", "Forrest's 'Get there first with the most' is an expression of Jomini's principle of concentration.", True,
    "It packs surprise, speed, objective and mass into one phrase; Brice's Crossroads showed concentration at work."),
  ],
  ("Two rivals at once",
   """You run a small food-delivery startup in one city. Two larger competitors have just announced a partnership: one will cover restaurants, the other groceries, and they'll cross-promote. Together they outspend you 5 to 1, but each is only strong in its own category, and their integration won't be complete for six months.""",
   [("Which Napoleonic strategy fits this situation, and how would you apply it?",
     """The central position: you face two allied opponents and are outnumbered overall. Drive a wedge in the gap before integration is complete. Concentrate nearly everything on one front (say, grocery delivery in the neighborhoods where the grocery partner is weakest) to win local superiority, while a small 'masking force' (basic retention offers) holds your position against the other. Time matters: act inside the six-month window."""),
    ("What would the checklist-minded (bad Jomini) version look like, and why would it fail?",
     """Matching both rivals everywhere at once with discounts and ads: a frontal assault on two entrenched fronts with one-fifth the resources. It spreads your force thin, ignores the timing window and the gap between allies, and fights on the ground where they are strongest.""")]),
  ["Is there a situation where two or more parties are teaming up against you? How could you concentrate against only one part of the opposition?",
   "Identify an oblique approach you could use against a competitor: where would you 'demonstrate,' and where would you really strike?",
   "Recall a time a hunch solved a problem. Where did it come from, and how could you listen to it more?"]),

L(4, "Modern Principles of Strategic Conflict",
  "Nine principles that survived every change in weapons, from 1940's Ardennes to your next negotiation.",
  [
   ("France, 1940", """
<p>The French trusted the Maginot Line and assumed the dense Ardennes forest would stop an attack. The Germans went through the Ardennes, achieving rare <b>strategic surprise</b>. They combined two ideas: assembling activities in innovative ways (tanks, aircraft and infantry together: <b>blitzkrieg</b>) and the indirect approach. They used offensive, mass, maneuver, economy of force and surprise. A sound principle is one that keeps working as technology, place and players change.</p>
"""),
   ("The nine principles (Fuller, adopted by the U.S. military)", """
<ul>
<li><b>Objective</b>: aim every operation at a clear, decisive, attainable goal.</li>
<li><b>Offensive</b>: seize, retain and exploit the initiative.</li>
<li><b>Mass</b>: concentrate overwhelming effect at the decisive place and time.</li>
<li><b>Economy of force</b>: allocate only the minimum to secondary efforts.</li>
<li><b>Maneuver</b>: put the enemy at a disadvantage through flexible use of power.</li>
<li><b>Unity of command</b>: one commander and one effort per objective.</li>
<li><b>Security</b>: never let the enemy gain unexpected advantage.</li>
<li><b>Surprise</b>: strike at a time, place or manner they're unprepared for.</li>
<li><b>Simplicity</b>: clear, uncomplicated plans and concise orders.</li>
</ul>
<p>Fuller grouped them under <b>control, pressure and resistance</b>.</p>
"""),
   ("Objective and offensive", """
<p>Everyone involved must know the objective, and every intermediate step must contribute to it directly, quickly and economically. Too many people confuse tactics with the goal; even Robert E. Lee is faulted as a master tactician but a mediocre strategist. The army's <b>METT-T</b> framework (mission, enemy, troops, terrain, time) translates easily: competitor, your people and energy, your organizational landscape.</p>
<p>Offensive action seizes the initiative and forces opponents to react. Defense is a temporary necessity before resuming the offensive.</p>
"""),
   ("Mass, economy of force and maneuver", """
<p><b>Mass</b> is synchronizing power in concentrated time and space, and sustaining it. It's harder than it sounds in big organizations. Because mass is never unlimited, <b>economy of force</b> matters: everything gets a job, and secondary efforts get the minimum so you can mass at the decisive point. In business, don't squander resources on peripheral ventures.</p>
<p><b>Maneuver</b> is moving relative to the opponent for positional advantage. It keeps them off balance, lets you choose where and when to fight (or decline to), and makes you unpredictable. It needs agility of thought, plans and organization.</p>
"""),
   ("Unity, security, surprise, simplicity", """
<p><b>Unity of command</b> means one person with authority; when that's impossible (partners, alliances), aim for <b>unity of effort</b>: coordination toward a shared objective. Diffused responsibility and closed-door decisions undermine both.</p>
<p><b>Security</b> means protecting your plans, resources and people by understanding competitors' likely courses of action. <b>Surprise</b> is a force multiplier, achieved through speed, intelligence, deception, unexpected force, operational security and varied methods. <b>Simplicity</b> ties it together: simple plans get executed; complex ones confuse.</p>
"""),
  ],
  ["A principle is sound if it holds across eras and technologies.",
   "Nine principles: objective, offensive, mass, economy of force, maneuver, unity of command, security, surprise, simplicity.",
   "Fuller's grouping: control, pressure, resistance.",
   "METT-T is a portable planning checklist: mission, enemy, troops, terrain, time.",
   "Don't confuse tactical brilliance with strategic progress."],
  [("Blitzkrieg", "Germany's 'lightning war' combining tanks, aircraft and infantry with the indirect approach (France, 1940).", "concept"),
   ("Economy of force", "Giving secondary efforts only the minimum so that maximum strength can be massed at the decisive point.", "concept"),
   ("Unity of effort", "Coordination of separate actors toward a shared objective when single command isn't possible.", "concept"),
   ("METT-T", "Army planning framework: mission, enemy, troops, terrain, time available.", "concept"),
   ("J. F. C. Fuller", "British colonel who distilled the principles of war during WWI; adopted by the U.S. Army.", "person")],
  [("mc", "Which principle says to give secondary efforts only the minimum necessary?",
    ["Mass", "Economy of force", "Security", "Simplicity"], 1,
    "Economy of force frees resources to mass at the decisive point."),
   ("mc", "Fuller grouped the nine principles under:",
    ["Control, pressure, resistance", "Plan, do, check", "Time, place, style", "Land, sea, air"], 0,
    "Fuller's three headings."),
   ("tf", "In 1940 the Germans attacked the Maginot Line head-on and broke through.", False,
    "They went through the Ardennes, around the line: strategic surprise plus the indirect approach."),
   ("mc", "When unity of command is impossible (e.g., an alliance), the course says aim for:",
    ["Unity of effort", "Mass", "Simplicity", "Offensive"], 0,
    "Unity of effort: coordination and cooperation toward a commonly recognized objective."),
   ("mc", "What does the 'T' that appears twice in METT-T stand for?",
    ["Tactics and timing", "Troops and terrain/time", "Threats and targets", "Training and tools"], 1,
    "Mission, enemy, troops, terrain, time available."),
   ("tf", "According to the offensive principle, defense should be a temporary respite before regaining the initiative.", True,
    "The side that keeps the initiative forces others to react."),
  ],
  ("The product launch with nine priorities",
   """A mid-size software company is launching a new product. The plan has nine 'equal priority' goals, four executives co-own the launch with no final decision-maker, the marketing budget is split evenly across eight countries, and the launch date was announced publicly a year in advance with a full feature list.""",
   [("Identify at least four principles of war the plan violates and explain each.",
     """Objective: nine equal priorities means no decisive objective. Unity of command: four co-owners, no one with authority. Mass and economy of force: an even split across eight countries means nowhere gets overwhelming effect. Security and surprise: announcing date and features a year ahead lets competitors prepare. Simplicity is also violated by the tangle of goals and owners."""),
    ("Propose a revised plan that applies the principles.",
     """One objective (e.g. 1,000 paying customers in the two best-fit markets within 90 days); one accountable launch owner; mass 70% of budget on those two markets, minimal holding effort elsewhere (economy of force); keep exact features and timing quiet until close to launch (security, surprise); a one-page plan everyone can repeat (simplicity).""")]),
  ["Do an 'idea inventory': which of your beliefs about how the world works were formed in conditions that no longer exist (like France's WWI-based thinking)?",
   "Pick three principles and check whether someone has used them against you recently.",
   "Pick three principles and apply them to a current goal."]),

L(5, "Geography—Know Your Terrain",
  "Every battlefield, from a chessboard to a conference room, has positional power. Map it before you fight on it.",
  [
   ("Geopolitics and its limits", """
<p>Geopolitics studies how unchanging physical geography conditions politics and conflict. It's criticized as <b>geographic determinism</b> (a single-factor explanation) and was tainted by Nazi use, but its core idea survives: geography is a source of political, military and economic power. Spykman: geography is the most fundamental factor in foreign policy because it is the most permanent; "ministers come and ministers go... but mountain ranges stand unperturbed." Small features matter too, like the sunken road of Ohain that wrecked Napoleon's cavalry at Waterloo.</p>
"""),
   ("Inherent positional power", """
<p>Geography matters only as people use it for a purpose, and its value is usually temporary. Competition is a <b>three-way dialectic</b>: opponents maneuver against each other while interacting with the terrain. The <b>rules</b> of the contest create the terrain's power: move the goal in football and every position's value changes.</p>
<p>Two kinds of power: <b>potential positional power</b> (from the technology and tactics both sides could invest in the field) and <b>realized positional power</b> (from actual deployment, condition, numbers, skill and timing).</p>
"""),
   ("Chess, conference rooms and boxing rings", """
<p>In chess the four center squares have the highest potential power, but every move changes each square's value, and pieces and squares amplify each other (synergy). A conference room works the same way: seating, table shape and chairs create power configurations. Negotiators manipulate micro-geography, as at P'anmunjŏm. In boxing, a featureless ring still gives each square foot meaning relative to the fighters.</p>
"""),
   ("Intelligence Preparation of the Battlefield (IPB)", """
<p>The military's systematic method for understanding the ground, easily adapted to business and personal decisions:</p>
<ol>
<li><b>Define the battlefield environment</b>: what influences both sides; its limits; what's unknown but should be known.</li>
<li><b>Describe the battlefield's effects</b>: terrain and weather, plus infrastructure, politics, press, population, demographics.</li>
<li><b>Evaluate the competitor</b>: how it normally organizes and operates (from history and threat models).</li>
<li><b>Determine the competitor's possible courses of action</b>: given its preferences and this environment, what will it likely try?</li>
</ol>
"""),
   ("Kursk 1943: defense in depth", """
<p>The Soviets learned through intelligence exactly when and where the Germans would attack the Kursk bulge (120 miles wide, 90 deep) with a pincer. Over months they built successive defense lines, used terrain to channel the Germans into minefields, artillery zones and hidden antitank points, and ground down the entire German strategic tank reserve in a week. The initiative passed to the Soviets for good.</p>
<p>Lesson: if you know where you'll be attacked, prepare the ground; once a challenger commits, wear them down with successive lines on terrain you chose. Choose your ground beforehand whenever possible.</p>
"""),
  ],
  ["Geography is power, but only relative to how people use it and to the rules.",
   "Potential vs. realized positional power.",
   "Micro-geography (seating, venues) shapes negotiations.",
   "IPB: define environment, describe effects, evaluate competitor, determine their courses of action.",
   "Kursk: known attack + prepared terrain = defense in depth."],
  [("Geographic determinism", "Criticism of geopolitics as explaining complex outcomes by geography alone.", "concept"),
   ("Potential positional power", "Power a location could provide given the technology and tactics available to both sides.", "concept"),
   ("Realized positional power", "Power actually produced by how, when and how well forces are deployed.", "concept"),
   ("Intelligence Preparation of the Battlefield (IPB)", "Four-step military method for analyzing the ground, its effects, the competitor and its likely courses of action.", "concept"),
   ("Defense in depth", "Successive prepared lines that absorb and wear down an attacker on chosen terrain (Kursk 1943).", "concept"),
   ("Nicholas Spykman", "Geopolitical theorist, 'godfather of containment'; geography is the most permanent factor in foreign policy.", "person")],
  [("mc", "What is the final step of IPB?",
    ["Define the battlefield", "Describe battlefield effects", "Evaluate the competitor", "Determine the competitor's possible courses of action"], 3,
    "It ends by asking what the competitor will likely do, given its habits and this environment."),
   ("tf", "According to the lecture, geography has value in and of itself regardless of how people use it.", False,
    "It takes importance only as people use it for a purpose, and its value is usually temporary."),
   ("mc", "Changing where the goal is in football illustrates that positional power depends on:",
    ["Weather", "The rules of the contest", "Player salaries", "Crowd size"], 1,
    "The rules create the terrain's positional power."),
   ("mc", "What did the Soviets do at Kursk?",
    ["Launched a surprise offensive first", "Built successive prepared defense lines on chosen terrain", "Retreated to Moscow", "Attacked through the Ardennes"], 1,
    "Defense in depth wore down the German tank reserve."),
   ("tf", "Realized positional power comes from actual deployment, condition, numbers and timing.", True,
    "Potential power is about what could be invested; realized power is what is actually deployed."),
   ("mc", "In chess, which squares have the highest potential power at the start?",
    ["The corners", "The four center squares", "The back rank", "The edges"], 1,
    "Early control of the center is the basis of a winning game, though values change every move."),
  ],
  ("The salary negotiation",
   """You're negotiating a raise. Your manager has suggested meeting Friday at 5 p.m. in their office, sitting behind their desk. Budget decisions for next year are finalized the following Wednesday. You know your manager tends to agree to things that make them look good to their own boss, and dislikes surprises in front of others.""",
   [("Run a quick IPB on this negotiation.",
     """1) Environment: the decision window closes Wednesday; the manager's boss and the budget process influence both sides; unknown: the size of the raise pool. 2) Effects: Friday 5 p.m. means tired and rushed; their office and desk give them positional power; after Wednesday the terrain disappears. 3) Competitor: wants to look good upward, avoids public surprises. 4) Likely courses: defer ('let's revisit next quarter'), offer a small standard raise, or agree if it can be framed as their win."""),
    ("How would you reshape the terrain in your favor?",
     """Move the meeting earlier in the week before Wednesday (time terrain), at a neutral spot like a small meeting room or side-by-side seating (micro-geography), and bring a one-page case framed as something your manager can take to their boss. Raise it privately so they aren't surprised in front of others.""")]),
  ["What factors give you a geographic advantage in your own interactions (where you sit, where you meet, whose turf)?",
   "List the unwritten rules in a setting you compete in. Where is the gap between official and real rules, and does it give you room to maneuver?",
   "If you had to defend against a strong opponent, what successive 'lines of defense' could you prepare?"]),

L(6, "Grand Strategists and Strategic Intent",
  "Without a big, clear intent, strategy is just soulless technique.",
  [
   ("Hamel and Prahalad's idea", """
<p>In 1989 Gary Hamel and C. K. Prahalad named <b>strategic intent</b> in Harvard Business Review. They attacked the "strategy of imitation": copying techniques instead of having a strategy. Strategic intent creates an <b>obsession to win</b>: a long-term aspiration that reaches beyond current capabilities and forces you to build new resources. Tailoring ambition to current capability preserves the status quo; <b>stretch goals</b> without intent are a recipe for failure. Japanese firms (Honda, Matsushita, Sony, Toyota) used this after WWII: identify an extreme gap between resources and ambition, then close it.</p>
"""),
   ("Myth and football", """
<p>Joseph Campbell's <b>hero's journey</b> (Prometheus, Ulysses, the Grail) is the archetype of intent overcoming impossible obstacles, and your own life has the same structure. Vince Lombardi: "Winning isn't everything, it's the only thing," translated into a mid-range goal every player could act on: "You never win a game unless you beat the guy in front of you." Seen as a value chain, every player's effort serves the intent. Nobody perfects blocking technique for "best practice."</p>
"""),
   ("Nations and movements", """
<ul>
<li><b>Kennedy</b>: "We choose to go to the moon in this decade," achieved within ten years.</li>
<li><b>Martin Luther King Jr.</b> joined a powerful vision (social justice) with a strategy every individual could execute: nonviolent civil disobedience. Against him stood George Wallace's own intent ("Segregation now... forever"). King won with intent and strategy alone; the Civil Rights Act of 1964 followed.</li>
<li><b>George Kennan's</b> 1946 Long Telegram: the Soviets ignore reason but respond to force, so "contain" them. Containment guided U.S. policy for 40 years until 1989 to 1991.</li>
<li><b>Lincoln</b> fought not reactively but to preserve the Union, articulated in the Gettysburg Address.</li>
</ul>
"""),
   ("Business: Tata, and the failures", """
<p><b>Ratan Tata</b> (2003) demanded a four-seat "People's Car" for about $2,000, on a brutal timeline, over engineers' objections. The Tata Nano (2010) may have triggered a management revolution comparable to kanban and kaizen.</p>
<p>Failures: <b>DEC</b> (1992): "committed to providing high-quality products and services and being a leader in data processing." Vague, unfocused; swallowed by Compaq six years later. <b>Levi Strauss</b> under Bob Haas adopted an inward-looking vision unrelated to selling jeans; share fell from 48% to 17% (1990 to 2000). <b>Imperial Japan's</b> "Co-Prosperity Sphere" overreached: ambition without the capabilities to match.</p>
"""),
   ("Charting a bold course", """
<p>Strategy without intent is "a great flurry of activity." Vague bold pronouncements aren't courage. Real intent needs boldness grounded in an accurate read of reality, and it <b>closes off options</b> on purpose to pursue one goal single-mindedly.</p>
"""),
  ],
  ["Strategic intent = obsession to win + a deliberate gap between ambition and current resources.",
   "Stretch goals need intent; intent needs translation into mid-range goals people can act on (Lombardi).",
   "Good intent is concrete (moon in a decade, $2,000 car); bad intent is vague (DEC) or inward-looking (Levi's).",
   "Ambition without capability-building becomes overreach (imperial Japan).",
   "Real intent closes off options."],
  [("Strategy of imitation", "Copying competitors' techniques as a substitute for strategy; what strategic intent was coined to counter.", "concept"),
   ("Stretch goal", "A goal deliberately beyond current capabilities, forcing the development of new resources.", "concept"),
   ("Hero's journey", "Joseph Campbell's archetypal story of a hero overcoming seemingly impossible obstacles.", "concept"),
   ("Containment", "Kennan's strategic intent: meet Soviet expansion with American power; U.S. policy for 40 years.", "concept"),
   ("Gary Hamel", "Strategy scholar who, with C. K. Prahalad, coined 'strategic intent' (1989).", "person"),
   ("C. K. Prahalad", "Hamel's co-author; later known for 'bottom of the pyramid' market solutions to poverty.", "person"),
   ("George Kennan", "Diplomat whose 1946 Long Telegram set the U.S. containment policy.", "person")],
  [("mc", "Hamel and Prahalad coined strategic intent to counter:",
    ["Cost leadership", "The strategy of imitation", "Game theory", "Scenario planning"], 1,
    "They saw firms pursuing imitative techniques as a substitute for strategy."),
   ("tf", "Setting stretch goals without strategic intent is, per the lecture, a recipe for failure.", True,
    "Stretch goals need the animating intent behind them."),
   ("mc", "What made DEC's 1992 statement a failure of strategic intent?",
    ["It was too ambitious", "It was vague and unfocused", "It targeted the poor", "It copied Apple"], 1,
    "'High-quality products... leader in data processing' rallies no one and closes no options."),
   ("mc", "Lombardi translated 'winning' into which actionable goal?",
    ["Run more plays", "Beat the guy in front of you", "Score first", "Never punt"], 1,
    "Intent must become mid-range goals each player can execute."),
   ("mc", "Imperial Japan's Co-Prosperity Sphere illustrates:",
    ["Successful containment", "Ambition exceeding capabilities (overreach)", "Blue ocean strategy", "Tit for tat"], 1,
    "Japan didn't have the capabilities to match its ambitions."),
   ("tf", "According to the lecture, good strategic intent keeps all options open.", False,
    "It deliberately closes off options to pursue one goal with single-minded fervor."),
  ],
  ("The nonprofit's new vision",
   """A literacy nonprofit's board proposes a new vision statement: "We strive to be a leading, innovative organization committed to excellence in education and community impact." Currently it tutors 400 kids a year in one city with 15 staff. A board member privately says the real dream is that no child in the region leaves third grade unable to read.""",
   [("Evaluate the proposed statement against the lecture's criteria.",
     """It is DEC all over again: generic words ('leading', 'innovative', 'excellence') that any organization could use, nothing measurable, no stretch, no options closed, nothing a tutor or donor can act on. It inspires no obsession to win."""),
    ("Rewrite it as real strategic intent and give one Lombardi-style mid-range goal.",
     """Intent: "By 2032, no child in our region leaves third grade unable to read." That is concrete and far beyond 400 kids a year, which forces capability building (training volunteers, partnering with schools, a scalable curriculum). Mid-range goal: "Every tutor gets one child from below grade level to grade level each semester." It also closes options: drop the adult-literacy side programs that dilute focus.""")]),
  ["Can you state the strategic intent behind your biggest current goal in one or two sentences?",
   "Are your goals easy to meet on purpose? Set one that seems out of reach, and list the resources and capabilities it would force you to build.",
   "Spend a few minutes thinking 'grandly' about an idea most people would dismiss with 'you can't do that.'"]),
]
