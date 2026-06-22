---
title: 三歪教你学Servlet
source: Java3y/基础知识原创电子书/Servlet电子书/三歪教你学Servlet.pdf
pages: 141
converted_at: 2026-06-22 22:29:24
---

# 三歪教你学Servlet

ڹ᥺
Tomcat
1.ՋԍฎTomcat
2.ԅՋԍ౯ժᵱᥝአکTomcat 
3.ᯈᗝTomcat 
4.ፘى๞᧍Օᕨ 
5.tomcatᕮ຅ፓ୯
5.1ፓ୯ጱᓌܔՕᕨ
5.2webappsፓ୯ጱᧇᕡ᧔ก
6.ᯈᗝᡦ೙ፓ୯
6.1ԅՋԍᵱᥝᯈᗝᡦ೙ፓ୯Ҙ
6.2ᯈᗝᡦ೙ፓ୯ොဩӞ
6.3ᯈᗝᡦ೙ፓ୯ොဩԫ
7.ᯈᗝԁ෸ऒݷ
7.1ᯈᗝԁ෸ऒݷྍṈ
8.ᦡᗝᡦ೙Ԇ๢
8.1Ջԍฎᡦ೙Ԇ๢Ҙ
8.2ԅՋԍᵱᥝአکᡦ೙Ԇ๢Ҙ
8.3ᯈᗝᡦ೙Ԇ๢ጱྍṈ
9.Tomcat֛ᔮᕮ຅
10.ၨᥦ࢏ᦢᳯWEBᩒრጱၞᑕࢶ
11.ᕞԟ
ServletचᏐᎣᦩ
1.ՋԍฎServletҘ
2.ԅՋԍᥝአکServletҘ
3.HTTPܐᦓ
3.1ՋԍฎHTPPܐᦓ
3.2HTTP1.0޾HTTP1.1ጱ܄ڦ
3.3HTTP᧗࿢
3.3.1᧗࿢ᤈ
3.3.2᧗࿢१
3.4HTTPߥଫ
3.4.1ᇫாᤈ
3.4.2ߥଫ१
4.JAVAWEBፓ୯ᕮ຅
5.ਫሿServletളݗᖫٟServletᑕଧ
5.1ᖫٟServletᑕଧጱྍṈ
6.Servletኞ޸ޮ๗
6.1Servletኞ޸ޮ๗ݢړԅ5ӻྍṈ
7.ᖀಥHttpServletᖫٟServletᑕଧ
ServletConﬁg̵ServletContext޾Servletᕡᜓ
1.Servletጱ᧣አࢶ
2.Servletጱᕡᜓ
2.1 Ӟӻ૪ᕪဳٙጱServletݢզᤩग़ེฉ੘
2.2 Servletฉ੘ጱURLݢզֵአ᭗ᯈᒧ
2.3 Servletฎܔֺጱ
2.3.1 ԅՋԍServletฎܔֺጱ

---

2.3.2 ྯེᦢᳯ᧗࿢੒᨝޾ߥଫ੒᨝᮷ฎෛጱ
2.3.3 ᕚᑕਞقᳯ᷌
2.4 load-on-startup
2.5 ࣁwebᦢᳯձ֜ᩒრ᮷ฎࣁᦢᳯServlet
3. ServletConﬁg੒᨝
3.1ServletConﬁg੒᨝ํՋԍአҘ
3.2឴ݐweb.xml෈կᯈᗝጱ݇හמ௳
4. ServletContext੒᨝
4.1 ՋԍฎServletContext੒᨝Ҙ
4.2 ServletContextํՋԍአҘ
4.3 Servletԏᳵਫሿ᭗ᦔ
4.4 ឴ݐwebᒊᅩᯈᗝጱמ௳
4.5 ᧛ݐᩒრ෈կ
᧛ݐᩒრᒫӞᐿොୗғ
᧛ݐᩒრᒫԫᐿොୗғ
᧛ݐᩒრᒫӣᐿොୗғ
Response੒᨝
1. response̵request੒᨝
2. ՋԍฎHttpServletResponse੒᨝Ҙ
3. HttpServletResponseጱଫአ
3.1᧣አgetOutputStream()ොဩݻၨᥦ࢏ᬌڊහഝ
3.2᧣አgetWriter()ොဩݻၨᥦ࢏ᬌڊහഝ
3.3ਫሿ෈կӥ᫹
3.4ਫሿᛔۖڬෛ
3.5ᦡᗝᖨਂ
3.6ਫሿහഝܴᖽ
3.7ኞڊᵋ๢ࢶᇆ
3.6᯿ਧݻ᪡᫨
3.7getWriter޾getOutputStreamᕡᜓ
Request੒᨝
1. ՋԍฎHttpServletRequest
2. HttpServletRequestଉአොဩ
2.1 ឴஑ਮಁ๢̓ၨᥦ࢏̈́מ௳
2.2 ឴஑ਮಁ๢᧗࿢१
2.3 ឴஑ਮಁ๢᧗࿢݇හ(ਮಁᒒ൉Իጱහഝ)
3. HttpServletRequestଫአ
3.1 ᴠፎ᱾
3.2ᤒܔ൉Իහഝ̓᭗ᬦpostොୗ൉Իහഝ̈́
3.4᩻᱾ളොୗ൉Իහഝ
3.5ᥴ٬Ӿ෈ԤᎱᳯ᷌
3.6 ਫሿ᫨ݎ
3.7 ᫨ݎጱ෸ଧࢶ
3.7.1᧗࿢᫨ݎጱᕡᜓ
3.8᫨ݎ޾᯿ਧݻጱ܄ڦ
3.8.1ਫᴬݎኞ֖ᗝӧݶ҅ࣈ࣎ໄӧݶ
3.8.2አဩӧݶ
3.8.3ᚆड़݄ஃጱURLጱ᝜ࢱӧӞ໏
3.8.4փ᭓හഝጱᔄࣳӧݶ
3.8.5᪡᫨ጱ෸ᳵӧݶ

---

3.9 ᫨ݎ޾᯿ਧݻֵአߺӞӻҘ
3.10 RequestDispatcherٚ᧔ก
Cookie
1. Ջԍฎտᦾದ๞
2. ԅՋԍ౯ժᥝֵአտᦾದ๞Ҙ
3. Cookie
3.1 ՋԍฎCookie
3.2Cookie API
3.3ᓌܔֵአCookie
4.Cookieᕡᜓ
4.1Cookieӧݢ᪜ऒݷ௔
4.2 CookieכਂӾ෈
4.3Cookieጱํප๗
4.4 Cookieጱץද޾ڢᴻ
4.5 Cookieጱऒݷ
4.6 Cookieጱ᪠ஆ
4.7 Cookieጱਞقં௔
5. Cookieጱଫአ
5.1ดᐏአಁӤེᦢᳯጱ෸ᳵ
5.2ดᐏӤེၨᥦᬦࠟߝ
Session
1. ՋԍฎSession
2. ԅՋԍᥝֵአSessionದ๞Ҙ
3. Session  API
4.Session֢ԅऒ੒᨝
5. Sessionጱኞ޸ޮ๗޾ํප๗
6. ֵአSessionਠ౮ᓌܔጱᨻᇔۑᚆ
7.Sessionጱਫሿܻቘ
8.ၨᥦ࢏ᐬአԧCookie҅SessionᬮᚆአހҘ
9.SessionᐬአCookie
10.Sessionໜֺ
10.1ֵአSessionਠ౮አಁᓌܔጭᴭ
10.2ڥአSessionᴠྊᤒܔ᯿॔൉Ի
10.3Ӟེ௔໊ḵᎱ
11. Session޾Cookieጱ܄ڦ
12. Cookie޾Sessionوݶֵአ
Servletᶎᦶ᷌
1. Tomcatଉᥠᶎᦶ᷌
1.1Tomcatጱᗌ፜ᒒݗฎग़੝҅ெԍץද
1.2Tomcat ํߺپᐿConnector ᬩᤈཛྷୗ(ս۸)Ҙ
2.Servletᶎᦶ᷌
2.1Servletኞ޸ޮ๗
2.2getොୗ޾postොୗํ֜܄ڦ
2.3forward޾redirectጱ܄ڦ
2.4 tomcat਻࢏ฎই֜ڠୌservletᔄਫֺҘአکԧՋԍܻቘҘ
2.5ՋԍฎcookieҘSession޾cookieํՋԍ܄ڦ Ҙ
2.6 Servletਞق௔ᳯ᷌

---

ڹ᥺
 
ᬯӻ෈໩ጱٖ਻ᕍಋ಑҅ইຎమᥝ፡ๅग़ጱଗᨵ෈ᒍ҅ىဳ౯ጱلռݩғJava3y̶ํๅग़ጱܻڠದ๞෈
ᒍ޾ଗᨵѺ
 
ፓڹዙᇰ॒ԭዙᇰๅෛPDFӾ҅ݝᥝฎJavaݸᒒጱᎣᦩ҅᮷տํѺཻᬨ๶౯لռݩ؛ๅѺஙמ൤
ᔱғJava3y
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺلռݩํ౯ጱᘶᔮොୗ
Javaᔜᗦᚏࢶ
Java਍ԟ᪠ᕚ
୏ݎଉአૡٍ
ᔜᗦኪৼԡ̵෈໩
ࣁلռݩӥࢧ॔̿888̀ܨݢ឴ݐѺѺ
 
਍ԟӧᚆፖፓ҅᪙፳౯҅տᦏ֦Ԫ܎ۑ׭
 
෈໩꧋ᦜᵋ఺փඎ҅֕ӧᚆץදձٖ֜਻̶
 
ኪৼԡጱෆቘԞฎꂁӧ਻ฃ҅ইຎ֦ᥧ஑ํଆۗ҅మᥝ಑ᩝ֢ᘏ҅ᮎԍݢզ᭗ᬦᬯӻතྃᎱ಑ᩝ౯҅ᰂ
᷐ӧ᯿ᥝ҅ஞ఺๋᯿ᥝ̶Ԇᥝฎ౯ݢզ᭗ᬦᬯӻ಑ᩝఘ٭๶ᶼᦇय़ਹ੒ᬯ๜ኪৼԡጱᦧհ҅ࢃࢃ

![三歪教你学Servlet 第4页插图](../assets/images/三歪教你学Servlet_p4_1_3c233a1a.jpeg)

![三歪教你学Servlet 第4页插图](../assets/images/三歪教你学Servlet_p4_2_08125413.png)

---

Tomcat
 
1.ՋԍฎTomcat
 
Tomcatᓌܔጱ᧔੪ฎӞӻᬩᤈJAVAጱᗑᕶ๐ۓ࢏҅ବ੶ฎSocketጱӞӻᑕଧ҅ਙԞฎJSP޾SerlvetጱӞ
ӻ਻࢏̶
2.ԅՋԍ౯ժᵱᥝአکTomcat
 
ইຎ֦਍ᬦhtml҅css֦҅տᎣ֦ٟ᭲ጱᶭᶎݝᚆᛔ૩ᦢᳯ҅ڦՈӧᚆᬱᑕᦢᳯ֦ٟጱᶭᶎ҅Tomcat੪
ฎ൉׀ᚆड़ᦏڦՈᦢᳯᛔ૩ٟጱᶭᶎጱӞӻᑕଧ

![三歪教你学Servlet 第5页插图](../assets/images/三歪教你学Servlet_p5_1_a7b96e96.jpeg)

![三歪教你学Servlet 第5页插图](../assets/images/三歪教你学Servlet_p5_2_46627a5a.jpeg)

![三歪教你学Servlet 第5页插图](../assets/images/三歪教你学Servlet_p5_3_f617314d.png)

---

3.ᯈᗝTomcat
 
ᬩᤈTomcatᵱᥝJDKጱඪ೮̓Tomcatտ᭗ᬦJAVA_HOMEತکಅᵱᥝጱJDK̶̈́
ෛୌJAVA_HOMEሾहݒᰁ̓᪠ஆฎJDKጱԆፓ୯̈́
ᬰفTomcatፓ୯ӥጱbinӾސۖstartup.bat҅զӥฎ౮ۑސۖTomcatጱᶭᶎ̶

![三歪教你学Servlet 第6页插图](../assets/images/三歪教你学Servlet_p6_1_5bc7c838.png)

---

ࣁၨᥦ࢏ࣈ࣎ໄᬌفhttp://localhost:8080,ইຎᚆड़ڊሿTomcatᶭᶎ҅᧔กᯈᗝ౮ۑԧ̶
ဳ఺ғইຎࣁֵአTomcat෸ڊሿԧ Error deploying web application directory web222 ,உय़
ܻࢩ੪ฎjdk޾tomcatጱᇇ๜ӧ܃ᯈ̶
ፓڹ҅jdk8ӧᚆ܃ᯈtomcat7.0҅ಅզᥝᴳ֗jdkᇇ๜̓ഘ౮JDK7̈́
୮ᆐԞํݢᚆӧฎӞ૴ᷚᶲᚆड़ፗളސۖTomcat҅ӧᚆྋଉސۖTomcatտํզӥఘ٭
1. JAVA_HOMEᯈᗝᲙ᧏
2. ᒒݗᤩܛአԧ
ᒫӞᐿොဩғࣁcmdᬌفnetstat -anbັ፡᧡ܛአԧᧆᒒݗ̓Tomcatἕᦊጱฎ8080̈́,ࣁᬰᑕ
Ӿىᳮਙ
ᒫԫᐿොဩғԆۖදݒtomcatጱᒒݗ, کtomcatԆፓ୯ӥጱconf/server.xml෈կӾץද,಩
8080ᒒݗද౮ฎ8088౲ᘏฎٌ՜ጱ

![三歪教你学Servlet 第7页插图](../assets/images/三歪教你学Servlet_p7_1_49a6ce0b.png)

![三歪教你学Servlet 第7页插图](../assets/images/三歪教你学Servlet_p7_2_ff48218e.png)

---

4.ፘى๞᧍Օᕨ
 
 
5.tomcatᕮ຅ፓ୯
 
5.1ፓ୯ጱᓌܔՕᕨ
 
1. binғސۖ޾ىᳮtomcatጱbat෈կ
2. confғᯈᗝ෈կ
server.xml ᧆ෈կአԭᯈᗝserverፘىጱמ௳҅ྲইtomcatސۖጱᒒݗݩ҅ᯈᗝԆ๢
(Host)
web.xml ෈կᯈᗝӨwebଫአҁwebଫአፘ୮ԭӞӻwebᒊᅩ҂

![三歪教你学Servlet 第8页插图](../assets/images/三歪教你学Servlet_p8_1_944c358f.png)

![三歪教你学Servlet 第8页插图](../assets/images/三歪教你学Servlet_p8_2_09019aad.png)

---

tomcat-user.xml ᯈᗝአಁݷੂᎱ޾ፘى๦ᴴ.
3. libғᧆፓ୯නᗝᬩᤈtomcatᬩᤈᵱᥝጱjar۱
4. logsғਂන෭ப҅୮౯ժᵱᥝັ፡෭பጱ෸ײ҅ݢզັᧃמ௳
5. webappsғනᗝ౯ժጱwebଫአ
6. workૡ֢ፓ୯ғᧆፓ୯አԭਂනjspᤩᦢᳯݸኞ౮੒ଫጱserver෈կ޾.class෈կ 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
5.2webappsፓ୯ጱᧇᕡ᧔ก
 
ࣁwebappsӾୌᒈԧweb1ፓ୯҅ӥᶎනᗝ౯ժጱhtml෈կ҅jsp෈կ҅ࢶᇆᒵᒵ҅ڞweb1੪ᤩ୮؉
webଫአᓕቘ᩸๶̓tomcat6.0զݸጱᇇ๜಍ඪ೮̈́
ֺৼғࣁwebappsӥڠୌӞӻwebᒊᅩ҅ࣁwebᒊᅩӥڠୌӞӻhtml෈կ҅ᦢᳯhtml෈կ

![三歪教你学Servlet 第9页插图](../assets/images/三歪教你学Servlet_p9_1_2739feea.png)

---

webᒊᅩጱፓ୯ฎํᥢ᝜ጱ
ԅՋԍᥝᬯ໏ᦡᗝwebᒊᅩፓ୯ޫҘ
ᵱ࿢ғ౯ํग़ӻhtml෈կ҅మ಩ٌӾጱӞӻhtml෈կ֢ԅ౯webᒊᅩጱḒᶭ̶
ইຎဌํWEB-INFፓ୯ӥጱweb.xml෈կඪ೮҅ฎ෫ဩᥴ٬౯ጱᵱ࿢ጱ
ᬯӻᥢ᝜ฎᕅਧᆧ౮ጱ̶

![三歪教你学Servlet 第10页插图](../assets/images/三歪教你学Servlet_p10_1_e607cafa.png)

![三歪教你学Servlet 第10页插图](../assets/images/三歪教你学Servlet_p10_2_af6e845d.png)

---

ӥᶎਖ਼webᒊᅩӥጱhelloword2.xml෈կ֢ԅᒊᅩጱḒᶭ҅ෛୌӞӻWEB-INFፓ୯
ࣁWEB-INFፓ୯ӥڠୌӞӻweb.xml
web.xml౯ժӧݢᚆտٟ҅ಅզݢզࣁwebappsፓ୯ӥٌ՜ጱᒊᅩӾಧӞղᬦ๶̓॔ګROOT/WEB-
INF/web.xmlጱ෈կکᛔ૩ጱᒊᅩӾ̈́
ࣁweb.xmlӾႲےզӥդᎱ
<welcome-file-list>
  <welcome-file>helloword2.html</welcome-file>
</welcome-file-list>

![三歪教你学Servlet 第11页插图](../assets/images/三歪教你学Servlet_p11_1_2e08f1a0.png)

![三歪教你学Servlet 第11页插图](../assets/images/三歪教你学Servlet_p11_2_9ab4624e.png)

---

ᦢᳯwebᒊᅩ̓helloword2.html૪ᕪฎwebᒊᅩጱḒᶭԧ҅ಅզӧᵱᥝ೰ਧᩒრᦢᳯԧ̈́

![三歪教你学Servlet 第12页插图](../assets/images/三歪教你学Servlet_p12_1_9bfabc1e.png)

![三歪教你学Servlet 第12页插图](../assets/images/三歪教你学Servlet_p12_2_13884e9b.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
6.ᯈᗝᡦ೙ፓ୯
 
6.1ԅՋԍᵱᥝᯈᗝᡦ೙ፓ୯Ҙ
 
ইຎ಩ಅํwebᒊᅩጱፓ୯᮷නࣁwebappsӥ҅ݢᚆ੕ᛘᏺፏᑮᳵӧड़አ҅Ԟӧڥԭ੒webᒊᅩ
ፓ୯ጱᓕቘ̓ইຎਂࣁᶋଉग़ጱwebᒊᅩፓ୯̈́
಩webᒊᅩጱፓ୯ړවکٌ՜ᏺፏᓕቘ੪ᵱᥝᯈᗝᡦ೙ፓ୯̓ἕᦊఘ٭ӥ҅ݝํwebappsӥጱፓ
୯಍ᚆᤩTomcatᛔۖᓕቘ౮Ӟӻwebᒊᅩ̈́
಩webଫአಅࣁፓ୯Իᕳweb๐ۓ࢏ᓕቘ҅ᬯӻᬦᑕᑍԏԅᡦ೙ፓ୯ጱฉ੘
6.2ᯈᗝᡦ೙ፓ୯ොဩӞ
 
ࣁٌ՜ፏᒧӥڠୌӞӻwebᒊᅩፓ୯҅ଚڠୌWEB-INFፓ୯޾Ӟӻhtml෈կ̶
ತکTomcatፓ୯ӥ/conf/server.xml෈կ

![三歪教你学Servlet 第13页插图](../assets/images/三歪教你学Servlet_p13_1_c61c6d9d.png)

![三歪教你学Servlet 第13页插图](../assets/images/三歪教你学Servlet_p13_2_b6d2079a.jpeg)

![三歪教你学Servlet 第13页插图](../assets/images/三歪教你学Servlet_p13_3_8a8d2480.png)

---

ࣁserver.xmlӾጱ<Host> ᜓᅩӥႲےইӥդᎱ̶pathᤒᐏጱฎᦢᳯ෸ᬌفጱwebᶱፓݷ҅docBaseᤒ
ᐏጱฎᒊᅩፓ୯ጱᕷ੒᪠ஆ
ᦢᳯᯈᗝঅጱwebᒊᅩ
6.3ᯈᗝᡦ೙ፓ୯ොဩԫ
 
ᬰفکconf\Catalina\localhost෈կӥ҅ڠୌӞӻxml෈կ҅ᧆ෈կጱݷਁ੪ฎᒊᅩጱݷਁ̶
  
xml෈կጱդᎱইӥ҅docBaseฎ֦webᒊᅩጱᕷ੒᪠ஆ
<Context path="/web1" docBase="D:\web1"/>

![三歪教你学Servlet 第14页插图](../assets/images/三歪教你学Servlet_p14_1_8659a31c.png)

![三歪教你学Servlet 第14页插图](../assets/images/三歪教你学Servlet_p14_2_fc7ccf7b.png)

![三歪教你学Servlet 第14页插图](../assets/images/三歪教你学Servlet_p14_3_cd523015.png)

---

ᦢᳯwebᒊᅩӥጱhtmlᩒრ
 
7.ᯈᗝԁ෸ऒݷ
 
ᦢᳯTomcat๐ۓ࢏ํঅپᐿොୗ
ֵአlocalhostऒݷᦢᳯ̓localhostդᤒ๜๢̈́
ֵአipࣈ࣎127.0.0.1ᦢᳯ̓ᧆipࣈ࣎Ԟฎ๜๢̈́
ֵአ๢࢏ݷᑍᦢᳯ̓ݝᴴአԭ๜๢Ӥ౲ᘏੴऒᗑ̈́
ֵአ๜๢IPࣈ࣎ᦢᳯ̓ࣁcmdӾᬌفipconﬁgݢզັᧃک๜๢IPࣈ࣎̈́
ᬮݢզԅ๢࢏ᯈᗝԁ෸ऒݷ
7.1ᯈᗝԁ෸ऒݷྍṈ
 
಑୏کC:\Windows\System32\drivers\etcӥ҅ತکhosts෈կ
ࣁhosts෈կӥᯈᗝԁ෸ऒݷ
<?xml version="1.0" encoding="UTF-8"?> 
<Context 
    docBase="D:\web1" 
    reloadable="true"> 
</Context>

![三歪教你学Servlet 第15页插图](../assets/images/三歪教你学Servlet_p15_1_99481fe0.png)

![三歪教你学Servlet 第15页插图](../assets/images/三歪教你学Servlet_p15_2_93a64946.png)

![三歪教你学Servlet 第15页插图](../assets/images/三歪教你学Servlet_p15_3_f20ccbca.png)

---

8.ᦡᗝᡦ೙Ԇ๢
 
8.1Ջԍฎᡦ೙Ԇ๢Ҙ
 
ग़ӻӧݶऒݷጱᗑᒊوਂԭӞӻTomcatӾ
8.2ԅՋԍᵱᥝአکᡦ೙Ԇ๢Ҙ
 
ֺৼғ౯ሿࣁ୏ݎԧ4ӻᗑᒊ҅ํ4ӻऒݷ̶ইຎ౯ӧᯈᗝᡦ೙Ԇ๢҅ӞӻTomcat๐ۓ࢏ᬩᤈӞӻᗑ
ᒊ҅౯੪ᵱᥝ4ݣኪᚏ಍ᚆ಩4ӻᗑᒊᬩᤈ᩸๶̶
8.3ᯈᗝᡦ೙Ԇ๢ጱྍṈ
 
ࣁtomcatጱserver.xml෈կӾႲےԆ๢ݷ
ᦢᳯᡦ೙Ԇ๢ӥጱwebᒊᅩ
9.Tomcat֛ᔮᕮ຅
 
<Host name="zhongfucheng" appBase="D:\web1">
  <Context path="/web1" docBase="D:\web1"/>
</Host>

![三歪教你学Servlet 第16页插图](../assets/images/三歪教你学Servlet_p16_1_092b3388.png)

![三歪教你学Servlet 第16页插图](../assets/images/三歪教你学Servlet_p16_2_b2e9d83b.png)

---

10.ၨᥦ࢏ᦢᳯWEBᩒრጱၞᑕࢶ

![三歪教你学Servlet 第17页插图](../assets/images/三歪教你学Servlet_p17_1_8f7e32fc.png)

![三歪教你学Servlet 第17页插图](../assets/images/三歪教你学Servlet_p17_2_c4785267.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
11.ᕞԟ
 
ࣁၨᥦ࢏ᬌف http//:zhongfucheng ፗളดᐏکᶭᶎ
ړຉғ
1. ᵱᥝᯈᗝᡦ೙Ԇ๢
2. ಩8080ᒒݗද౮80
3. ᦡᗝwebᒊᅩḒᶭ
4. ฉ੘ᡦ೙ፓ୯ԅ/

![三歪教你学Servlet 第18页插图](../assets/images/三歪教你学Servlet_p18_1_953b5bb8.jpeg)

![三歪教你学Servlet 第18页插图](../assets/images/三歪教你学Servlet_p18_2_00419a57.png)

![三歪教你学Servlet 第18页插图](../assets/images/三歪教你学Servlet_p18_3_c50146be.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
ServletचᏐᎣᦩ
 
1.ՋԍฎServletҘ
 
Servletٌਫ੪ฎӞӻ᭽஗Servlet୏ݎጱjavaᔄ̶Servletฎኧ๐ۓ࢏᧣አጱ҅ᬩᤈࣁ๐ۓ࢏ᒒ̶
2.ԅՋԍᥝአکServletҘ
 
౯ժᖫٟjavaᑕଧమᥝࣁᗑӤਫሿ ᘱॠ̵ݎૼ̵ᬯ໏ӞԶጱԻ԰ۑᚆ҅ฦ᭗ጱjavaದ๞ฎᶋଉᵙਠ౮
ጱ̶sunلݪ੪൉׀ԧServletᬯᐿದ๞׀౯ժֵአ̶
3.HTTPܐᦓ
 
3.1ՋԍฎHTPPܐᦓ
 
᩻෈๜փᬌܐᦓҁHTTP҅HyperText Transfer Protocol)ฎ԰ᘶᗑӤଫአ๋ԅଠာጱӞᐿᗑᕶܐ
ᦓ̶ಅํጱWWW෈կ᮷஠ᶳ᭽ਝᬯӻຽٵ̶ਙฎTCP/IPܐᦓጱӞӻଫአ੶ܐᦓ
ᓌܔ๶᧔҅HTTPܐᦓ੪ฎਮಁᒒ޾๐ۓ࢏Ի԰ጱӞᐿ᭗ᬥጱ໒ୗ̶
ֺৼ:ࣁၨᥦ࢏ᅩڋӞӻ᱾ള҅ၨᥦ࢏੪ԅ౯಑୏ᬯӻ᱾ളጱᗑᶭ̶
ܻቘғ୮ࣁၨᥦ࢏Ӿᅩڋᬯӻ᱾ളጱ෸ײ҅ၨᥦ࢏տݻ๐ۓ࢏ݎᭆӞྦྷ෈๜҅ޞᦫ๐ۓ࢏᧗࿢಑୏ጱฎ
ߺӞӻᗑᶭ̶๐ۓ࢏තک᧗࿢ݸ҅੪ᬬࢧӞྦྷ෈๜ᕳၨᥦ࢏҅ၨᥦ࢏տਖ਼ᧆ෈๜ᥴຉ҅ᆐݸดᐏڊ๶̶
ᬯྦྷ෈๜੪ฎ᭽஗HTTPܐᦓᥢ᝜ጱ̶
3.2HTTP1.0޾HTTP1.1ጱ܄ڦ
 
HTTP1.0ܐᦓӾ҅ਮಁᒒӨweb๐ۓ࢏ୌᒈᬳളݸ҅ݝᚆ឴஑Ӟӻwebᩒრ̓Ꭸᬳള҅឴ݐᩒრݸ੪ෙ
୏ᬳള̈́

![三歪教你学Servlet 第19页插图](../assets/images/三歪教你学Servlet_p19_1_3c233a1a.jpeg)

---

HTTP1.1ܐᦓ҅꧋ᦜਮಁᒒӨweb๐ۓ࢏ୌᒈᬳളݸ҅ࣁӞӻᬳളӤ឴ݐग़ӻwebᩒრ̓כ೮ᬳള̈́
3.3HTTP᧗࿢
 
ၨᥦ࢏ݻ๐ۓ࢏᧗࿢຤ӻwebᩒრ෸҅ᑍԏԅၨᥦ࢏ݻ๐ۓ࢏ݎᭆԧӞӻhttp᧗࿢̶
Ӟӻਠෆhttp᧗࿢ଫᧆ۱ތӣӻ᮱ړғ
1. ᧗࿢ᤈ̓ൈᬿਮಁᒒጱ᧗࿢ොୗ̵᧗࿢ጱᩒრݷᑍ҅զֵ݊አጱHTTPܐᦓᇇ๜ݩ̈́
2. ग़ӻၾ௳१̓ൈᬿਮಁᒒ᧗࿢ߺݣԆ๢҅զ݊ਮಁᒒጱӞԶሾहמ௳ᒵ̈́
3. Ӟӻᑮᤈ
3.3.1᧗࿢ᤈ
 
᧗࿢ᤈғGET /java.html HTTP/1.1
᧗࿢ᤈӾጱGETᑍԏԅ᧗࿢ොୗ҅᧗࿢ොୗํғPOST,GET,HEAD,OPTIONS,DELETE,TRACE,PUT̶
ଉአጱํғPOST,GET
Ӟᛱ๶᧔҅୮౯ժᅩڋ᩻᱾ള҅᭗ᬦࣈ࣎ໄᦢᳯ᮷ฎget᧗࿢ොୗ̶᭗ᬦᤒܔ൉ԻጱහഝӞᛱฎpostො
ୗ̶
ݢզᓌܔቘᥴGETොୗአ๶ັᧃහഝ,POSTොୗአ๶൉Իහഝ҅getጱ൉Ի᭛ଶྲpostள
GETොୗғࣁURLࣈ࣎ݸᴫଃጱ݇හฎํᴴګጱٌ҅හഝ਻ᰁ᭗ଉӧᚆ᩻ᬦ1K̶
POSTොୗғݢզࣁ᧗࿢ጱਫ֛ٖ਻Ӿݻ๐ۓ࢏ݎᭆහഝ҅փᭆጱහഝᰁ෫ᴴګ̶
3.3.2᧗࿢१
 
Accept: text/html,image/*    ̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ਙඪ೮ጱහഝᔄࣳ̈́
Accept-Charset: ISO-8859-1 ̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ਙඪ೮ߺᐿਁᒧᵞ̈́
Accept-Encoding: gzip,compress ̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ਙඪ೮ጱܴᖽ໒ୗ̈́
Accept-Language: en-us,zh-cn ̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ਙጱ᧍᥺ሾह̈́
Host: www.it315.org:80̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ਙጱమᦢᳯߺݣԆ๢̈́
If-Modiﬁed-Since: Tue, 11 Jul 2000 18:23:51 GMT̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ᖨਂහഝጱ෸ᳵ̈́
Referer: http://www.it315.org/index.jsp̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ਮಁ๢ฎ՗ᮎӻᶭᶎ๶ጱ---ݍፎ
᱾̈́
8.User-Agent: Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ၨᥦ
࢏ጱٖ໐ฎՋԍ̈́
Cookie̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅ଃ๶ጱCookieฎՋԍ̈́
Connection: close/Keep-Alive  ̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅᧗࿢ਠݸฎෙ୏᱾ളᬮฎכ೮᱾ള̈́ 
Date: Tue, 11 Jul 2000 18:23:51 GMT̓ၨᥦ࢏ޞᦫ๐ۓ࢏҅᧗࿢ጱ෸ᳵ̈́ 
3.4HTTPߥଫ
 
ӞӻHTTPߥଫդᤒ፳๐ۓ࢏ݻၨᥦ࢏ࢧᭆහഝ
ӞӻਠෆጱHTTPߥଫଫᧆ۱ތࢥӻ᮱ړ:
1. Ӟӻᇫாᤈ̓አԭൈᬿ๐ۓ࢏੒᧗࿢ጱ॒ቘᕮຎ̶̈́
2. ग़ӻၾ௳१̓አԭൈᬿ๐ۓ࢏ጱच๜מ௳҅զ݊හഝጱൈᬿ҅๐ۓ࢏᭗ᬦᬯԶහഝጱൈᬿמ௳҅ݢ

---

զ᭗Ꭳਮಁᒒই॒֜ቘᒵӞտدਙࢧᭆጱහഝ̈́
3. Ӟӻᑮᤈ
4. ਫ֛ٖ਻̓๐ۓ࢏ݻਮಁᒒࢧᭆጱහഝ̈́
3.4.1ᇫாᤈ
 
໒ୗғ HTTPᇇ๜ݩ̴ᇫாᎱ̴ܻࢩݓᬿ
ᇫாᤈғHTTP/1.1  200    OK
ᇫாᎱአԭᤒᐏ๐ۓ࢏੒᧗࿢ጱ॒ቘᕮຎ҅ਙฎӞӻӣ֖ጱ܈ᬰګහ̶ߥଫᇫாᎱړԅ5ᔄ
3.4.2ߥଫ१
 
Location: http://www.it315.org/index.jsp ̓๐ۓ࢏ޞᦫၨᥦ࢏ᥝ᪡᫨کߺӻᶭᶎ̈́
Server:apache tomcat̓๐ۓ࢏ޞᦫၨᥦ࢏҅๐ۓ࢏ጱࣳݩฎՋԍ̈́
Content-Encoding: gzip ̓๐ۓ࢏ޞᦫၨᥦ࢏හഝܴᖽጱ໒ୗ̈́
Content-Length: 80 ̓๐ۓ࢏ޞᦫၨᥦ࢏ࢧᭆහഝጱᳩଶ̈́
Content-Language: zh-cn ̓๐ۓ࢏ޞᦫၨᥦ࢏҅๐ۓ࢏ጱ᧍᥺ሾह̈́
Content-Type: text/html; charset=GB2312 ̓๐ۓ࢏ޞᦫၨᥦ࢏҅ࢧᭆහഝጱᔄࣳ̈́
Last-Modiﬁed: Tue, 11 Jul 2000 18:23:51 GMT̓๐ۓ࢏ޞᦫၨᥦ࢏ᧆᩒრӤེๅෛ෸ᳵ̈́
Refresh: 1;url=http://www.it315.org̓๐ۓ࢏ޞᦫၨᥦ࢏ᥝਧ෸ڬෛ̈́
Content-Disposition: attachment; ﬁlename=aaa.zip̓๐ۓ࢏ޞᦫၨᥦ࢏զӥ᫹ොୗ಑୏හഝ̈́
Transfer-Encoding: chunked  ̓๐ۓ࢏ޞᦫၨᥦ࢏හഝզړࣘොୗࢧᭆ̈́
Set-Cookie:SS=Q0=5Lb_nQ; path=/search̓๐ۓ࢏ޞᦫၨᥦ࢏ᥝכਂCookië́
Expires: -1̓๐ۓ࢏ޞᦫၨᥦ࢏ӧᥝᦡᗝᖨਂ̈́
Cache-Control: no-cache  ̓๐ۓ࢏ޞᦫၨᥦ࢏ӧᥝᦡᗝᖨਂ̈́
Pragma: no-cache   ̓๐ۓ࢏ޞᦫၨᥦ࢏ӧᥝᦡᗝᖨਂ̈́
Connection: close/Keep-Alive   ̓๐ۓ࢏ޞᦫၨᥦ࢏ᬳളොୗ̈́
Date: Tue, 11 Jul 2000 18:23:51 GMT̓๐ۓ࢏ޞᦫၨᥦ࢏ࢧᭆහഝጱ෸ᳵ̈́

![三歪教你学Servlet 第21页插图](../assets/images/三歪教你学Servlet_p21_1_0e0d58a1.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
4.JAVAWEBፓ୯ᕮ຅
 
զӤࢶ᧔กғ
bbsፓ୯դᤒӞӻwebଫአ
bbsፓ୯ӥጱhtml,jsp෈կݢզፗളᤩၨᥦ࢏ᦢᳯ
WEB-INFፓ୯ӥጱᩒრฎӧᚆፗളᤩၨᥦ࢏ᦢᳯጱ
web.xml෈կฎwebᑕଧጱԆᥝᯈᗝ෈կ
ಅํጱclasses෈կ᮷නࣁclassesፓ୯ӥ
jar෈կනࣁlibፓ୯ӥ

![三歪教你学Servlet 第22页插图](../assets/images/三歪教你学Servlet_p22_1_af6e845d.png)

![三歪教你学Servlet 第22页插图](../assets/images/三歪教你学Servlet_p22_2_2a13ce9e.jpeg)

---

5.ਫሿServletളݗᖫٟServletᑕଧ
 
ᑕଧ౯᮷ฎኧideaӥٟ҅ḒضᥝࣁideaӤᯈᗝTomcat҅ࣁ౯ڦጱܗ෈ӾํරᑕѺ
5.1ᖫٟServletᑕଧጱྍṈ
 
ڠୌӞӻᛔਧԎᔄ҅ਫሿServletളݗ
౯ժݎሿํ5ӻොဩᵱᥝ᯿ٟ҅ํinit̓ڡত۸̈́҅destroy̓ᲀྪ̈́,service̓๐
ۓ̈́,ServletConﬁg̓Servletᯈᗝ̈́,getServletInfo̓Servletמ௳̶̈́
ࣁྌӞ፡҅ݎሿservice()ොဩฎ๋ํݢᚆฎٟ᭦ᬋդᎱጱࣈො̶
ḒضٟӞӻhellwordفᳪض҅᧣አServletResponse੒᨝ጱොဩݻၨᥦ࢏ᬌڊHelloWorld
ᯈᗝxml෈կ҅طٟԧServletฎӧᤈጱ҅TomcatᬮᥝᎣ᭲ၨᥦ࢏ெԍᦢᳯᬯӻServlet̶

![三歪教你学Servlet 第23页插图](../assets/images/三歪教你学Servlet_p23_1_872b8dfa.png)

![三歪教你学Servlet 第23页插图](../assets/images/三歪教你学Servlet_p23_2_13caa246.png)

---

ᦢᳯᛔ૩ٟጱServletᑕଧ
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
6.Servletኞ޸ޮ๗

![三歪教你学Servlet 第24页插图](../assets/images/三歪教你学Servlet_p24_1_a9c25e3b.png)

![三歪教你学Servlet 第24页插图](../assets/images/三歪教你学Servlet_p24_2_f860d37b.png)

![三歪教你学Servlet 第24页插图](../assets/images/三歪教你学Servlet_p24_3_9fc53b19.png)

---

ӥᶎ౯ժ፡፡Servletጱኞ޸ޮ๗
ᒫӞེᦢᳯServlet҅౯ժݎሿinit()޾service()᮷ᤩ᧣አԧ
ᒫԫེᦢᳯServlet҅service()ᤩ᧣አԧ

![三歪教你学Servlet 第25页插图](../assets/images/三歪教你学Servlet_p25_1_a77dcf18.png)

![三歪教你学Servlet 第25页插图](../assets/images/三歪教你学Servlet_p25_2_02020d73.png)

---

ᒫӣེᦢᳯServlet҅ᬮฎservice()ᤩ᧣አԧ
୮౯ժىᳮTomcat๐ۓ࢏ጱ෸ײ҅destroy()ᤩ᧣አԧѺ

![三歪教你学Servlet 第26页插图](../assets/images/三歪教你学Servlet_p26_1_a5aa317c.png)

---

6.1Servletኞ޸ޮ๗ݢړԅ5ӻྍṈ
 
1. ے᫹Servlet̶୮TomcatᒫӞེᦢᳯServletጱ෸ײ҅TomcatտᨮᨱڠୌServletጱਫֺ
2. ڡত۸̶୮Servletᤩਫֺ۸ݸ҅Tomcatտ᧣አinit()ොဩڡত۸ᬯӻ੒᨝
3. ॒ቘ๐ۓ̶୮ၨᥦ࢏ᦢᳯServletጱ෸ײ҅Servlet տ᧣አservice()ොဩ॒ቘ᧗࿢
4. ᲀྪ̶୮Tomcatىᳮ෸౲ᘏ༄ၥکServletᥝ՗Tomcatڢᴻጱ෸ײտᛔۖ᧣አdestroy()ොဩ҅ᦏᧆ
ਫֺ᯽නധಅܛጱᩒრ̶ӞӻServletইຎᳩ෸ᳵӧᤩֵአጱᦾ҅ԞտᤩTomcatᛔۖᲀྪ
5. ܬ᫹̶୮Servlet᧣አਠdestroy()ොဩݸ҅ᒵஇ࣯࣍ࢧත̶ইຎํᵱᥝֵེٚአᬯӻServlet҅տ᯿
ෛ᧣አinit()ොဩᬰᤈڡত۸඙̶֢
 
ᓌܔ௛ᕮғݝᥝᦢᳯServlet҅service()੪տᤩ᧣አ̶init()ݝํᒫӞེᦢᳯServletጱ෸ײ಍տᤩ᧣
አ̶
destroy()ݝํࣁTomcatىᳮጱ෸ײ಍տᤩ᧣አ̶
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y

![三歪教你学Servlet 第27页插图](../assets/images/三歪教你学Servlet_p27_1_aac51d72.png)

![三歪教你学Servlet 第27页插图](../assets/images/三歪教你学Servlet_p27_2_d088d9fd.png)

---

7.ᖀಥHttpServletᖫٟServletᑕଧ
 
ࣁӤᶎ౯ժਫሿServletളݗ҅ᥝਫሿ5ӻොဩ̶ᬯ໏ॡἋᅸԧѺᘒHttpServletᔄ૪ᕪਫሿԧServletള
ݗጱಅํොဩ҅ᖫٟServlet෸҅ݝᵱᥝᖀಥHttpServlet҅᯿ٟ֦ᵱᥝጱොဩܨݢ҅ଚӬਙࣁܻํ
ServletളݗӤႲےԧӞԶӨHTTPܐᦓ॒ቘොဩ҅ਙྲServletളݗጱۑᚆๅԅ୩य̶़
Ӟᛱ౯ժ୏ݎጱ෸ײ҅᮷ฎ᯿ٟdoGet()޾doPost()ොဩጱ̶੒ԭideaᘒ᥺҅ڠୌServletጱ෸ײ૪
ᕪଆ֦᯿ٟঅԧ
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
ServletConﬁg̵ServletContext޾Servlet
ᕡᜓ
 
1.Servletጱ᧣አࢶ
 
ڹᶎ౯ժ૪ᕪ਍ᬦԧServletጱኞ޸ޮ๗ԧ҅౯ժ໑ഝServletጱኞ޸ޮ๗ኮڊServletጱ᧣አࢶےႮቘᥴ

![三歪教你学Servlet 第28页插图](../assets/images/三歪教你学Servlet_p28_1_3c233a1a.jpeg)

![三歪教你学Servlet 第28页插图](../assets/images/三歪教你学Servlet_p28_2_cc812499.png)

---

2.Servletጱᕡᜓ
 
2.1 Ӟӻ૪ᕪဳٙጱServletݢզᤩग़ེฉ੘
 
ݶӞӻServletݢզᤩฉ੘کग़ӻURLӤ̶
෫ᦞ౯ᦢᳯጱฎhttp://localhost:8080/Demo1ᬮฎhttp://localhost:8080/ouzicheng̶౯ᦢᳯጱ᮷ฎ
Demo1̶
<servlet>
  <servlet-name>Demo1</servlet-name>
  <servlet-class>zhongfucheng.web.Demo1</servlet-class>
</servlet>
<servlet-mapping>
  <servlet-name>Demo1</servlet-name>
  <url-pattern>/Demo1</url-pattern>
</servlet-mapping>
<servlet-mapping>
  <servlet-name>Demo1</servlet-name>
  <url-pattern>/ouzicheng</url-pattern>
</servlet-mapping>

![三歪教你学Servlet 第29页插图](../assets/images/三歪教你学Servlet_p29_1_78420874.png)

---

2.2 Servletฉ੘ጱURLݢզֵአ᭗ᯈᒧ
 
᭗ᯈᒧํӷᐿ໒ୗғ
1. *. ಘ઀ݷ
2. ྋෑ๴ҁ/҂୏१ଚզ“/*”ᕮੲ̶
܃ᯈಅํ
܃ᯈಘ઀ݷԅ.jspጱ

![三歪教你学Servlet 第30页插图](../assets/images/三歪教你学Servlet_p30_1_00405ac0.png)

![三歪教你学Servlet 第30页插图](../assets/images/三歪教你学Servlet_p30_2_a772dd4d.png)

![三歪教你学Servlet 第30页插图](../assets/images/三歪教你学Servlet_p30_3_5ee962f5.png)

![三歪教你学Servlet 第30页插图](../assets/images/三歪教你学Servlet_p30_4_3bedee01.png)

---

ইຎ.ಘ઀ݷ޾ྋෑ๴ҁ/҂୏१ଚզ“/”ᕮੲӷᐿ᭗ᯈᒧݶ෸ڊሿ҅܃ᯈጱฎߺӞӻޫҘ
1. ፡᧡ጱ܃ᯈଶṛ҅᧡੪ᤩᭌೠ
2. *. ಘ઀ݷጱսضᕆ๋֗
Servletฉ੘ጱURLݢզֵአ᭗ᯈᒧ޾Servletݢզᤩฉ੘کग़ӻURLӤጱ֢አғ
1. ᵌᡐᗑᒊฎአՋԍᖫᑕ᧍᥺ٟጱ̓.php,.net,.aspਫᴬӤᦢᳯጱ᮷ฎݶӞӻᩒრ̈́
2. አᇙਧጱݸᖗ्กᇇ๦̓لݪᖽٟ̈́
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
2.3 Servletฎܔֺጱ
 
2.3.1 ԅՋԍServletฎܔֺጱ
 
<servlet>
  <servlet-name>Demo1</servlet-name>
  <servlet-class>zhongfucheng.web.Demo1</servlet-class>
</servlet>
<servlet-mapping>
  <servlet-name>Demo1</servlet-name>
  <url-pattern>*.jsp</url-pattern>
</servlet-mapping>
<servlet-mapping>
  <servlet-name>Demo1</servlet-name>
  <url-pattern>*.net</url-pattern>
</servlet-mapping>
<servlet-mapping>
  <servlet-name>Demo1</servlet-name>
  <url-pattern>*.asp</url-pattern>
</servlet-mapping>
<servlet-mapping>
  <servlet-name>Demo1</servlet-name>
  <url-pattern>*.php</url-pattern>
</servlet-mapping>

![三歪教你学Servlet 第31页插图](../assets/images/三歪教你学Servlet_p31_1_5d4df7d4.png)

---

ၨᥦ࢏ग़ེ੒Servletጱ᧗࿢҅Ӟᛱఘ٭ӥ҅๐ۓ࢏ݝڠୌӞӻServlet੒᨝҅Ԟ੪ฎ᧔҅Servlet੒᨝Ӟ
෮ڠୌԧ҅੪տḦኸࣁٖਂӾ҅ԅݸᖅጱ᧗࿢؉๐ۓ҅ፗک๐ۓ࢏ىᳮ̶
2.3.2 ྯེᦢᳯ᧗࿢੒᨝޾ߥଫ੒᨝᮷ฎෛጱ
 
੒ԭྯེᦢᳯ᧗࿢҅Servlet୚ක᮷տڠୌӞӻෛጱHttpServletRequest᧗࿢੒᨝޾Ӟӻෛጱ
HttpServletResponseߥଫ੒᨝҅ᆐݸਖ਼ᬯӷӻ੒᨝֢ԅ݇හփ᭓ᕳਙ᧣አጱServletጱservice()ො
ဩ҅serviceොဩٚ໑ഝ᧗࿢ොୗړڦ᧣አdoXXXොဩ̶
2.3.3 ᕚᑕਞقᳯ᷌
 
୮ग़ӻአಁᦢᳯServletጱ෸ײ҅๐ۓ࢏տԅྯӻአಁڠୌӞӻᕚᑕ̶୮ग़ӻአಁଚݎᦢᳯServletوՁ
ᩒრጱ෸ײ੪տڊሿᕚᑕਞقᳯ̶᷌
ܻڞғ
1. ইຎӞӻݒᰁᵱᥝग़ӻአಁوՁ҅ڞଫ୮ࣁᦢᳯᧆݒᰁጱ෸ײ҅ےݶྍ๢ګsynchronized (੒᨝)
{}
2. ইຎӞӻݒᰁӧᵱᥝوՁ҅ڞፗളࣁ doGet() ౲ᘏ doPost()ਧԎ.ᬯ໏ӧտਂࣁᕚᑕਞقᳯ᷌
2.4 load-on-startup
 
ইຎࣁ<servlet> زᔰӾᯈᗝԧӞӻ <load-on-startup> زᔰ҅ᮎԍWEBଫአᑕଧࣁސۖ෸҅੪տ
ᤰ᫹ଚڠୌServletጱਫֺ੒᨝̵զ݊᧣አServletਫֺ੒᨝ጱinit()ොဩ̶

![三歪教你学Servlet 第32页插图](../assets/images/三歪教你学Servlet_p32_1_571b7835.png)

---

֢አғ
1. ԅwebଫአٟӞӻInitServlet҅ᬯӻservletᯈᗝԅސۖ෸ᤰ᫹҅ԅෆӻwebଫአڠୌ஠ᥝጱහഝପ
ᤒ޾හഝ
2. ਠ౮ӞԶਧ෸ጱձۓ̓ਧ෸ٟ෭ப҅ਧ෸॓ղහഝ̈́
2.5 ࣁwebᦢᳯձ֜ᩒრ᮷ฎࣁᦢᳯServlet
 
୮֦ސۖTomcat֦҅ࣁᗑ࣎Ӥᬌفhttp://localhost:8080̶ԅՋԍտڊሿTomcatੜሞጱᶭᶎҘ
ᬯฎኧᗌ፜Servletԅ֦๐ۓጱѺ
౯ժض፡Ӟӥweb.xml෈կӾጱᯈᗝ,web.xml෈կᯈᗝԧӞӻᗌ፜Servlet
<servlet>
  <servlet-name>default</servlet-name>
  <servlet-class>org.apache.catalina.servlets.DefaultServlet</servlet-class>
  <init-param>
    <param-name>debug</param-name>
    <param-value>0</param-value>
  </init-param>
  <init-param>
    <param-name>listings</param-name>
    <param-value>false</param-value>
  </init-param>
  <load-on-startup>1</load-on-startup>
</servlet>
<servlet-mapping>
  <servlet-name>default</servlet-name>
  <url-pattern>/</url-pattern>
</servlet-mapping>

![三歪教你学Servlet 第33页插图](../assets/images/三歪教你学Servlet_p33_1_d2e730a5.png)

---

Ջԍݞ؉ᗌ፜ServletҘٿฎࣁweb.xml෈կӾತӧک܃ᯈጱزᔰጱURL҅ਙժጱᦢᳯ᧗࿢᮷ਖ਼Իᕳᗌ፜
Servlet॒ቘ҅Ԟ੪ฎ᧔҅ᗌ፜Servletአԭ॒ቘಅํٌ՜Servlet᮷ӧ॒ቘጱᦢᳯ᧗࿢
෬ᆐ౯᧔ԧࣁwebᦢᳯձ֜ᩒრ᮷ฎࣁᦢᳯServlet҅ᮎԍ౯ᦢᳯᶉாᩒრ̓๜ࣈࢶᇆ҅๜ࣈHTML෈
կ̈́Ԟฎࣁᦢᳯᬯӻᗌ፜Servlet̓DefaultServleẗ́
ᦤਫӞӥғ୮౯ဌํಋૡᯈᗝᗌ፜Servletጱ෸ײ҅ᦢᳯ๜ࣈࢶᇆฎݢզᦢᳯ஑کጱ
ሿࣁ౯ᛔ૩ᯈᗝӞӻᗌ፜Servlet,Demo1੪ฎ౯ಋૡᯈᗝጱᗌ፜Servlet҅ᥟፍധweb.xmlᯈᗝጱᗌ፜
Servlet
ӥᶎ౯ᖀᖅᦢᳯӞӥڟ಍ጱࢶᇆ҅ྌ෸ᬌڊጱฎDemo1ᬯӻServletٟӤጱٖ਻ԧ
    <servlet>
        <servlet-name>Demo1</servlet-name>
        <servlet-class>zhongfucheng.web.Demo1</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>Demo1</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>

![三歪教你学Servlet 第34页插图](../assets/images/三歪教你学Servlet_p34_1_b3b3d939.png)

---

௛ᕮғ෫ᦞࣁwebӾᦢᳯՋԍᩒრ̓۱ೡJSP̈́҅᮷ฎࣁᦢᳯServlet̶ဌํಋૡᯈᗝᗌ፜Servletጱ෸
ײ֦҅ᦢᳯᶉாࢶᇆ҅ᶉாᗑᶭ҅ᗌ፜Servletտࣁ֦webᒊᅩӾ੔ತᧆࢶᇆ౲ᗑᶭ҅ইຎํ੪ᬬࢧᕳ
ၨᥦ࢏҅ဌํ੪ಸ404Კ᧏
3. ServletConﬁg੒᨝
 
3.1ServletConﬁg੒᨝ํՋԍአҘ
 
᭗ᬦྌ੒᨝ݢզ᧛ݐweb.xmlӾᯈᗝጱڡত۸݇හ̶
ሿࣁᳯ᷌๶ԧ҅ԅՋԍ౯ժᥝ಩݇හמ௳නکweb.xml෈կӾޫҘ౯ժݢզፗളࣁᑕଧӾ᮷ݢզਧԎ݇
හמ௳҅൥کweb.xml෈կӾ݈ํՋԍঅ॒ޫҘ
অ॒੪ฎғᚆड़ᦏ֦ጱᑕଧๅےᅎၚ̓ๅഘᵱ࿢҅ๅදᯈᗝ෈կweb.xmlܨݢ҅ᑕଧդᎱӧአද̈́
3.2឴ݐweb.xml෈կᯈᗝጱ݇හמ௳
 
ԅDemo1ᬯӻServletᯈᗝӞӻ݇හ҅݇හݷฎname҅꧊ฎzhongfucheng

![三歪教你学Servlet 第35页插图](../assets/images/三歪教你学Servlet_p35_1_479b3a7d.png)

---

ࣁServletӾ឴ݐServletConﬁg੒᨝҅᭗ᬦServletConﬁg੒᨝឴ݐࣁweb.xml෈կᯈᗝጱ݇හ
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
<servlet>
  <servlet-name>Demo1</servlet-name>
  <servlet-class>zhongfucheng.web.Demo1</servlet-class>
  <init-param>
    <param-name>name</param-name>
    <param-value>zhongfucheng</param-value>
  </init-param>
</servlet>
<servlet-mapping>
  <servlet-name>Demo1</servlet-name>
  <url-pattern>/Demo1</url-pattern>
</servlet-mapping>

![三歪教你学Servlet 第36页插图](../assets/images/三歪教你学Servlet_p36_1_42ffcf91.jpeg)

![三歪教你学Servlet 第36页插图](../assets/images/三歪教你学Servlet_p36_2_d11f9313.png)

---

4. ServletContext੒᨝
 
4.1 ՋԍฎServletContext੒᨝Ҙ
 
୮Tomcatސۖጱ෸ײ҅੪տڠୌӞӻServletContext੒᨝̶ਙդᤒ፳୮ڹwebᒊᅩ
4.2 ServletContextํՋԍአҘ
 
1. ServletContext෬ᆐդᤒ፳୮ڹwebᒊᅩ҅ᮎԍಅํServlet᮷وՁ፳ӞӻServletContext੒᨝҅
ಅզServletԏᳵݢզ᭗ᬦServletContextਫሿ᭗ᦔ̶
2. ServletConﬁg឴ݐጱฎᯈᗝጱฎܔӻServletጱ݇හמ௳҅ServletContextݢզ឴ݐጱฎᯈᗝෆӻ
webᒊᅩጱ݇හמ௳
3. ڥአServletContext᧛ݐwebᒊᅩጱᩒრ෈կ
4. ਫሿServletጱ᫨ݎ̓አServletContext᫨ݎӧग़҅Ԇᥝአrequest᫨ݎ̈́
4.3 Servletԏᳵਫሿ᭗ᦔ
 
ServletContext੒᨝ݢզᤩᑍԏԅऒ੒᨝
کᬯ᯾ݢᚆํӞӻወᳯ҅ऒ੒᨝ฎՋԍޫҘٌਫऒ੒᨝ݢզᓌܔቘᥴ౮Ӟӻ਻࢏̓ᔄ֒ԭMapᵞݳ̈́
ਫሿServletԏᳵ᭗ᦔ੪ᥝአکServletContextጱsetAttribute(String name,Object obj)ොဩ҅
ᒫӞӻ݇හฎىᲫਁ҅ᒫԫӻ݇හฎ֦ᥝਂؙጱ੒᨝
ᬯฎDemo2ጱդᎱ
ᬯฎDemo3ጱդᎱ
//឴ݐکServletContext੒᨝
ServletContext servletContext = this.getServletContext();
String value = "zhongfucheng";
//MyName֢ԅىᲫਁ҅value֢ԅ꧊ਂᬰ   ऒ੒᨝̓ᔄࣳԭMapᵞݳ̈́
servletContext.setAttribute("MyName", value);

![三歪教你学Servlet 第37页插图](../assets/images/三歪教你学Servlet_p37_1_3c233a1a.jpeg)

---

ᦢᳯDemo3ݢզ឴ݐDemo2ਂؙጱמ௳҅՗ᘒਫሿग़ӻServletԏᳵ᭗ᦔ
4.4 ឴ݐwebᒊᅩᯈᗝጱמ௳
 
ইຎ౯మᥝᦏಅํጱServlet᮷ᚆड़឴ݐکᬳളහഝପጱמ௳҅ӧݢᚆࣁweb.xml෈կӾྯӻServletӾ᮷
ᯈᗝӞӥ҅ᬯ໏դᎱᰁॡय़ԧѺଚӬտด஑ᶋଉ㺨ࡢ̶ٞ֟
web.xml෈կඪ೮੒ෆӻᒊᅩᬰᤈᯈᗝ݇හמ௳̓ಅํServlet᮷ݢզݐکᧆ݇හמ௳̈́
Demo4դᎱ
ᦶӞӥDemo3ฎވᚆ೭ک҅ፘݶጱդᎱ
//឴ݐServletContext੒᨝
ServletContext servletContext = this.getServletContext();
//᭗ᬦىᲫਁ឴ݐਂؙࣁऒ੒᨝ጱ꧊
String value = (String) servletContext.getAttribute("MyName");
System.out.println(value);
<context-param>
  <param-name>name</param-name>
  <param-value>zhongfucheng</param-value>
</context-param>
//឴ݐکServletContext੒᨝
ServletContext servletContext = this.getServletContext();
//᭗ᬦݷᑍ឴ݐ꧊
String value = servletContext.getInitParameter("name");
System.out.println(value);

![三歪教你学Servlet 第38页插图](../assets/images/三歪教你学Servlet_p38_1_d44004bd.png)

![三歪教你学Servlet 第38页插图](../assets/images/三歪教你学Servlet_p38_2_0ff400a0.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
4.5 ᧛ݐᩒრ෈կ
 
᧛ݐᩒრᒫӞᐿොୗғ
 
ᒫӞᐿොୗғሿࣁ౯ᥝ᭗ᬦServlet111᧛ݐ1.pngࢶᇆ
//឴ݐکServletContext੒᨝
ServletContext servletContext = this.getServletContext();
//᭗ᬦݷᑍ឴ݐ꧊
String value = servletContext.getInitParameter("name");
System.out.println(value);

![三歪教你学Servlet 第39页插图](../assets/images/三歪教你学Servlet_p39_1_49e385da.png)

![三歪教你学Servlet 第39页插图](../assets/images/三歪教你学Servlet_p39_2_ae42ba63.png)

---

ೲ౯ժզڹጱොୗ҅դᎱଫᧆฎᬯ໏ጱ̶
୮౯ժᦢᳯጱ෸ײ҅ܩڊᲙԧѺ᧔ತӧک1.png෈կ
ᬯฎԅՋԍޫҘ౯ժզڹ᧛ݐ෈կጱ෸ײ҅ইຎᑕଧ޾෈կࣁݶӞ۱ݷ҅ݢզፗള᭗ᬦ෈կݷᑍ឴ݐ஑
کጱѺܻ҅ࢩஉᓌܔ҅զڹ౯ժٟጱᑕଧ᮷ฎ᭗ᬦJVM๶ᬩᤈጱ҅ᘒሿࣁ҅౯ժฎ᭗ᬦTomcat๶ᬩᤈ
ጱ
໑ഝwebጱፓ୯ᥢ᝜҅Servletᖫᦲݸጱclass෈կฎਂනࣁWEB-INF\classes෈կ४Ӿጱ
FileInputStream fileInputStream = new FileInputStream("1.png");
System.out.println(fileInputStream);

![三歪教你学Servlet 第40页插图](../assets/images/三歪教你学Servlet_p40_1_e362f56f.png)

![三歪教你学Servlet 第40页插图](../assets/images/三歪教你学Servlet_p40_2_93a397f8.png)

---

፡کᬯ᯾҅౯ժᎣ᭲ԧᥝᬰفclassesፓ୯Ӿ᧛ݐ෈կ҅ಅզ౯ժਖ਼դᎱද౮զӥොୗ
݄ٚ᧛ݐ෸҅੪ݎሿݢզ឴ݐک෈կԧ̶֕ฎሿࣁᳯ݈᷌๶ԧ҅౯᧛ݐ෈կጱ෸ײ᮷ᥝٟӤᕷ੒᪠ஆ҅
ᬯ໏ॡӧᅎၚԧ̶ᦶమӞӥ҅ইຎ౯ਖ਼ᧆ᧛ݐ෈կጱཛྷࣘᑏکٌ՜ጱwebᒊᅩӤ҅౯ጱդᎱ੪݈ᥝץද
ԧ̓ࢩԅwebᒊᅩጱݷਁӧӞ໏̶̈́
౯ժ᭗ᬦServletContext᧛ݐ੪ݢզ᭿عץදդᎱጱఘ٭҅ࢩԅServletContext੒᨝ฎ໑ഝ୮ڹwebᒊ
ᅩᘒኞ౮ጱ
դᎱইӥಅᐏғ
FileInputStream fileInputStream = new 
FileInputStream("D:\\zhongfucheng\\web\\WEB-
INF\\classes\\zhongfucheng\\web\\1.png");
System.out.println(fileInputStream);
//឴ݐکServletContext੒᨝
ServletContext servletContext = this.getServletContext();
//᧣አServletContextොဩ឴ݐک᧛ݐ෈կጱၞ
InputStream inputStream = servletContext.getResourceAsStream("/WEB-
INF/classes/zhongfucheng/web/1.png");

![三歪教你学Servlet 第41页插图](../assets/images/三歪教你学Servlet_p41_1_4833f378.png)

---

᧛ݐᩒრᒫԫᐿොୗғ
 
ইຎ౯ጱ෈կනࣁwebፓ୯ӥ҅ᮎԍ੪ᓌܔ஑ग़ԧѺ,ፗള᭗ᬦ෈կݷᑍ੪ᚆ឴ݐ
դᎱইӥಅᐏ
//឴ݐکServletContext੒᨝
ServletContext servletContext = this.getServletContext();
//᧣አServletContextොဩ឴ݐک᧛ݐ෈կጱၞ
InputStream inputStream = servletContext.getResourceAsStream("2.png");

![三歪教你学Servlet 第42页插图](../assets/images/三歪教你学Servlet_p42_1_c1de39a8.png)

![三歪教你学Servlet 第42页插图](../assets/images/三歪教你学Servlet_p42_2_fec02197.png)

---

᧛ݐᩒრᒫӣᐿොୗғ
 
᭗ᬦᔄᤰ᫹࢏᧛ݐᩒრ෈կ̶౯ጱ෈կනࣁԧsrcፓ୯ӥ̓Ԟݞ؉ᔄፓ୯̈́
դᎱইӥಅᐏ
౯ጱ෈կනࣁԧsrcፓ୯ӥጱ۱ӥ
//឴ݐکᔄᤰ᫹࢏
ClassLoader classLoader = Servlet111.class.getClassLoader();
//᭗ᬦᔄᤰ᫹࢏឴ݐک᧛ݐ෈կၞ
InputStream inputStream = classLoader.getResourceAsStream("3.png");

![三歪教你学Servlet 第43页插图](../assets/images/三歪教你学Servlet_p43_1_9e3f4c04.png)

![三歪教你学Servlet 第43页插图](../assets/images/三歪教你学Servlet_p43_2_3167b9b5.png)

![三歪教你学Servlet 第43页插图](../assets/images/三歪教你学Servlet_p43_3_e289ac78.png)

---

դᎱইӥ҅Ⴒے۱ݷ᪠ஆܨݢ̶
ܻڞғইຎ෈կॡय़҅੪ӧᚆአᔄᤰ᫹࢏ጱොୗ݄᧛ݐ҅տ੕ᛘٖਂფڊ
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
//឴ݐکᔄᤰ᫹࢏
ClassLoader classLoader = Servlet111.class.getClassLoader();
//᭗ᬦᔄᤰ᫹࢏឴ݐک᧛ݐ෈կၞ
InputStream inputStream = 
classLoader.getResourceAsStream("/zhongfucheng/web/1.png");

![三歪教你学Servlet 第44页插图](../assets/images/三歪教你学Servlet_p44_1_fc24f11d.png)

![三歪教你学Servlet 第44页插图](../assets/images/三歪教你学Servlet_p44_2_f13a0eca.jpeg)

---

Response੒᨝
 
1. response̵request੒᨝
 
Tomcatතکਮಁᒒጱhttp᧗࿢҅տᰒ੒ྯӞེ᧗࿢҅ړڦڠୌӞӻդᤒ᧗࿢ጱrequest੒᨝̵޾
դᤒߥଫጱresponse੒᨝
෬ᆐrequest੒᨝դᤒhttp᧗࿢҅ᮎԍ౯ժ឴ݐၨᥦ࢏൉Իᬦ๶ጱහഝ҅ತrequest੒᨝ܨݢ̶
response੒᨝դᤒhttpߥଫ҅ᮎԍ౯ժݻၨᥦ࢏ᬌڊහഝ҅ತresponse੒᨝ܨݢ̶
2. ՋԍฎHttpServletResponse੒᨝Ҙ
 
httpߥଫኧᇫாᤈ̵ਫ֛ٖ਻̵ၾ௳१̵Ӟӻᑮᤈᕟ౮̶HttpServletResponse੒᨝੪੗ᤰԧhttpߥ
ଫጱמ௳̶
3. HttpServletResponseጱଫአ
 
3.1᧣አgetOutputStream()ොဩݻၨᥦ࢏ᬌڊහഝ
 
᧣አgetOutputStream()ොဩݻၨᥦ࢏ᬌڊහഝ,getOutputStream()ොဩݢզֵአprint()Ԟݢզֵአ
write()҅ਙժํՋԍ܄ڦޫҘ౯ժᦶḵӞӥ̶դᎱইӥ
౮ۑᬌڊ҅অ؟ဌՋԍྷየ̶
//឴ݐکOutputStreamၞ
ServletOutputStream servletOutputStream = response.getOutputStream();
//ݻၨᥦ࢏ᬌڊහഝ
servletOutputStream.print("aaaa");

![三歪教你学Servlet 第45页插图](../assets/images/三歪教你学Servlet_p45_1_3c233a1a.jpeg)

---

౯ժᦶ፳ᬌڊӾ෈ᦶᦶ
ڊ୑ଉԧѺѺѺ
ԅՋԍտڊሿ୑ଉޫҘࣁioӾ౯ժ਍ᬦ҅outputStreamฎᬌڊԫᬰګහഝጱ҅print()ොဩളතԧӞӻ
ਁᒧԀ҅print()ොဩᥝ಩“Ӿࢵ”ද౮ԫᬰګහഝ҅TomcatֵአIOS 8859-1ᖫᎱ੒ٌᬰᤈ᫨ഘ,“Ӿࢵ”໑
๜੒ISO 8859-1ᖫᎱӧඪ೮̶ಅզڊሿԧ୑ଉ
౯ժٚ፡፡write()ොဩ҅ضݻၨᥦ࢏ᬌڊ᝕෈හഝ
ဌํᳯ᷌
        //឴ݐکOutputStreamၞ
        ServletOutputStream servletOutputStream = response.getOutputStream();
        //ݻၨᥦ࢏ᬌڊහഝ
        servletOutputStream.print("ӾࢵѺ");
response.getOutputStream().write("aaa".getBytes());

![三歪教你学Servlet 第46页插图](../assets/images/三歪教你学Servlet_p46_1_83e4bec7.png)

![三歪教你学Servlet 第46页插图](../assets/images/三歪教你学Servlet_p46_2_b1c0d4f8.png)

---

ٚᦶᦶᬌڊӾ෈හഝ
ᨩ֒Ԟဌํᳯ̶᷌
ԅՋԍֵአwrite()ොဩᚆड़ྋଉݻၨᥦ࢏ᬌڊӾ෈ޫҘ "֦অޚ౯ฎӾࢵ".getBytes() ᬯݙդᎱࣁ᫨౮
byte[]හᕟጱ෸ײἕᦊັጱฎgb2312ᖫᎱ҅ᘒ"֦অޚ౯ฎӾࢵ"ඪ೮gb2312ᖫᎱ҅ಅզݢզྋଉดᐏ
ڊ๶̶
֕ฎ҅ᑕଧᥝਫሿ᭗አ௔҅ଫᧆֵአጱฎUTF-8ᖫᎱ҅౯ժࣁਁᒧԀ᫨ഘ౮ਁᜓහᕟ෸೰ਧUTF-8ᖫ
Ꮁ҅፡፡տெԍ໏̶
অጱ҅౮ۑ಩ਙ൥౮ԤᎱԧѺѺѺ
response.getOutputStream().write("֦অޚ౯ฎӾࢵ".getBytes());
  response.getOutputStream().write("֦অޚ౯ฎӾࢵ".getBytes("UTF-8"));

![三歪教你学Servlet 第47页插图](../assets/images/三歪教你学Servlet_p47_1_5091eaea.png)

![三歪教你学Servlet 第47页插图](../assets/images/三歪教你学Servlet_p47_2_c303b128.png)

![三歪教你学Servlet 第47页插图](../assets/images/三歪教你学Servlet_p47_3_913af8cc.png)

---

ԅՋԍਙݒ౮ԧԤᎱޫҘܻࢩฎᬯ໏ጱғ౯ࣁݻ๐ۓ࢏ᬌڊጱӾ෈ฎUTF-8ᖫᎱጱ҅ᘒၨᥦ࢏᯻አጱฎ
GBK҅GBKమดᐏUTF-8ጱӾ෈හഝ҅ӧԤᎱ಍ௗޫѺ
෬ᆐইྌ҅౯ਖ਼ၨᥦ࢏ጱᖫᎱද౮UTF-8ᦶᦶ̶
ԤᎱᳯ݈᷌ᥴ٬ԧ̶ݢฎ҅ྯེᖫٟUTF-8ᑕଧ෸᮷ᥝ݄ᗑᶭӤදᖫᎱ໒ୗހҘᬯ໏กดӧݢᚆጱ̶
෬ᆐHTTPߥଫํ੒ၨᥦ࢏᧔กࢧᭆහഝฎՋԍᔄࣳጱၾ௳१҅ᮎԍHttpServletResponse੒᨝੪ଫᧆํ
ፘ੒ଫጱොဩޞᦫၨᥦ࢏ࢧᭆጱහഝᖫᎱ໒ୗฎՋԍ
ԭฎԒ੪݄ັತServlet API҅ತکԧᦡᗝၾ௳१ጱොဩ

![三歪教你学Servlet 第48页插图](../assets/images/三歪教你学Servlet_p48_1_881a97b3.png)

![三歪教你学Servlet 第48页插图](../assets/images/三歪教你学Servlet_p48_2_8203257b.png)

---

ၨᥦ࢏ࣁดᐏහഝ෸҅ᛔۖ಩ᶭᶎጱᖫᎱ໒ୗᗝഘ౮UTF-8҅ԤᎱᳯ᷌Ԟᥴ٬ԧ
ݚक़҅ᴻԧֵአHttpServletResponse੒᨝ᦡᗝၾ௳१ጱොဩ҅౯ݢզֵአhtmlጱຽᓋཛྷ೙Ӟӻhttpၾ
௳१҅ӥᶎฎդᎱғ
ԤᎱᳯ᷌Ԟݢզᥴ٬
//ᦡᗝ१מ௳҅ޞᦫၨᥦ࢏౯ࢧᭆጱහഝᖫᎱฎutf-8ጱ
response.setHeader("Content-Type", "text/html;charset=UTF-8");        
response.getOutputStream().write("֦অޚ౯ฎӾࢵ".getBytes("UTF-8"));
//឴ݐکservletOutputStream੒᨝
ServletOutputStream servletOutputStream = response.getOutputStream();
//ֵአmetaຽᓋཛྷ೙httpၾ௳१҅ޞᦫၨᥦ࢏ࢧᭆහഝጱᖫᎱ޾໒ୗ
servletOutputStream.write("<meta http-equiv='content-type' 
content='text/html;charset=UTF-8'>".getBytes());
servletOutputStream.write("౯ฎӾࢵ".getBytes("UTF-8"));

![三歪教你学Servlet 第49页插图](../assets/images/三歪教你学Servlet_p49_1_980a9929.png)

![三歪教你学Servlet 第49页插图](../assets/images/三歪教你学Servlet_p49_2_1d20dfdc.png)

---

3.2᧣አgetWriter()ොဩݻၨᥦ࢏ᬌڊහഝ
 
੒ԭgetWriter()ොဩᘒ᥺҅ฎWriterጱৼᔄ҅ᮎԍݝᚆݻၨᥦ࢏ᬌڊਁᒧහഝ҅ӧᚆᬌڊԫᬰګහഝ҅
ֵአgetWriter()ොဩᬌڊӾ෈හഝ,դᎱইӥғ
ࡅ᳼ݢᥠጱԪ݈ڊሿԧ҅౯݈ڊሿԤᎱԧ̶
ԅՋԍڊሿԤᎱԧޫҘኧԭTomcatฎक़ࢵՈጱٟ҅TomcatἕᦊጱᖫᎱฎISO 8859-1҅୮౯ժᬌڊӾ෈
හഝጱ෸ײ҅TomcatտׁഝISO 8859-1Ꮁᤒᕳ౯ժጱහഝᖫᎱ҅Ӿ෈ӧඪ೮ᬯӻᎱᤒޚ҅ಅզڊሿԧ
ԤᎱ
෬ᆐইྌ҅౯ᦡᗝӞӥᖫᎱӧ੪অԧހ҅դᎱইӥғ
౯ٚᦢᳯԧӞӥ҅౯ጱॠѺ፡᩸๶ๅԤԧѺ
ԅՋԍԤᎱᳯ᷌ᬮဌํᥴ٬Ҙᕡஞጱ๏݋տݎሿ҅౯ݝฎࣁӾ෈᫨ഘጱ෸ײ಩Ꮁᤒᦡᗝ౮UTF-8҅֕ฎ
ၨᥦ࢏๚஠ฎֵአUTF-8Ꮁᤒ๶ดᐏහഝጱޚ
অጱ҅౯ժ๶፡፡ၨᥦ࢏ጱᖫᎱ໒ୗ҅ຎᆐ҅ၨᥦ࢏ֵአGB2312ดᐏUTF-8ጱහഝ҅ӧԤᎱ಍ௗޫ
//឴ݐکprintWriter੒᨝
PrintWriter printWriter = response.getWriter();
printWriter.write("፡ਠܗਮᅩᩩѺ");
//ܻ๜ฎISO 8859-1ጱᖫᎱ҅౯ᦡᗝ౮UTF-8
response.setCharacterEncoding("UTF-8");
//឴ݐکprintWriter੒᨝
PrintWriter printWriter = response.getWriter();
printWriter.write("፡ਠܗਮᅩᩩѺ");

![三歪教你学Servlet 第50页插图](../assets/images/三歪教你学Servlet_p50_1_00e41c2e.png)

![三歪教你学Servlet 第50页插图](../assets/images/三歪教你学Servlet_p50_2_dc3dfb33.png)

---

ᬯӻᳯ᷌౯ժࣁӤᶎ૪ᕪฎํӷᐿොဩᥴ٬ԧֵ̓አ<meta> ຽᓋཛྷ೙ၾ௳१̵ᦡᗝၾ௳१̈́,Servletᬮ
൉׀ԧӞӻොဩᕳ౯ժ
অጱ҅౯ժٚ๶ᦢᳯӞӥ
෬ᆐServletํᮎԍग़ොဩᥴ٬ԤᎱᳯ᷌҅ฎӧฎํӞᐿฎ๋ᓌ׎ጱޫҘဌᲙѺӥᶎᬯӻොဩฎ๋ᓌ׎
ጱ҅ਙӧՐᦡᗝၨᥦ࢏አUTF-8ดᐏහഝٖ҅᮱ᬮ಩Ӿ෈᫨ᎱጱᎱᤒᦡᗝ౮UTF-8ԧ҅Ԟ੪ฎ
᧔҅ response.setContentType("text/html;charset=UTF-8"); ಩
response.setCharacterEncoding("UTF-8") ጱԪఘԞଗԧѺ
//ᦡᗝၨᥦ࢏አUTF-8ᖫᎱดᐏහഝ
response.setContentType("text/html;charset=UTF-8");

![三歪教你学Servlet 第51页插图](../assets/images/三歪教你学Servlet_p51_1_4ad4e0ad.png)

![三歪教你学Servlet 第51页插图](../assets/images/三歪教你学Servlet_p51_2_c9e4eac3.png)

---

ֵአgetWriter()ดᐏӾ෈හഝ҅ݝᵱᥝӞӻොဩ੪൥തԧѺ
3.3ਫሿ෈կӥ᫹
 
ӥ᫹ᩒრ౯ժࣁ෭ଉӾԞஉଉአ҅ਙฎெԍ؉کጱޫҘᥝᚆड़ᕳڦՈӥ᫹҅๐ۓ࢏੪ଫᧆํᬯӻᩒრ
ሿࣁ౯webᒊᅩӥํӞӻࢶᇆԧѺ
෬ᆐၨᥦ࢏ݎᭆಅํጱ᧗࿢᮷ฎ݄ತServletጱᦾ҅ᮎԍ౯੪ٟӞӻServlet҅୮ڦՈᦢᳯ౯ᬯӻServlet
ጱ෸ײ҅ਙժ੪ݢզӥ᫹౯ᬯӻࢶᇆԧѺ
javaጱ෈կӤփӥ᫹᮷ฎ᭗ᬦioၞ๶ਠ౮ጱ҅෬ᆐᥝӥ᫹ࢶᇆ҅Ḓضᥝᚆड़᧛ݐکਙ
//ᦡᗝၨᥦ࢏አUTF-8ᖫᎱดᐏහഝ҅
response.setContentType("text/html;charset=UTF-8");
//឴ݐکprintWriter੒᨝
PrintWriter printWriter = response.getWriter();
printWriter.write("፡ਠܗਮᅩᩩѺ");

![三歪教你学Servlet 第52页插图](../assets/images/三歪教你学Servlet_p52_1_1da9be9d.png)

![三歪教你学Servlet 第52页插图](../assets/images/三歪教你学Servlet_p52_2_5ffe6c10.png)

---

ޞᦫၨᥦ࢏҅౯ᥝӥ᫹ᬯӻ෈կ
ਖ਼᧛ݐکጱٖ਻ࢧᭆᕳၨᥦ࢏
୮౯ᦢᳯ෸҅ၨᥦ࢏੪൉ᐏӥ᫹ԧ̶
Ԟݢզ౮ۑ಑୏Ѻ
//឴ݐکᩒრጱ᪠ஆ
String path = this.getServletContext().getRealPath("/download/1.png");
//᧛ݐᩒრ
FileInputStream fileInputStream = new FileInputStream(path);
//឴ݐک෈կݷ,᪠ஆࣁኪᚏӤכਂฎ\\୵ୗጱ̶
String fileName = path.substring(path.lastIndexOf("\\") + 1);
//ᦡᗝၾ௳१҅ޞᦫၨᥦ࢏҅౯ᥝӥ᫹1.pngᬯӻࢶᇆ
response.setHeader("Content-Disposition", "attachment; filename="+fileName);
//಩᧛ݐکጱᩒრٟᕳၨᥦ࢏
int len = 0;
byte[] bytes = new byte[1024];
ServletOutputStream servletOutputStream = response.getOutputStream();
while ((len = fileInputStream.read(bytes)) > 0) {
  servletOutputStream.write(bytes, 0, len);
}
//ىᳮᩒრ
servletOutputStream.close();
fileInputStream.close();

![三歪教你学Servlet 第53页插图](../assets/images/三歪教你学Servlet_p53_1_282ae78d.png)

---

ሿࣁᳯ݈᷌ํԧ҅ইຎ౯෈կጱݷਁฎӾ෈ޫҘ
౯ժٚᦢᳯӞӥ҅ݎሿݷਁԤᎱԧҁெԍ᮷ฎԤᎱ҂

![三歪教你学Servlet 第54页插图](../assets/images/三歪教你学Servlet_p54_1_8e482958.jpeg)

![三歪教你学Servlet 第54页插图](../assets/images/三歪教你学Servlet_p54_2_82dd29db.png)

---

ԅԧᥴ٬෈կݷԤᎱ҅౯ժᥝᬰᤈURLᖫᎱ҅դᎱইӥғ
ེٚᦢᳯ෸҅෈կݷԤᎱᳯ᷌੪ᥴ٬ԧѺ
3.4ਫሿᛔۖڬෛ
 
զᥢਧጱ෸ᳵᦏᶭᶎڬෛ҅ๅෛᩒრ҅ᦏၨᥦ࢏ਫሿᛔۖڬෛ҅ᮎᙗਧ݈ฎץදၾ௳१ԧ̶
response.setHeader("Content-Disposition", "attachment; filename=" + 
URLEncoder.encode(fileName, "UTF-8"));

![三歪教你学Servlet 第55页插图](../assets/images/三歪教你学Servlet_p55_1_7bf7ddc9.png)

![三歪教你学Servlet 第55页插图](../assets/images/三歪教你学Servlet_p55_2_2a67fe02.png)

---

ԅԧๅঅጱ፡පຎ҅౯ժےف෸ᳵ꧊ᬰ݄
ྯӣᑁ෸ᳵ꧊੪տݎኞݒ۸
਍ਠӤᶎጱ҅অ؟ဌํՋԍአ҅ᛔ૩Ӥᗑጱ෸ײ᧡፡஑ᥠᬯ໏ጱӳᥜ̶ᛔۖڬෛ҅ᚆड़ਫሿᶭᶎጱ᪡
᫨̈́
౯ժጭᴭਠᗑᒊ҅உग़෸ײ᮷տ፡ᥠ̓ጭᴭ౮ۑ҅3ᑁݸᛔۖ᪡᫨....ٌ̈́҅ਫᬯӻ੪ฎአRefresh๶ਠ౮
ጱ̶
፡ӥපຎ
//ྯ3ᑁᛔۖڬෛᗑᶭӞེ
response.setHeader("Refresh", "3");
response.getWriter().write("time is :" + System.currentTimeMillis());
response.setContentType("text/html;charset=UTF-8");
response.getWriter().write("3ᑁݸ᪡᫨ᶭᶎ.....");
//ӣᑁݸ᪡᫨کindex.jspᶭᶎ݄҅webଫአጱฉ੘᪠ஆ౯ᦡᗝ౮/҅urlဌํٟӤଫአݷ
response.setHeader("Refresh", "3;url='/index.jsp'");

![三歪教你学Servlet 第56页插图](../assets/images/三歪教你学Servlet_p56_1_8bf6b419.png)

![三歪教你学Servlet 第57页插图](../assets/images/三歪教你学Servlet_p57_1_42ffcf91.jpeg)

![三歪教你学Servlet 第57页插图](../assets/images/三歪教你学Servlet_p57_2_1c96c075.png)

![三歪教你学Servlet 第57页插图](../assets/images/三歪教你学Servlet_p57_3_1b8a7cb9.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
3.5ᦡᗝᖨਂ
 
ၨᥦ࢏๜᫝੪ਂࣁ፳ᖨਂ๢ګ҅୮౯ᒫӞེᦢᳯindex.jsp෸҅ၨᥦ࢏ݻ๐ۓ࢏ݎԧӷེ᧗࿢̓Ӟӻฎᗑ
ᶭጱ҅Ӟӻฎࢶᇆጱ̈́
୮౯ᒫԫེᦢᳯindex.jspጱ෸ײ҅ၨᥦ࢏ਖ਼ࢶᇆᖨਂ᩸๶ԧѺࢶᇆӧฎ᯿ෛے᫹ጱ҅ฎ՗ᖨਂ᯾ᶎݐڊ
๶ጱ̶
؟ᙎᐥᔄࣳጱᗑᶭฎӧᚆݐᖨਂጱහഝጱ҅හഝ᮷ฎᥝӧෙๅෛጱ̶ӥᶎ౯੪ᐬྊᖨਂጱۑᚆ

![三歪教你学Servlet 第58页插图](../assets/images/三歪教你学Servlet_p58_1_94959626.png)

![三歪教你学Servlet 第58页插图](../assets/images/三歪教你学Servlet_p58_2_3c233a1a.jpeg)

![三歪教你学Servlet 第58页插图](../assets/images/三歪教你学Servlet_p58_3_71946ef5.png)

---

୮ᆐԧ҅ইຎᶭᶎํԶහഝӧᳩ๗ๅෛ֦҅੪ਖ਼ਙᦡᗝ౮ᖨਂ҅ᬯ໏ݢզ൉ṛ๐ۓ࢏ጱ௔ᚆ
3.6ਫሿහഝܴᖽ
 
ᗑᶭӤጱמ௳ᰁฎஉय़ጱ҅ইຎӧਖ਼හഝܴᖽٚࢧᭆᕳၨᥦ࢏҅ᬯ໏੪܈ړᘙᩇၞᰁ҅ሿࣁ౯ํӞᓤ෈
ᒍᥝᬌڊᕳၨᥦ࢏
ᦢᳯӞӥݢզ፡کܻ҅๶ጱᳩଶฎ201
ܴᖽጱܻቘฎՋԍҘ౯ժᎣ᭲getOutputStream()޾getWriter()᮷ฎፗള಩හഝᬌڊᕳၨᥦ࢏ጱ̶ሿ
ࣁ౯ᥝ؉ጱ੪ฎᦏහഝӧፗളᬌڊᕳၨᥦ࢏҅ضᦏ౯ܴᖽԧ҅ٚᬌڊᕳၨᥦ࢏̶java൉׀ԧGZIPܴᖽᔄ
ᕳ౯ժ
੪ᦏ౯ժֵአGZIPᔄ๶੒හഝܴᖽމ
//ၨᥦ࢏ํӣၾ௳१ᦡᗝᖨਂ҅ԅԧّ਻௔Ѻਖ਼ӣӻၾ௳१᮷ᦡᗝԧ
response.setDateHeader("Expires", -1);
response.setHeader("Cache-Control","no-cache");
response.setHeader("Pragma", "no-cache");
//ᬯ᯾ԅԧ፡පຎ
PrintWriter printWriter = response.getWriter();
printWriter.print("֦অࠡ" + new Date().toString());
response.setContentType("text/html;charset=UTF-8");
String ss = "fsdfhsdfhuisdhfusdhfuids" +
  "fsdfdsfsdfsdfdsfdafdsfhsdjfhsdjkfhkjds" +
  "fdsfjdslkfjsldkfjsdlkfjsdkfsdjkff" +
  "fsjdfjdsklfjdsklfjkldsfjlksdjflksdjflkds" +
  "dsjfklsdjflsdjfkldsfkjsdkfjsldkfjsdlfk" +
  "fdsjlkfjdslkfjsdlkfjlkasjflk";
response.getWriter().write("ܻ๶ጱᳩଶฎғ"+ss.getBytes().length+"</br>");
//ᬌڊᕳၨᥦ࢏
response.getWriter().write(ss);

![三歪教你学Servlet 第59页插图](../assets/images/三歪教你学Servlet_p59_1_d6b5ac40.png)

---

ԭฎ౯੪ࣁ຅᭜ڍහӤփ᭓ӻByteArrayOutputStreamᕳਙ
ᘒአGZIPOutputStreamٟහഝጱ෸ײ҅ฎ಩හഝٟکByteArrayOutputStreamӤጱ҅ᒵտᬮᥝ಩
හഝݐڊ๶ٟ҅ٚᕳၨᥦ࢏҅ԭฎ੪ӧᚆզ܇ݷٖ᮱ᔄጱොୗᕳGZIPOutputStream҅஠ᶳ಩
ByteArrayOutputStreamਧԎڊ๶҅
಩ܴᖽݸጱහഝݐڊ๶ٟ҅ᕳၨᥦ࢏
౯ժ๶੒ྲӞӥܴᖽڹጱय़ੜ޾ܴᖽݸጱय़ੜ
හഝጱᏟฎܴᖽԧ҅ᆐᘒ҅ԅՋԍ݈ԤᎱԧࠡҘஉᓌܔ҅෬ᆐ֦ܴᖽԧහഝ֦ٟ҅ᕳၨᥦ࢏҅ၨᥦ࢏ฎ
ӧᎣ֦᭲ᬯฎܴᖽݸጱහഝ҅ਙฎզྋଉጱොୗ಑୏හഝጱ̶ᬯ୮ᆐ᭜౮ԤᎱࠩѺ҅ሿࣁ౯ᥝޞᦫၨᥦ
࢏౯ᬯฎܴᖽහഝ
//GZIPጱ຅᭜ොဩᵱᥝӞӻOutputStreamৼᔄ੒᨝҅ᑪᒌߺӻ੒᨝ᭇݳ҅౯ժ፡ӥwrite()ොဩ
GZIPOutputStream gzipOutputStream = new GZIPOutputStream();
//ັ፡ԧӥAPI҅write()ളතጱฎbyte[]ᔄࣳጱ̶
gzipOutputStream.write();
//෬ᆐฎbyte[]ᔄࣳ҅ᮎԍ౯੪ᕳ՜ӞӻByteArrayOutputStream
GZIPOutputStream gzipOutputStream = new GZIPOutputStream(new 
ByteArrayOutputStream());
//ڠୌGZIPOutputStream੒᨝҅ᕳԨਙByteArrayOutputStream
ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
GZIPOutputStream gzipOutputStream = new 
GZIPOutputStream(byteArrayOutputStream);
//GZIP੒හഝܴᖽ҅GZIPٟفጱහഝฎכਂࣁbyteArrayOutputStreamӤጱ
gzipOutputStream.write(ss.getBytes());
//gzipOutputStreamํᖨ٫҅಩ᖨ٫Ⴔԧ҅ଚᶲ׎ىᳮၞ
gzipOutputStream.close();
//ਖ਼ܴᖽጱහഝݐڊ๶
byte[] bytes = byteArrayOutputStream.toByteArray();
//ਖ਼ܴᖽጱහഝٟᕳၨᥦ࢏
response.getOutputStream().write(bytes);

![三歪教你学Servlet 第60页插图](../assets/images/三歪教你学Servlet_p60_1_10d17724.png)

---

ེٚᦢᳯӞӥ
3.7ኞڊᵋ๢ࢶᇆ
 
ኞ౮ᵋ๢ࢶᇆᬯฎᶋଉଉᥠጱ̶ࣁ౯ժጭᴭጱ෸ײᕪଉᥝٟḵᦤᎱ҅ᘒᮎԶḵᦤᎱฎӞୟࢶᇆ҅੪ฎ᭗
ᬦHttpServletResponseٟᕳၨᥦ࢏ጱ̶
ᥝኞ౮Ӟୟࢶᇆ҅java൉׀ԧBuﬀeredImageᔄ׀౯ժֵአ
অጱ҅ሿࣁ౯ժࣁٖਂӾڠୌԧӞୟࢶᇆ҅ଚٟӤԧ12345̶ള፳҅౯ժᥝ಩ࢶᇆٟᕳၨᥦ࢏ԧ̶಩ࢶ
ᇆٟᕳၨᥦ࢏҅java݈൉׀ԧࢶᇆၞ̓ImageIÖ́ᕳ౯ժֵአ
౯ժ๶ᦢᳯӞӥ҅፡ӥࢶᇆᳩՋԍ໏
//ޞᦫၨᥦ࢏ᬯฎgzipܴᖽጱහഝ
response.setHeader("Content-Encoding","gzip");
//ٚਖ਼ܴᖽጱහഝٟᕳၨᥦ࢏
response.getOutputStream().write(bytes);
//ࣁٖਂӾኞ౮Ӟୟࢶᇆ,਼ԅ80,ṛԅ20҅ᔄࣳฎRGB
BufferedImage bufferedImage = new BufferedImage(80, 20, 
BufferedImage.TYPE_INT_RGB);
//឴ݐکᬯୟࢶᇆ
Graphics graphics = bufferedImage.getGraphics();
//ஃࢶᇆᦡᗝ᷏ᜋ޾ਁ֛
graphics.setColor(Color.BLUE);
graphics.setFont(new Font(null, Font.BOLD, 20));
//ஃࢶᇆӤٟහഝ҅ضٟӻ12345҅ཞࣖຽฎ0҅ᕒࣖຽฎ20̓ṛଶ̈́
graphics.drawString("12345", 0, 20);
//ᥝஃၨᥦ࢏ٟӞୟࢶᇆ҅ᮎᥝޞᦫၨᥦ࢏ࢧᭆጱᔄࣳฎӞୟࢶᇆ
response.setHeader("ContentType", "jpeg");
//java൉׀ԧࢶᇆၞᕳ౯ժֵአ҅ᬯฎӞӻૡٍᔄ
//಩ࢶᇆփᬰ݄҅ᔄࣳฎjpgٟ҅ᕳၨᥦ࢏
ImageIO.write(bufferedImage, "jpg", response.getOutputStream());

![三歪教你学Servlet 第61页插图](../assets/images/三歪教你学Servlet_p61_1_1ad8760e.png)

---

ᬯ໏ॡӪԧ҅౯ժ಩ᙧวද౮ጮᜋ፡፡
ٚ፡፡පຎ҅ᬯกดঅ፡ग़ԧ
অጱ҅౯ժጱࢶᇆහਁӧݢᚆฎՈૡٟጱ҅හਁଫᧆฎᵋ๢ԾኞጱѺᬯӻ੪ᓌܔԧ̶ሿࣁ౯ᥝኞ౮7֖
ጱᵋ๢හ҅ኞ౮ᵋ๢හጱොဩইӥ
ইຎᥝኞ౮Ӿ෈҅੪ತӾ෈ฉ੘ᤒܨݢ̶
3.6᯿ਧݻ᪡᫨
 
Ջԍฎ᯿ਧݻ᪡᫨ޫҘᅩڋӞӻ᩻᱾ള҅᭗Ꭳၨᥦ࢏᪡᫨کݚक़ጱӞӻᶭᶎ੪ݞ᯿ਧݻ᪡᫨̶ฎ᭗Ꭳၨ
ᥦ࢏݄᪡᫨҅ᬯஉ᯿ᥝ̶ᶭᶎԏᳵጱ᪡᫨ํӷᐿොୗғ᯿ਧݻ޾᫨ݎ҅ᛗԭՋԍ෸ײአ᯿ਧݻ҅Ջԍአ
᫨ݎ҅౯ࣁᦖਠHttpServletRequest੒᨝ጱ෸ײտᧇᕡ᧔ก̶
//಩ጮᜋऴ꧌ෆୟࢶᇆ
graphics.setColor(Color.white);
graphics.fillRect(0, 0, 80, 20);
private String makeNum() {
  Random random = new Random();
  //ᬯ໏੪տኞ౮0-7֖ጱᵋ๢හ҅ሿࣁᳯ݈᷌๶ԧ҅ইຎᵋ๢හӧड़7֖ޫҘইຎӧड़7֖҅౯ժےک7֖
੪ᤈԧ
  int anInt = random.nextInt(9999999);
  //ਖ਼හਁ᫨౮ฎਁᒧԀ
  String num = String.valueOf(anInt);
  //ڣෙ֖හํग़੝ӻ҅ӧड़੪ے
  StringBuffer stringBuffer = new StringBuffer();
  for (int i = 0; i < 7 - num.length(); i++) {
    stringBuffer.append("0");
  }
  return stringBuffer.append(num).toString();
}

![三歪教你学Servlet 第62页插图](../assets/images/三歪教你学Servlet_p62_1_59a028ee.png)

![三歪教你学Servlet 第62页插图](../assets/images/三歪教你学Servlet_p62_2_e18ff649.png)

---

౯ժ๶ֵአզӥHttpServletResponse੒᨝ጱ᯿ਧݻ
ࣁၨᥦ࢏ጱࣈ࣎ໄᦢᳯServlet222
᪡᫨کindex.jspᶭᶎ҅ࣈ࣎ໄݎኞԧݒ۸
౯ժٚ๶፡፡httpܐᦓݎኞԧՋԍ
՗ࢶӤ፡҅౯ժ፡کԧӷӻᇫாᎱ҅Ӟӻฎ302̶Ӟӻฎ200̶302ᇫாᎱࣁhttpܐᦓӾդᤒጱฎԁ෸᯿
ਧݻ̶Ԉӻֺৼғ౯ತᕉ஌঩ާ᧔ғᕳ౯Ӟղ᧗؃ᤒ҅౯ᥝࢧਹ̶ᕉ஌঩ާޞᦫ౯ғ౯ᬯ᯾ဌํ᧗؃
ᤒ֦݄҅ತᬀ੕ާމ̶ٚ፡ࢧ౯ᦢᳯSevlet222෸ғ౯ತServlet222҅Servlet222ޞᦫၨᥦ࢏ғ౯ဌํ֦
మᥝጱᩒრ֦҅ᥝጱᩒრࣁindex.jspᶭᶎӾ֦҅ᛔ૩݄ತމ̶
உ਻ฃ፡ڊ᯿ਧݻฎ᭗ᬦ302ᇫாᎱ޾᪡᫨ࣈ࣎ਫሿጱ̶ԭฎԒ҅౯ժᦡᗝhttpၾ௳१੪ݢզਫሿ᯿ਧ
ݻ᪡᫨
ٌਫsendRedirect()ොဩ੪ฎ੒setStatus()޾setHeader()ᬰᤈ੗ᤰܻ҅ቘ੪ฎsetStatus()޾
setHeader()
3.7getWriter޾getOutputStreamᕡᜓ
 
//᯿ਧݻکindex.jspᶭᶎ
response.sendRedirect("/zhongfucheng/index.jsp");
//ᦡᗝᇫாᎱฎ302
response.setStatus(302);
//HttpServletResponse಩ଉአጱᇫாᎱ੗ᤰ౮ᶉாଉᰁԧ҅ಅզ౯ժݢզֵአ
SC_MOVED_TEMPORARILYդᤒ፳302
response.setStatus(HttpServletResponse.SC_MOVED_TEMPORARILY);
//᪡᫨ጱࣈ࣎ฎindex.jspᶭᶎ
response.setHeader("Location", "/zhongfucheng/index.jsp");

![三歪教你学Servlet 第63页插图](../assets/images/三歪教你学Servlet_p63_1_80517b2a.png)

![三歪教你学Servlet 第63页插图](../assets/images/三歪教你学Servlet_p63_2_4f52d2f8.png)

![三歪教你学Servlet 第63页插图](../assets/images/三歪教你学Servlet_p63_3_ef1c090f.png)

---

1. getWriter()޾getOutputStream()ӷӻොဩӧᚆݶ෸᧣አ̶ইຎݶ෸᧣አ੪տڊሿ୑ଉ
2. ServletᑕଧݻServletOutputStream౲PrintWriter੒᨝Ӿٟفጱහഝਖ਼ᤩServlet୚ක՗
response᯾ᶎ឴ݐ҅Servlet୚කਖ਼ᬯԶහഝ୮֢ߥଫၾ௳ጱྋ෈҅ᆐݸٚӨߥଫᇫாᤈ޾ݱߥଫ
१ᕟݳݸᬌڊکਮಁᒒ̶ 
3. Servletጱserice()ොဩᕮ๳ݸ̓Ԟ੪ฎdoPost()౲ᘏdoGet()ᕮ๳ݸ̈́҅Servlet୚කਖ਼༄ັ
getWriter౲getOutputStreamොဩᬬࢧጱᬌڊၞ੒᨝ฎވ૪ᕪ᧣አᬦcloseොဩ҅ইຎဌํ҅
Servlet୚කਖ਼᧣አcloseොဩىᳮᧆᬌڊၞ੒᨝.
 
 
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
Request੒᨝

![三歪教你学Servlet 第64页插图](../assets/images/三歪教你学Servlet_p64_1_54b944c6.png)

![三歪教你学Servlet 第64页插图](../assets/images/三歪教你学Servlet_p64_2_3c233a1a.jpeg)

---

1. ՋԍฎHttpServletRequest
 
HttpServletRequest੒᨝դᤒਮಁᒒጱ᧗࿢҅୮ਮಁᒒ᭗ᬦHTTPܐᦓᦢᳯ๐ۓ࢏෸҅HTTP᧗࿢
१Ӿጱಅํמ௳᮷੗ᤰࣁᬯӻ੒᨝Ӿ҅୏ݎՈާ᭗ᬦᬯӻ੒᨝ጱොဩ҅ݢզ឴஑ਮಁᬯԶמ௳̶
ᓌܔ๶᧔҅ᥝ஑کၨᥦ࢏מ௳҅੪ತHttpServletRequest੒᨝
2. HttpServletRequestଉአොဩ
 
2.1 ឴஑ਮಁ๢̓ၨᥦ࢏̈́מ௳
 
getRequestURLොဩᬬࢧਮಁᒒݎڊ᧗࿢෸ጱਠෆURL̶
getRequestURIොဩᬬࢧ᧗࿢ᤈӾጱᩒრݷ᮱ړ̶
getQueryString ොဩᬬࢧ᧗࿢ᤈӾጱ݇හ᮱ړ̶
getPathInfoොဩᬬࢧ᧗࿢URLӾጱ᷐क़᪠ஆמ௳̶᷐क़᪠ஆמ௳ฎ᧗࿢URLӾጱ֖ԭServletጱ᪠
ஆԏݸ޾ັᧃ݇හԏڹጱٖ਻҅ਙզ“/”୏१̶
getRemoteAddrොဩᬬࢧݎڊ᧗࿢ጱਮಁ๢ጱIPࣈ࣎
getRemoteHostොဩᬬࢧݎڊ᧗࿢ጱਮಁ๢ጱਠෆԆ๢ݷ
getRemotePortොဩᬬࢧਮಁ๢ಅֵአጱᗑᕶᒒݗݩ
getLocalAddrොဩᬬࢧWEB๐ۓ࢏ጱIPࣈ̶࣎
getLocalNameොဩᬬࢧWEB๐ۓ࢏ጱԆ๢ݷ
2.2 ឴஑ਮಁ๢᧗࿢१
 
getHeaderොဩ
getHeadersොဩ 
getHeaderNamesොဩ 
2.3 ឴஑ਮಁ๢᧗࿢݇හ(ਮಁᒒ൉Իጱහഝ)
 
getParameterොဩ
getParameterValuesҁString name҂ොဩ
getParameterNamesොဩ 
getParameterMapොဩ
3. HttpServletRequestଫአ
 
3.1 ᴠፎ᱾
 
Ջԍฎᴠፎ᱾ޫҘྲইғ౯ሿࣁํၹᩊሴ๋ෛጱᩒრ҅మᥝ፡ၹᩊሴጱᥝࣁ౯ጱᗑᶭӤ፡̶ሿࣁڦጱᗑ
ᒊጱՈ፡ک౯ํၹᩊሴጱᩒრ҅మᥝ಩౯ጱᩒრᔌᩂࣁ՜ᛔ૩ጱᗑᒊӤ̶ᬯ໏౯ᇿਹጱᩒრ੪ᤩӞӻ
CTRL+C޾CTRL+VಶᩳԧҘᘒݍፎ᱾੪ฎӧᚆᤩ՜ժCRTL+C޾CRTL+V
 
ӥᶎ౯ཛྷ೙Ӟӥ࣋ว̶ሿࣁ౯ḒᶭضํӞӻ᩻᱾ള҅೰ݻ፳ၹᩊሴ๋ෛᩒრ

---

୮౯ᅩᬰ݄҅੪ᚆ፡کၹᩊሴ๋ෛᩒრԧ
ٌ՜ጱՈݢզ᭗ᬦ॔ګᔌᩂ౯ጱࣈ࣎҅නکਙժጱᗑᶭӤ
ᬯ໏౯੪ښӧ๶ࠩ̓౯ጱଠޞ֦๶ဌ፡ޫѺ̶̈́మᥝ፡౯ጱᩒრ҅੪஠ᶳᕪᬦ౯ጱḒᶭᅩᬰ݄፡̶
మᥝਫሿᬯ໏ጱපຎ҅੪ᥝ឴ݐRefererᬯӻၾ௳१҅ڣෙRefererฎӧฎ՗౯ጱḒᶭ๶ጱ̶ইຎӧฎ
՗౯ጱḒᶭ๶ጱ҅᪡᫨ࢧ౯ጱḒᶭ̶
//឴ݐکᗑᶭฎ՗ߺ᯾๶ጱ
String referer = request.getHeader("Referer");
//ইຎӧฎ՗౯ጱḒᶭ๶౲ᘏ՗ࣈ࣎ໄፗളᦢᳯጱ҅
if ( referer == null || 
!referer.contains("localhost:8080/zhongfucheng/index.jsp") ) {
  //ࢧکḒᶭ݄

![三歪教你学Servlet 第66页插图](../assets/images/三歪教你学Servlet_p66_1_1510a4bd.png)

![三歪教你学Servlet 第66页插图](../assets/images/三歪教你学Servlet_p66_2_8ddfadfe.png)

![三歪教你学Servlet 第66页插图](../assets/images/三歪教你学Servlet_p66_3_73d39e33.png)

---

Ḓضೲྋଉᶼమጱ҅ڦՈ՗Ḓᶭᅩڋ౯ጱᩒრ҅ᦢᳯ౯ၹᩊሴ๋ෛጱᩒრ
ᚆड़౮ۑᦢᳯکᩒრ
ইຎ౯ࣁၨᥦ࢏ፗളᬌفࣈ࣎̓ྌ෸Refererฎԅnullጱ̈́҅౯ժ๶፡፡
᪡ࢧکḒᶭӤ҅ӧᚆᦢᳯکၹᩊሴᩒრ
  response.sendRedirect("/zhongfucheng/index.jsp");
  return;
}
//ᚆಗᤈӥᶎጱ᧍ݙ҅᧔กฎ՗౯ጱḒᶭᅩڋᬰ๶ጱ҅ᮎဌᳯ᷌҅ᆙଉดᐏ
response.setContentType("text/html;charset=UTF-8");
response.getWriter().write("᪠ᷢ؉ԧXXXXxxxxxxxxxxxxxxxx");

![三歪教你学Servlet 第67页插图](../assets/images/三歪教你学Servlet_p67_1_a862ff0d.png)

![三歪教你学Servlet 第67页插图](../assets/images/三歪教你学Servlet_p67_2_eb46812c.png)

![三歪教你学Servlet 第67页插图](../assets/images/三歪教你学Servlet_p67_3_5eec1c5d.png)

---

ٚᦶᦶ҅ইຎڦՈᔌᩂԧ౯ጱᩒრurl҅ࣁਙጱᗑᶭӤ೯ԧӞӻᗑ࣎ޫ̶
ࣁڦՈᗑᶭӤᅩڋጱ෸ײ
݈᪡ࢧکԧ౯ጱḒᶭԧ̶
3.2ᤒܔ൉Իහഝ̓᭗ᬦpostොୗ൉Իහഝ̈́

![三歪教你学Servlet 第68页插图](../assets/images/三歪教你学Servlet_p68_1_931060cf.png)

![三歪教你学Servlet 第68页插图](../assets/images/三歪教你学Servlet_p68_2_ec260156.png)

![三歪教你学Servlet 第68页插图](../assets/images/三歪教你学Servlet_p68_3_83eec1ae.png)

![三歪教你学Servlet 第68页插图](../assets/images/三歪教你学Servlet_p68_4_83eec1ae.png)

---

<form action="/zhongfucheng/Servlet111" method="post">
    <table>
        <tr>
            <td>አಁݷ</td>
            <td><input type="text" name="username"></td>
        </tr>
        <tr>
            <td>ੂᎱ</td>
            <td><input type="password" name="password"></td>
        </tr>
        <tr>
            <td>௔ڦ</td>
            <td>
                <input type="radio" name="gender" value="ካ">ካ
                <input type="radio" name="gender" value="ঀ">ঀ
            </td>
        </tr>
        <tr>
            <td>ᆽঅ</td>
            <td>
                <input type="checkbox" name="hobbies" value="჋်">჋်
                <input type="checkbox" name="hobbies" value="᪒ྍ">᪒ྍ
                <input type="checkbox" name="hobbies" value="ᷢᗼ">ᷢᗼ
            </td>
        </tr>
        <input type="hidden" name="aaa" value="my name is zhongfucheng">
        <tr>
            <td>֦ጱ๶ᛔԭߺ᯾</td>
            <td>
                <select name="address">
                    <option value="ଠ૞">ଠ૞</option>
                    <option value="Ⴎࣉ">Ⴎࣉ</option>
                    <option value="۹Ղ">۹Ղ</option>
                </select>
            </td>
        </tr>
        <tr>
            <td>ᧇᕡ᧔ก:</td>
            <td>
                <textarea cols="30" rows="2" name="textarea"></textarea>
            </td>
        </tr>
        <tr>
            <td><input type="submit" value="൉Ի"></td>
            <td><input type="reset" value="᯿ᗝ"></td>
        </tr>
    </table>

---

ࣁServlet111Ӿ឴ݐک൉Իጱහഝ҅դᎱইӥ
ݻᤒܔᬌفහഝ
Servlet111஑کᤒܔଃᬦ๶ጱහഝ๋҅ݸጱӞӻහഝฎᵌᡐऒଃᬦ๶ጱ̶
//ᦡᗝrequestਁᒧᖫᎱጱ໒ୗ
request.setCharacterEncoding("UTF-8");
//᭗ᬦhtmlጱnameં௔҅឴ݐک꧊
String username = request.getParameter("username");
String password = request.getParameter("password");
String gender = request.getParameter("gender");
//॔ᭌ໛޾ӥ೉໛ํग़ӻ꧊҅឴ݐکग़ӻ꧊
String[] hobbies = request.getParameterValues("hobbies");
String[] address = request.getParameterValues("address");
//឴ݐک෈๜ऒጱ꧊
String description = request.getParameter("textarea");
//஑کᵌᡐऒጱ꧊
String hiddenValue = request.getParameter("aaa");
....ݱᐿSystem.out.println().......

![三歪教你学Servlet 第70页插图](../assets/images/三歪教你学Servlet_p70_1_f8b98b8e.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
3.4᩻᱾ളොୗ൉Իහഝ
 
ଉᥠጱgetොୗ൉Իහഝํғֵአ᩻᱾ള҅sendRedirect()
໒ୗইӥғ
౯ժ๶ֵአӞӥ҅᭗ᬦ᩻᱾ളਖ਼හഝଃᕳၨᥦ࢏
ࣁServlet111ളතහഝ
sendRedirect("servletጱࣈ࣎?݇හݷ="+݇හ꧊ &"݇හݷ="+݇හ꧊);
<a href="/zhongfucheng/Servlet111?username=xxx">ֵአ᩻᱾ളਖ਼හഝଃᕳၨᥦ࢏</a>

![三歪教你学Servlet 第71页插图](../assets/images/三歪教你学Servlet_p71_1_0b0f5a40.jpeg)

![三歪教你学Servlet 第71页插图](../assets/images/三歪教你学Servlet_p71_2_853c67df.png)

---

ဳ఺፡ၨᥦ࢏ૢӥ᥯
๐ۓ࢏౮ۑളතکၨᥦ࢏ݎᭆᬦ๶ጱහഝ
ଚӬ҅փᬌහഝก෈ጱڊሿࣁၨᥦ࢏ጱࣈ࣎ໄӤ
sendRedirect()޾᩻᱾ളᔄ֒҅ࣁᬯ᯾੪ӧᩣᬿԧ
3.5ᥴ٬Ӿ෈ԤᎱᳯ᷌
 
ᕡஞጱ๏݋տݎሿ҅౯ࣁ឴ݐᤒܔහഝጱ෸ײ҅ํᬯݙդᎱrequest.setCharacterEncoding("UTF-
8"); ҅ইຎဌํᬯݙդᎱ҅տݎኞՋԍԪޫҘ౯ժ፡፡̶
ٚ᯿ෛऴٟහഝ
//ളතզusernameԅ݇හݷଃᬦ๶ጱ꧊
String username = request.getParameter("username");
System.out.println(username);

![三歪教你学Servlet 第72页插图](../assets/images/三歪教你学Servlet_p72_1_2d8ed2f0.png)

![三歪教你学Servlet 第72页插图](../assets/images/三歪教你学Servlet_p72_2_27923473.png)

![三歪教你学Servlet 第72页插图](../assets/images/三歪教你学Servlet_p72_3_d4f627b5.png)

![三歪教你学Servlet 第72页插图](../assets/images/三歪教你学Servlet_p72_4_a6582d87.png)

---

ࣁ๐ۓ࢏ັ፡൉Իᬦ๶ጱහഝ҅ಅํጱӾ෈හഝ᮷ԤᎱԧ
๶ᬯ᯾౯ժ๶ړຉӞӥԤᎱጱܻࢩ҅ࣁڹᶎጱܗਮӾ౯૪ᕪՕᕨԧ҅Tomcat๐ۓ࢏ἕᦊᖫᎱฎISO 
8859-1҅ᘒၨᥦ࢏ֵአጱฎUTF-8ᖫᎱ̶ၨᥦ࢏ጱӾ෈හഝ൉Իᕳ๐ۓ࢏҅TomcatզISO 8859-1ᖫᎱ
੒Ӿ෈ᖫᎱ҅୮౯ࣁServlet᧛ݐහഝጱ෸ײ҅೭کጱ୮ᆐฎԤᎱ̶ᘒ౯ᦡᗝrequestጱᖫᎱԅUTF-8҅
ԤᎱ੪ᥴ٬ԧ̶
 
ളӥ๶ֵአgetොୗփ᭓Ӿ෈හഝ҅಩ᤒܔጱොୗද౮getܨݢ҅୮౯ժᦢᳯጱ෸ײ݈҅ڊሿԤᎱԧѺ

![三歪教你学Servlet 第73页插图](../assets/images/三歪教你学Servlet_p73_1_12b7f72e.png)

![三歪教你学Servlet 第73页插图](../assets/images/三歪教你学Servlet_p73_2_c791c770.png)

---

ԭฎ౯ೲᆙӤᶎጱොୗ҅಩request੒᨝ᦡᗝᖫᎱԅUTF-8ᦶᦶ
ᕮຎᬮฎԤᎱ̶ᬯฎԅՋԍޫҘ౯กก૪ᕪ಩ᖫᎱᦡᗝ౮UTF-8ԧ҅ೲᆙpostොୗ҅ԤᎱᳯ᷌૪ᕪᥴ٬
ԧѺ̶౯ժ๶፡፡get޾postොୗጱ܄ڦࣁߺҘԅՋԍpostොୗᦡᗝԧrequestᖫᎱ੪ݢզᥴ٬ԤᎱᳯ
᷌҅ᘒgetොୗӧᚆޫ̶
Ḓض౯ժ๶፡Ӟӥpostොဩฎெԍᬰᤈ݇හփ᭓ጱ̶୮౯ժᅩڋ൉Իೲᰵጱ෸ײ҅හഝ੗ᤰᬰԧForm 
DataӾ҅http᧗࿢Ӿ಩ਫ֛Ԇ֛ଃᬦ݄ԧ̓փᬌጱහഝᑍԏԅਫ֛Ԇ֛̈́҅෬ᆐrequest੒᨝੗ᤰԧ
http᧗࿢҅ಅզrequest੒᨝ݢզᥴຉکݎᭆᬦ๶ጱහഝ҅ԭฎݝᥝ಩ᖫᎱᦡᗝ౮UTF-8੪ݢզᥴ٬Ԥ
Ꮁᳯ᷌ԧ̶
ᘒgetොୗӧݶ҅ਙጱහഝฎ՗ၾ௳ᤈଃᬦ݄ጱ҅ဌํ੗ᤰکrequest੒᨝᯾ᶎ҅ಅզֵአrequestᦡᗝ
ᖫᎱฎ෫පጱ̶
request.setCharacterEncoding("UTF-8");
String name = request.getParameter("name");

![三歪教你学Servlet 第74页插图](../assets/images/三歪教你学Servlet_p74_1_b235b106.png)

![三歪教你学Servlet 第74页插图](../assets/images/三歪教你学Servlet_p74_2_c8f58f93.png)

---

ᥝᥴ٬getොୗԤᎱᳯ᷌Ԟӧᵙ҅౯ժ෬ᆐᎣ᭲TomcatἕᦊጱᖫᎱฎISO 8859-1҅ᮎԍgetොୗኧၾ௳
֛ଃᬦ݄ᕳၨᥦ࢏ጱ෸ײᙗਧฎአISO 8859-1ᖫᎱԧ̶
ӤᶎጱդᎱํԶᵙቘᥴ҅౯ኮୟࢶ᧔กӞӥғ
//ྌ෸஑کጱහഝ૪ᕪฎᤩISO 8859-1ᖫᎱݸጱਁᒧԀԧ҅ᬯӻฎԤᎱ
String name = request.getParameter("username");
//ԤᎱ᭗ᬦݍݻັISO 8859-1஑کܻতጱහഝ
byte[] bytes = name.getBytes("ISO8859-1");
//᭗ᬦܻতጱහഝ҅ᦡᗝྋᏟጱᎱᤒ҅຅ୌਁᒧԀ
String value = new String(bytes, "UTF-8");

![三歪教你学Servlet 第75页插图](../assets/images/三歪教你学Servlet_p75_1_21870255.png)

---

ᕪᬦ౯ժಋૡ᫨ഘ҅ٚ๶ᦢᳯӞӥ
 
অጱ҅౮ۑᥴ٬ധԤᎱᳯ᷌ԧ̶ᴻԧಋૡ᫨ഘ҅getොୗᬮݢզදTomcat๐ۓ࢏ጱᯈᗝ๶ᥴ٬ԤᎱ҅֕
ฎӧവគֵአ҅ᬯ໏ӧᅎၚ̶“
౯ժ᮷Ꭳ᭲TomcatἕᦊጱᖫᎱฎISO 8859-1,ইຎࣁTomcat๐ۓ࢏ጱᯈᗝӥද౮ฎUTF-8ጱᖫᎱ҅ᮎ
ԍ੪ᥴ٬๐ۓ࢏ࣁᥴຉහഝጱ෸ײ᭜౮ԤᎱᳯ᷌ԧ
ࣁ8080ᒒݗጱConnectorӤےف URIEncoding="utf-8" ҅ᦡᗝTomcatጱᦢᳯᧆᒒݗ෸ጱᖫᎱԅutf-
8҅՗ᘒᥴ٬ԤᎱ҅ᬯᐿදဩฎࢴਧֵአUTF-8ᖫᎱጱ
ᦡᗝԧᖫᎱݸ҅ဌํ؉ձ֜ಋૡ᫨ഘ҅౮ۑ೭کහഝ
<Connector port="8080" protocol="HTTP/1.1" 
           connectionTimeout="20000" 
           redirectPort="8443" URIEncoding="utf-8"/>

![三歪教你学Servlet 第76页插图](../assets/images/三歪教你学Servlet_p76_1_69ba05ff.png)

![三歪教你学Servlet 第76页插图](../assets/images/三歪教你学Servlet_p76_2_bdfd5b47.png)

---

୮ᆐԞํݚӞᐿද๐ۓ࢏ᖫᎱጱොୗ̶ᦡᗝTomcatጱᦢᳯᧆᒒݗ෸ጱᖫᎱԅᶭᶎጱᖫᎱ҅ᬯᐿදဩฎ
ᵋ፳ᶭᶎጱᖫᎱᘒݒ
ᦡᗝᖫᎱԅUTF-8
ེٚᦢᳯ
ಋٟ᩻᱾ളইຎᴫଃӾ෈݇හᳯ᷌҅ᥝURL᯿ٟ҅ࣁJSPܗਮӾտᦖک
௛ᕮғ
postොୗፗളදrequest੒᨝ጱᖫᎱ
getොୗᵱᥝಋૡ᫨ഘᖫᎱ
    <Connector port="8080" protocol="HTTP/1.1" 
               connectionTimeout="20000" 
               redirectPort="8443" useBodyEncodingForURI="true" />
request.setCharacterEncoding("UTF-8");
String name = request.getParameter("name");

![三歪教你学Servlet 第77页插图](../assets/images/三歪教你学Servlet_p77_1_dde00d04.png)

![三歪教你学Servlet 第77页插图](../assets/images/三歪教你学Servlet_p77_2_8bf75071.png)

---

getොୗԞݢզץදTomcat๐ۓ࢏ጱᖫᎱ҅ӧവគ҅ࢩԅտॡׁᩢ๐ۓ࢏ԧѺ
൉Իහഝᚆአpost੪አpost
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
3.6 ਫሿ᫨ݎ
 
ԏڹᦖᬦֵአresponseጱsendRedirect()ݢզਫሿ᯿ਧݻ҅؉کጱۑᚆฎᶭᶎ᪡᫨ֵ҅አrequestጱ
getRequestDispatcher.forward(request,response)ਫሿ᫨ݎ҅؉کጱۑᚆԞฎᶭᶎ᪡᫨҅՜ժํՋԍ
܄ڦޫҘሿࣁ౯ض๶᧔ӥ᫨ݎ
դᎱইӥಅᐏ
ᦢᳯServlet111
Ӥᶎ૪ᕪ᧔ԧ҅ݢզ᭗ᬦsendRedirect()᯿ਧݻݢզࣁᩒრੲ᮱Ⴒے݇හ൉Իහഝᕳ๐ۓ࢏̶ᮎԍ᫨ݎ
ᚆӧᚆ൉Իහഝᕳ๐ۓ࢏ޫҘᒼໜกดฎݢզጱ҅ଚӬֵአᬯᐿොဩᶋଉ᷇ᔺ
 
//឴ݐکrequestDispatcher੒᨝҅᪡᫨کindex.jsp
RequestDispatcher requestDispatcher = 
request.getRequestDispatcher("/index.jsp");
//᧣አrequestDispatcher੒᨝ጱforward()ਫሿ᫨ݎ,փفrequest޾responseොဩ
requestDispatcher.forward(request, response);

![三歪教你学Servlet 第78页插图](../assets/images/三歪教你学Servlet_p78_1_7bcf1140.jpeg)

![三歪教你学Servlet 第78页插图](../assets/images/三歪教你学Servlet_p78_2_e569c6a3.png)

---

ࣁᦖServletContextጱ෸ײ้҅ᕪ᧔ᬦServletԏᳵݢզ᭗ᬦServletContextਫሿ᭗ᦔ҅
ServletContextԞᚆᑍԏԅऒ੒᨝̶ᘒrequestԞݢզᑍԏԅऒ੒᨝҅ݝӧᬦServletContextጱऒฎ
ෆӻwebଫአ҅ᘒrequestጱऒՐՐդᤒӞེhttp᧗࿢
 
ӥᶎ౯ժ๶ֵአrequestਫሿServletԏᳵጱ᭗ᦔ҅Servlet111դᎱ
Servlet222դᎱ
ᦢᳯServlet111፡ӥපຎ
ইӤࢶಅᐏ҅Servlet222౮ۑ೭کԧrequest੒᨝ࣁServlet111ਂᬰጱහഝ̶
 
ሿࣁᳯ݈᷌๶ԧ҅౯ժݢզֵአServletContext޾requestਫሿServletԏᳵጱ᭗ᦔ҅ᮎԍ౯ժአߺӞ
ᐿޫҘӞᛱጱܻڞғݢզֵአrequest੪ੱݢᚆֵአrequest̶ࢩԅServletContextդᤒ፳ෆӻwebଫ
አֵ҅አServletContextտၾᘙय़ᰁጱᩒრ҅ᘒrequest੒᨝տᵋ፳᧗࿢ጱᕮ๳ᘒᕮ๳҅ᩒრտᤩࢧ
ත̶ֵአrequestऒᬰᤈServletԏᳵጱ᭗ᦔࣁ୏ݎӾฎᶋଉ᷇ᔺጱ̶
3.7 ᫨ݎጱ෸ଧࢶ
 
//զusernameԅىᲫਁਂzhongfucheng꧊
request.setAttribute("username", "zhongfucheng");
//឴ݐکrequestDispatcher੒᨝
RequestDispatcher requestDispatcher = 
request.getRequestDispatcher("/Servlet222");
//᧣አrequestDispatcher੒᨝ጱforward()ਫሿ᫨ݎ,փفrequest޾responseොဩ
requestDispatcher.forward(request, response);
//឴ݐکਂᬰrequest੒᨝ጱ꧊
String userName = (String) request.getAttribute("username");
//ࣁၨᥦ࢏ᬌڊᧆ꧊
response.getWriter().write("i am :"+userName);

![三歪教你学Servlet 第79页插图](../assets/images/三歪教你学Servlet_p79_1_8f74c203.png)

---

3.7.1᧗࿢᫨ݎጱᕡᜓ
 
ইຎࣁ᧣አforwardොဩԏڹ҅ࣁServletᑕଧӾٟفጱ᮱ړٖ਻૪ᕪᤩ፥ྋࣈփᭆکԧਮಁᒒ҅
forwardොဩਖ਼ಲڊIllegalStateException୑ଉ̶ Ԟ੪ฎ᧔ғӧᥝࣁ᫨ݎԏڹٟහഝᕳၨᥦ࢏
౯ժ๶ᦶᦶฎӧฎ፥ጱտڊሿ୑ଉ̶
ᦢᳯጱ෸ײ҅፡کၨᥦ࢏ݢզᬌڊහഝ҅Tomcatݸݣಲڊԧ୑ଉ
OutputStream outputStream = response.getOutputStream();
outputStream.write("--------------------------------------------".getBytes());
//ىᳮၞ҅Ꮯכᦏහഝکၨᥦ࢏Ӿ
outputStream.close();
//᪡᫨
request.getRequestDispatcher("/Foot").forward(request, response);

![三歪教你学Servlet 第80页插图](../assets/images/三歪教你学Servlet_p80_1_1a54cef5.png)

![三歪教你学Servlet 第80页插图](../assets/images/三歪教你学Servlet_p80_2_04264df2.png)

---

ইຎࣁ᧣አforwardොဩԏڹݻServlet୚කጱᖨ٫܄Ӿٟفԧٖ਻҅ݝᥝٟفکᖨ٫܄Ӿጱٖ਻ᬮဌํ
ᤩ፥ྋᬌڊکਮಁᒒ҅forwardොဩ੪ݢզᤩྋଉಗᤈܻ҅๶ٟفکᬌڊᖨ٫܄Ӿጱٖ਻ਖ਼ᤩႴᑮ҅֕
ฎ҅૪ٟفکHttpServletResponse੒᨝Ӿጱߥଫ१ਁྦྷמ௳כ೮ํප̶
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
3.8᫨ݎ޾᯿ਧݻጱ܄ڦ
 
3.8.1ਫᴬݎኞ֖ᗝӧݶ҅ࣈ࣎ໄӧݶ
 
᫨ݎฎݎኞࣁ๐ۓ࢏ጱ
᫨ݎฎኧ๐ۓ࢏ᬰᤈ᪡᫨ጱ҅ᕡஞጱ๏݋տݎሿ҅ࣁ᫨ݎጱ෸ײ҅ၨᥦ࢏ጱࣈ࣎ໄฎဌํݎ
ኞݒ۸ጱ҅ࣁ౯ᦢᳯServlet111ጱ෸ײ҅ܨֵ᪡᫨کԧServlet222ጱᶭᶎ҅ၨᥦ࢏ጱࣈ࣎ᬮ
ฎServlet111ጱ̶Ԟ੪ฎ᧔ၨᥦ࢏ฎӧᎣ᭲ᧆ᪡᫨ጱ֢ۖ҅᫨ݎฎ੒ၨᥦ࢏᭐กጱ̶᭗ᬦӤ
ᶎጱ᫨ݎ෸ଧࢶ౯ժԞݢզݎሿ҅ਫሿ᫨ݎݝฎӞེጱhttp᧗࿢҅Ӟེ᫨ݎӾrequest޾
response੒᨝᮷ฎݶӞӻ̶ᬯԞᥴ᯽ԧ҅ԅՋԍݢզֵአrequest֢ԅऒ੒᨝ᬰᤈServlet

![三歪教你学Servlet 第81页插图](../assets/images/三歪教你学Servlet_p81_1_3c233a1a.jpeg)

![三歪教你学Servlet 第81页插图](../assets/images/三歪教你学Servlet_p81_2_1135866f.png)

---

ԏᳵጱ᭗ᦔ̶
᯿ਧݻฎݎኞࣁၨᥦ࢏ጱ
᯿ਧݻฎኧၨᥦ࢏ᬰᤈ᪡᫨ጱ҅ᬰᤈ᯿ਧݻ᪡᫨ጱ෸ײ҅ၨᥦ࢏ጱࣈ࣎տݎኞݒ۸ጱ̶้ᕪ
Օᕨᬦғਫሿ᯿ਧݻጱܻቘฎኧresponseጱᇫாᎱ޾Location१ᕟݳᘒਫሿጱ̶ᬯฎኧၨᥦ
࢏ᬰᤈጱᶭᶎ᪡᫨ਫሿ᯿ਧݻտݎڊӷӻhttp᧗࿢҅requestऒ੒᨝ฎ෫පጱ҅ࢩԅਙӧฎ
ݶӞӻrequest੒᨝
3.8.2አဩӧݶ
 
உग़Ո᮷൥ӧႴ༩᫨ݎ޾᯿ਧݻጱ෸ײ҅ᩒრࣈ࣎ᑪᒌெԍ̶ٟํጱ෸ײᥝ಩ଫአݷٟӤ҅ํጱ෸ײӧ
አ಩ଫአݷٟӤ̶உ਻ฃ಩Ո൥ฝ̶ᦕ֘Ӟӻܻڞғᕳ๐ۓ࢏አጱፗള՗ᩒრݷ୏তٟ҅ᕳၨᥦ࢏አጱ
ᥝ಩ଫአݷٟӤ
request.getRequestDispatcher("/ᩒრݷ URI").forward(request,response)
᫨ݎ෸"/"դᤒጱฎ๜ଫአᑕଧጱ໑ፓ୯̓zhongfucheng̈́
response.send("/webଫአ/ᩒრݷ URI");
᯿ਧݻ෸"/"դᤒጱฎwebappsፓ୯
3.8.3ᚆड़݄ஃጱURLጱ᝜ࢱӧӞ໏
 
᫨ݎฎ๐ۓ࢏᪡᫨ݝᚆ݄ஃ୮ڹwebଫአጱᩒრ
᯿ਧݻฎ๐ۓ࢏᪡᫨҅ݢզ݄ஃձ֜ጱᩒრ
3.8.4փ᭓හഝጱᔄࣳӧݶ
 
᫨ݎጱrequest੒᨝ݢզփ᭓ݱᐿᔄࣳጱහഝ҅۱ೡ੒᨝
᯿ਧݻݝᚆփ᭓ਁᒧԀ
3.8.5᪡᫨ጱ෸ᳵӧݶ
 
᫨ݎ෸ғಗᤈک᪡᫨᧍ݙ෸੪տᒈڰ᪡᫨
᯿ਧݻғෆӻᶭᶎಗᤈਠԏݸ಍ಗᤈ᪡᫨
3.9 ᫨ݎ޾᯿ਧݻֵአߺӞӻҘ
 
໑ഝӤᶎ᧔กԧ᫨ݎ޾᯿ਧݻጱ܄ڦԞݢզஉ਻ฃ༷ೡڊ๶̶᫨ݎฎଃ፳᫨ݎڹጱ᧗࿢ጱ݇හጱ̶᯿ਧ
ݻฎෛጱ᧗࿢̶
َࣳጱଫአ࣋วғ
1. ᫨ݎ: ᦢᳯ Servlet ॒ቘӱۓ᭦ᬋ҅ᆐݸ forward ک jsp ดᐏ॒ቘᕮຎ҅ၨᥦ࢏᯾ URL ӧݒ
2. ᯿ਧݻ: ൉Իᤒܔ॒҅ቘ౮ۑݸ redirect کݚӞӻ jsp҅ᴠྊᤒܔ᯿॔൉Ի҅ၨᥦ࢏᯾ URL ݒԧ
3.10 RequestDispatcherٚ᧔ก
 
RequestDispatcher੒᨝᧣አforward()ݢզਫሿ᫨ݎӤᶎ૪ᕪ᧔ᬦԧ̶RequestDispatcherᬮํݚक़Ӟ
ӻොဩinclude()҅ᧆොဩݢզਫሿ۱ތ҅ํՋԍአޫҘ

---

౯ժࣁٟᗑᶭጱ෸ײ҅Ӟᛱᗑᶭጱ१᮱޾ੲ᮱ฎӧᵱᥝදݒጱ̶ইຎ౯ժग़ӻࣈොֵአServletᬌڊᗑ
१޾ᗑੲጱᦾ҅ᵱᥝ಩դᎱ᯿ෛٟӞ̶᭭ᘒֵአRequestDispatcherጱinclude()ොဩ੪ݢզਫሿ۱ތᗑ
१޾ᗑੲጱපຎԧ̶
 
౯ժ๶඙֢މѺሿࣁ౯ํᗑ१޾ᗑੲጱServlet
ֵአServlet111ਖ਼ᗑ१޾ᗑੲ۱ތ
ᦢᳯӞӥServlet111,౮ۑ಩ᗑ१޾ᗑੲ۱ތԧ
request.getRequestDispatcher("/Head").include(request, response);
response.getWriter().write("--------------------------------------------");
request.getRequestDispatcher("/Foot").include(request, response);

![三歪教你学Servlet 第83页插图](../assets/images/三歪教你学Servlet_p83_1_63c47c79.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
Cookie

![三歪教你学Servlet 第84页插图](../assets/images/三歪教你学Servlet_p84_1_d2fb52f5.png)

![三歪教你学Servlet 第84页插图](../assets/images/三歪教你学Servlet_p84_2_3c233a1a.jpeg)

![三歪教你学Servlet 第84页插图](../assets/images/三歪教你学Servlet_p84_3_a4698bf2.png)

---

1. Ջԍฎտᦾದ๞
 
च๜༷ஷ: ೰አಁ୏Ӟӻၨᥦ࢏҅ᦢᳯӞӻᗑᒊ,ݝᥝӧىᳮᧆၨᥦ࢏҅ӧᓕᧆአಁᅩڋग़੝ӻ᩻
᱾ള҅ᦢᳯग़੝ᩒრ҅ፗکአಁىᳮၨᥦ࢏҅ෆӻᬯӻᬦᑕ౯ժᑍԅӞེտᦾ.
2. ԅՋԍ౯ժᥝֵአտᦾದ๞Ҙ
 
տᦾ᪙᪵ದ๞ݢզᥴ٬౯ժஉग़உग़ᳯ̶᷌
ࣁᦞࣚጭᴭጱ෸ײ҅உग़෸ײտํӞӻੜ໛໛ᳯ֦ฎވᥝᛔۖጭᴭ҅୮֦ӥེጭᴭጱ෸ײ੪ӧአᬌ
فੂᎱԧ
໑ഝ౯զڹၨᥦᬦጱࠟߝ҅ሖ౯ࡅཻՋԍࠟߝҁᥝሖ౯ࡅཻ҅௛஑Ꭳ᭲”౯ฎ᧡“҂
3. Cookie

![三歪教你学Servlet 第85页插图](../assets/images/三歪教你学Servlet_p85_1_9790f4c5.png)

![三歪教你学Servlet 第85页插图](../assets/images/三歪教你学Servlet_p85_2_cb80a03e.png)

---

տᦾ᪙᪵ದ๞ํCookie޾Session҅Cookieದ๞ฎضڊሿጱ̶౯ժضᦖCookieದ๞މ̶
3.1 ՋԍฎCookie
 
CookieฎኧW3Cᕟᕢ൉ڊ๋҅෱ኧnetscapeᐒ܄ݎ઀ጱӞᐿ๢ګ
ᗑᶭԏᳵጱԻ԰ฎ᭗ᬦHTTPܐᦓփᬌහഝጱ҅ᘒHttpܐᦓฎ෫ᇫாጱܐᦓ̶෫ᇫாጱܐᦓฎՋԍ
఺௏ޫҘӞ෮හഝ൉Իਠݸ҅ၨᥦ࢏޾๐ۓ࢏ጱᬳള੪տىᳮེ҅ٚԻ԰ጱ෸ײᵱᥝ᯿ෛୌᒈෛጱ
ᬳള̶
๐ۓ࢏෫ဩᏟᦊአಁጱמ௳҅ԭฎԒ҅W3C੪൉ڊԧғᕳྯӞӻአಁ᮷ݎӞӻ᭗ᤈᦤ҅෫ᦞ᧡ᦢ
ᳯጱ෸ײ᮷ᵱᥝ൭ଃ᭗ᤈᦤ҅ᬯ໏๐ۓ࢏੪ݢզ՗᭗ᤈᦤӤᏟᦊአಁጱמ௳̶᭗ᤈᦤ੪ฎCookie
 
Cookieጱၞᑕғၨᥦ࢏ᦢᳯ๐ۓ࢏҅ইຎ๐ۓ࢏ᵱᥝᦕ୯ᧆአಁጱᇫா҅੪ֵአresponseݻၨᥦ࢏ݎ
ᭆӞӻCookie҅ၨᥦ࢏տ಩Cookieכਂ᩸๶̶୮ၨᥦ࢏ེٚᦢᳯ๐ۓ࢏ጱ෸ײ҅ၨᥦ࢏տ಩᧗࿢ጱᗑ
࣎ᬳݶCookieӞݶԻᕳ๐ۓ࢏̶
3.2Cookie API
 
CookieᔄአԭڠୌӞӻCookie੒᨝
responseളݗӾਧԎԧӞӻaddCookieොဩ҅ਙአԭࣁٌߥଫ१ӾीےӞӻፘଫጱSet-Cookie१
ਁྦྷ
requestളݗӾਧԎԧӞӻgetCookiesොဩ҅ਙአԭ឴ݐਮಁᒒ൉ԻጱCookie
ଉአጱCookieොဩғ
public Cookie(String name,String value)
setValueӨgetValueොဩ 
setMaxAgeӨgetMaxAgeොဩ 
setPathӨgetPathොဩ 
setDomainӨgetDomainොဩ
getNameොဩ

![三歪教你学Servlet 第86页插图](../assets/images/三歪教你学Servlet_p86_1_ab2bd895.png)

---

3.3ᓌܔֵአCookie
 
ڠୌCookie੒᨝҅ݎᭆCookieᕳၨᥦ࢏̵
ၨᥦ࢏๜᫝ဌํձ֜Cookie
ᦢᳯServlet1҅ٚࢧک෈կ४Ӿ҅ᬮฎဌํݎሿCookie҅ᬯฎԅՋԍޫҘ౯กกݻၨᥦ࢏ݎᭆԧӞӻ
Cookieጱ̶
 
ܻ๶ݎᭆCookieᕳၨᥦ࢏ฎᵱᥝᦡᗝCookieጱ෸ᳵጱ̶ࣁᕳၨᥦ࢏ԏڹ҅ᦡᗝӞӥCookieጱ෸ᳵ
ེٚᦢᳯ҅૪ᕪݎሿ෈կ४Ӿग़ԧӻCookieጱ෈๜ԧ
//ᦡᗝresponseጱᖫᎱ
response.setContentType("text/html;charset=UTF-8");
//ڠୌCookie੒᨝҅೰ਧݷᑍ޾꧊
Cookie cookie = new Cookie("username", "zhongfucheng");
//ݻၨᥦ࢏ᕳӞӻCookie
response.addCookie(cookie);
response.getWriter().write("౯૪ᕪݻၨᥦ࢏ݎᭆԧӞӻCookie");
//ᦡᗝCookieጱ෸ᳵ
cookie.setMaxAge(1000);

![三歪教你学Servlet 第87页插图](../assets/images/三歪教你学Servlet_p87_1_212a4a7b.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
4.Cookieᕡᜓ
 
4.1Cookieӧݢ᪜ऒݷ௔
 
உग़Ոࣁڡ਍ጱ෸ײݢᚆํӞӻወᳯғࣁᦢᳯServletጱ෸ײၨᥦ࢏ฎӧฎ಩ಅํጱCookie᮷ଃᬦ݄ᕳ
๐ۓ࢏҅տӧտץදԧڦጱᗑᒊጱCookie
 
ᒼໜฎވਧጱ̶Cookieٍํӧݢ᪜ऒݷ௔̶ၨᥦ࢏ڣෙӞӻᗑᒊฎވᚆ඙֢ݚӞӻᗑᒊጱCookieጱׁ
ഝฎऒݷ̶ಅզӞᛱ๶᧔҅୮౯ᦢᳯbaiduጱ෸ײ҅ၨᥦ࢏ݝտ಩baiduᶹݎጱCookieଃᬦ݄҅ᘒӧտ
ଃӤgoogleጱCookie̶
4.2 CookieכਂӾ෈
 
Ӥᶎ౯ժጱֺৼכਂጱฎ᝕෈ਁᒧ҅ӥᶎ౯ժ๶፡ӥכਂӾ෈ਁᒧտெԍ໏̶

![三歪教你学Servlet 第88页插图](../assets/images/三歪教你学Servlet_p88_1_c53b2cc8.png)

![三歪教你学Servlet 第88页插图](../assets/images/三歪教你学Servlet_p88_2_9ef93dcf.jpeg)

---

ᦢᳯServlet1҅অމ̶ڊ୑ଉԧѺ
Ӿ෈ંԭUnicodeਁᒧ҅᝕෈හഝASCIIਁᒧ҅Ӿ෈ܛ4ӻਁᒧ౲ᘏ3ӻਁᒧ҅᝕෈ܛ2ӻਁᒧ̶ᥴ٬ғ
CookieֵአUnicodeਁᒧ෸ᵱᥝ੒UnicodeਁᒧᬰᤈᖫᎱ̶
ེٚᦢᳯServlet1҅૪ᕪ಩Cookie౮ۑᶹݎᕳၨᥦ࢏ԧ
response.setContentType("text/html;charset=UTF-8");
PrintWriter printWriter = response.getWriter();
String name = "Ӿࢵ";
Cookie cookie = new Cookie("country", name);
cookie.setMaxAge(2000);
response.addCookie(cookie);
printWriter.write("౯ᶹݎԧӞӻCookie҅꧊כਂጱฎӾ෈හഝ");
//੒UnicodeਁᒧᬰᤈᖫᎱ
Cookie cookie = new Cookie("country", URLEncoder.encode(name, "UTF-8"));

![三歪教你学Servlet 第89页插图](../assets/images/三歪教你学Servlet_p89_1_79a307aa.png)

![三歪教你学Servlet 第89页插图](../assets/images/三歪教你学Servlet_p89_2_472b8d09.png)

![三歪教你学Servlet 第89页插图](../assets/images/三歪教你学Servlet_p89_3_dd1ffed1.png)

---

౯ժݎሿCookieכਂࣁᏝፏጱӾ෈හഝฎᕪᬦᖫᎱጱ҅ᮎԍ౯ժࣁݐڊCookieጱ෸ײᥝ੒Ӿ෈හഝᬰ
ᤈᥴᎱ
ݐڊਂᬰCookieጱ꧊
4.3Cookieጱํප๗
 
Cookieጱํප๗ฎ᭗ᬦsetMaxAge()๶ᦡᗝጱ̶
ইຎMaxAgeԅྋහ҅ၨᥦ࢏տ಩CookieٟکᏝፏӾ҅ݝᥝᬮࣁMaxAgeᑁԏڹ҅ጭᴭᗑᒊ෸ᧆ
Cookie੪ํප̓ӧᦞىᳮԧၨᥦ࢏ᬮฎኪᚏ̈́
ইຎMaxAgeԅᨮහ҅Cookieฎԁ෸௔ጱ҅Րࣁ๜ၨᥦ࢏ٖํප҅ىᳮၨᥦ࢏Cookie੪०පԧ҅
CookieӧտٟکᏝፏӾ̶Cookieἕᦊ꧊੪ฎ-1̶ᬯԞ੪ԅՋԍࣁ౯ᒫӞӻֺৼӾ҅ইຎ౯ဌᦡᗝ
Cookieጱํප๗҅ࣁᏝፏӾ੪ತӧک੒ଫጱ෈կ̶
ইຎMaxAgeԅ0҅ڞᤒᐏڢᴻᧆCookie̶Cookie๢ګဌํ൉׀ڢᴻCookie੒ଫጱොဩ҅಩
MaxAgeᦡᗝԅ0ᒵݶԭڢᴻCookie
4.4 Cookieጱץද޾ڢᴻ
 
Ӥᶎ౯ժ૪ᕪᎣ᭲ԧCookie๢ګဌํ൉׀ڢᴻCookieጱොဩ̶ٌਫᕡஞᅩ౯ժݢզݎሿ҅Cookie๢ګ
Ԟဌํ൉׀ץදCookieጱොဩ̶ᮎԍ౯ժெԍץදCookieጱ꧊ޫҘ
 
Cookieਂؙጱොୗᔄ֒ԭMapᵞݳ҅ইӥࢶಅᐏ
Cookie[] cookies = request.getCookies();
for (int i = 0; cookies != null && i < cookies.length; i++) {
  String name = cookies[i].getName();
  //ᕪᬦURLEncoding੪ᥝURLDecoding
  String value = URLDecoder.decode(cookies[i].getValue(), "UTF-8");
  printWriter.write(name + "------" + value);
}

![三歪教你学Servlet 第90页插图](../assets/images/三歪教你学Servlet_p90_1_1511d829.png)

---

Cookieጱݷᑍፘݶ҅᭗ᬦresponseႲےکၨᥦ࢏Ӿ҅տᥟፍܻ๶ጱCookie̶զcountryԅݷכਂጱ
ฎ%E4%B8%AD%E5%9B%BD҅ӥᶎ౯ٚզcountryԅݷ҅಩꧊දݒӞӥ̶
ེٚັ፡Cookieጱ෸ײ҅꧊૪ᕪදݒԧ҅֕ฎ෈կᬮฎᮎӞղ
ሿࣁ౯ᥝڢᴻᧆCookie҅಩MaxAgeᦡᗝԅ0҅ଚႲےکၨᥦ࢏Ӿܨݢ
ᦢᳯServlet҅ࣁᏝፏ૪ᕪತӧکCookieጱ෈կԧѺ
String name = "፡ਠܗਮ੪ᅩᩩ";
//੒UnicodeਁᒧᬰᤈᖫᎱ
Cookie cookie = new Cookie("country", URLEncoder.encode(name, "UTF-8"));
String name = "፡ਠܗਮ੪ᅩᩩ";
//੒UnicodeਁᒧᬰᤈᖫᎱ
Cookie cookie = new Cookie("country", URLEncoder.encode(name, "UTF-8"));
//Ӟਧӧᥝ஫ᦕႲےکၨᥦ࢏Ӿ
cookie.setMaxAge(0);
response.addCookie(cookie);
printWriter.write("౯ڢᴻԧᧆCookie");

![三歪教你学Servlet 第91页插图](../assets/images/三歪教你学Servlet_p91_1_3dc8ecdc.png)

![三歪教你学Servlet 第91页插图](../assets/images/三歪教你学Servlet_p91_2_9baca283.png)

![三歪教你学Servlet 第91页插图](../assets/images/三歪教你学Servlet_p91_3_9d5d69e0.png)

![三歪教你学Servlet 第91页插图](../assets/images/三歪教你学Servlet_p91_4_dd483f02.png)

---

ဳ఺ғڢᴻ҅ץදCookie෸҅ෛୌጱCookieᴻԧvalue̵maxAgeԏक़ጱಅํં௔᮷ᥝӨܻCookieፘ
ݶ̶ވڞၨᥦ࢏ਖ਼ᥤԅӧݶጱCookie҅ӧԨᥟፍ҅੕ᛘڢᴻץද०ᨳѺ౯ժ๶ᦶḵӞӥ಩̶
ӤᶎෛୌԧӞӻCookie҅౯ץදӥCookieጱٌ՜ં௔҅ٚڢᴻ҅፡ᚆވ಩Cookieڢᴻധ
String name = "፡ਠܗਮ੪ᅩᩩ";
//੒UnicodeਁᒧᬰᤈᖫᎱ
Cookie cookie = new Cookie("country", URLEncoder.encode(name, "UTF-8"));
//Ӟਧӧᥝ஫ᦕႲےکၨᥦ࢏Ӿ
cookie.setMaxAge(10000);
response.addCookie(cookie);

![三歪教你学Servlet 第92页插图](../assets/images/三歪教你学Servlet_p92_1_0ee99b0c.png)

![三歪教你学Servlet 第92页插图](../assets/images/三歪教你学Servlet_p92_2_8ac84c6a.png)

---

ᕮຎCookieᬮࣁᏝፏӾ
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
4.5 Cookieጱऒݷ
 
Cookieጱdomainં௔٬ਧᬩᤈᦢᳯCookieጱऒݷ̶domainጱ꧊ᥢਧԅ“.ऒݷ”
Cookieጱᵌᐺਞق๢ګ٬ਧCookieฎӧݢ᪜ऒݷጱ̶Ԟ੪ฎ᧔www.baidu.com޾www.google.co
mԏᳵጱCookieฎ԰ӧԻളጱ̶ܨֵฎݶӞᕆऒݷ҅ӧݶԫᕆऒݷԞӧᚆԻള҅Ԟ੪ฎ᧔ғwww.
goole.com޾www.image.goole.comጱCookieԞӧᚆᦢᳯ
౯ࣁ๜ࣈӤᯈᗝԧ3ӻᡦ೙Ԇ๢҅localhost,www.zhongfucheng.com,www.image.zhongfucheng
.com̓ইຎӧᎣ᭲ெԍᯈᗝ҅ࣁ౯Tomcatጱܗਮํ̈́
//Ӟਧӧᥝ஫ᦕႲےکၨᥦ࢏Ӿ
cookie.setPath("/ouzicheng");
cookie.setMaxAge(0);
response.addCookie(cookie);
printWriter.write("ڢᴻӞӻCookie");

![三歪教你学Servlet 第93页插图](../assets/images/三歪教你学Servlet_p93_1_aa467633.png)

![三歪教你学Servlet 第93页插图](../assets/images/三歪教你学Servlet_p93_2_a2ea4f55.jpeg)

---

౯አwww.zhongfucheng.comऒݷݎᭆԧӞӻCookieᕳၨᥦ࢏
Cookie cookie = new Cookie("name", "zhongfucheng");
cookie.setMaxAge(1000);
response.addCookie(cookie);
printWriter.write("ֵአwww.zhongfucheng.comऒݷႲےԧӞӻCookie");

![三歪教你学Servlet 第94页插图](../assets/images/三歪教你学Servlet_p94_1_fae57887.png)

![三歪教你学Servlet 第94页插图](../assets/images/三歪教你学Servlet_p94_2_fdb7adaa.png)

---

Ḓض҅ᦤกԧCookieӧݢ᪜ݷ௔҅localhostऒݷ೭ӧکwww.zhongfucheng.comᶹݎᕳၨᥦ࢏ጱ
Cookie
ֵٚአwww.image.zhongfucheng.comऒݷᦢᳯ,ᦤกܨֵӞᕆऒݷፘݶ҅ԫᕆऒݷӧݶ҅Ԟӧᚆ឴ݐ
کCookie

![三歪教你学Servlet 第95页插图](../assets/images/三歪教你学Servlet_p95_1_21ad6c05.png)

![三歪教你学Servlet 第95页插图](../assets/images/三歪教你学Servlet_p95_2_63591d8b.png)

---

୮ᆐֵ҅አwww.zhongfucheng.com୮ᆐᚆ឴ݐکCookie҅Cookie᭗ᬦ᧗࿢१ଃᕳ๐ۓ࢏
ሿࣁ౯૶๕ӞᕆऒݷፘݶጱᗑᶭCookieԏᳵݢզፘ԰ᦢᳯ̶Ԟ੪ฎ᧔www.image.zhongfucheng.co
mݢզ឴ݐکwww.zhongfucheng.comጱCookie੪ᵱᥝֵአکdomainොဩ̶
Cookie cookie = new Cookie("name", "ouzicheng");
cookie.setMaxAge(1000);
cookie.setDomain(".zhongfucheng.com");
response.addCookie(cookie);
printWriter.write("ֵአwww.zhongfucheng.comऒݷႲےԧӞӻCookie,ݝᥝӞᕆฎ
zhongfucheng.comܨݢᦢᳯ");

![三歪教你学Servlet 第96页插图](../assets/images/三歪教你学Servlet_p96_1_aec849c6.png)

![三歪教你学Servlet 第96页插图](../assets/images/三歪教你学Servlet_p96_2_5da3a609.png)

---

ֵአwww.zhongfucheng.comݎ૲ӞӻCookie
ֵአwww.image.zhongfucheng.comऒݷᦢᳯӞӥ̶ݎሿݢզ឴ݐکCookieԧ
 
4.6 Cookieጱ᪠ஆ
 
Cookieጱpathં௔٬ਧ꧋ᦜᦢᳯCookieጱ᪠ஆ̶Ӟᛱࣈ҅Cookieݎ૲ڊ๶҅ෆӻᗑᶭጱᩒრ᮷ݢզ
ֵአ̶ሿࣁ౯ݝమServlet1ݢզ឴ݐکCookieٌ҅՜ጱᩒრӧᚆ឴ݐ̶
 
ֵአServlet2ᶹݎӞӻCookieᕳၨᥦ࢏,ᦡᗝ᪠ஆԅ"/Servlet1"̶
ֵአServlet3ᦢᳯ๐ۓ࢏҅፡፡ၨᥦ࢏ฎވ಩CookieଃӤ̶ดᆐ҅ၨᥦ࢏ᦢᳯServlet3ଚဌํ಩Cookie
ଃӤ̶
Cookie cookie = new Cookie("username", "java");
cookie.setPath("/Servlet1");
cookie.setMaxAge(1000);
response.addCookie(cookie);
printWriter.write("ᧆCookieݝํServlet1឴ݐ஑ک");

![三歪教你学Servlet 第97页插图](../assets/images/三歪教你学Servlet_p97_1_d39491d3.png)

![三歪教你学Servlet 第97页插图](../assets/images/三歪教你学Servlet_p97_2_120238f7.png)

---

ֵአServlet1ᦢᳯ๐ۓ࢏҅፡፡ၨᥦ࢏ฎވ಩CookieଃӤ̶ᒼໜฎᙗਧጱѺ
4.7 Cookieጱਞقં௔
 
HTTPܐᦓӧՐՐฎ෫ᇫாጱ҅ᘒӬฎӧਞقጱѺইຎӧ૶๕CookieࣁᶋਞقܐᦓӾփᬌ҅ݢզᦡ
ᗝCookieጱsecureં௔ԅtrue҅ၨᥦ࢏ݝտࣁHTTPS޾SSLᒵਞقܐᦓӾփᬌᧆCookie̶
୮ᆐԧ҅ᦡᗝsecureં௔ӧտਖ਼Cookieጱٖ਻ےੂ̶ইຎమᥝכᦤਞق๋҅অֵአmd5ᓒဩےੂ
̓ݸᶎํ̶̈́

![三歪教你学Servlet 第98页插图](../assets/images/三歪教你学Servlet_p98_1_d9a38347.png)

![三歪教你学Servlet 第98页插图](../assets/images/三歪教你学Servlet_p98_2_548fa288.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
5. Cookieጱଫአ
 
5.1ดᐏአಁӤེᦢᳯጱ෸ᳵ
 
ٌਫ੪ฎྯེጭᴭጱ෸ײ҅ݐکCookieכਂጱ꧊҅ٚๅෛӥCookieጱ꧊̶
ᦢᳯSerlvetํӷᐿఘ٭
ᒫӞེᦢᳯ
૪ᕪᦢᳯᬦԧ
ق᮱դᎱইӥғ
SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd 
HH:mm:ss");
response.setContentType("text/html;charset=UTF-8");
PrintWriter printWriter = response.getWriter();

![三歪教你学Servlet 第99页插图](../assets/images/三歪教你学Servlet_p99_1_80babd6f.png)

![三歪教你学Servlet 第99页插图](../assets/images/三歪教你学Servlet_p99_2_3c233a1a.jpeg)

---

ೲᆙྋଉጱ᭦ᬋ๶ٟ҅ᑕଧၞᑕଫᧆฎᬯ໏ৼጱ̶ضڠୌCookie੒᨝҅ࢧᭆCookieᕳၨᥦ࢏̶ٚ
᭭ܲCookie҅ๅෛCookieጱ꧊̶
//឴ݐᗑᶭӤಅํጱCookie
Cookie[] cookies = request.getCookies();
//ڣෙCookieጱ꧊ฎވԅᑮ
String cookieValue = null;
for (int i = 0; cookies != null && i < cookies.length; i++) {
  //឴ݐکզtimeԅݷጱCookie
  if (cookies[i].getName().equals("time")) {
    printWriter.write("఍Ӥེጭᴭጱ෸ᳵฎғ");
    cookieValue = cookies[i].getValue();
    printWriter.write(cookieValue);
    cookies[i].setValue(simpleDateFormat.format(new Date()));
    response.addCookie(cookies[i]);
    //෬ᆐ૪ᕪತکԧ੪ݢզbreak஗ሾԧ
    break;
  }
}
//ইຎCookieጱ꧊ฎᑮጱ҅ᮎԍ੪ฎᒫӞེᦢᳯ
if (cookieValue == null) {
  //ڠୌӞӻCookie੒᨝҅෭๗ԅ୮ڹ෸ᳵ
  Cookie cookie = new Cookie("time", simpleDateFormat.format(new Date()));
  //ᦡᗝCookieጱኞ޸๗
  cookie.setMaxAge(20000);
  //response੒᨝ࢧᭆCookieᕳၨᥦ࢏
  response.addCookie(cookie);
  printWriter.write("఍ฎᒫӞེጭᴭࠡѺ");
}

---

֕ฎ҅ೲᆙӤᶎጱ᭦ᬋฎ؉ӧکጱѺࢩԅྯེᦢᳯServletጱ෸ײ᮷տᥟፍܻ๶ጱCookie҅ݐک
Cookieጱ꧊࿞ᬱ᮷ฎ୮ڹ෸ᳵ҅ᘒӧฎӤེכਂጱ෸ᳵ̶
౯ժഘӞӻ᭦ᬋٟғض༄ັҁ᭭ܲ҂ಅํCookieํဌํ౯ᥝጱ҅ইຎ஑ӧک౯మᥝጱCookie҅
Cookieጱ꧊ฎnull҅ᮎԍ੪ฎᒫӞེጭᴭ҅ԭฎ੪ํԧӤᶎጱդᎱԧ̶
౯ժ๶፡ӥපຎމѺ୮౯ᒫӞེጭᴭጱ෸ײ
CookieכਂࣁᏝፏӾ̶
ེٚᦢᳯServlet̶กดࣈ҅ݐکጱ੪ฎCookieጱ꧊

![三歪教你学Servlet 第101页插图](../assets/images/三歪教你学Servlet_p101_1_da580edc.png)

![三歪教你学Servlet 第101页插图](../assets/images/三歪教你学Servlet_p101_2_c890e358.png)

![三歪教你学Servlet 第101页插图](../assets/images/三歪教你学Servlet_p101_3_9e50ae2a.png)

---

5.2ดᐏӤེၨᥦᬦࠟߝ
 
౯੪զԡᔁԅֺৼԧѺḒضᦡᦇBook੒᨝
ᦡᦇӞӻᓌܔጱහഝପਂؙහഝ̶੪አLinkedHashMapᵞݳ̓໑ഝࠟߝጱidತԡᔁಅզአMap҅ڢද
᫾ग़ಅզአLinked̈́
    private String id ;
    private String name ;
    private String author;
    public Book() {
    }
    public Book(String id, String name, String author) {
        this.id = id;
        this.name = name;
        this.author = author;
    }
  ...ݱᐿset̵getොဩ
private static LinkedHashMap<String, Book> linkedHashMap = new 
LinkedHashMap();
//ᓌ۸୏ݎ॔๥ଶ҅bookጱid޾ࠟߝጱidፘݶ
static {
  linkedHashMap.put("1", new Book("1", "javaweb", "zhong"));
  linkedHashMap.put("2", new Book("2", "java", "fu"));
  linkedHashMap.put("3", new Book("3", "oracle", "cheng"));
  linkedHashMap.put("4", new Book("4", "mysql", "ou"));
  linkedHashMap.put("5", new Book("5", "ajax", "zi"));
}

![三歪教你学Servlet 第102页插图](../assets/images/三歪教你学Servlet_p102_1_13b0d4d4.png)

---

ดᐏᗑᶭӤಅํጱԡᔁ̓Ḓᶭ̈́
ള፳҅౯ժᥝ؉ጱ੪ฎᕳดᐏጱԡᔁ೯ӤӞӻ᩻᱾ള҅୮አಁᅩڋమ፡ጱԡᔁ෸҅੪᪡᫨کᧆԡᔁጱᧇ
ᕡמ௳ᶭᶎ
᩻᱾ളଫᧆ಩ԡጱidփ᭓ᬦ݄҅ӧᆐ॒ቘᶭᶎฎӧᎣ᭲አಁమ፡ጱฎߺӞ๜ԡጱѺ
//឴ݐکಅํԡᔁ
public static LinkedHashMap getAll() {
  return linkedHashMap;
}
printWriter.write("ᗑᶭӤಅํጱԡᔁғ"+"<br/>");
//೭کහഝପಅํጱԡ
LinkedHashMap<String, Book> linkedHashMap = DB.getAll();
Set<Map.Entry<String, Book>> entry = linkedHashMap.entrySet();
//ดᐏಅํጱԡکᗑᶭӤ
for (Map.Entry<String, Book> stringBookEntry : entry) {
  Book book = stringBookEntry.getValue();
  printWriter.write(book.getId() +"           "+ book.getName()+"<br/>");
}
//ดᐏಅํጱԡکᗑᶭӤ
for (Map.Entry<String, Book> stringBookEntry : entry) {
  Book book = stringBookEntry.getValue();
  printWriter.write("<a href='/ouzicheng/Servlet2?id=" + book.getId() + 
"''target=_blank' +" + book.getName() + "</a>");
  printWriter.write("<br/>");
}

![三歪教你学Servlet 第103页插图](../assets/images/三歪教你学Servlet_p103_1_4d511358.png)

---

ളතid҅ತکአಁమᥝ፡ߺӞ๜ԡ҅ᬌڊᧆԡጱᧇᕡמ௳
ᅩڋమᥝጱԡᔁ̶
஑کԡᔁጱᧇᕡמ௳
        String id = request.getParameter("id");
        //ኧԭbookጱid޾ࠟߝጱidฎӞᛘጱ̶឴ݐکአಁᅩڋጱԡ
        Book book = (Book) DB.getAll().get(id);
        //ᬌڊԡጱᧇᕡמ௳
        printWriter.write("ԡጱᖫݩฎғ" + book.getId()+"<br/>");
        printWriter.write("ԡጱݷᑍฎғ" + book.getName()+"<br/>");
        printWriter.write("ԡጱ֢ᘏฎғ" + book.getAuthor()+"<br/>");

![三歪教你学Servlet 第104页插图](../assets/images/三歪教你学Servlet_p104_1_ac7d37ab.png)

![三歪教你学Servlet 第104页插图](../assets/images/三歪教你学Servlet_p104_2_98168de5.png)

---

෬ᆐአಁᅩڋԧԡᔁ҅ᮎԍ๐ۓ࢏੪ଫᧆᶹݎCookieᕳၨᥦ࢏҅ᦕ֘አಁᅩڋԧᧆԡᔁ̶ሿࣁᳯ᷌๶
ԧ҅Cookieጱ꧊ଫᧆฎՋԍޫҘᦶమӞӥ҅இտᬮᥝ಩ၨᥦᬦጱԡᔁดᐏڊ๶҅ಅզአԡᔁጱidฎ๋অ
ӧᬦጱ̶మکԧአԡᔁጱid֢ԅCookieጱ꧊҅౯ժᬮᥝਧԎӞԶᥢڞѺ
 
౯ժݢᚆํᶋଉग़ጱԡᔁ҅ӧݢᚆ಩አಁၨᥦᬦጱԡᔁ᮷ดᐏڊ๶̶ಅզ౯ժਧԎݝᚆดᐏ3๜ၨᥦᬦ
ጱԡᔁ
ԡᔁጱid᮷ฎහਁ҅ইຎӧ؉ձ֜ץද҅ਂکCookie᯾ᬟݢᚆ੪ฎ231҅345҅123ྌᔄጱහਁ҅ᬯ໏
ݐڊ຤Ӟӻidጱ෸ײ੪܈ړᩇ۝ଚӬݸᶎᬮᥝڣෙᧆԡฎވਂࣁCookie᯾ᬟԧ҅ಅզ౯ժᥝ಩ਂؙک
Cookieጱԡᔁidړۆ᩸๶̶ಅզ౯ժਧԎ”_“֢ԅړᵍᒧ
ೲӤᶎጱଫአ҅౯ժጱ᭦ᬋଫᧆฎғض᭭ܲӥCookie҅፡ӥํဌํ౯ժమᥝጱCookie̶ইຎತکమᥝ
ጱCookie҅ᮎ੪ݐڊCookieጱ꧊
ݐڊԧCookieጱ꧊Ԟړپᐿఘ٭
1. Cookieጱ꧊ԅnull̓ፗള಩փفᬰ๶ጱid୮؉ฎCookieጱ꧊̈́
2. Cookieጱ꧊ᳩଶํ3ӻԧ̓಩ഭࣁ๋ݸጱid݄ധ҅಩փᬰ๶ጱidഭࣁ๋ڹᬟ̈́
3. Cookieጱ꧊૪ᕪ۱ތํփ᭓ᬰ๶ጱidԧ̓಩૪ᕪ۱ތጱidض݄ധ҅ٚ಩idഭࣁ๋ڹᶎ̈́
4. Cookieጱ꧊੪ݝํ1ӻ౲2ӻ҅ፗള಩idഭࣁ๋ڹᬟ
String bookHistory = null;
Cookie[] cookies = request.getCookies();
for (int i = 0; cookies != null && i < cookies.length; i++) {
  if (cookies[i].getName().equals("bookHistory")) {
    bookHistory = cookies[i].getValue();
  }
}
if (bookHistory == null) {
  return id;
}

![三歪教你学Servlet 第105页插图](../assets/images/三歪教你学Servlet_p105_1_bf1c8145.png)

---

ᬯԍರᚸਠԧ҅౯ժጱCookie꧊੪ࣁLinkedListᵞݳ᯾ᬟԧ̶ളӥ๶҅౯ժᥝ؉ጱ੪ฎ಩ᵞݳӾጱ꧊ݐ
ڊ๶҅೪ള౮ӞӻਁᒧԀ
অጱ҅౯ժሿࣁ૪ᕪਠ౮ԧCookie꧊ԧ̶ളӥ๶ᦡᗝCookieጱኞ޸ޮ๗҅ࢧᭆᕳၨᥦ࢏ܨݢ
෬ᆐ౯ժ૪ᕪ಩Cookieࢧᭆᕳၨᥦ࢏ԧ̶ᮎԍളӥ๶౯ժ੪ࣁḒᶭӤ឴ݐCookieጱ꧊҅ดᐏአಁၨᥦ
ᬦՋԍࠟߝ੪ᤈԧѺ
//ইຎCookieጱ꧊ӧฎnullጱ҅ᮎԍ੪ړᥴCookieጱ஑کԏڹጱid̶
String[] strings = bookHistory.split("\\_");
//ԅԧीڢ਻ฃଚӬᬮᥝڣෙidฎވਂࣁԭᧆਁᒧԀٖ-----౯ժֵአLinkedListᵞݳᤰ᫹ړᥴڊ๶ጱ
id
List list = Arrays.asList(strings);
LinkedList<String> linkedList = new LinkedList<>();
linkedList.addAll(list);
if (linkedList.contains(id)) {
  linkedList.remove(id);
  linkedList.addFirst(id);
}else {
  if (linkedList.size() >= 3) {
    linkedList.removeLast();
    linkedList.addFirst(id);
  } else {
    linkedList.addFirst(id);
  }
}
StringBuffer stringBuffer = new StringBuffer();
//᭭ܲLinkedListᵞݳ҅Ⴒےӻӥښᕚ“_”
for (String s : linkedList) {
  stringBuffer.append(s + "_");
}
//๋ݸӞӻزᔰݸᶎ੪ӧᵱᥝӥښᕚԧ
return stringBuffer.deleteCharAt(stringBuffer.length() - 1).toString();
String bookHistory = makeHistory(request, id);
Cookie cookie = new Cookie("bookHistory", bookHistory);
cookie.setMaxAge(30000);
response.addCookie(cookie);
printWriter.write("఍้ᕪၨᥦᬦጱࠟߝғ");
printWriter.write("<br/>");

---

অጱ҅౯ժ๶ᦶḵӞӥމѺѺ҅ᒫӞེᦢᳯḒᶭ҅ଚဌํၨᥦᬦጱࠟߝ
୮౯ᅩڋjavawebԡᔁٚᦢᳯḒᶭጱ෸ײ
ٚᅩڋajaxᆐݸᦢᳯḒᶭ
ٚᅩڋjavawebᆐݸᦢᳯḒᶭ
//ดᐏአಁၨᥦᬦጱࠟߝ
Cookie[] cookies = request.getCookies();
for (int i = 0; cookies != null && i < cookies.length; i++) {
  if (cookies[i].getName().equals("bookHistory")) {
    //឴ݐکጱbookHistoryฎ2_3_1ԏᔄጱ
    String bookHistory = cookies[i].getValue();
    //ೆᥴ౮ྯӞӻid꧊
    String[] ids = bookHistory.split("\\_");
    //஑کྯӞӻid꧊
    for (String id : ids) {
      //᭗ᬦidತکྯӞ๜ԡ
      Book book = linkedHashMap.get(id);
      printWriter.write(book.getName());
      printWriter.write("<br/>");
    }
    break;
  }
}

![三歪教你学Servlet 第107页插图](../assets/images/三歪教你学Servlet_p107_1_c1c0cb2d.png)

---

ᅩڋoracleᆐݸᦢᳯḒᶭ
অጱ҅ᕪᬦၥᦶ҅ᧆᑕଧଫᧆဌํՋԍᳯ᷌ԧѺ
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y

![三歪教你学Servlet 第108页插图](../assets/images/三歪教你学Servlet_p108_1_1bcce90a.png)

![三歪教你学Servlet 第108页插图](../assets/images/三歪教你学Servlet_p108_2_008c0e6d.png)

![三歪教你学Servlet 第108页插图](../assets/images/三歪教你学Servlet_p108_3_9390fc1e.png)

---

Session
 
1. ՋԍฎSession
 
Session ฎݚӞᐿᦕ୯ၨᥦ࢏ᇫாጱ๢ګ̶ӧݶጱฎCookieכਂࣁၨᥦ࢏Ӿ҅Sessionכਂࣁ๐ۓ
࢏Ӿ̶አಁֵአၨᥦ࢏ᦢᳯ๐ۓ࢏ጱ෸ײ҅๐ۓ࢏಩አಁጱמ௳զ຤ᐿጱ୵ୗᦕ୯ࣁ๐ۓ࢏҅ᬯ
੪ฎSession
ইຎ᧔Cookieฎ༄ັአಁ᫝Ӥጱ”᭗ᤈᦤ“๶Ꮯᦊአಁጱ᫝ղ҅ᮎԍSession੪ฎ᭗ᬦ༄ັ๐ۓ࢏Ӥጱ”ਮ
ಁกᕡᤒ“๶Ꮯᦊአಁጱ᫝ղጱ̶Sessionፘ୮ԭࣁ๐ۓ࢏ӾୌᒈԧӞղ“ਮಁกᕡᤒ”̶
2. ԅՋԍᥝֵአSessionದ๞Ҙ
 
SessionྲCookieֵአො׎҅Sessionݢզᥴ٬Cookieᥴ٬ӧԧጱԪఘ̓Sessionݢզਂؙ੒᨝҅
CookieݝᚆਂؙਁᒧԀ̶̶̈́
3. Session API
 
long getCreationTime();̓឴ݐSessionᤩڠୌ෸ᳵ̈́
String getId();̓឴ݐSessionጱid̈́
long getLastAccessedTime();̓ᬬࢧSession๋ݸၚ᪋ጱ෸ᳵ̈́
ServletContext getServletContext();̓឴ݐServletContext੒᨝̈́
void setMaxInactiveInterval(int var1);̓ᦡᗝSession᩻෸෸ᳵ̈́
int getMaxInactiveInterval();̓឴ݐSession᩻෸෸ᳵ̈́
Object getAttribute(String var1);̓឴ݐSessionં௔̈́
Enumeration getAttributeNames();̓឴ݐSessionಅํጱં௔ݷ̈́
void setAttribute(String var1, Object var2);̓ᦡᗝSessionં௔̈́
void removeAttribute(String var1);̓ᑏᴻSessionં௔̈́
void invalidate();̓ᲀྪᧆSession̈́
boolean isNew();̓ᧆSessionฎވԅෛጱ̈́
4.Session֢ԅऒ੒᨝

![三歪教你学Servlet 第109页插图](../assets/images/三歪教你学Servlet_p109_1_3c233a1a.jpeg)

---

՗ӤᶎጱAPI፡ڊ҅Sessionํ፳request޾ServletContextᔄ֒ጱොဩ̶ٌਫSessionԞฎӞӻऒ੒᨝̶
Session֢ԅӞᐿᦕ୯ၨᥦ࢏ᇫாጱ๢ګ҅ݝᥝSession੒᨝ဌํᤩᲀྪ҅Servletԏᳵ੪ݢզ᭗ᬦ
Session੒᨝ਫሿ᭗ᦔ
 
౯ժ๶ᦶᦶމ҅ࣁServlet4ӾᦡᗝSessionં௔
ࣁServlet5Ӿ឴ݐکSessionਂᬰ݄ጱં௔
ᦢᳯServlet4҅ٚᦢᳯServlet5
 
Ӟᛱ๶ᦖ҅୮౯ժᥝਂᬰጱฎአಁᕆڦጱහഝ੪አSession҅ᮎՋԍฎአಁᕆڦޫҘݝᥝၨᥦ࢏ӧى
ᳮ҅૶๕හഝᬮࣁ҅੪ֵአSession๶כਂ̶
5. Sessionጱኞ޸ޮ๗޾ํප๗
 
SessionࣁአಁᒫӞེᦢᳯ๐ۓ࢏Servlet҅jspᒵۖாᩒრ੪տᤩᛔۖڠୌ҅Session੒᨝כਂࣁٖਂ
᯾҅ᬯԞ੪ԅՋԍӤᶎጱֺৼݢզፗളֵአrequest੒᨝឴ݐ஑کSession੒᨝̶ইຎᦢᳯ
HTML,IMAGEᒵᶉாᩒრSessionӧտᤩڠୌ̶
 
Sessionኞ౮ݸ҅ݝᥝአಁᖀᖅᦢᳯ҅๐ۓ࢏੪տๅෛSessionጱ๋ݸᦢᳯ෸ᳵ҅෫ᦞฎވ੒Sessionᬰ
ᤈ᧛ٟ҅๐ۓ࢏᮷տᦊԅSessionၚ᪋ԧӞ̶ེ
 
ኧԭտํ᩼๶᩼ग़ጱአಁᦢᳯ๐ۓ࢏҅ࢩྌSessionԞտ᩼๶᩼ग̶़ԅԧᴠྊٖਂფڊ҅๐ۓ࢏տ಩ᳩ
෸ᳵဌํၚ᪋ጱSession՗ٖਂӾڢᴻ҅ᬯӻ෸ᳵԞ੪ฎSessionጱ᩻෸෸ᳵ̶
Sessionጱ᩻෸෸ᳵἕᦊฎ30ړᰦ҅ํӣᐿොୗݢզ੒Sessionጱ᩻෸෸ᳵᬰᤈץද
 
ᒫӞᐿොୗғࣁtomcat/conf/web.xml෈կӾᦡᗝ҅෸ᳵ꧊ԅ20ړᰦ҅ಅํጱWEBଫአ᮷ํප
//஑کSession੒᨝
HttpSession httpSession = request.getSession();
//ᦡᗝSessionં௔
httpSession.setAttribute("name", "፡ਠܗਮ੪ᥝᅩᩩѺѺ");
//឴ݐک՗Servlet4ጱSessionਂᬰ݄ጱ꧊
HttpSession httpSession = request.getSession();
String value = (String) httpSession.getAttribute("name");
System.out.println(value);

---

ᒫԫᐿොୗғࣁܔӻጱweb.xml෈կӾᦡᗝ҅੒ܔӻwebଫአํප҅ইຎํ٫ᑱ҅զᛔ૩ጱwebଫአԅ
ٵ̶
ᒫӣᐿොୗғ᭗ᬦsetMaxInactiveInterval()ොဩᦡᗝ
Sessionጱํප๗ӨCookieጱฎӧݶጱ
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
<session-config>
  <session-timeout>20</session-timeout>
</session-config> 
<session-config>
  <session-timeout>20</session-timeout>
</session-config> 
//ᦡᗝSession๋ᳩ᩻෸෸ᳵԅ60ᑁ҅ᬯ᯾ጱܔ֖ฎᑁ
httpSession.setMaxInactiveInterval(60);
System.out.println(httpSession.getMaxInactiveInterval());

![三歪教你学Servlet 第111页插图](../assets/images/三歪教你学Servlet_p111_1_a6d9076a.jpeg)

---

6. ֵአSessionਠ౮ᓌܔጱᨻᇔۑᚆ
 
౯ժᬮฎզԡᔁԅֺ҅ಅզݢզcopy“ดᐏၨᥦᬦጱࠟߝ“ֺৼ᮱ړጱդᎱ̶
ࣁᨻᇔ᫣ᶭᶎӤ҅឴ݐکአಁమԣጱԡᔁ̓አಁݢᚆӧܔమԣӞ๜ԡ҅ԭฎԒ҅੪አӞӻList਻࢏ᤰ᫹
ԡᔁ̈́҅ํԧғض᭭ܲCookie҅ٚڣෙฎވฎᒫӞེᦢᳯServletጱ᭦ᬋ௏᪠҅౯ժ੪ݢզض឴ݐک
Sessionጱં௔҅ইຎSessionጱં௔ԅnull҅ᮎԍ੪ฎᬮဌํᧆં௔
response.setContentType("text/html;charset=UTF-8");
PrintWriter printWriter = response.getWriter();
printWriter.write("ᗑᶭӤಅํጱԡᔁғ" + "<br/>");
//೭کහഝପಅํጱԡ
LinkedHashMap<String, Book> linkedHashMap = DB.getAll();
Set<Map.Entry<String, Book>> entry = linkedHashMap.entrySet();
//ดᐏಅํጱԡکᗑᶭӤ
for (Map.Entry<String, Book> stringBookEntry : entry) {
  Book book = stringBookEntry.getValue();
  String url = "/ouzicheng/Servlet6?id=" + book.getId();
  printWriter.write(book.getName());
  printWriter.write("<a href='" + url + "'>ᨻԣ</a>");
  printWriter.write("<br/>");
}
//஑کአಁమԣԡᔁጱid
String id = request.getParameter("id");
//໑ഝԡᔁጱidತکአಁమԣጱԡ
Book book = (Book) DB.getAll().get(id);

![三歪教你学Servlet 第112页插图](../assets/images/三歪教你学Servlet_p112_1_3c233a1a.jpeg)

---

ೲ౯ժྋଉጱ᭦ᬋ௏᪠ғضڠୌӞӻArrayList੒᨝҅಩ԡےکlistᵞݳӾ҅ᆐݸᦡᗝSessionጱં௔̶ᬯ
໏ฎᤈӧ᭗ጱ̶ྯེServletᤩᦢᳯጱ෸ײ᮷տڠୌӞӻArrayListᵞݳ҅ԡᔁտᤩړݎکӧݶጱArrayList
Ӿ̶݄ಅզӥᶎጱդᎱฎӧᤈጱѺ
෬ᆐአಁ૪ᕪᨻԣԧԡᔁ҅ᮎԍԞଫᧆᕳ൉׀ᶭᶎดᐏአಁᨻԣᬦߺԶԡᔁ
//឴ݐکSession੒᨝
HttpSession httpSession = request.getSession();
//ኧԭአಁݢᚆమԣग़๜ԡጱ҅ಅզ౯ժአӞӻ਻࢏ᤰ፳ԡᔁ
List list = (List) httpSession.getAttribute("list");
if (list == null) {
  list = new ArrayList();
  //ᦡᗝSessionં௔
  httpSession.setAttribute("list",list);
}
//಩ԡᔁےفکlistᵞݳӾ
list.add(book);
//஑کአಁమԣԡᔁጱid
String id = request.getParameter("id");
//໑ഝԡᔁጱidತکአಁమԣጱԡ
Book book = (Book) DB.getAll().get(id);
//឴ݐکSession੒᨝
HttpSession httpSession = request.getSession();
//ڠୌListᵞݳ
List list = new ArrayList();
list.add(book);
httpSession.setAttribute("list", list);
//஑کአಁమԣԡᔁጱid
String id = request.getParameter("id");
//໑ഝԡᔁጱidತکአಁమԣጱԡ
Book book = (Book) DB.getAll().get(id);
//឴ݐکSession੒᨝
HttpSession httpSession = request.getSession();

---

ڜڊአಁᨻԣᬦጱԡᔁ
පຎইӥ
7.Sessionጱਫሿܻቘ
 
አሿ᨝᧔กᳯ᷌҅౯ࣁServlet4ӾጱդᎱᦡᗝԧSessionጱં௔
//ኧԭአಁݢᚆమԣग़๜ԡጱ҅ಅզ౯ժአӞӻ਻࢏ᤰ፳ԡᔁ
List list = (List) httpSession.getAttribute("list");
if (list == null) {
  list = new ArrayList();
  //ᦡᗝSessionં௔
  httpSession.setAttribute("list",list);
}
//಩ԡᔁےفکlistᵞݳӾ
list.add(book);
String url = "/ouzicheng/Servlet7";
response.sendRedirect(url);
//ᥝ஑کአಁᨻԣᬦߺԶԡᔁ҅஑کSessionጱં௔᭭ܲܨݢ
HttpSession httpSession = request.getSession();
List<Book> list = (List) httpSession.getAttribute("list");
if (list == null || list.size() == 0) {
  printWriter.write("੒ӧ֦᩸҅ᬮဌํԣᬦձ֜ࠟߝ");
} else {
  printWriter.write("఍ᨻԣᬦզӥࠟߝғ");
  printWriter.write("<br/>");
  for (Book book : list) {
    printWriter.write(book.getName());
    printWriter.write("<br/>");
  }
}
//஑کSession੒᨝
HttpSession httpSession = request.getSession();
//ᦡᗝSessionં௔
httpSession.setAttribute("name", "፡ਠܗਮ੪ᥝᅩᩩѺѺ");

---

ള፳ࣁServlet7಩Sessionጱં௔ݐڊ๶
ᛔᆐࣈ҅౯ժᚆݐکࣁServlet4ӾSessionᦡᗝጱં௔
ള፳҅౯ࣁၨᥦ࢏ӾෛୌӞӻտᦾེ҅ٚᦢᳯServlet7
ݎሿಸԧᑮ೰ᰒ୑ଉጱᲙ᧏
ሿࣁᳯ᷌๶ԧғ๐ۓ࢏ฎই֜ਫሿӞӻsessionԅӞӻአಁၨᥦ࢏๐ۓጱҘഘӻ᧔ဩғԅՋԍ๐ۓ࢏ᚆ
ड़ԅӧݶጱአಁၨᥦ࢏൉׀ӧݶsessionҘ
 
HTTPܐᦓฎ෫ᇫாጱ҅SessionӧᚆׁഝHTTPᬳള๶ڣෙฎވԅݶӞӻአಁ̶ԭฎԒғ๐ۓ࢏ݻአಁ
ၨᥦ࢏ݎᭆԧӞӻݷԅJESSIONIDጱCookie҅ਙጱ꧊ฎSessionጱid꧊̶ٌਫSessionׁഝCookie๶ᦩ
ڦฎވฎݶӞӻአಁ̶
 
ᓌܔ๶᧔ғSession ԏಅզݢզᦩڦӧݶጱአಁׁ҅ᶌጱ੪ฎCookie
 
ᧆCookieฎ๐ۓ࢏ᛔۖᶹݎᕳၨᥦ࢏ጱ҅ӧአ౯ժಋૡڠୌጱ̶ᧆCookieጱmaxAge꧊ἕᦊฎ-1҅Ԟ
੪ฎ᧔Ր୮ڹၨᥦ࢏ֵአ҅ӧਖ਼ᧆCookieਂࣁᏝፏӾ
 
౯ժ๶എӞഎ௏᪠ၞᑕғ୮౯ժᦢᳯServlet4ጱ෸ײ҅๐ۓ࢏੪տڠୌӞӻSession੒᨝҅ಗᤈ౯ժጱ
ᑕଧդᎱ҅ଚᛔۖᶹݎӻCookieᕳአಁၨᥦ࢏
୮౯ժአݶӞӻၨᥦ࢏ᦢᳯServlet7ጱ෸ײ҅ၨᥦ࢏տ಩Cookieጱ꧊᭗ᬦhttpܐᦓଃᬦ݄ᕳ๐ۓ࢏҅
๐ۓ࢏੪Ꭳ᭲አߺӞSession̶
ᘒ୮౯ժֵአෛտᦾጱၨᥦ࢏ᦢᳯServlet7ጱ෸ײ҅ᧆෛၨᥦ࢏ଚဌํCookie҅๐ۓ࢏෫ဩᬙᦊֵአ
ߺӞӻSession҅ಅզ੪឴ݐӧک꧊
String value = (String) request.getSession().getAttribute("name");
printWriter.write(value);

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
8.ၨᥦ࢏ᐬአԧCookie҅SessionᬮᚆአހҘ
 
Ӥᶎ᧔ԧSessionฎׁᶌCookie๶ᦩڦአಁၨᥦ࢏ጱ̶ইຎ౯ጱአಁၨᥦ࢏ᐬአԧCookieԧޫҘᕷय़ग़
හጱಋ๢ၨᥦ࢏᮷ӧඪ೮Cookie҅ᮎ౯ጱSessionெԍېҘ

![三歪教你学Servlet 第116页插图](../assets/images/三歪教你学Servlet_p116_1_9fc53b19.png)

![三歪教你学Servlet 第116页插图](../assets/images/三歪教你学Servlet_p116_2_3c233a1a.jpeg)

![三歪教你学Servlet 第116页插图](../assets/images/三歪教你学Servlet_p116_3_3d16cd02.png)

---

অጱ҅౯ժ๶፡፡ఘ٭ฎெԍ໏ጱ̶አಁၨᥦ࢏ᦢᳯServlet4ጱ෸ײ҅๐ۓ࢏ݻአಁၨᥦ࢏ᶹݎԧӞӻ
Cookie
֕ฎޫ҅୮አಁၨᥦ࢏ᦢᳯServlet7ጱ෸ײ҅ኧԭ౯ժᐬአԧCookie҅ಅզአಁၨᥦ࢏ଚဌํ಩
Cookieଃᬦ݄ᕳ๐ۓ࢏̶
Ӟ፡҅Sessionঅ؟ӧᚆአԧ̶֕ฎJava Web൉׀ԧᥴ٬ොဩғURLࣈ࣎᯿ٟ
HttpServletResponseᔄ൉׀ԧӷӻURLࣈ࣎᯿ٟጱොဩғ
encodeURL(String url)
encodeRedirectURL(String url)
ᵱᥝ꧊஑ဳ఺ጱฎғᬯӷӻොဩտᛔۖڣෙᧆၨᥦ࢏ฎވඪ೮Cookie҅ইຎඪ೮Cookie҅᯿ٟݸጱURL
ࣈ࣎੪ӧտଃํjsessionidԧ̓୮ᆐԧ҅ܨֵၨᥦ࢏ඪ೮Cookie҅ᒫӞེᬌڊURLࣈ࣎ጱ෸ײᬮฎտڊ
ሿjsessionidҁࢩԅဌํձ֜Cookieݢଃ҂̈́
ӥᶎ౯ժ੪զӤᶎ“ᨻᇔ”ጱֺৼ๶؉ᦶḵމѺḒض౯ժ๶፡፡ᐬአധCookie੒ܻ๶ጱੜֺৼํՋԍ୽
ߥ̶
ᦢᳯServlet1҅ᵋ׎ᅩڋӞ๜ԡᔁᨻԣ

![三歪教你学Servlet 第117页插图](../assets/images/三歪教你学Servlet_p117_1_573ad7fe.png)

![三歪教你学Servlet 第117页插图](../assets/images/三歪教你学Servlet_p117_2_f063e6b3.png)

---

෫ᦞᅩڋग़੝ེ҅᮷տፗള൉ᐏ౯ժํԣᬦձ֜ࠟߝ
ܻࢩԞᶋଉᓌܔ҅ဌํCookieփ᭓ᕳ๐ۓ࢏҅๐ۓ࢏ྯེڠୌጱ෸ײ᮷ฎෛጱSession҅੕ᛘ๋ݸ឴ݐ
کጱListᵞݳӞਧฎᑮጱ̶
ӧݶServlet឴ݐکጱSessionጱidݩ᮷ฎӧݶጱ̶

![三歪教你学Servlet 第118页插图](../assets/images/三歪教你学Servlet_p118_1_e6527a34.png)

![三歪教你学Servlet 第118页插图](../assets/images/三歪教你学Servlet_p118_2_3d100b94.png)

---

ӥᶎ౯ժ੪੒URLᬰᤈ᯿ٟ҅፡፡ᚆӧᚆ௩॔ဌํᐬധCookieԏڹጱපຎ̶
ܻڞғ಩Sessionጱં௔ଃᬦ݄̓փ᭓ᕳ̈́ݚक़ӞӻServlet҅᮷ᥝURLࣈ࣎᯿ٟ
ࣁ᪡᫨کดᐏᨻԣᬦࠟߝጱServletጱ෸ײ҅URLࣈ࣎᯿̶ٟ
ེٚᦢᳯServlet1҅୮౯ᅩڋjavawebጱ෸ײ҅૪ᕪᚆड़౮ۑڊሿ౯ԣᬦጱࠟߝԧ̶ଚӬSessionጱid᭗
ᬦURLࣈ࣎᯿ֵٟ҅አጱฎݶӞӻSession
URLࣈ࣎᯿ٟጱܻቘғਖ਼Sessionጱidמ௳᯿ٟکURLࣈ࣎Ӿ̶๐ۓ࢏ᥴຉ᯿ٟݸURL҅឴ݐSessionጱ
id̶ᬯ໏Ӟ๶҅ܨֵၨᥦ࢏ᐬአധԧCookie҅֕Sessionጱid᭗ᬦ๐ۓ࢏ᒒփ᭓҅ᬮฎݢզֵአSession
๶ᦕ୯አಁጱᇫா̶
9.SessionᐬአCookie
 
Java Webᥢ᝜ඪ೮᭗ᬦᯈᗝᐬአCookie҅ᐬአᛔ૩ᶱፓጱCookie҅ࣁMETA-INF෈կ४ӥጱ
context.xml෈կӾץදҁဌํڞڠୌ҂
String url = "/ouzicheng/Servlet7";
response.sendRedirect(response.encodeURL(url));

![三歪教你学Servlet 第119页插图](../assets/images/三歪教你学Servlet_p119_1_3f6b3dd6.png)

![三歪教你学Servlet 第119页插图](../assets/images/三歪教你学Servlet_p119_2_21ea6745.png)

---

ᐬአق᮱webଫአጱCookie
ࣁconf/context.xmlӾץද
ဳ఺ғᧆᯈᗝݝฎᦏ๐ۓ࢏ӧᚆᛔۖᖌಷݷԅjsessionidጱCookie҅ଚӧᚆᴥྊCookieጱ᧛̶ٟ
    <?xml version='1.0' encoding='utf-8'?>
    
    <Context path="/ouzicheng" cookies="false">
    </Context>

![三歪教你学Servlet 第120页插图](../assets/images/三歪教你学Servlet_p120_1_8b402fbc.png)

![三歪教你学Servlet 第120页插图](../assets/images/三歪教你学Servlet_p120_2_1ad164ed.png)

![三歪教你学Servlet 第120页插图](../assets/images/三歪教你学Servlet_p120_3_5ea6f4c4.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
10.Sessionໜֺ
 
10.1ֵአSessionਠ౮አಁᓌܔጭᴭ
 
ضڠୌUserᔄ
ֵአᓌܔጱᵞݳཛྷ೙Ӟӻහഝପ
private String username = null;
private String password = null;
public User() {
}
public User(String username, String password) {
  this.username = username;
  this.password = password;
}
....ݱᐿset̵getොဩ
private static List<User> list = new ArrayList<>();
//ᤰ᫹Զහഝᬰහഝପ
static {
  list.add(new User("aaa","111"));
  list.add(new User("bbb","222"));
  list.add(new User("ccc","333"));
}
//᭗ᬦአಁݷ޾ੂᎱັತአಁ
public static User find(String username, String password) {
  for (User user : list) {
    if (user.getUsername().equals(username) && 
user.getPassword().equals(password)) {
      return user;
    }
  }
  return null;
}

---

ᤒܔ൉Իጱૡ֢౯੪ࣁjspٟԧ҅ইຎࣁServletٟॡἋᅸԧѺ
឴ݐکᤒܔ൉Իጱහഝ҅ັತහഝପฎވํፘ੒ଫጱአಁݷ޾ੂᎱ̶ইຎဌํ੪൉ᐏአಁݷ౲ੂᎱڊᲙ
ԧ҅ইຎํ੪᪡᫨کݚक़Ӟӻᶭᶎ
౯ժ๶ᦶᦶӥහഝପဌํጱአಁݷ޾ੂᎱ҅൉ᐏ౯ӧᚆጭᴭ̶
ᦶᦶහഝପਂࣁጱአಁݷ޾ੂᎱ
<form action="/ouzicheng/LoginServlet" method="post">
    አಁݷғ<input type="text" name="username"><br/>
    ੂᎱғ<input type="password" name="password"><br/>
    <input type="submit" value="൉Ի">
</form>
String username = request.getParameter("username");
String password = request.getParameter("password");
User user = UserDB.find(username, password);
//ইຎತӧک҅੪ฎአಁݷ౲ੂᎱڊᲙԧ̶
if (user == null) {
  response.getWriter().write("you can't login");
  return;
}
//ຽᦕ፳ᧆአಁ૪ᕪጭᴭԧѺ
HttpSession httpSession = request.getSession();
httpSession.setAttribute("user", user);
//᪡᫨کٌ՜ᶭᶎ҅ޞᦫአಁ౮ۑጭᴭԧ̶
response.sendRedirect(response.encodeURL("index.jsp"));

![三歪教你学Servlet 第122页插图](../assets/images/三歪教你学Servlet_p122_1_e2408727.png)

---

10.2ڥአSessionᴠྊᤒܔ᯿॔൉Ի
 
᯿॔൉Իጱܧਸ਼ғ
ࣁಭᐥጱᗑᶭӤӧ؊ࣈ൉Ի҅ਫሿԧڬᐥጱපຎ̶
ဳٙग़ӻአಁ҅ӧෙݎૼৼ҅ಟԤྋଉݎૼᑉଧ̶
Ḓض౯ժ๶፡Ӟӥଉᥠጱ᯿॔൉Ի̶
ࣁ॒ቘᤒܔጱServletӾڬෛ̶
ݸᭅٚ൉Ի
ᗑᕶ୊᬴҅ग़ེᅩڋ൉Իೲᰵ
ӥᶎጱgifฎݸᭅٚ൉Ի҅ࣁ॒ቘ൉Ի᧗࿢ጱServletӾڬෛ

![三歪教你学Servlet 第123页插图](../assets/images/三歪教你学Servlet_p123_1_087bea5b.png)

---

ӥᶎጱgifฎᗑᕶ୊᬴҅ग़ེᅩڋ൉Իೲᰵ
੒ԭᗑᕶ୊᬴᭜౮ጱग़ེ൉Իහഝᕳ๐ۓ࢏ٌ҅ਫฎਮಁᒒጱᳯ̶᷌ԭฎ҅౯ժݢզֵአjavaScript๶
ᴠྊᬯᐿఘ٭
ᥝ؉ጱԪఘԞᶋଉᓌܔғ୮አಁᒫӞེᅩڋ൉Իೲᰵ෸҅಩හഝ൉Իᕳ๐ۓ࢏̶୮አಁེٚᅩڋ൉Իೲ
ᰵ෸҅੪ӧ಩හഝ൉Իᕳ๐ۓ࢏ԧ̶
 
ፊލአಁ൉ԻԪկ̶ݝᚆᦏአಁ൉ԻӞེᤒܔѺ
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>ᤒܔ൉Ի</title>
    <script type="text/javascript">
        //ਧԎӞӻقੴຽᦩᰁғฎވ૪ᕪ൉Իᬦᤒܔහഝ
        var isCommitted = false;
        function doSubmit() {
            //falseᤒᐏጱฎဌํ൉Իᬦ҅ԭฎ੪ݢզᦏᤒܔ൉ԻᕳServlet
            if(isCommitted==false) {
                isCommitted = true;
                return true;
            }else {

![三歪教你学Servlet 第124页插图](../assets/images/三歪教你学Servlet_p124_1_0b04e0e4.png)

---

অጱ҅౯ժ๶ᦶӞӥฎӧฎ፥ጱݢզᥴ٬ᗑᕶ୊᬴ಅ᭜౮ጱग़ེ൉Իᤒܔහഝ҅ဳ఺Ἤຽ҅౯૪ᕪᅩڋ
ᬦஉग़ེጱԧѺ
ኧԭᗑᕶ୊᬴᭜౮ጱग़ེ൉Իහഝᕳ๐ۓ࢏҅౯ժᬮݢզֵአjavaScriptդᎱᬯ໏ᥴ٬ғ୮౯ᅩڋᬦӞ
ེ൉Իೲᰵ෸҅౯੪಩൉Իጱೲᰵᵌᡐ᩸๶̶ӧᚆᦏአಁᅩڋԧѺ
మᥝᦏೲᰵᵌᡐ᩸๶҅Ԟஉᓌܔ̶ݝᥝ឴ݐکೲᰵጱᜓᅩ҅੪ݢզഴګೲᰵጱᵌᡐ౲ดᐏԧѺ
౯ժٚ๶፡Ӟӥපຎ
ࣁ॒ቘᤒܔጱServletӾڬෛ޾ݸᭅٚ൉Իᬯӷᐿොୗӧᚆݝᶌਮಁᒒ๶ᴴګԧ̶Ԟ੪ฎ᧔javaScriptդ
Ꮁ෫ဩᴥྊᬯӷᐿఘ٭ጱݎኞ̶
ԭฎԒ҅౯ժ੪మ஑አٌ՜ېဩ๶ᴥྊᤒܔහഝ᯿॔൉Իԧ̶౯ժሿࣁ਍ԧSession҅Sessionݢզአ๶
ຽᦩӞӻአಁฎވጭᴭԧ̶SessionጱܻቘԞ᧔ԧғӧݶጱአಁၨᥦ࢏տ೜ํӧݶጱSession̶ᘒ
request޾ServletContextԅՋԍ੪ӧᤈޫҘrequestጱऒ੒᨝ݝᚆฎӞེhttp᧗࿢҅൉Իᤒܔහഝጱ෸
ײrequestऒ੒᨝ጱහഝݐӧڊ๶̶ServletContextդᤒෆӻwebଫአ҅ইຎํپӻአಁၨᥦ࢏ݶ෸ᦢ
ᳯ҅ServletContextऒ੒᨝ጱහഝտᤩग़ེᥟፍധ҅Ԟ੪ฎ᧔ऒ੒᨝ጱහഝ੪ྺ෫఺Ԏԧ̶
ݢᚆکᬯ᯾҅౯ժտమکғࣁ൉Իහഝጱ෸ײ҅ਂᬰSessionऒ੒᨝ጱහഝ҅ࣁ॒ቘ൉ԻහഝጱServlet
ӾڣෙSessionऒ੒᨝හഝ????̶ᑪᒌڣෙSessionՋԍҘڣෙSessionऒ੒᨝ጱහഝӧԅnullҘဌአޚ҅
෬ᆐ૪ᕪ൉Իᬦ๶ԧ҅ᮎᙗਧӧԅnull̶
                return false;
            }
        }
    </script>
</head>
<body>
<form action="/ouzicheng/Servlet7" onsubmit="return doSubmit()">
    አಁݷғ<input type="text" name="username">
    <input type="submit" value="൉Ի">
</form>
</body>
</html>
<script type="text/javascript">
  function doSubmit() {
  var button = document.getElementById("button");
  button.disabled = disabled;
  return true;
}
</script>

---

ྌ෸҅౯ժ੪మکԧ҅ࣁᤒܔӾᬮํӞӻᵌᡐऒ҅ݢզ᭗ᬦᵌᡐऒ಩හഝԻᕳ๐ۓ࢏̶
ڣෙSessionऒ੒᨝ጱහഝ޾jspᵌᡐऒ൉Իጱහഝฎވ੒ଫ̶
ڣෙᵌᡐऒጱහഝฎވԅᑮ̓ইຎԅᑮ҅੪ฎፗളᦢᳯᤒܔ॒ቘᶭᶎጱServleẗ́
ڣෙSessionጱහഝฎވԅᑮ̓servletڣෙਠฎވ᯿॔൉Ի๋҅অᚆᒈḘᑏᴻSessionጱහ
ഝ҅ӧᆐᬮဌํᑏᴻጱ෸ײ҅ਮಁᒒᮎᬟدጱ᧗࿢݈๶ԧ҅੪݈ᚆ܃ᯈԧ҅Ծኞԧ᯿॔൉
Ի̶ইຎSessionऒ੒᨝හഝԅᑮ҅ᦤก૪ᕪ൉ԻᬦහഝԧѺ̈́
౯ժݻSessionऒ੒᨝ጱਂفහഝᑪᒌฎՋԍޫҘᓌܔጱӞӻහਁҘঅ؟Ԟᤈ̶ࠡࢩԅݝᥝSessionऒ੒
᨝ጱහഝ޾jspᵌᡐऒଃᬦ݄ጱහഝ੒஑Ӥݩ੪ᤈԧޚ҅ݍྋࣁServletӤڣෙਠฎވ᯿॔൉Ի҅տᒈḘ
಩Sessionጱහഝᑏᴻധጱ̶ๅӫӱጱ؉ဩฎғݻSessionऒ੒᨝ਂفጱහഝฎӞӻᵋ๢හ̓Token--ե
ᇈ̶̈́
ኞ౮ӞӻᇿӞ෫ԫጱᵋ๢හ
/*
* Ծኞᵋ๢හ੪ଫᧆአӞӻ੒᨝๶ኞ౮҅ᬯ໏ݢզ᭿عᵋ๢හጱ᯿̶॔
* ಅզᦡᦇ౮ܔֺ
* */
public class TokenProcessor {
    private TokenProcessor() {
    }
    private final static TokenProcessor TOKEN_PROCESSOR = new 
TokenProcessor();
    public static TokenProcessor getInstance() {
        return TOKEN_PROCESSOR;
    }
    public static String makeToken() {
        //ᬯӻᵋ๢ኞ౮ڊ๶ጱTokenጱᳩଶฎӧᏟਧጱ
        String token = String.valueOf(System.currentTimeMillis() + new 
Random().nextInt(99999999));
        try {
            //౯ժమᥝᵋ๢හጱᳩଶӞᛘ҅੪ᥝ឴ݐکහഝ೰ᕖ
            MessageDigest messageDigest = MessageDigest.getInstance("md5");
            byte[] md5 = messageDigest.digest(token.getBytes());
            //ইຎ౯ժፗള return  new String(md5)ڊ݄҅஑کጱᵋ๢හտԤᎱ̶
            //ࢩԅᵋ๢හฎձ఺ጱ01010101010҅ࣁ᫨ഘ౮ਁᒧԀጱ෸ײ҅տັgb2312ጱᎱᤒ҅
gb2312ᎱᤒӧӞਧඪ೮ᧆԫᬰګහഝ҅஑کጱ੪ฎԤᎱ
            
            //ԭฎԒᕪᬦbase64ᖫᎱ౮ԧก෈ጱහഝ

---

ڠୌTokenᵋ๢හ҅ଚ᪡᫨کjspᶭᶎ
jspᵌᡐऒ឴ݐکSessionጱ꧊
ࣁ॒ቘᤒܔ൉ԻᶭᶎӾڣෙғjspᵌᡐऒฎވํ꧊ଃᬦ๶҅SessionӾጱ꧊ฎވԅᑮ҅SessionӾጱ꧊޾
jspᵌᡐऒଃᬦ๶ጱ꧊ฎވፘᒵ
            BASE64Encoder base64Encoder = new BASE64Encoder();
            return base64Encoder.encode(md5);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return null;
    }
}
        //ኞڊᵋ๢හ
        TokenProcessor tokenProcessor = TokenProcessor.getInstance();
        String token = tokenProcessor.makeToken();
        //ਖ਼ᵋ๢හਂᬰSessionӾ
        request.getSession().setAttribute("token", token);
        //᪡᫨کดᐏᶭᶎ
        request.getRequestDispatcher("/login.jsp").forward(request, response);
<form action="/ouzicheng/Servlet7" >
    አಁݷғ<input type="text" name="username">
    <input type="submit" value="൉Ի" id="button">
    <%--ֵአELᤒᬡୗݐڊsessionӾጱToken--%>
    <input type="hidden" name="token" value="${token}" >
</form>
String serverValue = (String) request.getSession().getAttribute("token");

---

ӥᶎ౯ժٚ๶፡Ӟӥ,૪ᕪݢզᥴ٬ᤒܔ᯿॔൉Իጱᳯ᷌ԧѺ
ਫሿܻቘฎᶋଉᓌܔጱғ
ࣁsessionऒӾਂؙӞӻtoken
ᆐݸڹݣᶭᶎጱᵌᡐऒ឴ݐ஑کᬯӻtoken
ࣁᒫӞེᦢᳯጱ෸ײ҅౯ժ੪ڣෙseesionํဌํ꧊҅ইຎํ੪ྲ੒̶੒ྲྋᏟݸ౯ժ੪॒ቘ᧗
࿢҅ള፳੪಩sessionਂؙጱහഝᕳڢᴻԧ
ᒵکེٚᦢᳯጱ෸ײ҅౯ժsession੪ဌํ꧊ԧ҅੪ӧݑቘڹݣጱ᧗࿢ԧѺ
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
String clientValue = request.getParameter("token");
if (serverValue != null && clientValue != null && 
serverValue.equals(clientValue)) {
  System.out.println("॒ቘ᧗࿢");
  //ႴᴻSessionऒ੒᨝හഝ
  request.getSession().removeAttribute("token");
}else {
  System.out.println("᧗ӧᥝ᯿॔൉ԻහഝѺ");
}

![三歪教你学Servlet 第128页插图](../assets/images/三歪教你学Servlet_p128_1_ab8a3c52.jpeg)

---

10.3Ӟེ௔໊ḵᎱ
 
Ӟེ௔໊ḵᎱٌਫ੪ฎԅԧᴠྊูێሖၥੂᎱ҅ࣁᦖresponse੒᨝ጱ෸ײ҅౯ժֵአresponse੒᨝ᬌ
ڊᬦḵᦤᎱ҅֕ฎဌํ݄ḵᦤѺ
 
ḵᦤጱܻቘԞᶋଉᓌܔғኞ౮ḵᦤᎱݸ҅಩ḵᦤᎱጱහഝਂᬰSessionऒ੒᨝Ӿ҅ڣෙአಁᬌفḵᦤᎱ
ฎވ޾Sessionऒ੒᨝ጱහഝӞᛘ̶
 
ኞ౮ḵᦤᎱࢶᇆ҅ଚਖ਼ḵᦤᎱਂᬰSessionऒӾ
//ࣁٖਂӾኞ౮ࢶᇆ
BufferedImage bufferedImage = new BufferedImage(80, 20, 
BufferedImage.TYPE_INT_RGB);
//឴ݐکᬯୟࢶᇆ
Graphics2D graphics2D = (Graphics2D) bufferedImage.getGraphics();
//ᦡᗝᙧวᜋԅጮᜋ
graphics2D.setColor(Color.white);
graphics2D.fillRect(0, 0, 80, 20);
//ᦡᗝࢶᇆጱਁ֛޾᷏ᜋ
graphics2D.setFont(new Font(null, Font.BOLD, 20));
graphics2D.setColor(Color.BLUE);
//ኞ౮ᵋ๢හ
String randomNum = makeNum();
//ஃᬯୟࢶᇆӤٟහഝ,ཞࣖຽฎ0҅ᕒࣖຽฎ20
graphics2D.drawString(randomNum, 0, 20);
//ਖ਼ᵋ๢හਂᬰSessionऒӾ

![三歪教你学Servlet 第129页插图](../assets/images/三歪教你学Servlet_p129_1_3c233a1a.jpeg)

---

ኞ౮ᵋ๢හጱොဩғ
jspดᐏᶭᶎ
request.getSession().setAttribute("randomNum", randomNum);
//ഴګၨᥦ࢏ӧᖨਂᧆࢶᇆ
response.setHeader("Expires", "-1");
response.setHeader("Cache-Control", "no-cache");
response.setHeader("Pragma", "no-cache");
//᭗Ꭳၨᥦ࢏զࢶᇆጱොୗ಑୏
response.setHeader("Content-type", "image/jpeg");
//಩ࢶᇆٟᕳၨᥦ࢏
ImageIO.write(bufferedImage, "jpg", response.getOutputStream());
private String makeNum() {
  Random random = new Random();
  //ኞ౮0-6֖ጱᵋ๢හ
  int num = random.nextInt(999999);
  //ḵᦤᎱጱහ֖ق᮷ᥝ6֖හ҅ԭฎਖ਼ᧆᵋ๢හ᫨ഘ౮ਁᒧԀ҅ӧड़֖හ੪Ⴒے
  String randomNum = String.valueOf(num);
  //ֵአStringBuffer๶೪ٻਁᒧԀ
  StringBuffer stringBuffer = new StringBuffer();
  for (int i = 0; i < 6 - randomNum.length(); i++) {
    stringBuffer.append("0");
  }
  return stringBuffer.append(randomNum).toString();
}

---

॒ቘ൉ԻᤒܔහഝጱServlet҅ڣෙአಁଃᬦ๶ḵᦤᎱጱහഝฎވ޾Sessionጱහഝፘݶ̶
 
ดᐏᶭᶎฎᬯ໏ৼጱ
౯ժ๶፡ӞӥපຎѺ
੒ԭ໊ḵᎱਫሿ௏᪠ฎᬯ໏ৼጱғ
ֵአawt᧍ဩ๶ൈٟӞୟḵᦤᎱ҅ኞ౮ᵋ๢හכਂࣁseesionऒӾ҅౯ժᦏḵᦤᎱӧᚆᖨਂ᩸๶
̓؉کḵᦤᎱ᮷ӧӞ໏̈́
ᶭᶎፗളᦢᳯServlet๶឴ݐ౯ժጱḵᦤᎱ҅ԭฎ౯ժḵᦤᎱጱ꧊੪տදݒ̓ݶ෸sessionጱ꧊Ԟտ
ᤩදݒ̈́
୮አಁḵᦤጱ෸ײ҅੪ฎsessionٖጱ꧊ጱḵᦤԧ̶
<form action="/ouzicheng/Login2Servlet">
    አಁݷғ<input type="text" name="username"><br>
    ੂᎱғ<input type="password" name="password"><br>
    ḵᦤᎱғ<input type="text" name="randomNum">
    <img src="/ouzicheng/ImageServlet" ><br><br>
    <input type="submit" value="൉Ի">
</form>
//឴ݐአಁᬌفḵᦤᎱጱහഝ
String client_randomNum = request.getParameter("randomNum");
//឴ݐSessionӾጱහഝ
String session_randomNum = (String) 
request.getSession().getAttribute("randomNum");
//ڣෙ՜עහഝฎވፘᒵ҅አಁฎވํᬌفḵᦤᎱ҅SessionӾฎވԅᑮ
if (client_randomNum == null || session_randomNum == null || 
!client_randomNum.equals(session_randomNum)) {
  System.out.println("ḵᦤᎱᲙ᧏ԧѺѺѺ");
  return ;
}
//ӥᶎ੪ฎḵᦤአಁݷ޾ੂᎱ...................

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
11. Session޾Cookieጱ܄ڦ
 
՗ਂؙොୗӤྲ᫾
CookieݝᚆਂؙਁᒧԀ҅ইຎᥝਂؙᶋASCIIਁᒧԀᬮᥝ੒ٌᖫᎱ̶
Sessionݢզਂؙձ֜ᔄࣳጱහഝ҅ݢզ಩Session፡౮ฎӞӻ਻࢏
՗ᵌᐺਞقӤྲ᫾
Cookieਂؙࣁၨᥦ࢏Ӿ҅੒ਮಁᒒฎݢᥠጱ̶מ௳਻ฃအᶂڊ̶݄ইຎֵአCookie๋҅অਖ਼
Cookieےੂ
Sessionਂؙࣁ๐ۓ࢏Ӥ҅੒ਮಁᒒฎ᭐กጱ̶ӧਂࣁභఽמ௳အᶂᳯ̶᷌
՗ํප๗Ӥྲ᫾
CookieכਂࣁᏝፏӾ҅ݝᵱᥝᦡᗝmaxAgeં௔ԅྲ᫾य़ጱྋෆහ҅ܨֵىᳮၨᥦ࢏҅
Cookieᬮฎਂࣁጱ
Sessionጱכਂࣁ๐ۓ࢏Ӿ҅ᦡᗝmaxInactiveIntervalં௔꧊๶ᏟਧSessionጱํප๗̶ଚ
ӬSessionׁᩢԭݷԅJSESSIONIDጱCookie҅ᧆCookieἕᦊጱmaxAgeં௔ԅ-1̶ইຎى
ᳮԧၨᥦ࢏҅ᧆSessionᡱᆐဌํ՗๐ۓ࢏ӾၾԹ҅֕Ԟ੪०පԧ̶
՗੒๐ۓ࢏ጱᨮ೅ྲ᫾
Sessionฎכਂࣁ๐ۓ࢏ጱ҅ྯӻአಁ᮷տԾኞӞӻSession҅ইຎฎଚݎᦢᳯጱአಁᶋଉ
ग़҅ฎӧᚆֵአSessionጱ҅Sessionտၾᘙय़ᰁጱٖਂ̶
Cookieฎכਂࣁਮಁᒒጱ̶ӧܛአ๐ۓ࢏ጱᩒრ̶؟baidu̵Sinaᬯ໏ጱय़ࣳᗑᒊ҅Ӟᛱ᮷
ฎֵአCookie๶ᬰᤈտᦾ᪙̶᪵
՗ၨᥦ࢏ጱඪ೮Ӥྲ᫾
ইຎၨᥦ࢏ᐬአԧCookie҅ᮎԍCookieฎ෫አጱԧѺ

![三歪教你学Servlet 第132页插图](../assets/images/三歪教你学Servlet_p132_1_3c233a1a.jpeg)

![三歪教你学Servlet 第132页插图](../assets/images/三歪教你学Servlet_p132_2_fb2bae66.png)

---

ইຎၨᥦ࢏ᐬአԧCookie҅Sessionݢզ᭗ᬦURLࣈ࣎᯿ٟ๶ᬰᤈտᦾ᪙̶᪵
՗᪜ऒݷӤྲ᫾
Cookieݢզᦡᗝdomainં௔๶ਫሿ᪜ऒݷ
Sessionݝࣁ୮ڹጱऒݷٖํප҅ӧݢ३ऒݷ
12. Cookie޾Sessionوݶֵአ
 
ইຎՐՐֵአCookie౲ՐՐֵአSessionݢᚆᬡӧکቘమጱපຎ̶ᬯ෸ଫᧆ੤ᦶӞӥݶ෸ֵአSession
޾Cookie̶ᮎԍ҅Ջԍ෸ײ಍ᵱᥝݶ෸ֵአCookie޾SessionޫҘ
 
ࣁӤӞᓤܗਮӾ҅౯ժֵአԧSession๶ᬰᤈᓌܔጱᨻᇔ҅ۑᚆԞጱᏟਫሿԧ̶ሿࣁํӞӻᳯ᷌ғ౯ࣁ
ᨻᇔጱ᭔Ӿ҅ӧੜஞىᳮԧၨᥦ࢏̶୮౯ٚᬬࢧᬰ݄ၨᥦ࢏ጱ෸ײ҅ݎሿ౯ᨻԣᬦጱࠟߝᦕ୯᮷ဌ
ԧѺѺԅՋԍտဌԧޫҘܻࢩԞᶋଉᓌܔғ๐ۓ࢏ԅSessionᛔۖᖌಷጱCookieጱmaxAgeં௔ἕᦊ
ฎ-1ጱ҅୮ၨᥦ࢏ىᳮധԧ҅ᧆCookie੪ᛔۖၾԹԧ̶୮አಁེٚᦢᳯጱ෸ײ҅૪ᕪӧฎܻ๶ጱ
Cookieԧ̶
 
౯ժሿࣁమጱฎғܨֵ౯ӧੜஞىᳮԧၨᥦ࢏ԧ҅౯᯿ෛᬰ݄ᗑᒊ҅౯ᬮᚆತک౯ጱᨻԣᦕ୯̶
ᥝਫሿᧆۑᚆԞ܈ړᓌܔ҅ᳯٌ᷌ਫ੪ࣁғ๐ۓ࢏ԅSessionᛔۖᖌಷጱCookieጱmaxAgeં௔ฎ-1҅
CookieဌํכਂࣁᏝፏӾ̶౯ሿࣁᥝ؉ጱ੪ฎғ಩CookieכਂࣁᏝፏӾ҅ܨֵ౯ىᳮԧၨᥦ࢏҅ၨᥦ
࢏ེٚᦢᳯᶭᶎጱ෸ײ҅ݢզଃӤCookie҅՗ᘒ๐ۓ࢏ᦩڦڊSession̶
 
ᒫӞᐿොୗғݝᵱᥝࣁ॒ቘᨻԣᶭᶎӤڠୌCookie҅Cookieጱ꧊ฎSessionጱidᬬࢧᕳၨᥦ࢏ܨݢ
ᒫԫᐿොୗғ ࣁserver.xml෈կӾᯈᗝ҅ਖ਼ྯӻአಁጱSessionࣁ๐ۓ࢏ىᳮጱ෸ײଧڜ۸کᏝፏ౲හ
ഝପӤכਂ̶֕ྌොဩӧଉአ҅Ꭳ᭲ܨݢѺ
 
ӥᶎ፡Ӟӥපຎ
 
    Cookie cookie = new Cookie("JSESSIONID",session.getId());
    cookie.setMaxAge(30*60);
    cookie.setPath("/ouzicheng/");
    response.addCookie(cookie);

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
Servletᶎᦶ᷌
 
 
ӥᶎฎ౯ෆቘӥ๶ጱServletᎣᦩᅩ:
 
ࢶӤጱᎣᦩᅩ᮷ݢզࣁ౯ٌ՜ጱ෈ᒍٖತکፘଫٖ਻̶
1. Tomcatଉᥠᶎᦶ᷌
 
1.1Tomcatጱᗌ፜ᒒݗฎग़੝҅ெԍץද
 
Tomcatጱᗌ፜ᒒݗฎग़੝҅ெԍץද
1. ತکTomcatፓ୯ӥጱconf෈կ४
2. ᬰفconf෈կ४᯾ᶎತکserver.xml෈կ
3. ಑୏server.xml෈կ
4. ࣁserver.xml෈կ᯾ᶎತکӥڜמ௳
5. ಩port=”8080″ද౮port=”8888″҅ଚӬכਂ
6. ސۖTomcat҅ଚӬࣁIEၨᥦ࢏᯾ᶎጱࣈ࣎ໄᬌفhttp://127.0.0.1:8888/
کtomcatԆፓ୯ӥጱconf/server.xml෈կӾץද,಩8080ᒒݗද౮ฎ8088౲ᘏฎٌ՜ጱ
<Service name="Catalina">
<Connector port="8080" protocol="HTTP/1.1" 
             connectionTimeout="20000" 
             redirectPort="8443" />

![三歪教你学Servlet 第134页插图](../assets/images/三歪教你学Servlet_p134_1_1125705a.png)

---

1.2Tomcat ํߺپᐿConnector ᬩᤈཛྷୗ(ս۸)Ҙ
 
tomcat ํߺپᐿConnector ᬩᤈཛྷୗ(ս۸)Ҙ
1. bio(blocking I/O)
2. nio(non-blocking I/O)
3. apr(Apache Portable Runtime/Apacheݢᑏ༙ᬩᤈପ)
ፘىᥴ᯽:
bio: փᕹጱJava I/O඙֢҅ݶྍӬᴥलIO̶
nio: JDK1.4୏তඪ೮҅ݶྍᴥल౲ݶྍᶋᴥलIO
aio(nio.2): JDK7୏তඪ೮҅୑ྍᶋᴥलIO
apr: Tomcatਖ਼զJNIጱ୵ୗ᧣አApache HTTP๐ۓ࢏ጱ໐ஞۖா᱾ളପ๶॒ቘ෈կ᧛ݐ౲ᗑᕶփᬌ
඙֢҅՗ᘒय़य़ࣈ ൉ṛTomcat੒ᶉா෈կጱ॒ቘ௔ᚆ
ӥᶎฎᯈᗝTomcatᬩᤈཛྷୗද౮ฎNIOཛྷୗ҅ଚᯈᗝᬳള࿰ፘى݇හ๶ᬰᤈս۸:
aprཛྷୗސۖ᩸๶ฎྲ᫾॔๥ጱ҅ᧇఘݢ݇
ᘍ:http://blog.csdn.net/wanglei_storage/article/details/50225779
੒ԭbio,nio,nio.2ጱቘᥴݢ݇ᘍ:http://blog.csdn.net/itismelzp/article/details/50886009
2.Servletᶎᦶ᷌
 
    <!--
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
    -->
    <!-- protocol ސአ nioཛྷୗ҅(tomcat8ἕᦊֵአጱฎnio)(aprཛྷୗڥአᔮᕹᕆ୑ྍio) -->
    <!-- minProcessors๋ੜᑮᳳᬳളᕚᑕහ-->
    <!-- maxProcessors๋य़ᬳളᕚᑕහ-->
    <!-- acceptCount꧋ᦜጱ๋य़ᬳളහ҅ଫय़ԭᒵԭmaxProcessors-->
    <!-- enableLookups ইຎԅtrue,requst.getRemoteHostտಗᤈDNSັತ҅ݍݻᥴຉip੒ଫ
ऒݷ౲Ԇ๢ݷ-->
    <Connector port="8080" 
protocol="org.apache.coyote.http11.Http11NioProtocol" 
        connectionTimeout="20000"
        redirectPort="8443
        maxThreads=“500” 
        minSpareThreads=“100” 
        maxSpareThreads=“200”
        acceptCount="200"
        enableLookups="false"       
    />

---

2.1Servletኞ޸ޮ๗
 
Servletኞ޸ޮ๗?
ᒫӞེᦢᳯServlet҅౯ժݎሿinit()޾service()᮷ᤩ᧣አԧ
ᒫԫེᦢᳯServlet҅service()ᤩ᧣አԧ
ᒫӣེᦢᳯServlet҅ᬮฎservice()ᤩ᧣አԧ
୮౯ժىᳮTomcat๐ۓ࢏ጱ෸ײ҅destroy()ᤩ᧣አԧѺ

![三歪教你学Servlet 第136页插图](../assets/images/三歪教你学Servlet_p136_1_a5aa317c.png)

---

Servletኞ޸ޮ๗ݢړԅ5ӻྍṈ
1. ے᫹Servlet̶୮TomcatᒫӞེᦢᳯServletጱ෸ײ҅TomcatտᨮᨱڠୌServletጱਫֺ
2. ڡত۸̶୮Servletᤩਫֺ۸ݸ҅Tomcatտ᧣አinit()ොဩڡত۸ᬯӻ੒᨝
3. ॒ቘ๐ۓ̶୮ၨᥦ࢏ᦢᳯServletጱ෸ײ҅Servlet տ᧣አservice()ොဩ॒ቘ᧗࿢
4. ᲀྪ̶୮Tomcatىᳮ෸౲ᘏ༄ၥکServletᥝ՗Tomcatڢᴻጱ෸ײտᛔۖ᧣አdestroy()ොဩ҅ᦏᧆ
ਫֺ᯽නധಅܛጱᩒრ̶ӞӻServletইຎᳩ෸ᳵӧᤩֵአጱᦾ҅ԞտᤩTomcatᛔۖᲀྪ
5. ܬ᫹̶୮Servlet᧣አਠdestroy()ොဩݸ҅ᒵஇ࣯࣍ࢧත̶ইຎํᵱᥝֵེٚአᬯӻServlet҅տ᯿
ෛ᧣አinit()ොဩᬰᤈڡত۸඙̶֢
 
ᓌܔ௛ᕮғݝᥝᦢᳯServlet҅service()੪տᤩ᧣አ̶init()ݝํᒫӞེᦢᳯServletጱ෸ײ಍տᤩ᧣
አ̶destroy()ݝํࣁTomcatىᳮጱ෸ײ಍տᤩ᧣አ̶
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y̶ๅग़
ܻڠದ๞෈ᒍݢىဳ౯ጱGitHub

![三歪教你学Servlet 第137页插图](../assets/images/三歪教你学Servlet_p137_1_aac51d72.png)

![三歪教你学Servlet 第137页插图](../assets/images/三歪教你学Servlet_p137_2_54b944c6.png)

---

2.2getොୗ޾postොୗํ֜܄ڦ
 
getොୗ޾postොୗํ֜܄ڦ
හഝ൭ଃӤ:
GETොୗғࣁURLࣈ࣎ݸᴫଃጱ݇හฎํᴴګጱٌ҅හഝ਻ᰁ᭗ଉӧᚆ᩻ᬦ1K̶
POSTොୗғݢզࣁ᧗࿢ጱਫ֛ٖ਻Ӿݻ๐ۓ࢏ݎᭆහഝ҅փᭆጱහഝᰁ෫ᴴګ̶
᧗࿢݇හጱ֖ᗝӤ:
GETොୗғ᧗࿢݇හනࣁURLࣈ࣎ݸᶎ҅զ?ጱොୗ๶ᬰᤈ೪ള
POSTොୗ:᧗࿢݇හනࣁHTTP᧗࿢۱Ӿ
አ᭔Ӥ:
GETොୗӞᛱአ๶឴ݐහഝ
POSTොୗӞᛱአ๶൉Իහഝ
ܻࢩ:
ḒضฎࢩԅGETොୗ൭ଃጱහഝᰁྲ᫾ੜ҅෫ဩଃᬦ݄உय़ጱහᰁ
POSTොୗ൉Իጱ݇හݸݣๅے਻ฃᥴຉ(ֵአPOSTොୗ൉ԻጱӾ෈හഝ҅ݸݣԞๅے਻
ฃᥴ٬)
GETොୗྲPOSTොୗᥝள
GETොୗྲPOSTොୗᥝள҅ᧇఘݢ
፡:https://www.cnblogs.com/strayling/p/3580048.html
2.3forward޾redirectጱ܄ڦ
 
forward޾redirectጱ܄ڦ
ਫᴬݎኞ֖ᗝӧݶ҅ࣈ࣎ໄӧݶ
᫨ݎฎݎኞࣁ๐ۓ࢏ጱ
᫨ݎฎኧ๐ۓ࢏ᬰᤈ᪡᫨ጱ҅ᕡஞጱ๏݋տݎሿ҅ࣁ᫨ݎጱ෸ײ҅ၨᥦ࢏ጱࣈ࣎ໄฎဌ
ํݎኞݒ۸ጱ҅ࣁ౯ᦢᳯServlet111ጱ෸ײ҅ܨֵ᪡᫨کԧServlet222ጱᶭᶎ҅ၨᥦ࢏
ጱࣈ࣎ᬮฎServlet111ጱ̶Ԟ੪ฎ᧔ၨᥦ࢏ฎӧᎣ᭲ᧆ᪡᫨ጱ֢ۖ҅᫨ݎฎ੒ၨᥦ࢏᭐

![三歪教你学Servlet 第138页插图](../assets/images/三歪教你学Servlet_p138_1_3c233a1a.jpeg)

---

กጱ̶᭗ᬦӤᶎጱ᫨ݎ෸ଧࢶ౯ժԞݢզݎሿ҅ਫሿ᫨ݎݝฎӞེጱhttp᧗࿢҅Ӟེ᫨
ݎӾrequest޾response੒᨝᮷ฎݶӞӻ̶ᬯԞᥴ᯽ԧ҅ԅՋԍݢզֵአrequest֢ԅ
ऒ੒᨝ᬰᤈServletԏᳵጱ᭗ᦔ̶
᯿ਧݻฎݎኞࣁၨᥦ࢏ጱ
᯿ਧݻฎኧၨᥦ࢏ᬰᤈ᪡᫨ጱ҅ᬰᤈ᯿ਧݻ᪡᫨ጱ෸ײ҅ၨᥦ࢏ጱࣈ࣎տݎኞݒ۸ጱ̶
้ᕪՕᕨᬦғਫሿ᯿ਧݻጱܻቘฎኧresponseጱᇫாᎱ޾Location१ᕟݳᘒਫሿጱ̶ᬯ
ฎኧၨᥦ࢏ᬰᤈጱᶭᶎ᪡᫨ਫሿ᯿ਧݻտݎڊӷӻhttp᧗࿢҅requestऒ੒᨝ฎ෫ප
ጱ҅ࢩԅਙӧฎݶӞӻrequest੒᨝
አဩӧݶ:
உग़Ո᮷൥ӧႴ༩᫨ݎ޾᯿ਧݻጱ෸ײ҅ᩒრࣈ࣎ᑪᒌெԍ̶ٟํጱ෸ײᥝ಩ଫአݷٟӤ҅
ํጱ෸ײӧአ಩ଫአݷٟӤ̶உ਻ฃ಩Ո൥ฝ̶ᦕ֘Ӟӻܻڞғ ᕳ๐ۓ࢏አጱፗള՗ᩒრݷ
୏তٟ҅ᕳၨᥦ࢏አጱᥝ಩ଫአݷٟӤ
request.getRequestDispatcher("/ᩒრݷ URI").forward(request,response)
᫨ݎ෸"/"դᤒጱฎ๜ଫአᑕଧጱ໑ፓ୯̓zhongfucheng̈́
response.send("/webଫአ/ᩒრݷ URI");
᯿ਧݻ෸"/"դᤒጱฎwebappsፓ୯
ᚆड़݄ஃጱURLጱ᝜ࢱӧӞ໏:
᫨ݎฎ๐ۓ࢏᪡᫨ݝᚆ݄ஃ୮ڹwebଫአጱᩒრ
᯿ਧݻฎ๐ۓ࢏᪡᫨҅ݢզ݄ஃձ֜ጱᩒრ
փ᭓හഝጱᔄࣳӧݶ
᫨ݎጱrequest੒᨝ݢզփ᭓ݱᐿᔄࣳጱහഝ҅۱ೡ੒᨝
᯿ਧݻݝᚆփ᭓ਁᒧԀ
᪡᫨ጱ෸ᳵӧݶ
᫨ݎ෸ғಗᤈک᪡᫨᧍ݙ෸੪տᒈڰ᪡᫨
᯿ਧݻғෆӻᶭᶎಗᤈਠԏݸ಍ಗᤈ᪡᫨
ᮎԍ᫨ݎ(forward)޾᯿ਧݻ(redirect)ֵአߺӞӻҘ
໑ഝӤᶎ᧔กԧ᫨ݎ޾᯿ਧݻጱ܄ڦԞݢզஉ਻ฃ༷ೡڊ๶̶᫨ݎฎଃ፳᫨ݎڹጱ᧗࿢ጱ݇හጱ̶
᯿ਧݻฎෛጱ᧗࿢̶
َࣳጱଫአ࣋วғ
1. ᫨ݎ: ᦢᳯ Servlet ॒ቘӱۓ᭦ᬋ҅ᆐݸ forward ک jsp ดᐏ॒ቘᕮຎ҅ၨᥦ࢏᯾ URL ӧݒ
2. ᯿ਧݻ: ൉Իᤒܔ॒҅ቘ౮ۑݸ redirect کݚӞӻ jsp҅ᴠྊᤒܔ᯿॔൉Ի҅ၨᥦ࢏᯾ URL ݒԧ
2.4 tomcat਻࢏ฎই֜ڠୌservletᔄਫֺҘአکԧՋԍܻቘҘ
 
tomcat਻࢏ฎই֜ڠୌservletᔄਫֺҘአکԧՋԍܻቘ
1. ୮਻࢏ސۖ෸҅տ᧛ݐࣁwebappsፓ୯ӥಅํጱwebଫአӾጱweb.xml෈կ҅ᆐݸ੒ xml෈կᬰ
ᤈᥴຉ҅ଚ᧛ݐservletဳٙמ௳̶ᆐݸ҅ਖ਼ྯӻଫአӾဳٙጱservletᔄ᮷ᬰᤈے᫹҅ଚ᭗ᬦ ݍ੘
ጱොୗਫֺ۸̶ҁํ෸ײԞฎࣁᒫӞེ᧗࿢෸ਫֺ۸҂
2. ࣁservletဳٙ෸ےӤ <load-on-startup> 1 </load-on-startup> ইຎԅྋහ҅ڞࣁӞ୏ত੪ਫ
ֺ۸҅ইຎӧٟ౲ԅᨮහ҅ڞᒫӞེ᧗࿢ਫֺ۸̶
2.5ՋԍฎcookieҘSession޾cookieํՋԍ܄ڦ Ҙ

---

ՋԍฎcookieҘ
 CookieฎኧW3Cᕟᕢ൉ڊ๋҅෱ኧnetscapeᐒ܄ݎ઀ጱӞᐿ๢ګ
ᗑᶭԏᳵጱԻ԰ฎ᭗ᬦHTTPܐᦓփᬌහഝጱ҅ᘒHttpܐᦓฎ෫ᇫாጱܐᦓ̶෫ᇫாጱܐᦓฎՋԍ఺௏
ޫҘӞ෮හഝ൉Իਠݸ҅ၨᥦ࢏޾๐ۓ࢏ጱᬳള੪տىᳮེ҅ٚԻ԰ጱ෸ײᵱᥝ᯿ෛୌᒈෛጱᬳള̶
๐ۓ࢏෫ဩᏟᦊአಁጱמ௳҅ԭฎԒ҅W3C੪൉ڊԧғᕳྯӞӻአಁ᮷ݎӞӻ᭗ᤈᦤ҅෫ᦞ᧡ᦢᳯጱ෸
ײ᮷ᵱᥝ൭ଃ᭗ᤈᦤ҅ᬯ໏๐ۓ࢏੪ݢզ՗᭗ᤈᦤӤᏟᦊአಁጱמ௳̶᭗ᤈᦤ੪ฎCookie
Session޾cookieํՋԍ܄ڦҘ
՗ਂؙොୗӤྲ᫾
CookieݝᚆਂؙਁᒧԀ҅ইຎᥝਂؙᶋASCIIਁᒧԀᬮᥝ੒ٌᖫᎱ̶
Sessionݢզਂؙձ֜ᔄࣳጱහഝ҅ݢզ಩Session፡౮ฎӞӻ਻࢏
՗ᵌᐺਞقӤྲ᫾
Cookieਂؙࣁၨᥦ࢏Ӿ҅੒ਮಁᒒฎݢᥠጱ̶מ௳਻ฃအᶂڊ̶݄ইຎֵአCookie๋҅অਖ਼
Cookieےੂ
Sessionਂؙࣁ๐ۓ࢏Ӥ҅੒ਮಁᒒฎ᭐กጱ̶ӧਂࣁභఽמ௳အᶂᳯ̶᷌
՗ํප๗Ӥྲ᫾
CookieכਂࣁᏝፏӾ҅ݝᵱᥝᦡᗝmaxAgeં௔ԅྲ᫾य़ጱྋෆහ҅ܨֵىᳮၨᥦ࢏҅
Cookieᬮฎਂࣁጱ
Sessionጱכਂࣁ๐ۓ࢏Ӿ҅ᦡᗝmaxInactiveIntervalં௔꧊๶ᏟਧSessionጱํප๗̶ଚ
ӬSessionׁᩢԭݷԅJSESSIONIDጱCookie҅ᧆCookieἕᦊጱmaxAgeં௔ԅ-1̶ইຎى
ᳮԧၨᥦ࢏҅ᧆSessionᡱᆐဌํ՗๐ۓ࢏ӾၾԹ҅֕Ԟ੪०පԧ̶
՗੒๐ۓ࢏ጱᨮ೅ྲ᫾
Sessionฎכਂࣁ๐ۓ࢏ጱ҅ྯӻአಁ᮷տԾኞӞӻSession҅ইຎฎଚݎᦢᳯጱአಁᶋଉ
ग़҅ฎӧᚆֵአSessionጱ҅Sessionտၾᘙय़ᰁጱٖਂ̶
Cookieฎכਂࣁਮಁᒒጱ̶ӧܛአ๐ۓ࢏ጱᩒრ̶؟baidu̵Sinaᬯ໏ጱय़ࣳᗑᒊ҅Ӟᛱ᮷
ฎֵአCookie๶ᬰᤈտᦾ᪙̶᪵
՗ၨᥦ࢏ጱඪ೮Ӥྲ᫾
ইຎၨᥦ࢏ᐬአԧCookie҅ᮎԍCookieฎ෫አጱԧѺ
ইຎၨᥦ࢏ᐬአԧCookie҅Sessionݢզ᭗ᬦURLࣈ࣎᯿ٟ๶ᬰᤈտᦾ᪙̶᪵

![三歪教你学Servlet 第140页插图](../assets/images/三歪教你学Servlet_p140_1_ab2bd895.png)

---

՗᪜ऒݷӤྲ᫾
Cookieݢզᦡᗝdomainં௔๶ਫሿ᪜ऒݷ
Sessionݝࣁ୮ڹጱऒݷٖํප҅ӧݢ३ऒݷ
2.6 Servletਞق௔ᳯ᷌
 
ኧԭServletฎܔֺጱ҅୮ग़ӻአಁᦢᳯServletጱ෸ײ҅๐ۓ࢏տԅྯӻአಁڠୌӞӻᕚᑕ̶୮ग़ӻአಁ
ଚݎᦢᳯServletوՁᩒრጱ෸ײ੪տڊሿᕚᑕਞقᳯ̶᷌
ܻڞғ
1. ইຎӞӻݒᰁᵱᥝग़ӻአಁوՁ҅ڞଫ୮ࣁᦢᳯᧆݒᰁጱ෸ײ҅ےݶྍ๢ګsynchronized (੒᨝)
{}
2. ইຎӞӻݒᰁӧᵱᥝوՁ҅ڞፗളࣁ doGet() ౲ᘏ doPost()ਧԎ.ᬯ໏ӧտਂࣁᕚᑕਞقᳯ᷌
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y

![三歪教你学Servlet 第141页插图](../assets/images/三歪教你学Servlet_p141_1_1fda961c.jpeg)

![三歪教你学Servlet 第141页插图](../assets/images/三歪教你学Servlet_p141_2_3c233a1a.jpeg)