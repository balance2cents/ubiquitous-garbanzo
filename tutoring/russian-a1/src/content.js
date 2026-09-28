// Lesson content for Jasno! neu A1–A2, Lektion 1–9 (the A1 half of the book).
// quiz  = the workbook's "Что правильно?" self-test for the lesson (answer keys written by us)
// drill = typed answers in Cyrillic; answers are compared without stress marks, ё≈е, case, punctuation
// Russian inside <i class="ru"> is clickable to hear it.

const EXAM_DATE = '2026-12-16';

const LESSONS = [
{
  n:1, ru:'Здравствуйте!', en:'Hello!', kb:'KB p. 12–25 · ÜB p. 6–15',
  can:['Greet people and say goodbye','Ask "who is this / what is this?"','Read the first 25 letters and recognize international words'],
  grammar:`
<h3>1 · No "to be" in the present</h3>
<p>Russian simply drops <em>am / is / are</em> in the present tense. The book calls this <span class="de">das Hilfsverb „sein“</span>.</p>
<table class="gt"><tr><td><i class="ru">Это Москва.</i></td><td>This <b>is</b> Moscow.</td></tr>
<tr><td><i class="ru">Я Анна.</i></td><td>I <b>am</b> Anna.</td></tr>
<tr><td><i class="ru">Кто это?</i></td><td>Who <b>is</b> this?</td></tr>
<tr><td><i class="ru">Что это?</i></td><td>What <b>is</b> this?</td></tr></table>
<p><b>кто</b> asks about people (and animals), <b>что</b> about things.</p>

<h3>2 · Questions are just intonation</h3>
<p>A yes/no question has the same word order as a statement. Only the voice rises on the word you're asking about. In writing, only the <b>?</b> changes.</p>
<table class="gt"><tr><td><i class="ru">Это Анна.</i></td><td>That's Anna.</td></tr><tr><td><i class="ru">Это Анна?</i></td><td>Is that Anna?</td></tr></table>

<h3>3 · Saying "no" and "not"</h3>
<p><b>нет</b> = no (the answer). <b>не</b> = not (goes right before the word it negates).</p>
<table class="gt"><tr><td><i class="ru">Это Анна? — Нет, это не Анна. Это Ольга.</i></td><td>Is that Anna? No, that's not Anna. That's Olga.</td></tr></table>

<h3>4 · ты vs. вы</h3>
<p><b>ты</b> = one person you know well (friend, kid, family). <b>вы</b> = polite "you" <em>or</em> any group. Your teacher is always <b>вы</b>. Greetings follow the same split: <i class="ru">Здравствуй!</i> (ты) vs. <i class="ru">Здравствуйте!</i> (вы). <i class="ru">Привет!</i> and <i class="ru">Пока!</i> are casual only.</p>

<h3>5 · Stress changes the sound</h3>
<p>Each word has one stressed vowel (the book marks it with an accent: <i class="ru">молоко́</i>). An <b>unstressed о sounds like "a"</b>: <i class="ru">молоко́</i> ≈ "ma-la-KO". This is why every word in this platform shows its stress mark. Learn it with the word. <span class="de">Betonung = stress</span></p>`,
  quiz:[
    ['Кто это? asks about…', ['a person','a thing'], 0, 'кто = who (people). что = what (things).'],
    ['You greet your teacher in the morning:', ['Привет!','Здравствуйте!'], 1, 'Teacher = вы → Здравствуйте!'],
    ['— Это Анна? — Нет, это … Анна.', ['не','нет'], 0, 'не = not (inside the sentence). нет = the answer "no".'],
    ['Which letter sounds like English "r"?', ['Р','Н','В'], 0, 'Р = r. Н = n, В = v. These three look like Latin letters but sound different.'],
    ['Which letter sounds like English "n"?', ['Н','Р','П'], 0, 'Н = n. П = p.'],
    ['<i class="ru">ресторан</i> means…', ['restaurant','subway','theater'], 0, 'Read it letter by letter: r-e-s-t-o-r-a-n.'],
    ['In <i class="ru">молоко́</i> the first two <i class="ru">о</i> sound like…', ['o','a'], 1, 'Unstressed о is reduced to an "a" sound.'],
    ['You say bye to a friend:', ['До свидания!','Пока!'], 1, 'Пока is casual. До свидания is the neutral/formal goodbye.'],
    ['<i class="ru">Это Москва?</i> is…', ['a statement','a question'], 1, 'The question mark (and rising intonation) is the only difference.'],
    ['<i class="ru">вы</i> can mean…', ['only polite "you"','polite "you" or several people'], 1, 'вы = formal singular and any plural.'],
  ],
  drill:[
    ['yes', 'да'], ['no', 'нет'], ['who', 'кто'], ['what', 'что'],
    ['Hi! (casual)', 'Привет'], ['This is Moscow.', 'Это Москва'],
    ['you (polite)', 'вы'], ['Goodbye! (neutral)', 'До свидания'],
  ],
},
{
  n:2, ru:'Мы из Владимира!', en:'We are from Vladimir!', kb:'KB p. 26–37 · ÜB p. 16–25',
  can:['Ask for and give a name','Introduce someone and react','Ask how someone is and where they are from','Use the whole alphabet'],
  grammar:`
<h3>1 · Pronouns: nominative and accusative</h3>
<p>Russian says "they call me …" instead of "my name is …". The person being called goes in the <b>accusative</b> (<span class="de">Akkusativ</span>).</p>
<table class="gt"><tr><th>Nominative</th><th>Accusative</th><th></th></tr>
<tr><td><i class="ru">я</i></td><td><i class="ru">меня</i></td><td><i class="ru">Меня зовут Лиза.</i></td></tr>
<tr><td><i class="ru">ты</i></td><td><i class="ru">тебя</i></td><td><i class="ru">Как тебя зовут?</i></td></tr>
<tr><td><i class="ru">он / оно</i></td><td><i class="ru">его</i> (say "yevo")</td><td><i class="ru">Его зовут Макс.</i></td></tr>
<tr><td><i class="ru">она</i></td><td><i class="ru">её</i></td><td><i class="ru">Её зовут Анна.</i></td></tr>
<tr><td><i class="ru">мы</i></td><td><i class="ru">нас</i></td><td></td></tr>
<tr><td><i class="ru">вы</i></td><td><i class="ru">вас</i></td><td><i class="ru">Как вас зовут?</i></td></tr>
<tr><td><i class="ru">они</i></td><td><i class="ru">их</i></td><td><i class="ru">Их зовут Том и Тея.</i></td></tr></table>

<h3>2 · Every noun has a gender, and the ending tells you</h3>
<table class="gt"><tr><th>Masculine</th><th>Neuter</th><th>Feminine</th></tr>
<tr><td>consonant / -ь / -й<br><i class="ru">фильм, кремль, музей</i></td><td>-о / -е<br><i class="ru">слово, море</i></td><td>-а / -я<br><i class="ru">фирма, неделя</i></td></tr></table>
<p class="tip">-ь words can be masculine <em>or</em> feminine. Learn those with their gender. The vocab list marks them.</p>

<h3>3 · "From" = из + genitive</h3>
<p>After <b>из</b> the noun goes into the <b>genitive</b> (<span class="de">Genitiv</span>):</p>
<table class="gt"><tr><th>m / n</th><th>add -а / -я</th></tr>
<tr><td><i class="ru">Берлин → из Берлина</i></td><td><i class="ru">Суздаль → из Суздаля</i></td></tr>
<tr><th>f</th><th>-а → -ы, -я → -и</th></tr>
<tr><td><i class="ru">Москва → из Москвы</i></td><td><i class="ru">Калуга → из Калуги</i> (!)</td></tr></table>
<p class="tip"><b>Spelling rule (the "7-letter rule"):</b> after <b>г к х ж ш ч щ</b> you never write <b>ы</b>, you write <b>и</b>. That's why it's <i class="ru">из Калуги</i>, not "Калугы". This rule comes back in every lesson. <span class="de">Zischlaut = ж ш ч щ</span></p>

<h3>4 · Nationality has two forms</h3>
<table class="gt"><tr><td><i class="ru">Он русский. Она русская.</i></td><td>He's Russian. She's Russian.</td></tr>
<tr><td><i class="ru">Он немец. Она немка.</i></td><td>He's German. She's German.</td></tr></table>
<p>Ask: <i class="ru">Кто вы по национальности?</i> Answer with your own gender form.</p>

<h3>5 · Formal names</h3>
<p>Russians address each other formally with first name + patronymic (<i class="ru">отчество</i>): <i class="ru">Анна Сергеевна, Игорь Андреевич</i>. That's the cue for <b>вы</b> and <i class="ru">ваши дела</i>. First name alone means <b>ты</b> and <i class="ru">твои дела</i>.</p>`,
  quiz:[
    ['— Здравствуйте, как … зовут?<br>— Меня зовут Татьяна Борисовна.', ['тебя','вас'], 1, 'Name + patronymic = formal → вас.'],
    ['— Меня зовут Михаил Петрович.<br>— … .', ['Очень приятно','Спасибо'], 0, 'Reply to an introduction: Очень приятно (nice to meet you).'],
    ['Здравствуйте, Надежда Михайловна. Как …?', ['твои дела','ваши дела'], 1, 'Formal address → ваши дела.'],
    ['— Маша, … ты?<br>— Я из Москвы.', ['как','откуда'], 1, 'The answer "from Moscow" means the question was откуда (from where).'],
    ['— Вадим, вы из Мурманска?<br>— Нет, я из … .', ['Владимир','Владимира'], 1, 'из + genitive: masculine adds -а.'],
    ['Меня зовут Таня. Я из … .', ['Калуга','Калуги'], 1, 'из + genitive; after г write и, not ы.'],
    ['— Привет! Как … зовут?<br>— Таня. А тебя?', ['вас','тебя'], 1, 'Привет is casual → тебя.'],
    ['…, пожалуйста! Это Валентина Васильевна, а это Григорий Петрович.', ['Очень приятно','Познакомьтесь'], 1, 'Познакомьтесь = "let me introduce you" / "meet each other".'],
    ['Привет, Миша! Как … дела?', ['ваши','твои'], 1, 'Привет + first name = ты → твои.'],
    ['Познакомьтесь, пожалуйста! Это Пётр Иванович. Он из … .', ['Суздаля','Суздаль'], 0, 'Суздаль is masculine (-ь) → genitive -я.'],
    ['Это Маргарита Голубева. Она менеджер. Она … .', ['русский','русская'], 1, 'Она → feminine form русская.'],
    ['— Мартин, кто вы по национальности?<br>— Я … .', ['немец','немка'], 0, 'Martin is a man → немец.'],
  ],
  drill:[
    ['What\'s your name? (polite) — Как … зовут?', 'вас'],
    ['My name is Lisa. — … зовут Лиза.', 'Меня'],
    ['from Berlin — из (Берлин)', 'Берлина'],
    ['from Moscow — из (Москва)', 'Москвы'],
    ['from Kaluga — из (Калуга)', 'Калуги'],
    ['She is German. — Она (немец → f)', 'немка'],
    ['She is Russian. — Она (русский → f)', 'русская'],
    ['Nice to meet you.', 'Очень приятно'],
    ['Where are you from? (polite)', ['Откуда вы','Вы откуда']],
  ],
  write:{id:'w2', prompt:'Introduce yourself in 4–5 sentences: name, where you are from (country and city), nationality, how you are today.', words:25},
},
{
  n:3, ru:'Где вы живёте?', en:'Where do you live?', kb:'KB p. 38–49 · ÜB p. 26–35',
  can:['Say where you come from and which languages you speak (and how well)','Ask for and give an address and phone number','Count to 20'],
  grammar:`
<h3>1 · Countries in -ия</h3>
<p>Feminine nouns ending in <b>-ия</b> take <b>-ии</b> in both genitive and prepositional:</p>
<table class="gt"><tr><th>Nominative</th><th>из + genitive</th><th>в + prepositional</th></tr>
<tr><td><i class="ru">Германия</i></td><td><i class="ru">из Германии</i></td><td><i class="ru">в Германии</i></td></tr>
<tr><td><i class="ru">Россия</i></td><td><i class="ru">из России</i></td><td><i class="ru">в России</i></td></tr>
<tr><td><i class="ru">Франция</i></td><td><i class="ru">из Франции</i></td><td><i class="ru">во Франции</i></td></tr></table>
<p class="tip">Foreign names ending in a vowel (except unstressed -а) never change: <i class="ru">из Токио, в Баку, в Хельсинки</i>. Same for <i class="ru">кафе, кино, метро, такси</i>: <i class="ru">в кафе, в метро</i>.</p>

<h3>2 · The two verb conjugations</h3>
<p>Verbs come in two families, named after the vowel in their endings (<span class="de">e-Konjugation / и-Konjugation</span>). Learn the <b>я</b>, <b>ты</b> and <b>они</b> forms and you can build the rest.</p>
<table class="gt"><tr><th></th><th>жить (е-conj.)</th><th>говорить (и-conj.)</th></tr>
<tr><td>я</td><td><i class="ru">живу</i></td><td><i class="ru">говорю</i></td></tr>
<tr><td>ты</td><td><i class="ru">живёшь</i></td><td><i class="ru">говоришь</i></td></tr>
<tr><td>он / она</td><td><i class="ru">живёт</i></td><td><i class="ru">говорит</i></td></tr>
<tr><td>мы</td><td><i class="ru">живём</i></td><td><i class="ru">говорим</i></td></tr>
<tr><td>вы</td><td><i class="ru">живёте</i></td><td><i class="ru">говорите</i></td></tr>
<tr><td>они</td><td><i class="ru">живут</i></td><td><i class="ru">говорят</i></td></tr></table>
<p class="tip">The <b>ты</b> form always ends in <b>-шь</b>, with a soft sign. Leaving off the ь is the most common exam mistake here.</p>

<h3>3 · Where? = в / на + prepositional</h3>
<p>The prepositional case (<span class="de">Präpositiv</span>) only appears after prepositions. For <b>где?</b> (where?) use <b>в</b> (in) or <b>на</b> (on/at). Most nouns just take <b>-е</b>:</p>
<table class="gt"><tr><td><i class="ru">город → в городе</i></td><td><i class="ru">центр → в центре</i></td></tr>
<tr><td><i class="ru">Москва → в Москве</i></td><td><i class="ru">улица → на улице</i></td></tr>
<tr><td><i class="ru">море → на море</i></td><td><i class="ru">Россия → в России</i> (-ия → -ии)</td></tr></table>
<p><b>на</b> goes with streets, open spaces and some fixed words: <i class="ru">на улице, на море, на севере</i>. Learn those as a set.</p>

<h3>4 · Languages: по-русски</h3>
<p>With <i class="ru">говорить</i> use the adverb form: <i class="ru">Я говорю по-немецки, по-английски и немного по-русски.</i> How well: <i class="ru">свободно</i> (fluently), <i class="ru">хорошо</i>, <i class="ru">немного</i>, <i class="ru">плохо</i>, <i class="ru">к сожалению, не говорю</i>.</p>

<h3>5 · Numbers 1–20 and phone numbers</h3>
<p>11–19 all end in <b>-надцать</b> (from "на десять", on top of ten): <i class="ru">одиннадцать, двенадцать … девятнадцать</i>. Russians read phone numbers in pairs: 8 (916) 45-78-99.</p>`,
  quiz:[
    ['— Привет! Меня зовут Томас. Я из … .', ['Германия','Германии'], 1, 'из + genitive, -ия → -ии.'],
    ['— Анна, ты из Канады?<br>— Нет, я из … .', ['Франции','Франция'], 0, 'из + genitive → Франции.'],
    ['Это моя коллега Мария. Она из … .', ['России','Россия'], 0, 'из + genitive → России.'],
    ['Мы из Канады. Мы … по-английски и по-французски.', ['говорят','говорим'], 1, 'мы → -им in the и-conjugation.'],
    ['— Вы … по-русски?<br>— Да, немного.', ['говорю','говорите'], 1, 'вы → говорите.'],
    ['— Кристиан, ты … по-французски?', ['говорите','говоришь'], 1, 'ты → -ишь.'],
    ['Это студенты из Германии. Они хорошо … по-русски.', ['говорим','говорят'], 1, 'они → говорят.'],
    ['— Пётр, где вы живёте?<br>— В … .', ['Москва','Москве'], 1, 'где? → в + prepositional (-е).'],
    ['— Мария, где ты сейчас?<br>— Я в … .', ['Париже','Парижа'], 0, 'где? → prepositional -е. (Парижа is genitive.)'],
    ['Мы живём в … .', ['центр','центре'], 1, 'в + prepositional → центре.'],
    ['Это моя сестра Надя. Она … в Германии.', ['живут','живёт'], 1, 'она → живёт.'],
    ['— Вы … в России?<br>— Да, мы из Санкт-Петербурга.', ['живут','живёте'], 1, 'вы → живёте.'],
    ['Коля, ты живёшь … улице Вернадского?', ['на','в'], 0, 'Streets take на: на улице.'],
    ['— Какой у тебя адрес?<br>— Улица Центральная, дом 5, … 2.', ['квартира','квартире'], 0, 'An address is a list in the nominative: улица …, дом 5, квартира 2.'],
  ],
  drill:[
    ['я (жить) в Москве', 'живу'], ['они (жить)', 'живут'], ['ты (говорить)', 'говоришь'], ['мы (говорить)', 'говорим'],
    ['в (Москва)', 'Москве'], ['в (Россия)', 'России'], ['на (улица)', 'улице'], ['из (Франция)', 'Франции'],
    ['14 in words', 'четырнадцать'], ['I speak a little Russian.', ['Я немного говорю по-русски','Я говорю немного по-русски']],
  ],
  write:{id:'w3', prompt:'Write about where you live: country, city, street. Which languages do you speak and how well? Where does your best friend live?', words:30},
},
{
  n:4, ru:'Моя семья', en:'My family', kb:'KB p. 50–59 · ÜB p. 36–43',
  can:['Introduce family and friends','Say what you have and don\'t have','Say what someone does for work and where'],
  grammar:`
<h3>1 · Possessives: my, your, our</h3>
<p>These agree with the <b>thing owned</b>, not the owner:</p>
<table class="gt"><tr><th></th><th>m</th><th>f</th><th>n</th><th>pl</th></tr>
<tr><td>my</td><td><i class="ru">мой</i></td><td><i class="ru">моя</i></td><td><i class="ru">моё</i></td><td><i class="ru">мои</i></td></tr>
<tr><td>your (ты)</td><td><i class="ru">твой</i></td><td><i class="ru">твоя</i></td><td><i class="ru">твоё</i></td><td><i class="ru">твои</i></td></tr>
<tr><td>our</td><td><i class="ru">наш</i></td><td><i class="ru">наша</i></td><td><i class="ru">наше</i></td><td><i class="ru">наши</i></td></tr>
<tr><td>your (вы)</td><td><i class="ru">ваш</i></td><td><i class="ru">ваша</i></td><td><i class="ru">ваше</i></td><td><i class="ru">ваши</i></td></tr></table>
<p class="tip"><b>his / her / their never change:</b> <i class="ru">его</i> (his), <i class="ru">её</i> (her), <i class="ru">их</i> (their). <i class="ru">его брат, его сестра, его дети</i>.</p>

<h3>2 · "I have" = у меня есть</h3>
<p>Russian has no everyday "to have". It says "at me there is". The owner goes in the <b>genitive</b> after <b>у</b>, and the thing owned stays in the <b>nominative</b>:</p>
<table class="gt"><tr><td><i class="ru">У меня есть брат.</i></td><td>I have a brother.</td></tr>
<tr><td><i class="ru">У Ирины есть сестра.</i></td><td>Irina has a sister.</td></tr></table>
<p>After a preposition, <i class="ru">его / её / их</i> get an <b>н-</b>: <i class="ru">у него, у неё, у них</i>.</p>
<table class="gt"><tr><th>я</th><th>ты</th><th>он</th><th>она</th><th>мы</th><th>вы</th><th>они</th></tr>
<tr><td><i class="ru">у меня</i></td><td><i class="ru">у тебя</i></td><td><i class="ru">у него</i></td><td><i class="ru">у неё</i></td><td><i class="ru">у нас</i></td><td><i class="ru">у вас</i></td><td><i class="ru">у них</i></td></tr></table>

<h3>3 · "I don't have" = у меня нет + genitive</h3>
<p>With <b>нет</b>, the missing thing <b>also</b> goes into the genitive:</p>
<table class="gt"><tr><td><i class="ru">У меня нет брата.</i></td><td>I don't have a brother.</td></tr>
<tr><td><i class="ru">У неё нет сестры.</i></td><td>She doesn't have a sister.</td></tr></table>
<p class="tip">Check: <b>есть</b> + nominative, <b>нет</b> + genitive. The exam tests this every time.</p>

<h3>4 · Counting people: 1 vs. 2–4</h3>
<table class="gt"><tr><td><b>1</b> + nominative</td><td><i class="ru">один брат, одна сестра</i></td></tr>
<tr><td><b>2, 3, 4</b> + genitive singular</td><td><i class="ru">два брата, две сестры, три сына, четыре студента</i></td></tr></table>
<p><i class="ru">два</i> for m/n, <i class="ru">две</i> for f. For children specifically: <i class="ru">двое детей, трое детей</i>. (<span class="de">Rektion der Grundzahlen</span> = which case a number requires.)</p>

<h3>5 · Where do you work? в / на + prepositional</h3>
<p><i class="ru">в офисе, в школе, в больнице, в банке, в редакции</i> · but <i class="ru">на заводе, на фирме</i> (also <i class="ru">в фирме</i>). Profession: <i class="ru">Кто он по профессии? — Он инженер.</i></p>`,
  quiz:[
    ['— Это моя мама.<br>— Как … зовут?<br>— Надежда.', ['его','её'], 1, 'мама is "she" → её.'],
    ['— Это твой папа?<br>— Да. … зовут Геннадий Петрович.', ['Их','Его'], 1, 'папа is "he" → Его.'],
    ['— Это мои братья.<br>— Как … зовут?', ['его','их'], 1, 'братья = plural → их.'],
    ['Это … дочь. Её зовут Аня.', ['мой','моя'], 1, 'дочь is feminine (despite -ь) → моя.'],
    ['Это я и мой муж Николай. А это … внуки.', ['ваши','наши'], 1, '"me and my husband" → our → наши.'],
    ['— У … есть брат?<br>— Да, его зовут Валерий.', ['вас','ваш'], 0, 'у + genitive pronoun → у вас.'],
    ['— … муж работает в редакции?', ['Ваши','Ваш'], 1, 'муж is masculine singular → Ваш.'],
    ['— У вас есть дети?<br>— Да, у меня три … .', ['сын','сына'], 1, '2–4 + genitive singular → три сына.'],
    ['У неё три сына и … дочь, моя мама.', ['один','одна'], 1, 'дочь is feminine → одна.'],
    ['Это мой сын Михаил. У … три сына.', ['него','неё'], 0, 'сын = he → у него.'],
    ['Моя сестра Светлана − менеджер. У … интересная работа.', ['нас','неё'], 1, 'сестра = she → у неё.'],
    ['У Татьяны три дочки. Но у неё нет … .', ['сын','сына'], 1, 'нет + genitive → сына.'],
    ['— Где ты работаешь?<br>— Я работаю … заводе.', ['в','на'], 1, 'завод takes на: на заводе.'],
    ['— Кто ваш отец по профессии?<br>— Инженер. Он работает на … .', ['фирма','фирме'], 1, 'на + prepositional → фирме.'],
  ],
  drill:[
    ['(my) мама', 'моя'], ['(our) дети', 'наши'], ['У (он) есть сестра.', 'него'], ['У меня нет (брат).', 'брата'],
    ['У неё нет (сестра).', 'сестры'], ['два (сын)', 'сына'], ['(2) дочки', 'две'], ['Он работает на (завод).', 'заводе'],
    ['teacher (f) — учитель → ?', 'учительница'], ['I have a cat.', 'У меня есть кошка'],
  ],
  write:{id:'w4', prompt:'Describe your family: who is in it, their names, where they live, what they do. Say one thing you don\'t have (a brother, a cat…).', words:40},
},
{
  n:5, ru:'В магазине', en:'At the store', kb:'KB p. 60–69 · ÜB p. 44–51',
  can:['Buy food at the supermarket and the market','Give amounts, weights and packaging','Ask for and understand prices','Write a shopping list'],
  grammar:`
<h3>1 · Plural (nominative)</h3>
<table class="gt"><tr><th>m / f</th><th>hard stem → <b>-ы</b></th><th>soft stem, or after г к х ж ш ч щ → <b>-и</b></th></tr>
<tr><td></td><td><i class="ru">помидор → помидоры</i><br><i class="ru">конфета → конфеты</i></td><td><i class="ru">шницель → шницели, груша → груши, пирог → пироги</i></td></tr>
<tr><th>n</th><th>-о → <b>-а</b></th><th>-е → <b>-я</b></th></tr>
<tr><td></td><td><i class="ru">яйцо → яйца</i></td><td><i class="ru">печенье → печенья</i></td></tr></table>
<p class="tip">Exception: <i class="ru">яблоко → яблоки</i>. Some words lose a vowel (<span class="de">Vokalausfall</span>): <i class="ru">огурец → огурцы, напиток → напитки</i>.</p>
<p>Some words are singular-only (<i class="ru">масло, творог, капуста, лук, картофель, морковь</i>) and some are plural-only (<i class="ru">деньги</i>). The verb follows: <i class="ru">Сколько стоит капуста? Сколько стоят яблоки?</i></p>

<h3>2 · Accusative: what you buy or ask for</h3>
<p>For <b>things</b> (inanimate), the accusative looks like the nominative, <b>except feminine -а / -я → -у / -ю</b>:</p>
<table class="gt"><tr><td><i class="ru">Дайте, пожалуйста, лук, масло, капусту и бананы.</i></td></tr></table>
<table class="gt"><tr><th></th><th>m</th><th>n</th><th>f</th></tr>
<tr><td>Nom.</td><td><i class="ru">один литр</i></td><td><i class="ru">одно яйцо</i></td><td><i class="ru">одна пачка</i></td></tr>
<tr><td>Acc.</td><td><i class="ru">один литр</i></td><td><i class="ru">одно яйцо</i></td><td><i class="ru">одну пачку</i></td></tr></table>

<h3>3 · Numbers 21–200</h3>
<p><i class="ru">двадцать, тридцать, сорок, пятьдесят, шестьдесят, семьдесят, восемьдесят, девяносто, сто, двести</i>. Build compounds like English: <i class="ru">сто двадцать пять</i> = 125.</p>

<h3>4 · Prices: рубль / рубля / рублей</h3>
<p>The <b>last word of the number</b> decides the form:</p>
<table class="gt"><tr><td>ends in 1 (21, 31, 101…)</td><td>+ nominative singular</td><td><i class="ru">один рубль, 31 рубль</i></td></tr>
<tr><td>ends in 2, 3, 4</td><td>+ genitive singular</td><td><i class="ru">два рубля, 152 рубля</i></td></tr>
<tr><td>ends in 5–9, 0, and 11–14</td><td>+ genitive plural</td><td><i class="ru">пять рублей, 12 рублей, 165 рублей</i></td></tr></table>
<p class="tip">11, 12, 13, 14 always take <i class="ru">рублей</i>, even though they "end" in 1–4. <i class="ru">евро</i> never changes.</p>
<p>Price per unit: <i class="ru">Масло стоит 200 рублей пачка. Морковь стоит 52 рубля килограмм.</i></p>

<h3>5 · At the counter</h3>
<table class="gt"><tr><td><i class="ru">Что вы хотите? / Что ещё?</i></td><td>What would you like? / Anything else?</td></tr>
<tr><td><i class="ru">Дайте мне, пожалуйста, хлеб и молоко.</i></td><td>Give me bread and milk, please.</td></tr>
<tr><td><i class="ru">Это всё. Сколько с меня?</i></td><td>That's all. How much do I owe?</td></tr>
<tr><td><i class="ru">С вас 178 рублей. Вот сдача.</i></td><td>That's 178 rubles. Here's your change.</td></tr></table>`,
  quiz:[
    ['Скажите, сколько стоит …?', ['булочка','булочки'], 0, 'стоит (singular) → булочка.'],
    ['Сколько стоят …?', ['яблоко','яблоки'], 1, 'стоят (plural) → яблоки.'],
    ['— Извините, где здесь …?<br>— Они там.', ['огурец','огурцы'], 1, 'Они → plural огурцы (vowel drops out).'],
    ['— У нас есть …?<br>— Да, они в холодильнике.', ['яйцо','яйца'], 1, 'они → plural яйца.'],
    ['Конфеты стоят 152 … коробка.', ['рубль','рубля','рублей'], 1, 'Ends in 2 → рубля.'],
    ['Картофель стоит 31 … килограмм.', ['рубль','рубля','рублей'], 0, 'Ends in 1 → рубль.'],
    ['Чай стоит 165 … пачка.', ['рубль','рубля','рублей'], 2, 'Ends in 5 → рублей.'],
    ['В бутылке … литр.', ['один','одна','одну'], 0, 'литр is masculine → один.'],
    ['… пачка стоит 198 рублей.', ['Один','Одно','Одна'], 2, 'пачка is feminine, subject → Одна.'],
    ['Лук стоит 48 … килограмм.', ['рубль','рубля','рублей'], 2, 'Ends in 8 → рублей.'],
    ['Дайте мне, пожалуйста, … .', ['капуста','капусту'], 1, 'Object of дайте → accusative, -а → -у.'],
    ['Дайте, пожалуйста, … .', ['груша','грушу'], 1, 'Accusative feminine → грушу.'],
    ['Дайте мне, пожалуйста, … пачку.', ['один','одна','одну'], 2, 'Accusative feminine → одну.'],
    ['Мне, пожалуйста, … коробку.', ['один','одна','одну'], 2, 'коробку is accusative feminine → одну.'],
    ['Сколько стоит … бутылка?', ['один','одна','одну'], 1, 'бутылка is the subject → nominative одна.'],
    ['Вот сдача – 151 … .', ['рубль','рубля','рублей'], 0, 'Ends in 1 (not 11) → рубль.'],
    ['С вас 178 … .', ['рубль','рубля','рублей'], 2, 'Ends in 8 → рублей.'],
  ],
  drill:[
    ['plural: помидор', 'помидоры'], ['plural: груша', 'груши'], ['plural: яблоко', 'яблоки'], ['plural: яйцо', 'яйца'],
    ['Дайте, пожалуйста, (колбаса).', 'колбасу'], ['22 (рубль)', 'рубля'], ['45 (рубль)', 'рублей'], ['12 (рубль)', 'рублей'],
    ['Сколько (стоить) яблоки?', 'стоят'], ['90 in words', 'девяносто'], ['Anything else?', 'Что ещё'],
  ],
  write:{id:'w5', prompt:'Write a shopping list with amounts (a kilo of…, a bottle of…, a pack of…) and a short dialog at the market: ask the price, buy two things, pay.', words:40},
},
{
  n:6, ru:'Свободное время', en:'Free time', kb:'KB p. 70–81 · ÜB p. 52–59',
  can:['Talk about hobbies and what you (don\'t) like doing','Say when and how often you do things','Say where you like to go'],
  grammar:`
<h3>1 · любить and ходить: the consonant changes in "я"</h3>
<p>Both are и-conjugation, but the <b>я</b> form changes a consonant, and the stress moves after it:</p>
<table class="gt"><tr><th></th><th>любить (б → бл)</th><th>ходить (д → ж)</th></tr>
<tr><td>я</td><td><i class="ru">люблю</i></td><td><i class="ru">хожу</i></td></tr>
<tr><td>ты</td><td><i class="ru">любишь</i></td><td><i class="ru">ходишь</i></td></tr>
<tr><td>он / она</td><td><i class="ru">любит</i></td><td><i class="ru">ходит</i></td></tr>
<tr><td>мы</td><td><i class="ru">любим</i></td><td><i class="ru">ходим</i></td></tr>
<tr><td>вы</td><td><i class="ru">любите</i></td><td><i class="ru">ходите</i></td></tr>
<tr><td>они</td><td><i class="ru">любят</i></td><td><i class="ru">ходят</i></td></tr></table>
<p><b>любить</b> + accusative (<i class="ru">Я люблю музыку, спорт</i>) or + infinitive (<i class="ru">Я люблю читать</i>).</p>

<h3>2 · играть в vs. играть на</h3>
<table class="gt"><tr><td>sports and games</td><td><b>в</b> + accusative</td><td><i class="ru">играть в футбол, в теннис, в шахматы</i></td></tr>
<tr><td>instruments and devices</td><td><b>на</b> + prepositional</td><td><i class="ru">играть на гитаре, на пианино, на планшете</i></td></tr></table>

<h3>3 · Reflexive verbs: -ся / -сь</h3>
<p>Conjugate normally, then add <b>-ся</b> after a consonant and <b>-сь</b> after a vowel:</p>
<table class="gt"><tr><td><i class="ru">я катаюсь</i></td><td><i class="ru">мы катаемся</i></td></tr>
<tr><td><i class="ru">ты катаешься</i></td><td><i class="ru">вы катаетесь</i></td></tr>
<tr><td><i class="ru">он катается</i></td><td><i class="ru">они катаются</i></td></tr></table>
<p><i class="ru">кататься на</i> + prepositional: <i class="ru">на велосипеде, на лыжах, на коньках</i>.</p>

<h3>4 · Where? vs. where to?</h3>
<table class="gt"><tr><td><b>где?</b> (location)</td><td>в / на + <b>prepositional</b></td><td><i class="ru">Я в театре.</i></td></tr>
<tr><td><b>куда?</b> (direction)</td><td>в / на + <b>accusative</b></td><td><i class="ru">Я хожу в театр, в кино, на выставку.</i></td></tr></table>
<p class="tip">German speakers have this exact logic (wo? + Dativ, wohin? + Akkusativ). Use it: <span class="de">Wo? → Präpositiv, Wohin? → Akkusativ</span>.</p>

<h3>5 · Days of the week: в + accusative</h3>
<p><i class="ru">в понедельник, во вторник, в среду, в четверг, в пятницу, в субботу, в воскресенье</i>. Feminine days change -а → -у. How often: <i class="ru">всегда, обычно, часто, иногда, редко, никогда не</i>.</p>`,
  quiz:[
    ['— Наташа, вы … читать книги?', ['любит','любите'], 1, 'вы → любите.'],
    ['— Да, а ещё мы … играть в гандбол.', ['любят','любим'], 1, 'мы → любим.'],
    ['— Твой брат тоже играет в хоккей?<br>— Нет, он не … спорт.', ['любит','любят'], 0, 'он → любит.'],
    ['— Ты любишь гулять в парке?<br>— Нет, я … сидеть в Интернете.', ['любим','люблю'], 1, 'я → люблю (б → бл).'],
    ['Я люблю слушать … .', ['музыка','музыку'], 1, 'Object → accusative -у.'],
    ['В воскресенье наша семья любит … на природе.', ['отдыхает','отдыхать'], 1, 'любить + infinitive.'],
    ['— Когда ты … в теннис?', ['играешь','играете'], 0, 'ты → играешь.'],
    ['Маша очень любит музыку. Она играет … гитаре и пианино.', ['в','на'], 1, 'Instruments → на + prepositional.'],
    ['Наши дети любят спорт. Они часто играют … футбол.', ['в','на'], 0, 'Sports → в + accusative.'],
    ['— У тебя есть хобби?<br>— Да, я люблю … на велосипеде.', ['катаюсь','кататься'], 1, 'любить + infinitive.'],
    ['— Что ты сегодня делаешь?<br>— Я … на скейтборде.', ['катаюсь','катаешься'], 0, 'я → катаюсь (-сь after vowel).'],
    ['— Куда ты … в воскресенье?', ['ходит','ходишь'], 1, 'ты → ходишь.'],
    ['— Вы … на выставки?', ['ходят','ходите'], 1, 'вы → ходите.'],
    ['Это мои друзья. Мы вместе … в бассейн и в парк.', ['ходим','ходят'], 0, 'мы → ходим.'],
  ],
  drill:[
    ['я (любить)', 'люблю'], ['ты (любить)', 'любишь'], ['я (ходить)', 'хожу'], ['они (ходить)', 'ходят'],
    ['играть … футбол (preposition)', 'в'], ['играть на (гитара)', 'гитаре'], ['мы (кататься)', 'катаемся'],
    ['on Wednesday', 'в среду'], ['Я люблю (музыка).', 'музыку'], ['кататься на (велосипед)', 'велосипеде'],
  ],
  write:{id:'w6', prompt:'What do you do in your free time? Name three hobbies, say when/how often you do them (use days of the week), and where you like to go.', words:40},
},
{
  n:7, ru:'Приятного аппетита!', en:'Enjoy your meal!', kb:'KB p. 82–91 · ÜB p. 60–67',
  can:['Talk about what you eat and drink at each meal','Ask and tell the time','Host guests and thank the host','Order in a restaurant'],
  grammar:`
<h3>1 · Instrumental singular: "with"</h3>
<table class="gt"><tr><th>m / n</th><th>-ом / -ем</th><td><i class="ru">салат → с салатом, молоко → с молоком, картофель → с картофелем</i></td></tr>
<tr><th>f</th><th>-ой / -ей</th><td><i class="ru">колбаса → с колбасой, курица → с курицей</i></td></tr></table>
<p><b>с</b> + instrumental = with. <b>без</b> + genitive = without:</p>
<table class="gt"><tr><td><i class="ru">чай с лимоном и без сахара</i></td><td>tea with lemon and without sugar</td></tr>
<tr><td><i class="ru">вода без газа</i></td><td>still water</td></tr></table>

<h3>2 · Three irregular verbs you'll use constantly</h3>
<table class="gt"><tr><th></th><th>есть (eat)</th><th>пить (drink)</th><th>хотеть (want)</th></tr>
<tr><td>я</td><td><i class="ru">ем</i></td><td><i class="ru">пью</i></td><td><i class="ru">хочу</i></td></tr>
<tr><td>ты</td><td><i class="ru">ешь</i></td><td><i class="ru">пьёшь</i></td><td><i class="ru">хочешь</i></td></tr>
<tr><td>он / она</td><td><i class="ru">ест</i></td><td><i class="ru">пьёт</i></td><td><i class="ru">хочет</i></td></tr>
<tr><td>мы</td><td><i class="ru">едим</i></td><td><i class="ru">пьём</i></td><td><i class="ru">хотим</i></td></tr>
<tr><td>вы</td><td><i class="ru">едите</i></td><td><i class="ru">пьёте</i></td><td><i class="ru">хотите</i></td></tr>
<tr><td>они</td><td><i class="ru">едят</i></td><td><i class="ru">пьют</i></td><td><i class="ru">хотят</i></td></tr></table>
<p class="tip">хотеть is е-conjugation in the singular and и-conjugation in the plural. That's why the exam likes it.</p>

<h3>3 · Dative pronouns: мне, тебе, нам, вам</h3>
<p>"To / for me": <i class="ru">Мне, пожалуйста, чай.</i> (For me, tea please.) <i class="ru">Что вам принести?</i> (What can I bring you?) <i class="ru">Принесите нам воду.</i></p>

<h3>4 · Telling the time</h3>
<table class="gt"><tr><th></th><th>hours</th><th>minutes</th></tr>
<tr><td>1</td><td><i class="ru">час</i></td><td><i class="ru">одна минута</i></td></tr>
<tr><td>2, 3, 4</td><td><i class="ru">часа</i></td><td><i class="ru">две, три, четыре минуты</i></td></tr>
<tr><td>5–20</td><td><i class="ru">часов</i></td><td><i class="ru">пять … минут</i></td></tr></table>
<p>Same last-digit logic as rubles: <i class="ru">22 часа, 21 минута</i>. Ask: <i class="ru">Который час? / Сколько времени?</i> "At" a time = <b>в</b>: <i class="ru">В 8 часов 30 минут мы ужинаем.</i></p>

<h3>5 · Meals</h3>
<p><i class="ru">на завтрак / на обед / на ужин / на десерт</i> = for breakfast / lunch / dinner / dessert. Verbs: <i class="ru">завтракать, обедать, ужинать</i>. Times of day: <i class="ru">утром, днём, вечером</i>. Numbers now go to 1000: <i class="ru">триста, четыреста, пятьсот … девятьсот, тысяча</i>.</p>`,
  quiz:[
    ['Что ты обычно … на обед?', ['ем','едят','ешь'], 2, 'ты → ешь.'],
    ['На обед я обычно … щи.', ['ем','ест','ешь'], 0, 'я → ем.'],
    ['Утром мы любим … кашу.', ['ест','есть','ешь'], 1, 'любить + infinitive есть.'],
    ['Они … воду и сок.', ['пьют','пьёт','пить'], 0, 'они → пьют.'],
    ['Попробуйте блины с … .', ['творогом','творог'], 0, 'с + instrumental → творогом.'],
    ['Нам, пожалуйста, пироги с … .', ['курицей','курица'], 0, 'с + instrumental, feminine -ей.'],
    ['Я очень … есть.', ['хотеть','хочу','хочешь'], 1, 'я → хочу.'],
    ['Мы не … рыбу.', ['хотим','хотят','хотеть'], 0, 'мы → хотим.'],
    ['— Сколько сейчас времени?<br>— Сейчас 8 … 20 минут.', ['час','часа','часов'], 2, '8 → часов.'],
    ['Сейчас 22 … 31 минута.', ['час','часа','часов'], 1, 'Ends in 2 → часа.'],
    ['— Когда мы сегодня обедаем?<br>— …', ['В два часа.','Два часа.'], 0, 'когда? (at what time) → в + time.'],
    ['— Скажите, который час?<br>— Сейчас 10 часов 21 … .', ['минута','минуты','минут'], 0, 'Ends in 1 → минута.'],
    ['Мы ужинаем сегодня в 18 часов 30 … .', ['минута','минуты','минут'], 2, '30 → минут.'],
    ['Вы хотите …?', ['пицца','пиццей','пиццу'], 2, 'Object of хотеть → accusative пиццу.'],
    ['Я не пью воду без … .', ['газ','газа','газом'], 1, 'без + genitive → газа.'],
    ['Мне, пожалуйста, чай без … .', ['лимон','лимона','лимоном'], 1, 'без + genitive → лимона.'],
    ['Что вы хотите? Что … принести?', ['вы','вас','вам'], 2, 'bring to you → dative вам.'],
    ['Мы хотим пить. Принесите …, пожалуйста, воду.', ['мне','нам','вам'], 1, 'мы → to us → нам.'],
  ],
  drill:[
    ['я (есть)', 'ем'], ['они (есть)', 'едят'], ['ты (пить)', 'пьёшь'], ['мы (хотеть)', 'хотим'], ['он (хотеть)', 'хочет'],
    ['чай с (лимон)', 'лимоном'], ['кофе без (сахар)', 'сахара'], ['с (рыба)', 'рыбой'], ['3 (час)', 'часа'], ['5 (минута)', 'минут'],
    ['For me, please, … (start of an order)', 'Мне, пожалуйста'], ['500 in words', 'пятьсот'],
  ],
  write:{id:'w7', prompt:'Describe a normal day of eating: what you eat and drink for breakfast, lunch and dinner, and at what time. Then order a meal in a café (3–4 lines of dialog).', words:45},
},
{
  n:8, ru:'Что мы носим', en:'What we wear', kb:'KB p. 92–101 · ÜB p. 68–75',
  can:['Name clothes and colors','Ask about price and size','Say what you think of clothes and give compliments','Talk about what you like to wear'],
  grammar:`
<h3>1 · носить (с → ш in "я")</h3>
<p><i class="ru">я ношу, ты носишь, он носит, мы носим, вы носите, они носят</i>. Same pattern as <i class="ru">ходить → хожу</i>.</p>

<h3>2 · этот: this</h3>
<table class="gt"><tr><th></th><th>m</th><th>f</th><th>n</th><th>pl</th></tr>
<tr><td>Nom.</td><td><i class="ru">этот</i></td><td><i class="ru">эта</i></td><td><i class="ru">это</i></td><td><i class="ru">эти</i></td></tr>
<tr><td>Acc.</td><td><i class="ru">этот</i></td><td><b><i class="ru">эту</i></b></td><td><i class="ru">это</i></td><td><i class="ru">эти</i></td></tr></table>
<p><i class="ru">Покажите мне, пожалуйста, эти шорты, эту блузку, это платье и этот свитер.</i></p>
<p class="tip">Don't mix up <i class="ru">это платье</i> (this dress) and <i class="ru">Это платье.</i> (This is a dress.).</p>

<h3>3 · Adjectives: nominative</h3>
<table class="gt"><tr><th></th><th>m</th><th>f</th><th>n</th><th>pl</th></tr>
<tr><td>hard, stem-stressed</td><td><i class="ru">белый</i></td><td><i class="ru">белая</i></td><td><i class="ru">белое</i></td><td><i class="ru">белые</i></td></tr>
<tr><td>hard, end-stressed</td><td><i class="ru">голубой</i></td><td><i class="ru">голубая</i></td><td><i class="ru">голубое</i></td><td><i class="ru">голубые</i></td></tr>
<tr><td>soft</td><td><i class="ru">синий</i></td><td><i class="ru">синяя</i></td><td><i class="ru">синее</i></td><td><i class="ru">синие</i></td></tr></table>
<p class="tip">The 7-letter rule again: after г к х ж ш ч щ write <b>и</b>, never ы: <i class="ru">маленький, дорогие, большие, хорошие</i>. After ж ш ч щ an unstressed о becomes е: <i class="ru">хорошее</i> (not "хорошое").</p>
<p>Adjectives agree with their noun: <i class="ru">зелёная рубашка, модное пальто, удобные кроссовки</i>. <b>какой?</b> (which? / what kind of?) works exactly like an adjective: <i class="ru">какой костюм, какая футболка, какое платье, какие туфли</i>.</p>

<h3>4 · Adjectives: accusative</h3>
<p>For things, the accusative looks like the nominative, <b>except feminine: -ую / -юю</b>.</p>
<table class="gt"><tr><td><i class="ru">Какую куртку вы хотите? — Коричневую или синюю?</i></td></tr></table>

<h3>5 · "I like it" and "it suits you" use the dative</h3>
<p>In Russian the <b>thing</b> is the subject and the person is in the dative: "it pleases me".</p>
<table class="gt"><tr><td><i class="ru">Мне нравится эта куртка.</i></td><td>I like this jacket.</td></tr>
<tr><td><i class="ru">Мне нравятся эти джинсы.</i></td><td>I like these jeans. (plural → нравятся)</td></tr>
<tr><td><i class="ru">Эта блузка вам очень идёт!</i></td><td>This blouse really suits you!</td></tr></table>
<p>Color questions: <i class="ru">Какого цвета футболка? — Красная.</i> Numbers now go to 20 000 for prices: <i class="ru">пять тысяч триста рублей</i>.</p>`,
  quiz:[
    ['— Сколько стоит … платье?<br>— 5300 рублей.', ['эта','это'], 1, 'платье is neuter → это.'],
    ['— … блузка вам очень идёт!', ['Это','Эта'], 1, 'блузка is feminine → Эта.'],
    ['Наташа, … пуловер стоит 7800 рублей.', ['эти','этот'], 1, 'пуловер is masculine → этот.'],
    ['Дайте мне, пожалуйста, … блузку.', ['эту','эта'], 0, 'Accusative feminine → эту.'],
    ['— У вас есть … рубашки?<br>— Да. Какой у вас размер?', ['белая','белые'], 1, 'рубашки is plural → белые.'],
    ['— Виктор, тебе нравится эта … куртка?', ['синяя','синюю'], 0, 'куртка is the subject of нравится → nominative синяя.'],
    ['— Ира, это … пальто тебе очень идёт!', ['красные','красное'], 1, 'пальто is neuter → красное.'],
    ['— Какой костюм вы хотите? …?', ['Классические','Классический'], 1, 'костюм is masculine singular.'],
    ['— … у вас размер?<br>— 44-ый.', ['Какая','Какой'], 1, 'размер is masculine → Какой.'],
    ['— … футболку мне примерить? Голубую или жёлтую?', ['Какую','Какая'], 0, 'Accusative feminine → Какую.'],
    ['У нас строгий дресс-код, поэтому я ношу костюм и … рубашку.', ['белое','белую'], 1, 'Accusative feminine → белую.'],
    ['— Лена, что ты покупаешь?<br>— … туфли на высоком каблуке.', ['модные','модную'], 0, 'туфли is plural → модные.'],
    ['— Какую одежду ты любишь … дома?', ['носишь','носить'], 1, 'любить + infinitive.'],
    ['— Что вы обычно носите в офисе?<br>— На работе я … костюм.', ['ношу','носит'], 0, 'я → ношу.'],
  ],
  drill:[
    ['я (носить)', 'ношу'], ['Дайте (этот) блузку.', 'эту'], ['(белый) рубашка', 'белая'], ['(синий) платье', 'синее'],
    ['(большой) сумки', 'большие'], ['Я хочу (красный) куртку.', 'красную'], ['Мне (нравиться) эти джинсы.', 'нравятся'],
    ['Вам (идти) этот цвет.', 'идёт'], ['(какой) платье?', 'какое'], ['(хороший) пальто', 'хорошее'],
  ],
  write:{id:'w8', prompt:'What do you usually wear at school, at home, and at a party? What is your favorite color? Describe one piece of clothing you really like (color, price, why).', words:45},
},
{
  n:9, ru:'С праздником!', en:'Happy holidays!', kb:'KB p. 102–113 · ÜB p. 76–83',
  can:['Name holidays and say when they are','Ask and give the date and someone\'s age','Congratulate and wish someone well','Talk about presents'],
  grammar:`
<h3>1 · Verbs in -овать / -евать</h3>
<p>In the present tense, <b>-ова- / -ева-</b> becomes <b>-у-</b>:</p>
<table class="gt"><tr><td><i class="ru">праздновать → я праздную, ты празднуешь … они празднуют</i></td></tr>
<tr><td><i class="ru">танцевать → я танцую, ты танцуешь … они танцуют</i></td></tr>
<tr><td><i class="ru">фотографировать → я фотографирую …</i></td></tr></table>

<h3>2 · Months: в + prepositional</h3>
<p><i class="ru">в январе, в феврале, в марте, в апреле, в мае, в июне, в июле, в августе, в сентябре, в октябре, в ноябре, в декабре</i>. Months aren't capitalized. Seasons: <i class="ru">зимой, весной, летом, осенью</i> (no preposition).</p>

<h3>3 · Ordinal numbers and dates</h3>
<p>Ordinals behave like adjectives: <i class="ru">первый, второй, третий, четвёртый, пятый …</i> In compound numbers only the last word is ordinal: <i class="ru">двадцать седьмой</i>.</p>
<table class="gt"><tr><td>What's the date?</td><td><i class="ru">Какое сегодня число?</i></td></tr>
<tr><td>Today is May 1.</td><td><i class="ru">Сегодня первое мая.</i><br>neuter ordinal (nom.) + month in the <b>genitive</b></td></tr>
<tr><td>On what date?</td><td><i class="ru">Какого числа?</i></td></tr>
<tr><td>On May 1.</td><td><i class="ru">Первого мая.</i><br>everything in the <b>genitive</b></td></tr></table>
<p class="tip">The ordinal is neuter because it agrees with the hidden word <i class="ru">число</i> (date). Dates are written without a dot: 2 мая.</p>

<h3>4 · Dative: giving and wishing "to" someone</h3>
<table class="gt"><tr><th>m</th><td>-у / -ю</td><td><i class="ru">брат → брату, учитель → учителю</i></td></tr>
<tr><th>f</th><td>-е / -и</td><td><i class="ru">мама → маме, подруга → подруге, Мария → Марии</i></td></tr></table>
<p>Pronouns: <i class="ru">мне, тебе, ему, ей, нам, вам, им</i>. <i class="ru">дарить</i> <b>кому</b> (dative) <b>что</b> (accusative): <i class="ru">Я дарю подруге книгу. Мы дарим учителю цветы.</i></p>

<h3>5 · Age: dative + год / года / лет</h3>
<table class="gt"><tr><td><i class="ru">Сколько тебе лет? — Мне двадцать один год.</i></td></tr>
<tr><td><i class="ru">Ей двадцать три года. Ему тридцать лет.</i></td></tr></table>
<p>Same last-digit rule: 1 → <i class="ru">год</i>, 2–4 → <i class="ru">года</i>, 5–20 and 0 → <i class="ru">лет</i>.</p>

<h3>6 · Animate masculine accusative = genitive</h3>
<p>Masculine <b>people and animals</b> take <b>-а / -я</b> in the accusative: <i class="ru">Я фотографирую брата, учителя.</i> Things don't change: <i class="ru">Я фотографирую парк, музей.</i> Congratulate someone: <i class="ru">поздравлять</i> + accusative + <i class="ru">с</i> + instrumental: <i class="ru">Я поздравляю друга с днём рождения!</i></p>`,
  quiz:[
    ['Моя семья … Женский день.', ['праздновать','празднует'], 1, 'семья = она → празднует.'],
    ['Мы любим … Новый год.', ['праздновать','празднуем'], 0, 'любить + infinitive.'],
    ['Рождество люди в России празднуют седьмого … .', ['январь','январе','января'], 2, 'Date → month in the genitive.'],
    ['У меня день рождения в … .', ['июль','июле','июля'], 1, 'в + month → prepositional июле.'],
    ['— Когда у тебя день рождения?<br>— …', ['Второго февраля.','Второе февраля.'], 0, 'Когда? → all genitive: второго февраля.'],
    ['Сегодня двадцать … сентября.', ['третье','третьего'], 0, 'Сегодня … → nominative neuter ordinal.'],
    ['У сестры день рождения … октября.', ['тридцать первое','тридцать первого'], 1, 'When something happens on a date → genitive.'],
    ['Что ты обычно даришь …?', ['брат','брата','брату'], 2, 'дарить кому → dative брату.'],
    ['Мы дарим … цветы.', ['Мария','Марии'], 1, 'Dative of Мария → Марии.'],
    ['Я дарю … футболку.', ['сестра','сестре','сестру'], 1, 'дарить кому → dative сестре.'],
    ['Я поздравляю … с праздником.', ['учитель','учителю','учителя'], 2, 'поздравлять кого → accusative; animate masculine = -я.'],
    ['Олег фотографирует … .', ['мама','мамы','маму'], 2, 'Accusative feminine → маму.'],
    ['Что ты обычно даришь …?', ['папа','папе','папу'], 1, 'дарить кому → dative папе.'],
    ['— Что ты даришь бабушке?<br>— Обычно я дарю … книгу.', ['ей','ему','им'], 0, 'бабушка = she → ей.'],
    ['Я очень люблю … .', ['дедушка','дедушке','дедушку'], 2, 'любить + accusative; дедушка declines like a feminine -а noun → дедушку.'],
    ['— Что вы дарите детям?<br>— Мы дарим … игрушки.', ['ей','ему','им'], 2, 'дети = they → им.'],
    ['Сколько лет …?', ['Ирины','Ирине'], 1, 'Age uses the dative → Ирине.'],
    ['… 38 лет.', ['Виктора','Виктору'], 1, 'Age uses the dative → Виктору.'],
  ],
  drill:[
    ['я (праздновать)', 'праздную'], ['in March', 'в марте'], ['Today is May 1. (in words)', 'Сегодня первое мая'], ['on May 9 (in words)', 'девятого мая'],
    ['Я дарю (брат) книгу.', 'брату'], ['Мы дарим (мама) цветы.', 'маме'], ['Сколько (он) лет?', 'ему'],
    ['Мне 21 (год).', 'год'], ['Ей 23 (год).', 'года'], ['Ему 30 (год).', 'лет'], ['Я поздравляю (друг).', 'друга'],
  ],
  write:{id:'w9', prompt:'Write a birthday card to a friend (congratulate, wish 2–3 things). Then write when your birthday is, how old you are, and what your favorite holiday is and how you celebrate it.', words:45},
},
];

// Reading passages for the mock exam. lessons = the lessons whose grammar/vocab it needs.
const READINGS = [
  {id:'r1', lessons:[2,3,4], title:'Лиза', text:'Меня зовут Лиза. Я из Германии, из Гамбурга, но сейчас я живу в Москве. Я студентка. Я говорю по-немецки, по-английски и немного по-русски. У меня есть брат и сестра. Брата зовут Макс, он инженер и работает на заводе. Сестру зовут Анна, она врач и работает в больнице. Мои родители живут в Гамбурге. Папа журналист, а мама учительница.',
   items:[['Liza is from Hamburg.',true],['Liza lives in Hamburg now.',false],['Liza speaks Russian fluently.',false],['Max works at a factory.',true],['Anna is a teacher.',false],['Liza\'s mom is a teacher.',true]]},
  {id:'r2', lessons:[5,6,7], title:'Суббота', text:'В субботу Олег обычно ходит на рынок. Там он покупает хлеб, сыр, помидоры и яблоки. Яблоки стоят сто двадцать рублей килограмм. Потом он гуляет в парке или играет в теннис. Вечером Олег и его подруга Маша ужинают в кафе. Маша не ест мясо. Она ест рыбу с рисом и пьёт чай с лимоном. Олег хочет пиццу и пьёт сок.',
   items:[['Oleg usually goes to the market on Sundays.',false],['Apples cost 120 rubles a kilo.',true],['After the market he plays volleyball.',false],['Masha eats fish with rice.',true],['Masha drinks tea with sugar.',false],['Oleg drinks juice.',true]]},
  {id:'r3', lessons:[8,9], title:'День рождения', text:'Сегодня двадцать пятое декабря. У Кати день рождения! Ей девятнадцать лет. Мама дарит Кате красное платье, а брат дарит ей книгу. Катя очень любит Новый год. В России Рождество празднуют седьмого января. Вечером Катя и её друзья танцуют. Катя носит новое платье и чёрные туфли.',
   items:[['Today is December 25.',true],['Katya is 18.',false],['Her mom gives her a red dress.',true],['Her brother gives her flowers.',false],['In Russia, Christmas is on January 7.',true],['Katya wears white shoes.',false]]},
];

// German instructions and grammar terms that will appear on the exam paper.
const EXAM_GERMAN = [
  ['Setzen Sie die Endungen / Wörter ein.','Fill in the endings / words.','Вставьте окончания / слова.'],
  ['Wählen Sie die richtige Antwort aus.','Choose the correct answer.','Выберите правильный ответ.'],
  ['Kreuzen Sie an.','Tick / check the box.','Отметьте.'],
  ['Richtig oder falsch?','True or false?','Правильно или неправильно?'],
  ['Ergänzen Sie die Sätze / die Tabelle.','Complete the sentences / the table.','Дополните предложения / таблицу.'],
  ['Beantworten Sie die Fragen.','Answer the questions.','Ответьте на вопросы.'],
  ['Stellen Sie Fragen.','Ask questions.','Задайте вопросы.'],
  ['Formulieren Sie die Fragen.','Write the questions.','Сформулируйте вопросы.'],
  ['Übersetzen Sie die Sätze ins Russische.','Translate the sentences into Russian.','Переведите предложения на русский.'],
  ['Ordnen Sie zu.','Match (the items).','Подберите / соедините.'],
  ['Bilden Sie Sätze.','Make sentences.','Составьте предложения.'],
  ['Bilden Sie den Plural.','Form the plural.','Образуйте множественное число.'],
  ['Konjugieren Sie die Verben.','Conjugate the verbs.','Проспрягайте глаголы.'],
  ['Markieren Sie die Betonung.','Mark the stress.','Поставьте ударение.'],
  ['Verneinen Sie die Sätze.','Make the sentences negative.','Ответьте отрицательно.'],
  ['Korrigieren Sie die Fehler.','Correct the mistakes.','Исправьте ошибки.'],
  ['Lesen Sie den Text.','Read the text.','Прочитайте текст.'],
  ['Welches Wort passt nicht in die Reihe?','Which word doesn\'t belong?','Какое слово лишнее?'],
  ['Schreiben Sie einen Text über …','Write a text about …','Напишите текст о …'],
  ['Schreiben Sie in Schreibschrift.','Write in cursive (handwriting).','Напишите прописью.'],
  ['Beschreiben Sie das Foto.','Describe the photo.','Опишите фотографию.'],
  ['Notieren Sie …','Write down …','Запишите …'],
];
const GERMAN_TERMS = [
  ['Nominativ','nominative: the subject, dictionary form'],['Genitiv','genitive: "of", after из, у, без, нет, 2–4'],
  ['Dativ','dative: "to / for" someone, мне нравится, age'],['Akkusativ','accusative: the direct object, куда?'],
  ['Instrumental','instrumental: "with" (с), by means of'],['Präpositiv','prepositional: after в / на / о for где?'],
  ['Maskulinum / Femininum / Neutrum','masculine / feminine / neuter'],['Singular / Plural','singular / plural'],
  ['Endung','ending'],['Stamm / Stammauslaut','stem / last letter of the stem'],['Konjugation','conjugation (е- or и-)'],
  ['Betonung','stress (the accented vowel)'],['Zischlaut','hushing consonant: ж ш ч щ'],
  ['Weichheitszeichen / Härtezeichen','soft sign ь / hard sign ъ'],['Rektion','which case a word requires'],
  ['Grundzahl / Ordnungszahl','cardinal (два) / ordinal (второй) number'],['belebt / unbelebt','animate / inanimate'],
  ['Vokalausfall','fleeting vowel (огурец → огурцы)'],['Personalpronomen','personal pronoun'],
  ['Possessivpronomen','possessive (мой, твой…)'],['Demonstrativpronomen','demonstrative (этот)'],
  ['Infinitiv','infinitive (-ть)'],['Präsens','present tense'],['reflexiv','reflexive (-ся / -сь)'],
];

// The 33 letters. [letter, sound in English, example word, "trap" note]
const ALPHABET = [
  ['А а','a in "father"','ма́ма',''],['Б б','b','банк',''],['В в','v','вода́','Looks like B, sounds like V'],
  ['Г г','g in "go"','го́род',''],['Д д','d','дом',''],['Е е','ye in "yes"','е́вро',''],['Ё ё','yo in "yonder"','мёд','Always stressed'],
  ['Ж ж','s in "measure"','жена́',''],['З з','z','зоопа́рк','Looks like 3'],['И и','ee in "meet"','и́мя','Looks like a backward N'],
  ['Й й','y in "boy"','чай',''],['К к','k','ко́фе',''],['Л л','l','лимо́н',''],['М м','m','метро́',''],
  ['Н н','n','нет','Looks like H, sounds like N'],['О о','o (stressed) / a (unstressed)','молоко́',''],['П п','p','па́па',''],
  ['Р р','rolled r','рестора́н','Looks like P, sounds like R'],['С с','s','суп','Looks like C, always S'],['Т т','t','торт',''],
  ['У у','oo in "boot"','у́лица','Looks like y, sounds like OO'],['Ф ф','f','футбо́л',''],['Х х','kh, as in "Bach"','хлеб','Looks like X'],
  ['Ц ц','ts in "cats"','цирк',''],['Ч ч','ch in "cheese"','чай',''],['Ш ш','sh (hard)','шарф',''],['Щ щ','shsh (soft, long)','щи',''],
  ['Ъ ъ','hard sign (no sound)','объе́кт','Separates sounds'],['Ы ы','i in "bit" pushed back','ры́ба','No English equivalent'],
  ['Ь ь','soft sign (no sound)','день','Softens the consonant before it'],['Э э','e in "met"','э́то',''],
  ['Ю ю','yu in "you"','ю́бка',''],['Я я','ya in "yard"','я',''],
];

// Default study plan: 16 Dec exam, assuming the class covers Lektion 1–9.
const DEFAULT_WEEKS = [
  ['2026-09-28','Lektion 1–2: alphabet, greetings, names, из + genitive'],
  ['2026-10-05','Lektion 3: conjugations, в/на + prepositional, numbers 1–20'],
  ['2026-10-12','Lektion 4: family, у меня есть / нет, possessives'],
  ['2026-10-19','Lektion 5: shopping, plurals, accusative, prices'],
  ['2026-10-26','Lektion 6: free time, любить/ходить, где? vs. куда?'],
  ['2026-11-02','Review 1–6 + first mock exam'],
  ['2026-11-09','Lektion 7: food, instrumental, есть/пить/хотеть, time'],
  ['2026-11-16','Lektion 8: clothes, adjectives, этот, нравится'],
  ['2026-11-23','Lektion 9: holidays, dates, dative, age'],
  ['2026-11-30','Full review 1–9 + mock exam 2'],
  ['2026-12-07','Fix weak spots, mock exam 3, writing tasks'],
  ['2026-12-14','Exam week: light review only. Exam Wed 16 Dec'],
];
