from _dsl import L

LECTURES = [

L(7, "The Core and the Rise of Strategic Planning",
  "Mission first, then a six-step loop. And beware the binder on the shelf.",
  [
   ("Founding myths and mission statements", """
<p>The French Foreign Legion draws its identity from the stand at <b>Camerone</b> (Mexico, 1863) and the respect its enemies showed. Every organization should have a founding myth that captures its spirit (think Apple's two young men in a garage).</p>
<p>The myth feeds the <b>mission statement</b>, which anchors strategy and strategic intent. Good ones are bold and inspiring: Coca-Cola's "To refresh the world; to inspire moments of optimism and happiness..." Henry Mintzberg: the most interesting, successful companies "are not boring"; their strategies are novel, creative, sometimes playful. Equal Exchange ("Fairness to farmers...") shows how a mission can generate achievable objectives.</p>
"""),
   ("How planning grew up", """
<p>Planning began in the military: the Prussian general staff (1807) started formal staff planning. Business picked it up slowly: the <b>Harvard policy model</b> (1920s) was a call to action more than a method. After WWII, Ford hired ten former officers (the team led by Robert McNamara), introducing planning, control systems and fiscal discipline; McNamara later took planning to the Pentagon. By the 1960s planning was standard but had degenerated into an <b>annual budgeting exercise</b> built on last year's numbers. U.S. dominance hid the flaws until the 1970s, when Japanese competition and the oil states exposed them: the models ignored human irrationality and the moves of other players.</p>
"""),
   ("Mintzberg's three fallacies", """
<ul>
<li><b>Predetermination</b>: believing we can predict the future ("predict and prepare").</li>
<li><b>Detachment</b>: planners removed from the action; formulation cut off from implementation.</li>
<li><b>Formalization</b>: the "binder mentality"; the plan ossifies on a shelf and drifts from what the company does.</li>
</ul>
<p>McKinsey's 1978 "The Evolution of Strategic Management" described four phases: <b>financial planning</b> (1950s annual budgets), <b>forecast-based planning</b>, <b>externally oriented planning</b>, and finally <b>strategic management</b>, which welds planning and management into one process and spreads strategic thinking throughout the organization.</p>
"""),
   ("The six-step strategic planning process", """
<ol>
<li><b>Mission</b>: your reason for being; the core everything refers back to.</li>
<li><b>Objectives</b>: clear, concise, achievable, measurable goals that serve the mission.</li>
<li><b>Situation analysis</b> (environmental scan): external and internal environments. The most involved step.</li>
<li><b>Strategy formulation</b>: decide how to get from here to there; allocate resources; connect decisions to the people who implement.</li>
<li><b>Implementation</b>: where companies fail by not following the military dictum "<b>supervise and refine</b>."</li>
<li><b>Control</b>: a monitoring mechanism; when it signals trouble, loop back to the situation analysis.</li>
</ol>
<p>Porter's reminders: strategy means doing things differently, and the right timeframe may be a decade or more. A single budget cycle is too short; long plans build unique capabilities and fit across activities.</p>
"""),
  ],
  ["A founding myth feeds a mission; a mission anchors strategy.",
   "Early planning degenerated into annual budgeting and ignored competitors and irrationality.",
   "Mintzberg's fallacies: predetermination, detachment, formalization.",
   "Six steps: mission, objectives, situation analysis, formulation, implementation, control (then loop).",
   "Mission = reason for being; objectives = measurable goals that serve it."],
  [("Mission statement", "A concise statement of an organization's (or person's) reason for being that anchors strategy.", "concept"),
   ("Fallacy of predetermination", "Mintzberg: the false belief that we can predict the future and plan for one line of events.", "concept"),
   ("Fallacy of detachment", "Mintzberg: planners removed from the action, separating formulation from implementation.", "concept"),
   ("Fallacy of formalization", "Mintzberg: the plan ossifies in a binder and drifts away from reality.", "concept"),
   ("Supervise and refine", "Military dictum for implementation: don't issue orders and assume they're executed.", "concept"),
   ("Henry Mintzberg", "Contrarian management scholar; critic of rigid strategic planning; 'successful companies are not boring.'", "person"),
   ("Robert McNamara", "Led the ex-military team at Ford; brought formal planning to the Pentagon as Kennedy's defense secretary.", "person")],
  [("mc", "What is the correct order of the six-step process?",
    ["Objective, mission, strategy, analysis, control, implementation",
     "Mission, objective, situation analysis, strategy formulation, implementation, control",
     "Situation analysis, mission, objective, implementation, strategy, control",
     "Mission, strategy formulation, objective, control, implementation, analysis"], 1,
    "Mission, objective, situation analysis, formulation, implementation, control, then loop back."),
   ("mc", "The 'binder on the shelf' describes which fallacy?",
    ["Predetermination", "Detachment", "Formalization", "Overreach"], 2,
    "Formalization: the plan ossifies and drifts from what the company actually does."),
   ("tf", "In McKinsey's 1978 scheme, the highest phase is forecast-based planning.", False,
    "The highest is strategic management, which welds planning and management together."),
   ("mc", "When the control step signals trouble, you should loop back to:",
    ["Mission", "Situation analysis", "Implementation", "Objectives only"], 1,
    "Check whether environmental factors have changed."),
   ("mc", "According to Porter, the proper timeframe for strategic planning may be:",
    ["One quarter", "One budget cycle", "A decade or more", "Exactly three years"], 2,
    "A single budget cycle is usually too short for a strategy to work."),
   ("tf", "A mission is the reason for being; objectives are the measurable goals set to fulfill it.", True,
    "If your mission is to heal the sick, objectives might be degrees, residencies, a practice."),
  ],
  ("The café that plans by spreadsheet",
   """A café owner does 'strategic planning' every December: take this year's revenue, add 8%, set the budget, put the document in a folder. Last year a chain opened nearby and foot traffic fell 20% by spring, but the plan wasn't revisited until the next December. The owner never wrote down what the café is for.""",
   [("Diagnose the problems using Mintzberg's fallacies and McKinsey's phases.",
     """It's stuck in McKinsey's first phase (financial planning as an annual budget). Predetermination: it assumes next year looks like this year plus 8%. Formalization: the plan sits in a folder and isn't consulted. There's no control step, so the chain's arrival didn't trigger a rethink for months. No mission means nothing anchors the objectives."""),
    ("Walk the owner through the six steps in a few lines each.",
     """Mission: e.g. "the neighborhood's living room for remote workers." Objectives: 60 regulars with a weekly pass by June; 25% of revenue from laptop-hours packages. Situation analysis: chain nearby (cheaper, faster), remote-worker growth, our strengths (space, quiet, owner knows names). Formulation: don't compete on speed; invest in seating, power, a quiet room. Implementation: owner checks in weekly, assigns tasks. Control: monthly review of regulars and revenue mix; if off-track, re-scan the environment.""")]),
  ["Do you have a personal mission statement? Write one now and ask honestly whether it inspires you.",
   "Compare your employer's (or school's) mission statement with what it actually does. Measure the gap between slogan and action.",
   "Sketch the six steps for one long-term personal goal."]),

L(8, "Which Business Strategy? Fundamental Choices",
  "You compete either on low cost or on difference. If you can choose, choose difference.",
  [
   ("Two umbrellas (and one offshoot)", """
<p>Following Porter, every competitor travels under one of two umbrellas: <b>cost leadership</b> or <b>differentiation</b>. Within them you can apply tactics, target segments or focus on parts of the value chain. <b>Focus</b> is the offshoot: serving a narrow segment, by cost or by difference.</p>
"""),
   ("Cost leadership", """
<p>Sell at the lowest price the market will bear and profit on volume, attracting value-conscious buyers. <b>Walmart</b>: volume, volume discounts, squeeze suppliers, pass savings on. In 2007 it drifted upmarket, dropped 300+ low-price items, alienated its base, and returned to the formula in 2011. <b>Netflix</b> (2011) raised prices and split streaming from mail and lost over a million subscribers in six months.</p>
<p>Commodities like cement almost force price competition: low margins, fierce rivalry. Many job seekers unknowingly choose low cost by presenting themselves as interchangeable commodities. A chiropractor who specializes in athletes' low back pain escapes commodity pricing.</p>
<p>Military parallel: WWI armies all competed on "low cost," producing undifferentiated, bloody stalemate until the <b>tank</b> broke it. In WWII Germany differentiated with elite divisions; the U.S. and USSR spread quality evenly and won on volume. That success convinced many postwar U.S. firms that low-price/high-volume was the only way.</p>
"""),
   ("Differentiation", """
<p>Offer something unique and valuable beyond low price: a <b>unique selling proposition (USP)</b>. The common error is blurring the proposition to "do more things" for more people until the brand means nothing. Rolex and Casio both sell watches but don't compete; the Tata Nano (under $3,000) and Lexus LS460 ($75,000) both sell cars. Differentiation means specializing, adding features, delivering crucial service superbly, and building a <b>reputation or aura</b> (Nike).</p>
<p>Military: the U.S. ended Cold War volume competition (ICBMs, bombers, subs) with the Strategic Defense Initiative (1983), using research and economic advantages the Soviets couldn't imitate.</p>
<p>Differentiating a commodity is the hardest trick. <b>Starbucks</b> differentiated coffee by how it's served: a European-style "lifestyle" destination. When it broadened its format (2007) it lost distinctiveness; Schultz returned in 2008 and refocused on the USP.</p>
"""),
   ("Focus", """
<p>Focus is hyper-differentiation for a narrow market: ethnic grocers, ultra-high-end cars, <b>Equal Exchange</b> (fair-trade coffee for buyers motivated by social justice; small, stable, profitable niche), and <b>Jolt Cola</b> ("All the sugar, and twice the caffeine") targeting rebels against the health trend.</p>
"""),
   ("Differentiating yourself", """
<p>Inventory your resources and capabilities and check <b>strategic fit</b> with your intentions. Then write a <b>personal USP</b>: one sentence describing what you offer that few can match. Do it for a trusted friend too, and swap.</p>
"""),
  ],
  ["Two generic strategies: cost leadership and differentiation; focus is an offshoot.",
   "Low-cost players that drift from their formula get punished (Walmart 2007, Netflix 2011).",
   "Commodity thinking traps people too: job seekers who sell themselves on 'price.'",
   "Differentiation = USP; blurring it dilutes the brand (Starbucks 2007).",
   "Check strategic fit and write a one-sentence personal USP."],
  [("Cost leadership", "Competing by selling at the lowest price the market bears and profiting on volume.", "concept"),
   ("Differentiation", "Competing by offering something unique and valuable beyond low price.", "concept"),
   ("Focus strategy", "Serving a narrow, sharply defined segment better than anyone, via cost or differentiation.", "concept"),
   ("Unique selling proposition (USP)", "The distinctive value you offer that competitors can't easily match.", "concept"),
   ("Strategic fit", "Alignment between your resources and capabilities and your intentions.", "concept")],
  [("mc", "Rolex and Casio illustrate that:",
    ["All watchmakers compete on price", "Well-differentiated products may not compete at all", "Focus always beats differentiation", "Luxury brands should cut prices"], 1,
    "Each offers a different value; they serve different buyers."),
   ("mc", "Equal Exchange's fair-trade coffee is an example of:",
    ["Cost leadership", "Focus", "Frontal assault", "A red ocean"], 1,
    "A niche strategy targeting customers motivated by social justice."),
   ("tf", "Walmart's 2007 move upmarket strengthened its core strategy.", False,
    "It alienated its base customers; Walmart returned to its formula in 2011."),
   ("mc", "How did Starbucks differentiate a commodity?",
    ["Cheaper beans", "The way coffee is served: a lifestyle destination", "Faster drive-throughs", "Only selling decaf"], 1,
    "A European-style coffee house experience."),
   ("mc", "Job seekers who present themselves like everyone else are, per Ridgley:",
    ["Following a focus strategy", "Unwittingly choosing a low-cost strategy", "Using the indirect approach", "Building strategic intent"], 1,
    "They advertise themselves as commodities and end up competing on price."),
   ("tf", "In WWI the tank was a differentiation move that broke an undifferentiated stalemate.", True,
    "All sides had been competing 'on volume' until the tank."),
  ],
  ("The freelance translator",
   """Mira is a freelance German-English translator on a platform with 4,000 other German-English translators. Clients filter by price, and she keeps lowering her rate to win jobs. She has a law degree, spent two years in a Swiss bank's compliance team, and loves writing.""",
   [("Which strategy is Mira currently following, and why is it a trap?",
     """Unwittingly, cost leadership: she's a commodity among 4,000 others competing on price, with low margins and endless rivalry. She can't win a price war against people with lower costs of living or machine translation."""),
    ("Write Mira a personal USP and say whether it's differentiation or focus.",
     """"I translate Swiss and German financial-compliance and legal documents into English that a regulator would sign off on, because I've worked inside a Swiss bank's compliance team." It's a focus strategy (narrow segment: finance/legal compliance, DACH region) built on genuine differentiation (law degree plus insider experience). She should leave the general platform and price on value, e.g. per project.""")]),
  ["How do you compete professionally: doing the same thing as everyone, faster, or combining a skill set no one else has? List the components.",
   "When you hear Nike charges a premium, do you say 'it's not worth it' or 'what's the formula'? Apply the second question to yourself.",
   "If you launched a coffee brand tomorrow, what mix of attributes, service, brand and distribution would set it apart?"]),

L(9, "Your Competitive Advantage—Find the Blue Ocean",
  "Stop fighting in the red ocean. Eliminate, reduce, raise, create.",
  [
   ("Madonna as strategist", """
<p>Madonna arrived in New York in 1977 unknown, and her 1983 debut seemed to come from nowhere. It didn't: she set a core mission and objectives, held relentless strategic intent, and carved out uncontested space with a USP and personal brand unlike anyone's. She didn't benchmark; she studied the competition coolly to find empty space.</p>
"""),
   ("Red oceans vs. blue oceans", """
<p>Many think competition means doing the same thing better: benchmarking and best practices. Do only that and you play a game of <b>mimicry</b>. W. Chan Kim and Renée Mauborgne (INSEAD), in <b>Blue Ocean Strategy</b>, describe <b>red oceans</b> (competitors fighting over a shrinking profit pool, commodity margins) and <b>blue oceans</b> (uncontested market space created by differentiating in ways that matter to a target market).</p>
"""),
   ("The value curve and the Four Actions Framework", """
<p>A <b>value curve</b> plots how an offer performs across an industry's accepted factors of competition (for cars: price, prestige, mileage, size, comfort, performance, longevity, safety, service). The conventional model competes on all of them. The blue ocean approach questions the factors themselves:</p>
<ol>
<li><b>Eliminate</b>: which factors the industry takes for granted should go?</li>
<li><b>Reduce</b>: which should drop well below the standard?</li>
<li><b>Raise</b>: which should rise well above it?</li>
<li><b>Create</b>: which should exist that the industry never offered?</li>
</ol>
<p>Tata's Nano ignored most car factors and bet on price for the ignored bottom of the pyramid.</p>
"""),
   ("[yellow tail]", """
<p>Wine competed on price, intriguing terminology, high-visibility marketing, aging quality, vineyard prestige, complexity and range. Casella Wines <b>eliminated</b> the jargon and complexity (even different bottles for red and white), <b>reduced</b> range (one red, one white at first), <b>raised</b> fun (a bright kangaroo label, lowercase name in brackets) and <b>created</b> easy drinking, ease of selection, and fun and adventure. It grew the market itself by attracting new wine drinkers and prospered during an industry dip, later adding a few offerings that reinforced the USP.</p>
"""),
   ("Personal blue oceans and your brand", """
<p>A résumé of experience and eagerness isn't a blue ocean. Ridgley's provocations: the manager blamed for the failed 1993 Diet Coke campaign (which cost Lintas the Coke account) could have owned it, becoming "the manager who lost the Coke account" and turning that into insight, a book, TV commentary. Or join BP at its 2010 low point and build a brand as part of the turnaround. Risky, but the point is to <b>untrain conventional thinking</b> and stop needing external validation; truly new ideas look odd at first.</p>
<p>You'll be labeled by others anyway, so take control. Your <b>brand is your reputation</b>: Mercedes means quality, Volvo means safety. What does your name mean?</p>
"""),
  ],
  ["Benchmarking alone = mimicry in a red ocean.",
   "Blue ocean = uncontested space created by redefining the factors of competition.",
   "Four Actions: eliminate, reduce, raise, create; they redraw the value curve.",
   "[yellow tail] grew the market by making wine simple and fun.",
   "Your personal brand is your reputation; shape it before others do."],
  [("Red ocean", "A crowded market where competitors fight over a shrinking profit pool with commodity margins.", "concept"),
   ("Blue ocean", "Uncontested market space created by differentiating in ways a target market values.", "concept"),
   ("Value curve", "A plot of how an offer performs across an industry's accepted factors of competition.", "concept"),
   ("Four Actions Framework", "Kim and Mauborgne's eliminate/reduce/raise/create questions for building a new value curve.", "concept"),
   ("Personal brand", "Your reputation: what people think first when they hear your name.", "concept"),
   ("Kim and Mauborgne", "INSEAD professors W. Chan Kim and Renée Mauborgne, authors of Blue Ocean Strategy.", "person")],
  [("mc", "Which is NOT one of the Four Actions?",
    ["Eliminate", "Reduce", "Benchmark", "Create"], 2,
    "Eliminate, reduce, raise, create. Benchmarking is red-ocean behavior."),
   ("mc", "What did [yellow tail] create that the wine industry didn't offer?",
    ["Vineyard prestige", "Aging quality", "Easy drinking and fun", "A wider range"], 2,
    "It created easy drinking, ease of selection, and fun and adventure."),
   ("tf", "[yellow tail] grew mainly by stealing share from prestige wines.", False,
    "It grew the market by attracting new wine drinkers."),
   ("mc", "A red ocean is characterized by:",
    ["Uncontested space", "Competitors fighting over a shrinking profit pool", "High margins", "No benchmarking"], 1,
    "Low margins, high stress, commodity survival."),
   ("mc", "The 'manager who lost the Coke account' example teaches:",
    ["Avoid all risk", "Unconventional thinking can create a unique personal brand", "Blame others quickly", "Benchmark competitors"], 1,
    "Owning the failure could become a bold, unique selling proposition."),
   ("tf", "A value curve shows performance across an industry's accepted factors of competition.", True,
    "Blue ocean strategy redraws it by questioning those factors."),
  ],
  ("The language school",
   """A language school competes with dozens of others on the same factors: number of languages offered, certified teachers, textbook quality, classroom location, exam-prep certificates and price. Its adult students mostly want to have real conversations on trips and at work, and many quit after two months because classes feel like school.""",
   [("Apply the Four Actions Framework to design a blue ocean offer.",
     """Eliminate: textbooks and grammar-drill homework; maybe the downtown classroom. Reduce: number of languages (focus on the three most-requested), formal certification emphasis. Raise: speaking time per student, schedule flexibility. Create: real-world 'missions' (order at a partner restaurant, a mock job interview), conversation clubs with native speakers, a 'trip-ready in 8 weeks' guarantee."""),
    ("Who is the new customer this attracts, and why is it uncontested?",
     """Adults who don't think of themselves as 'students' and were never served by schools: travelers and professionals who hate classrooms. It's uncontested because rivals still compete on certifications and textbooks; the school now competes on outcomes like confidence and speaking that the others don't measure.""")]),
  ["Pick two competing products, a leader and an also-ran. What metrics do people judge them on, and what explains the gap?",
   "Take a recent corporate PR disaster. What opportunity hides in it if you had to swim in those waters?",
   "What tagline does your name currently evoke? What do you want it to evoke?"]),

L(10, "Strengths, Weaknesses, Opportunities, Threats",
  "Act from knowledge, not impressions: PEST, five forces, value chain, then SWOT ties them together.",
  [
   ("Copperfield's Books and the great wheel", """
<p>Copperfield's Books (northern California, founded 1981) grew for 13 years, then stagnated in 1995. It sold the same products in the same places, but the environment had turned: megastores, Amazon, e-readers. Strategic thinking means replacing impressions with orderly reasoning about causes and effects. Four tools help.</p>
"""),
   ("PEST: scanning the outside", """
<ul>
<li><b>Political</b>: government and regulation (zoning, tax, approval rules), and personally, the web of power relationships at work and home. The political tide shifts; swim with it.</li>
<li><b>Economic</b>: are there enough customers willing to pay? Does the economy favor you or rivals?</li>
<li><b>Social</b>: trends, fads, and deep long-term cultural factors; spot tomorrow's trends in today's indicators.</li>
<li><b>Technological</b>: does technology support your plan or threaten it?</li>
</ul>
"""),
   ("Porter's five forces", """
<p>Usable, with tweaks, from computer industries to romantic relationships:</p>
<ul>
<li><b>Buyer power</b>: Copperfield's customers could buy identical books anywhere on price; little loyalty. High.</li>
<li><b>Supplier power</b>: publishers gave chains volume discounts independents couldn't get. High for independents.</li>
<li><b>Rivalry</b>: mature, low-growth industry with megastore consolidation. Intense.</li>
<li><b>Threat of substitutes</b>: libraries, online, nonspecialist stores, TV, games. High.</li>
<li><b>Threat of new entrants</b>: capital needs and low margins made it unattractive. Low.</li>
</ul>
<p>Verdict: time to change the business model.</p>
"""),
   ("Value chain: looking inside", """
<p>Break an organization into its value-producing activities to see what makes it strong or weak. A football team's win-loss record hides the contribution of each unit; disassemble offense, defense, coaching and personnel decisions against the mission. Do the same with your <b>personal value chain</b>. Firms and people <b>outsource</b> what they don't do well (Borders let Starbucks run its cafés; you don't sew your own clothes).</p>
"""),
   ("SWOT: putting it together", """
<p>Value chain gives internal <b>strengths and weaknesses</b>; PEST and five forces give external <b>opportunities and threats</b>. SWOT combines them. For Copperfield's, a changing environment turned an old strength (thoughtful selection) into a weakness (lack of choice). Its answer: a uniquely local persona with book-buying and social experiences unavailable online or in megastores. <b>Borders</b>, an apparent winner, then failed to adapt: it outsourced online sales to Amazon, missed e-readers, and lost its Starbucks contract to Barnes & Noble. Same pressures, different responses.</p>
"""),
  ],
  ["PEST scans the external macro environment.",
   "Five forces: buyers, suppliers, rivalry, substitutes, new entrants.",
   "Value chain reveals internal strengths and weaknesses; outsource non-core activities.",
   "SWOT unites internal (S, W) and external (O, T).",
   "Environment change can flip a strength into a weakness (Copperfield's selection)."],
  [("PEST analysis", "A scan of the political, economic, social and technological environment.", "concept"),
   ("Five forces", "Porter's model: buyer power, supplier power, rivalry, threat of substitutes, threat of new entrants.", "concept"),
   ("Value chain", "Breaking an organization (or person) into value-producing activities to find strengths and weaknesses.", "concept"),
   ("SWOT", "Strengths and weaknesses (internal) combined with opportunities and threats (external).", "concept")],
  [("mc", "Which tool looks inside the organization?",
    ["PEST", "Five forces", "Value chain", "Scenario analysis"], 2,
    "Value chain analysis evaluates internal activities; PEST and five forces look outward."),
   ("mc", "For Copperfield's Books, which force was LOW?",
    ["Buyer power", "Supplier power", "Threat of new entrants", "Threat of substitutes"], 2,
    "Capital requirements and low margins made entry unattractive."),
   ("tf", "In SWOT, opportunities and threats come from the external environment.", True,
    "S and W are internal; O and T are external."),
   ("mc", "What did Copperfield's do to survive?",
    ["Matched Amazon's prices", "Built a local persona with experiences unavailable online", "Became a megastore", "Outsourced sales to Amazon"], 1,
    "A uniquely local, social book-buying experience."),
   ("mc", "Which was one of Borders' mistakes?",
    ["Investing early in e-readers", "Outsourcing its online sales to Amazon", "Running its own cafés", "Going local"], 1,
    "It also missed e-readers and lost its Starbucks deal to Barnes & Noble."),
   ("tf", "A changing environment can turn a former strength into a weakness.", True,
    "Copperfield's thoughtful selection became 'relative lack of choice.'"),
  ],
  ("Career SWOT for a new graduate",
   """Jonas just finished a business degree in Switzerland. He speaks German, English and Spanish, built a small e-commerce side business, but has weak Excel/data skills and no corporate internship. AI tools are automating junior analyst tasks, Swiss firms are expanding into Latin America, and hiring for generic junior roles is slow.""",
   [("Build Jonas's SWOT.",
     """Strengths: trilingual (incl. Spanish), real e-commerce experience, entrepreneurial initiative. Weaknesses: weak Excel/data skills, no corporate internship. Opportunities: Swiss firms expanding into Latin America; demand for people who can work with AI tools. Threats: AI automating junior analyst tasks; slow hiring for generic roles."""),
    ("What strategy does the SWOT suggest? Connect specific S/O and W/T pairs.",
     """S+O: market himself to Swiss firms entering Latin America as the bridge (language plus hands-on commerce), a differentiated rather than generic junior. W+T: close the data gap fast and learn to use AI tools to do analyst work faster, so automation becomes leverage rather than a replacement. Avoid the generic-junior red ocean.""")]),
  ["Scan your own environment (PEST), then inventory your personal value chain honestly. What actions follow?",
   "Use PEST to explain what drove Apple and Amazon into competition over e-readers and tablets.",
   "Apply value-chain thinking to a team or company you follow. What strategy does it suggest?"]),

L(11, "Avoid the Pathologies of Execution",
  "Five ways good plans die: no one responsible, overreach, broken communication, bad intelligence, inertia.",
  [
   ("Operation Market Garden", """
<p>September 1944: Montgomery's plan to seize six bridges behind German lines up to Arnhem and end the war. Its built-in flaw: <b>everything had to go right</b>. The Allies believed German resistance had broken; two panzer divisions were resting and refitting nearby, one at Arnhem itself. After nine days, withdrawal. The planners underestimated the enemy, overestimated themselves, and built a plan too tightly wound, with too many objectives, moving parts and coordination needs, plus wishful thinking that hid red flags.</p>
"""),
   ("The five pathologies", """
<ol>
<li><b>Omission of responsibility</b>: nothing happens when no one is responsible. Planners don't connect plans to specific tasks; the classic planning-execution gap.</li>
<li><b>Overreach</b>: capabilities and strategy don't align (Market Garden; Germany's Battle of the Bulge plan, which also needed everything to go right and underestimated the enemy's ability to interfere).</li>
<li><b>Communication and coordination breakdown</b>: the <b>Charge of the Light Brigade</b> (Balaklava, 1854). A vague order to "advance rapidly to the front... to prevent the enemy carrying away the guns" didn't say which guns; the cavalry charged straight at massed Russian artillery.</li>
<li><b>Poor intelligence</b>: the <b>Dieppe raid</b> (1942). Unclear objective ("learn lessons"), resurrected by Mountbatten without authorization, months-old intelligence, beach assessed from <b>holiday snapshots</b>, hidden German guns unknown, insufficient naval support and no bombing for political reasons. Only 15 tanks got off the beach; the Germans had been expecting a landing for weeks.</li>
<li><b>Inertia</b>: a body in motion stays on course, especially when egos and careers are invested. At the <b>Somme</b> (1916), a seven-day barrage warned the Germans and failed to destroy their defenses, yet Rawlinson let the attack proceed: 60,000 British casualties on the first day.</li>
</ol>
"""),
   ("Control: strategy is not autopilot", """
<p>Jack Welch spent a full week every year, for 20 years, reviewing each GE unit's operating plan. You can't publish strategy and wait. Assign responsibility, avoid overreach, communicate clearly, nurture intelligence, and reject inertia when new information arrives. <b>Strategy is a process, not an event.</b> A decision has no effect unless <b>action commitments</b> are built in from the start; grand strategy must be translated into unit-level steps, with follow-through, checks and some "management by walking around."</p>
"""),
  ],
  ["Plans that need everything to go right will fail.",
   "Five pathologies: no responsibility, overreach, communication breakdown, poor intelligence, inertia.",
   "Vague orders kill (Light Brigade); stale intelligence kills (Dieppe); sunk-cost momentum kills (Somme).",
   "Build action commitments and named owners into every decision.",
   "Control mechanisms (Welch's reviews) keep strategy alive."],
  [("Overreach", "When strategy demands more than your capabilities can deliver, often from underestimating the opponent.", "concept"),
   ("Omission of responsibility", "No one is assigned to execute, so nothing happens; the gap between planning and execution.", "concept"),
   ("Inertia (strategic)", "The tendency to stay on a set course, especially when egos are invested, even as it fails.", "concept"),
   ("Action commitment", "A specific, owned task built into a decision so that it actually takes effect.", "concept"),
   ("Operation Market Garden", "1944 Allied plan to seize six bridges to Arnhem; failed through overreach and poor intelligence.", "concept")],
  [("mc", "The Charge of the Light Brigade is the course's example of:",
    ["Inertia", "Communication breakdown", "Overreach", "Omission of responsibility"], 1,
    "A vague order didn't specify which guns, so the cavalry charged the wrong way."),
   ("mc", "British planners assessed the Dieppe beach using:",
    ["Satellite images", "Holiday snapshots", "Spies on the ground", "Captured German maps"], 1,
    "Months-old, unreliable intelligence, including tourist photos."),
   ("tf", "At the Somme, Rawlinson canceled the attack when the barrage failed to destroy German defenses.", False,
    "He let inertia take over and ordered the attack to proceed: 60,000 casualties."),
   ("mc", "Market Garden's 'built-in disadvantage' was that:",
    ["It was too simple", "It required everything to go right", "It had no objective", "It used no airborne troops"], 1,
    "Tightly wound plans with many moving parts break at the first surprise."),
   ("mc", "Jack Welch's annual week of plan reviews illustrates:",
    ["Control", "Surprise", "Overreach", "Economy of force"], 0,
    "A control mechanism to steer strategy to completion."),
   ("tf", "Per the lecture, a decision won't take effect unless action commitments are built in from the start.", True,
    "If a decision is no one's specific work and responsibility, nothing happens."),
  ],
  ("The app relaunch",
   """A team of five plans to relaunch their app in six weeks: new design, new payment system, a partnership with a bank that hasn't signed yet, launches in three countries, and a marketing campaign. The CEO's kickoff email says "Let's all make this happen!" with no owners named. Two weeks in, user tests show people hate the new design, but the CEO says it's too late to change direction.""",
   [("Which pathologies are present? Name at least four with evidence.",
     """Omission of responsibility: no owners, just 'let's all make this happen.' Overreach: five people, six weeks, five major workstreams; it needs everything to go right (the bank hasn't signed). Poor intelligence: assumes the bank deal and three markets without validation. Inertia: ignoring negative user tests because 'it's too late.' Likely communication breakdown too, with vague goals and no coordination plan."""),
    ("What control mechanism and changes would you put in place?",
     """Cut scope to what five people can do (one country, design fix, payments only if the bank signs: a branch plan). Name an owner and deadline for each workstream. Weekly 30-minute review against simple metrics, with pre-agreed triggers ("if user test scores are below X, we revise the design") so new information changes course instead of being rationalized away.""")]),
  ["Recall a time you were too optimistic about results. Was the plan too tightly wound, with no margin for error?",
   "Find personal examples of each of the five pathologies. Would recognizing them have changed the outcome?",
   "What control mechanism do you use to catch these pathologies early?"]),

L(12, "Tactics of Combat as Problem-Solving Tools",
  "Frontal assault, indirect approach, flank attack, rear area battle: pick the maneuver that fits the situation.",
  [
   ("Strategy vs. tactics, revisited", """
<p>Strategy is the overall plan; tactics execute it. But you can't know in advance which details will become strategic. Intended strategy merges into <b>emergent strategy</b> through execution and responses to competitors. Richard Rumelt: "One person's strategy is another's tactics"; it depends where you sit. Execution is the <b>neglected child of strategy</b>. Ridgley calls the techniques <b>strategic maneuvers</b>.</p>
<p>Maneuvers apply from armies to individuals and from war to business and sports. In fencing they happen faster than conscious thought: you must abandon your line of attack when a better opening appears. Not every maneuver fits every situation.</p>
"""),
   ("Frontal assault", """
<p>An all-out attack on the enemy's front, usually on ground they chose and fortified. If it's your only option, mitigate: on <b>D-Day</b> the Allies had no alternative to the French coast, but deception hid the exact time and place. In business the frontal assault is the <b>price war</b>, and often only customers win. Attacking a strong, prepared enemy head-on violates almost every principle in the course.</p>
"""),
   ("The indirect approach", """
<p>Liddell Hart noted seven of eight frontal assaults in the Civil War failed. Keep opponents guessing between <b>two equally attractive objectives</b>, forcing them to split their forces to defend everything. Sherman's 1864 Georgia campaign kept Johnston unable to fix his objectives. Business: Honda mastered small engines first, then expanded horizontally into cars and caught Detroit napping.</p>
"""),
   ("Turning the flank", """
<p>Move to the enemy's side to dislocate them and force a disruptive response: Napoleon's specialty, MacArthur at Inch'ŏn, Sherman repeatedly forcing Johnston out of prepared positions. Lee's greatest victory, <b>Chancellorsville</b> (1863), paired a demonstration on the Union front with Jackson's march to the unsuspecting right flank.</p>
<p>In business, flanking often means a niche in a leader's blind spot. <b>Royal Crown Cola</b> failed in a frontal assault on Coke and Pepsi but flanked them with Diet Rite (1962), the best-selling soft drink by decade's end. It then failed to concentrate on its winner, tried to compete on both fronts, and Diet Rite faded when Diet Coke arrived.</p>
"""),
   ("Rear area battle", """
<p>Sow confusion behind the lines so no ground feels safe, forcing the opponent to spend resources defending what it thought was won. Commandos, the French Underground and Soviet partisans tied down German troops; German commandos in U.S. uniforms caused confusion at the Bulge. The psychological effect matters as much as the physical. Politics: campaigns strike rivals' home bases. History: the 1864 raid on Washington to relieve Cold Harbor. Business: <b>Fujifilm attacked Kodak in the U.S.</b> in the 1980s; Kodak counterattacked in Japan.</p>
"""),
   ("Which maneuver?", """
<p>It depends on your position, resources, capabilities, risk tolerance and strategic intent. Knit engagements into a coherent whole; tactics without strategy is aimless conflict. Even a battle you'd win isn't worth fighting if it doesn't advance your strategy.</p>
"""),
  ],
  ["Rumelt: strategy vs. tactics depends on where you sit; execution is strategy's neglected child.",
   "Frontal assault = price war; avoid it, or mitigate with deception.",
   "Indirect approach: threaten two objectives to split the defense (Sherman, Honda).",
   "Flank: attack the niche or blind spot, then concentrate on the winner (RC Cola didn't).",
   "Rear area battle: make the opponent defend its home base (Fuji vs. Kodak)."],
  [("Emergent strategy", "The strategy that actually takes shape through execution and responses to events, as opposed to the intended plan.", "concept"),
   ("Frontal assault", "An all-out attack on an opponent's prepared front; in business, the price war.", "concept"),
   ("Turning the flank", "Moving against an opponent's side or blind spot to force a disruptive response.", "concept"),
   ("Rear area battle", "Attacking an opponent's 'safe' ground behind the lines to force it to divert resources.", "concept"),
   ("Richard Rumelt", "Strategy scholar: 'One person's strategy is another's tactics'; firms succeed by inventing or exploiting change.", "person"),
   ("Basil Liddell Hart", "British strategist of the indirect approach; championed the tank after WWI.", "person")],
  [("mc", "In business, the frontal assault usually takes the form of:",
    ["A niche product", "A price war", "A joint venture", "Rebranding"], 1,
    "Often the only winners are consumers."),
   ("mc", "Royal Crown's Diet Rite was a successful:",
    ["Frontal assault", "Flank attack", "Rear area battle", "Retreat"], 1,
    "It flanked Coke and Pepsi with the first national diet soda."),
   ("tf", "RC Cola concentrated its resources on Diet Rite once it led the market.", False,
    "It competed on both fronts, let the market choose, and Diet Rite faded after Diet Coke."),
   ("mc", "Fujifilm attacking Kodak in the U.S. is an example of:",
    ["Rear area battle", "Frontal assault", "Central position", "Focus strategy"], 0,
    "Hitting the rival's home base; Kodak responded in Japan."),
   ("mc", "Keeping two equally attractive objectives in play aims to:",
    ["Simplify your plan", "Force the opponent to split its forces", "Save money", "Avoid maneuver"], 1,
    "A technique of the indirect approach (Sherman in Georgia)."),
   ("tf", "Rumelt argues that whether something is strategy or tactics depends on where you sit.", True,
    "Corporate tactics can be a business unit's strategy."),
  ],
  ("Taking on the incumbent meal-kit brand",
   """A young meal-kit company with limited funds faces a dominant competitor that owns the 'busy families' segment, spends heavily on discounts, and is strongest in big cities. The incumbent ignores vegetarians, small towns, and people with specific medical diets. Investors are pushing the startup to go head-to-head with a bigger discount.""",
   [("Evaluate the investors' suggestion using the lecture.",
     """It's a frontal assault on ground the incumbent chose and fortified, in the form of a price war against a rival with deeper pockets. It violates mass, economy of force and maneuver, and the likely winners are customers, not the startup."""),
    ("Propose a flank or indirect approach, and say what the startup must do once it works.",
     """Flank: own a blind spot, e.g. kits for medical diets (diabetic, low-FODMAP) or small-town delivery. Indirect: threaten two attractive niches so the incumbent can't defend both. Once one niche clearly wins, concentrate resources there (the RC Cola lesson) and fortify it before the incumbent copies it, rather than spreading across fronts.""")]),
  ["Do you always respond to problems the same way? Pick one maneuver you've never used and try it at the next opportunity.",
   "What options did Lee have on the third day of Gettysburg besides Pickett's frontal charge?",
   "Where could you create a new threat in an area your opponent thinks is secure?"]),
]
