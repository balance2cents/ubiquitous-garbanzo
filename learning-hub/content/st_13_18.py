from _dsl import L

LECTURES = [

L(13, "Shock of the New—Inflection Points",
  "Some changes are hiccups; some change the rules of the game. Senior leaders usually spot the second kind last.",
  [
   ("What a strategic inflection point is", """
<p>Andy Grove (Intel) coined the term in <b>Only the Paranoid Survive</b> (1996): a dramatic change in your environment that forces you to change how you operate or risk extinction. The advantage goes to whoever recognizes and responds first, which connects back to PEST and five forces scanning. But advantage is temporary: the response diffuses, becomes best practice, and one firm's edge becomes everyone's parity.</p>
"""),
   ("In business", """
<p>Causes: technology, shifts in competition, customer preferences, regulation, raw-material prices. Grove warns senior management usually recognizes them <b>last</b>.</p>
<ul>
<li><b>Talkies</b>: within a decade of sound films, silent film production had stopped.</li>
<li><b>Airline deregulation (1978)</b>: freedom on fares, routes and entry was a bounty for consumers, but legacy airlines kept doing business as usual.</li>
<li><b>Kodak and Polaroid</b>: digital imaging ended chemical film fast. Polaroid went bankrupt in 2001; Kodak sought bankruptcy protection in 2012.</li>
</ul>
<p>The counterexample: <b>Richard Harrington</b> became CEO of Thomson Corporation in 1997, a profitable publishing grab bag with nearly $9 billion revenue. Seeing electronic publishing coming, he accepted a short-term earnings hit, spent $7 billion on 200+ businesses, shed 130+ regional newspapers, and within five years was challenging Elsevier in professional publishing.</p>
"""),
   ("In games, sports and politics", """
<p>Rule changes are inflection points, sometimes built from small steps: the <b>chess queen</b> was weak until rule changes in the 15th to 16th centuries made her the strongest piece, forcing new strategy. Football rule tweaks changed which players get recruited.</p>
<p>In politics: the two-term presidential limit created lame ducks; nomination power moved from conventions to primaries; new media (FDR on radio, Kennedy and Reagan on TV, Obama on the internet in 2008) reshaped campaigns. Even non-tech sectors face technology inflection points.</p>
"""),
   ("In war: the Crusades and the Mongols", """
<p>The First Crusade (1095) hit Arab and Turkish armies with armor, heavy horses, siege machines and the <b>crossbow</b>, a technological and tactical surprise. In 1241 the Europeans were on the receiving end: Batu Khan's Mongols, with speed, unique supply, spies and scouts, and leaders protected at a distance, crushed the Hungarians. Only the death of the Great Khan Ögödei broke the invasion's tempo: fortune, not European adaptation, saved Europe.</p>
"""),
   ("Spotting your own inflection points", """
<p>The hard part is telling an inflection point from a historical hiccup, especially since we resist change. Grove's warning signs:</p>
<ul>
<li>The key firm or player you deal with seems to have "<b>shifted</b>."</li>
<li>Your attention moves away from a lifelong competitor toward someone or something <b>new</b>.</li>
<li>The <b>silver bullet test</b>: if you had one bullet, where would you aim? If the answer has changed, it's more than a minor shift.</li>
</ul>
"""),
  ],
  ["A strategic inflection point changes the rules; respond or risk extinction.",
   "First responders gain advantage, but it erodes into parity.",
   "Leaders often see it last (Kodak, legacy airlines); bold reinvention works (Thomson).",
   "Rule changes are inflection points too (the chess queen, primaries).",
   "Grove's tests: things have 'shifted'; a new competitor worries you; your silver bullet changes target."],
  [("Strategic inflection point", "Grove: a dramatic change in the environment that forces a change in strategy or risks extinction.", "concept"),
   ("Silver bullet test", "Grove's question: if you had one bullet, which competitor would you aim at? A changed answer signals an inflection point.", "concept"),
   ("Competitive parity", "When an advantage has diffused and become standard practice, so no one gains from it.", "concept"),
   ("Andy Grove", "Intel leader; author of Only the Paranoid Survive (1996), which named strategic inflection points.", "person"),
   ("Richard Harrington", "Thomson CEO (from 1997) who transformed it into an electronic professional publisher.", "person"),
   ("Genghis Khan", "Founder of the Mongol Empire who revolutionized 13th-century warfare.", "person")],
  [("mc", "Who coined 'strategic inflection point'?",
    ["Michael Porter", "Andy Grove", "Henry Mintzberg", "Clayton Christensen"], 1,
    "In Only the Paranoid Survive (1996)."),
   ("tf", "According to Grove, senior management usually recognizes inflection points first.", False,
    "They usually recognize them last."),
   ("mc", "What did Thomson's Harrington do?",
    ["Doubled down on regional newspapers", "Took a short-term hit to move into electronic publishing", "Sold the company", "Waited for competitors to move"], 1,
    "$7 billion in acquisitions and 130+ newspapers shed."),
   ("mc", "The chess queen example shows that inflection points can:",
    ["Only come from technology", "Build up from a series of small rule changes", "Be predicted exactly", "Never affect games"], 1,
    "Gradual rule changes made her the most powerful piece."),
   ("mc", "What stopped the Mongols from pushing deeper into Europe in 1241?",
    ["European adaptation", "The death of the Great Khan Ögödei", "The crossbow", "Winter"], 1,
    "Fortune, not adaptation, broke the invasion's tempo."),
   ("tf", "Competitive advantage from responding to an inflection point tends to be temporary.", True,
    "It diffuses and becomes best practice, then parity."),
  ],
  ("The translation agency and AI",
   """A 30-person translation agency had record revenue last year. This year, three long-time clients started running first drafts through AI and only buying 'review' services at half the price. A new competitor offering AI-plus-human editing at 40% lower prices keeps coming up in sales calls. The founder says it's a blip and that quality always wins.""",
   [("Apply Grove's warning signs. Is this an inflection point?",
     """Yes, very likely. Clients have 'shifted' (buying review instead of translation). Attention has moved to a new competitor that wasn't on the radar. Silver bullet: a year ago they'd aim at the other big agency; now they'd aim at the AI-hybrid firm. All three signals fire, and the founder's 'blip' framing is the classic senior-management-sees-it-last pattern, made worse by record revenue last year."""),
    ("What would a Harrington-style response look like?",
     """Accept a short-term earnings hit to rebuild the model: invest in an AI-plus-expert workflow, retrain translators as editors and domain specialists, reprice around speed and accuracy guarantees, and drop low-value general work while doubling down on high-stakes domains (legal, medical) where human review is required. Act before parity sets in.""")]),
  ["How could a company overcome blindness to inflection points when times are good?",
   "Treat an inflection point as a rule change. What written and unwritten rules govern your competitive interactions, and could a new behavior within them give you an edge?",
   "What do the rules of your game allow that nobody is doing yet?"]),

L(14, "Surprise! Perils and Power of Strategic Deception",
  "Surprise multiplies force; deception multiplies surprise. Five kinds: intention, time, place, strength, style.",
  [
   ("Stratagem and surprise", """
<p>From the Trojan Horse to Pearl Harbor, Inch'ŏn and Schwarzkopf's "left hook" (1991), surprise is the goal and the <b>stratagem</b> (a trick to deceive the enemy) is the means. No other principle multiplies combat power as well. Great commanders from Hannibal to Stonewall Jackson used it. Between 1900 and WWII it fell out of favor, except for unconventional leaders like <b>T. E. Lawrence</b> (Arab Revolt, 1916 to 1918) and <b>Churchill</b>, a lover of deception and new technology.</p>
"""),
   ("Strategic vs. tactical surprise", """
<p>Strategic surprise disrupts an enemy's mobilization, deployment and grand strategy; it is far harder because of scale, variables, time and chance of discovery. A failed strategic surprise can still be a tactical one, with much less impact.</p>
<p>The <b>tank in 1916</b>: Lt. Col. Ernest Swinton wanted tanks kept secret and used en masse to break through and hit enemy artillery. Generals ignored him and fed 32 tanks piecemeal across a broad front at the Somme: a little local panic, a minor tactical success, and a game-changing secret wasted. You only get <b>one first use</b> of a powerful new weapon.</p>
"""),
   ("What surprise really is", """
<p>Surprise is the <b>gap between what we expect and what happens</b>, deliberately created and exploited. Enemies don't just add uncertainty; deception gives you false certainty, false expectations or diverted attention. At Troy, the hollow horse was only half the trick: burning their camp and appearing to leave created the false expectation that made the horse work.</p>
<p>Tactical surprise pays out of all proportion to effort; strategic surprise is rarer but can deliver short- and long-term wins. Stealth and ambiguity help, but <b>deception is the amplifier</b>.</p>
"""),
   ("Five types of surprise", """
<ol>
<li><b>Intention</b>: will they strike at all? The yes/no gateway to all others.</li>
<li><b>Time</b>: Pearl Harbor, while Japan's ambassador sought talks with Cordell Hull; Philip IV's arrest of the Knights Templar (1307); the Night of the Long Knives (1934); the political "October surprise."</li>
<li><b>Place</b>: Operation Bodyguard convinced Germany D-Day would hit the Pas-de-Calais; in 1991 a threatened Marine landing pinned Iraqi forces while the left hook swept through the desert.</li>
<li><b>Strength</b>: the Mongols showed only part of their force to lure attacks, appeared from flanks and rear, or faked size with extra campfires and dust clouds dragged by horses.</li>
<li><b>Style</b>: unexpected weapons or methods (the tank, Cannae, Delium). Surprise can be defensive too: Britain's undetected evacuation of Gallipoli.</li>
</ol>
"""),
   ("Sports and the double edge", """
<p>Sports now treat scouting, film study and statistical analysis as part of the game, searching tendencies for weakness. Surprise is a <b>double-edged sword</b>: know the five types so you can see them coming.</p>
"""),
  ],
  ["Surprise is a force multiplier; deception multiplies surprise.",
   "Surprise = a deliberately created gap between expectation and reality.",
   "Five types: intention, time, place, strength, style.",
   "You get one first use of a new weapon; don't waste it piecemeal (tanks, 1916).",
   "Defensive surprise exists (Gallipoli); know the types to defend against them."],
  [("Stratagem", "A trick designed to deceive the enemy in order to achieve surprise.", "concept"),
   ("Strategic surprise", "Surprise that disrupts an opponent's mobilization, deployment and overall strategy; rare and hard.", "concept"),
   ("Force multiplier", "A factor that makes your existing capabilities far more effective, like surprise.", "concept"),
   ("Operation Bodyguard", "Allied deception before D-Day that made Germany expect the invasion at the Pas-de-Calais.", "concept"),
   ("T. E. Lawrence", "'Lawrence of Arabia'; led the Arab Revolt; wrote Seven Pillars of Wisdom on guerrilla tactics.", "person"),
   ("Ernest Swinton", "British officer who championed secret, massed use of the tank; ignored in 1916.", "person")],
  [("mc", "Which surprise type is the 'gateway' to all others?",
    ["Time", "Intention", "Place", "Style"], 1,
    "Whether the enemy intends to strike at all."),
   ("mc", "The Mongols lighting extra campfires is an example of surprise of:",
    ["Strength", "Time", "Intention", "Place"], 0,
    "They masked or exaggerated their numbers."),
   ("tf", "In 1916 the British used tanks en masse, exactly as Swinton advised.", False,
    "Only 32 were fed piecemeal across a broad front, wasting the strategic surprise."),
   ("mc", "Operation Bodyguard targeted which kind of surprise?",
    ["Place", "Style", "Strength", "Intention"], 0,
    "It shaped German expectations about where the invasion would land."),
   ("mc", "The lecture defines surprise as:",
    ["Any random event", "The gap between what we expect and what actually happens", "A sudden attack", "Bad luck"], 1,
    "And strategic surprise is a gap deliberately created and exploited."),
   ("tf", "The British evacuation of Gallipoli is an example of defensive surprise.", True,
    "Surprise isn't only for offensive operations."),
  ],
  ("The product announcement",
   """A startup has built a feature its much larger competitor doesn't have and can't copy for about six months. The team wants to announce it right away in a blog post and on social media 'to build hype,' then release it gradually over three months to small groups of users.""",
   [("What lesson from the 1916 tank story applies here?",
     """You only get one first use of a game changer. Announcing early and releasing piecemeal is the 1916 tank mistake: it tells the competitor what's coming, starts their six-month clock early, and spreads the impact thin, so you get local buzz instead of a breakthrough."""),
    ("Design a launch that uses at least three of the five types of surprise.",
     """Intention: keep the project quiet so the competitor doesn't think you're entering this space. Time: launch right before the competitor's busy season or big conference. Place: launch first in the segment where the competitor is weakest. Strength: release fully to all target users at once with sales and support ready (mass). Style: package it in a way the market doesn't expect, e.g. free for switchers.""")]),
  ["What information do you control exclusively, and would results change if you handled its timing differently?",
   "How might the timing of an announcement, against an opponent's expectations, strengthen your position?",
   "Where have you become so predictable that opponents can counter you easily? Break the routine once on purpose."]),

L(15, "The Sources and Uses of Reliable Intelligence",
  "Intelligence is analyzed information you actually act on. Run the cycle and resist the Cassandra curse.",
  [
   ("The Death Star mistake", """
<p>In Star Wars (1977) an intelligence officer analyzes the rebel attack and advises evacuation; the commander refuses because victory seems near. We want certainty, yet we reject reliable information that conflicts with our biases. Leonard Fuld: actively seek intelligence and learn to use it, and information becomes a weapon.</p>
"""),
   ("What intelligence is", """
<p>Intelligence is <b>analyzed information</b>, not raw information. Spying (human intelligence, "humint") is only one part of intelligence, which is only one part of strategy. NFL teams spend millions on scouting, tendency charts and scenario questions (legal if from open sources; stealing signals is not). Political parties run "opposition research" on tax liens, lawsuits and voting records, timed for maximum effect.</p>
<p>Former CIA analyst <b>Jan Herring's</b> five uses of intelligence analysis: (1) early warning to prevent surprise, (2) supporting decisions, (3) competitor assessment and monitoring, (4) planning and strategy development, (5) supporting collection and reporting.</p>
<p>It targets three elements of friends, enemies and yourself: <b>resources, capabilities, intentions</b>. In football: resources = money, draft picks, contacts; capabilities = developed resources visible as strengths and weaknesses; intentions = how they'll use them against you.</p>
"""),
   ("The intelligence cycle", """
<ol>
<li><b>Planning and priority intelligence requirements</b>: decide what to collect and what to ignore, so research doesn't become endless procrastination.</li>
<li><b>Collection</b>: systematic and multi-source (databases, trade shows, press releases, ex-employees, overheard conversations). Don't rely only on comfortable sources.</li>
<li><b>Analysis</b>: part art; use multiple tools (PEST, five forces, value chain, SWOT, competitor, political risk and scenario analysis). Never rely on one.</li>
<li><b>Dissemination</b>: where many efforts fail by delivering facts without analysis or relevance. Beware "<b>nice-to-know</b>" syndrome; intelligence is perishable.</li>
<li><b>Action</b>: needs courage: "This means we should..."</li>
</ol>
<p>The cycle is virtuous: each turn sharpens the next. Its speed depends on how critical and time-pressed the issue is.</p>
"""),
   ("The Cassandra curse", """
<p>Apollo gave Cassandra prophecy, then cursed her never to be believed. The <b>paradox of leadership</b>: the qualities that make strong senior leaders (confidence, conviction) also make them reject informed advice.</p>
"""),
   ("Antietam, 1862: intelligence without boldness", """
<p>A Union private found a copy of Lee's orders showing his army was split. McClellan saw the chance to destroy Lee and perhaps end the war, but moved too slowly, probably overestimating Lee's strength. Result: indecisive Antietam, the bloodiest day in U.S. military history, and two and a half more years of war. Lesson: when high-quality intelligence arrives, <b>act boldly, correctly and quickly</b>.</p>
"""),
  ],
  ["Intelligence = analyzed, actionable information; spying is a small part.",
   "Assess resources, capabilities and intentions (yours too).",
   "Cycle: requirements, collection, analysis, dissemination, action.",
   "Failure points: 'nice-to-know' dissemination and lack of courage to act.",
   "Cassandra curse / McClellan: great intelligence is wasted without boldness."],
  [("Intelligence", "Information that has been analyzed for relevance to a decision, as opposed to raw facts.", "concept"),
   ("Intelligence cycle", "Planning/requirements, collection, analysis, dissemination, action; repeated to sharpen focus.", "concept"),
   ("Priority intelligence requirements", "The defined questions that decide what information to collect and what to ignore.", "concept"),
   ("Nice-to-know syndrome", "Delivering collected facts without analysis or relevance to action.", "concept"),
   ("Cassandra curse", "Having accurate foresight that no one believes; leaders rejecting intelligence that contradicts their views.", "concept"),
   ("Resources, capabilities, intentions", "The three things intelligence aims to learn about competitors, allies and yourself.", "concept"),
   ("Jan Herring", "Former CIA analyst who identified five uses of intelligence analysis.", "person")],
  [("mc", "What's the correct order of the intelligence cycle?",
    ["Collection, planning, action, analysis, dissemination",
     "Planning/requirements, collection, analysis, dissemination, action",
     "Analysis, collection, planning, action, dissemination",
     "Planning, analysis, collection, action, dissemination"], 1,
    "Five steps ending in action."),
   ("tf", "Intelligence and information are the same thing.", False,
    "Intelligence is analyzed information."),
   ("mc", "'Nice-to-know syndrome' is a failure at which stage?",
    ["Planning", "Collection", "Dissemination", "Action"], 2,
    "Facts are presented with minimal analysis and relevance."),
   ("mc", "McClellan at Antietam shows that:",
    ["Intelligence is useless", "Great intelligence needs bold, fast action", "Lee had no plan", "Spies always fail"], 1,
    "He moved too slowly and squandered a pivotal advantage."),
   ("mc", "The paradox of leadership is that:",
    ["Weak leaders listen too much", "The traits of strong leaders make them reject informed advice", "Analysts never lead", "Leaders lack confidence"], 1,
    "Confidence and conviction cut both ways."),
   ("tf", "Setting priority intelligence requirements helps prevent research from becoming procrastination.", True,
    "It gives direction so you don't collect aimlessly."),
  ],
  ("The competitor's hiring spree",
   """You lead product at a project-management software company. Over two months you notice: your main competitor posted 12 job ads for 'healthcare compliance' engineers, its CEO spoke at a hospital-IT conference, and two of your sales reps lost deals to it at clinics. Your CEO says they're a general tool like us and that healthcare is a distraction for them.""",
   [("Run this through the intelligence cycle. What are your priority requirements, and what do the clues suggest?",
     """Requirements: Is the competitor entering healthcare as a focus? When? With what product? Collection: job ads, conference talk, lost-deal notes, plus ex-employees, press releases, partner announcements. Analysis: resources (hiring budget), capabilities (compliance engineering), and intentions (CEO's healthcare positioning) all point the same way: a focused move into healthcare, possibly flanking you. Dissemination: a one-page brief with the implication, not a pile of facts. Action: decide whether to defend, partner or concede that segment."""),
    ("How do you avoid the Cassandra curse with your CEO?",
     """Bring analysis tied to a decision and money (lost clinic deals, pipeline at risk), not 'nice-to-know' facts. Present it as testable: name the indicators that would confirm or refute it within 60 days. Propose a small, low-cost action so the CEO can act without fully abandoning their view.""")]),
  ["What's an example from your life where analysis, not just information, explained a situation?",
   "Using resources/capabilities/intentions, assess your toughest competitor. Do stated aims match their resources?",
   "Build your own intelligence cycle with three priority requirements and run it monthly."]),

L(16, "Move and Countermove—The Theory of Games",
  "Your best move depends on their move. Game theory structures that, as long as you remember people aren't always 'rational.'",
  [
   ("Let's meet in New York", """
<p>Thomas Schelling's game: two strangers win $1,000 each if they meet in New York City, with no communication and 30 seconds to answer. Most pick Times Square, Grand Central or the Empire State Building, at noon. With more time and information, answers scatter: <b>more information can reduce clarity</b>. With little information, we fall back on shared logic (focal points).</p>
"""),
   ("What a game is", """
<p>A game is a situation where several goal-oriented decision makers interact, and each one's outcome depends on the others' actions. Driving in traffic, asking for a raise and campaigning are games. Game theory began with <b>John von Neumann</b> analyzing bluffing in poker (1920s); with Morgenstern he later claimed it could ground economics. It builds mathematical models assuming <b>rational actors</b> who maximize utility (highest payoff or least damage): cost-benefit analysis applied to the mind.</p>
"""),
   ("The Prisoner's Dilemma and the Cold War", """
<p>Two prisoners, questioned separately, choose to stay silent (cooperate) or implicate the other (defect). Both silent: light sentences. Both defect: longer sentences. One defects: the defector goes free and the cooperator gets the worst outcome. <b>Defection is the dominant strategy</b> because cooperation is too risky. Game theorists saw the nuclear arms race as this game: the advantage went to a successful first strike, making a tiny misstep catastrophic.</p>
"""),
   ("Rational irrationality and mirror-imaging", """
<p>Opponents may seem irrational because they play for different stakes, or they may <b>feign irrationality</b> because it is rational to do so. In the <b>$20 bill auction</b>, the top two bidders both pay, so they keep bidding past $20 just to cut losses.</p>
<p>We also misjudge payoffs: colleagues may want money, recognition or authority. <b>Mirror-imaging</b> means assuming opponents share your values. McNamara played a rational limited war of carrots and sticks in Vietnam; the Vietnamese played a total war of national liberation.</p>
"""),
   ("Commons and free riders", """
<p><b>Tragedy of the Commons</b> (Garrett Hardin): each herder gets all the benefit of an extra cow while the damage is shared, so rational individuals overgraze the common pasture. National parks are a modern commons. Game theory calls the pattern <b>CC-PP</b>: commonize costs, privatize profits (e.g. a firm dumping waste in a river).</p>
<p><b>Free rider problem</b>: the keg runs dry, the hat goes around, and the rational student knows the new keg arrives whether or not they chip in. It's a collective action problem; one fix is designing incentives that align individual and group goals.</p>
"""),
   ("Lessons and limits", """
<p>Game theory makes you think about payoffs and stakes, and whether everyone sees them the same way. Its artificial assumption of rationality is a weakness in daily life. It also shows cooperative alternatives to pure conflict that can maximize outcomes for all sides.</p>
"""),
  ],
  ["A game: interdependent goal-directed decisions; your payoff depends on others' moves.",
   "Prisoner's Dilemma: defection dominates in a one-shot game.",
   "Apparent irrationality may be rational for different stakes or feigned on purpose.",
   "Avoid mirror-imaging: others may play a different game (Vietnam).",
   "Commons, CC-PP and free riders: individual rationality can wreck group outcomes."],
  [("Game (game theory)", "A situation where several goal-oriented decision makers interact and outcomes depend on each other's choices.", "concept"),
   ("Rational actor", "Game theory's assumption that each player acts to maximize their own payoff (utility).", "concept"),
   ("Prisoner's Dilemma", "Two-player game where defecting is individually dominant though mutual cooperation pays better.", "concept"),
   ("Dominant strategy", "A choice that gives a better payoff no matter what the other player does.", "concept"),
   ("Rational irrationality", "Behavior that looks irrational but is rational given the player's stakes, or is feigned for effect.", "concept"),
   ("Mirror-imaging", "Assuming an opponent shares your values and incentives.", "concept"),
   ("Tragedy of the Commons", "Individuals rationally overuse a shared resource because benefits are private and costs shared.", "concept"),
   ("Free rider problem", "People benefit from a shared good without contributing to it; a collective action problem.", "concept"),
   ("Thomas Schelling", "Game theorist and strategist of the nuclear era; the 'meet in New York' focal-point game.", "person"),
   ("John von Neumann", "Mathematician who founded game theory by analyzing bluffing in poker.", "person")],
  [("mc", "In a one-shot Prisoner's Dilemma, the dominant strategy is:",
    ["Cooperate", "Defect", "Alternate", "Stay silent then confess"], 1,
    "Defecting pays more whatever the other does."),
   ("tf", "In Schelling's game, giving people more time and information made their answers converge more.", False,
    "Answers scattered; more information reduced clarity."),
   ("mc", "Assuming your opponent shares your values is called:",
    ["Free riding", "Mirror-imaging", "Groupthink", "Rational irrationality"], 1,
    "McNamara in Vietnam is the course example."),
   ("mc", "CC-PP stands for:",
    ["Cooperate-cooperate, punish-punish", "Commonize costs, privatize profits", "Collective choice, private payoff", "Central command, peripheral power"], 1,
    "Hardin's description of the commons dynamic in private enterprise."),
   ("mc", "Why do bidders in the $20 auction go above $20?",
    ["They value the bill more", "They are minimizing losses since second place also pays", "They misread the rules", "They want to help the auctioneer"], 1,
    "The payoff shifts from winning $20 to limiting losses."),
   ("tf", "Game theory began with von Neumann's analysis of bluffing in poker.", True,
    "In the 1920s."),
  ],
  ("The shared office kitchen",
   """Eight small startups share a coworking floor with a kitchen. Coffee and snacks are paid from a voluntary jar. The jar is always short, the kitchen is a mess, and the coworking manager threatens to remove the coffee machine. Each founder says they'd chip in more 'if others did.'""",
   [("Which game-theory problems does this illustrate, and why do rational people behave this way?",
     """A free rider problem (coffee appears whether or not you pay) and a Tragedy of the Commons (each person enjoys the benefit of using the kitchen while the mess is shared). Each founder rationally reasons their contribution makes little difference; individually rational choices produce a bad group outcome, likely losing the coffee entirely."""),
    ("Redesign the incentives so cooperation becomes the rational choice.",
     """Turn it into a club good: a small monthly fee per startup added to rent (no free riding), or a coffee machine that needs a team card. Make use visible (a cleaning rota per team, posted publicly) so reputations matter in a repeated game. Tie a clear consequence (losing kitchen access) to defection.""")]),
  ["Which ongoing game-like interactions do you have at work? What's really going on in them?",
   "Can you put numbers on the payoffs in those games? Are you usually winning or losing?",
   "How could you change the payoffs or the structure of a game to improve your position?"]),

L(17, "The Evolution of Cooperation",
  "In repeated games, cooperation can emerge between rivals, and even enemies. Tit for tat shows how.",
  [
   ("Christmas 1914", """
<p>On the first Christmas of WWI, Germans placed lit Christmas trees on their trench parapets; greetings crossed no man's land; at dawn soldiers came out to bury the dead and then mingled freely. Despite both high commands, the truce lasted the day and in places several days. Research shows why: <b>small units facing each other for long periods</b>, which made communication and reciprocity possible.</p>
"""),
   ("Axelrod's cooperation theory", """
<p>Robert Axelrod's <b>The Evolution of Cooperation</b> (1984) asked what conditions let cooperation emerge among self-interested players. He studied trench warfare and the U.S. Senate, where rivals like Orrin Hatch and Ted Kennedy found ways to reciprocate and compromise.</p>
<p>Back to the Prisoner's Dilemma with payoffs: both defect $1 each, both cooperate $3 each, defector $5 and cooperator $0. Defection dominates <b>in a single game</b>. But when the same players meet repeatedly, a simple strategy wins: <b>tit for tat</b>. Cooperate first, then copy the other player's previous move.</p>
"""),
   ("Five conditions for tit for tat", """
<ol>
<li><b>Avoid unnecessary conflict</b>: cooperate as long as the other side does.</li>
<li><b>Respond quickly</b> to an uncalled-for defection.</li>
<li><b>Forgive</b> after responding.</li>
<li>Be <b>clear</b> so the other player can recognize your pattern.</li>
<li>Expect an <b>indefinite number of interactions</b>: the "shadow of the future."</li>
</ol>
<p>Reciprocity wins by eliciting cooperation, not by beating the other player. It's especially useful abroad where detailed contracts are uncommon.</p>
"""),
   ("Cooperation between enemies", """
<ul>
<li>The <b>Washington-Moscow hotline</b> (1963), after the Cuban missile crisis.</li>
<li>Late Cold War <b>confidence- and security-building measures</b>, including mutual inspection of exercises, because exercises can be misread as attacks or can mask real ones (the 1968 invasion of Czechoslovakia).</li>
<li>The Korean DMZ (150+ miles long, 2.5 wide): a cease-fire, not a peace, yet routinized cooperation at P'anmunjŏm.</li>
<li>KGB general Alexei Kondaurov signaled to dissidents which line would provoke police, and they respected it: live and let live.</li>
</ul>
"""),
   ("Spontaneous order and business alliances", """
<p>Against the drift to disorder, <b>spontaneous order</b> says structure can emerge from self-interested people who aren't trying to build it: a dirt path across a meadow, or the price-regulated market economy.</p>
<p>Firms often avoid unilateral moves to escape painful responses; price wars show what happens when tacit cooperation breaks. A <b>strategic alliance</b> aligns firms' actions for <b>synergy</b> (whole greater than the sum of parts). When regulators blocked AT&T's 2011 purchase of T-Mobile, the two arranged spectrum access and coverage expansion instead.</p>
"""),
  ],
  ["Repeated interaction (the shadow of the future) makes cooperation rational.",
   "Tit for tat: cooperate first, then mirror the last move.",
   "Conditions: be nice, retaliate fast, forgive, be clear, expect more rounds.",
   "Even enemies cooperate when miscommunication costs more than cooperation (hotline, CSBMs).",
   "Spontaneous order and alliances: structure and synergy can emerge without central design."],
  [("Tit for tat", "Strategy for repeated games: cooperate first, then copy the other player's previous move.", "concept"),
   ("Shadow of the future", "The expectation of future interactions that makes cooperation worthwhile now.", "concept"),
   ("Spontaneous order", "Social order emerging from self-interested individuals who aren't trying to create it (a meadow path, markets).", "concept"),
   ("Strategic alliance", "Firms aligning their strategic actions because cooperation beats unfettered competition.", "concept"),
   ("Synergy", "When a combined result is greater than the sum of its parts.", "concept"),
   ("Robert Axelrod", "Political scientist; The Evolution of Cooperation (1984); showed tit for tat's success in repeated games.", "person")],
  [("mc", "Tit for tat begins by:",
    ["Defecting", "Cooperating", "Randomizing", "Waiting"], 1,
    "Cooperate on the first move, then copy the other player's last move."),
   ("mc", "Using the lecture's payoffs, what do both players get if both cooperate?",
    ["$0 each", "$1 each", "$3 each", "$5 each"], 2,
    "$3 each; $1 each if both defect; $5 vs $0 if they split."),
   ("tf", "Tit for tat works best when players expect only one interaction.", False,
    "It needs an indefinite number of interactions."),
   ("mc", "Why did the 1914 truce emerge, per research?",
    ["Orders from high command", "Small units faced each other for long periods", "Both sides ran out of ammunition", "Neutral mediators"], 1,
    "Long-term proximity enabled communication and reciprocity."),
   ("mc", "Mutual inspections of military exercises were introduced because:",
    ["Exercises could be mistaken for, or used to mask, an invasion", "They were cheaper", "The UN required it", "Soldiers requested it"], 0,
    "The Soviets used an exercise as cover to invade Czechoslovakia in 1968."),
   ("tf", "A dirt path across a meadow is the lecture's example of spontaneous order.", True,
    "No one designed it; many people's choices created it."),
  ],
  ("Two rival bakeries on one street",
   """Two bakeries face each other on a busy street. Last month Bakery A cut croissant prices by 30%; Bakery B matched and went lower. Now both are losing money on croissants. Both owners plan to stay on this street for years. They also both complain about high flour prices from the same supplier.""",
   [("Explain the situation in Prisoner's Dilemma terms, and why it can be escaped.",
     """Each owner's dominant short-term move was to defect (undercut), producing mutual defection: both lose money. But it's a repeated game with a long shadow of the future (years on the same street), which makes tit for tat and reciprocal cooperation rational."""),
    ("Design a tit-for-tat approach and one cooperative move that creates synergy (without illegal price-fixing).",
     """Bakery A signals cooperation by quietly returning to a normal price and differentiating (sourdough focus) instead of undercutting; if B keeps undercutting, A responds quickly, then forgives once B stops; A keeps its behavior clear and predictable. Synergy: jointly buy flour from a cheaper supplier or as a buying group to cut costs for both, and co-promote the street (a weekend market), growing the pie instead of slicing it. Explicit price-fixing stays off the table.""")]),
  ["Think of your most intractable opponent. Design a tit-for-tat exercise and try it.",
   "How can you lengthen the 'shadow of the future' with someone so their defection becomes less likely?",
   "What made it possible for enemy soldiers to mingle freely in 1914 without orders?"]),

L(18, "When Strategy Breaks Down",
  "Smart organizations do dumb things: strategic masquerade, misalignment, groupthink, politics, overconfidence, loss of focus.",
  [
   ("Kodak", """
<p>Kodak dominated film via focused R&D and even <b>patented the first digital camera in 1975</b>, then chose not to develop it. It bought digital firms without changing its strategic focus; disposable cameras in the late 1980s reinforced the belief that film was the bedrock. It had nondigital core competencies and a slow-moving industry history. A possible path: lead the output side of digital, finished prints. Facing an inflection point, it stayed the course.</p>
"""),
   ("Strategic masquerade", """
<p>Good strategy closes options; Kodak was never going to dominate all of digital. A <b>strategic masquerade</b> substitutes slogans or operational techniques (TQM, benchmarking, best practices, Six Sigma) for real strategic choices. Strip those away and strategy is the ability to make <b>tradeoffs</b>: do some things and not others. Efficiency programs push the industry's efficiency frontier forward but don't create advantage. Personally, procrastination and routine busywork are masquerades: we feel strategic while absorbed in minor tasks, often from a desire to keep all options open.</p>
"""),
   ("Strategic misalignment", """
<ul>
<li><b>Internal</b>: resources, capabilities and intentions don't mesh, or structure, operations and strategy don't. Personally: goals without the resources or capabilities, and without honesty about that gap.</li>
<li><b>External</b>: the environment shifts slowly with no explosion. Generals "fight the last war": rifles and minié balls made frontal assault suicidal in the Civil War, and Europe repeated it in WWI.</li>
<li><b>Strategy creep</b> (dilution, erosion): chasing every change without focus; people and resources get add-on tasks until stretched to breaking.</li>
</ul>
"""),
   ("Conspirators against strategy", """
<ul>
<li><b>Groupthink</b>: excessive agreement; group values assumed right; no room to dissent.</li>
<li><b>Bureaucratic politics</b>: insufficient agreement; leaders bargain for power and the output is a suboptimal compromise. DEC (1992): the CEO demanded consensus on focus, none came, and a non-strategy was announced.</li>
<li><b>Overconfidence</b>: overestimating our judgment; assuming we understand new information without analysis.</li>
<li><b>Loss of focus</b>: cause and symptom of erosion, often born from success, "building on our success," or hiring someone to "shake things up." Brand equity can't be extended, only diluted (Coca-Cola means soft drink).</li>
</ul>
"""),
   ("Walmart, 2005", """
<p>A new marketing head arrived in April 2005 to "shake things up." By August, Walmart was buying Vogue ads at nearly $1 million per issue, then supercenters, remodeling, decluttering, organics, an upmarket push, and higher prices. The cause: overconfidence and mission creep, losing focus on "saving people money so they can live better." The cure for all these pathologies: steer a bold course and keep your eyes on the strategic goal.</p>
"""),
  ],
  ["Kodak invented digital and still lost: staying the course at an inflection point.",
   "Strategic masquerade: efficiency tools and slogans pretending to be strategy; real strategy = tradeoffs.",
   "Misalignment: internal, external (fighting the last war), and strategy creep.",
   "Conspirators: groupthink, bureaucratic politics, overconfidence, loss of focus.",
   "Brand equity can't be extended, only diluted (Walmart in Vogue)."],
  [("Strategic masquerade", "Substituting slogans or operational techniques (TQM, benchmarking) for real strategic choices.", "concept"),
   ("Tradeoff", "Deciding to do some things and not others; the heart of strategic management.", "concept"),
   ("Strategy creep", "Gradual dilution of strategy as people and resources take on unfocused add-on tasks.", "concept"),
   ("Groupthink", "Excessive agreement in a group that suppresses dissent and lets bad ideas thrive.", "concept"),
   ("Bureaucratic politics", "Decisions as the outcome of bargaining among leaders rather than rational analysis.", "concept"),
   ("Fighting the last war", "Planning based on past conflicts while ignoring changes such as new technology.", "concept")],
  [("mc", "Which is a 'strategic masquerade' according to the lecture?",
    ["Choosing a niche", "Benchmarking presented as strategy", "Making tradeoffs", "Closing options"], 1,
    "Operational techniques move the efficiency frontier but aren't strategy."),
   ("tf", "Kodak patented the first digital camera in 1975.", True,
    "It chose not to develop the technology."),
   ("mc", "DEC's 1992 'non-strategy' resulted mainly from:",
    ["Groupthink", "Bureaucratic politics", "Inertia", "A price war"], 1,
    "The CEO demanded consensus; bargaining failed; a vague non-strategy came out."),
   ("mc", "'Brand equity cannot be extended; it can only be...'",
    ["Sold", "Diluted", "Doubled", "Protected"], 1,
    "Coca-Cola's brand means soft drink and nothing else."),
   ("mc", "Generals 'fighting the last war' is an example of:",
    ["Internal misalignment", "External misalignment", "Tit for tat", "Focus strategy"], 1,
    "The environment (technology) changed but strategy didn't."),
   ("tf", "Hiring someone to 'shake things up' is, per the lecture, a warning sign of strategic erosion.", True,
    "It sounds reasonable but often triggers loss of focus (Walmart 2005)."),
  ],
  ("The student who is 'very busy'",
   """Lena wants to get into a top master's program in two years. Her week: color-coding her notes, reorganizing her study app, joining a fourth student club 'for networking,' taking every extra shift her part-time job offers, and reading productivity blogs. Her grades are flat, and she hasn't researched the programs' admission criteria.""",
   [("Diagnose Lena's situation with concepts from this lecture.",
     """Strategic masquerade: she substitutes technique (notes, apps, productivity reading) for strategy and feels busy instead of progressing. Strategy creep: club number four and every extra shift are add-ons that dilute focus. Internal misalignment: her intention (top program) isn't matched by resources or capabilities (grades, a test score, research). Poor intelligence: she doesn't know the admission criteria. She's keeping all options open instead of making tradeoffs."""),
    ("What tradeoffs should she make?",
     """First run the intelligence: list the 3 to 5 target programs and their real criteria. Then cut: quit two clubs, cap work shifts, stop tool-tinkering. Mass her time on what moves admission (GPA in key courses, test prep, one relevant project or internship, two strong recommenders). Saying no is the strategy.""")]),
  ["Do you absorb yourself in detailed execution instead of real strategic thinking? Where?",
   "Which management tools in your workplace or school have substituted for an actual strategy?",
   "What difficult tradeoffs have you made in your personal strategy? If none, reexamine your plan."]),
]
