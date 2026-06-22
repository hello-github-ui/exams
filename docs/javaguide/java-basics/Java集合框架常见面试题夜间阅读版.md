---
title: Java集合框架常见面试题夜间阅读版
source: JavaGuide/Java/Java集合框架常见面试题夜间阅读版.pdf
pages: 26
converted_at: 2026-06-22 22:30:13
---

# Java集合框架常见面试题夜间阅读版

ڽຉᶎᦶ๋ଉᥠᳯ᷌ԏ Java ᵞݳ໛ຝ
 
ᵞݳ༷ᬿ
 
Java ᵞݳ༷ᥦ
 
՗ӥࢶݢզ፡ڊ҅ࣁ Java Ӿᴻԧզ Map  ᕮੲጱᔄԏक़҅ ٌ՜ᔄ᮷ਫሿԧ Collection  ളݗ̶
ଚӬ҅զ Map  ᕮੲጱᔄ᮷ਫሿԧ Map  ളݗ̶
᧔᧔ List,Set,Map ӣᘏጱ܄ڦҘ
 
List (੒՞ᶲଧጱঅଆಋ)ғ ਂؙጱزᔰฎํଧጱ̵ݢ᯿॔ጱ̶
Set (ဳ᯿ᇿӞ෫ԫጱ௔ᨶ): ਂؙጱزᔰฎ෫ଧጱ̵ӧݢ᯿॔ጱ̶
Map (አ Key ๶൤ᔱጱӫਹ): ֵአᲫ꧊੒ҁkye-value҂ਂؙ҅ᔄ֒ԭහ਍Ӥጱڍහ y=f(x)҅“x”դᤒ
key҅"y"դᤒ value҅Key ฎ෫ଧጱ̵ӧݢ᯿॔ጱ҅value ฎ෫ଧጱ̵ݢ᯿॔ጱ҅ྯӻᲫ๋ग़ฉ੘ک
Ӟӻ꧊̶
ᵞݳ໛ຝବ੶හഝᕮ຅௛ᕮ
 
ض๶፡Ӟӥ Collection  ളݗӥᶎጱᵞݳ̶
List
 
Arraylist ғ Object[] හᕟ

![Java集合框架常见面试题夜间阅读版 第1页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p1_1_eb7528ac.jpeg)

---

Vector ғ Object[] හᕟ
LinkedList ғ ݌ݻ᱾ᤒ(JDK1.6 ԏڹԅ஗ሾ᱾ᤒ҅JDK1.7 ݐၾԧ஗ሾ)
Set
 
HashSet ҁ෫ଧ҅ࠔӞ҂: चԭ HashMap  ਫሿጱ҅ବ੶᯻አ HashMap  ๶כਂزᔰ
LinkedHashSet ғ LinkedHashSet  ฎ HashSet  ጱৼᔄ҅ଚӬٌٖ᮱ฎ᭗ᬦ LinkedHashMap  ๶
ਫሿጱ̶ํᅩᔄ֒ԭ౯ժԏڹ᧔ጱ LinkedHashMap  ٌٖ᮱ฎचԭ HashMap  ਫሿӞ໏҅ӧᬦᬮฎ
ํӞᅩᅩ܄ڦጱ
TreeSet ҁํଧ҅ࠔӞ҂ғ ᕁἓ໅(ᛔଘᤍጱഭଧԫ݉໅)
ٚ๶፡፡ Map  ളݗӥᶎጱᵞݳ̶
Map
 
HashMap ғ JDK1.8 ԏڹ HashMap ኧහᕟ+᱾ᤒᕟ౮ጱ҅හᕟฎ HashMap ጱԆ֛҅᱾ᤒڞฎԆᥝ
ԅԧᥴ٬ߢ૶٫ᑱᘒਂࣁጱҁ“೉᱾ဩ”ᥴ٬٫ᑱ҂̶JDK1.8 զݸࣁᥴ٬ߢ૶٫ᑱ෸ํԧ᫾य़ጱݒ
۸҅୮᱾ᤒᳩଶय़ԭᴇ꧊ҁἕᦊԅ 8҂ҁਖ਼᱾ᤒ᫨ഘ౮ᕁἓ໅ڹտڣෙ҅ইຎ୮ڹහᕟጱᳩଶੜԭ
64҅ᮎԍտᭌೠضᬰᤈහᕟಘ਻҅ᘒӧฎ᫨ഘԅᕁἓ໅҂෸҅ਖ਼᱾ᤒ᫨۸ԅᕁἓ໅҅զٺ੝൤ᔱ෸
ᳵ
LinkedHashMap ғ LinkedHashMap  ᖀಥᛔ HashMap ҅ಅզਙጱବ੶Ֆᆐฎचԭ೉᱾ୗවڜᕮ຅
ܨኧහᕟ޾᱾ᤒ౲ᕁἓ໅ᕟ౮̶ݚक़҅ LinkedHashMap  ࣁӤᶎᕮ຅ጱचᏐӤ҅ीےԧӞ๵݌ݻ᱾
ᤒֵ҅஑Ӥᶎጱᕮ຅ݢզכ೮Ძ꧊੒ጱൊفᶲଧ̶ݶ෸᭗ᬦ੒᱾ᤒᬰᤈፘଫጱ඙֢҅ਫሿԧᦢᳯᶲ
ଧፘى᭦ᬋ̶ᧇᕡݢզັ፡ғ̽LinkedHashMap რᎱᧇᕡړຉҁJDK1.8҂̾
Hashtable ғ හᕟ+᱾ᤒᕟ౮ጱ҅හᕟฎ HashMap ጱԆ֛҅᱾ᤒڞฎԆᥝԅԧᥴ٬ߢ૶٫ᑱᘒਂ
ࣁጱ
TreeMap ғ ᕁἓ໅ҁᛔଘᤍጱഭଧԫ݉໅҂
ই֜ᭌአᵞݳ?
 
Ԇᥝ໑ഝᵞݳጱᇙᅩ๶ᭌአ҅ྲই౯ժᵱᥝ໑ഝᲫ꧊឴ݐکزᔰ꧊෸੪ᭌአ Map  ളݗӥጱᵞݳ҅ᵱᥝ
ഭଧ෸ᭌೠ TreeMap ,ӧᵱᥝഭଧ෸੪ᭌೠ HashMap ,ᵱᥝכᦤᕚᑕਞق੪ᭌአ
ConcurrentHashMap ̶
୮౯ժݝᵱᥝਂනزᔰ꧊෸҅੪ᭌೠਫሿCollection  ളݗጱᵞݳ҅ᵱᥝכᦤزᔰࠔӞ෸ᭌೠਫሿ
Set  ളݗጱᵞݳྲই TreeSet  ౲ HashSet ҅ӧᵱᥝ੪ᭌೠਫሿ List  ളݗጱྲই ArrayList  ౲
LinkedList ҅ᆐݸٚ໑ഝਫሿᬯԶളݗጱᵞݳጱᇙᅩ๶ᭌአ̶
ԅՋԍᥝֵአᵞݳҘ
 
୮౯ժᵱᥝכਂӞᕟᔄࣳፘݶጱහഝጱ෸ײ҅౯ժଫᧆฎአӞӻ਻࢏๶כਂ҅ᬯӻ਻࢏੪ฎහᕟ҅֕
ฎֵ҅አහᕟਂؙ੒᨝ٍํӞਧጱ୕ᒒ҅ ࢩԅ౯ժࣁਫᴬ୏ݎӾ҅ਂؙጱහഝጱᔄࣳฎग़ᐿग़໏ጱ҅ԭ
ฎ҅੪ڊሿԧ“ᵞݳ”҅ᵞݳݶ໏Ԟฎአ๶ਂؙग़ӻහഝጱ̶

---

හᕟጱᗌᅩฎӞ෮्กԏݸ҅ᳩଶ੪ӧݢݒԧҔݶ෸्҅กහᕟ෸ጱහഝᔄࣳԞ٬ਧԧᧆහᕟਂؙጱහ
ഝጱᔄࣳҔᘒӬ҅හᕟਂؙጱහഝฎํଧጱ̵ݢ᯿॔ጱ҅ᇙᅩܔӞ̶ ֕ฎᵞݳ൉ṛԧහഝਂؙጱᅎၚ
௔҅Java ᵞݳӧՐݢզአ๶ਂؙӧݶᔄࣳӧݶහᰁጱ੒᨝҅ᬮݢզכਂٍํฉ੘ىᔮጱහഝ
Iterator ᬽդ࢏
 
ᬽդ࢏ Iterator ฎՋԍҘ
 
Iterator  ੒᨝ᑍԅᬽդ࢏ҁᦡᦇཛྷୗጱӞᐿ҂҅ᬽդ࢏ݢզ੒ᵞݳᬰᤈ᭭ܲ҅֕ྯӞӻᵞݳٖ᮱ጱහ
ഝᕮ຅ݢᚆฎӧੱፘݶጱ҅ಅզྯӞӻᵞݳਂ޾ݐ᮷உݢᚆฎӧӞ໏ጱ҅ᡱᆐ౯ժݢզՈԅࣈࣁྯӞӻ
ᔄӾਧԎ hasNext()  ޾ next()  ොဩ҅֕ᬯ໏؉տᦏෆӻᵞݳ֛ᔮᬦԭᛎᙠ̶ԭฎ੪ํԧᬽդ࢏̶
ᬽդ࢏ฎਖ਼ᬯ໏ጱොဩುݐڊളݗ҅ᆐݸࣁྯӻᔄጱٖ᮱҅ਧԎᛔ૩ᬽդොୗ҅ᬯ໏؉੪ᥢਧԧෆӻᵞ
ݳ֛ᔮጱ᭭ܲොୗ᮷ฎ hasNext() ޾next() ොဩֵ҅አᘏӧአᓕெԍਫሿጱ҅տአܨݢ̶ᬽդ࢏ጱ
ਧԎԅғ൉׀ӞᐿොဩᦢᳯӞӻ਻࢏੒᨝Ӿݱӻزᔰ҅ᘒ݈ӧᵱᥝูᶂᧆ੒᨝ጱٖ᮱ᕡᜓ̶
ᬽդ࢏ Iterator ํࠨአҘ
 
Iterator  Ԇᥝฎአ๶᭭ܲᵞݳአጱ҅ਙጱᇙᅩฎๅےਞق҅ࢩԅਙݢզᏟכ҅ࣁ୮ڹ᭭ܲጱᵞݳزᔰ
ᤩๅදጱ෸ײ҅੪տಲڊ ConcurrentModificationException  ୑ଉ̶
ইֵ֜አҘ
 
౯ժ᭗ᬦֵአᬽդ࢏๶᭭ܲ HashMap ҅ᄍᐏӞӥ ᬽդ࢏ Iterator ጱֵአ̶
public interface Iterator<E> {
    //ᵞݳӾฎވᬮํزᔰ
    boolean hasNext();
    //឴஑ᵞݳӾጱӥӞӻزᔰ
    E next();
    ......
}
Map<Integer, String> map = new HashMap();
map.put(1, "Java");
map.put(2, "C++");
map.put(3, "PHP");
Iterator<Map.Entry<Integer, String>> iterator = map.entrySet().iterator();
while (iterator.hasNext()) {
  Map.Entry<Integer, String> entry = iterator.next();
  System.out.println(entry.getKey() + entry.getValue());
}

---

ํߺԶᵞݳฎᕚᑕӧਞقጱҘெԍᥴ٬ޫҘ
 
౯ժଉአጱ Arraylist  , LinkedList , Hashmap , HashSet , TreeSet , TreeMap ҅ PriorityQueue  ᮷
ӧฎᕚᑕਞقጱ̶ᥴ٬ېဩஉᓌܔ҅ݢզֵአᕚᑕਞقጱᵞݳ๶դ̶๊
ইຎ֦ᥝֵአᕚᑕਞقጱᵞݳጱᦾ҅ java.util.concurrent  ۱Ӿ൉׀ԧஉग़ଚݎ਻࢏׀ֵ֦አғ
1. 
ConcurrentHashMap : ݢզ፡֢ฎᕚᑕਞقጱ HashMap
2. 
CopyOnWriteArrayList :ݢզ፡֢ฎᕚᑕਞقጱ ArrayList ҅ࣁ᧛ग़ٟ੝ጱ࣋ݳ௔ᚆᶋଉঅ҅ᬱ
ᬱঅԭ Vector .
3. 
ConcurrentLinkedQueue :ṛපጱଚݎᴚڜֵ҅አ᱾ᤒਫሿ̶ݢզ፡؉Ӟӻᕚᑕਞقጱ
LinkedList ҅ᬯฎӞӻᶋᴥलᴚڜ̶
4. 
BlockingQueue : ᬯฎӞӻളݗ҅JDK ٖ᮱᭗ᬦ᱾ᤒ̵හᕟᒵොୗਫሿԧᬯӻളݗ̶ᤒᐏᴥलᴚ
ڜ҅ᶋଉᭇݳአԭ֢ԅහഝوՁጱ᭗̶᭲
5. 
ConcurrentSkipListMap  :᪡ᤒጱਫሿ̶ᬯฎӞӻ Map ֵ҅አ᪡ᤒጱහഝᕮ຅ᬰᤈள᭛ັತ̶
Collection ৼളݗԏ List
 
Arraylist ޾ Vector ጱ܄ڦ?
 
1. ArrayList ฎ List ጱԆᥝਫሿᔄ҅ବ੶ֵአ Object[ ]ਂؙ҅ᭇአԭ᷇ᔺጱັತૡ֢҅ᕚᑕӧਞق Ҕ
2. Vector ฎ List ጱݘᘌਫሿᔄ҅ବ੶ֵአ Object[ ]ਂؙ҅ᕚᑕਞقጱ̶
Arraylist Ө LinkedList ܄ڦ?
 
1. ฎވכᦤᕚᑕਞقғ ArrayList  ޾ LinkedList  ᮷ฎӧݶྍጱ҅Ԟ੪ฎӧכᦤᕚᑕਞقҔ
2. ବ੶හഝᕮ຅ғ Arraylist  ବ੶ֵአጱฎ Object
Object  හᕟҔ LinkedList  ବ੶ֵአጱฎ ݌ݻ᱾ᤒ
හഝᕮ຅ҁJDK1.6 ԏڹԅ஗ሾ᱾ᤒ҅JDK1.7 ݐၾԧ஗ሾ̶ဳ఺݌ݻ᱾ᤒ޾݌ݻ஗ሾ᱾ᤒጱ܄ڦ҅
ӥᶎํՕᕨکѺ҂
3. ൊف޾ڢᴻฎވݑزᔰ֖ᗝጱ୽ߥғ ɠ ArrayList
ArrayList  ᯻አහᕟਂؙ҅ಅզൊف޾ڢᴻزᔰጱ෸ᳵ
॔๥ଶݑزᔰ֖ᗝጱ୽ߥ̶ ྲইғಗᤈadd(E e) ොဩጱ෸ײ҅ ArrayList  տἕᦊࣁਖ਼೰ਧጱز
ᔰ᭄ےکྌڜᤒጱ๛ੲ҅ᬯᐿఘ٭෸ᳵ॔๥ଶ੪ฎ O(1)̶֕ฎইຎᥝࣁ೰ਧ֖ᗝ i ൊف޾ڢᴻزᔰ
ጱᦾҁ add(int index, E element) ҂෸ᳵ॔๥ଶ੪ԅ O(n-i)̶ࢩԅࣁᬰᤈӤᬿ඙֢ጱ෸ײᵞݳӾ
ᒫ i ޾ᒫ i ӻزᔰԏݸጱ(n-i)ӻزᔰ᮷ᥝಗᤈݻݸ֖/ݻڹᑏӞ֖ጱ඙̶֢ ɡ LinkedList
LinkedList  ᯻አ᱾
ᤒਂؙ҅ಅզ੒ԭ add(E e)
add(E e) ොဩጱൊف҅ڢᴻزᔰ෸ᳵ॔๥ଶӧݑزᔰ֖ᗝጱ୽ߥ҅ᬪ֒
O(1)҅ইຎฎᥝࣁ೰ਧ֖ᗝi ൊف޾ڢᴻزᔰጱᦾҁ (add(int index, E element)
(add(int index, E element) ҂ ෸ᳵ
॔๥ଶᬪ֒ԅ o(n))
o(n)) ࢩԅᵱᥝضᑏۖک೰ਧ֖ᗝٚൊف̶
4. ฎވඪ೮ள᭛ᵋ๢ᦢᳯғ LinkedList  ӧඪ೮ṛපጱᵋ๢زᔰᦢᳯ҅ᘒ ArrayList  ඪ೮̶ள᭛ᵋ
๢ᦢᳯ੪ฎ᭗ᬦزᔰጱଧݩள᭛឴ݐزᔰ੒᨝(੒ଫԭ get(int index) ොဩ)̶
5. ٖਂᑮᳵܛአғ ArrayList ጱᑮ ᳵၵᩇԆᥝ֛ሿࣁࣁ list ڜᤒጱᕮੲտᶼኸӞਧጱ਻ᰁᑮᳵ҅ᘒ
LinkedList ጱᑮᳵᜰᩇڞ֛ሿࣁਙጱྯӞӻزᔰ᮷ᵱᥝၾᘙྲ ArrayList ๅग़ጱᑮᳵҁࢩԅᥝਂනፗ
ളݸᖀ޾ፗളڹḝզ݊හഝ҂̶
ᤑ꧌ٖ਻:݌ݻ᱾ᤒ޾݌ݻ஗ሾ᱾ᤒ

---

݌ݻ᱾ᤒғ ۱ތӷӻ೰ᰒ҅Ӟӻ prev ೰ݻڹӞӻᜓᅩ҅Ӟӻ next ೰ݻݸӞӻᜓᅩ̶
ݚक़വគӞᓤ಩݌ݻ᱾ᤒᦖႴ༩ጱ෈ᒍғhttps://juejin.im/post/5b5d1a9af265da0f47352f14
݌ݻ஗ሾ᱾ᤒғ ๋ݸӞӻᜓᅩጱ next ೰ݻ head҅ᘒ head ጱ prev ೰ݻ๋ݸӞӻᜓᅩ҅຅౮Ӟӻሾ̶
ᤑ꧌ٖ਻:RandomAccess ളݗ
 
ັ፡რᎱ౯ժݎሿਫᴬӤ RandomAccess  ളݗӾՋԍ᮷ဌํਧԎ̶ಅզ҅ࣁ౯፡๶ RandomAccess  ള
ݗӧᬦฎӞӻຽᦩᗙԧ̶ຽᦩՋԍҘ ຽᦩਫሿᬯӻളݗጱᔄٍํᵋ๢ᦢᳯۑᚆ̶
ࣁ binarySearchҁ)  ොဩӾ҅ਙᥝڣෙփفጱ list ฎވ RamdomAccess  ጱਫֺ҅ইຎฎ҅᧣
አindexedBinarySearch() ොဩ҅ইຎӧฎ҅ᮎԍ᧣አiteratorBinarySearch() ොဩ
public interface RandomAccess {
}

![Java集合框架常见面试题夜间阅读版 第5页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p5_1_13f1de27.png)

![Java集合框架常见面试题夜间阅读版 第5页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p5_2_62cc1c9e.png)

---

ArrayList  ਫሿԧ RandomAccess  ളݗ҅ ᘒ LinkedList  ဌํਫሿ̶ԅՋԍޫҘ౯ᥧ஑ᬮฎ޾ବ੶
හഝᕮ຅ํىѺ ArrayList  ବ੶ฎහᕟ҅ᘒ LinkedList  ବ੶ฎ᱾ᤒ̶හᕟॠᆐඪ೮ᵋ๢ᦢᳯ҅෸ᳵ
॔๥ଶԅ O(1)҅ಅզᑍԅள᭛ᵋ๢ᦢᳯ̶᱾ᤒᵱᥝ᭭ܲکᇙਧ֖ᗝ಍ᚆᦢᳯᇙਧ֖ᗝጱزᔰ҅෸ᳵ॔๥
ଶԅ O(n)҅ಅզӧඪ೮ள᭛ᵋ๢ᦢᳯ̶҅ ArrayList  ਫሿԧ RandomAccess  ളݗ҅੪ᤒกԧ՜ٍํள
᭛ᵋ๢ᦢᳯۑᚆ̶ RandomAccess  ളݗݝฎຽᦩ҅ଚӧฎ᧔ ArrayList  ਫሿ RandomAccess  ളݗ಍
ٍํள᭛ᵋ๢ᦢᳯۑᚆጱѺ
᧔Ӟ᧔ ArrayList ጱಘ਻๢ګމ
 
ᧇᥠᒟԆጱᬯᓤ෈ᒍ:᭗ᬦრᎱӞྍӞྍړຉ ArrayList ಘ਻๢ګ
Collection ৼളݗԏ Set
 
comparable ޾ Comparator ጱ܄ڦ
 
comparable  ളݗਫᴬӤฎڊᛔjava.lang ۱ ਙํӞӻ compareTo(Object obj) ොဩአ๶ഭଧ
comparator ളݗਫᴬӤฎڊᛔ java.util ۱ਙํӞӻ compare(Object obj1, Object obj2) ොဩአ
๶ഭଧ
Ӟᛱ౯ժᵱᥝ੒ӞӻᵞݳֵአᛔਧԎഭଧ෸҅౯ժ੪ᥝ᯿ٟ compareTo() ොဩ౲compare() ොဩ҅୮
౯ժᵱᥝ੒຤Ӟӻᵞݳਫሿӷᐿഭଧොୗ҅ྲইӞӻ song ੒᨝Ӿጱྈݷ޾ྈಋݷړڦ᯻አӞᐿഭଧො
ဩጱᦾ҅౯ժݢզ᯿ٟ compareTo() ොဩ޾ֵአᛔګጱComparator ොဩ౲ᘏզӷӻ Comparator ๶ਫ
ሿྈݷഭଧ޾ྈจݷഭଧ҅ᒫԫᐿդᤒ౯ժݝᚆֵአӷӻ݇හᇇጱ Collections.sort() .
Comparator ਧګഭଧ
 
    public static <T>
    int binarySearch(List<? extends Comparable<? super T>> list, T key) {
        if (list instanceof RandomAccess || list.size()
<BINARYSEARCH_THRESHOLD)
            return Collections.indexedBinarySearch(list, key);
        else
            return Collections.iteratorBinarySearch(list, key);
    }
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        arrayList.add(-1);
        arrayList.add(3);
        arrayList.add(3);
        arrayList.add(-5);
        arrayList.add(7);
        arrayList.add(4);
        arrayList.add(-9);
        arrayList.add(-7);

---

Output:
᯿ٟ compareTo ොဩਫሿೲଙἻ๶ഭଧ
 
        System.out.println("ܻতහᕟ:");
        System.out.println(arrayList);
        // void reverse(List list)ғݍ᫨
        Collections.reverse(arrayList);
        System.out.println("Collections.reverse(arrayList):");
        System.out.println(arrayList);
        // void sort(List list),ೲᛔᆐഭଧጱ܋ଧഭଧ
        Collections.sort(arrayList);
        System.out.println("Collections.sort(arrayList):");
        System.out.println(arrayList);
        // ਧګഭଧጱአဩ
        Collections.sort(arrayList, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2.compareTo(o1);
            }
        });
        System.out.println("ਧګഭଧݸғ");
        System.out.println(arrayList);
ܻতහᕟ:
[-1, 3, 3, -5, 7, 4, -9, -7]
Collections.reverse(arrayList):
[-7, -9, 4, 7, -5, 3, 3, -1]
Collections.sort(arrayList):
[-9, -7, -5, -1, 3, 3, 4, 7]
ਧګഭଧݸғ
[7, 4, 3, 3, -1, -5, -7, -9]
// person੒᨝ဌํਫሿComparableളݗ҅ಅզ஠ᶳਫሿ҅ᬯ໏಍ӧտڊᲙ҅಍ݢզֵtreemapӾ
ጱහഝೲᶲଧഭڜ
// ڹᶎӞӻֺৼጱStringᔄ૪ᕪἕᦊਫሿԧComparableളݗ҅ᧇᕡݢզັ፡StringᔄጱAPI෈
໩҅ݚक़ٌ՜
// ؟Integerᔄᒵ᮷૪ᕪਫሿԧComparableളݗ҅ಅզӧᵱᥝݚक़ਫሿԧ
public  class Person implements Comparable<Person> {
    private String name;
    private int age;

---

public Person(String name, int age) {
        super();
        this.name = name;
        this.age = age;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    /**
     * T᯿ٟcompareToොဩਫሿೲଙἻ๶ഭଧ
     */
    @Override
    public int compareTo(Person o) {
        if (this.age > o.getAge()) {
            return 1;
        }
        if (this.age < o.getAge()) {
            return -1;
        }
        return 0;
    }
}

---

Outputғ
෫ଧ௔޾ӧݢ᯿॔௔ጱތԎฎՋԍ
 
1̵Ջԍฎ෫ଧ௔Ҙ෫ଧ௔ӧᒵԭᵋ๢௔ ҅෫ଧ௔ฎ೰ਂؙጱහഝࣁବ੶හᕟӾଚᶋೲᆙහᕟᔱ୚ጱᶲ
ଧႲے ҅ᘒฎ໑ഝහഝጱߢ૶꧊٬ਧጱ̶
2̵Ջԍฎӧݢ᯿॔௔Ҙӧݢ᯿॔௔ฎ೰Ⴒےጱزᔰೲᆙ equals()ڣෙ෸ ҅ᬬࢧ false҅ᵱᥝݶ෸᯿ٟ
equals()ොဩ޾ HashCode()ොဩ̶
ྲ᫾ HashSet̵LinkedHashSet ޾ TreeSet ӣᘏጱ୑ݶ
 
HashSet ฎ Set ളݗጱԆᥝਫሿᔄ ҅HashSet ጱବ੶ฎ HashMap҅ᕚᑕӧਞقጱ҅ݢզਂؙ null ꧊Ҕ
LinkedHashSet ฎ HashSet ጱৼᔄ҅ᚆड़ೲᆙႲےጱᶲଧ᭭ܲҔ
TreeSet ବ੶ֵአᕁἓ໅҅ᚆड़ೲᆙႲےزᔰጱᶲଧᬰᤈ᭭ܲ҅ഭଧጱොୗํᛔᆐഭଧ޾ਧګഭଧ̶
Map ളݗ
 
HashMap ޾ Hashtable ጱ܄ڦ
 
1. ᕚᑕฎވਞقғ HashMap ฎᶋᕚᑕਞقጱ҅HashTable ฎᕚᑕਞقጱ,ࢩԅ HashTable ٖ᮱ጱොဩ
च๜᮷ᕪᬦsynchronized  ץ̶᷶ҁইຎ֦ᥝכᦤᕚᑕਞقጱᦾ੪ֵአ ConcurrentHashMap
މѺ҂Ҕ
    public static void main(String[] args) {
        TreeMap<Person, String> pdata = new TreeMap<Person, String>();
        pdata.put(new Person("ୟӣ", 30), "zhangsan");
        pdata.put(new Person("๫ࢥ", 20), "lisi");
        pdata.put(new Person("ሴԲ", 10), "wangwu");
        pdata.put(new Person("ੜᕁ", 5), "xiaohong");
        // ஑کkeyጱ꧊ጱݶ෸஑کkeyಅ੒ଫጱ꧊
        Set<Person> keys = pdata.keySet();
        for (Person key : keys) {
            System.out.println(key.getAge() + "-" + key.getName());
        }
    }
5-ੜᕁ
10-ሴԲ
20-๫ࢥ
30-ୟӣ

---

2. පሲғ ࢩԅᕚᑕਞقጱᳯ᷌҅HashMap ᥝྲ HashTable පሲṛӞᅩ̶ݚक़҅HashTable च๜ᤩႣ
࿶҅ӧᥝࣁդᎱӾֵአਙҔ
3. ੒ Null key ޾ Null value ጱඪ೮ғ HashMap ݢզਂؙ null ጱ key ޾ value҅֕ null ֢ԅᲫݝᚆํ
Ӟӻ҅null ֢ԅ꧊ݢզํग़ӻҔHashTable ӧ꧋ᦜํ null Ძ޾ null ꧊҅ވڞտಲڊ
NullPointerException̶
4. ڡত਻ᰁय़ੜ޾ྯེಘ꧌਻ᰁय़ੜጱӧݶ ғ ɠ ڠୌ෸ইຎӧ೰ਧ਻ᰁڡত꧊҅Hashtable ἕᦊጱ
ڡতय़ੜԅ 11҅ԏݸྯེಘ꧌҅਻ᰁݒԅܻ๶ጱ 2n+1̶HashMap ἕᦊጱڡত۸य़ੜԅ 16̶ԏݸ
ྯེಘ꧌҅਻ᰁݒԅܻ๶ጱ 2 ׭̶ɡ ڠୌ෸ইຎᕳਧԧ਻ᰁڡত꧊҅ᮎԍ Hashtable տፗളֵአ֦
ᕳਧጱय़ੜ҅ᘒ HashMap տਖ਼ٌಘ꧌ԅ 2 ጱ଍ེොय़ੜҁHashMap ӾጱtableSizeFor() ොဩכ
ᦤ҅ӥᶎᕳڊԧრդᎱ҂̶Ԟ੪ฎ᧔ HashMap ௛ฎֵአ 2 ጱ଍֢ԅߢ૶ᤒጱय़ੜ,ݸᶎտՕᕨکԅ
Ջԍฎ 2 ጱ଍ེො̶
5. ବ੶හഝᕮ຅ғ JDK1.8 զݸጱ HashMap ࣁᥴ٬ߢ૶٫ᑱ෸ํԧ᫾य़ጱݒ۸҅୮᱾ᤒᳩଶय़ԭᴇ
꧊ҁἕᦊԅ 8҂ҁਖ਼᱾ᤒ᫨ഘ౮ᕁἓ໅ڹտڣෙ҅ইຎ୮ڹහᕟጱᳩଶੜԭ 64҅ᮎԍտᭌೠضᬰᤈ
හᕟಘ਻҅ᘒӧฎ᫨ഘԅᕁἓ໅҂෸҅ਖ਼᱾ᤒ᫨۸ԅᕁἓ໅҅զٺ੝൤ᔱ෸ᳵ̶Hashtable ဌํᬯ
໏ጱ๢ګ̶
HashMap Ӿଃํڡত਻ᰁጱ຅᭜ڍහғ
ӥᶎᬯӻොဩכᦤԧ HashMap ௛ฎֵአ 2 ጱ଍֢ԅߢ૶ᤒጱय़ੜ̶
    public HashMap(int initialCapacity, float loadFactor) {
        if (initialCapacity < 0)
            throw new IllegalArgumentException("Illegal initial capacity: " 
+
                                               initialCapacity);
        if (initialCapacity > MAXIMUM_CAPACITY)
            initialCapacity = MAXIMUM_CAPACITY;
        if (loadFactor <= 0 || Float.isNaN(loadFactor))
            throw new IllegalArgumentException("Illegal load factor: " +
                                               loadFactor);
        this.loadFactor = loadFactor;
        this.threshold = tableSizeFor(initialCapacity);
    }
     public HashMap(int initialCapacity) {
        this(initialCapacity, DEFAULT_LOAD_FACTOR);
    }

---

HashMap
HashSet
ਫሿԧ Map ളݗ
ਫሿ Set ളݗ
ਂؙᲫ꧊੒
Րਂؙ੒᨝
᧣አ put() ݻ map
ӾႲےزᔰ
᧣አ add() ොဩݻ Set ӾႲےزᔰ
HashMap ֵአᲫ
ҁKey҂ᦇᓒ
Hashcode
HashSet ֵአ౮ާ੒᨝๶ᦇᓒ hashcode ꧊҅੒ԭӷӻ੒᨝๶᧔
hashcode ݢᚆፘݶ҅ಅզ equals()ොဩአ๶ڣෙ੒᨝ጱፘᒵ௔҅
HashMap ޾ HashSet ܄ڦ
 
ইຎ֦፡ᬦ HashSet  რᎱጱᦾ੪ଫᧆᎣ᭲ғHashSet ବ੶੪ฎचԭ HashMap ਫሿጱ̶ҁHashSet ጱ
რᎱᶋଉᶋଉ੝҅ࢩԅᴻԧ clone() ̵ writeObject() ̵ readObject() ฎ HashSet ᛔ૩ӧ஑ӧਫሿ
ԏक़ٌ҅՜ොဩ᮷ฎፗള᧣አ HashMap Ӿጱොဩ̶
HashMap ޾ TreeMap ܄ڦ
 
TreeMap  ޾HashMap  ᮷ᖀಥᛔAbstractMap  ҅֕ฎᵱᥝဳ఺ጱฎTreeMap ਙᬮਫሿԧ
NavigableMap ളݗ޾SortedMap  ളݗ̶
    /**
     * Returns a power of two size for the given target capacity.
     */
    static final int tableSizeFor(int cap) {
        int n = cap - 1;
        n |= n >>> 1;
        n |= n >>> 2;
        n |= n >>> 4;
        n |= n >>> 8;
        n |= n >>> 16;
        return (n < 0) ? 1 : (n >= MAXIMUM_CAPACITY) ? MAXIMUM_CAPACITY : n 
+ 1;
    }

---

ਫሿ NavigableMap  ളݗᦏ TreeMap  ํԧ੒ᵞݳٖزᔰጱ൤ᔱጱᚆێ̶
ਫሿSortMap ളݗᦏ TreeMap  ํԧ੒ᵞݳӾጱزᔰ໑ഝᲫഭଧጱᚆێ̶ἕᦊฎೲ key ጱ܋ଧഭଧ҅ӧ
ᬦ౯ժԞݢզ೰ਧഭଧጱྲ᫾࢏̶ᐏֺդᎱইӥғ
/**
 * @author shuang.kou
 * @createTime 2020ଙ06์15෭ 17:02:00
 */
public class Person {
    private Integer age;
    public Person(Integer age) {
        this.age = age;
    }
    public Integer getAge() {
        return age;
    }
    public static void main(String[] args) {
        TreeMap<Person, String> treeMap = new TreeMap<>(new 
Comparator<Person>() {
            @Override
            public int compare(Person person1, Person person2) {
                int num = person1.getAge() - person2.getAge();
                return Integer.compare(num, 0);
            }
        });
        treeMap.put(new Person(3), "person1");
        treeMap.put(new Person(18), "person2");

![Java集合框架常见面试题夜间阅读版 第12页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p12_1_8c1011a8.png)

---

ᬌڊ:
ݢզ፡ڊ҅ TreeMap  Ӿጱزᔰ૪ᕪฎೲᆙ Person  ጱ age ਁྦྷጱ܋ଧ๶ഭڜԧ̶
Ӥᶎ҅౯ժฎ᭗ᬦփف܇ݷٖ᮱ᔄጱොୗਫሿጱ֦҅ݢզਖ਼դᎱ๊ഘ౮ Lambda ᤒᬡୗਫሿጱොୗғ
ᖓӤ҅ፘྲԭ HashMap
HashMap ๶᧔ TreeMap
TreeMap  Ԇᥝग़ԧ੒ᵞݳӾጱزᔰ໑ഝᲫഭଧጱᚆێզ݊੒ᵞݳٖزᔰ
ጱ൤ᔱጱᚆێ̶
HashSet ই֜༄ັ᯿॔
 
୮֦಩੒᨝ےف HashSet ෸҅HashSet տضᦇᓒ੒᨝ጱhashcode ꧊๶ڣෙ੒᨝ےفጱ֖ᗝ҅ݶ෸Ԟտ
Өٌ՜ےفጱ੒᨝ጱ hashcode ꧊֢ྲ᫾҅ইຎဌํፘᒧጱ hashcode҅HashSet տ؃ᦡ੒᨝ဌํ᯿॔
ڊሿ̶֕ฎইຎݎሿํፘݶ hashcode ꧊ጱ੒᨝҅ᬯ෸տ᧣አequals() ොဩ๶༄ັ hashcode ፘᒵጱ
੒᨝ฎވ፥ጱፘݶ̶ইຎӷᘏፘݶ҅HashSet ੪ӧտᦏےف඙֢౮ۑ̶ҁ൹ᛔ౯ጱ Java ސ᠃ԡ̽Head
ﬁst java̾ᒫԫᇇ҂
hashCode()Ө equals()ጱፘىᥢਧғ
1. ইຎӷӻ੒᨝ፘᒵ҅ڞ hashcode ӞਧԞฎፘݶጱ
2. ӷӻ੒᨝ፘᒵ,੒ӷӻ equals ොဩᬬࢧ true
3. ӷӻ੒᨝ํፘݶጱ hashcode ꧊҅ਙժԞӧӞਧฎፘᒵጱ
4. ᖓӤ҅equals ොဩᤩᥟፍᬦ҅ڞ hashCode ොဩԞ஠ᶳᤩᥟፍ
5. hashCode()ጱἕᦊᤈԅฎ੒ञӤጱ੒᨝Ծኞᇿᇙ꧊̶ইຎဌํ᯿ٟ hashCode()҅ڞᧆ class ጱӷӻ
੒᨝෫ᦞই֜᮷ӧտፘᒵҁܨֵᬯӷӻ੒᨝೰ݻፘݶጱහഝ҂̶
        treeMap.put(new Person(35), "person3");
        treeMap.put(new Person(16), "person4");
        treeMap.entrySet().stream().forEach(personStringEntry -> {
            System.out.println(personStringEntry.getValue());
        });
    }
}
person1
person4
person2
person3
TreeMap<Person, String> treeMap = new TreeMap<>((person1, person2) -> {
  int num = person1.getAge() - person2.getAge();
  return Integer.compare(num, 0);
});

---

==Ө equals ጱ܄ڦ
੒ԭच๜ᔄࣳ๶᧔҅== ྲ᫾ጱฎ꧊ฎވፘᒵҔ
੒ԭ୚አᔄࣳ๶᧔҅== ྲ᫾ጱฎӷӻ୚አฎވ೰ݻݶӞӻ੒᨝ࣈ࣎ҁӷᘏࣁٖਂӾਂනጱࣈ࣎ҁञٖ
ਂࣈ࣎҂ฎވ೰ݻݶӞӻࣈො҂Ҕ
੒ԭ୚አᔄࣳҁ۱ೡ۱ᤰᔄࣳ҂๶᧔҅equals ইຎဌํᤩ᯿ٟ҅੒ྲਙժጱࣈ࣎ฎވፘᒵҔইຎ
equals()ොဩᤩ᯿ٟҁֺই String҂҅ڞྲ᫾ጱฎࣈ࣎᯾ጱٖ਻̶
HashMap ጱବ੶ਫሿ
 
JDK1.8 ԏڹ
 
JDK1.8 ԏڹ HashMap  ବ੶ฎ හᕟ޾᱾ᤒ ᕮݳࣁӞֵ᩸አԞ੪ฎ ᱾ᤒවڜ̶HashMap ᭗ᬦ key ጱ
hashCode ᕪᬦಟۖڍහ॒ቘᬦݸ஑ک hash ꧊҅ᆐݸ᭗ᬦ (n - 1) & hash ڣෙ୮ڹزᔰਂනጱ֖ᗝ
ҁᬯ᯾ጱ n ೰ጱฎහᕟጱᳩଶ҂҅ইຎ୮ڹ֖ᗝਂࣁزᔰጱᦾ҅੪ڣෙᧆزᔰӨᥝਂفጱزᔰጱ hash
꧊զ݊ key ฎވፘݶ҅ইຎፘݶጱᦾ҅ፗളᥟፍ҅ӧፘݶ੪᭗ᬦ೉᱾ဩᥴ٬٫ᑱ̶
ಅ᧲ಟۖڍහ೰ጱ੪ฎ HashMap ጱ hash ොဩ̶ֵአ hash ොဩԞ੪ฎಟۖڍහฎԅԧᴠྊӞԶਫሿ
ྲ᫾૧ጱ hashCode() ොဩ ഘݙᦾ᧔ֵአಟۖڍහԏݸݢզٺ੝Ᏻඊ̶
JDK 1.8 HashMap ጱ hash ොဩრᎱ:
JDK 1.8 ጱ hash ොဩ ፘྲԭ JDK 1.7 hash ොဩๅےᓌ۸҅֕ฎܻቘӧݒ̶
੒ྲӞӥ JDK1.7 ጱ HashMap ጱ hash ොဩრᎱ.
    static final int hash(Object key) {
      int h;
      // key.hashCode()ғᬬࢧවڜ꧊Ԟ੪ฎhashcode
      // ^ ғೲ֖୑౲
      // >>>:෫ᒧݩݦᑏ҅஺ኼᒧݩ֖҅ᑮ֖᮷զ0ᤑἶ
      return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
  }
static int hash(int h) {
    // This function ensures that hashCodes that differ only by
    // constant multiples at each bit position have a bounded
    // number of collisions (approximately 8 at default load factor).
    h ^= (h >>> 20) ^ (h >>> 12);
    return h ^ (h >>> 7) ^ (h >>> 4);
}

---

ፘྲԭ JDK1.8 ጱ hash ොဩ ҅JDK 1.7 ጱ hash ොဩጱ௔ᚆտᑖ૧Ӟᅩᅩ҅ࢩԅླᒌಟۖԧ 4 ̶ེ
ಅ᧲ “೉᱾ဩ” ੪ฎғਖ਼᱾ᤒ޾හᕟፘᕮݳ̶Ԟ੪ฎ᧔ڠୌӞӻ᱾ᤒහᕟ҅හᕟӾྯӞ໒੪ฎӞӻ᱾
ᤒ̶ᝑ᭬کߢ૶٫ᑱ҅ڞਖ਼٫ᑱጱ꧊ےک᱾ᤒӾܨݢ̶
JDK1.8 ԏݸ
 
ፘྲԭԏڹጱᇇ๜҅ JDK1.8 ԏݸࣁᥴ٬ߢ૶٫ᑱ෸ํԧ᫾य़ጱݒ۸҅୮᱾ᤒᳩଶय़ԭᴇ꧊ҁἕᦊԅ
8҂ҁਖ਼᱾ᤒ᫨ഘ౮ᕁἓ໅ڹտڣෙ҅ইຎ୮ڹහᕟጱᳩଶੜԭ 64҅ᮎԍտᭌೠضᬰᤈහᕟಘ਻҅ᘒӧ
ฎ᫨ഘԅᕁἓ໅҂෸҅ਖ਼᱾ᤒ᫨۸ԅᕁἓ໅҅զٺ੝൤ᔱ෸ᳵ̶

![Java集合框架常见面试题夜间阅读版 第15页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p15_1_dd3af169.png)

---

TreeMap̵TreeSet զ݊ JDK1.8 ԏݸጱ HashMap ବ੶᮷አکԧᕁἓ໅̶ᕁἓ໅੪ฎԅԧᥴ
٬ԫ݉ັತ໅ጱᗌᵅ҅ࢩԅԫ݉ັತ໅ࣁ຤Զఘ٭ӥտᭅ۸౮Ӟӻᕚ௔ᕮ຅̶
HashMap ጱᳩଶԅՋԍฎ 2 ጱ଍ེො
 
ԅԧᚆᦏ HashMap ਂݐṛප҅ੱᰁ᫾੝Ᏻඊ҅Ԟ੪ฎᥝੱᰁ಩හഝړᯈ࣐۰̶౯ժӤᶎԞᦖکԧᬦ
ԧ҅Hash ꧊ጱ᝜ࢱ꧊-2147483648 ک 2147483647҅ڹݸے᩸๶य़༷ 40 Պጱฉ੘ᑮᳵ҅ݝᥝߢ૶ڍහ
ฉ੘஑ྲ᫾࣐۰ຂව҅ӞᛱଫአฎஉᵙڊሿᏳඊጱ̶֕ᳯ᷌ฎӞӻ 40 Պᳩଶጱහᕟٖ҅ਂฎනӧӥ
ጱ̶ಅզᬯӻවڜ꧊ฎӧᚆፗള೭๶አጱ̶አԏڹᬮᥝض؉੒හᕟጱᳩଶݐཛྷᬩᓒ҅஑کጱ֟හ಍ᚆአ
๶ᥝਂනጱ֖ᗝԞ੪ฎ੒ଫጱහᕟӥຽ̶ᬯӻහᕟӥຽጱᦇᓒොဩฎ“ (n - 1) & hash ”̶ҁn դᤒහ
ᕟᳩଶ҂̶ᬯԞ੪ᥴ᯽ԧ HashMap ጱᳩଶԅՋԍฎ 2 ጱ଍ེො̶
ᬯӻᓒဩଫᧆই֜ᦡᦇޫҘ
౯ժḒضݢᚆտమک᯻አ%ݐ֟ጱ඙֢๶ਫሿ̶֕ฎ҅᯿ᅩ๶ԧғ“ݐ֟(%)඙֢Ӿইຎᴻහฎ 2 ጱ଍ེ
ڞᒵհԭӨٌᴻහٺӞጱӨ(&)඙֢ҁԞ੪ฎ᧔ hash%length==hash&(length-1)ጱڹ൉ฎ length ฎ 2
ጱ n ེොҔ҂̶” ଚӬ ᯻አԫᬰګ֖඙֢ &҅ፘ੒ԭ%ᚆड़൉ṛᬩᓒපሲ҅ᬯ੪ᥴ᯽ԧ HashMap ጱᳩ
ଶԅՋԍฎ 2 ጱ଍ེො̶
HashMap ग़ᕚᑕ඙֢੕ᛘྒ஗ሾᳯ᷌
 
Ԇᥝܻࢩࣁԭଚݎӥጱ Rehash տ᭜౮زᔰԏᳵտ୵౮Ӟӻ஗ሾ᱾ᤒ̶ӧᬦ҅jdk 1.8 ݸᥴ٬ԧᬯӻᳯ
᷌҅֕ฎᬮฎӧୌᦓࣁग़ᕚᑕӥֵአ HashMap,ࢩԅग़ᕚᑕӥֵአ HashMap ᬮฎտਂࣁٌ՜ᳯ᷌ྲই
හഝӶ०̶ଚݎሾहӥവគֵአ ConcurrentHashMap ̶

![Java集合框架常见面试题夜间阅读版 第16页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p16_1_03c086da.png)

---

ᧇఘ᧗ັ፡ғhttps://coolshell.cn/articles/9606.html
HashMap ํߺپᐿଉᥠጱ᭭ܲොୗ?
 
HashMap ጱ 7 ᐿ᭭ܲොୗӨ௔ᚆړຉѺ
ConcurrentHashMap ޾ Hashtable ጱ܄ڦ
 
ConcurrentHashMap ޾ Hashtable ጱ܄ڦԆᥝ֛ሿࣁਫሿᕚᑕਞقጱොୗӤӧݶ̶
ବ੶හഝᕮ຅ғ JDK1.7 ጱ ConcurrentHashMap ବ੶᯻አ ړྦྷጱහᕟ+᱾ᤒ ਫሿ҅JDK1.8 ᯻አጱ
හഝᕮ຅᪙ HashMap1.8 ጱᕮ຅Ӟ໏҅හᕟ+᱾ᤒ/ᕁἓԫ݉໅̶Hashtable ޾ JDK1.8 ԏڹጱ
HashMap ጱବ੶හഝᕮ຅ᔄ֒᮷ฎ᯻አ හᕟ+᱾ᤒ ጱ୵ୗ҅හᕟฎ HashMap ጱԆ֛҅᱾ᤒڞฎ
Ԇᥝԅԧᥴ٬ߢ૶٫ᑱᘒਂࣁጱҔ
ਫሿᕚᑕਞقጱොୗҁ᯿ᥝ҂ғ ɠ ࣁ JDK1.7 ጱ෸ײ҅ConcurrentHashMapҁړྦྷᲁ҂ ੒ෆӻ
໲හᕟᬰᤈԧړۆړྦྷ(Segment)҅ྯӞ಩ᲁݝᲁ਻࢏ٌӾӞ᮱ړහഝ҅ग़ᕚᑕᦢᳯ਻࢏᯾ӧݶහ
ഝྦྷጱහഝ҅੪ӧտਂࣁᲁᒋԩ҅൉ṛଚݎᦢᳯሲ̶ کԧ JDK1.8 ጱ෸ײ૪ᕪ൷୒ԧ Segment ጱ
༷ஷ҅ᘒฎፗളአ Node හᕟ+᱾ᤒ+ᕁἓ໅ጱහഝᕮ຅๶ਫሿ҅ଚݎഴګֵአ synchronized ޾
CAS ๶඙̶֢ҁJDK1.6 զݸ ੒ synchronized ᲁ؉ԧஉग़ս۸҂ ෆӻ፡᩸๶੪؟ฎս۸ᬦӬᕚᑕ
ਞقጱ HashMap҅ᡱᆐࣁ JDK1.8 Ӿᬮᚆ፡ک Segment ጱහഝᕮ຅҅֕ฎ૪ᕪᓌ۸ԧં௔҅ݝฎ
ԅԧّ਻෯ᇇ๜Ҕɡ Hashtable(ݶӞ಩ᲁ) :ֵአ synchronized ๶כᦤᕚᑕਞق҅පሲᶋଉ֗ӥ̶
୮Ӟӻᕚᑕᦢᳯݶྍොဩ෸ٌ҅՜ᕚᑕԞᦢᳯݶྍොဩ҅ݢᚆտᬰفᴥल౲᫪ᧃᇫா҅ইֵአ put
Ⴒےزᔰ҅ݚӞӻᕚᑕӧᚆֵአ put Ⴒےزᔰ҅Ԟӧᚆֵአ get҅ᒋԩտ᩼๶᩼ᄶᅱපሲ̶᩼֗
ӷᘏጱ੒ྲࢶғ
HashTable:

---

http://www.cnblogs.com/chengxiao/p/6842045.html>
JDK1.7 ጱ ConcurrentHashMapғ
http://www.cnblogs.com/chengxiao/p/6842045.html>
JDK1.8 ጱ ConcurrentHashMapғ

![Java集合框架常见面试题夜间阅读版 第18页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p18_1_38742188.png)

![Java集合框架常见面试题夜间阅读版 第18页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p18_2_25f80745.png)

---

JDK1.8 ጱ ConcurrentHashMap  ӧࣁฎ Segment හᕟ + HashEntry හᕟ + ᱾ᤒ҅ᘒฎ Node හᕟ +
᱾ᤒ / ᕁἓ໅̶ӧᬦ҅Node ݝᚆአԭ᱾ᤒጱఘ٭҅ᕁἓ໅ጱఘ٭ᵱᥝֵአ TreeNode
TreeNode ̶୮٫ᑱ᱾ᤒᬡ
کӞਧᳩଶ෸҅᱾ᤒտ᫨ഘ౮ᕁἓ໅̶
ConcurrentHashMap ᕚᑕਞقጱٍ֛ਫሿොୗ/ବ੶ٍ֛ਫሿ
 
JDK1.7ҁӤᶎํᐏ఺ࢶ҂
 
Ḓضਖ਼හഝړԅӞྦྷӞྦྷጱਂؙ҅ᆐݸᕳྯӞྦྷහഝᯈӞ಩ᲁ҅୮ӞӻᕚᑕܛአᲁᦢᳯٌӾӞӻྦྷහഝ
෸ٌ҅՜ྦྷጱහഝԞᚆᤩٌ՜ᕚᑕᦢᳯ̶
ConcurrentHashMap ฎኧ Segment හᕟᕮ຅޾ HashEntry හᕟᕮ຅ᕟ౮̶
Segment ਫሿԧ ReentrantLock,ಅզ Segment ฎӞᐿݢ᯿فᲁ҅ಝᄍᲁጱ᥯ᜋ̶HashEntry አԭਂؙ
Ძ꧊੒හഝ̶
Ӟӻ ConcurrentHashMap ᯾۱ތӞӻ Segment හᕟ̶Segment ጱᕮ຅޾ HashMap ᔄ֒҅ฎӞᐿහ
ᕟ޾᱾ᤒᕮ຅҅Ӟӻ Segment ۱ތӞӻ HashEntry හᕟ҅ྯӻ HashEntry ฎӞӻ᱾ᤒᕮ຅ጱزᔰ҅ྯ
ӻ Segment ਝಷ፳Ӟӻ HashEntry හᕟ᯾ጱزᔰ҅୮੒ HashEntry හᕟጱහഝᬰᤈץද෸҅஠ᶳḒض
឴஑੒ଫጱ Segment ጱᲁ̶
JDK1.8 ҁӤᶎํᐏ఺ࢶ҂
 
ConcurrentHashMap ݐၾԧ Segment ړྦྷᲁ҅᯻አ CAS ޾ synchronized ๶כᦤଚݎਞق̶හഝᕮ຅
᪙ HashMap1.8 ጱᕮ຅ᔄ֒҅හᕟ+᱾ᤒ/ᕁἓԫ݉໅̶Java 8 ࣁ᱾ᤒᳩଶ᩻ᬦӞਧᴇ꧊ҁ8҂෸ਖ਼᱾ᤒ
ҁ੔࣎෸ᳵ॔๥ଶԅ O(N)҂᫨ഘԅᕁἓ໅ҁ੔࣎෸ᳵ॔๥ଶԅ O(log(N))҂
static class Segment<K,V> extends ReentrantLock implements Serializable {
}

![Java集合框架常见面试题夜间阅读版 第19页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p19_1_0cc2dd60.png)

---

synchronized ݝᲁਧ୮ڹ᱾ᤒ౲ᕁἓԫ݉໅ጱḒᜓᅩ҅ᬯ໏ݝᥝ hash ӧ٫ᑱ҅੪ӧտԾኞଚݎ҅පሲ
݈൉܋ N ׭̶
Collections ૡٍᔄ
 
Collections ૡٍᔄଉአොဩ:
1. ഭଧ
2. ັತ,๊ഘ඙֢
3. ݶྍഴګ(ӧവគ҅ᵱᥝᕚᑕਞقጱᵞݳᔄࣳ෸᧗ᘍᡤֵአ JUC ۱ӥጱଚݎᵞݳ)
ഭଧ඙֢
 
ັತ,๊ഘ඙֢
 
ݶྍഴګ
 
Collections  ൉׀ԧग़ӻ synchronizedXxx() ොဩ·҅ᧆොဩݢզਖ਼೰ਧᵞݳ۱ᤰ౮ᕚᑕݶྍጱᵞݳ҅
՗ᘒᥴ٬ग़ᕚᑕଚݎᦢᳯᵞݳ෸ጱᕚᑕਞقᳯ̶᷌
void reverse(List list)//ݍ᫨
void shuffle(List list)//ᵋ๢ഭଧ
void sort(List list)//ೲᛔᆐഭଧጱ܋ଧഭଧ
void sort(List list, Comparator c)//ਧګഭଧ҅ኧComparatorഴګഭଧ᭦ᬋ
void swap(List list, int i , int j)//Իഘӷӻᔱ୚֖ᗝጱزᔰ
void rotate(List list, int distance)//෤᫨̶୮distanceԅྋහ෸҅ਖ਼listݸ
distanceӻزᔰෆ֛ᑏکڹᶎ̶୮distanceԅᨮහ෸҅ਖ਼ listጱڹdistanceӻزᔰෆ֛ᑏکݸ
ᶎ
int binarySearch(List list, Object key)//੒Listᬰᤈԫړັತ҅ᬬࢧᔱ୚҅ဳ఺List
஠ᶳฎํଧጱ
int max(Collection coll)//໑ഝزᔰጱᛔᆐᶲଧ҅ᬬࢧ๋य़ጱزᔰ̶ ᔄྲint 
min(Collection coll)
int max(Collection coll, Comparator c)//໑ഝਧګഭଧ҅ᬬࢧ๋य़زᔰ҅ഭଧᥢڞኧ
Comparatatorᔄഴګ̶ᔄྲint min(Collection coll, Comparator c)
void fill(List list, Object obj)//አ೰ਧጱزᔰդ๊೰ਧlistӾጱಅํزᔰ̶
int frequency(Collection c, Object o)//ᕹᦇزᔰڊሿེහ
int indexOfSubList(List list, List target)//ᕹᦇtargetࣁlistӾᒫӞེڊሿጱᔱ
୚҅ತӧکڞᬬࢧ-1҅ᔄྲint lastIndexOfSubList(List source, list target).
boolean replaceAll(List list, Object oldVal, Object newVal), አෛزᔰ๊ഘ෯ز
ᔰ

---

౯ժᎣ᭲ HashSet ҅ TreeSet ҅ ArrayList , LinkedList , HashMap , TreeMap  ᮷ฎᕚᑕӧਞق
ጱ̶ Collections  ൉׀ԧग़ӻᶉாොဩݢզ಩՜ժ۱ᤰ౮ᕚᑕݶྍጱᵞݳ̶
๋অӧᥝአӥᶎᬯԶොဩ҅පሲᶋଉ֗҅ᵱᥝᕚᑕਞقጱᵞݳᔄࣳ෸᧗ᘍᡤֵአ JUC ۱ӥጱଚݎᵞ
ݳ̶
ොဩইӥғ
ٌ՜᯿ᥝᳯ᷌
 
Ջԍฎள᭛०ᨳ(fail-fast)Ҙ
 
ள᭛०ᨳ(fail-fast) ฎ Java ᵞݳጱӞᐿᲙ᧏༄ၥ๢ګ̶ࣁֵአᬽդ࢏੒ᵞݳᬰᤈ᭭ܲጱ෸ײ҅౯ժࣁग़
ᕚᑕӥ඙֢ᶋਞق०ᨳ(fail-safe)ጱᵞݳᔄݢᚆ੪տ᥶ݎ fail-fast ๢ګ҅੕ᛘಲڊ
ConcurrentModificationException
ConcurrentModificationException  ୑ଉ̶ ݚक़҅ࣁܔᕚᑕӥ҅ইຎࣁ᭭ܲᬦᑕӾ੒ᵞݳ੒᨝
ጱٖ਻ᬰᤈԧץදጱᦾԞտ᥶ݎ fail-fast ๢ګ̶
ဳғी୩ for ஗ሾԞฎ׵ۗᬽդ࢏ᬰᤈ̶᭭ܲ
Ԉӻֺৼғग़ᕚᑕӥ҅ইຎᕚᑕ 1 ྋࣁ੒ᵞݳᬰᤈ᭭ܲ҅ྌ෸ᕚᑕ 2 ੒ᵞݳᬰᤈץදҁीے̵ڢᴻ̵ץ
ද҂҅౲ᘏᕚᑕ 1 ࣁ᭭ܲᬦᑕӾ੒ᵞݳᬰᤈץද҅᮷տ੕ᛘᕚᑕ 1 ಲڊ
ConcurrentModificationException  ୑ଉ̶
ԅՋԍޫҘ
ྯ୮ᬽդ࢏ֵአ hashNext() / next() ᭭ܲӥӞӻزᔰԏڹ҅᮷տ༄ၥ modCount  ݒᰁฎވԅ
expectedModCount  ꧊҅ฎጱᦾ੪ᬬࢧ᭭ܲҔވڞಲڊ୑ଉ҅ᕣྊ̶᭭ܲ
ইຎ౯ժࣁᵞݳᤩ᭭ܲ๗ᳵ੒ٌᬰᤈץදጱᦾ҅੪տදݒ modCount  ጱ꧊҅ᬰᘒ੕ᛘ modCount !=
expectedModCount  ҅ᬰᘒಲڊ ConcurrentModificationException  ୑ଉ̶
ဳғ᭗ᬦ Iterator  ጱොဩץදᵞݳጱᦾտץදک expectedModCount  ጱ꧊҅ಅզӧտಲڊ
୑ଉ̶
synchronizedCollection(Collection<T>  c) //ᬬࢧ೰ਧ collection ඪ೮ጱݶྍҁᕚᑕ
ਞقጱ҂collection̶
synchronizedList(List<T> list)//ᬬࢧ೰ਧڜᤒඪ೮ጱݶྍҁᕚᑕਞقጱ҂List̶
synchronizedMap(Map<K,V> m) //ᬬࢧኧ೰ਧฉ੘ඪ೮ጱݶྍҁᕚᑕਞقጱ҂Map̶
synchronizedSet(Set<T> s) //ᬬࢧ೰ਧ set ඪ೮ጱݶྍҁᕚᑕਞقጱ҂set̶

---

অމѺፘמय़ਹ૪ᕪ൥౜ԧள᭛०ᨳ(fail-fast)๢ګզ݊ਙጱܻቘ̶
౯ժٚ๶᩹ᅾ಑᱈҅፡Ӟӻᴨ᯾૬૬ಋٙፘىጱᥢਧғ
ํԧڹᶎᦖጱचᏐ҅౯ժଫᧆᎣ᭲ғֵአ Iterator  ൉׀ጱ remove  ොဩ҅ݢզץදک
expectedModCount  ጱ꧊̶ಅզ҅಍ӧտٚಲڊ ConcurrentModificationException  ୑ଉ̶
Ջԍฎਞق०ᨳ(fail-safe)ޫҘ
 
กጮԧள᭛०ᨳ(fail-fast)ԏݸ҅ਞق०ᨳ(fail-safe)౯ժ੪உঅቘᥴԧ̶
᯻አਞق०ᨳ๢ګጱᵞݳ਻࢏҅ࣁ᭭ܲ෸ӧฎፗളࣁᵞݳٖ਻Ӥᦢᳯጱ҅ᘒฎض॔ګܻํᵞݳٖ਻҅ࣁ
೩ᨬጱᵞݳӤᬰᤈ̶᭭ܲಅզ҅ࣁ᭭ܲᬦᑕӾ੒ܻᵞݳಅ֢ጱץදଚӧᚆᤩᬽդ࢏༄ၥک҅ඳӧտಲ
ConcurrentModificationException  ୑ଉ̶
Arrays.asList()᭿ࣗ೰ܖ
 
final void checkForComodification() {
    if (modCount != expectedModCount)
        throw new ConcurrentModificationException();
}

![Java集合框架常见面试题夜间阅读版 第22页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p22_1_3323296b.png)

---

๋ᬪֵአArrays.asList() ᭬کԧӞԶࣗ҅ᆐݸࣁᗑӤ፡کᬯᓤ෈ᒍғJava Array to List Examples ఽ
ᥧꂁӧᲙጱ҅֕ฎᬮӧฎᇙڦقᶎ̶ಅզ҅ᛔ૩੒ԭᬯࣘੜᎣᦩᅩᬰᤈԧᓌܔጱ௛ᕮ̶
ᓌՕ
 
Arrays.asList() ࣁଘ෸୏ݎӾᬮฎྲ᫾ଉᥠጱ҅౯ժݢզֵአਙਖ਼Ӟӻහᕟ᫨ഘԅӞӻ List ᵞݳ̶
JDK რᎱ੒ԭᬯӻොဩጱ᧔กғ
̽ᴨ᯾૬૬ Java ୏ݎಋٙ̾੒ٌጱൈᬿ
 
Arrays.asList() ਖ਼හᕟ᫨ഘԅᵞݳݸ,ବ੶ٌਫᬮฎහᕟ҅̽ᴨ᯾૬૬ Java ୏ݎಋٙ̾੒ԭᬯӻොဩ
ํইӥൈᬿғ
ֵአ෸ጱဳ఺Ԫᶱ௛ᕮ
 
փ᭓ጱහᕟ஠ᶳฎ੒᨝හᕟ҅ᘒӧฎच๜ᔄ̶ࣳ
Arrays.asList() ฎာࣳොဩ҅փفጱ੒᨝஠ᶳฎ੒᨝හᕟ̶
String[] myArray = { "Apple", "Banana", "Orange" }Ҕ
List<String> myList = Arrays.asList(myArray);
//Ӥᶎӷӻ᧍ݙᒵհԭӥᶎӞ๵᧍ݙ
List<String> myList = Arrays.asList("Apple","Banana", "Orange");
/**
 *ᬬࢧኧ೰ਧහᕟඪ೮ጱࢴਧय़ੜጱڜᤒ̶ྌොဩ֢ԅचԭහᕟ޾चԭᵞݳጱAPIԏᳵጱ໫໴҅Ө   
        Collection.toArray()ᕮݳֵአ̶ᬬࢧጱListฎݢଧڜ۸ଚਫሿRandomAccessള
ݗ̶
 */
public static <T> List<T> asList(T... a) {
    return new ArrayList<>(a);
}

![Java集合框架常见面试题夜间阅读版 第23页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p23_1_59e78da9.png)

---

୮փفӞӻܻኞහഝᔄࣳහᕟ෸҅ Arrays.asList()  ጱ፥ྋ஑کጱ݇හ੪ӧฎහᕟӾጱزᔰ҅ᘒฎහ
ᕟ੒᨝๜᫝Ѻྌ෸ List ጱࠔӞزᔰ੪ฎᬯӻහᕟ҅ᬯԞ੪ᥴ᯽ԧӤᶎጱդᎱ̶
౯ժֵአ۱ᤰᔄࣳහᕟ੪ݢզᥴ٬ᬯӻᳯ̶᷌
ֵአᵞݳጱץදොဩ: add()
add() ̵ remove()
remove() ̵ clear()
clear() տಲڊ୑ଉ̶
Arrays.asList()  ොဩᬬࢧጱଚӧฎ java.util.ArrayList  ҅ᘒฎ java.util.Arrays  ጱӞӻٖ᮱
ᔄ,ᬯӻٖ᮱ᔄଚဌํਫሿᵞݳጱץදොဩ౲ᘏ᧔ଚဌํ᯿ٟᬯԶොဩ̶
ӥࢶฎjava.util.Arrays$ArrayList ጱᓌฃრᎱ҅౯ժݢզ፡کᬯӻᔄ᯿ٟጱොဩํߺԶ̶
int[] myArray = { 1, 2, 3 };
List myList = Arrays.asList(myArray);
System.out.println(myList.size());//1
System.out.println(myList.get(0));//හᕟࣈ࣎꧊
System.out.println(myList.get(1));//ಸᲙғArrayIndexOutOfBoundsException
int [] array=(int[]) myList.get(0);
System.out.println(array[0]);//1
Integer[] myArray = { 1, 2, 3 };
List myList = Arrays.asList(1, 2, 3);
myList.add(4);//ᬩᤈ෸ಸᲙғUnsupportedOperationException
myList.remove(1);//ᬩᤈ෸ಸᲙғUnsupportedOperationException
myList.clear();//ᬩᤈ෸ಸᲙғUnsupportedOperationException
List myList = Arrays.asList(1, 2, 3);
System.out.println(myList.getClass());//class java.util.Arrays$ArrayList
  private static class ArrayList<E> extends AbstractList<E>
        implements RandomAccess, java.io.Serializable
    {
        ...
        @Override
        public E get(int index) {
          ...
        }
        @Override

---

౯ժٚ፡Ӟӥ java.util.AbstractList ጱremove() ොဩ҅ᬯ໏౯ժ੪กጮԅࠨտಲڊ
UnsupportedOperationException ̶
 
̽Javaᶎᦶᑱڋ̾: Java ᑕଧާᶎᦶ஠॓ጱ̽Javaᶎᦶᑱڋ̾V3.0 PDF ᇇ๜ಚᎱىဳӥᶎጱلռݩ҅
ࣁݸݣࢧ॔ "ᶎᦶᑱڋ" ܨݢعᩇᶾݐѺ
        public E set(int index, E element) {
          ...
        }
        @Override
        public int indexOf(Object o) {
          ...
        }
        @Override
        public boolean contains(Object o) {
           ...
        }
        @Override
        public void forEach(Consumer<? super E> action) {
          ...
        }
        @Override
        public void replaceAll(UnaryOperator<E> operator) {
          ...
        }
        @Override
        public void sort(Comparator<? super E> c) {
          ...
        }
    }
public E remove(int index) {
    throw new UnsupportedOperationException();
}

![Java集合框架常见面试题夜间阅读版 第26页插图](../assets/images/Java集合框架常见面试题夜间阅读版_p26_1_6257e5bb.jpeg)