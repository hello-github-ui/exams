---
title: 三歪教你学Java集合(1)
source: Java3y/基础知识原创电子书/Java集合 电子书/三歪教你学Java集合(1).pdf
pages: 123
converted_at: 2026-06-22 22:29:28
---

# 三歪教你学Java集合(1)

ڹ᥺
Ӟ̵਍ԟ೰ܖ
Ӟ̵Javaᵞݳ਍ԟ೰ܖ
1.1਍ԟӞᶱದ๞ԏڹ҅஠ᶳᎣ᭲ԅՋԍᥝ਍ਙѺ
1.2ই֜فᳪ਍ԟJavaᵞݳ
1.3 ᵞݳᬰᴤӨᶎᦶ
ԫ̵Collection
Ӟ̵ᵞݳ(Collection)Օᕨ
1.1ԅՋԍᵱᥝCollection
1.2හᕟ޾ᵞݳጱ܄ڦ
1.3Collectionጱኧ๶Өۑᚆ
ԫ̵ᬽդ࢏(Iterator)Օᕨ
ӣ̵ListᵞݳՕᕨ
3.1Listᵞݳଉአৼᔄ
ࢥ̵SetᵞݳՕᕨ
4.1Setᵞݳଉአৼᔄ
ӣ̵Listᵞݳ
Ӟ̵ArrayListᥴຉ
1.1຅᭜ොဩ
1.2Addොဩ
1.2.1add(E e)
1.2.2add(int index, E element)
1.3 getොဩ
1.4 setොဩ
1.5removeොဩ
1.6ᕡᜓٚ᧔ก
ԫ̵VectorӨArrayList܄ڦ
ӣ̵LinkedListᥴຉ
3.1຅᭜ොဩ
3.2addොဩ
3.3removeොဩ
3.4getොဩ
3.5setොဩ
ࢥ̵Listᵞݳ௛ᕮ
ࢥ̵Mapᵞݳ
Ӟ̵MapՕᕨ
1.1ԅՋԍᵱᥝMap
1.2MapӨCollectionጱ܄ڦ
1.3Mapጱۑᚆ
ԫ̵වڜᤒՕᕨ
2.1වڜᤒૡ֢ܻቘ
ӣ̵ᕁἓ໅Օᕨ
3.1ࢧᶶԫ݉ັತ໅
3.2Ꭳෛ2-3໅
3.3՗2-3໅کᕁἓ໅
3.4ᕁἓ໅चᏐᎣᦩ
Բ̵HashMap

---

Ӟ̵HashMapڽຉ
1.1HashMap຅᭜ොဩ
1.2putොဩ
1.3getොဩ
1.4removeොဩ
ԫ̵HashMapӨHashtable੒ྲ
ӣ̵HashMap௛ᕮ
م̵LinkedHashMap
Ӟ̵LinkedHashMap
1.1LinkedHashMapጱऒ
1.2LinkedHashMap᯿ٟጱොဩ
1.3຅᭜ොဩ
1.4putොဩ
1.5getොဩ
1.6removeොဩ
1.7᭭ܲጱොဩ
ԫ̵LinkedHashMap௛ᕮ
Ӡ̵TreeMap
Ӟ̵TreeMapڽຉ
1.1TreeMapጱऒ
1.2TreeMap຅᭜ොဩ
1.3putොဩ
1.4getොဩ
1.5removeොဩ
1.6᭭ܲොဩ
ԫ̵TreeMap௛ᕮ
ك̵ConcurrentHashMap
Ӟ̵ConCurrentHashMapڽຉ
1.1ڡᦩConCurrentHashMap
1.2JDK1.7ବ੶ਫሿ
1.3ํԧHashtableԅࠨᵱᥝConCurrentHashMap
1.4CASᓒဩ޾volatileᓌܔՕᕨ
1.5ConCurrentHashMapऒ
1.6ConCurrentHashMap຅᭜ොဩ
1.7putොဩ
1.8getොဩ
ԫ̵ConcurrentHashMap௛ᕮ
Ԝ̵Set
Ӟ̵HashSetڽຉ
ԫ̵TreeSetڽຉ
ӣ̵LinkedHashSetڽຉ
ࢥ̵Setᵞݳ௛ᕮ
܈̵CopyOnWriteArrayList
Ӟ̵Vector޾SynchronizedList
1.1ࢧᶶᕚᑕਞقጱVector޾SynchronizedList
1.2Vector޾SynchronizedListݢᚆտڊሿጱᳯ᷌
ԫ̵CopyOnWriteArrayList(Set)Օᕨ
2.1CopyOnWriteArrayListਫሿܻቘ
2.1.1፡ӞӥCopyOnWriteArrayListच๜ጱᕮ຅

---

2.1.2ଉᥠොဩጱਫሿ
2.1.3ڽຉԅՋԍ᭭ܲ෸ӧአ᧣አᘏดୗےᲁ
2.1.4CopyOnWriteArrayListᗌᅩ
2.1.5CopyOnWriteSet
܈Ӟ̵Javaᵞݳᶎᦶ᷌
Ӟ̵ArrayList޾Vectorጱ܄ڦ
ԫ̵HashMap޾Hashtableጱ܄ڦ
ӣ̵List޾Mapጱ܄ڦ
ࢥ̵Set᯾ጱزᔰฎӧᚆ᯿॔ጱ҅ᮎԍአՋԍොဩ๶܄ړ᯿॔Өވޫ? ฎአ==ᬮฎequals()?
Բ̵Collection޾Collectionsጱ܄ڦ
م̵᧔ڊArrayList,LinkedListጱਂؙ௔ᚆ޾ᇙ௔
6.1ಘ઀ғ
Ӡ̵Enumeration޾Iteratorളݗጱ܄ڦ
ك̵ListIteratorํՋԍᇙᅩ
Ԝ̵ଚݎᵞݳᔄฎՋԍҘ
܈̵JavaӾHashMapጱkey꧊ᥝฎԅᔄ੒᨝ڞᧆᔄᵱᥝჿ᪃Ջԍ๵կҘ
܈Ӟ̵ӨJavaᵞݳ໛ຝፘىጱํߺԶ๋অጱਫ᪢
܈ԫ̵ArrayListᵞݳےف1ӡ๵හഝ҅ଫᧆெԍ൉ṛපሲ
 
ڹ᥺
 
ᬯӻ෈໩ጱٖ਻ᕍಋ಑҅ইຎమᥝ፡ๅग़ጱଗᨵ෈ᒍ҅ىဳ౯ጱلռݩғJava3y̶ํๅग़ጱܻڠದ๞෈
ᒍ޾ଗᨵѺ
 
ፓڹዙᇰ॒ԭዙᇰๅෛPDFӾ҅ݝᥝฎJavaݸᒒጱᎣᦩ҅᮷տํѺཻᬨ๶౯لռݩ؛ๅѺஙמ൤
ᔱғJava3y
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺلռݩํ౯ጱᘶᔮොୗ

![三歪教你学Java集合(1) 第3页插图](../assets/images/三歪教你学Java集合(1)_p3_1_3c233a1a.jpeg)

---

Javaᔜᗦᚏࢶ
Java਍ԟ᪠ᕚ
୏ݎଉአૡٍ
ᔜᗦኪৼԡ̵෈໩
ࣁلռݩӥࢧ॔̿888̀ܨݢ឴ݐѺѺ
 
਍ԟӧᚆፖፓ҅᪙፳౯҅տᦏ֦Ԫ܎ۑ׭
 
෈໩꧋ᦜᵋ఺փඎ҅֕ӧᚆץදձٖ֜਻̶
 
ኪৼԡጱෆቘԞฎꂁӧ਻ฃ҅ইຎ֦ᥧ஑ํଆۗ҅మᥝ಑ᩝ֢ᘏ҅ᮎԍݢզ᭗ᬦᬯӻතྃᎱ಑ᩝ౯҅ᰂ
᷐ӧ᯿ᥝ҅ஞ఺๋᯿ᥝ̶Ԇᥝฎ౯ݢզ᭗ᬦᬯӻ಑ᩝఘ٭๶ᶼᦇय़ਹ੒ᬯ๜ኪৼԡጱᦧհ҅ࢃࢃ
 
 
Ӟ̵਍ԟ೰ܖ
 
Ӟ̵Javaᵞݳ਍ԟ೰ܖ
 
๜෈տ൉ڊஉग़ݢᚆෛಋտమکጱᳯ᷌҅֕ӧտӞӞᥴᒼ҅ݝտஃय़ොݻ݄᧔กጮ̶๜෈ጱٖ਻
؇ݻԭ೰ܖ҅ᘒᶋದ๞රᑕᦖᥴ̶
ইຎమᥝ஑کٍ֛ጱᒼໜ҅ݢզᘉᴅ౯้ᕪٟᬦጱᩒ
ාғhttps://github.com/ZhongFuCheng3y/3y҅౲ᘏےفՈ಍Իၞᗭ᪙ռग़୏ݎᘏᦎᦞ҅ڹᶎጱ
Github᱾ളํ౯ጱᘶᔮොୗ̶
1.1਍ԟӞᶱದ๞ԏڹ҅஠ᶳᎣ᭲ԅՋԍᥝ਍ਙѺ
 
Q: ౯ժ஑Ꭳ᭲ԅՋԍᥝ਍ԟJavaᵞݳ҅਍کJavaᵞݳጱ෸ײ૪ᕪ਍ᬦԧහᕟԧ҅ԅՋԍ౯ӧአහᕟݍᘒ
አJavaᵞݳ̶හᕟ޾JavaᵞݳํՋԍ܄ڦҘ

![三歪教你学Java集合(1) 第4页插图](../assets/images/三歪教你学Java集合(1)_p4_1_46627a5a.jpeg)

![三歪教你学Java集合(1) 第4页插图](../assets/images/三歪教你学Java集合(1)_p4_2_08125413.png)

![三歪教你学Java集合(1) 第4页插图](../assets/images/三歪教你学Java集合(1)_p4_3_a7b96e96.jpeg)

---

A:JavaฎӞᳪᶎݻ੒᨝ጱ᧍᥺҅੪عӧԧ॒ቘ੒᨝҅ԅԧො׎඙֢ग़ӻ੒᨝҅ᮎԍ౯ժ੪஑಩ᬯग़ӻ੒
᨝ਂؙ᩸๶҅మᥝਂؙग़ӻ੒᨝(ݒᰁ),உ਻ฃ੪ᚆమکӞӻ਻࢏(ᵞݳ)๶ᤰ᫹
 
௛ጱ๶᧔ғ੪ฎJavaᕳ౯ժ൉׀ԧૡٍො׎౯ժ݄඙֢ग़ӻJava੒᨝̶
1.2ই֜فᳪ਍ԟJavaᵞݳ
 
Q: ՗Ӥᶎ౯ժ૪ᕪᎣ᭲ԧԅՋԍᥝ਍Javaᵞݳ҅ӥᶎ౯ժ੪ᧆᎣ᭲Javaᵞݳጱच๜አဩ҅զ݊՗ਙෆ֛
ጱᎣᦩᅩ݄ԧᥴਙฎՋԍ
Aғ ౯ժ਍ԟJavaᵞݳਫᴬӤ੪ฎԅԧො׎඙֢ग़ӻ੒᨝҅ᘒJavaᕳ౯ժ൉׀ӞᔮڜጱAPI(ොဩ)׀౯ժ
݄඙̶֢ಅզࣁڡ਍Javaᵞݳጱ෸ײ౯ժๅग़ጱฎ਍ԟᬯԶAPI(ොဩ)ړڦฎՋԍ఺௏̶

![三歪教你学Java集合(1) 第5页插图](../assets/images/三歪教你学Java集合(1)_p5_1_45af3e1f.png)

![三歪教你学Java集合(1) 第5页插图](../assets/images/三歪教你学Java集合(1)_p5_2_e5eda945.png)

![三歪教你学Java集合(1) 第5页插图](../assets/images/三歪教你学Java集合(1)_p5_3_41546a53.png)

---

Qғ ੒JavaᵞݳጱAPIֵአํӞਧጱԧᥴԏݸ҅౯ժ੪ଫᧆ՗ᶎݻ੒᨝ጱ᥯ଶ݄ቘᥴਙ̶ԅՋԍտು᨝
ڊग़ӻളݗ҅զ݊ྯӻളݗጱํՋԍᇙ௔̶
A: ౯ժݢզ௛ᕮڊپӻଉአጱਫሿᔄ҅ᬯپӻଉአጱਫሿᔄ౯ժ஠ᶳᥝᎣ᭲ਙጱහഝᕮ຅ฎՋԍ҅Ջԍ
෸ײֵአᬯӻᔄ̶
 
ᵱᥝ਍ԟ޾ԧᥴጱහഝᕮ຅ғ

![三歪教你学Java集合(1) 第6页插图](../assets/images/三歪教你学Java集合(1)_p6_1_f77a066d.png)

![三歪教你学Java集合(1) 第6页插图](../assets/images/三歪教你学Java集合(1)_p6_2_154bfc75.png)

![三歪教你学Java集合(1) 第6页插图](../assets/images/三歪教你学Java集合(1)_p6_3_87c8230a.png)

---

کᬯ᯾҅౯ժᓌܔԧᥴݱӻਫሿᔄጱහഝᕮ຅զݸ҅౯ժݢᚆտᓌܔᦕ֘ӥᶎጱᕮᦞғ
ইຎฎᵞݳᔄࣳ҅ํList޾Set׀౯ժᭌೠ̶Listጱᇙᅩฎൊفํଧጱ҅زᔰฎݢ᯿॔ጱ̶Setጱᇙ
ᅩฎൊف෫ଧጱ҅زᔰӧݢ᯿॔ጱ̶ᛗԭᭌೠߺӻਫሿᔄ๶֢ԅ౯ժጱਂؙ਻࢏҅౯ժ੪஑፡ٍ֛
ጱଫአ࣋ว̶ฎ૶๕ݢ᯿॔ጱ੪஑አList҅ᭌೠListӥଉᥠጱৼᔄ̶ฎ૶๕ӧݢ᯿॔҅ᭌೠSetӥଉ
ᥠጱৼᔄ̶
ইຎฎKey-Value ࣳ҅ᮎ౯ժտᭌೠMap̶ইຎᥝכ೮ൊفᶲଧጱ҅౯ժݢզᭌೠ
LinkedHashMap҅ইຎӧᵱᥝڞᭌೠHashMap҅ইຎᥝഭଧڞᭌೠTreeMap̶
௛ԏғ਍ਠଉᥠਫሿᔄጱහഝᕮ຅ԏݸ֦҅੒ਙጱֵአ࣋ว੪ํӞӻႴ༩ጱᦊᎣԧ̶
1.3 ᵞݳᬰᴤӨᶎᦶ
 
ইຎ౯ժࣁٟդᎱጱ෸ײ౜஑ᭌೠՋԍ໏ጱᵞݳ֢ԅ౯ժጱ਻࢏҅ᮎ૪ᕪฎفᳪԧ̶֕ᥝᎣ᭲ጱฎ҅ই
ຎ݄ᶎᦶԏڹ֦҅౜ጱӧଫᧆݝํᬯԍ੝̶
ҁইຎᬮࣁڡ਍౲ᘏᵭचᏐጱݶ਍౯ୌᦓݢզ᪡ᬦᬯӞ᮱ړ҅ࣁᗑӤํݢᚆஉग़᥺ᦞ҅ྲইғ“ইຎ֦
JavaचᏐಎਫጱᦾ҅ᮎ֦զݸತૡ֢੪ӧఴԧ̶ࣁ਍JavaचᏐጱ෸ײӞਧᥝ಩चᏐ਍অ҅፡რᎱѺ”̶
֕౯ᦊԅ҅ᬯӞࣘฎୌᒈࣁํӞਧጱᖫᎱ/ᶱፓ౲ᘏฎ݄ತૡ֢ጱ෸ײ಍౮ᒈጱ҅Ӟӻڟفᳪ਍Java
ጱ҅੪ӧଫᧆ፡რᎱ҅ᬯஉ਻ฃ಩ᛔ૩ۏᭅԧ҂

![三歪教你学Java集合(1) 第7页插图](../assets/images/三歪教你学Java集合(1)_p7_1_3ce70964.png)

![三歪教你学Java集合(1) 第7页插图](../assets/images/三歪教你学Java集合(1)_p7_2_80cb1a30.png)

---

౯ጱᥡᅩฎғইຎڟفᳪ਍Java҅Ḓض֦ᥝ܈ړႴ༩Ꭳ᭲ԅՋԍᥝ਍ᬯӻ҅ᬯӻکବํՋԍአ҅አࣁߺ
Զࣈො҅զ݊ᆧఀଉአጱොဩ҅੪᪃ड़ԧ̶ܨ׎֦ᜰԧӷޮૢݦ෸ᳵ݄፡რᎱਫሿԧ҅ݢᚆ፡౜ԧ̶֕
ฎ֦҅ፘמ౯֦҅य़༷ሲտ஫ധ̶
 
Javaᵞݳฎᶎᦶጱ᯿ᅩ҅౯ࣁᶎᦶጱ෸ײپԒྯਹلݪ᮷տᳯᵞݳጱᳯ᷌҅՗चᏐکრᎱ҅ӞྍӞྍႮ
ف̶JavaᵞݳᶎᦶጱᎣᦩᅩ੪ӧᴴԭच๜ጱአဩԧ̶ݢᚆᶎᦶਥտᳯ֦ғ
HashMapጱහഝᕮ຅ฎՋԍҘ՜ฎெԍಘ਻ጱҘବ੶ํဌํአᕁἓ໅ҘݐKey Hash꧊ฎJDKრᎱ
ฎெԍਫሿጱҘԅՋԍᥝᬯ໏؉Ҙ
HashMapฎᕚᑕਞقጱހҘՋԍฎᕚᑕਞقҘํՋԍๅঅጱᥴ٬ොໜҘᮎᕚᑕਞقጱHashMapฎ
ெԍਫሿጱҘ
HashSetฎই֜ڣෙKeyฎ᯿॔ጱҘ
.....உग़உग़
௛ጱ๶᧔҅فᳪJavaᵞݳଚӧᵙ҅୭໑کବ౯ᦊԅ੪ฎӣկԪғ
ԧᥴԅՋԍᥝ਍ԟJavaᵞݳ
਍ԟJavaᵞݳጱݱӻളݗզ݊ଉአጱਫሿᔄአဩ
਍ԟଉአਫሿᔄጱහഝᕮ຅ฎՋԍ҅ᚆࣁٟդᎱጱ෸ײᭌೠӞӻݳᭇጱਫሿᔄᤰ᫹ᛔ૩ጱ੒᨝̶
 
ᵭचᏐفᳪӧᵱᥝᴅ᧛რᎱ҅ᶎᦶڹӞਧᥝࢧᶶ޾ᴅ᧛რᎱҁᬯฎᶎᦶ஠ᘍጱᎣᦩᅩ҂Ѻ

![三歪教你学Java集合(1) 第8页插图](../assets/images/三歪教你学Java集合(1)_p8_1_f4e927a6.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
ԫ̵Collection

![三歪教你学Java集合(1) 第9页插图](../assets/images/三歪教你学Java集合(1)_p9_1_b6d2079a.jpeg)

![三歪教你学Java集合(1) 第9页插图](../assets/images/三歪教你学Java集合(1)_p9_2_3c233a1a.jpeg)

![三歪教你学Java集合(1) 第9页插图](../assets/images/三歪教你学Java集合(1)_p9_3_49e3c417.png)

---

Ӟ̵ᵞݳ(Collection)Օᕨ
 
1.1ԅՋԍᵱᥝCollection
 
1. JavaฎӞᳪᶎݻ੒᨝ጱ᧍᥺҅੪عӧԧ॒ቘ੒᨝
2. ԅԧො׎඙֢ग़ӻ੒᨝҅ᮎԍ౯ժ੪஑಩ᬯग़ӻ੒᨝ਂؙ᩸๶
3. మᥝਂؙग़ӻ੒᨝(ݒᰁ),உ਻ฃ੪ᚆమکӞӻ਻࢏
4. ଉአጱ਻࢏౯ժᎣ᭲ํ-->StringBuffered,හᕟ(ᡱᆐํ੒᨝හᕟ҅֕ฎහᕟጱᳩଶฎӧݢݒጱѺ)
5. ಅզ҅Java੪ԅ౯ժ൉׀ԧᵞݳ(Collection)ӗ
1.2හᕟ޾ᵞݳጱ܄ڦ
 
ളӥ๶҅౯ժݢզ੒හᕟ޾ᵞݳጱ܄ڦ๶ړຉӞӥғ
හᕟ޾ᵞݳጱ܄ڦ:
1:ᳩଶጱ܄ڦ
හᕟጱᳩଶࢴਧ
ᵞݳጱᳩଶݢݒ
2:زᔰጱහഝᔄࣳ
හᕟݢզਂؙच๜හഝᔄࣳ,Ԟݢզਂؙ୚አᔄࣳ
ᵞݳݝᚆਂؙ୚አᔄࣳ(֦ਂؙጱฎᓌܔጱint҅ਙտᛔۖᤰᓟ౮Integer)
1.3Collectionጱኧ๶Өۑᚆ
 
Collectionጱኧ๶ғ
ᵞݳݢզਂؙग़ӻزᔰ,֕౯ժ੒ग़ӻزᔰԞํӧݶጱᵱ࿢
ग़ӻزᔰ,ӧᚆํፘݶጱ
ग़ӻزᔰ,ᚆड़ೲᆙ຤ӻᥢڞഭଧ
ᰒ੒ӧݶጱᵱ࿢ғjava੪൉׀ԧஉग़ᵞݳᔄ҅ग़ӻᵞݳᔄጱහഝᕮ຅ӧݶ̶֕ฎ҅ᕮ຅ӧ᯿ᥝ҅᯿
ᥝጱฎᚆड़ਂؙӳᥜ,ᚆड़ڣෙ,឴ݐ
಩ᵞݳو௔ጱٖ਻ӧෙஃӤ൉ݐ,๋ᕣ୵౮ᵞݳጱᖀಥ֛ᔮ---->Collection
Collectionጱय़ᛘᕮ຅֛ᔮฎᬯ໏ጱғ

---

֕ฎ҅Ӟᛱ౯ժᥝഩൎጱଚӧᵱᥝᮎԍग़҅ݝᵱᥝഩൎӞԶଉአጱᵞݳᔄ੪ᤈԧ̶ӥᶎ౯ࢻڊ๶ጱᮎ
Զғ
ེٚᔜٺғ

![三歪教你学Java集合(1) 第11页插图](../assets/images/三歪教你学Java集合(1)_p11_1_d2e0a981.jpeg)

![三歪教你学Java集合(1) 第11页插图](../assets/images/三歪教你学Java集合(1)_p11_2_56ff3a80.png)

---

CollectionጱचᏐۑᚆғ

![三歪教你学Java集合(1) 第12页插图](../assets/images/三歪教你学Java集合(1)_p12_1_9e5c67ec.png)

![三歪教你学Java集合(1) 第12页插图](../assets/images/三歪教你学Java集合(1)_p12_2_abe5d52b.png)

![三歪教你学Java集合(1) 第12页插图](../assets/images/三歪教你学Java集合(1)_p12_3_72345ac1.png)

---

ԫ̵ᬽդ࢏(Iterator)Օᕨ
 
౯ժݢզݎሿCollectionጱრᎱӾᖀಥԧIterable҅ํiterator()ᬯӻොဩ...
ᅩᬰ݄፡ԧӞӥ҅IterableฎӞӻളݗғ
ਙํiterator()ᬯӻොဩ҅ᬬࢧጱฎIterator
ٚ๶፡Ӟӥ҅IteratorԞฎӞӻളݗ҅ਙݝํӣӻොဩғ
hasNext()
next()
remove()

![三歪教你学Java集合(1) 第13页插图](../assets/images/三歪教你学Java集合(1)_p13_1_a15b24f6.png)

![三歪教你学Java集合(1) 第13页插图](../assets/images/三歪教你学Java集合(1)_p13_2_e50b7c11.png)

---

ݢฎ҅౯ժဌᚆತک੒ଫጱਫሿොဩ҅ݝᚆஃCollectionጱৼᔄӥತತԧ҅ԭฎ౯ժತکԧ---
>ArrayList(ᧆᔄݸᶎտ᧔)
ԭฎ҅౯ժࣁArrayListӥತکԧiteratorਫሿጱ᫝୽ғਙฎࣁArrayListզٖ᮱ᔄጱොୗਫሿጱѺଚӬ҅
՗რᎱݢᎣғIteratorਫᴬӤ੪ฎࣁ᭭ܲᵞݳ
ಅզ᧔ғ౯ժ᭭ܲᵞݳ(Collection)ጱزᔰ᮷ݢզֵአIterator҅ᛗԭਙጱٍ֛ਫሿฎզٖ᮱ᔄጱොୗ
ਫሿጱѺ

![三歪教你学Java集合(1) 第14页插图](../assets/images/三歪教你学Java集合(1)_p14_1_18717538.png)

![三歪教你学Java集合(1) 第14页插图](../assets/images/三歪教你学Java集合(1)_p14_2_a8c53031.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
ӣ̵ListᵞݳՕᕨ
 
՗Ӥᶎ૪ᕪݢզ፡کԧ҅CollectionԆᥝ਍ԟᵞݳጱᔄࣳӷᐿғSet޾List҅ᬯ᯾ԆᥝᦖᥴListѺ

![三歪教你学Java集合(1) 第15页插图](../assets/images/三歪教你学Java集合(1)_p15_1_3c233a1a.jpeg)

![三歪教你学Java集合(1) 第15页插图](../assets/images/三歪教你学Java集合(1)_p15_2_b445b576.png)

![三歪教你学Java集合(1) 第15页插图](../assets/images/三歪教你学Java集合(1)_p15_3_953b5bb8.jpeg)

---

౯ժ๶፡ӞӥListളݗጱොဩ҅ྲCollectionग़ԧӞᅩᅩғ
Listᵞݳጱᇙᅩ੪ฎғํଧ(ਂؙᶲଧ޾ݐڊᶲଧӞᛘ),ݢ᯿॔
CollectionᬬࢧጱฎIteratorᬽդ࢏ളݗ҅ᘒListӾ݈ํਙᛔ૩੒ଫጱਫሿ-->ListIteratorളݗ
ᧆളݗྲฦ᭗ጱIteratorളݗग़ԧپӻොဩғ
՗ොဩݷ੪ݢզᎣ᭲ғListIteratorݢզஃڹ᭭ܲ҅Ⴒےزᔰ҅ᦡᗝزᔰ
 
 
3.1Listᵞݳଉአৼᔄ
 
Listᵞݳଉአጱৼᔄํӣӻғ
ArrayList
ବ੶හഝᕮ຅ฎහᕟ̶ᕚᑕӧਞق
LinkedList
ବ੶හഝᕮ຅ฎ᱾ᤒ̶ᕚᑕӧਞق
Vector
ବ੶හഝᕮ຅ฎහᕟ̶ᕚᑕਞق
ሿࣁᎣ᭲ํӣӻଉአጱᵞݳᔄܨݢ҅ݸᶎտ୏ෛጱ෈ᒍ๶ᦖᥴጱӗ

![三歪教你学Java集合(1) 第16页插图](../assets/images/三歪教你学Java集合(1)_p16_1_ca41be28.png)

![三歪教你学Java集合(1) 第16页插图](../assets/images/三歪教你学Java集合(1)_p16_2_c3e56e3c.png)

---

ࢥ̵SetᵞݳՕᕨ
 
՗Setᵞݳጱොဩ౯ժݢզ፡کғොဩဌํྲCollectionᥝग़
Setᵞݳጱᇙᅩฎғزᔰӧݢ᯿॔
4.1Setᵞݳଉአৼᔄ
 
HashSetᵞݳ
A:ବ੶හഝᕮ຅ฎߢ૶ᤒ(ฎӞӻزᔰԅ᱾ᤒጱහᕟ) 
TreeSetᵞݳ
A:ବ੶හഝᕮ຅ฎᕁἓ໅(ฎӞӻᛔଘᤍጱԫ݉໅)
B:כᦤزᔰጱഭଧොୗ
LinkedHashSetᵞݳ       
A:ғବ੶හഝᕮ຅ኧߢ૶ᤒ޾᱾ᤒᕟ౮̶

![三歪教你学Java集合(1) 第17页插图](../assets/images/三歪教你学Java集合(1)_p17_1_8af84281.png)

![三歪教你学Java集合(1) 第17页插图](../assets/images/三歪教你学Java集合(1)_p17_2_1135866f.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
ӣ̵Listᵞݳ
 
ሿࣁᬯᓤԆᥝᦖListᵞݳጱӣӻৼᔄғ
ArrayList
ବ੶හഝᕮ຅ฎහᕟ̶ᕚᑕӧਞق
LinkedList
ବ੶හഝᕮ຅ฎ᱾ᤒ̶ᕚᑕӧਞق
Vector
ବ੶හഝᕮ຅ฎහᕟ̶ᕚᑕਞق
ᬯᓤԆᥝ๶፡፡ਙժྲ᫾᯿ᥝጱොဩฎই֜ਫሿጱ҅ᵱᥝဳ఺ԶՋԍ๋҅ݸྲ᫾Ӟӥߺӻ෸ײአߺӻӗ

![三歪教你学Java集合(1) 第18页插图](../assets/images/三歪教你学Java集合(1)_p18_1_4fc0f18c.png)

![三歪教你学Java集合(1) 第18页插图](../assets/images/三歪教你学Java集合(1)_p18_2_3c233a1a.jpeg)

---

Ӟ̵ArrayListᥴຉ
 
Ḓض҅౯ժ๶ᦖᥴጱฎArrayListᵞݳ҅ਙฎ౯ժአ஑ᶋଉᶋଉग़ጱӞӻᵞݳ~
Ḓض҅౯ժ๶፡ӞӥArrayListጱં௔ғ

![三歪教你学Java集合(1) 第19页插图](../assets/images/三歪教你学Java集合(1)_p19_1_ecd91010.png)

![三歪教你学Java集合(1) 第19页插图](../assets/images/三歪教你学Java集合(1)_p19_2_93312951.png)

---

໑ഝӤᶎ౯ժݢզႴศጱݎሿғArrayListବ੶ٌਫ੪ฎӞӻහᕟ҅ArrayListӾํಘ਻ᬯԍӞӻ༷ஷ҅
ྋࢩԅਙಘ਻҅ಅզਙᚆड़ਫሿ“ۖா”ीᳩ
1.1຅᭜ොဩ
 
౯ժ๶፡፡຅᭜ොဩ๶ܦᦤ౯ժӤᶎ᧔஑੒ӧ੒ғ

![三歪教你学Java集合(1) 第20页插图](../assets/images/三歪教你学Java集合(1)_p20_1_64b78b8b.png)

---

1.2Addොဩ
 
addොဩݢզ᧔ฎArrayListྲ᫾᯿ᥝጱොဩԧ҅౯ժ๶௛ᥦӞӥғ

![三歪教你学Java集合(1) 第21页插图](../assets/images/三歪教你学Java集合(1)_p21_1_83708b03.png)

---

1.2.1add(E e)
 
ྍṈғ
༄ັฎވᵱᥝಘ਻
ൊفزᔰ
Ḓض҅౯ժ๶፡፡ᬯӻොဩғ
ᧆොဩஉᎨ҅౯ժݢզ໑ഝොဩݷ੪ሖک՜ฎଗԧՋԍғ
Ꮯᦊlist਻ᰁ҅੤ᦶ਻ᰁے1҅፡፡ํ෫஠ᥝ
Ⴒےزᔰ
ളӥ๶౯ժ๶፡፡ᬯӻੜ਻ᰁ(+1)ฎވჿ᪃౯ժጱᵱ࿢ғ
    public boolean add(E e) {
        ensureCapacityInternal(size + 1);  // Increments modCount!!
        elementData[size++] = e;
        return true;
    }

![三歪教你学Java集合(1) 第22页插图](../assets/images/三歪教你学Java集合(1)_p22_1_42b394ea.png)

![三歪教你学Java集合(1) 第22页插图](../assets/images/三歪教你学Java集合(1)_p22_2_eb7272fe.png)

---

ᵋݸ᧣አensureExplicitCapacity() ๶ᏟਧกᏟጱ਻ᰁ҅౯ժԞ๶፡፡ᬯӻොဩฎெԍਫሿጱғ
ಅզ҅ളӥ๶፡፡grow() ฎெԍਫሿጱ~
ᬰ݄፡copyOf() ොဩғ
کፓڹԅྊ҅౯ժ੪ݢզᎣ᭲add(E e) ጱच๜ਫሿԧғ
Ḓض݄༄ັӞӥහᕟጱ਻ᰁฎވ᪃ड़
᪃ड़ғፗളႲے
ӧ᪃ड़ғಘ਻
ಘ਻کܻ๶ጱ1.5׭
ᒫӞེಘ਻ݸ҅ইຎ਻ᰁᬮฎੜԭminCapacity҅੪ਖ਼਻ᰁಘ꧌ԅminCapacity̶

![三歪教你学Java集合(1) 第23页插图](../assets/images/三歪教你学Java集合(1)_p23_1_e52bde1d.png)

![三歪教你学Java集合(1) 第23页插图](../assets/images/三歪教你学Java集合(1)_p23_2_85512291.png)

![三歪教你学Java集合(1) 第23页插图](../assets/images/三歪教你学Java集合(1)_p23_3_f218c561.png)

---

1.2.2add(int index, E element)
 
ྍṈғ
༄ັ᥯ຽ
ᑮᳵ༄ັ҅ইຎํᵱᥝᬰᤈಘ਻
ൊفزᔰ
౯ժ๶፡፡ൊفጱਫሿғ
౯ժݎሿ҅Өಘ਻ፘىArrayListጱaddොဩବ੶ٌਫ᮷ฎarraycopy() ๶ਫሿጱ
፡ک arraycopy() ҅౯ժݢզݎሿғᧆොဩฎኧC/C++๶ᖫٟጱ҅ଚӧฎኧJavaਫሿғ
௛ጱ๶᧔ғ arraycopy() ᬮฎྲ᫾ݢᶌṛපጱӞӻොဩ̶
 
1.3 getොဩ
 
༄ັ᥯ຽ
ᬬࢧزᔰ

![三歪教你学Java集合(1) 第24页插图](../assets/images/三歪教你学Java集合(1)_p24_1_2c3c2bd7.png)

![三歪教你学Java集合(1) 第24页插图](../assets/images/三歪教你学Java集合(1)_p24_2_f544b40b.png)

![三歪教你学Java集合(1) 第24页插图](../assets/images/三歪教你学Java集合(1)_p24_3_480f8f11.png)

---

1.4 setොဩ
 
ྍṈғ
༄ັ᥯ຽ
๊դزᔰ
ᬬࢧ෯꧊
1.5removeොဩ
 
ྍṈғ
༄ັ᥯ຽ
ڢᴻزᔰ
ᦇᓒڊᵱᥝᑏۖጱӻහ҅ଚᑏۖ
ᦡᗝԅnull҅ᦏGcࢧත
// ༄ັ᥯ຽ
private void rangeCheck(int index) {
  if (index >= size)
    throw new IndexOutOfBoundsException(outOfBoundsMsg(index));
}
 
// ᬬࢧزᔰ
E elementData(int index) {
  return (E) elementData[index];
}

![三歪教你学Java集合(1) 第25页插图](../assets/images/三歪教你学Java集合(1)_p25_1_6296c213.png)

---

1.6ᕡᜓٚ᧔ก
 
ArrayListฎचԭۖாහᕟਫሿጱ҅ࣁीڢ෸ײ҅ᵱᥝහᕟጱ೩ᨬ॔ګ̶
ArrayListጱἕᦊڡত۸਻ᰁฎ10҅ྯེಘ਻෸ײीےܻض਻ᰁጱӞ܎҅Ԟ੪ฎݒԅܻ๶ጱ1.5׭
ڢᴻزᔰ෸ӧտٺ੝਻ᰁ҅ᝑ૶๕ٺ੝਻ᰁڞ᧣አtrimToSize()
ਙӧฎᕚᑕਞقጱ̶ਙᚆਂනnull꧊̶

![三歪教你学Java集合(1) 第26页插图](../assets/images/三歪教你学Java集合(1)_p26_1_29b0c967.png)

![三歪教你学Java集合(1) 第26页插图](../assets/images/三歪教你学Java集合(1)_p26_2_470d85bf.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
ԫ̵VectorӨArrayList܄ڦ
 
Vectorฎjdk1.2ጱᔄԧ҅ྲ᫾ᘌ෯ጱӞӻᵞݳᔄ̶

![三歪教你学Java集合(1) 第27页插图](../assets/images/三歪教你学Java集合(1)_p27_1_b6d2079a.jpeg)

![三歪教你学Java集合(1) 第27页插图](../assets/images/三歪教你学Java集合(1)_p27_2_3c233a1a.jpeg)

---

Vectorବ੶Ԟฎහᕟ҅ӨArrayList๋य़ጱ܄ڦ੪ฎғݶྍ(ᕚᑕਞق)
Vectorฎݶྍጱ҅౯ժݢզ՗ොဩӤ੪ݢզ፡஑ڊ๶~
ࣁᥝ࿢ᶋݶྍጱఘ٭ӥ҅౯ժӞᛱ᮷ฎֵአArrayList๶๊դVectorጱԧ~
ইຎమᥝArrayListਫሿݶྍ҅ݢզֵአCollectionsጱොဩғ List list = 
Collections.synchronizedList(new ArrayList(...)); ҅੪ݢզਫሿݶྍԧ~
ᬮํݚӞӻ܄ڦғ
ArrayListࣁବ੶හᕟӧड़አ෸ࣁܻ๶ጱचᏐӤಘ઀0.5׭҅Vectorฎಘ઀1׭̶̵

![三歪教你学Java集合(1) 第28页插图](../assets/images/三歪教你学Java集合(1)_p28_1_721c4209.png)

![三歪教你学Java集合(1) 第28页插图](../assets/images/三歪教你学Java集合(1)_p28_2_f94cd4f3.png)

---

ӣ̵LinkedListᥴຉ
 
LinkedListବ੶ฎ݌ݻ᱾ᤒ~ইຎ੒ԭ᱾ᤒӧᆧఀጱݶ਍ݢض፡፡౯ጱܔݻ᱾ᤒ(݌ݻ᱾ᤒጱᕞԟ౯ᬮဌ
؉)̓Javaਫሿܔݻ᱾ᤒ̈́
ቘᥴԧܔݻ᱾ᤒ҅݌ݻ᱾ᤒԞ੪ӧᵙԧ̶

![三歪教你学Java集合(1) 第29页插图](../assets/images/三歪教你学Java集合(1)_p29_1_1c422ad4.png)

![三歪教你学Java集合(1) 第29页插图](../assets/images/三歪教你学Java集合(1)_p29_2_2c99b036.png)

![三歪教你学Java集合(1) 第29页插图](../assets/images/三歪教你学Java集合(1)_p29_3_dc4d17cc.png)

---

՗ᕮ຅Ӥ҅౯ժᬮ፡کԧLinkedListਫሿԧDequeളݗ҅ࢩྌ҅౯ժݢզ඙֢LinkedList؟඙֢ᴚڜ
޾຾Ӟ໏~

![三歪教你学Java集合(1) 第30页插图](../assets/images/三歪教你学Java集合(1)_p30_1_4eea60eb.png)

---

LinkedListݒᰁ੪ᬯԍپӻ҅ࢩԅ౯ժ඙֢ܔݻ᱾ᤒጱ෸ײԞݎሿԧғํԧ१ᕮᅩٌ҅՜ጱහഝ౯ժ᮷
ݢզ឴ݐ஑کԧ̶(݌ݻ᱾ᤒԞݶቘ)

![三歪教你学Java集合(1) 第31页插图](../assets/images/三歪教你学Java集合(1)_p31_1_968e6016.png)

---

3.1຅᭜ොဩ
 
LinkedListጱ຅᭜ොဩํӷӻғ
3.2addොဩ
 
ইຎ؉ᬦ᱾ᤒጱᕞԟ҅੒ԭӥᶎጱդᎱଚӧᴲኞጱ~
addොဩਫᴬӤ੪ฎஃ᱾ᤒ๋ݸႲےزᔰ
    public boolean add(E e) {
        linkLast(e);
        return true;
    }
 
    void linkLast(E e) {
        final Node<E> l = last;
        final Node<E> newNode = new Node<>(l, e, null);
        last = newNode;

![三歪教你学Java集合(1) 第32页插图](../assets/images/三歪教你学Java集合(1)_p32_1_a8e7bd6e.png)

![三歪教你学Java集合(1) 第32页插图](../assets/images/三歪教你学Java集合(1)_p32_2_28a2b1f5.png)

---

3.3removeොဩ
 
        if (l == null)
            first = newNode;
        else
            l.next = newNode;
        size++;
        modCount++;
    }

![三歪教你学Java集合(1) 第33页插图](../assets/images/三歪教你学Java集合(1)_p33_1_920992c2.png)

---

ਫᴬӤ੪ฎӥᶎᮎӻࢶጱ඙֢ғ
3.4getොဩ
 
ݢզ፡کgetොဩਫሿ੪ӷྦྷդᎱғ

![三歪教你学Java集合(1) 第34页插图](../assets/images/三歪教你学Java集合(1)_p34_1_43e15c65.jpeg)

![三歪教你学Java集合(1) 第34页插图](../assets/images/三歪教你学Java集合(1)_p34_2_01ff6bce.png)

---

౯ժᬰ݄፡Ӟӥٍ֛ጱਫሿฎெԍ໏ጱғ
3.5setොဩ
 
 
setොဩ޾getොဩٌਫ૧ӧग़҅໑ഝӥຽ๶ڣෙฎ՗१᭭ܲᬮฎ՗ੲ᭭ܲ
 
ࢥ̵Listᵞݳ௛ᕮ
 
ٌਫᵞݳጱრᎱ፡᩸๶ଚӧฎஉࢯᵙ᭬҅کᳯ᷌ݢզᘉӞᘉ҅ଫᧆฎᚆड़፡౜ጱ~
    public E get(int index) {
        checkElementIndex(index);
        return node(index).item;
    }
    public E set(int index, E element) {
        checkElementIndex(index);
        Node<E> x = node(index);
        E oldVal = x.item;
        x.item = element;
        return oldVal;
    }

![三歪教你学Java集合(1) 第35页插图](../assets/images/三歪教你学Java集合(1)_p35_1_51c9fedd.png)

---

ArrayList̵LinkedList̵Vectorᓒฎࣁᶎᦶ᷌Ӿྲ᫾ଉᥠጱጱᎣᦩᅩԧ̶ӥᶎ౯੪๶؉Ӟӻᓌܔጱ௛
ᕮғ
ArrayListғ
ବ੶ਫሿฎහᕟ
ArrayListጱἕᦊڡত۸਻ᰁฎ10҅ྯེಘ਻෸ײीےܻض਻ᰁጱӞ܎҅Ԟ੪ฎݒԅܻ๶ጱ1.5׭
ࣁीڢ෸ײ҅ᵱᥝහᕟጱ೩ᨬ॔ګ(navite ොဩኧC/C++ਫሿ)
LinkedListғ
ବ੶ਫሿฎ݌ݻ᱾ᤒ[݌ݻ᱾ᤒො׎ਫሿஃڹ᭭ܲ]
Vectorғ
ବ੶ฎහᕟ҅ሿࣁ૪੝አ҅ᤩArrayList๊դܻ҅ࢩํӷӻғ
Vectorಅํොဩ᮷ฎݶྍ҅ํ௔ᚆഖ०̶
Vectorڡতlengthฎ10 ᩻ᬦlength෸ զ100%ྲሲीᳩ҅ፘྲԭArrayListๅग़ၾᘙٖਂ̶
௛ጱ๶᧔ғັᧃग़አArrayList҅ीڢग़አLinkedList̶
ArrayListीڢౌӧฎᕷ੒ጱ(ࣁහᰁय़ጱఘ٭ӥ҅૪ၥᦶ)ғ
ইຎीےزᔰӞፗฎֵአadd() (ीےک๛ੲ)ጱᦾ҅ᮎฎArrayListᥝள
Ӟፗڢᴻ๛ੲጱزᔰԞฎArrayListᥝள̓ӧአ॔ګᑏ֖ۖᗝ̈́
ᛗԭইຎڢᴻጱฎӾᳵጱ֖ᗝጱᦾ҅ᬮฎArrayListᥝளѺ
֕Ӟᛱ๶᧔ғीڢग़ᬮฎአLinkedList҅ࢩԅӤᶎጱఘ٭ฎຄᒒጱ~

![三歪教你学Java集合(1) 第36页插图](../assets/images/三歪教你学Java集合(1)_p36_1_a6d9076a.jpeg)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
ࢥ̵Mapᵞݳ
 
 
Ӟ̵MapՕᕨ
 
1.1ԅՋԍᵱᥝMap
 
ڹᶎ౯ժ਍ԟጱCollectionݞ؉ᵞݳ҅ਙݢզள᭛ັತሿํጱزᔰ̶
ᘒMapࣁ̽Core Java̾Ӿᑍԏԅ-->ฉ੘..
ฉ੘ጱཛྷࣳࢶฎᬯ໏ጱғ

![三歪教你学Java集合(1) 第37页插图](../assets/images/三歪教你学Java集合(1)_p37_1_3c233a1a.jpeg)

![三歪教你学Java集合(1) 第37页插图](../assets/images/三歪教你学Java集合(1)_p37_2_6852a83e.png)

---

ᮎԅՋԍ౯ժᵱᥝᬯᐿහഝਂؙᕮ຅ޫҘҘҘԈӻֺৼ
֢ԅ਍ኞ๶᧔҅౯ժฎ໑ഝ਍ݩ๶܄ړӧݶጱ਍ኞ̶ݝᥝ౯ժᎣ᭲਍ݩ҅੪ݢզ឴ݐ੒ଫጱ਍ኞמ
௳̶ᬯ੪ฎMapฉ੘ጱ֢አѺ
ኞၚӾᬮํஉग़ᬯ໏ጱֺৼғݝᥝ֦ഫڊ᫝ղᦤ(key)҅ᮎ੪ݢզᦤกฎ֦ᛔ૩(value)
1.2MapӨCollectionጱ܄ڦ
 
1.3Mapጱۑᚆ
 
ӥᶎ౯ժ๶፡፡MapጱრᎱғ
ᓌܔଉአጱMapۑᚆํᬯԍӞԶғ

![三歪教你学Java集合(1) 第38页插图](../assets/images/三歪教你学Java集合(1)_p38_1_6bdc7fb1.png)

![三歪教你学Java集合(1) 第38页插图](../assets/images/三歪教你学Java集合(1)_p38_2_57749f39.png)

---

ӥᶎአᕁᜋ໛໛ࢻ֘ጱ੪ฎMap꧊஑ىဳጱৼᔄғ
ԫ̵වڜᤒՕᕨ
 
෫ᦞฎSetᬮฎMap҅౯ժտݎሿ᮷տํ੒ଫጱ-->HashSet,HashMap
Ḓض౯ժԞض஑ࢧᶶӞӥහഝ޾᱾ᤒғ
᱾ᤒ޾හᕟ᮷ݢզೲᆙՈժጱ఺ౄ๶ഭڜزᔰጱེଧ҅՜ժݢզ᧔ฎํଧጱ(ਂؙጱᶲଧ޾ݐڊጱ
ᶲଧฎӞᛘጱ)
֕ݶ෸҅ᬯտଃ๶ᗌᅩғమᥝ឴ݐ຤ӻزᔰ҅੪ᥝᦢᳯಅํጱزᔰ҅ፗکತکԅྊ̶
ᬯտᦏ౯ժၾᘙஉग़ጱ෸ᳵࣁ᯾ᬟ҅᭭ܲᦢᳯزᔰ~

![三歪教你学Java集合(1) 第39页插图](../assets/images/三歪教你学Java集合(1)_p39_1_60fb4a7a.png)

![三歪教你学Java集合(1) 第39页插图](../assets/images/三歪教你学Java集合(1)_p39_2_79e095cf.png)

---

ᘒᬮํݚक़ጱӞԶਂؙᕮ຅ғӧࣁ఺زᔰጱᶲଧ҅ᚆड़ள᭛ጱັತزᔰጱහഝ
ٌӾ੪ํӞᐿᶋଉଉᥠጱғවڜᤒ
2.1වڜᤒૡ֢ܻቘ
 
වڜᤒԅྯӻ੒᨝ᦇᓒڊӞӻෆහ҅ᑍԅවڜᎱ̶໑ഝᬯԶᦇᓒڊ๶ጱෆහ(වڜᎱ)כਂࣁ੒ଫጱ֖ᗝ
ӤѺ
ࣁJavaӾ҅වڜᤒአጱฎ᱾ᤒහᕟਫሿጱ҅ྯӻڜᤒᑍԏԅ໲̶̓ԏڹԞٟᬦ໲ഭଧ੪ᬯԍᓌܔ҅ݢզ
ࢧᶶࢧᶶ̈́

---

Ӟӻ໲Ӥݢᚆտ᭬کᤩܛአጱఘ٭(hashCodeවڜᎱፘݶ҅੪ਂؙࣁݶӞӻ֖ᗝӤ)҅ᬯᐿఘ٭ฎ෫ဩ
᭿عጱ҅ᬯᐿሿ᨝ᑍԏԅғවڜ٫ᑱ
ྌ෸ᵱᥝአᧆ੒᨝Ө໲Ӥጱ੒᨝ᬰᤈྲ᫾҅፡፡ᧆ੒᨝ฎވਂࣁ໲ৼӤԧ~ইຎਂࣁ҅੪ӧႲے
ԧ҅ইຎӧਂࣁڞႲےک໲ৼӤ
୮ᆐԧ҅ইຎhashcodeڍහᦡᦇ஑᪃ड़অ҅໲ጱහፓԞ᪃ड़҅ᬯᐿྲ᫾ฎஉ੝ጱ~
ࣁJDK1.8Ӿ҅໲ჿ෸տ՗᱾ᤒݒ౮ଘᤍԫ݉໅

![三歪教你学Java集合(1) 第41页插图](../assets/images/三歪教你学Java集合(1)_p41_1_7526dace.jpeg)

---

ইຎවڜᤒॡჿ҅ฎᵱᥝ੒වڜᤒٚවڜ҅ڠୌӞӻ໲හๅग़ጱවڜᤒ҅ଚਖ਼ܻํጱزᔰൊفکෛᤒ
Ӿ҅Ӷ୒ܻ๶ጱᤒ~
ᤰऴࢩৼ(load factor)٬ਧԧ֜෸੒වڜᤒٚවڜ~
ᤰऴࢩৼἕᦊԅ0.75҅ইຎᤒӾ᩻ᬦԧ75%ጱ֖ᗝ૪ᕪऴفԧزᔰ҅ᮎԍᬯӻᤒ੪տአ݌׭ጱ໲හ
ᛔۖᬰᤈٚවڜ
୮ᆐԧ҅ ࣁݸᶎᴅ᧛რᎱጱ෸ײտᖀᖅ᧔กጱ҅ሿࣁᓌܔԧᥴӞӥܨݢ~
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
ӣ̵ᕁἓ໅Օᕨ
 
ӤᶎවڜᤒӾ૪ᕪ൉ᬦԧғইຎ໲හჿጱ෸ײ҅JDK8ฎਖ਼᱾ᤒ᫨౮ᕁἓ໅ጱ~̶ଚӬ҅౯ժጱTreeSet̵
TreeMapବ੶᮷ฎᕁἓ໅๶ਫሿጱ̶
ಅզ҅ࣁᬯ᯾਍ԟӞူᕁἓ໅کବฎࠨሻ఺̶
ࣁ๚਍ԟԏڹ҅౯ժݢᚆฎލᬦᕁἓ໅ᬯԍӞӻහഝᕮ຅ᔄࣳጱ҅ᬮํٌ՜ՋԍB/B+໅ᒵᒵ҅ݍྋฎྲ
᫾॔๥ጱහഝᕮ຅ԧ~~~
ݱᐿଉᥠጱ໅ጱአ᭔ғ

![三歪教你学Java集合(1) 第42页插图](../assets/images/三歪教你学Java集合(1)_p42_1_5d4df7d4.png)

![三歪教你学Java集合(1) 第42页插图](../assets/images/三歪教你学Java集合(1)_p42_2_3c233a1a.jpeg)

---

3.1ࢧᶶԫ݉ັತ໅
 
Ḓض౯ժ๶ࢧᶶӞӥғڥአԫ݉ັತ໅ጱᇙ௔҅౯ժӞᛱ๶᧔ݢզஉளࣈັತڊ੒ଫጱزᔰ̶
ݢฎԫ݉ັತ໅Ԟํӻֺ(๋ࣕ)ጱఘ٭(ᕚ௔)ғ
Ӥᶎᒧݳԫ݉໅ጱᇙ௔҅֕ฎਙฎᕚ௔ጱ҅ਠقဌ໅ጱአ॒~
໅ฎᥝ“࣐ᤍ”಍ᚆਖ਼ਙጱսᅩ઀ᐏڊ๶ጱ~҅ྲইӥᶎᬯᐿғ

![三歪教你学Java集合(1) 第43页插图](../assets/images/三歪教你学Java集合(1)_p43_1_377f8a2b.png)

![三歪教你学Java集合(1) 第43页插图](../assets/images/三歪教你学Java集合(1)_p43_2_82912b53.png)

---

ࢩྌ҅੪ํԧଘᤍ໅ᬯԍӞӻ༷ஷ~ᕁἓ໅੪ฎӞᐿଘᤍ໅҅ਙݢզכᦤԫ݉໅च๜ᒧݳᎩᎩᙪᙪ(࣐ᤍ)
ጱᕮ຅
3.2Ꭳෛ2-3໅
 
ᦖکԧଘᤍ໅੪ӧ஑ӧ᧔๋चᏐጱ2-3໅҅2-3໅ᳩጱฎᬯӻ໏ৼғ
ࣁԫ݉ັತ໅Ӥ҅౯ժൊفᜓᅩጱᬦᑕฎᬯ໏ጱғੜԭᜓᅩ꧊ஃݦᖀᖅӨૢৼᜓᅩྲ҅य़ԭڞᖀᖅӨݦ
ৼᜓᅩྲ҅ፗک຤ᜓᅩૢ౲ݦৼᜓᅩԅᑮ҅಩꧊ൊفᬰ̶݄ᬯ໏෫ဩ᭿ع؇ݻᳯ᷌
ᘒ2-3໅ӧӞ໏ғਙൊفጱ෸ײݢզכ೮໅ጱଘᤍѺ
ࣁ2-3໅ൊفጱ෸ݢզᓌܔ௛ᕮԅӷӻ඙֢ғ
ݳଚ2-ᜓᅩԅ3-ᜓᅩ҅ಘ꧌ਖ਼3-ᜓᅩಘ꧌ԅӞӻ4-ᜓᅩ
ړᥴ4-ᜓᅩԅ3-ᜓᅩ҅ᜓᅩ3-ᜓᅩԅ2-ᜓᅩ
........ᛗֵ஑໅ଘᤍ~
ݳଚړᥴጱ඙֢ᬮฎྲ᫾॔๥ጱ҅ᥝړঅپᐿఘ٭҅դᎱᰁஉय़~ᬯ᯾౯੪ӧՕᕨԧ҅ࢩԅᥝ਍᩸๶ฎ
Ӟय़ञጱ҅உἋᅸ~
3.3՗2-3໅کᕁἓ໅
 
ኧԭ2-3໅ԅԧכ೮ଘᤍ௔҅ࣁᖌಷጱ෸ײฎᵱᥝय़ᰁጱᜓᅩԻഘጱѺᬯԶݒഘࣁਫᴬդᎱӾฎஉ॔๥
ጱ҅य़֬ժࣁ2-3໅ጱቘᦞचᏐӤݎกԧᕁἓ໅(2-3-4໅Ԟฎݶ໏ጱ᭲ቘ҅ݝฎ2-3໅ฎ๋ᓌܔጱӞᐿఘ
٭҅ಅզ౯੪ӧ᧔2-3-4໅ԧ)̶

![三歪教你学Java集合(1) 第44页插图](../assets/images/三歪教你学Java集合(1)_p44_1_a52856cb.png)

![三歪教你学Java集合(1) 第44页插图](../assets/images/三歪教你学Java集合(1)_p44_2_a946f633.png)

---

ᕁἓ໅ฎ੒2-3ັತ໅ጱදᬰ҅ਙᚆአӞᐿᕹӞጱොୗਠ౮ಅํݒഘ̶
ᕁἓ໅ฎӞᐿଘᤍԫ݉໅,ࢩྌਙဌํ3-ᜓᅩ̶ᮎᕁἓ໅ฎெԍਖ਼3-ᜓᅩ๶දᬰ౮ق᮷ฎԫ݉໅ޫҘ
ᕁἓ໅੪ਁᶎӤጱ఺௏҅ํᕁᜋጱᜓᅩ҅ํἓᜋጱᜓᅩғ
౯ժݢզਖ਼ᕁᜋᜓᅩጱૢ᱾ളኮଘ፡፡ғ
Ӟَ᷋ࣳጱԫ݉໅ғ

![三歪教你学Java集合(1) 第45页插图](../assets/images/三歪教你学Java集合(1)_p45_1_6d6a26ed.png)

![三歪教你学Java集合(1) 第45页插图](../assets/images/三歪教你学Java集合(1)_p45_2_02980305.png)

---

ਖ਼ᕁᜋᜓᅩጱૢ᱾ളኮଘԏݸғ஑ک2-3ଘᤍ໅:
3.4ᕁἓ໅चᏐᎣᦩ
 
ڹᶎ૪ᕪ᧔ԧ҅ᕁἓ໅ฎࣁ2-3ጱचᏐӤਫሿጱӞᐿ໅҅ਙᚆड़አᕹӞጱොୗਠ౮ಅํݒഘ̶உঅቘ
ᥴғᕁἓ໅Ԟฎଘᤍ໅ጱӞᐿ҅ࣁൊفزᔰጱ෸ײਙԞ஑כ೮໅ጱଘᤍ҅ᮎᕁἓ໅ฎզՋԍጱොୗ๶כ
೮໅ጱଘᤍጱޫҘ
ᕁἓ໅አጱฎԞฎӷᐿොୗ๶๊դ2-3໅ӧෙጱᜓᅩԻഘ඙֢ғ
෤᫨ғᶲ෸ᰒ෤᫨޾ᭋ෸ᰒ෤᫨
ݍᜋғԻഘᕁἓጱ᷏ᜋ
ᬯӻӷӻਫሿྲ2-3໅Իഘጱᜓᅩ(ݳଚ҅ړᥴ)ᥝො׎ӞԶ
 
ᕁἓ໅ԅԧכ೮ଘᤍ҅ᬮํګਧӞԶᕅ๳҅᭽ਝᬯԶᕅ๳ጱ಍ᚆݞ؉ᕁἓ໅ғ
1. ᕁἓ໅ฎԫ݉൤ᔱ໅̶
2. ໑ᜓᅩฎἓᜋ̶

![三歪教你学Java集合(1) 第46页插图](../assets/images/三歪教你学Java集合(1)_p46_1_2e67a8de.png)

![三歪教你学Java集合(1) 第46页插图](../assets/images/三歪教你学Java集合(1)_p46_2_da13d83b.png)

---

3. ྯӻݨৼᜓᅩ᮷ฎἓᜋጱᑮᜓᅩҁNILᜓᅩ҂̶
4. ྯӻᕁᜋᜓᅩጱӷӻৼᜓᅩ᮷ฎἓᜋ̶(՗ྯӻݨৼک໑ጱಅํ᪠ஆӤӧᚆํӷӻᬳᖅጱᕁᜋᜓᅩ)
5. ՗ձӞᜓᅩکٌྯӻݨৼጱಅํ᪠ஆ᮷۱ތፘݶහፓጱἓᜋᜓᅩ(ྯӞ๵໅᱾Ӥጱἓᜋᜓᅩහᰁ
ҁᑍԏԅ“ἓṛ”҂஠ᶳፘᒵ)̶
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
Բ̵HashMap
 
Ӟ̵HashMapڽຉ
 
Ḓض፡፡HashMapጱᶮ᮱ဳ᯽᧔ԧԶՋԍғ

![三歪教你学Java集合(1) 第47页插图](../assets/images/三歪教你学Java集合(1)_p47_1_3c233a1a.jpeg)

![三歪教你学Java集合(1) 第47页插图](../assets/images/三歪教你学Java集合(1)_p47_2_a6d9076a.jpeg)

![三歪教你学Java集合(1) 第47页插图](../assets/images/三歪教你学Java集合(1)_p47_3_b950d35d.png)

---

ٚ๶፡፡HashMapጱᔄᖀಥࢶғ

![三歪教你学Java集合(1) 第48页插图](../assets/images/三歪教你学Java集合(1)_p48_1_b950d35d.png)

---

ӥᶎ౯ժ๶፡ӞӥHashMapጱં௔ғ
౮ާં௔ํᬯԍپӻғ

![三歪教你学Java集合(1) 第49页插图](../assets/images/三歪教你学Java集合(1)_p49_1_186f4946.png)

![三歪教你学Java集合(1) 第49页插图](../assets/images/三歪教你学Java集合(1)_p49_2_ea2f2429.jpeg)

---

ٚ๶፡ӞӥhashMapጱӞӻٖ᮱ᔄNodeғ
౯ժᎣ᭲Hashጱବ੶ฎවڜᤒ҅ᘒࣁJavaӾවڜᤒጱਫሿฎ᭗ᬦහᕟ+᱾ᤒጱ~
ٚ๶ᓌܔ፡፡putොဩ੪ݢզܦᦤ౯ժጱ᧔ဩԧғහᕟ+᱾ᤒ-->වڜᤒ
౯ժݢզᓌܔ௛ᕮڊHashMapғ
෫ଧ҅꧋ᦜԅnull҅ᶋݶྍ
ବ੶ኧවڜᤒ(ߢ૶ᤒ)ਫሿ
ڡত਻ᰁ޾ᤰ᫹ࢩৼ੒HashMap୽ߥꂁय़ጱ҅ᦡᗝੜԧӧঅ҅ᦡᗝय़ԧԞӧঅ
1.1HashMap຅᭜ොဩ
 
HashMapጱ຅᭜ොဩํ4ӻғ

![三歪教你学Java集合(1) 第50页插图](../assets/images/三歪教你学Java集合(1)_p50_1_906536c7.png)

![三歪教你学Java集合(1) 第50页插图](../assets/images/三歪教你学Java集合(1)_p50_2_880d85b2.png)

![三歪教你学Java集合(1) 第50页插图](../assets/images/三歪教你学Java集合(1)_p50_3_6c9da229.png)

---

ࣁӤᶎጱ຅᭜ොဩ๋ݸӞᤈ҅౯ժտݎሿ᧣አԧ tableSizeFor() ҅౯ժᬰ݄፡፡ғ
፡ਠӤᶎݢᚆտఽک॰ௗጱฎғԅࠨฎਖ਼2ጱෆහ଍ጱහᩙᕳthresholdҘ
thresholdᬯӻ౮ާݒᰁฎᴇ꧊҅٬ਧԧฎވᥝਖ਼වڜᤒٚවڜ̶ਙጱ꧊ଫᧆฎғ capacity * 
load factor ಍੒ጱ̶
ٌਫᬯ᯾ՐՐฎӞӻڡত۸҅୮ڠୌߢ૶ᤒጱ෸ײ҅ਙտ᯿ෛᩙ꧊ጱғ
 
ᛗԭڦጱ຅᭜ොဩ᮷૧ӧग़҅ᬯ᯾౯੪ӧᕡᦖԧғ

![三歪教你学Java集合(1) 第51页插图](../assets/images/三歪教你学Java集合(1)_p51_1_08fa7daf.png)

![三歪教你学Java集合(1) 第51页插图](../assets/images/三歪教你学Java集合(1)_p51_2_3cb388b7.png)

![三歪教你学Java集合(1) 第51页插图](../assets/images/三歪教你学Java集合(1)_p51_3_399841b7.png)

![三歪教你学Java集合(1) 第51页插图](../assets/images/三歪教你学Java集合(1)_p51_4_ca76029a.png)

---

1.2putොဩ
 
putොဩݢզ᧔ฎHashMapጱ໐ஞ҅౯ժ๶፡፡ғ
౯ժ๶፡፡ਙฎெԍᦇᓒߢ૶꧊ጱғ
ԅՋԍᥝᬯ໏ଗޫҘҘ౯ժӞᛱ๶᧔ፗളਖ਼key֢ԅߢ૶꧊ӧ੪অԧހ҅؉୑౲ᬩᓒฎଗࡶአጱҘҘ
౯ժ፡ӥ๶ғ

![三歪教你学Java集合(1) 第52页插图](../assets/images/三歪教你学Java集合(1)_p52_1_21e8262d.png)

![三歪教你学Java集合(1) 第52页插图](../assets/images/三歪教你学Java集合(1)_p52_2_b8fc56d6.png)

![三歪教你学Java集合(1) 第52页插图](../assets/images/三歪教你学Java集合(1)_p52_3_49c208bc.png)

---

౯ժฎ໑ഝkeyጱߢ૶꧊๶כਂࣁවڜᤒӾጱ҅౯ժᤒἕᦊጱڡত਻ᰁฎ16҅ᥝනکවڜᤒӾ҅੪ฎ0-
15ጱ֖ᗝӤ̶Ԟ੪ฎtab[i = (n - 1) & hash] ̶ݢզݎሿጱฎғࣁ؉ & ᬩᓒጱ෸ײ҅ՐՐฎݸ4֖
ํප~ᮎইຎ౯ժkeyጱߢ૶꧊ṛ֖ݒ۸உय़֖҅֗ݒ۸உੜ̶ፗള೭ᬦ݄؉ & ᬩᓒ҅ᬯ੪տ੕ᛘᦇᓒڊ
๶ጱHash꧊ፘݶጱஉग̶़
ᘒᦡᦇᘏਖ਼keyጱߢ૶꧊ጱṛ֖Ԟ؉ԧᬩᓒ(Өṛ16֖؉୑౲ᬩᓒֵ҅஑ࣁ؉&ᬩᓒ෸҅ྌ෸ጱ֖֗ਫᴬ
Ӥฎṛ֖Ө֖֗ጱᕮݳ)҅ᬯ੪ीےԧᵋ๢௔҅ٺ੝ԧᏳඊ٫ᑱጱݢᚆ௔Ѻ
ӥᶎ౯ժٚ๶፡፡ၞᑕฎெԍ໏ጱғ
ෛ꧊ᥟፍ෯꧊҅ᬬࢧ෯꧊ၥᦶғ

![三歪教你学Java集合(1) 第53页插图](../assets/images/三歪教你学Java集合(1)_p53_1_a9d9f524.png)

![三歪教你学Java集合(1) 第53页插图](../assets/images/三歪教你学Java集合(1)_p53_2_a0bab89e.png)

---

ളӥ๶౯ժ፡፡resize() ොဩ҅ࣁڡত۸ጱ෸ײᥝ᧣አᬯӻොဩ҅୮වڜᤒزᔰय़ԭ capacity * 
load factor ጱ෸ײԞฎ᧣አresize()

![三歪教你学Java集合(1) 第54页插图](../assets/images/三歪教你学Java集合(1)_p54_1_6adaf429.png)

---

1.3getොဩ

![三歪教你学Java集合(1) 第55页插图](../assets/images/三歪教你学Java集合(1)_p55_1_6d470517.png)

---

ളӥ๶౯ժ፡፡getNode() ฎெԍਫሿጱғ
1.4removeොဩ
 
ٚ๶፡፡removeNode() ጱਫሿғ

![三歪教你学Java集合(1) 第56页插图](../assets/images/三歪教你学Java集合(1)_p56_1_3bfa15aa.png)

![三歪教你学Java集合(1) 第56页插图](../assets/images/三歪教你学Java集合(1)_p56_2_6a636677.png)

![三歪教你学Java集合(1) 第56页插图](../assets/images/三歪教你学Java集合(1)_p56_3_5ac6fa60.png)

---

ԫ̵HashMapӨHashtable੒ྲ
 
՗ਂؙᕮ຅޾ਫሿ๶ᦖच๜Ӥ᮷ฎፘݶጱ̶ਙ޾HashMapጱ๋य़ጱӧݶฎਙฎᕚᑕਞقጱ҅ݚक़
ਙӧ꧋ᦜkey޾valueԅnull̶Hashtableฎӻᬦ෸ጱᵞݳᔄ҅ӧୌᦓࣁෛդᎱӾֵአ҅ӧᵱᥝᕚᑕ
ਞقጱ࣋ݳݢզአHashMap๊ഘ҅ᵱᥝᕚᑕਞقጱ࣋ݳݢզአConcurrentHashMap๊ഘ

![三歪教你学Java集合(1) 第57页插图](../assets/images/三歪教你学Java集合(1)_p57_1_038143a8.png)

---

ӣ̵HashMap௛ᕮ
 
ࣁJDK8ӾHashMapጱବ੶ฎғහᕟ+᱾ᤒ(වڜᤒ)+ᕁἓ໅
ࣁවڜᤒӾํᤰ᫹ࢩৼᬯԍӞӻં௔҅୮ᤰ᫹ࢩৼ*ڡত਻ᰁੜԭවڜᤒزᔰ෸҅ᧆවڜᤒտٚවڜ҅
ಘ਻2׭Ѻ
ᤰ᫹ࢩৼጱἕᦊ꧊ฎ0.75҅෫ᦞฎڡতय़ԧᬮฎڡতੜԧ੒౯ժHashMapጱ௔ᚆ᮷ӧঅ
ᤰ᫹ࢩৼڡত꧊य़ԧ҅ݢզٺ੝වڜᤒٚවڜ(ಘ਻ጱེහ)҅֕ݶ෸տ੕ᛘවڜ٫ᑱጱݢᚆ௔ݒय़
(වڜ٫ᑱԞฎᘙ௔ᚆጱӞӻ඙֢҅ᥝ஑඙֢᱾ᤒ(ᕁἓ໅)Ѻ
ᤰ᫹ࢩৼڡত꧊ੜԧ҅ݢզٺੜවڜ٫ᑱጱݢᚆ௔҅֕ݶ෸ಘ਻ጱེහݢᚆ੪տݒग़Ѻ
ڡত਻ᰁጱἕᦊ꧊ฎ16҅ਙԞӞ໏҅෫ᦞڡতय़ԧᬮฎੜԧ҅੒౯ժጱHashMap᮷ฎํ୽ߥጱғ
ڡত਻ᰁᬦय़҅ᮎԍ᭭ܲ෸౯ժጱ᭛ଶ੪տݑ୽ߥ~
ڡত਻ᰁᬦੜ҅වڜᤒٚවڜ(ಘ਻ጱེහ)ݢᚆ੪ݒ஑ग़҅ಘ਻ԞฎӞկᶋଉᘙᩇ௔ᚆጱӞկԪ~
՗რᎱӤ౯ժݢզݎሿғHashMapଚӧฎፗള೭keyጱߢ૶꧊๶አጱ҅ਙտਖ਼keyጱߢ૶꧊ጱṛ16֖ᬰ
ᤈ୑౲඙ֵ֢҅஑౯ժਖ਼زᔰනفߢ૶ᤒጱ෸ײीےԧӞਧጱᵋ๢௔̶
ᬮᥝ꧊஑ဳ఺ጱฎғଚӧฎ໲ৼӤํ8֖زᔰጱ෸ײਙ੪ᚆݒ౮ᕁἓ໅҅ਙ஑ݶ෸ჿ᪃౯ժጱවڜᤒ਻
ᰁय़ԭ64಍ᤈጱ~

![三歪教你学Java集合(1) 第58页插图](../assets/images/三歪教你学Java集合(1)_p58_1_fc53548e.png)

![三歪教你学Java集合(1) 第59页插图](../assets/images/三歪教你学Java集合(1)_p59_1_61238920.png)

![三歪教你学Java集合(1) 第59页插图](../assets/images/三歪教你学Java集合(1)_p59_2_0813eda9.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
م̵LinkedHashMap
 
Ӟ̵LinkedHashMap
 
Ḓض౯ժ๶፡፡ᔄᖀಥࢶғ

![三歪教你学Java集合(1) 第60页插图](../assets/images/三歪教你学Java集合(1)_p60_1_3c233a1a.jpeg)

![三歪教你学Java集合(1) 第60页插图](../assets/images/三歪教你学Java集合(1)_p60_2_9ef93dcf.jpeg)

---

౯ᓌܔᘉᦲԧӞӥᶮ᮱ጱဳ᯽(౯᝕෈࿜ଘჂ҅ইຎํᲙጱࣈො᧗ग़ग़۱႗~ཻᬨࣁᦧᦞ܄ӥ೰ྋ)

![三歪教你学Java集合(1) 第61页插图](../assets/images/三歪教你学Java集合(1)_p61_1_fe0239b4.png)

![三歪教你学Java集合(1) 第61页插图](../assets/images/三歪教你学Java集合(1)_p61_2_aefdabc7.png)

---

՗ᶮ᮱ᘉᦲ౯ժ੪ݢզ୭ᕑ௛ᕮڊLinkedHashMapپᅩғ
ବ੶ฎවڜᤒ޾݌ݻ᱾ᤒ
꧋ᦜԅnull҅ӧݶྍ
ൊفጱᶲଧฎํଧጱ(ବ੶᱾ᤒᛘֵํଧ)
ᤰ᫹ࢩৼ޾ڡত਻ᰁ੒LinkedHashMap୽ߥฎஉय़ጱ~
ݶ෸Ԟᕳ౯ଃԧپӻወᳯғ
access-ordered޾insertion-orderedٍ֛ጱֵአ޾఺௏
ԅՋԍ᧔ڡত਻ᰁ੒᭭ܲဌํ୽ߥҘ
૶๕ݢզࣁ፡რᎱጱᬦᑕӾݢզᥴ٬ധ౯ᬯӷӻወᳯ~~~ᮎളӥ๶੪୏তމ
1.1LinkedHashMapጱऒ

![三歪教你学Java集合(1) 第62页插图](../assets/images/三歪教你学Java集合(1)_p62_1_aefdabc7.png)

---

1.2LinkedHashMap᯿ٟጱොဩ
 
ӥᶎ౯ڜԈ੪ᬯӷӻྲ᫾᯿ᥝጱғ
ᬯ੪ܦᦤԧ౯ժጱLinkedHashMapବ੶ᏟᏟਫਫฎවڜᤒ޾݌ݻ᱾ᤒ~
ࣁ຅ୌෛᜓᅩ෸҅຅ୌጱฎLinkedHashMap.Entry  ӧٚฎNode .
1.3຅᭜ොဩ
 
ݢզݎሿ҅LinkedHashMapํ5ӻ຅᭜ොဩғ
ӥᶎ౯ժ๶፡፡຅᭜ොဩጱਧԎฎெԍ໏ጱғ

![三歪教你学Java集合(1) 第63页插图](../assets/images/三歪教你学Java集合(1)_p63_1_48b62a8b.png)

![三歪教你学Java集合(1) 第63页插图](../assets/images/三歪教你学Java集合(1)_p63_2_6abd8c42.png)

![三歪教你学Java集合(1) 第63页插图](../assets/images/三歪教你学Java集合(1)_p63_3_0b77884a.png)

---

՗຅᭜ොဩӤ౯ժݢզᎣ᭲ጱฎғLinkedHashMapἕᦊֵአጱฎൊفᶲଧ
1.4putොဩ
 
ܻ๜౯ฎమᥝತputොဩ҅፡፡ฎெԍਫሿጱ҅ݸ๶ဌತ፳҅੪॰ԧӻௗ~

![三歪教你学Java集合(1) 第64页插图](../assets/images/三歪教你学Java集合(1)_p64_1_8604d5bd.png)

---

ٚᶷԧӞӥܻ҅๶LinkedHashMap޾HashMapጱputොဩฎӞ໏ጱѺLinkedHashMapᖀಥ፳
HashMap҅LinkedHashMapဌํ᯿ٟHashMapጱputොဩ
ಅզ҅LinkedHashMapጱputොဩ޾HashMapฎӞ໏ጱ̶
୮ᆐԧ҅ࣁڠୌᜓᅩጱ෸ײ҅᧣አጱฎLinkedHashMap᯿ٟጱොဩ~

![三歪教你学Java集合(1) 第65页插图](../assets/images/三歪教你学Java集合(1)_p65_1_12707f8b.png)

---

1.5getොဩ

![三歪教你学Java集合(1) 第66页插图](../assets/images/三歪教你学Java集合(1)_p66_1_d36cfc9f.png)

![三歪教你学Java集合(1) 第66页插图](../assets/images/三歪教你学Java集合(1)_p66_2_fab23887.png)

---

getොဩԞฎग़ԧғڣෙฎވԅᦢᳯᶲଧ~~~
ᦖکԧᬯ᯾҅ఽᥧ౯ժݢզᓌܔၥᦶӞူԧғ
Ḓض౯ժ๶፡፡૪ൊفᶲଧ๶ᬰᤈൊف޾᭭ܲғ
ၥᦶӞူғ
    public static void insertOrder() {
 
        // ἕᦊฎൊفᶲଧ
        LinkedHashMap<Integer,String>  insertOrder = new LinkedHashMap();
 
        String value = "ىဳلռݩJava3y";
        int i = 0;
 
        insertOrder.put(i++, value);
        insertOrder.put(i++, value);
        insertOrder.put(i++, value);
        insertOrder.put(i++, value);
        insertOrder.put(i++, value);
 
        //᭭ܲ
        Set<Integer> set = insertOrder.keySet();
        for (Integer s : set) {
            String mapValue = insertOrder.get(s);
            System.out.println(s + "---" + mapValue);
        }
    }

![三歪教你学Java集合(1) 第67页插图](../assets/images/三歪教你学Java集合(1)_p67_1_f28a7359.png)

---

ള፳҅౯ժ๶ၥᦶӞӥզᦢᳯᶲଧ๶ᬰᤈൊف޾᭭ܲғ
դᎱ፡֒ฎဌํᳯ᷌҅֕ฎᬩᤈտڊᲙጱѺ
    public static void accessOrder() {
        // ᦡᗝԅᦢᳯᶲଧጱොୗ
        LinkedHashMap<Integer,String> accessOrder = new LinkedHashMap(16, 
0.75f, true);
 
        String value = "ىဳلռݩJava3y";
        int i = 0;
        accessOrder.put(i++, value);
        accessOrder.put(i++, value);
        accessOrder.put(i++, value);
        accessOrder.put(i++, value);
        accessOrder.put(i++, value);
 
 
        // ᭭ܲ
        Set<Integer> sets = accessOrder.keySet();
        for (Integer key : sets) {
            String mapValue = accessOrder.get(key);
            System.out.println(key + "---" + mapValue);
        }
 
    }

![三歪教你学Java集合(1) 第68页插图](../assets/images/三歪教你学Java集合(1)_p68_1_18d6c75b.png)

---

ڹᶎࣁ፡რᎱဳ᯽ጱ෸ײ౯ժ੪ݎሿԧғࣁAccessOrderጱఘ٭ӥֵ҅አgetොဩԞฎᕮ຅௔ጱץදѺ
ԅԧᓌܔ፡ڊ՜עጱ܄ڦ҅ӥᶎ౯੪ፗളአkey๶ᬰᤈ፡ԧ~
զӥฎᦢᳯᶲଧጱၥᦶғ
ၥᦶᕮຎғ
 
    public static void accessOrder() {
        // ᦡᗝԅᦢᳯᶲଧጱොୗ
        LinkedHashMap<Integer,String> accessOrder = new LinkedHashMap(16, 
0.75f, true);
 
        String value = "ىဳلռݩJava3y";
        int i = 0;
        accessOrder.put(i++, value);
        accessOrder.put(i++, value);
        accessOrder.put(i++, value);
        accessOrder.put(i++, value);
        accessOrder.put(i++, value);
 
 
        // ᦢᳯӞӥkeyԅ3ጱزᔰٚᬰᤈ᭭ܲ
        accessOrder.get(3);
 
        // ᭭ܲ
        Set<Integer> sets = accessOrder.keySet();
        for (Integer key : sets) {
 
            System.out.println(key );
        }
 
    }

![三歪教你学Java集合(1) 第69页插图](../assets/images/三歪教你学Java集合(1)_p69_1_43e780a9.png)

---

զӥฎൊفᶲଧጱၥᦶ(դᎱ੪ӧᩂԧ҅޾ӤᶎپԒӞ໏)ғ
౯ժݢզᬯ໏ቘᥴғ๋ଉአጱਖ਼ٌනࣁ᱾ᤒጱ๋ݸ҅ӧଉአጱනࣁ᱾ᤒጱ๋ڹ~
ᬯӻᎣᦩᅩզ౯ጱቘᥴᘒ᥺҅ਙᬯӻᦢᳯᶲଧࣁLinkedHashMapইຎӧ᯿ٟአ॒ଚӧय़~ਙฎአ๶ᕳ
ڦጱਫሿᬰᤈಘ઀ጱ
ࢩԅ๋ଉᤩֵአጱزᔰٚ᭭ܲጱ෸ײܩනࣁԧ๋ݸᬟ҅ࣁLinkedHashMapӾ౯Ԟဌತک੒ଫጱො
ဩ๶ᬰᤈ᧣አ~
Ӟӻ removeEldestEntry(Map.Entry<K,V> eldest) ොဩ҅᯿ٟਙݢզڢᴻ๋ԋ๚ᤩֵአጱز
ᔰѺѺ
ᬮํӞӻฎafterNodeInsertion(boolean evict) ොဩ҅ෛी෸ڣෙฎވᵱᥝڢᴻ๋ԋ๚ᤩֵ
አጱزᔰѺѺ

![三歪教你学Java集合(1) 第70页插图](../assets/images/三歪教你学Java集合(1)_p70_1_c5c8dd86.png)

![三歪教你学Java集合(1) 第70页插图](../assets/images/三歪教你学Java集合(1)_p70_2_4b91a8f3.png)

---

1.6removeොဩ
 
੒ԭremoveොဩ҅ࣁLinkedHashMapӾԞဌํ᯿ٟ҅ਙ᧣አጱᬮฎᆿᔄጱHashMapጱremove() ො
ဩ҅ࣁLinkedHashMapӾ᯿ٟጱฎғ afterNodeRemoval(Node<K,V> e) ᬯӻොဩ
୮ᆐԧ҅ࣁremoveጱ෸ײտၿ݊کӤᶎ᯿ٟጱොဩғ
1.7᭭ܲጱොဩ

![三歪教你学Java集合(1) 第71页插图](../assets/images/三歪教你学Java集合(1)_p71_1_26794901.png)

![三歪教你学Java集合(1) 第71页插图](../assets/images/三歪教你学Java集合(1)_p71_2_c29c6076.png)

![三歪教你学Java集合(1) 第71页插图](../assets/images/三歪教你学Java集合(1)_p71_3_b19b48d4.png)

---

Set<Map.Entry<K,V>> entrySet() ฎᤩ᯿ٟጱԧ
፡کԧᬯ᯾҅౯ժ੪Ꭳ᭲ԅࠨဳ᯽᧔ғڡত਻ᰁ੒᭭ܲဌํ୽ߥ
ࢩԅਙ᭭ܲጱฎLinkedHashMapٖ᮱ᖌಷጱӞӻ݌ݻ᱾ᤒ҅ᘒӧฎවڜᤒ(୮ᆐԧ҅᱾ᤒ݌ݻ᱾ᤒጱز
ᔰ᮷๶რԭවڜᤒ)
 
ԫ̵LinkedHashMap௛ᕮ
 
LinkedHashMapྲHashMapग़ԧӞӻ݌ݻ᱾ᤒጱᖌಷ҅ࣁහഝᕮ຅ᘒ᥺ਙᥝ॔๥ӞԶ҅ᴅ᧛რᎱ᩸๶
ྲ᫾᫷ຂӞԶ҅ࢩԅय़ग़᮷ኧHashMapਫሿԧ..
ᴅ᧛რᎱጱ෸ײ౯ժտݎሿग़ாฎ෫॒ӧࣁጱ~ৼᔄአᆿᔄጱොဩ҅ৼᔄ᯿ٟԧᆿᔄጱ᮱ړොဩܨݢᬡ
کӧӞ໏ጱපຎѺ
ྲইғLinkedHashMapଚဌํ᯿ٟputොဩ҅ᘒputොဩٖ᮱ጱnewNode() ොဩ᯿ٟԧ̶
LinkedHashMap᧣አᆿᔄጱputොဩ҅᯾ᶎࢧ᧣ጱฎ᯿ٟݸጱnewNode() ҅՗ᘒᬡکፓጱѺ

![三歪教你学Java集合(1) 第72页插图](../assets/images/三歪教你学Java集合(1)_p72_1_8001f4f7.png)

![三歪教你学Java集合(1) 第72页插图](../assets/images/三歪教你学Java集合(1)_p72_2_11d772c3.png)

---

LinkedHashMapݢզᦡᗝӷᐿ᭭ܲᶲଧғ
ᦢᳯᶲଧҁaccess-ordered҂
ൊفᶲଧҁinsertion-ordered҂
ἕᦊฎൊفᶲଧጱ
੒ԭᦢᳯᶲଧ҅ਙฎLRU(๋ᬪ๋੝ֵአ)ᓒဩጱਫሿ҅ᥝֵአਙᥝԍ᯿ٟLinkedListMapጱپӻොဩ
( removeEldestEntry(Map.Entry<K,V> eldest) ޾afterNodeInsertion(boolean evict) )҅ᥝ
ԍฎಘ઀౮LRUMap๶ֵአ҅ӧᆐᦡᗝԅᦢᳯᶲଧҁaccess-ordered҂ጱአ॒ӧय़~
LinkedHashMap᭭ܲጱฎٖ᮱ᖌಷጱ݌ݻ᱾ᤒ҅ಅզ᧔ڡত਻ᰁ੒LinkedHashMap᭭ܲฎӧݑ୽ߥ
ጱ
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
Ӡ̵TreeMap
 
 
Ӟ̵TreeMapڽຉ

![三歪教你学Java集合(1) 第73页插图](../assets/images/三歪教你学Java集合(1)_p73_1_3c233a1a.jpeg)

![三歪教你学Java集合(1) 第73页插图](../assets/images/三歪教你学Java集合(1)_p73_2_c50146be.png)

---

ೲᆙబֺ҅౯ᓌܔᘉᦲԧӞӥᶮ᮱ጱဳ᯽(౯᝕෈࿜ଘჂ҅ইຎํᲙጱࣈො᧗ग़ग़۱႗~ཻᬨࣁᦧᦞ܄ӥ
೰ྋ)
ള፳౯ժ๶፡፡ᔄᖀಥࢶғ

![三歪教你学Java集合(1) 第74页插图](../assets/images/三歪教你学Java集合(1)_p74_1_04b1cdb3.png)

---

ࣁဳ᯽Ӿ൉کጱᥝᅩ҅౯๶௛ᕮӞӥғ
TreeMapਫሿԧNavigableMapളݗ҅ᘒNavigableMapളݗᖀಥ፳SortedMapളݗ҅ᛘֵ౯ժጱ
TreeMapฎํଧጱѺ
TreeMapବ੶ฎᕁἓ໅҅ਙොဩጱ෸ᳵ॔๥ଶ᮷ӧտॡṛ:log(n)~
ᶋݶྍ
ֵአComparator౲ᘏComparable๶ྲ᫾keyฎވፘᒵӨഭଧጱᳯ᷌~
 
੒౯ᘒ᥺҅Comparator޾Comparable౯᮷஫஑૧ӧग़ԧ~~~ӥᶎ੪୏ত፡TreeMapጱრᎱ๶፡፡ਙฎ
ெԍਫሿጱ҅ଚӬࢧᶶӞӥComparator޾ComparableጱአဩމѺ
1.1TreeMapጱऒ

![三歪教你学Java集合(1) 第75页插图](../assets/images/三歪教你学Java集合(1)_p75_1_74586890.png)

![三歪教你学Java集合(1) 第75页插图](../assets/images/三歪教你学Java集合(1)_p75_2_dbf18a7c.png)

---

1.2TreeMap຅᭜ොဩ
 
TreeMapጱ຅᭜ොဩํ4ӻғ
ݢզݎሿ҅TreeMapጱ຅᭜ොဩय़ग़හӨcomparatorํىғ

![三歪教你学Java集合(1) 第76页插图](../assets/images/三歪教你学Java集合(1)_p76_1_f3326c73.png)

---

Ԟ੪ฎᶮ᮱ဳ᯽᧔ጱғTreeMapํଧฎ᭗ᬦComparator๶ᬰᤈྲ᫾ጱ҅ইຎcomparatorԅnull҅ᮎ
ԍ੪ֵአᛔᆐᶲଧ~
಑ӻྲොғইຎvalueฎෆහ҅ᛔᆐᶲଧ೰ጱ੪ฎ౯ժଘଉഭଧጱᶲଧ(1,2,3,4,5..)~
    TreeMap<Integer, Integer> treeMap = new TreeMap<>();
 
    treeMap.put(1, 5);

![三歪教你学Java集合(1) 第77页插图](../assets/images/三歪教你学Java集合(1)_p77_1_8b0c1a9a.png)

---

1.3putොဩ
 
౯ժ๶፡፡TreeMapጱ໐ஞputොဩ҅ᴅ᧛ਙ੪ݢզ឴ݐӧ੝ىԭTreeMapᇙ௔ጱӳᥜԧ~
    treeMap.put(2, 4);
    treeMap.put(3, 3);
    treeMap.put(4, 2);
    treeMap.put(5, 1);
 
    for (Entry<Integer, Integer> entry : treeMap.entrySet()) {
 
        String s = entry.getKey() +"ىဳلռݩғJava3y---->" + entry.getValue();
 
        System.out.println(s);
    }

![三歪教你学Java集合(1) 第78页插图](../assets/images/三歪教你学Java集合(1)_p78_1_9d335cc0.png)

---

ӥᶎฎcompare(Object k1, Object k2) ොဩ
ইຎ౯ժᦡᗝkeyԅnull҅տಲڊ୑ଉጱ҅੪ӧಗᤈӥᶎጱդᎱԧ̶
    /**
     * Compares two keys using the correct comparison method for this TreeMap.
     */
    @SuppressWarnings("unchecked")
    final int compare(Object k1, Object k2) {
        return comparator==null ? ((Comparable<? super K>)k1).compareTo((K)k2)
            : comparator.compare((K)k1, (K)k2);
    }

![三歪教你学Java集合(1) 第79页插图](../assets/images/三歪教你学Java集合(1)_p79_1_749c1053.png)

---

1.4getොဩ
 
ളӥ๶౯ժ๶፡፡getොဩጱਫሿғ
ᅩᬰ݄getEntry() ፡፡ਫሿғ
ইຎComparatorӧԅnull҅ളӥ๶౯ժᬰ݄፡፡getEntryUsingComparator(Object key) ҅ฎெԍ
ਫሿጱ

![三歪教你学Java集合(1) 第80页插图](../assets/images/三歪教你学Java集合(1)_p80_1_3ea9ea92.png)

![三歪教你学Java集合(1) 第80页插图](../assets/images/三歪教你学Java集合(1)_p80_2_8607db66.png)

![三歪教你学Java集合(1) 第80页插图](../assets/images/三歪教你学Java集合(1)_p80_3_35ae5781.png)

---

1.5removeොဩ
 
ڢᴻᜓᅩጱ෸ײ᧣አጱฎdeleteEntry(Entry<K,V> p) ොဩ҅ᬯӻොဩԆᥝฎڢᴻᜓᅩଚӬଘᤍᕁἓ
໅
ଘᤍᕁἓ໅ጱդᎱฎྲ᫾॔๥ጱ҅౯੪ӧ᧔ԧ֦҅ժ݄፡މ(ݍྋ౯፡ӧ౜)....
1.6᭭ܲොဩ
 
ࣁ፡რᎱጱ෸ײݢᚆӧᎣ᭲ߺӻฎ໐ஞጱ᭭ܲොဩ҅ࢩԅIteratorํᶋଉᶋଉग़~

![三歪教你学Java集合(1) 第81页插图](../assets/images/三歪教你学Java集合(1)_p81_1_0ec9a4ee.png)

![三歪教你学Java集合(1) 第81页插图](../assets/images/三歪教你学Java集合(1)_p81_2_f670fd3e.png)

---

ྌ෸҅౯ժݝᵱᥝdebugӞӥ፡፡҅᪙ӥ݄੪অѺ
ԭฎԒ҅౯ժݢզತکғTreeMap᭭ܲฎֵአEntryIteratorᬯӻٖ᮱ᔄጱ
Ḓض๶፡፡EntryIteratorጱᔄᕮ຅ࢶމғ

![三歪教你学Java集合(1) 第82页插图](../assets/images/三歪教你学Java集合(1)_p82_1_f72e1678.png)

![三歪教你学Java集合(1) 第82页插图](../assets/images/三歪教你学Java集合(1)_p82_2_d9ecb5f7.png)

![三歪教你学Java集合(1) 第82页插图](../assets/images/三歪教你学Java集合(1)_p82_3_c807e29e.png)

---

ݢզݎሿ҅EntryIteratorय़ग़ጱਫሿ᮷ฎࣁᆿᔄӾғ
ᮎളӥ๶౯ժ݄፡፡PrivateEntryIteratorྲ᫾᯿ᥝጱොဩғ

![三歪教你学Java集合(1) 第83页插图](../assets/images/三歪教你学Java集合(1)_p83_1_69614cb5.png)

![三歪教你学Java集合(1) 第83页插图](../assets/images/三歪教你学Java集合(1)_p83_2_9f4abca7.png)

---

౯ժᬰ݄successor(e) ොဩ፡፡ਫሿғ
successor ٌਫ੪ฎӞӻᕮᅩጱ ӥӞӻᕮᅩ҅ಅ᧲ ӥӞӻ҅ฎೲེଧഭଧݸጱӥӞӻᕮᅩ̶՗դ
ᎱӾݢզ፡ڊ҅ইຎݦৼ໅ӧԅᑮ҅੪ᬬࢧݦৼ໅Ӿ๋ੜᕮᅩ̶ইຎݦৼ໅ԅᑮ҅੪ᥝݻӤࢧშ
ԧ̶ࣁᬯᐿఘ٭ӥ҅t ฎզٌԅ໑ጱ໅ጱ๋ݸӞӻᕮᅩ̶ইຎਙฎٌᆿᕮᅩጱૢ਎ৼ҅ᮎԍᆿᕮᅩ
੪ฎਙጱӥӞӻᕮᅩ҅ވڞ҅t ੪ฎզٌᆿᕮᅩԅ໑ጱ໅ጱ๋ݸӞӻᕮᅩ҅ᵱᥝེٚݻӤࢧშ̶Ӟ
ፗک ch ฎ p ጱૢ਎ৼԅྊ̶
๶რғhttps://blog.csdn.net/on_1y/article/details/27231855

![三歪教你学Java集合(1) 第84页插图](../assets/images/三歪教你学Java集合(1)_p84_1_c2d5febb.png)

---

ԫ̵TreeMap௛ᕮ
 
TreeMapବ੶ฎᕁἓ໅҅ᚆड़ਫሿᧆMapᵞݳํଧ~
ইຎࣁ຅᭜ොဩӾփ᭓ԧComparator੒᨝҅ᮎԍ੪տզComparator੒᨝ጱොဩᬰᤈྲ᫾̶ވڞ҅ڞֵ
አComparableጱcompareTo(T o) ොဩ๶ྲ᫾̶
꧊஑᧔กጱฎғইຎֵአጱฎcompareTo(T o) ොဩ๶ྲ᫾҅keyӞਧฎӧᚆԅnull҅ଚӬ஑ਫሿ
ԧComparableളݗጱ̶
ܨֵฎփفԧComparator੒᨝҅ӧአcompareTo(T o) ොဩ๶ྲ᫾҅keyԞฎӧᚆԅnullጱ
    public static void main(String[] args) {
        TreeMap<Student, String> map = new TreeMap<Student, String>((o1, o2) -
> {
            //Ԇᥝ๵կ
            int num = o1.getAge() - o2.getAge();
 
            //ེᥝ๵կ
            int num2 = num == 0 ? o1.getName().compareTo(o2.getName()) : num;
 
            return num2;
        });
 
        //ڠୌ਍ኞ੒᨝
        Student s1 = new Student("ᄞਞ", 30);
        Student s2 = new Student("ືӥణ", 35);
 
        //Ⴒےزᔰᬰᵞݳ
        map.put(s1, "ਟ๖");

![三歪教你学Java集合(1) 第85页插图](../assets/images/三歪教你学Java集合(1)_p85_1_0705ab41.png)

---

౯ժ՗რᎱӾጱஉग़ࣈොӾݎሿғComparator޾Comparableڊሿጱ᷇ሲฎஉṛጱ҅ࢩԅTreeMapਫ
ሿํଧᥝԍ੪ฎक़ኴփ᭓ᬰ๶Comparator੒᨝҅ᥝԍ੪ֵአἕᦊkeyጱComparableളݗ(ਫሿᛔᆐഭ
ଧ)
๋ݸ౯੪๶௛ᕮӞӥTreeMapᥝᅩމғ
1. ኧԭବ੶ฎᕁἓ໅҅ᮎԍ෸ᳵ॔๥ଶݢզכᦤԅlog(n)
2. keyӧᚆԅnull҅ԅnullԅಲڊNullPointExceptionጱ
3. మᥝᛔਧԎྲ᫾҅ࣁ຅᭜ොဩӾփفCo smparator੒᨝҅ވڞֵአkeyጱᛔᆐഭଧ๶ᬰᤈྲ᫾
4. TreeMapᶋݶྍጱ҅మᥝݶྍݢզֵአCollections๶ᬰᤈ੗ᤰ
 
        map.put(s2, "ز๖");
        map.put(null, "࿥๖");
 
        //឴ݐkeyᵞݳ
        Set<Student> set = map.keySet();
 
        //᭭ܲkeyᵞݳ
        for (Student student : set) {
            String value = map.get(student);
            System.out.println(student + "---------" + value);
        }
    }

![三歪教你学Java集合(1) 第86页插图](../assets/images/三歪教你学Java集合(1)_p86_1_a674b9c0.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
ك̵ConcurrentHashMap
 
 
Ӟ̵ConCurrentHashMapڽຉ
 
ConCurrentHashMapࣁڡ਍ጱ෸ײݍྋ౯ฎဌํള᥶ᬦጱ҅ӧᎣ֦᭲ժള᥶ᬦԧဌํ~
ᬯӻᔄލ஑Ԟꂁ੝ጱ҅ࣁᵞݳӾฎྲ᫾॔๥ጱӞӻᔄԧ҅ਙၿ݊کԧӞԶग़ᕚᑕጱᎣᦩᅩ̶
ӧԧᥴ౲஫ᦕग़ᕚᑕᎣᦩᅩጱݶ਍Ԟӧᥝொ҅ߺدአکԧग़ᕚᑕጱᎣᦩᅩ҅౯᮷տᓌܔՕᕨӞӥ҅ଚᕳ
ڊ੒ଫጱᩒා݄ᴅ᧛ጱ~
অԧ҅౯ժ੪๶୏তމ~
1.1ڡᦩConCurrentHashMap

![三歪教你学Java集合(1) 第87页插图](../assets/images/三歪教你学Java集合(1)_p87_1_9ef93dcf.jpeg)

![三歪教你学Java集合(1) 第87页插图](../assets/images/三歪教你学Java集合(1)_p87_2_3c233a1a.jpeg)

---

ConCurrentHashMapጱବ੶ฎғවڜᤒ+ᕁἓ໅҅ӨHashMapฎӞ໏ጱ̶
՗ڹᶎጱᒍᜓ౯ժԞݢզݎሿғ๋ளԧᥴӞӥᔄฎଗࡶጱ҅౯ժ፡რᎱጱᶮ᮱ဳ᯽੪ݢզԧѺ
౯ᓌܔᘉᦲԧӞӥᶮ᮱ጱဳ᯽(౯᝕෈࿜ଘჂ҅ইຎํᲙጱࣈො᧗ग़ग़۱႗~ཻᬨࣁᦧᦞ܄ӥ೰ྋ)

![三歪教你学Java集合(1) 第88页插图](../assets/images/三歪教你学Java集合(1)_p88_1_984cce1e.png)

![三歪教你学Java集合(1) 第89页插图](../assets/images/三歪教你学Java集合(1)_p89_1_65308c7b.png)

---

໑ഝӤᶎဳ᯽౯ժݢզᓌܔ௛ᕮғ
JDK1.8ବ੶ฎවڜᤒ+ᕁἓ໅
ConCurrentHashMapඪ೮ṛଚݎጱᦢᳯ޾ๅෛ҅ਙฎᕚᑕਞقጱ
༄ᔱ඙֢ӧአےᲁ҅getොဩฎᶋᴥलጱ
key޾value᮷ӧ꧋ᦜԅnull
1.2JDK1.7ବ੶ਫሿ
 
Ӥᶎ೰กጱฎJDK1.8ବ੶ฎғවڜᤒ+ᕁἓ໅҅Ԟ੪఺ޱ፳҅JDK1.7ጱବ੶᪙JDK1.8ฎӧݶጱ~
JDK1.7ጱବ੶ฎғsegments+HashEntryහᕟғ
ࢶ๶რғhttps://blog.csdn.net/panweiwei1994/article/details/78897275
SegmentᖀಥԧReentrantLock,ྯӻᇆྦྷ᮷ํԧӞӻᲁ҅ݞ؉“ᲁړྦྷ”
1.3ํԧHashtableԅࠨᵱᥝConCurrentHashMap
 
HashtableฎࣁྯӻොဩӤ᮷ےӤԧSynchronizedਠ౮ݶྍ҅පሲ֗ӥ̶
ConcurrentHashMap᭗ᬦࣁ᮱ړےᲁ޾ڥአCASᓒဩ๶ਫሿݶྍ̶
1.4CASᓒဩ޾volatileᓌܔՕᕨ
 
ࣁ፡ConCurrentHashMapრᎱԏڹ҅౯ժ๶ᓌܔᦖᦖCASᓒဩ޾volatileىᲫਁ
CASҁྲ᫾ӨԻഘ҅Compare and swap҂ ฎӞᐿํݷጱ෫ᲁᓒဩ
CASํ3ӻ඙֢හ

![三歪教你学Java集合(1) 第90页插图](../assets/images/三歪教你学Java集合(1)_p90_1_c7aa58e8.png)

---

ٖਂ꧊V
෯ጱᶼ๗꧊A
ᥝץදጱෛ꧊B
୮ӬՐ୮ᶼ๗꧊A޾ٖਂ꧊Vፘݶ෸҅ਖ਼ٖਂ꧊VץදԅB҅ވڞՋԍ᮷ӧ؉
୮ग़ӻᕚᑕ੤ᦶֵአCASݶ෸ๅෛݶӞӻݒᰁ෸҅ݝํٌӾӞӻᕚᑕᚆๅෛݒᰁጱ꧊(A޾ٖਂ꧊V
ፘݶ෸҅ਖ਼ٖਂ꧊VץදԅB)҅ᘒٌਙᕚᑕ᮷०ᨳ҅०ᨳጱᕚᑕଚӧտᤩ೯᩸҅ᘒฎᤩޞᎣᬯེᒋ
ԩӾ०ᨳ҅ଚݢզེٚ੤ᦶ(ވڞՋԍ᮷ӧ؉)
፡ԧӤᶎጱൈᬿଫᧆ੪உ਻ฃቘᥴԧ҅ضྲ᫾ฎވፘᒵ҅ইຎፘᒵڞ๊ഘ(CASᓒဩ)
ളӥ๶౯ժ፡፡volatileىᲫਁ҅ࣁڡ਍ጱ෸ײԞஉ੝ֵአکvolatileᬯӻىᲫਁ̶ݍྋ౯ဌአک҅ᘒ݈
ᕪଉࣁ፡Javaፘىᶎᦶ᷌ጱ෸ײ፡کਙ҅ᥧ஑ฎӞӻꂁᐟᑃ݈உᵙጱӞӻىᲫਁ̶ٌਫӧᆐ҅ᬮฎꂁ਻
ฃቘᥴጱ~
volatileᕪَ௛ᕮғvolatileՐՐአ๶כᦤᧆݒᰁ੒ಅํᕚᑕጱݢᥠ௔҅֕ӧכᦤܻৼ௔
౯ժਖ਼ٌೆ୏๶ᥴ᯽Ӟӥғ
כᦤᧆݒᰁ੒ಅํᕚᑕጱݢᥠ௔
ࣁग़ᕚᑕጱሾहӥғ୮ᬯӻݒᰁץද෸҅ಅํጱᕚᑕ᮷տᎣ᭲ᧆݒᰁᤩץදԧ҅Ԟ੪ฎಅ᧲
ጱ“ݢᥠ௔”
ӧכᦤܻৼ௔
ץදݒᰁ(ᩙ꧊)ਫᨶӤฎࣁJVMӾړԧঅپྍ҅ᘒࣁᬯپྍٖ(՗ᤰ᫹ݒᰁکץද)҅ਙฎӧਞ
قጱ̶
 
1.5ConCurrentHashMapऒ
 
ऒ੒᨝ํᬯԍپӻғ
౯ժ๶ᓌܔ፡Ӟӥ՜ժฎՋԍӳӳғ

![三歪教你学Java集合(1) 第91页插图](../assets/images/三歪教你学Java集合(1)_p91_1_40614ee0.png)

---

ڡེᴅ᧛ਠԏݸ҅ํጱં௔౯ԞӧॡႴ༩ਙฎଗՋԍጱ҅ࣁᖀᖅᴅ᧛ԏݸݢᚆ੪ก๔ԧ~
1.6ConCurrentHashMap຅᭜ොဩ
 
ConcurrentHashMapጱ຅᭜ොဩํ5ӻғ
ٍ֛ጱਫሿฎᬯ໏ৼጱғ

![三歪教你学Java集合(1) 第92页插图](../assets/images/三歪教你学Java集合(1)_p92_1_3061b7ae.png)

![三歪教你学Java集合(1) 第92页插图](../assets/images/三歪教你学Java集合(1)_p92_2_888b978a.png)

---

ݢզݎሿ҅ࣁ຅᭜ොဩӾํپ॒᮷᧣አԧ tableSizeFor() ҅౯ժ๶፡Ӟӥ՜ฎଗՋԍጱғ
ᅩᬰ݄ԏݸݎሿܻ҅ࠡ҅๶౯፡ᬦᬯӻොဩ҅ࣁHashMapጱ෸ײ.....

![三歪教你学Java集合(1) 第93页插图](../assets/images/三歪教你学Java集合(1)_p93_1_366f7dec.png)

---

ਙ੪ฎአ๶឴ݐय़ԭ݇හӬ๋ളᬪ2ጱෆེ଍ጱහ...
ᩙ꧊ᕳsizeCtlં௔Ԟ੪᧔กԧғᬯฎӥེಘ਻ጱय़ੜ~
 
1.7putොဩ
 
ᕣԭ๶کԧ๋໐ஞጱොဩԏӞғputොဩࠩ~~~~
౯ժض๶ෆ֛፡ӞӥputොဩଗԧՋԍԪғ

![三歪教你学Java集合(1) 第94页插图](../assets/images/三歪教你学Java集合(1)_p94_1_6e259a06.png)

---

ളӥ๶҅౯ժ๶፡፡ڡত۸වڜᤒጱ෸ײଗԧՋԍԪғ initTable()

![三歪教你学Java集合(1) 第95页插图](../assets/images/三歪教你学Java集合(1)_p95_1_ec45d4cf.png)

---

ݝᦏӞӻᕚᑕ੒වڜᤒᬰᤈڡত۸Ѻ
1.8getොဩ
 
՗ᶮ᮱ဳ᯽౯ժݢզ᧛ک҅getොဩฎӧአےᲁጱ҅ฎᶋᴥलጱ̶
౯ժݢզݎሿ҅Nodeᜓᅩฎ᯿ٟጱ҅ᦡᗝԧvolatileىᲫਁץ҅᷶ᛘֵਙྯེ឴ݐጱ᮷ฎ๋ෛᦡᗝጱ꧊

![三歪教你学Java集合(1) 第96页插图](../assets/images/三歪教你学Java集合(1)_p96_1_daa88d52.png)

![三歪教你学Java集合(1) 第96页插图](../assets/images/三歪教你学Java集合(1)_p96_2_c51cae10.png)

---

ԫ̵ConcurrentHashMap௛ᕮ
 
ӤᶎᓌܔՕᕨԧConcurrentHashMapጱ໐ஞᎣᦩ҅ᬮํஉग़Ꭳᦩᅩ᮷ဌํ൉݊ک֢҅ᘏጱ࿜ଘԞӧᚆ
ਖ਼ٌ୓౜~~ํي᪁ᬰفጱݶ਍ݢکӥᶎጱ᱾ളᖀᖅ਍ԟ̶
ӥᶎ౯๶ᓌܔ௛ᕮӞӥConcurrentHashMapጱ໐ஞᥝᅩғ
ବ੶ᕮ຅ฎවڜᤒ(හᕟ+᱾ᤒ)+ᕁἓ໅҅ᬯӞᅩ޾HashMapฎӞ໏ጱ̶
Hashtableฎਖ਼ಅํጱොဩᬰᤈݶྍ҅පሲ֗ӥ̶ᘒConcurrentHashMap֢ԅӞӻṛଚݎጱ਻
࢏҅ਙฎ᭗ᬦ᮱ړᲁਧ+CASᓒဩ๶ᬰᤈਫሿᕚᑕਞقጱ̶CASᓒဩԞݢզᦊԅฎԔᥡᲁጱӞᐿ~
ࣁṛଚݎሾहӥ҅ᕹᦇහഝ(ᦇᓒsize...ᒵᒵ)ٌਫฎ෫఺Ԏጱ҅ࢩԅࣁӥӞ෸ڰsize꧊੪ݒ۸ԧ̶
getොဩฎᶋᴥल҅෫ᲁጱ̶᯿ٟNodeᔄ҅᭗ᬦvolatileץ᷶next๶ਫሿྯེ឴ݐ᮷ฎ๋ෛᦡᗝጱ
꧊
ConcurrentHashMapጱkey޾Value᮷ӧᚆԅnull

![三歪教你学Java集合(1) 第97页插图](../assets/images/三歪教你学Java集合(1)_p97_1_99b2e9e0.png)

![三歪教你学Java集合(1) 第97页插图](../assets/images/三歪教你学Java集合(1)_p97_2_5d4df7d4.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
Ԝ̵Set
 
Ӟ̵HashSetڽຉ
 
Ḓض҅౯ժ๶፡ӞӥHashSetጱᖀಥᕮ຅ࢶғ
ೲᆙబֺ҅౯ժ๶፡፡HashSetᶮ᮱ဳ᯽ғ

![三歪教你学Java集合(1) 第98页插图](../assets/images/三歪教你学Java集合(1)_p98_1_c5371f9d.png)

![三歪教你学Java集合(1) 第98页插图](../assets/images/三歪教你学Java集合(1)_p98_2_3c233a1a.jpeg)

---

՗ᶮ᮱ဳ᯽๶፡҅౯ժ੪ݢզ୭ᕑHashSetጱᥝᅩԧғ
ਫሿSetളݗ
ӧכᦤᬽդᶲଧ
꧋ᦜزᔰԅnull
ବ੶ਫᴬӤฎӞӻHashMapਫֺ
ᶋݶྍ
ڡত਻ᰁᶋଉ୽ߥᬽդ௔ᚆ
 
 
ᶮ᮱ဳ᯽᧔ବ੶ਫᴬӤฎӞӻHashMapਫֺ҅ᮎᦤഝޫҘ

![三歪教你学Java集合(1) 第99页插图](../assets/images/三歪教你学Java集合(1)_p99_1_b75d3153.png)

---

౯ժٚ๶፡ӞӥHashSetෆӻᔄጱොဩ޾ં௔ғ
੒ԭ਍ԟᬦHashMapጱՈ๶᧔҅ᓌፗᓌܔ஑ᦏՈ୏ஞ҅ߢߢߢ~
౯ժᎣ᭲MapฎӞӻฉ੘҅ํkeyํvalue҅෬ᆐHashSetବ੶አጱฎHashMap҅ᮎԍvalueࣁߺ᯾
ޫҘҘҘ
valueฎӞӻObject҅ಅํጱvalue᮷ฎਙ
ಅզݢզፗള௛ᕮڊғHashSetਫᴬӤ੪ฎ੗ᤰԧHashMap҅඙֢HashSetزᔰਫᴬӤ੪ฎ඙֢
HashMap̶ᬯԞฎᶎݻ੒᨝ጱӞᐿ֛ሿ҅᯿አ௔ᩊṛѺ
 
ԫ̵TreeSetڽຉ
 
Ḓض҅౯ժԞ๶፡፡TreeSetጱᔄᖀಥᕮ຅ࢶғ

![三歪教你学Java集合(1) 第100页插图](../assets/images/三歪教你学Java集合(1)_p100_1_32637f58.png)

![三歪教你学Java集合(1) 第100页插图](../assets/images/三歪教你学Java集合(1)_p100_2_7b63def5.png)

![三歪教你学Java集合(1) 第100页插图](../assets/images/三歪教你学Java集合(1)_p100_3_0791b2f4.png)

---

ೲᆙబֺ҅౯ժ๶፡፡TreeSetᶮ᮱ဳ᯽ғ

![三歪教你学Java集合(1) 第101页插图](../assets/images/三歪教你学Java集合(1)_p101_1_e32e2492.png)

---

՗ᶮ᮱ဳ᯽๶፡҅౯ժ੪ݢզ୭ᕑTreeSetጱᥝᅩԧғ
ਫሿNavigableSetളݗ
ݢզਫሿഭଧۑᚆ
ବ੶ਫᴬӤฎӞӻTreeMapਫֺ
ᶋݶྍ

![三歪教你学Java集合(1) 第102页插图](../assets/images/三歪教你学Java集合(1)_p102_1_a9f9650e.png)

---

ӣ̵LinkedHashSetڽຉ
 
Ḓض҅౯ժԞ๶፡፡TreeSetጱᔄᖀಥᕮ຅ࢶғ
ೲᆙబֺ҅౯ժ๶፡፡LinkedHashSetᶮ᮱ဳ᯽ғ

![三歪教你学Java集合(1) 第103页插图](../assets/images/三歪教你学Java集合(1)_p103_1_ecde9f42.png)

![三歪教你学Java集合(1) 第103页插图](../assets/images/三歪教你学Java集合(1)_p103_2_46ead6b2.png)

---

՗ᶮ᮱ဳ᯽๶፡҅౯ժ੪ݢզ୭ᕑLinkedHashSetጱᥝᅩԧғ
ᬽդฎํଧጱ
꧋ᦜԅnull
ବ੶ਫᴬӤฎӞӻHashMap+݌ݻ᱾ᤒਫֺ(ٌਫ੪ฎLinkedHashMap)...
ᶋݶྍ

![三歪教你学Java集合(1) 第104页插图](../assets/images/三歪教你学Java集合(1)_p104_1_65dadde3.png)

---

௔ᚆྲHashSet૧ӞӶӶ҅ࢩԅᥝᖌಷӞӻ݌ݻ᱾ᤒ
ڡত਻ᰁӨᬽդ෫ى҅LinkedHashSetᬽդጱฎ݌ݻ᱾ᤒ
ࢥ̵Setᵞݳ௛ᕮ
 
ݢզஉกดࣈ፡ک҅Setᵞݳጱବ੶੪ฎMap҅ಅզ౯᮷ဌํ؉ॡग़ጱړຉࣁӤᶎ҅ԞဌՋԍঅړຉጱ
ԧ̶
ӥᶎ௛ᕮӞӥSetᵞݳଉአጱӣӻৼᔄމғ
HashSetғ
෫ଧ҅꧋ᦜԅnull҅ବ੶ฎHashMap(වڜᤒ+ᕁἓ໅)҅ᶋᕚᑕݶྍ
TreeSetғ
ํଧ҅ӧ꧋ᦜԅnull҅ବ੶ฎTreeMap(ᕁἓ໅),ᶋᕚᑕݶྍ
LinkedHashSetғ
ᬽդํଧ҅꧋ᦜԅnull҅ବ੶ฎHashMap+݌ݻ᱾ᤒ҅ᶋᕚᑕݶྍ
՗ᕮᦞᘒ᥺౯ժ੪ݢզ໑ഝᛔ૩ጱਫᴬఘ٭๶ֵአԧ̶

![三歪教你学Java集合(1) 第105页插图](../assets/images/三歪教你学Java集合(1)_p105_1_3c233a1a.jpeg)

![三歪教你学Java集合(1) 第105页插图](../assets/images/三歪教你学Java集合(1)_p105_2_c50146be.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
܈̵CopyOnWriteArrayList
 
 
CopyWriteOn ݢᚆय़ਹ੒ᬯӻದ๞ྲ᫾ᴲኞމ҅֕ᬯᶱದ๞ฎꂁग़ଫአ࣋วጱ̶ᴻԧӤ෈ಅ᧔ጱ
Linux̵෈կᔮᕹक़ٌ҅ਫࣁJavaԞํٌ᫝୽̶
य़ਹ੒ᕚᑕਞق਻࢏ݢᚆ๋ᆧఀጱ੪ฎConcurrentHashMapԧ҅ࢩԅᬯӻ਻࢏ᕪଉտࣁᶎᦶጱ෸ײᘍ
ັ̶
ྲই᧔҅Ӟӻଉᥠጱᶎᦶ࣋วғ
ᶎᦶਥᳯғ“HashMapฎᕚᑕਞقጱހҘইຎHashMapᕚᑕӧਞقጱᦾ҅ᮎํဌํਞقጱMap਻
࢏”
3yғ“ᕚᑕਞقጱMapํӷӻ҅ӞӻฎHashtable҅ӞӻฎConcurrentHashMap”
ᶎᦶਥᖀᖅᳯғ“ᮎHashtable޾ConcurrentHashMapํՋԍ܄ڦࠡҘ”
3yғ“balabalabalabalabalabala"
ᶎᦶਥғ”ok,ok,ok,፡֦JavaचᏐꂁӧᲙጱޚ“
ᮎইຎํᬯ໏ጱᶎᦶޫҘ
ᶎᦶਥᳯғ“ArrayListฎᕚᑕਞقጱހҘইຎArrayListᕚᑕӧਞقጱᦾ҅ᮎํဌํਞقጱᔄ֒
ArrayListጱ਻࢏”
3yғ“ᕚᑕਞقጱArrayList౯ժݢզֵአVector҅౲ᘏ᧔౯ժݢզֵአCollectionsӥጱොဩ๶۱ᤰ
Ӟӥ”
ᶎᦶਥᖀᖅᳯғ“ࡧ҅౯ፘמ֦ԞᎣ᭲VectorฎӞӻྲ᫾ᘌጱ਻࢏ԧ҅ᬮํဌํٌ՜ጱޫҘ”
3yғ“Emmmm,ᬯӻ...“
ᶎᦶਥ൉ᐏғ“੪ྲইJUCӾํConcurrentHashMap҅ᮎJUCӾํᔄ֒"ArrayList"ጱᕚᑕਞق਻࢏
ᔄހҘ“
3yғ“Emmmm,ᬯӻ...“
ᶎᦶਥғ”ok,ok,ok,Քॠጱᶎᦶ෸ᳵԞ૧ӧग़ԧ֦҅ࢧ݄ᒵ᭗Ꭳމ̶“
ՔॠԆᥝᦖᥴጱฎCopyOnWriteArrayList~
๜෈ێ࿢ᓌܔᦖႴྯӻᎣᦩᅩ҅૶๕य़ਹ፡ਠᚆํಅත឴
Ӟ̵Vector޾SynchronizedList
 
1.1ࢧᶶᕚᑕਞقጱVector޾SynchronizedList
 
౯ժᎣ᭲ArrayListฎአԭ๊դVectorጱ҅Vectorฎᕚᑕਞقጱ਻࢏̶ࢩԅਙپԒࣁྯӻොဩ्ก॒᮷ے
ԧsynchronizedىᲫਁ๶ֵ਻࢏ਞق̶

---

ইຎֵአCollections.synchronizedList(new ArrayList()) ๶ֵArrayListݒ౮ฎᕚᑕਞقጱ
ᦾ҅ԞฎپԒ᮷ฎྯӻොဩ᮷ےӤsynchronizedىᲫਁጱ҅ݝӧᬦਙӧฎےࣁොဩጱ्ก॒҅ᘒฎොဩ
ጱٖ᮱̶
1.2Vector޾SynchronizedListݢᚆտڊሿጱᳯ᷌
 
ࣁᦖᥴCopyOnWrite਻࢏ԏڹ҅౯ժᬮฎض๶፡Ӟӥᕚᑕਞق਻࢏ጱӞԶݢᚆဌํဳ఺کጱࣈො~
ӥᶎ౯ժፗള๶፡ӞӥᬯྦྷդᎱғ

![三歪教你学Java集合(1) 第107页插图](../assets/images/三歪教你学Java集合(1)_p107_1_cb758ba4.png)

![三歪教你学Java集合(1) 第107页插图](../assets/images/三歪教你学Java集合(1)_p107_2_1fc2aa9e.png)

---

զ౯ժᒫӞݍଫ๶ړຉӞӥӤᶎӷӻොဩғࣁग़ᕚᑕሾहӥ҅ฎވํᳯ᷌Ҙ
౯ժݢզᎣ᭲ጱฎVectorጱsize()޾get()զ݊remove() ᮷ᤩsynchronizedץ᷶ጱ̶
ᒼໜғ՗᧣አᘏጱ᥯ଶฎํᳯ᷌ጱ
౯ժݢզٟྦྷդᎱၥᦶӞӥғ
    // ஑کVector๋ݸӞӻزᔰ
    public static Object getLast(Vector list) {
        int lastIndex = list.size() - 1;
        return list.get(lastIndex);
    }
 
    // ڢᴻVector๋ݸӞӻزᔰ
    public static void deleteLast(Vector list) {
        int lastIndex = list.size() - 1;
        list.remove(lastIndex);
    }
 
import java.util.Vector;
 
public class UnsafeVectorHelpers {
 
 
    public static void main(String[] args) {
 
        // ڡত۸Vector
        Vector<String> vector = new Vector();
        vector.add("ىဳلռݩ");
        vector.add("Java3y");
        vector.add("ԣLinuxݢک౯ӥᶎጱ᱾ള҅Ձݑ๋֗հ");
        vector.add("ᕳ3yےểᚹ");
 
        new Thread(() -> getLast(vector)).start();
        new Thread(() -> deleteLast(vector)).start();
        new Thread(() -> getLast(vector)).start();
        new Thread(() -> deleteLast(vector)).start();
    }
 
    // ஑کVector๋ݸӞӻزᔰ
    public static Object getLast(Vector list) {
        int lastIndex = list.size() - 1;
        return list.get(lastIndex);
    }
 
    // ڢᴻVector๋ݸӞӻزᔰ
    public static void deleteLast(Vector list) {

---

ݢզݎሿጱฎ҅ํݢᚆտಲڊ୑ଉጱғ
ܻࢩԞஉᓌܔ҅౯ժᆙ፳ၞᑕᩳӞӥ੪অԧғ
ᕚᑕAಗᤈgetLast() ොဩ҅ᕚᑕBಗᤈdeleteLast() ොဩ
ᕚᑕAಗᤈint lastIndex = list.size() - 1; ஑کlastIndexጱ꧊ฎ3̶ݶ෸҅ᕚᑕBಗ
ᤈint lastIndex = list.size() - 1; ஑کጱlastIndexጱ꧊Ԟฎ3
ྌ෸ᕚᑕBض஑کCPUಗᤈ๦҅ಗᤈlist.remove(lastIndex) ਖ਼ӥຽԅ3ጱزᔰڢᴻԧ
ള፳ᕚᑕA஑کCPUಗᤈ๦҅ಗᤈlist.get(lastIndex); ҅ݎሿ૪ᕪဌํӥຽԅ3ጱزᔰ҅ಲڊ
୑ଉԧ.
ڊሿᬯӻᳯ᷌ጱܻࢩԞஉᓌܔғ
getLast() ޾deleteLast() ᬯӷӻොဩଚӧฎܻৼ௔ጱ҅ܨֵ՜ժٖ᮱ጱྯӞྍ඙֢ฎܻৼ௔
ጱ(ᤩSynchronizeץ᷶੪ݢզਫሿܻৼ௔)҅֕ฎٖ᮱ԏᳵᬮฎݢզԻ๊ಗᤈ̶
ᬯ᯾ጱ఺௏੪ฎғ size()޾get()զ݊remove() ᮷ฎܻৼ௔ጱ҅֕ฎইຎଚݎಗ
ᤈgetLast() ޾deleteLast() ҅ොဩ᯾ᶎጱsize()޾get()զ݊remove() ฎݢզԻ๊ಗ
ᤈጱ̶
ᥝᥴ٬Ӥᶎᬯᐿఘ٭Ԟஉᓌܔ҅ࢩԅ౯ժ᮷ฎ੒Vectorᬰᤈ඙֢ጱ҅ݝᥝ඙֢Vectorڹ಩ਙᲁ֘੪ဌྷ
የԧѺ
ಅզ౯ժݢզද౮ᬯ໏ৼғ
        int lastIndex = list.size() - 1;
        list.remove(lastIndex);
    }
}
 
    // ஑کVector๋ݸӞӻزᔰ
    public static Object getLast(Vector list) {
        synchronized (list) {
            int lastIndex = list.size() - 1;
            return list.get(lastIndex);

![三歪教你学Java集合(1) 第109页插图](../assets/images/三歪教你学Java集合(1)_p109_1_efa5c9c1.png)

![三歪教你学Java集合(1) 第109页插图](../assets/images/三歪教你学Java集合(1)_p109_2_0c90d84f.png)

---

ps:ইຎํՈ݄ၥᦶӞӥ҅ݎሿտಲڊ୑ଉjava.lang.ArrayIndexOutOfBoundsException: -1҅ᬯ
ฎဌํ༄ັ᥯ຽጱ୑ଉ҅ӧฎଚݎ੕ᛘጱᳯ̶᷌
ᕪᬦӤᶎጱֺৼ౯ժݢզ፡፡ӥᶎጱդᎱғ
ݶ໏ࣈғইຎࣁ᭭ܲVectorጱ෸ײ҅ํڦጱᕚᑕץදԧVectorጱᳩଶ҅ᮎᬮฎտํᳯ᷌Ѻ
ᕚᑕA᭭ܲVector҅ಗᤈvector.size() ෸҅ݎሿVectorጱᳩଶԅ5
ྌ෸உํݢᚆਂࣁᕚᑕB੒Vectorᬰᤈclear() ඙֢
ᵋݸᕚᑕAಗᤈvector.get(i) ෸҅ಲڊ୑ଉ
ࣁJDK5զݸ҅Javaവគֵአfor-each (ᬽդ࢏)๶᭭ܲ౯ժጱᵞݳ҅অ॒੪ฎᓌ၄̵හᕟᔱ୚ጱᬟኴ꧊
ݝᦇᓒӞ̶ེ
ইຎֵአfor-each (ᬽդ࢏)๶؉Ӥᶎጱ඙֢҅տಲڊConcurrentModificationException୑ଉ
        }
    }
    // ڢᴻVector๋ݸӞӻزᔰ
    public static void deleteLast(Vector list) {
        synchronized (list) {
            int lastIndex = list.size() - 1;
            list.remove(lastIndex);
        }
    }
 
    public static void main(String[] args) {
 
        // ڡত۸Vector
        Vector<String> vector = new Vector();
        vector.add("ىဳلռݩ");
        vector.add("Java3y");
        vector.add("ԣLinuxݢک౯ӥᶎጱ᱾ള҅Ձݑ๋֗հ");
        vector.add("ᕳ3yےểᚹ");
 
        // ᭭ܲVector
        for (int i = 0; i < vector.size(); i++) {
 
            // ྲইࣁᬯಗᤈvector.clear();
            //new Thread(() -> vector.clear()).start();
 
            System.out.println(vector.get(i));
        }
    }

![三歪教你学Java集合(1) 第110页插图](../assets/images/三歪教你学Java集合(1)_p110_1_71365a6d.png)

---

SynchronizedListࣁֵአᬽդ࢏᭭ܲጱ෸ײݶ໏տํᳯ᷌ጱ҅რᎱ૪ᕪ൉ᯯ౯ժᥝಋۖےᲁԧ̶
ইຎమᥝਠᗦᥴ٬Ӥᶎಅᦖጱᳯ᷌҅౯ժݢզࣁ᭭ܲڹےᲁғ
ํᕪḵጱݶ਍੪ݢզᎣ᭲ғߡ҅᭭ܲӞӥ਻࢏᮷ᥝ౯ےӤᲁ҅ᬯᬯᬯӧฎᥝౌྒԧހ.ጱᏟฎꂁౌጱ..
ಅզ౯ժጱCopyOnWriteArrayList੪ጭ࣋ԧѺ
ԫ̵CopyOnWriteArrayList(Set)Օᕨ
 
Ӟᛱ๶᧔҅౯ժտᦊԅғCopyOnWriteArrayListฎݶྍListጱ๊դߝ҅CopyOnWriteArraySetฎݶྍ
Setጱ๊դߝ̶
෫ᦞฎHashtable-->ConcurrentHashMap҅ᬮฎ᧔Vector-->CopyOnWriteArrayList̶JUCӥඪ೮ଚݎ
ጱ਻࢏ӨᘌӞդጱᕚᑕਞقᔄፘྲ҅௛ᕮ᩸๶੪ฎےᲁᔉଶጱᳯ᷌
Hashtable̵Vectorےᲁጱᔉଶय़(ፗളࣁොဩ्กֵ॒አsynchronized)
ConcurrentHashMap̵CopyOnWriteArrayListےᲁᔉଶੜ(አݱᐿጱොୗ๶ਫሿᕚᑕਞق҅ྲই
౯ժᎣ᭲ጱConcurrentHashMapአԧcasᲁ̵volatileᒵොୗ๶ਫሿᕚᑕਞق..)
JUCӥጱᕚᑕਞق਻࢏ࣁ᭭ܲጱ෸ײӧտಲڊConcurrentModificationException୑ଉ
ಅզӞᛱ๶᧔҅౯ժ᮷տֵአJUC۱ӥᕳ౯ժ൉׀ጱᕚᑕਞق਻࢏҅ᘒӧฎֵአᘌӞդጱᕚᑕਞق਻
࢏̶
    // ᭭ܲVector
    synchronized (vector) {
            for (int i = 0; i < vector.size(); i++) {
                vector.get(i);
            }
        }

![三歪教你学Java集合(1) 第111页插图](../assets/images/三歪教你学Java集合(1)_p111_1_39c428d6.png)

![三歪教你学Java集合(1) 第111页插图](../assets/images/三歪教你学Java集合(1)_p111_2_7966ded5.png)

---

ӥᶎ౯ժ๶፡፡CopyOnWriteArrayListฎெԍਫሿጱ҅ԅՋԍֵአᬽդ࢏᭭ܲጱ෸ײ੪ӧአ᷐क़ےᲁ҅
ԞӧտಲڊConcurrentModificationException୑ଉ̶
2.1CopyOnWriteArrayListਫሿܻቘ
 
౯ժᬮฎض๶ࢧᶶӞӥCOWғ
ইຎํग़ӻ᧣አᘏҁcallers҂ݶ෸᧗࿢ፘݶᩒრҁইٖਂ౲ᏺፏӤጱහഝਂؙ҂҅՜ժտوݶ឴
ݐፘݶጱ೰ᰒ೰ݻፘݶጱᩒრ҅ፗک຤ӻ᧣አᘏᦶࢶץදᩒრጱٖ਻෸҅ᔮᕹ಍տ፥ྋ॔ګӞղ
ӫአۅ๜ҁprivate copy҂ᕳᧆ᧣አᘏ҅ᘒٌ՜᧣አᘏಅᥠکጱ๋ڡጱᩒრՖᆐכ೮ӧݒ̶սᅩฎ
ইຎ᧣አᘏဌํץදᧆᩒრ҅੪ӧտํۅ๜ҁprivate copy҂ᤩୌᒈ҅ࢩྌग़ӻ᧣አᘏݝฎ᧛ݐ඙
֢෸ݢզوՁݶӞղᩒრ̶
݇ᘍᛔᖌचጯ
ᑀғhttps://zh.wikipedia.org/wiki/%E5%AF%AB%E5%85%A5%E6%99%82%E8%A4%87%E8%A3%B
D
ԏڹٟܗਮጱ෸ײ҅ইຎฎᥝ፡რᎱ҅ӞᛱտᘉᦲӞӥრᎱጱဳ᯽ଚአࢶᩂࣁ෈ᒍӤጱ̶
Emmm҅ݎሿᴅ᧛֛ḵଚӧฎஉঅ҅ಅզ౯ᬯ᯾੪ፗള༷ೡӞӥრᎱဳ᯽᧔ԧՋԍމ̶ݚक़҅ই
ຎֵአIDEAጱᦾ҅ݢզӥӞӻൊկTranslation(عᩇঅአ).

![三歪教你学Java集合(1) 第112页插图](../assets/images/三歪教你学Java集合(1)_p112_1_9900912c.png)

![三歪教你学Java集合(1) 第112页插图](../assets/images/三歪教你学Java集合(1)_p112_2_81a8a611.png)

---

༷ೡӞӥCopyOnWriteArrayListრᎱဳ᯽ՕᕨԧՋԍғ
CopyOnWriteArrayListฎᕚᑕਞق਻࢏(ፘ੒ԭArrayList)҅ବ੶᭗ᬦ॔ګහᕟጱොୗ๶ਫሿ̶
CopyOnWriteArrayListࣁ᭭ܲጱֵአӧտಲڊConcurrentModificationException୑ଉ҅ଚӬ᭭ܲ
ጱ෸ײ੪ӧአ᷐क़ےᲁ
زᔰݢզԅnull
2.1.1፡ӞӥCopyOnWriteArrayListच๜ጱᕮ຅
 
፡᩸๶ꂁᓌܔጱ҅CopyOnWriteArrayListବ੶੪ฎහᕟ҅ےᲁ੪ԻኧReentrantLock๶ਠ౮̶
2.1.2ଉᥠොဩጱਫሿ
 
 
໑ഝӤᶎጱړຉ౯ժᎣ᭲ইຎ᭭ܲVector/SynchronizedList ฎᵱᥝᛔ૩ಋۖےᲁጱ̶
CopyOnWriteArrayListֵአᬽդ࢏᭭ܲ෸ӧᵱᥝดᐏےᲁ҅፡፡add()̵clear()̵remove()
Ө get() ොဩጱਫሿݢᚆ੪ํᅩ፠ፓԧ̶
Ḓض౯ժݢզ፡፡add() ොဩ
    /** ݢ᯿فᲁ੒᨝ */
    final transient ReentrantLock lock = new ReentrantLock();
 
    /** CopyOnWriteArrayListବ੶ኧහᕟਫሿ҅volatileץ᷶ */
    private transient volatile Object[] array;
 
    /**
     * ஑کහᕟ
     */
    final Object[] getArray() {
        return array;
    }
 
    /**
     * ᦡᗝහᕟ
     */
    final void setArray(Object[] a) {
        array = a;
    }
 
    /**
     * ڡত۸CopyOnWriteArrayListፘ୮ԭڡত۸හᕟ
     */
    public CopyOnWriteArrayList() {
        setArray(new Object[0]);
    }
    public boolean add(E e) {

---

᭗ᬦդᎱ౯ժݢզᎣ᭲ғࣁႲےጱ෸ײ੪Ӥᲁ҅ଚ॔ګӞӻෛහᕟ҅ीے඙֢ࣁෛහᕟӤਠ౮҅ਖ਼
array೰ݻکෛහᕟӾ๋҅ݸᥴᲁ̶
ٚ๶፡፡size() ොဩғ
ٚ๶፡፡get() ොဩғ
ᮎٚ๶፡፡set() ොဩ
    
    // ےᲁ
        final ReentrantLock lock = this.lock;
        lock.lock();
        try {
      
      // ஑کܻහᕟጱᳩଶ޾زᔰ
            Object[] elements = getArray();
            int len = elements.length;
      
      // ॔ګڊӞӻෛහᕟ
            Object[] newElements = Arrays.copyOf(elements, len + 1);
      
      // Ⴒے෸҅ਖ਼ෛزᔰႲےکෛහᕟӾ
            newElements[len] = e;
      
      // ਖ਼volatile Object[] array ጱ೰ݻ๊ഘ౮ෛහᕟ
            setArray(newElements);
            return true;
        } finally {
            lock.unlock();
        }
    }
 
  public int size() {
 
    // ፗള஑کarrayහᕟጱᳩଶ
        return getArray().length;
    }
 
    public E get(int index) {
        return get(getArray(), index);
    }
 
  final Object[] getArray() {
        return array;
    }

---

੒ԭ remove()̵clear() ᪙set()޾add() ฎᔄ֒ጱ҅ᬯ᯾౯੪ӧٚᩂڊդᎱԧ̶
௛ᕮғ
ࣁץද෸҅॔ګڊӞӻෛහᕟ҅ץදጱ඙֢ࣁෛහᕟӾਠ౮๋҅ݸਖ਼ෛහᕟԻኧarrayݒᰁ೰ݻ̶
ٟےᲁ҅᧛ӧےᲁ
2.1.3ڽຉԅՋԍ᭭ܲ෸ӧአ᧣አᘏดୗےᲁ
 
ଉአጱොဩਫሿ౯ժ૪ᕪच๜ԧᥴԧ҅֕ᬮฎӧᎣ᭲ԅࠨᚆड़ࣁ਻࢏᭭ܲጱ෸ײ੒ٌᬰᤈץදᘒӧಲڊ
୑ଉ̶ಅզ҅๶፡Ӟӥ՜ጱᬽդ࢏މғ
public E set(int index, E element) {
  final ReentrantLock lock = this.lock;
  lock.lock();
  try {
    
    // ஑کܻහᕟጱ෯꧊
    Object[] elements = getArray();
    E oldValue = get(elements, index);
 
    // ڣෙෛ꧊޾෯꧊ฎވፘᒵ
    if (oldValue != element) {
      
      // ॔ګෛහᕟ҅ෛ꧊ࣁෛහᕟӾਠ౮
      int len = elements.length;
      Object[] newElements = Arrays.copyOf(elements, len);
      newElements[index] = element;
      
      // ਖ਼array୚አ೰ݻෛහᕟ
      setArray(newElements);
    } else {
      // Not quite a no-op; enssures volatile write semantics
      setArray(elements);
    }
    return oldValue;
  } finally {
    lock.unlock();
  }
}
 
 
  // 1. ᬬࢧጱᬽդ࢏ฎCOWIterator
  public Iterator<E> iterator() {
        return new COWIterator<E>(getArray(), 0);
    }

---

کᬯ᯾҅౯ժଫᧆ੪ݢզమกጮԧѺCopyOnWriteArrayListࣁֵአᬽդ࢏᭭ܲጱ෸ײ҅඙֢ጱ᮷ฎܻහ
ᕟѺ
2.1.4CopyOnWriteArrayListᗌᅩ
 
፡ԧӤᶎጱਫሿრᎱ҅౯ժଫᧆԞय़༷ᚆړຉڊCopyOnWriteArrayListጱᗌᅩԧ̶
ٖਂܛአғইຎCopyOnWriteArrayListᕪଉᥝीڢද᯾ᶎጱහഝ҅ᕪଉᥝಗᤈadd()̵set()̵
remove() ጱᦾ҅ᮎฎྲ᫾ᘙᩇٖਂጱ̶
ࢩԅ౯ժᎣ᭲ྯེadd()̵set()̵remove() ᬯԶीڢද඙֢᮷ᥝ॔ګӞӻහᕟڊ๶̶
හഝӞᛘ௔ғCopyOnWrite਻࢏ݝᚆכᦤහഝጱ๋ᕣӞᛘ௔҅ӧᚆכᦤහഝጱਫ෸Ӟᛘ௔̶
՗ӤᶎጱֺৼԞݢզ፡ڊ๶҅ྲইᕚᑕAࣁᬽդCopyOnWriteArrayList਻࢏ጱහഝ̶ᕚᑕBࣁ
ᕚᑕAᬽդጱᳵᵐӾਖ਼CopyOnWriteArrayList᮱ړጱහഝץදԧ(૪ᕪ᧣አsetArray() ԧ)̶
֕ฎᕚᑕAᬽդڊ๶ጱฎܻํጱහഝ̶
  // 2. ᬽդ࢏ጱ౮ާં௔
    private final Object[] snapshot;
    private int cursor;
 
  // 3. ᬽդ࢏ጱ຅᭜ොဩ
  private COWIterator(Object[] elements, int initialCursor) {
        cursor = initialCursor;
        snapshot = elements;
    }
 
  // 4. ᬽդ࢏ጱොဩ...
  public E next() {
        if (! hasNext())
            throw new NoSuchElementException();
        return (E) snapshot[cursor++];
    }
 
  //.... ݢզݎሿጱฎ҅ᬽդ࢏ಅํጱ඙֢᮷चԭsnapshotහᕟ҅ᘒsnapshotฎփ᭓ᬰ๶ጱarrayහ
ᕟ

![三歪教你学Java集合(1) 第116页插图](../assets/images/三歪教你学Java集合(1)_p116_1_66f68598.png)

---

2.1.5CopyOnWriteSet
 
CopyOnWriteArraySetጱܻቘ੪ฎCopyOnWriteArrayList̶
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
܈Ӟ̵Javaᵞݳᶎᦶ᷌
 
 
Java਻࢏ݢړԅӷय़ᔄғ
Collection
    private final CopyOnWriteArrayList<E> al;
 
    public CopyOnWriteArraySet() {
        al = new CopyOnWriteArrayList<E>();
    }

![三歪教你学Java集合(1) 第117页插图](../assets/images/三歪教你学Java集合(1)_p117_1_3c233a1a.jpeg)

![三歪教你学Java集合(1) 第117页插图](../assets/images/三歪教你学Java集合(1)_p117_2_a6d9076a.jpeg)

---

List
ArrayList
LinkedList
Vector(ԧᥴ҅૪ᬦ෸)
Set
HashSet
LinkedHashSet
TreeSet
Map
HashMap
LinkedHashMap
TreeMap
ConcurrentHashMap
Hashtable(ԧᥴ҅҅૪ᬦ෸)
፳᯿ຽڊጱᮎԶ੪ฎ౯ժአ஑๋ग़ጱ਻࢏̶
 
Ӟ̵ArrayList޾Vectorጱ܄ڦ
 
وݶᅩғ
ᬯӷӻᔄ᮷ਫሿԧListളݗ҅ਙժ᮷ฎํଧጱᵞݳ(ਂؙํଧ)҅ବ੶ฎහᕟ̶౯ժݢզೲ֖ᗝᔱ୚
ݩݐڊ຤ӻزᔰ҅꧋ᦜزᔰ᯿॔޾ԅnull̶
܄ڦғ
ݶྍ௔ғ
ArrayListฎᶋݶྍጱ
Vectorฎݶྍጱ
ܨ׎ᵱᥝݶྍጱ෸ײ҅౯ժݢզֵአCollectionsૡٍᔄ๶຅ୌڊݶྍጱArrayListᘒӧአ
Vector
ಘ਻य़ੜғ
Vectorीᳩܻ๶ጱӞ׭҅ArrayListीᳩܻ๶ጱ0.5׭
ԫ̵HashMap޾Hashtableጱ܄ڦ
 
وݶᅩғ
՗ਂؙᕮ຅޾ਫሿ๶ᦖच๜Ӥ᮷ฎፘݶጱ҅᮷ฎਫሿMapളݗ~
܄ڦғ
ݶྍ௔ғ
HashMapฎᶋݶྍጱ
Hashtableฎݶྍጱ

---

ᵱᥝݶྍጱ෸ײ҅౯ժஃஃӧֵአ҅ᘒֵአConcurrentHashMapConcurrentHashMapचԭ
JDK1.8რᎱڽຉ
ฎވ꧋ᦜԅnullғ
HashMap꧋ᦜԅnull
Hashtableӧ꧋ᦜԅnull
containsොဩ
ᬯᎣᦩᅩฎࣁᇍਮᗑڬکጱ҅ဌమکᬯᐿ᷌ᬮտํ(౯ӧॡࡅཻ)....
Hashtableํcontainsොဩ
HashMap಩Hashtableጱcontainsොဩ݄ധԧ҅ද౮ԧcontainsValue޾containsKey
ᖀಥӧݶғ
HashMap<K,V> extends AbstractMap<K,V>
public class Hashtable<K,V> extends Dictionary<K,V>
ӣ̵List޾Mapጱ܄ڦ
 
وݶᅩғ
᮷ฎJavaଉአጱ਻࢏҅᮷ฎളݗ(psғٟڊ๶ఽᥧঅ؟޾ဌٟӞ໏.....)
ӧݶᅩғ
ਂؙᕮ຅ӧݶғ
Listฎਂؙܔڜጱᵞݳ
Mapਂؙጱฎkey-valueᲫ꧊੒ጱᵞݳ
زᔰฎވݢ᯿॔ғ
List꧋ᦜزᔰ᯿॔
Mapӧ꧋ᦜkey᯿॔
ฎވํଧғ
Listᵞݳฎํଧጱ(ਂؙํଧ)
Mapᵞݳฎ෫ଧጱ(ਂؙ෫ଧ)
ࢥ̵Set᯾ጱزᔰฎӧᚆ᯿॔ጱ҅ᮎԍአՋԍොဩ๶܄ړ᯿
॔Өވޫ? ฎአ==ᬮฎequals()?
 
౯ժᎣ᭲Setᵞݳਫᴬय़᮷ֵአጱฎMapᵞݳጱputොဩ๶Ⴒےزᔰ̶
զHashSetԅֺ҅HashSet᯾ጱزᔰӧᚆ᯿॔҅ࣁრᎱ(HashMap)ฎᬯ໏֛ሿጱғ

---

Ⴒےزᔰጱ෸ײ҅ইຎkey(Ԟ੒ଫጱSetᵞݳጱزᔰ)ፘᒵ҅ᮎԍڞץදvalue꧊̶ᘒࣁSetᵞݳӾ҅value
꧊ՐՐฎӞӻObject੒᨝ᗙԧ(ᧆ੒᨝੒Set๜᫝ᘒ᥺ฎ෫አጱ)̶
Ԟ੪ฎ᧔ғSetᵞݳইຎႲےጱزᔰፘݶ෸҅ฎ໑๜ဌํൊفጱ(ՐץදԧӞӻ෫አጱvalue꧊)Ѻ՗რᎱ
(HashMap)ӾԞ፡ڊ๶҅==޾equals()ොဩ᮷ํֵአѺ
Բ̵Collection޾Collectionsጱ܄ڦ
 
1. CollectionฎᵞݳጱӤᕆളݗ҅ᖀಥਙጱํSet޾Listളݗ
2. Collectionsฎᵞݳጱૡٍᔄ҅൉׀ԧӞᔮڜጱᶉாොဩ੒ᵞݳጱ൤ᔱ̵ັತ̵ݶྍᒵ඙֢
م̵᧔ڊArrayList,LinkedListጱਂؙ௔ᚆ޾ᇙ௔
 
ArrayListጱବ੶ฎහᕟ҅LinkedListጱବ੶ฎ݌ݻ᱾ᤒ̶
ArrayListਙඪ೮զ᥯ຽ֖ᗝᬰᤈᔱ୚ڊ੒ଫጱزᔰ(ᵋ๢ᦢᳯ)҅ᘒLinkedListڞᵱᥝ᭭ܲෆӻ᱾ᤒ
๶឴ݐ੒ଫጱزᔰ̶ࢩྌӞᛱ๶᧔ArrayListጱᦢᳯ᭛ଶฎᥝྲLinkedListᥝளጱ
ArrayListኧԭฎහᕟ҅੒ԭڢᴻ޾ץදᘒ᥺ၾᘙฎྲ᫾य़(॔ګ޾ᑏۖහᕟਫሿ)҅LinkedListฎ݌
ݻ᱾ᤒڢᴻ޾ץදݝᵱᥝץද੒ଫጱ೰ᰒܨݢ҅ၾᘙฎஉੜጱ̶ࢩྌӞᛱ๶᧔LinkedListጱीڢ
᭛ଶฎᥝྲArrayListᥝளጱ
6.1ಘ઀ғ
 
ArrayListጱीڢ๚஠੪ฎྲLinkedListᥝౌ̶
ইຎीڢ᮷ฎࣁ๛ੲ๶඙֢̓ྯེ᧣አጱ᮷ฎremove()޾add()̈́҅ྌ෸ArrayList੪ӧᵱᥝᑏۖ޾
॔ګහᕟ๶ᬰᤈ඙֢ԧ̶ইຎහഝᰁํጯӡᕆጱ෸҅᭛ଶฎտྲLinkedListᥝளጱ̶(౯ၥᦶᬦ)
ইຎڢᴻ඙֢ጱ֖ᗝฎࣁӾᳵ̶ኧԭLinkedListጱၾᘙԆᥝฎࣁ᭭ܲӤ҅ArrayListጱၾᘙԆᥝฎࣁ
ᑏۖ޾॔ګӤ(ବ੶᧣አጱฎarraycopy()ොဩ҅ฎnativeොဩ)̶
LinkedListጱ᭭ܲ᭛ଶฎᥝౌԭArrayListጱ॔ګᑏۖ᭛ଶጱ
ইຎහഝᰁํጯӡᕆጱ෸҅ᬮฎArrayListᥝள̶(౯ၥᦶᬦ)
Ӡ̵Enumeration޾Iteratorളݗጱ܄ڦ
 
  
  // 1. ইຎkey ፘᒵ  
    if (p.hash == hash &&
        ((k = p.key) == key || (key != null && key.equals(k))))
        e = p;
  // 2. ץද੒ଫጱvalue
     if (e != null) { // existing mapping for key
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);
            return oldValue;
       }

---

ᬯӻ౯ࣁڹᶎጱ෈ᒍӾԞဌํᧇᕡ݄ᦖਙժ҅ݝฎय़༷Ꭳ᭲ጱฎғIterator๊դԧEnumeration҅
EnumerationฎӞӻ෯ጱᬽդ࢏ԧ̶
ӨEnumerationፘྲ҅Iteratorๅےਞق҅ࢩԅ୮Ӟӻᵞݳྋࣁᤩ᭭ܲጱ෸ײ҅ਙտᴥྊٌਙᕚᑕ݄ץ
දᵞݳ̶
౯ժࣁ؉ᕞԟጱ෸ײ҅ᬽդ෸տӧտᕪଉڊᲙ҅ಲڊConcurrentModificationException୑ଉ҅᧔
౯ժࣁ᭭ܲጱ෸ײᬮࣁץදزᔰ̶
ᬯٌਫ੪ฎfail-fast๢ګ~ٍ֛ݢ݇ᘍܗ
෈ғhttps://blog.csdn.net/panweiwei1994/article/details/77051261
܄ڦํӣᅩғ
IteratorጱොဩݷྲEnumerationๅᑀ਍
Iteratorํfail-fast๢ګ҅ྲEnumerationๅਞق
Iteratorᚆड़ڢᴻزᔰ҅Enumerationଚӧᚆڢᴻزᔰ
ك̵ListIteratorํՋԍᇙᅩ
 
ListIteratorᖀಥԧIteratorളݗ҅ਙአԭ᭭ܲListᵞݳጱزᔰ̶
ListIteratorݢզਫሿ݌ݻ᭭ܲ,Ⴒےزᔰ҅ᦡᗝزᔰ
፡ӞӥრᎱጱොဩ੪Ꭳ᭲ԧғ
Ԝ̵ଚݎᵞݳᔄฎՋԍҘ
 
Java1.5ଚݎ۱ҁjava.util.concurrent҂۱ތᕚᑕਞقᵞݳᔄ҅꧋ᦜࣁᬽդ෸ץදᵞݳ̶
Utils۱ӥጱᵞݳᬽդ࢏ᤩᦡᦇԅfail-fastጱ҅տಲڊConcurrentModificationException̶֕
java.util.concurrentጱଚӧտ҅ఽᨀᦧᦞ܄൉ᯯ~
Ӟ᮱ړᔄԅғ
CopyOnWriteArrayList
ConcurrentHashMap
CopyOnWriteArraySet

![三歪教你学Java集合(1) 第121页插图](../assets/images/三歪教你学Java集合(1)_p121_1_bc07de77.png)

---

܈̵JavaӾHashMapጱkey꧊ᥝฎԅᔄ੒᨝ڞᧆᔄᵱᥝჿ
᪃Ջԍ๵կҘ
 
ᵱᥝݶ෸᯿ٟᧆᔄጱhashCode()ොဩ޾ਙጱequals()ොဩ̶
՗რᎱݢզ஑Ꭳ҅ࣁൊفزᔰጱ෸ײฎضᓒڊᧆ੒᨝ጱhashCode̶ইຎhashcodeፘᒵᦾጱ̶ᮎ
ԍᤒกᧆ੒᨝ฎਂؙࣁݶӞӻ֖ᗝӤጱ̶
ইຎ᧣አequals()ොဩ҅ӷӻkeyፘݶ҅ڞ๊ഘزᔰ
ইຎ᧣አequals()ොဩ҅ӷӻkeyӧፘݶ҅ڞ᧔กᧆhashCodeՐՐฎᏳૣፘݶ҅ྌ෸ฎවڜ٫
ᑱ҅ਖ਼ෛीጱزᔰනࣁ໲ৼӤ
Ӟᛱ๶᧔҅౯ժտᦊԅғݝᥝӷӻ੒᨝ጱ౮ާݒᰁጱ꧊ฎፘᒵጱ҅ᮎԍ౯ժ੪ᦊԅᬯӷӻ੒᨝ฎፘᒵ
ጱѺࢩԅ҅Objectବ੶ྲ᫾ጱฎӷӻ੒᨝ጱࣈ࣎҅ᘒ੒౯ժ୏ݎ๶᧔ᬯ໏ጱ఺Ԏଚӧय़~ᬯԞ੪ԅՋԍ
౯ժᥝ᯿ٟ equals() ොဩ
᯿ٟԧequals()ොဩ҅੪ᥝ᯿ٟhashCode()ጱොဩ̶ࢩԅequals()ᦊਧԧᬯӷӻ੒᨝ፘݶ҅ᘒݶӞӻ੒
᨝᧣አhashCode()ොဩ෸҅ฎଫᧆᬬࢧፘݶጱ꧊ጱѺ
 
܈Ӟ̵ӨJavaᵞݳ໛ຝፘىጱํߺԶ๋অጱਫ᪢
 
1. ໑ഝᵱᥝᏟਧᵞݳጱᔄ̶ࣳইຎฎܔڜጱᵞݳ҅౯ժᘍᡤአCollectionӥጱৼളݗArrayList޾
Set̶ইຎฎฉ੘҅౯ժ੪ᘍᡤֵአMap~
2. Ꮯਧਠ౯ժጱᵞݳᔄࣳ҅౯ժളӥ๶Ꮯਧֵአᧆᵞݳᔄࣳӥጱߺӻৼᔄ~౯ᦊԅݢզᓌܔړ౮پӻ
ྍṈғ
ฎވᵱᥝݶྍ
݄ತᕚᑕਞقጱᵞݳᔄֵአ
ᬽդ෸ฎވᵱᥝํଧ(ൊفᶲଧํଧ)
݄ತLinked݌ݻڜᤒᕮ຅ጱ
ฎވᵱᥝഭଧ(ᛔᆐᶲଧ౲ᘏಋۖഭଧ)
݄ತTreeᕁἓ໅ᔄࣳጱ(JDK1.8) 
3. ֌ᓒਂනᵞݳጱහഝᰁํग़य़҅෫ᦞฎListᬮฎMap҅ਙժਫሿۖாीᳩ҅᮷ฎํ௔ᚆၾᘙጱ̶ࣁ
ڡতᵞݳጱ෸ײᕳڊӞӻݳቘጱ਻ᰁտٺ੝ۖாीᳩ෸ጱၾᘙ~
4. ֵአာࣳ҅᭿عࣁᬩᤈ෸ڊሿClassCastException
5. ੱݢᚆֵአCollectionsૡٍᔄ҅౲ᘏ឴ݐݝ᧛̵ݶྍ౲ᑮጱᵞݳ҅ᘒᶋᖫٟᛔ૩ጱਫሿ̶ਙਖ਼տ
൉׀դᎱ᯿አ௔҅ਙํ፳ๅঅጱᑞਧ௔޾ݢᖌಷ௔
܈ԫ̵ArrayListᵞݳےف1ӡ๵හഝ҅ଫᧆெԍ൉ṛපሲ 
ArrayListጱἕᦊڡত਻ᰁԅ10҅ᥝൊفय़ᰁහഝጱ෸ײᵱᥝӧෙಘ਻҅ᘒಘ਻ฎᶋଉ୽ߥ௔ᚆጱ̶ࢩ
ྌ҅ሿࣁกᏟԧ10ӡ๵හഝԧ҅౯ժݢզፗളࣁڡত۸ጱ෸ײ੪ᦡᗝArrayListጱ਻ᰁѺ
ᬯ໏੪ݢզ൉ṛපሲԧ~

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y

![三歪教你学Java集合(1) 第123页插图](../assets/images/三歪教你学Java集合(1)_p123_1_b6d2079a.jpeg)

![三歪教你学Java集合(1) 第123页插图](../assets/images/三歪教你学Java集合(1)_p123_2_3c233a1a.jpeg)