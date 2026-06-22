---
title: Java基础知识篇
source: JavaGuide/Java/Java基础知识篇.pdf
pages: 43
converted_at: 2026-06-22 22:30:14
---

# Java基础知识篇

必知
 
关于本⼩册
 
hÒù̯;¹dƜ\ňǏ Java bǜMď§¸Êê-ʜ̨-ʜ
Ǜƣ̯=̰½Ĝż̯½¸M
½Ĝż̯½¸M̨n-ʜ̯%ǻ3·Ł%Ùð
bǜMɃƇǛƣ̨
ªÏ;?ɇ ̪JavaGuideÁǂźě̫ Ǖǈːǲ̯hĻ.bǜMòĤ®
̯)-ʜbǜM̉ʊXƄM̨̪JavaGuideÁǂźě̫ůːǲě9
Ñ̰https://snailclimb.gitee.io/javaguide-interview ̨
是否免费?
 
-ʜňǏ²uƗĸ?ɇ̬9Ñ̰https://github.com/Snailclimb/JavaGuide ̨
⼩册系列会涵盖哪些知识点?
 
Ů+ģ¥ȸ̯˂̉ʊg ¦bǜM
1. Java̰Ŗ̑̆ȋõ̧ü:̧JVM
2. ŇŕkȒ̰̆Ňŕk ʍ̧ɳňǤ
3. ĲǼ˹̰ MySQĻRedis
4. ̓ɪ̰SprinģNetty......
5. 3Ưƅ
如何贡献
 
8ːǲ)Ǔglưɹ9p(6Ċÿ
8ːǲ)Ǔglưɹ9p(6Ċÿ JavaGuide ĵš
ĵš issue ńĻ
ńĻ pr,5
5
ȅ pr ǹƅ̩̩̩
ǹƅ̩̩̩
¡Z(6é)ɿʠ̰koushuangbwcx@163.com¢šº̨
Ƃñ8UĵƢ̖$£(6ɈĚg ŭƅ̰
o!JavaȒ̆Ă31.2.1òĤ˺Ƚ	Êê̯ýĖ`˺Ƚ̰̩ȁǆȁǆ̩ 
X̬ǚÀ(6ųƵ Oracle ƀp~˥̯9Ñ̰~~~~̨
ĵjƣȸ¯vŢ$Æĸ̯Ƃñ8ƴæȸĨKäƣȸ¯̨
如何赞赏
 
glo!~˥<	ƖǢr̯ȅÃbǜÒƁ̨ǟǇÒƁŮwĵ
jbǜɄ̯̊Hmȑ̠ɑ®±8Ħ̨ÒƁ/	ƗĸÝƧǃÌ̡̯ĵjÇ
ÃǲĻŔæ̨ÒƁiȫ8Êê̯XX˘ÁƟǩ̬
1
JavaGuide

---

2
JavaGuide

![Java基础知识篇 第2页插图](../assets/images/Java基础知识篇_p2_1_861817a1.png)

---

Mź·Ł¨Ɇİǁ$¤½ɗw5X~þ̯ü(Ɨĸî½~˥Ǖǈ̪Java Áǂ
ź̫6ǁ Java çǓęŢƪYſƨɇ̨
1. Java ȒŞ
1.1. Java ÃÌ̭Ȓ̆˂Ƌ¢ďǜ̮
1.1.1. Java ƃƺ	ł¦ģM?
1.1.2. · JVM JDK ; JRE 5ɝǨé˔Ħȫ
1.1.2.1. JVM
1.1.2.2. JDK ; JRE
1.1.3. Oracle JDK ; OpenJDK <±
1.1.4. Java ; C++Ʋ¥?
1.1.5. T" Java ǓɀwȎ ýEǓɀ;-ǓɀwȎ	ħ?
1.1.6. Java ýEǓɀ¢-Ǔɀe	ł¦Ȉ¥?
1.1.7. import java ; javax 	T"Ʋ¥̲
1.1.8. T"' Java ƃƺ“ʭ̌¢ĦʌüǗ”̲
1.2. Java ƃä
1.2.1. Ż́ǣďæ;Ż́˨ďæƲ¥?
1.2.2. ·Łʌ̲
1.2.3. Ǜǜ́;·ʶŻƲ¥T"̲
1.2.4. Java	ł¦ď§·ʶŻ̲
1.2.5. |Ȇĭŕ́
1.2.6. continuȩbreaķ;returnƲ¥T"̲
1.2.7. Java̋ǣĦ"̲T"ȎǣɵȌ̲ʗ˖ ďEéǕ̲́
1.2.8. ==;equalsƲ¥
1.2.9. hashCode()¢ equals()
1.3. ȒĲǼȎǣ
1.3.1. Java_ȒĲǼȎǣT"̲<ýĩĢȎǣT"̲ŀ
˃EØŻŎì̲
1.3.2. ]Ģʠ¢˰ʠ
1.3.3. 8_ȒȎǣĩĢȎ;ďæˣ
1.4. pä̭̜Ĳ̮
1.4.1. T"pä˩iƸ?˩iƸȎpäOET"?
1.4.2. T" Java D	Ƹĥˡ̲
1.4.3. ¸É;¸ŹƲ¥ - 1.4.3.1. ¸É - 1.4.3.2. ¸Ź
1.4.4. Ľ̤Ȑ vs ʩ̤Ȑ
1.4.5. päĆ_Ȏǣ
2. Java ā<ǫ
2.1. Ȏ;<ǫ
2.1.1. ā<ǫ;ā)ǓƲ¥
2.1.2. ˁƱȖ Constructor Ƀ(t override?
2.1.3.  Java Ȝ\Qȝ/	ųĲˁƱpäE
2.1.4. @Ĕ¼æ¢ȭĂ¼æƲ¥	ł¦̲
3
JavaGuide

---

2.1.5. ǟǇ<ǫET"ĭŕ́?<ǫÀ¢<ǫȰE	ħ?
2.1.6. ȎˁƱpäET"? ɓȎ/	į{ˁƱpä̯
ĖǓɀ°ȸʁy? T"?
2.1.7. ˁƱpä	ł¦ģ¯̲
2.1.8. ƊE4ȎˁƱpäeŸƊEɲȎ/	ųĲˁƱpä,»Ů
?
2.1.9. <ǫ®z¢ŶāI%ȰE®z,hĻ	T"?
2.2. ā<ǫPģʽ
2.2.1. ʪĢ
2.2.2. Ʒɒ
2.2.3. ƚ
2.3. ǧɽ́
2.3.1. ƐƚpäòƊEŤƐƚ@ĔT"Ťä?
2.3.2. Ɛƚpä;ˈpä	ħ
2.3.3. ď§·ʶŻÙð:static,ﬁnal,this,super
2.4. ÿă;ǴǫȎ
2.4.1. ÿă;ǴǫȎƲ¥T"̲
2.5. »Ğ¸bǜM
2.5.1. String StringBu!er ; StringBuilder Ʋ¥T"? String 
T"(¼?
2.5.2. Object Ȏď§päÙð
2.5.3. == ¢ equals(¸)
2.5.4. hashCode ¢ equals (¸)
2.5.4.1. hashCodḙ̮ʗ˖
2.5.4.2. T"	 hashCode
2.5.4.3. hashCodḙ̮¢ equals̭̮®·ɍ
2.5.5. Java ɀǏķgl	¦ŻƘÇyɀǏķ̯È"Ƥ̲
2.5.6. ¤½EʶȀʄÃďEh_pä
3. Java ʔ&Ȳȏ
3.1. ȋõ
3.1.1. Collections çǚȎ; Arrays çǚȎď§päÙð
3.2. ɺď
3.2.1. Java ɺďȎȵaðˁâ
3.2.2. Throwable ȎďEpä
3.2.3. try-catch-ﬁnally
3.2.4. ıE try-with-resources ņ˒try-catch-finally
3.3. ůǓ
3.3.1. ƼȽůǓ̧Ǔɀ̧ÇǓȒ˂Ƌ̨6ǁI%e·ňT"?
3.3.2. ůǓ	ł¦Ȓɡƚ?
3.4. ~Ó¢ I\O º
3.4.1. Java  IO º3_?
4
JavaGuide

---

3.4.1.1. ɤZ	ŻŎº,T"+	Ż́º?
3.4.1.2. BIO,NIO,AIO 	T"Ʋ¥?
4. ųƵ
5. ¨Ɇİ
1. Java 基本功
 
1.1. Java ⼊⻔（基础概念与常识）
 
1.1.1. Java 语⾔有哪些特点?
 
1. ƼēŅY̱
2. ā<ǫ̭ʪĢ̯Ʒɒ̯ƚ̮̱
3. ĄƔR·¯̭ Java ɸ̂kWĄƔR·¯̮̱
4. (ű¯̱
5. µu¯̱
6. ƎĮůṶ̌ C++ ƃƺ/	òȧůǓkġ̯ČŢɕƊEɳňǤůǓŞ
ÇyůǓǓɀƧŇ̯f Java ƃƺûĵʇůǓƎĮ̮̱
7. ƎĮ ʍʭǓüȝ.pṶ̄ Java ƃƺ˵*Ƽķ ʍʭǓƧŇ̯Č
Java ƃƺȡƎĮ ʍʭǓfȝ.pŪ̮̱
8. ʭ̌¢ĦʌüǗ̱
ǧ°̭ų§̰ issue#544̮̰C++11 ?Ḓ̌2011 C$£̮,C++ȰÃůǓ
˹̯ windowşlinux̧macos (6ıEstd::thread;std::asyncǟǇ
ůŲ̌ųƵɷÿ̰http://www.cplusplus.com/reference/thread/thread/?kw=thre
ad
1.1.2. 关于 JVM JDK 和 JRE 最详细通俗的解答
 
1.1.2.1. JVM
 
Java ɸ̂k̭JVM̮ĭy Java ŻŎŘɸ̂k̨JVM 	ʈ<ňǤģW
̭Windows̯Linux̯macOS̮̯ŮıE®ŻŎŘ̯Ğ%U7®ð
l̨
T"ŻŎŘ
T"ŻŎŘ?ʒEŻŎŘğT"
ʒEŻŎŘğT"?
 Java ̯JVM (6«ĦņŘŃ\字节码̭ī˾Ƕ .class ~Ó̮̯Ğ
āŊħģğ«Ȗ̯Dāɸ̂k̨Java ƃƺé)ŻŎŘpƅ̯Ǔ
ßĦƜĥǤĦʌǣƃƺʁyƌɨǉÊê̯$cĨƳĦʌǣƃƺ(ɾˢ
ģM̨6 Java Ǔɀĭy$±ǳjƌ̯fȝ̯ŨŻŎŘüʈ<_ģk
Ȗ̯Č̯Java ǓɀRɕ¸ʭ̌Ū(_ɳňǤŇŕkĭy̨
Java Ǔɀ¶ɇņŘĭyɖ	 
Ǔɀ¶ɇņŘĭyɖ	  3 ŷ̰
ŷ̰
5
JavaGuide

---

%ėŭáŁ .class->kȖŘ ŷ̨ŷ JVM ȎÉȖūŸÉŻŎŘ
~Ó̯ZJé)ĦʌȖ˗yĦʌʁy̯_pƅʁyƙß®<±ǳƹ̨fȝ̯	¦p
ä;ņŘǝvďėtƊE(ɼÖMņŘ)̯6JȰÇ JIT ʭ̌Ȗ̯
f JIT Ķĭy$ʭ̨̌¡ JIT ʭ̌Ȗ²@}aʭ̌J̯»­ŻŎŘ<ýkȖŘĨ
Ǘ ̯ a(6ĊÿıĘf%bS̯kȖŘĭyƌɨʅj Java ĦʌȖ
̨Ħʌ%T"vď' Java ʭ̌¢ĦʌǦǗƃƺ̨
HotSpot ʒE̕¯ǀˉ(Lazy Evaluation)\ä̯ǽǼ©ǒʓ̯Ų˳Ă3ň
ǤƨɇD	=-Ă3ņŘ̭ÖMņŘ̮̯f JIT ėʭ̌Ă3̨
JVM ǽǼņŘnatʁyFɯôȋmëü®ý9\7¦Ơķ̯Čʁya
ĲÚ̯ĞƙßÚ>̨JDK 9 ȰÃ_ʭ̌Ȩƅ AOT(Ahead of Time
Compilation)̯ĞĊÿ­ŻŎŘʭ̌@kȖŘ̯`ʟƗ JIT ȪÖzŀp
?ɔ̨JDK ƎĮ3ȵʭ̌; AOT ʬıĘ¬ ̯AOT ʭ̌Ȗʭ̌Ŕæʅ
± JIT ʭ̌Ȗ̨
Ùð̰
Ùð̰
Java ɸ̂k̭JVM̮ĭy Java ŻŎŘɸ̂k̨JVM 	ʈ<ňǤģW
̭Windows̯Linux̯macOS̮̯ŮıE®ŻŎŘ̯Ğ%U7®ð
l̨ŻŎŘ;ňǤ JVM W Java ƃƺ“aʭ̯̌őğ(6ĭy”·ʶ̨
1.1.2.2. JDK 和 JRE
 
JDK  Java Development Kit̯ĞŞʕu Java SDK̨Ğƕ	 JRE ƕ	
Ɔ̯+	ʭ̌Ṷ̑javac̮;çṷ̈̌g javadoc ; jdb̨̮ĞƩǟǇ;ʭ̌Ǔɀ̨
JRE  Java ĭy$ǱȘ̨Ğĭyʭ̌ Java Ǔɀė	òĤȋõ̯ĩ˧ Java
ɸ̂k̭JVM̮̯Java Ȏ˹̯java žȾ;»I¦Ȓ̆ˁǪ́¬̯ĞEǟǇ
Ǔɀ̨
glDĭy  Java Ǔɀr̯="DėµĢ JRE (6̨glė
Çy¦ Java ʭǓpç̯="ėµĢ JDK ̨¬̯ǅ<̨	
$̯īıŕŇŕkÇyŊħ Java ?:̯ʢZėµĢ JDK̨ˈg̯glı
E JSP Ă̙ Web ýEǓɀ̯="¶ȲȏŴ̯DýEǓɀąǋȖĭy Java Ǔ
ɀ̨=T"ė JDK ì̲ýEǓɀąǋȖ­ JSP ÷Ʈ Java servlet̯üȝė
ıE JDK ʭ̌ servlet̨
1.1.3. Oracle JDK 和 OpenJDK 的对⽐
 
6
JavaGuide

![Java基础知识篇 第6页插图](../assets/images/Java基础知识篇_p6_1_a4dabe26.png)

---

(Êêe.
;`ü/	ÿʵ;ıE) OpenJDK ̨=" Oracle ;
OpenJDK eɃǗ¸Ȉɺ̲ é)ôȋ¦ƨǭ̯Ħȫt.

ʑĕÊę̂
< Java 7̯/T"·ʶ9p̨OpenJDK ȂŮwȒ Sun ̈˯ HotSpot ɇņ
Ř̨Čá̯OpenJDK tĈ Java 7 ųƵW̯Ũ Oracle çǓęŜǷ̨· JVM̯
JDK̯JRE ; OpenJDK eƲ¥̯Oracle GŰ˸4 2012 C	XɝǨȫɥ̰
Ḛ̂OpenJDK Ǘʦ˹ɇņŘ¢EˁǇ Oracle JDK ņŘe	T"Ʋ¥̲
ȫ̰Ťďÿč - % Oracle JDK ěˁǇ)ǓȒ OpenJDK 7 ˁǇ̯D˙
Ă3̯ˈgĂ̙ņŘ̯»ĩ˧ Oracle  Java ˇÓ; Java WebStart W̯6
ǁ¦ʪʨɇņŘʮ<țÓ̯gâǹø̢ķȖ̯¦?ɇ}PpțÓ̯g
Rhino̯6ǁ¦ʣɩÛË̯gˀ~˥ń}PpŻĄ̀Ƕñţ̯%Ů
?ɇ Oracle JDK 	Ă3̯Ȍ%ƵʡǎĉŞĂ3̨
Ùð̰
Ùð̰
1. Oracle JDK ˂n 6 Ü:awě̯f OpenJDK ě˂nPÜ:Ư
ą¬ʿ̯o!Ħ/ɊEğ̨ɝFų
§̰https://blogs.oracle.com/java-platform-group/update-and-faq-on-
the-java-se-release-cadence ̨
2. OpenJDK ųƵȨǣüȝ²u?ɇ̯f Oracle JDK  OpenJDK 
W̯ü²u?ɇ̱
3. Oracle JDK ± OpenJDK Xʖ̨OpenJDK ; Oracle JDK ņŘȬ®̯¬
Oracle JDK 	XȎ;¦ɹǧƶ̨Č̯gl?:ʃĉ/ǎĉɘÓ̯
ǇȺĈǠ Oracle JDK̯Ğv)˅ƉǐÁ;ʖ̨ǔ¦Fɯ ̯	¦
ĵ
ıE OpenJDK (ưŽýEǓɀ˷˲Êê̯¬̯DėƆƮ
Oracle JDK (6ĦƜÊê̱
4. ȳý¯; JVM ¯p̯Oracle JDK ¢ OpenJDK ®±ĵʇX¯̱
5. Oracle JDK ī­:ƯěĵʇùƎĮ̯EƍnaŢɕé)X5
ě¤!ƎĮ¤½5ě̱
6. Oracle JDK ǽǼ©ÇġņŘŽ(ʬȺ¤!Ž(̯f OpenJDK ǽǼ GPL v2 Ž(¤
!Ž(̨
1.1.4. Java 和 C++的区别?
 
bS.
/Y) C++̯¬Áƀ/QŌʰ% Java ; C++ ±ƻ̬/Ƥ
ä̬̬̬ŕ/Y) C++̯ï ̬
ā<ǫƃƺ̯ƎĮʪĢ̧Ʒɒ;ƚ
Java ĵʇŶʈĊÿʹÊòǗ̯ǓɀòǗXµu
Java ȎēƷɒ̯C++ ƎĮ¸Ʒɒ̱ȗZ Java Ȏ(6Ʒɒ̯¬ÿ
ă(6Ʒɒ̨
Java 	]òǗŵ«kġ̯ėǓɀĔV]ʌREòǗ
 C ƃƺ̯Ż́˨ńŻ́Ĳț5J	ˆáŻ́
ƃƺ̯Ż́˨ńŻ́Ĳț5J	ˆáŻ́‘\0’´ƈðɧ̨
´ƈðɧ̨
¬̯
¬̯Java ƃƺ/	ðɧ́˂Ƌ̨
ƃƺ/	ðɧ́˂Ƌ̨ Ƹ!ĽßŚƵÊê̯ǚÀÝ
ªÏǪ~þ̰
7
JavaGuide

---

https://blog.csdn.net/sszgg2006/article/details/49148189
1.1.5. 什么是 Java 程序的主类 应⽤程序和⼩程序的主类有何不同?
 
Ǔɀ(6	Ȏ̯¬D	ȎwǪ̑ Java ýEǓɀ̯wȎŶ
ĩɫ maiṋ̮päǪ̑f Java -Ǔɀ̯wȎƷɒňǤȎ JApplet
ń Applet 4Ǫ̑ýEǓɀwȎĘ public Ȏ̯¬-ǓɀwȎĘŢɕ
public Ǫ̑wȎ Java ǓɀʁyÃăM̨
1.1.6. Java 应⽤程序与⼩程序之间有哪些差别?
 
Ƽē'ýEǓɀ¶wůǓʞ]( main() pä)̨applet -Ǔɀ/	 main() p
ä̯w̝ȞȉȖƥĭy(ƊEinit()ńĻrun()ʞ])̯̝ÃȞȉȖMĹ
ﬂash -ÕťȎȢ̨
1.1.7. import java 和 javax 有什么区别？
 
?Ď$£ JavaAPI Ţėĩ java ?ĩ̯javax ¡$D˾Ƕ API ĩı
ĘZfő1$ªɾ̯javax ˗ʐ9˾Ƕ@ Java API ț@Ă3̨¬̯­˾Ƕ¶
javax ĩɾ] java ĩȸ[ȿƦ̯5ĿȼȓʆW	ņŘ̨Č̯5ĿƜ
javax ĩ­@Ǜƣ API Ă3̨
6̯Ȥ java ; javax /	Ʋ¥̨Ż̨
1.1.8. 为什么说 Java 语⾔“编译与解释并存”？
 
jĳʭǓƃƺɈĚǓɀʁypƅ3ʭ̌ǣ;Ħʌǣh_̨Ƽē'̯ʭ̌ǣƃƺŶ
ʭ̌Ȗʈ<ģɳňǤ­ɇņŘa¯ǯ̌@(tĖĄƔʁykȖṞ̌Ħʌǣƃƺ
ŶĦʌȖ<ɇǓɀ˗yĦʌ@ģĄƔkȖŘüǃīʁy̨±g̯ːǲƿ~
0̯(6ċƿ~ǯ̌
ĔƖǢːǲ̯ 	h_ĈǠpƅ̯(6Ÿzǯ̌
Ĕ­
uƿ~0̭ɇŘ̮ǯ̌@ʂƃ̯,ːǲ̯(6Lǯ̌
Ĕǯ̌Ƙ̯
ʝĐːǲƘ̯ƹƹŒǲ²̨
Java ƃƺɤǚ	ʭ̌ǣƃƺģʽ̯ǚ	Ħʌǣƃƺģʽ̯ Java Ǔɀv)Ÿ
ʭ̯̌JĦʌhŷ̗̯Ũ Java ʭŹǓɀėŸv)ʭ̌ŷ̗̯*@ŻŎŘ̭*.class
~Ó̮̯_ŻŎŘŢɕŨ Java ĦʌȖĦʌʁy̨Č̯%(6ŗ Java ƃƺʭ̌
¢ĦʌüŲ̈́
1.2. Java 语法
 
1.2.1. 字符型常量和字符串常量的区别?
 
1. ǹƅ: Ż́ďæēȰİȰ2Ż́; Ż́˨ďæĀȰİȰ2ɓƟŻ́
2. ɫȜ: Ż́ďæ®¡ƛǣƸ( ASCII Ƹ),(6ų´Ƈƅĭŕ; Ż́˨ďæņ
´9ÑƸ(ĖŻ́˨òǗǗíȧ)
3. ˃òǗ- Ż́ďæD˃ 2 ŻŎ; Ż́˨ďæ˃ɓƟŻŎ (Ł̰
Ł̰ char 
Java ˃hŻŎ
˃hŻŎ)
8
JavaGuide

---

java ʭǓŚ}Ćḛ̌2.2.2 Ŏ 
1.2.2. 关于注释？
 
Java Łʌ	P_̰
1. ēyŁʌ
2. yŁʌ
3. ~˥Łʌ̨
%ʭŹņŘ$£̯glņŘæ±ǳØ̯%KńĻǺǍ»I@Ĕ+(6.ŖŅ9
œņŘ̯¬¡ȂŮðˁ˓ƶɞ2̯%ėEŁʌ̨Łʌüʁy̯
%ǓɀĔŹUK̯ŁʌņŘ'{Œ̯ƩƖǢņŘ
>ƙ9«åņŘ
e̐ȩ·ň̨Č̯ŹǓɀ$£őVŁʌŤďſȷ̨
̪Clean Code̫Œ{ȸŶ7̰
ņŘŁʌÚɝǨÚ̨ȤņŘŁʌ̯%ƴæɍʋ
ņŘŁʌÚɝǨÚ̨ȤņŘŁʌ̯%ƴæɍʋ
;NķKņŘȆØŢŁʌ̨
;NķKņŘȆØŢŁʌ̨
ɓʭǓƃƺǄƩ	´Ƈs̯ėŁʌ̯ƴæé)ņŘ̣Ƚ̨
ɓʭǓƃƺǄƩ	´Ƈs̯ėŁʌ̯ƴæé)ņŘ̣Ƚ̨
ȱˈ4̰
,Ƭ ƶɞŁʌ̯DėǟǇ¢ŁʌƺQú̜Ĳī(
ý˒Ʈ
1.2.3. 标识符和关键字的区别是什么？
 
// check to see if the employee is eligible for full benefits
if ((employee.falgs & HOURLY_FLAG) && (employee.age > 65))
if (employee.isEligibleForFullBenefits())
9
JavaGuide

![Java基础知识篇 第9页插图](../assets/images/Java基础知识篇_p9_1_1381d278.png)

---

ʹÊɭġ
ʹÊɭġ
private
protected
public
 
 
 
 
Ȏ̯pä;¼æǧɽ́
abstract
class
extends
ﬁnal
implements
interface
native
 
new
static
strictfp
synchronized
transient
volatile
 
Ǔɀɭġ
break
continue
return
do
while
if
else
 
for
instanceof
switch
case
default
 
 
ɹğ«
try
catch
throw
throws
ﬁnally
 
 
ĩ®·
import
package
 
 
 
 
 
ȒȎǣ
boolean
byte
char
double
ﬂoat
int
long
 
short
null
true
false
 
 
 
¼æȰE
super
this
void
 
 
 
 
ĨƳŻ
goto
const
 
 
 
 
 
%ʭŹǓɀ$£̯ėæ9Ǔɀ̧Ȏ̧¼æ̧päz½Ż̯	Ǜǜ
̯́Ƽē'̯Ǜǜ́Ż̨¬	¦Ǜǜ̯́Java ƃƺv̑ˍ»ģ̃
ɫȜ̯DEģ9p̯_ģ̃Ǜǜ́·ʶŻ̨Č̯·ʶŻt̑ˍģ̃
ɫȜǛų̈̀́±g̯%Aď*^ ̯“ɉʫȭ”Żvt̑ˍģ̃ɫ
Ȝ̯6gl?8ơ̯ơŻŃ“ɉʫȭ”̯“ɉʫȭ”%Aď*^
·ʶŻ̨
1.2.4. Java中有哪些常⻅的关键字？
 
1.2.5. ⾃增⾃减运算符
 
ŹņŘ)Ǔ̯ď§_FɯėǔƛĲȎǣ¼æ| 1 ńȆØ 1̯Java ĵʇ
_ģ̃ĭŕ̯́E_´Ƈƅ̯Ń\|ĭŕ̭́++);Ȇĭŕ̭́--̨̮
++;--ĭŕ́(6ɳĲe̯(6ɳĲeJ̯¡ĭŕ́ɳĲe
$̯Ÿ|/Ȇ̯̑Ƹ̱¡ĭŕ́ɳĲeJ$̯Ÿ̑Ƹ̯|/Ę̑ˈg̯¡
“b=++a”$̯Ÿ|̭K| 1̮̯̑Ƹ̭̑ƸU b̮̱¡“b=a++”$̯Ÿ̑Ƹ(̑
ƸU b)̯|̭K| 1̨̮̯++a ʄ7 a+1 Ƹ̯a++ʄ7 a Ƹ̨
EĬă̎̰“́İŸ/Ȇ̯́İJJ/Ȇ”̨
1.2.6. continue、break、和return的区别是什么？
 
ˤǱðˁ̯¡ˤǱóÓĺǄńĻˤǱaĲƇĘ$̯ˤǱ°ďðɧ̨¬̯	
$£(ėˤǱ)Ǔ̯¡:*ǔ_óÓeJ ̯ĵĿȦˤǱ̯ėE 
·ʶɴ̰
1. continue ̰Ŷɋ7¡aˤǱ̯ƷŦ aˤǱ̨
2. break ̰Ŷɋ7ƛˤǱÀ̯ƷŦʁyˤǱ ƃĮ̆
10
JavaGuide

---

return Eɋ7pä̯ðɧĖpäĭy̨return ɖ	h_Eä̰
1. return; ̰ĊÿıE return ðɧpäʁy̯E/	˩iƸ̜Ĳpä
2. return value; ̰return ģƸ̯E	˩iƸ̜Ĳpä
1.2.7. Java泛型了解么？什么是类型擦除？介绍⼀下常⽤的通配符？
 
Java ̋ǣ̭generics̮ JDK 5 ȰÃģ¯, ̋ǣĵʇʭ̌$Ȏǣµuʤǐk
ġ̯Ėkġ̇ŽǓɀĔʭ̌$ʤǐŤäȎǣ̨̋ǣŔųĲķȎǣ̯'
ɳĲǼȎǣtŶųĲ̨
Java̋ǣˮ̋ǣ̯
̋ǣˮ̋ǣ̯Javaʭ̌ù̯	̋ǣmëtɵƬ̯
ʭ̌ù̯	̋ǣmëtɵƬ̯
éď'ȎǣɵȌ
éď'ȎǣɵȌ ̨ X·ȎǣɵȌÊê̯(6ƏǪ~þ̰̪Java̋ǣ
ȎǣɵȌ6ǁȎǣɵȌÔÊê̫ ̨
̋ǣɖ	P_ıEpƅ:̋ǣȎ̧̋ǣÿă̧̋ǣpą̈
1.̋ǣȎ
̋ǣȎ̰
għˈķ̋ǣȎ̰
List<Integer> list = new ArrayList<>();
list.add(12);
//这⾥直接添加会报错
list.add("a");
Class<? extends List> clazz = list.getClass();
Method add = clazz.getDeclaredMethod("add", Object.class);
//但是通过反射添加，是可以的
add.invoke(list, "kl");
System.out.println(list)
//此处T可以随便写为任意标识，常⻅的如T、E、K、V等形式的参数常⽤于表示泛型
//在实例化泛型类时，必须指定T的具体类型
public class Generic<T>{ 
   
    private T key;
    public Generic(T key) { 
        this.key = key;
    }
    public T getKey(){ 
        return key;
    }
}
11
JavaGuide

---

2.̋ǣÿă
̋ǣÿă ̰
W̋ǣÿă̯ŶȎǣ̰
W̋ǣÿă̯ŶȎǣ̰
3.̋ǣpä
̋ǣpä ̰
ıḚ
ďEéǕ́̰
ďEéǕ́̰ T̯E̯K̯V̯̲
̯̲
̲ ´ƈȸ java Ȏǣ
Generic<Integer> genericInteger = new Generic<Integer>(123456);
public interface Generator<T> {
    public T method();
}
class GeneratorImpl<T> implements Generator<T>{
    @Override
    public T method() {
        return null;
    }
}
class GeneratorImpl<T> implements Generator<String>{
    @Override
    public String method() {
        return "hello";
    }
}
   public static < E > void printArray( E[] inputArray )
   {         
         for ( E element : inputArray ){        
            System.out.printf( "%s ", element );
         }
         System.out.println();
    }
// 创建不同类型数组： Integer, Double 和 Character
Integer[] intArray = { 1, 2, 3 };
String[] stringArray = { "Hello", "World" };
printArray( intArray  ); 
printArray( stringArray  ); 
12
JavaGuide

---

T (type) ´ƈǚÀjavaȎǣ
K V (key value) 3¥ņ´javaʶƸKey Value
E (element) ņ´Element
X·Java ̋ǣéǕ́(6ƏǪ~þ̰̪ǬǬ-JAVA ̋ǣéǕ́ T̯
E̯K̯V̯̲̫
1.2.8. ==和equals的区别
 
== : ĞE˦ȇh<ǫ9Ñ®z̨ī˦ȇh<ǫ<ǫ̨
(ȒĲǼȎǣ
ȒĲǼȎǣ==±ǳƸ̯ȰEĲǼȎǣ
±ǳƸ̯ȰEĲǼȎǣ==±ǳòǗ9Ñ
±ǳòǗ9Ñ)
 Java D	Ƹĥˡ̯6̯< == '̯ŵ±ǳȒĲǼȎǣ̯+ȰE
ĲǼȎǣ¼æ̯»Ŕ±ǳƸ̯DȰEȎǣ¼æǗƸ<ǫ9Ñ̨
equals() : ĞE˦ȇh<ǫɃ®z̯ĞE±ǳȒĲǼȎǣ¼
æ̨equals()päǗObjectȎ̯fObjectȎ	ȎĊÿńÿɲǪ̑
ObjectȎequals()pä̰
equals() päǗh_ıEFɯ̰
Fɯ 1̰Ȏ/	ˠʊ equals()pą̈ȍé)equals()±ǳĖȎh<ǫ$̯z
Ĵé)“==”±ǳh<ǫ̨ıEǮŗ ObjectȎequals()pą̈
Fɯ 2̰Ȏˠʊ equals()pą̈ɖ̯%ˠʊ equals()päh<ǫ
òĤ®ẕɓĞ%òĤ®z̯ȍ˩i true(ī̯ŗh<ǫ®z)̨
ȱˈ4̰
ȱˈ4̰
public boolean equals(Object obj) {
     return (this == obj);
}
public class test1 {
    public static void main(String[] args) {
        String a = new String("ab"); // a 为⼀个引⽤
        String b = new String("ab"); // b为另⼀个引⽤,对象的内容⼀样
        String aa = "ab"; // 放在常量池中
        String bb = "ab"; // 从常量池中查找
        if (aa == bb) // true
            System.out.println("aa==bb");
        if (a == b) // false，⾮同⼀对象
            System.out.println("a==b");
        if (a.equals(b)) // true
            System.out.println("aEQb");
        if (42 == 42.0) { // true
            System.out.println("true");
        }
13
JavaGuide

---

'{̰
'{̰
String  equals pät¸Ź)̯ Object  equals pä±ǳ
<ǫòǗ9Ñ̯f String  equals pä±ǳ<ǫƸ̨
¡ǟǇ String Ȏǣ<ǫ$̯ɸ̂kďæˣƏċ	/	vǗƸ;
ǟǇƸ®<ǫ̯gl	Ğ̑U¡ȰĘgl/	ďæˣ¸ǟ
Ǉ String <ǫ̨
StringȎequals()pä̰
1.2.9. hashCode()与 equals()
 
Áƀ(Ê̰“¸Ź) hashcode ; equals"̯T"¸Ź equals $Ţɕ¸
Ź hashCode pä̲”
1)hashCode()ʗ˖
ʗ˖:
hashCode() E¤½¿ƂŘ̯ȔɚǏṞ̌ĞȤ˩i int ƛĲ̨
¿ƂŘEȸĖ<ǫ¿Ƃ´ʏȰíą̇hashCode()Ȝ JDK  Object
Ȏ̯ŉ1 Java ŊħȎĩɫ	 hashCode() ̜Ĳ̨ǖáėŁ̰
Object  hashcode pä9pä̯E c ƃƺń c++ W̯ĖpäéďE
­<ǫ òǗ9Ñ ÷ƮƛĲeJ˩į
    }
}
public boolean equals(Object anObject) {
    if (this == anObject) {
        return true;
    }
    if (anObject instanceof String) {
        String anotherString = (String)anObject;
        int n = value.length;
        if (n == anotherString.value.length) {
            char v1[] = value;
            char v2[] = anotherString.value;
            int i = 0;
            while (n-- != 0) {
                if (v1[i] != v2[i])
                    return false;
                i++;
            }
            return true;
        }
    }
    return false;
}
14
JavaGuide

---

ɚǏ´ǗʦʶƸ<(key-value)̯ĞģM̰ǽǼ“ʶ”>ƙʤʏ7<ý
“Ƹ”̨»ŬEɚǏŘ̬̭(6>ƙċė<ǫ̮
2)T"	
T"	 hashCode̲
%6“HashSet għʤƏ¸ƶ”ˈ4'{T"	 hashCode̲
¡<ǫÃ HashSet $̯HashSet ŸŇŕ<ǫ hashcode Ƹ˦ȇ<ǫÃ
íȧ̯$¢»IvÃ<ǫ hashcode Ƹ±ǳ̯gl/	®́
hashcode̯HashSet ƫƧ<ǫ/	¸ƶ7W̨¬gl:W	® hashcode Ƹ<
ǫ̯$ƊE equals̭̮päʤƏ hashcode ®z<ǫɃB®̨glhĻ
®̯HashSet L»Ãɳ@Ş̨glr̯¸ɚǏ»Iíą̇
̭̀ Java ʞ˜Œ̪Head ﬁst java̫}©ę̮̌`%ȆØ equals 
aĲ̯®ýĵjʁyƙß̨
3)T"¸Ź
T"¸Ź equals $Ţɕ¸Ź
$Ţɕ¸Ź hashCode pä̲
pä̲
glh<ǫ®z̯ȍ hashcode ®̨h<ǫ®z,<h<ǫ3¥ƊE
equals pä˩i truę¬̯h<ǫ	® hashcode Ƹ̯Ğ%®z
 ̨Č̯
Č̯equals pätˠʊ)̯ȍ
pätˠʊ)̯ȍ hashCode päŢɕtˠʊ̨
päŢɕtˠʊ̨
hashCode()Ǯŗy<ʆ<ǫƑ*ƝģƸ̨gl/	¸Ź
hashCode()̯ȍĖ class h<ǫRřgħ®z̭īıh<ǫŶā®
ĲǼ̮
4)T"h<ǫ	®
T"h<ǫ	® hashcode Ƹ̯Ğ%®z̲
Ƹ̯Ğ%®z̲
OĦʌí-ʴɦÊę̂6 òĤ̀̪Head Fisrt Javą̫
 hashCode() ıEɞ̏ŕäŽL<ǫĥi®ɞ̏Ƹ̨Ú˕ʲ
ɞ̏ŕäÚĤŅʛʷ̯¬¢ĲǼƸʼ3Ưģ¯	·̭ɼʛʷŶ
<ǫ!® hashCodę
%ĵ HashSet,gl HashSet <±$£̯` hashcode 	<
ǫ̯ĞıE equals() ˦ȇɃB®̨' hashcode DE˱-Əċ
@̨
 
X· hashcode() ; equals() òĤ(6Ə̰Java hashCode() ; equals()
ɓƟÊêĦȫ
1.3. 基本数据类型
 
public native int hashCode();
15
JavaGuide

---

ȒȎǣ
ȒȎǣ
íĲ
íĲ
ŻŎ
ŻŎ
ǮŗƸ
ǮŗƸ
int
32
4
0
short
16
2
0
long
64
8
0L
byte
8
1
0
char
16
2
'u0000'
ﬂoat
32
4
0f
double
64
8
0d
boolean
1
 
false
1.3.1. Java中的⼏种基本数据类型是什么？对应的包装类型是什么？各⾃占⽤多
少字节呢？
 
Java	8_ȒĲǼȎǣ̯3¥̰
1. 6_ĲŻȎǣ ̰bytȩshorţinţlonģﬂoaţdouble
2. 1_Ż́Ȏǣ̰char
3. 1Ưȣǣ̰boolean̨
ǒ_ȒȎǣ	<ýĩĢȎ3¥̰BytȩShorţIntegeŗLonģFloaţ
DoublȩCharacteŗBoolean
<boolean̯ƀp~˥ţ{ȸȜ̯ĞǸˑ JVM ˘ǎǚÀW̨̐ȩ«Ħ˃
E 1í̯¬ȤƵʡŇŕkjƌǗʦȠ̨
Ł̰
1. Java OıE long ȎǣĲǼĲƸJ L̯Ƀȍ­ƛǣĦˋ̰
2. char a = 'h'char :ēȰİ̯String a = "hello" :ĀȰİ
1.3.2. ⾃动装箱与拆箱
 
Ģʠ
Ģʠ̰­ȒȎǣEĞ%<ýȰEȎǣĩĢ2̱
˰ʠ
˰ʠ̰­ĩĢȎǣ÷ƮȒĲǼȎǣ̱
XòĤ§̰ĽÃ̚ˋ Java Ģʠ;˰ʠ
1.3.3. 8种基本类型的包装类和常量池
 
16
JavaGuide

---

Java ȒȎǣĩĢȎĂ3WďæˣȲȏ̯ī
ȒȎǣĩĢȎĂ3WďæˣȲȏ̯ī
Byte,Short,Integer,Long,Character,Booleaṉ
̱ 4 _ĩĢȎǮŗǟǇĲƸ
_ĩĢȎǮŗǟǇĲƸ
[-128̯127] ®ýȎǣ˄ǗĲǼ̯
®ýȎǣ˄ǗĲǼ̯CharacterǟǇĲƸ
ǟǇĲƸ[0,127]ʋȄ˄ǗĲ
ʋȄ˄ǗĲ
Ǽ̯
Ǽ̯Boolean Ċÿ˩i
Ċÿ˩iTrue Or Falsęgl×7<ýʋȄʢZ,ǟǇ<ǫ̨
̨gl×7<ýʋȄʢZ,ǟǇ<ǫ̨
Ɋ˄ǗƧȧ[-128̯127]Ʋ̲̭ų§issue/461̮¯;ƨɇeɌˬ̨
h_ʳMĲȎǣĩĢȎ Float,Double ü/	WďæˣȲǫ̑**
Integer ˄ǗɇņŘ̰
˄ǗɇņŘ̰
ýE¾ǥ̰
ýE¾ǥ̰
1. Integer i1=40̱Java ʭ̌$£Ċÿ­ņŘʪĢ@ Integer
public static Boolean valueOf(boolean b) {
    return (b ? TRUE : FALSE);
}
private static class CharacterCache {         
    private CharacterCache(){}
          
    static final Character cache[] = new Character[127 + 1];          
    static {             
        for (int i = 0; i < cache.length; i++)                 
            cache[i] = new Character((char)i);         
    }   
}
    Integer i1 = 33;
    Integer i2 = 33;
    System.out.println(i1 == i2);// 输出 true
    Integer i11 = 333;
    Integer i22 = 333;
    System.out.println(i11 == i22);// 输出 false
    Double i3 = 1.2;
    Double i4 = 1.2;
    System.out.println(i3 == i4);// 输出 false
/**
*此⽅法将始终缓存-128 到 127（包括端点）范围内的值，并可以缓存此范围之外的其他值。
*/
    public static Integer valueOf(int i) {
        if (i >= IntegerCache.low && i <= IntegerCache.high)
            return IntegerCache.cache[i + (-IntegerCache.low)];
        return new Integer(i);
    }
17
JavaGuide

---

i1=Integer.valueOf(40);̯¶fıEďæˣ<ǫ̨
2. Integer i1 = new Integer(40);_Fɯ ǟǇ<ǫ̨
Integer ±ǳXɻǿˈ4
±ǳXɻǿˈ4:
ðl̰
Ħʌ̰
ƃĬ i4 == i5 + i6̯+ɳ́ƭE Integer <ǫ̯ūŸ i5 ; i6 Çy]˰
ʠɳ̯ÇyĲƸ®̯ī i4 == 40̨ZJ Integer <ǫRä¢ĲƸÇyĊÿ±ǳ̯6
i4 ]˰ʠ÷ int Ƹ 40̯5ĿóƃĬ÷ 40 == 40 ÇyĲƸ±ǳ̨
1.4. ⽅法（函数）
 
1.4.1. 什么是⽅法的返回值?返回值在类的⽅法⾥的作⽤是什么?
 
pä˩iƸŶ%¤½ǔpäÀņŘʁyJƑ*ðl̬̭ĵĖpä
(Ƒ*ðl̨̮˩iƸEÿô7ðl̯ı!Ğ(6E»Iɳ̬
1.4.2. 为什么 Java 中只有值传递？
 
  Integer i1 = 40;
  Integer i2 = new Integer(40);
  System.out.println(i1==i2);//输出 false
  Integer i1 = 40;
  Integer i2 = 40;
  Integer i3 = 0;
  Integer i4 = new Integer(40);
  Integer i5 = new Integer(40);
  Integer i6 = new Integer(0);
  
  System.out.println("i1=i2   " + (i1 == i2));
  System.out.println("i1=i2+i3   " + (i1 == i2 + i3));
  System.out.println("i1=i4   " + (i1 == i4));
  System.out.println("i4=i5   " + (i4 == i5));
  System.out.println("i4=i5+i6   " + (i4 == i5 + i6));   
  System.out.println("40=i5+i6   " + (40 == i5 + i6));     
i1=i2   true
i1=i2+i3   true
i1=i4   false
i4=i5   false
i4=i5+i6   true
40=i5+i6   true
18
JavaGuide

---

ūŸiɐ ǓɀƧŇƃƺ	·­ųĲĥˡUpä̭ń̜Ĳ̮¦èĉȏƃ̨ɈƸ
ɈƸ
ƊE
ƊE(call by value)´ƈpäÿôƊEĻĵʇƸ̯fɈȰEƊḘ
´ƈpäÿôƊEĻĵʇƸ̯fɈȰEƊḘcall by
reference)´ƈpäÿôƊEĻĵʇ¼æ9Ñ̨pä(6ǧũĥˡȰE
´ƈpäÿôƊEĻĵʇ¼æ9Ñ̨pä(6ǧũĥˡȰE
<ý¼æƸ̯fǧũĥˡƸƊE<ý¼æƸ̨
<ý¼æƸ̯fǧũĥˡƸƊE<ý¼æƸ̨ ĞE˺Ƚŀ_ǓɀƧŇƃ
ƺ̭D Java)päųĲĥˡpƅ̨
Java ǓɀƧŇƃƺÙʒEɈƸƊĘ'̯pä!	ųĲƸ
ǓɀƧŇƃƺÙʒEɈƸƊĘ'̯pä!	ųĲƸ
̤Ȑ̯'̯päǧũĥˡUĞŊħųĲ¼æòĤ̨
̤Ȑ̯'̯päǧũĥˡUĞŊħųĲ¼æòĤ̨
 é)
 é) 3 ˈ4U8'{
ˈ4U8'{
example 1
ðl̰
ðl̰
Ħˋ̰
Ħˋ̰
public static void main(String[] args) {
    int num1 = 10;
    int num2 = 20;
    swap(num1, num2);
    System.out.println("num1 = " + num1);
    System.out.println("num2 = " + num2);
}
public static void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
}
a = 20
b = 10
num1 = 10
num2 = 20
19
JavaGuide

---

 swap pä̯a̧b ƸÇyšƮ̯üĝȳ num1̧num2̨̯a̧b 
Ƹ̯D¶ num1̧num2 ƶġ)̨'̯a̧b ®¡ num1̧num2 ʉ
̯ʉòĤRřÈ"ǧũ̯ĝȳÝÓ̨
é)ˈ4̯%vbSpäǧũȒĲǼȎǣųĲ̯f<
é)ˈ4̯%vbSpäǧũȒĲǼȎǣųĲ̯f<
ǫȰEųĲ`̯Å
ǫȰEųĲ`̯Å example2.
example 2
ðl̰
ðl̰
  public static void main(String[] args) {
    int[] arr = { 1, 2, 3, 4, 5 };
    System.out.println(arr[0]);
    change(arr);
    System.out.println(arr[0]);
  }
  public static void change(int[] array) {
    // 将数组的第⼀个元素变为0
    array[0] = 0;
  }
1
0
20
JavaGuide

![Java基础知识篇 第20页插图](../assets/images/Java基础知识篇_p20_1_41ad0049.png)

---

Ħˋ̰
Ħˋ̰
array tșĎķ arr ̤Ȑ<ǫȰE̯' array ; arr Ŷā
Ĳț<ǫ̨ Č̯áĂ<ȰE<ǫũ¼Ƣ˞<ý<ǫ̨
é)
é) example2 %v̯Wũ¼<ǫųĲɡƚpäüÓ³
%v̯Wũ¼<ǫųĲɡƚpäüÓ³
Q̨«Ũ.Ƽē̯pä!<ǫȰE̤Ȑ̯<ǫȰEǁ»I̤Ȑ$ȰE
Q̨«Ũ.Ƽē̯pä!<ǫȰE̤Ȑ̯<ǫȰEǁ»I̤Ȑ$ȰE
<ǫ̨
<ǫ̨
.ǓɀƧŇƃƺ̭ģ¥̯
.ǓɀƧŇƃƺ̭ģ¥̯C++; Pascal)ĵʇh_ųĲĥˡpƅ̰ƸƊE;
ĵʇh_ųĲĥˡpƅ̰ƸƊE;
ȰEƊĘ	¦ǓɀḘ̆ʱŧŒĻ̮ŗ
ȰEƊĘ	¦ǓɀḘ̆ʱŧŒĻ̮ŗ Java ǓɀƧŇƃƺ<<ǫʒE
ǓɀƧŇƃƺ<<ǫʒE
ȰEƊE̯Ȥ̯_«Ħ<̨Ũ_ɹĦǚ	ɠȮ¯̯6 
ȰEƊE̯Ȥ̯_«Ħ<̨Ũ_ɹĦǚ	ɠȮ¯̯6 
U7ƢˈɝǨ9̣Ƚ Êę̂
U7ƢˈɝǨ9̣Ƚ Êę̂
example 3
public class Test {
  public static void main(String[] args) {
    // TODO Auto-generated method stub
    Student s1 = new Student("⼩张");
    Student s2 = new Student("⼩李");
    Test.swap(s1, s2);
    System.out.println("s1:" + s1.getName());
    System.out.println("s2:" + s2.getName());
  }
  public static void swap(Student x, Student y) {
    Student temp = x;
    x = y;
    y = temp;
21
JavaGuide

![Java基础知识篇 第21页插图](../assets/images/Java基础知识篇_p21_1_7cb7b14d.png)

---

ðl̰
ðl̰
Ħˋ̰
Ħˋ̰
šƮe̰
šƮeJ̰
    System.out.println("x:" + x.getName());
    System.out.println("y:" + y.getName());
  }
}
x:⼩李
y:⼩张
s1:⼩张
s2:⼩李
22
JavaGuide

![Java基础知识篇 第22页插图](../assets/images/Java基础知识篇_p22_1_290284b9.png)

---

é)hćâ(6.å̍7̰ päü/	ũ¼Ǘʦ¼æ
päü/	ũ¼Ǘʦ¼æ s1 ; s2 <ǫȰ
<ǫȰ
Ę
Ęswap päųĲ
päųĲ x ; y tșĎķh<ǫȰE̤Ȑ̯päšƮ
tșĎķh<ǫȰE̤Ȑ̯päšƮ
h̤Ȑ
h̤Ȑ
Ùð
Ùð
Java ǓɀƧŇƃƺ<<ǫʒEȰEƊE̯Ȥ̯<ǫȰEɈ Ƹĥˡ̨
 Ùð  Java päųĲıEFɯ̰
päǧũȒĲǼȎǣųĲ̭īĲƸǣńƯȣǣ̨̮
pä(6ũ¼<ǫųĲɡƚ̨
päL<ǫųĲȰE<ǫ̨
ųƵ̰
ųƵ̰
̪Java ʔ&Ȳȏʸ Ⅰ̫Ȓ̆bǜ}àě}Ćþ 4.5 -Ŏ
1.4.3. 重载和重写的区别
 
¸É`päƩǽǼʄÃĲǼ̯\7ğ«
¸Ź¡4ȎƷɒɲȎ®pä̯ʄÃĲǼ`̯¬\7	¥ɲȎȳ
ý$̯ˠʊɲȎpä
1.4.3.1. 重载
 
:*Ȏ̯päŢɕ®̯ųĲȎǣ̧Ĳ̧ȕɀ̯pä˩iƸ
;ʹÊǧɽ́(6̨
 ̪Java ʔ&Ȳȏ̫<¸É˂Ƌʗ˖̰
23
JavaGuide

![Java基础知识篇 第23页插图](../assets/images/Java基础知识篇_p23_1_6f5b3d46.png)

---

Ʋ¥M
Ʋ¥M
¸Épä
¸Épä
¸Źpä
¸Źpä
:*ʋȄ
Ȏ
4Ȏ 
ųĲǏ´
Ţɕǧũ
ǧũ
˩iȎǣ
(ǧũ
ǧũ
ɺď
(ǧũ
(6ȆØń˟Ȍ̯ˊ7ńĻXƄɺď
˻̰¸ÉȎpäǽǼĥųʁy̐ȩğ«̨
˻̰¸ÉȎpäǽǼĥųʁy̐ȩğ«̨
1.4.3.2. 重写
 
¸Ź:*ĭyù̯4Ȏ<ɲȎ̇ŽʹÊpäW)ǓÇy¸ʭŹ̨
1. ˩iƸȎǣ̧pä̧ųĲǏ´Ţɕ®̯ˊ7ɺďʋȄ-zɲȎ̯ʹÊǧ
ɽ́ʋȄzɲǪ̑
2. glɲȎpäʹÊǧɽ́ private/ﬁnal/static ȍ4Ȏ¸ŹĖpä̯¬
t static ǧɽpäƩtaį{̨
3. ˁƱpäRät¸Ź
˻̰¸Ź4Ȏ<ɲȎpä¸ũƱ̯áĂ`4ũ¼̯òĂ̐ȩ(6ũ
˻̰¸Ź4Ȏ<ɲȎpä¸ũƱ̯áĂ`4ũ¼̯òĂ̐ȩ(6ũ
¼
ȟ&
ȟ& Guide ǰ5JâǛÙð ̬
ǰ5JâǛÙð ̬
24
JavaGuide

![Java基础知识篇 第24页插图](../assets/images/Java基础知识篇_p24_1_13d126ac.jpeg)

---

ʹÊǧɽ́
(ǧũ
\XɬŭǞġ̭(6ɏǉǞġ̮
:*˫Ƙ
ʭ̌ù
ĭyù
1.4.4. 深拷⻉ vs 浅拷⻉
 
1. ʩ̤Ȑ
ʩ̤Ȑ̰<ȒĲǼȎǣÇyƸĥˡ̯<ȰEĲǼȎǣÇyȰEĥˡɖ̤Ȑ̯Č
ʩ̤Ȑ̨
2. Ľ̤Ȑ
Ľ̤Ȑ̰<ȒĲǼȎǣÇyƸĥˡ̯<ȰEĲǼȎǣ̯ǟǇ<ǫ̯üƶ
ġ»òĤ̯ČĽ̤Ȑ̨
1.4.5. ⽅法的四种类型
 
1̧RųĲR˩iƸpä
2̧	ųĲR˩iƸpä
3̧	˩iƸRųĲpä
// ⽆参数⽆返回值的⽅法(如果⽅法没有返回值，不能不写，必须写void，表示没有返回值)
public void f1() {
    System.out.println("⽆参数⽆返回值的⽅法");
}
/**
* 有参数⽆返回值的⽅法
* 参数列表由零组到多组“参数类型+形参名”组合⽽成，多组参数之间以英⽂逗号（,）隔开，
形参类型和形参名之间以英⽂空格隔开
*/
public void f2(int a, String b, int c) {
    System.out.println(a + "-->" + b + "-->" + c);
}
25
JavaGuide

![Java基础知识篇 第25页插图](../assets/images/Java基础知识篇_p25_1_9f9340f0.jpeg)

---

4̧	˩iƸ	ųĲpä
5̧return R˩iƸpäģ̃ıE
2. Java ⾯向对象
 
2.1. 类和对象
 
2.1.1. ⾯向对象和⾯向过程的区别
 
ā)Ǔ
ā)Ǔ ̰ā)Ǔ¯±ā<ǫj̨
ā)Ǔ¯±ā<ǫj̨ ȎƊE$ėˈķ̯?ɔ±ǳ
̯±ǳŲ˳ƨɇ̯6¡¯5¸ƵæȠ$£̯±gēķ̝Ãƅ
?:̧Linux/Unix zɖʒEā)Ǔ?:̨¬̯ā)Ǔ/	ā<ǫŅŜ
ā)Ǔ/	ā<ǫŅŜ
Ƿ̧ŅƶȨŅ˾Ƕ̨
Ƿ̧ŅƶȨŅ˾Ƕ̨
ā<ǫ
ā<ǫ ̰ā<ǫŅŜǷ̧ŅƶȨŅ˾Ƕ̨
ā<ǫŅŜǷ̧ŅƶȨŅ˾Ƕ̨ ā<ǫ	ʪĢ̧Ʒɒ̧
ƚ¯ģ¯̯6(6ƧŇ7ǉ̦õňǤ̯ıňǤXǵ^̧XŅŜǷ̨
¬̯ā<ǫ¯±ā)Ǔǉ
ā<ǫ¯±ā)Ǔǉ̨
ų§ issue : ā)Ǔ ̰ā)Ǔ¯±ā<ǫj̲̲
üǽÝ̯ā)Ǔė3ǕòǗ̯ŇŕòǗʥɾæ̯Java ¯Ȉ
wÝüĞā<ǫƃƺ̯f Java ľʭ̌ƃƺ̯5ĿʁyņŘ
ü(6Ċÿt CPU ʁy©Çġk̒Ř̨
fā)ǓƃƺĊÿʭ̌@k̒Řƞʁy̯üȝ»Ğ¦ā)Ǔ
Ȋƃƺ¯ü± Java ̨
// 有返回值⽆参数的⽅法（返回值可以是任意的类型,在函数⾥⾯必须有return关键字返回对
应的类型）
public int f3() {
    System.out.println("有返回值⽆参数的⽅法");
    return 2;
}
// 有返回值有参数的⽅法
public int f4(int a, int b) {
    return a * b;
}
// return在⽆返回值⽅法的特殊使⽤
public void f5(int a) {
    if (a>10) {
    return;//表示结束所在⽅法 （f5⽅法）的执⾏,下⽅的输出语句不会执⾏
}
    System.out.println(a);
}
26
JavaGuide

---

2.1.2. 构造器 Constructor 是否可被 override?
 
Constructor t overridḙ¸Ź̮,¬(6 overloaḓ¸É̮,6(6
Ȏ	ˁƱ̜ĲFɯ̨
2.1.3. 在 Java 中定义⼀个不做事且没有参数的构造⽅法的作⽤
 
Java Ǔɀʁy4ȎˁƱpäe̯gl/	E super()ƊEɲȎģˁƱp
ä̯ȍƊEɲȎ“/	ųĲˁƱpä”̨Č̯glɲȎDȜ	ųĲˁƱp
ä̯f4ȎˁƱpäc/	E super()ƊEɲȎģˁƱpä̯ȍʭ̌$
­:*ɹ̯ Java ǓɀɲȎċ/	ųĲˁƱpä(ʇʁy̨ĦƜƤä
ɲȎO\Qȝ/	ųĲˁƱpą̈
2.1.4. 成员变量与局部变量的区别有哪些？
 
1. ¶ƃäǹƅ:@Ĕ¼æĶȎ̯fȭĂ¼æpäȜ¼æńpä
ųĲ̱@Ĕ¼æ(6t public,private,static zǧɽ́ǧɽ̯fȭĂ¼æ
tʹÊɭġǧɽ́ǁ static ǧɽ̱¬̯@Ĕ¼æ;ȭĂ¼æt ﬁnal ǧ
ɽ̨
2. ¶¼æòǗǗʦpƅ:gl@Ĕ¼æıEstaticǧɽ̯="@
Ĕ¼æĶȎ̯gl/	ıEstaticǧɽ̯@Ĕ¼æĶˈ̨f<
ǫǗʆòǗ̯ȭĂ¼æȍǗ̟òŲ̈́
3. ¶¼æòǗ*Ǘ$:@Ĕ¼æ<ǫĂ3̯Ğő1<ǫǟǇfǗ
̯fȭĂ¼æő1päƊEf]Ųđ̨
4. @Ĕ¼ægl/	t̑șƸ:ȍ]6ȎǣǮŗƸf̑Ƹ̭_Fɯˈá:t
ﬁnal ǧɽ@Ĕ¼æŢɕȃƅ9̑Ƹ̮̯fȭĂ¼æȍ]̑Ƹ̨
2.1.5. 创建⼀个对象⽤什么运算符?对象实体与对象引⽤有何不同?
 
new ĭŕ̯́new ǟǇ<ǫˈ̭<ǫˈʆòǗ̮̯<ǫȰEŶā<ǫˈ̭<
ǫȰEǗ̟òǗ̨̮<ǫȰE(6Ŷā 0 ń 1 <ǫ̭ǽ̔4(6ň
Ɓ̯(6ňƁ̮;<ǫ(6	 n ȰEŶāĞ̭(6E n ó̔4ňã
Ɓ̨̮
2.1.6. ⼀个类的构造⽅法的作⽤是什么? 若⼀个类没有声明构造⽅法，该程序能
正确执⾏吗? 为什么?
 
wE²@<Ȏ<ǫșĎķç̨(6ʁy̨Ȏīı/	į{ˁƱpä
	ǮŗÔųĲˁƱpą̈gl%K˙ȎˁƱpä̭RřɃ	ų̮̯
Java ˙ǮŗRųĲˁƱpä̯$£̯Ċÿ new <ǫf
ĥˡųĲ̯6%Ċbo9ıEˁƱpä̯T"%ǟǇ<ǫ
$£J˧İ̭ƊERųˁƱpą̮̈gl%¸É	ųˁƱp
ä̯ï!RųˁƱpäŹ7̭RřɃE̮̯(6ƖǢ%ǟǇ
<ǫ$£Ø˴ʙ̨
2.1.7. 构造⽅法有哪些特性？
 
1. Ż¢Ȏ®̨
27
JavaGuide

---

2. /	˩iƸ̯¬E void į{ˁƱ̜Ĳ̨
3. *@Ȏ<ǫ$]ʁy̯RėƊĘ
2.1.8. 在调⽤⼦类构造⽅法之前会先调⽤⽗类没有参数的构造⽅法,其⽬的是?
 
ƖǢ4Ȏ\șĎķç̨
2.1.9. 对象的相等与指向他们的引⽤相等,两者有什么不同?
 
<ǫ®z̯±òǗǗòĤɃ®z̨fȰE®z̯±ǳI%ŶāòǗ
9ÑɃ®z̨
2.2. ⾯向对象三⼤特征
 
2.2.1. 封装
 
ʪĢŶ<ǫɡƚmḙ̈Ķ¯̮ʘȯ<ǫòĂ̯̇ŽáĂ<ǫĊÿʹ
Ê<ǫòĂmę̈¬(6ĵʇ¦(6táÞʹÊpäɳĶ¯̨Ä%
ɱʻĒƊòĂʣÓmḙ̈Ķ¯̮̯¬(6é)ˎɭṶ̑pä̮
ɭġĒƊ̨glĶ¯táÞʹÊ̯%(ŢĵʇpäUáÞʹĘ̂¬gl
Ȏ/	ĵʇUáÞʹÊpä̯="Ȏ/	T"Ȝ̨Ägl/	ĒƊˎɭ
Ȗ̯="%RäɳɭĒ̞ġƽ̯ĒƊ/	Ȝ̭¡ZW+	.»Ipä
̯ODȱˈ4̨̮
public class Student {
    private int id;//id属性私有化
    private String name;//name属性私有化
    //获取id的⽅法
    public int getId() {
        return id;
    }
    //设置id的⽅法
    public void setId(int id) {
        this.id = id;
    }
    //获取name的⽅法
    public String getName() {
        return name;
    }
    //设置name的⽅法
    public void setName(String name) {
        this.name = name;
    }
}
28
JavaGuide

---

2.2.2. 继承
 
Ȏǣ<ǫ̯®ɟevď	ĲæǦM̨ˈg̯-{Y̧-şY̧-ɮ
Y̯ǦxY*ģ¯̭ŏĳ̧Yİz̨̮$̯n<ǫ+Ȝˆáģ¯ı!
I%¢Ɇ̨ˈg-{ĲY±ǳ̯-ş¯ŭ˪
#̱-ɮs±ǳ̨Ʒɒ
ıEǗȎȜȒ̆ǇǃȎȲȏ̯ȎȜ(6|ĲǼń
Ş̯(6EɲȎŞ̯¬ĈǠ¯9ƷɒɲǪ̑é)ıEƷɒ̯(6>ƙ9ǟǇ
Ȏ̯(6ĵjņŘ¸E̯Ǔɀ(ŜǷ¯̯ŎɢæǟǇȎ$ ̯ĵj%
?:ƌɨ̨
·Ʒɒg 
·Ʒɒg  3 MÅïã̰
MÅïã̰
1. 4Ȏƕ	ɲȎ<ǫ	Ķ¯;pä̭ĩ˧ʚ	Ķ¯;ʚ	pä̮̯¬ɲȎ
ʚ	Ķ¯;pä4ȎRäʹÊ̯Dƕ	
Dƕ	̨
2. 4Ȏ(6ƕ	KĶ¯;pä̯ī4Ȏ(6<ɲȎÇy˾Ƕ̨
3. 4Ȏ(6EKpƅWɲȎpą̭̈6Jʗ˖̨̮
2.2.3. 多态
 
ƚ̯ɐŚȜ̯´ƈ<ǫǚ	_ɡƚ̨ǚÀ´WɲȎȰEŶā4Ȏ
ˈ̨
ƚģM
ƚģM:
<ǫȎǣ;ȰEȎǣeǚ	Ʒɒ̭Ȏ̮/W̭ÿă̮·ṉ̌
<ǫȎǣ(¼̯ȰEȎǣ(¼̱
päǚ	ƚ¯̯Ķ¯ǚ	ƚ¯̱
ȰEȎǣ¼æ:7päƊEƉłȎpä̯ŢɕǓɀĭyùq
ȸ̱
ƚƊE“D4ȎǗ¬ɲȎǗ”pä̱
gl4Ȏ¸ŹɲȎpä̯B°ʁy4Ȏˠʊpä̯gl4Ȏ/	ˠʊɲ
Ȏpä̯ʁyɲȎpą̈
2.3. 修饰符
 
2.3.1. 在⼀个静态⽅法内调⽤⼀个⾮静态成员为什么是⾮法的?
 
ŨƐƚpä(6é)<ǫÇyƊE̯ČƐƚpäO̯ƊE»IŤƐƚ¼æ̯
(6ʹÊŤƐƚ¼æ@Ę̆
2.3.2. 静态⽅法和实例⽅法有何不同
 
1. áĂƊEƐƚpä$̯(6ıE"Ȏ.pä"pƅ̯(6ıE"<ǫ.pä
"pƅ̨fˈpäD	J_pƅ̨'̯ƊEƐƚpä(6RėǟǇ
<ǫ̨
2. ƐƚpäʹÊȎ@Ĕ$̯ḊŽʹÊƐƚ@Ḙ̆īƐƚ@Ĕ¼æ;Ɛƚp
ä̮̯f̇ŽʹÊˈ@Ĕ¼æ;ˈpä̱ˈpäȍRČǞġ̨
2.3.3. 常⻅关键字总结:static,ﬁnal,this,super
 
29
JavaGuide

---

ɝ§ɗwǪ~þ: https://snailclimb.gitee.io/javaguide/#/docs/java/basic/ﬁnal
,static,this,super
2.4. 接⼝和抽象类
 
2.4.1. 接⼝和抽象类的区别是什么？
 
1. ÿăpäǮŗ public̯	päÿă	W(Java 8 ?Ďÿăpä(
6	ǮŗW̮̯fǴǫȎ(6	ŤǴǫpą̈
2. ÿăȌ statiçﬁnal ¼æ̯	»I¼æ̯fǴǫȎȍ̨
3. Ȏ(6Wÿă̯¬DWǴǫǪ̑ÿăK(6é)
extends ·ʶŻ˾Ƕÿą̆
4. ÿăpäǮŗǧɽ́ public̯Ǵǫpä(6	 publiçprotected ; default 
¦ǧɽ̭́Ǵǫpät¸Ź6ıE private ·ʶŻǧɽ̨̬̮
5. ¶ƧŇȵ'̯Ǵǫ<ȎǴǫ̯_ȨȚƧŇ̯fÿă<yǴǫ̯
_yɍʋ̨
ƪŁ̰
1.  JDK8 ̯ÿă(6ȜƐƚpä̯(6ĊÿEÿăƊĘWȎ;
W(6ƊE̨gl$Whÿă̯ÿăȜ`Ǯŗpä̯
ȍŢɕ¸Ź̯ZŠ̨(ɝ§
issue:https://github.com/Snailclimb/JavaGuide/issues/146̨
2. jdk9 ÿăṫŽȜʚ	pä ̨
Ùð  jdk7~jdk9 Java ÿă˂Ƌ¼ķ̭®·ːǲ̮̰
1.  jdk 7 ńXÂě̯ÿăOD	ďæ¼æ;Ǵǫpą̈¦ÿăpäŢɕ
ŨĈǠWÿăȎW̨
2. jdk8 $£ÿă(6	Ǯŗpä;ƐƚpäŞ̨
3. Jdk 9 ÿăȰÃʚ	pä;ʚ	Ɛƚpą̈
2.5. 其它重要知识点
 
2.5.1. String StringBuffer 和 StringBuilder 的区别是什么? String 为什么是不可
变的?
 
Ƽē'̰String ȎıE ﬁnal ·ʶŻǧɽŻ́ĲțĨǗŻ́˨̯private
final char value[]̯6String <ǫ(¼̨
ɂǻ̭issue 675̮̰ Java 9 eJ̯String ȎWũE byte ĲțǗʦŻ́
˨ private final byte[] value;
f StringBuilder ¢ StringBuffer Ʒɒ AbstractStringBuilder Ȏ̯
AbstractStringBuilder ıEŻ́ĲțĨǗŻ́˨char[]value ¬/	E
final ·ʶŻǧɽ̯6h_<ǫ(¼̨
30
JavaGuide

---

StringBuilder ¢ StringBuffer ˁƱpäƊEɲȎˁƱpä
AbstractStringBuilder W̯8(6yƏːɇŘ̨
AbstractStringBuilder.java
ůǓµu¯
ůǓµu¯
String <ǫ(¼̯(6«Ħďæ̯ůǓµ
ųAbstractStringBuilder  StringBuilder ¢ StringBuffer ¨ǦɲȎ̯
Ȝ¦Ż́˨Ȓɳ̯g expandCapacity̧appenḑinserţindexOf
z¨Ǧpą̈StringBuffer <päŷ˛ńĻ<ƊEpäŷ˛̯6
ůǓµu̨StringBuilder ü/	<päÇyŷ˛̯6ŤůǓµu̨
¯
¯
na< String ȎǣÇyũ¼$£̯*@ String <ǫ̯ZJ­ŶʈŶā
 String <ǫ̨StringBuffer na< StringBuffer <ǫÇyɳ̯f
*@<ǫüũ¼<ǫȰĘ®Fɯ ıE StringBuilder ®±ıE
StringBuffer ȡ¤! 10%~15% Ȼɣ¯ĵŐ̯¬ûɎůǓµuÐȥ̨
<PĻıEÙð̰
<PĻıEÙð̰
1. ɳØæĲǼ: ƭE String
2. ēůǓɳŻ́˨˄ȹƲ ɳæĲǼ: ƭE StringBuilder
3. ůǓɳŻ́˨˄ȹƲ ɳæĲǼ: ƭE StringBuffer
2.5.2. Object 类的常⻅⽅法总结
 
Object Ȏģ̃Ȏ̯	ȎɲǪ̑Ğwĵʇ6  11 pä̰
abstract class AbstractStringBuilder implements Appendable, 
CharSequence {
    /**
     * The value is used for character storage.
     */
    char[] value;
    /**
     * The count is the number of characters used.
     */
    int count;
    AbstractStringBuilder(int capacity) {
        value = new char[capacity];
    }}
31
JavaGuide

---

2.5.3. == 与 equals(重要)
 
== : ĞE˦ȇh<ǫ9Ñ®z̨ī̯˦ȇh<ǫ<ǫ
(ȒĲǼȎǣ==±ǳƸ̯ȰEĲǼȎǣ==±ǳòǗ9Ñ)̨
equals() : ĞE˦ȇh<ǫɃ®z̨¬Ğɖ	h_ıEFɯ̰
Fɯ 1̰Ȏ/	ˠʊ equals() pą̈ȍé) equals() ±ǳĖȎh<ǫ$̯zĴ
é)“==”±ǳh<ǫ̨
Fɯ 2̰Ȏˠʊ equals() pą̈ɖ̯%ˠʊ equals() pä±ǳh<
public final native Class<?> getClass()//native⽅法，⽤于返回当前运⾏时对象
的Class对象，使⽤了final关键字修饰，故不允许⼦类重写。
public native int hashCode() //native⽅法，⽤于返回对象的哈希码，主要使⽤在哈
希表中，⽐如JDK中的HashMap。
public boolean equals(Object obj)//⽤于⽐较2个对象的内存地址是否相等，String
类对该⽅法进⾏了重写⽤户⽐较字符串的值是否相等。
protected native Object clone() throws 
CloneNotSupportedException//naitive⽅法，⽤于创建并返回当前对象的⼀份拷⻉。⼀
般情况下，对于任何对象 x，表达式 x.clone() != x 为true，x.clone().getClass() 
== x.getClass() 为true。Object本身没有实现Cloneable接⼝，所以不重写clone⽅法
并且进⾏调⽤的话会发⽣CloneNotSupportedException异常。
public String toString()//返回类的名字@实例的哈希码的16进制的字符串。建议
Object所有的⼦类都重写这个⽅法。
public final native void notify()//native⽅法，并且不能重写。唤醒⼀个在此对
象监视器上等待的线程(监视器相当于就是锁的概念)。如果有多个线程在等待只会任意唤醒⼀
个。
public final native void notifyAll()//native⽅法，并且不能重写。跟notify⼀
样，唯⼀的区别就是会唤醒在此对象监视器上等待的所有线程，⽽不是⼀个线程。
public final native void wait(long timeout) throws 
InterruptedException//native⽅法，并且不能重写。暂停线程的执⾏。注意：sleep⽅
法没有释放锁，⽽wait⽅法释放了锁 。timeout是等待时间。
public final void wait(long timeout, int nanos) throws 
InterruptedException//多了nanos参数，这个参数表示额外时间（以毫微秒为单位，范围
是 0-999999）。 所以超时的时间还需要加上nanos毫秒。
public final void wait() throws InterruptedException//跟之前的2个wait⽅
法⼀样，只不过该⽅法⼀直等待，没有超时时间这个概念
protected void finalize() throws Throwable { }//实例被垃圾回收器回收的时候
触发的操作
32
JavaGuide

---

ǫòĤɃ®ẕɓĞ%òĤ®z̯ȍ˩i true (ī̯ŗh<ǫ®z)̨
ȱˈ4̰
ȱˈ4̰
'{̰
'{̰
String  equals pät¸Ź)̯ object  equals pä±ǳ<ǫ
òǗ9Ñ̯f String  equals pä±ǳ<ǫƸ̨
¡ǟǇ String Ȏǣ<ǫ$̯ɸ̂kďæˣƏċ	/	vǗƸ;ǟ
ǇƸ®<ǫ̯gl	Ğ̑U¡ȰĘgl/	ďæˣ¸ǟǇ
 String <ǫ̨
2.5.4. hashCode 与 equals (重要)
 
Áƀ(Ê̰“¸Ź) hashcode ; equals "̯T"¸Ź equals $Ţɕ¸Ź
hashCode pä̲”
2.5.4.1. hashCode（）介绍
 
hashCode() E¤½¿ƂŘ̯ȔɚǏṞ̌ĞȤ˩i int ƛĲ̨
¿ƂŘEȸĖ<ǫ¿Ƃ´ʏȰíą̇hashCode() Ȝ JDK 
Object.java ̯ŉ1 Java ŊħȎĩɫ	 hashCode() ̜Ĳ̨
ɚǏ´ǗʦʶƸ<(key-value)̯ĞģM̰ǽǼ“ʶ”>ƙʤʏ7<ý
“Ƹ”̨»ŬEɚǏŘ̬̭(6>ƙċė<ǫ̮
2.5.4.2. 为什么要有 hashCode
 
public class test1 {
    public static void main(String[] args) {
        String a = new String("ab"); // a 为⼀个引⽤
        String b = new String("ab"); // b为另⼀个引⽤,对象的内容⼀样
        String aa = "ab"; // 放在常量池中
        String bb = "ab"; // 从常量池中查找
        if (aa == bb) // true
            System.out.println("aa==bb");
        if (a == b) // false，⾮同⼀对象
            System.out.println("a==b");
        if (a.equals(b)) // true
            System.out.println("aEQb");
        if (42 == 42.0) { // true
            System.out.println("true");
        }
    }
}
33
JavaGuide

---

%Ÿ6
%Ÿ6“HashSet għʤƏ¸ƶ
għʤƏ¸ƶ”ˈ4'{T"	
ˈ4'{T"	 hashCodḛ ¡<
ǫÃ HashSet $̯HashSet ŸŇŕ<ǫ hashcode Ƹ˦ȇ<ǫÃíȧ̯
$¢Ėíȧ»IvÃ<ǫ hashcode Ƹ±ǳ̯gl/	®́
hashcode̯HashSet ƫƧ<ǫ/	¸ƶ7W̨¬gl:W	® hashcode Ƹ<
ǫ̯$ƊE equals()päʤƏ hashcode ®z<ǫɃB®̨glhĻ®
̯HashSet L»Ãɳ@Ş̨glr̯¸ɚǏ»Iíą̭̇̀
 Java ʞ˜Œ̪Head ﬁrst java̫}©ę̮̌`%ȆØ equals a
Ĳ̯®ýĵjʁyƙß̨
é)%(67̰hashCode() E¤½¿ƂŘ
¤½¿ƂŘ̯ȔɚǏṞ̌ĞȤ
˩i int ƛĲ̨¿ƂŘE
¿ƂŘEȸĖ<ǫ¿Ƃ´ʏȰí
ą̇hashCode()ɚǏ´q	E̯»ĞFɯ /E
ɚǏ´q	E̯»ĞFɯ /ĘɚǏ´ hashCode() 
E¤½<ǫɚǏŘ̯ÇfȸĖ<ǫɚǏ´íą̇
2.5.4.3. hashCode（）与 equals（）的相关规定
 
1. glh<ǫ®z̯ȍ hashcode ®
2. h<ǫ®z,<h<ǫ3¥ƊE equals pä˩i true
3. h<ǫ	® hashcode Ƹ̯Ğ%®z
4. Č̯
Č̯equals pätˠʊ)̯ȍ
pätˠʊ)̯ȍ hashCode päŢɕtˠʊ
päŢɕtˠʊ
5. hashCode() Ǯŗy<ʆ<ǫƑ*ƝģƸ̨gl/	¸Ź
hashCode()̯ȍĖ class h<ǫRřgħ®z̭īıh<ǫŶā®
ĲǼ̮
ªÏːǲ̰Java hashCode() ; equals()ɓƟÊêĦȫ
2.5.5. Java 序列化中如果有些字段不想进⾏序列化，怎么办？
 
<ÇyɀǏķ¼æ̯ıE transient ·ʶŻǧɽ̨
transient ·ʶŻE̰˭Ȧˈ=¦EČ·ʶŻǧɽ¼æɀǏķ̱¡<ǫt
ƢɀǏķ$̯t transient ǧɽ¼æƸtĮōķ;˿ƶ̨transient Dǧɽ¼
æ̯ǧɽȎ;pą̈
2.5.6. 获取⽤键盘输⼊常⽤的两种⽅法
 
pä 1̰é) Scanner
pä 2̰é) Bu!eredReader
Scanner input = new Scanner(System.in);
String s  = input.nextLine();
input.close();
BufferedReader input = new BufferedReader(new 
InputStreamReader(System.in));
String s = input.readLine();
34
JavaGuide

---

3. Java 核⼼技术
 
3.1. 集合
 
3.1.1. Collections ⼯具类和 Arrays ⼯具类常⻅⽅法总结
 
ɝ§ɗwǪ~þ: https://gitee.com/SnailClimb/JavaGuide/blob/master/docs/j
ava/basic/Arrays,CollectionsCommonMethods.md
3.2. 异常
 
3.2.1. Java 异常类层次结构图
 
â̰https://simplesnippets.tech/exception-handling-in-java-part-1/
35
JavaGuide

![Java基础知识篇 第35页插图](../assets/images/Java基础知识篇_p35_1_774512e5.png)

![Java基础知识篇 第35页插图](../assets/images/Java基础知识篇_p35_2_1d31b914.png)

---

â̰https://chercher.tech/java-programming/exceptions-java
 Java ̯	ɺď	Ǧ˝Ÿ java.lang ĩ Throwable Ǫ̑
Throwablḛ 	h¸4Ȏ̰Exceptioṋɺď̮
̭ɺď̮ ; Error̭ɹ̮
̭ɹ̮ ̯©Ļ
Java ɺďğ«¸4Ȏ̯ŀĩɫæ4Ǫ̑
Error̭ɹ̮
̭ɹ̮:ǓɀRäğ«ɹ
ǓɀRäğ«ɹ̯´ƈĭyýEǓɀǳɬ¸Êę̂Ĳɹ
¢ņŘʭŹĻʁyɳR·̯f´ƈņŘĭy$ JVM̭Java ɸ̂k̮7WÊę̂ˈ
g̯Java ɸ̂kĭyɹ̭Virtual MachineError̮̯¡ JVM 	ƷŦʁyɳė
òǗƨɇ$̯­7W OutOfMemoryError̨¦ɺď:*$̯Java ɸ̂k̭JVM̮
ɖĈǠůǓĿĄ̇
¦ɹ´ƈƓ˶:*ɸ̂k̧ńĻ:*ɸ̂kÁâʁyýE$̯g Java ɸ̂
kĭyɹ̭Virtual MachineErroŗ̮ȎȜɹ̭NoClassDefFoundError̮z̨
¦ɹ(Ə̯Ğ%ýEǓɀɭġ;ğ«se á̯fȝǅĲǓɀ
ĭy$̇Ž7Wɡɯ̨<ƧŇõ«ýEǓɀ'̯īıȸ:*ɹ̯Ŕ
ýĖÁâ,ğ«ĞȰ2ɺďɡɯ̨ Java ̯ɹé) Error 4Ȏ˺Ƚ̨
Exceptioṋɺď̮
̭ɺď̮:Ǔɀ(6ğ«ɺď
Ǔɀ(6ğ«ɺď̨Exception Ȏ	¸4Ȏ
RuntimeException̨RuntimeException ɺďŨ Java ɸ̂kˊ
7̨NullPointerExceptioṋʹÊ¼æ/	ȰEŊħ<ǫ$̯ˊ7Ėɺ
ḑ̮̌ArithmeticExceptioṋŕȏĭŕɺď̯ƛĲȌ6 0 $̯ˊ7Ėɺď̮;
ArrayIndexOutOfBoundsException ̭ ǛÚÞɺď̨̮
Ł̰ɺď;ɹƲ¥̰ɺďtǓɀğ«̯ɹRäğ«̨
Ł̰ɺď;ɹƲ¥̰ɺďtǓɀğ«̯ɹRäğ«̨
3.2.2. Throwable 类常⽤⽅法
 
public string getMessage():˩iɺď:*$Ƽ˺Ƚ
public string toString():˩iɺď:*$ɝǨmë
public string getLocalizedMessage():˩iɺď<ǫ9ķmę̈ıE
Throwable 4Ȏˠʊpä̯(6*@9ķmę̈gl4Ȏ/	ˠʊĖp
ä̯ȍĖpä˩imë¢ getMessage（）˩iðl®
public void printStackTrace():ɭġƔɰ Throwable <ǫʪĢ
ɺďmë
3.2.3. try-catch-ﬁnally
 
try ǝ̰
ǝ̰ E̄¤ɺď̨»J(ÿʣń catch ǝ̯gl/	 catch ǝ̯ȍŢ
ɕĹ ﬁnally ǝ̨
catch ǝ̰
ǝ̰ Eğ« try ̄¤ɺď̨
ﬁnally ǝ̰
ǝ̰ RřɃ̄¤ńğ«ɺď̯ﬁnally ǝOƃĬtʁy̨¡ try
ǝń catch ǝư return ƃĬ$̯ﬁnally ƃĬǝ­pä˩ietʁy̨
6 
6  4 _ģ̃Fɯ ̯
_ģ̃Fɯ ̯ﬁnally ǝtʁy̰
ǝtʁy̰
1.  ﬁnally ƃĬǝ}y:*ɺď̨ »Iy̯ﬁnally ǝ+!ʁy
2. ņŘE System.exit(int)ʀ7Ǔɀ̨ exit Ôų̜Ĳ ̱ɓĖƃĬ
36
JavaGuide

---

ɺďƃĬeJ̯ﬁnally ʁy
3. ǓɀůǓˏ̨
4. ·ʨ CPŲ
 Ă3òĤ issue:https://github.com/Snailclimb/JavaGuide/issues/190̨
Ł̰
Ł̰ ¡ try ƃĬ; ﬁnally ƃĬ	 return ƃĬ$̯pä˩ie̯ﬁnally ƃĬ
òĤ­tʁy̯üȝ ﬁnally ƃĬ˩iƸ­ˠʊÝĎ˩iƸ̨g ̰
glƊE f(2)̯˩iƸ­ 0̯ ﬁnally ƃĬ˩iƸˠʊ try ƃĬǝ˩iƸ̨
3.2.4. 使⽤ try-with-resources 来代替try-catch-finally
 
̪E!ecitve Java̫{ȸŶ7̰
<Ţɕ·ʨƨɇ̯%ÙýĖƠŸıEtry-with-resourcesftry-
finally̨őeƑ*ņŘXƼƾ̯Xå̯̍Ƒ*ɺď<%X	Ętry-
with-resourcesƃĬL%XĤŅʭŹŢɕ·ʨƨɇņŘ̯ɓʒEtry-
finallyȍȬ\M̨
Java ȎȢInputStream̧OutputStream ̧Scanner ̧PrintWriterzƨɇ
ė%ƊEclose()päV]·ʨ̯ɖFɯ %é)try-catch-
finallyƃĬWėĘ̯g ̰
public class Test {
    public static int f(int value) {
        try {
            return value * value;
        } finally {
            if (value == 2) {
                return 0;
            }
        }
    }
}
        //读取⽂本⽂件的内容
        Scanner scanner = null;
        try {
            scanner = new Scanner(new File("D://read.txt"));
            while (scanner.hasNext()) {
                System.out.println(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            if (scanner != null) {
                scanner.close();
37
JavaGuide

---

ıEJava 7eJ try-with-resources ƃĬũƱņŘ:
¡Zƨɇė·ʨ$£̯ıE try-with-resources W2ŤďƼē̯gl
+Etry-catch-finally(Ô.Êę̂
é)ıE3İ3ʧ̯(6try-with-resourcesǝį{ƨɇ̰
3.3. 多线程
 
3.3.1. 简述线程、程序、进程的基本概念。以及他们之间关系是什么?
 
ůǓ
ůǓ¢ÇǓ®Ȣ̯¬ůǓ±ÇǓX-ʁyēį́ÇǓ»ʁy)Ǔ(6
Ƒ*ůŲ̌¢ÇǓȎůǓǦxǝòǗĒ;țňǤƨɇ̯
6ňǤƑ*ůǓ̯ńŀůǓeƆƮç$̯ɛɶ±ÇǓ-!̯°
gČ̯ůǓtȔŖæĳÇŲ̌
Ǔɀ
Ǔɀɫ	ŶȾ;ĲǼ~Ó̯tǗʦ̘Ȁń»IĲǼǗʦƧƪ̯'Ǔɀ
ƐƚņŘ̨
ÇǓ
ÇǓǓɀaʁy)Ǔ̯ňǤĭyǓɀȒēí̯ČÇǓ]ƚ̨ňǤĭy
ǓɀīÇǓ¶ǟǇ̯ĭyŲˏ)Ų̌Ƽē'̯ÇǓʁy
Ǔɀ̯ĞŇŕkŶȾÿ1ŶȾ9ʁy1̯$̯nÇǓ+˃	ǔ¦ňǤ
ƨɇg CPU $̯òǗĒ̯~Ó̯ʄÃʄ7ƧƪıEɌzz̨ƮĬr'̯¡Ǔɀ
ʁy$̯­tɳňǤÉÃòǗ̨ ůǓÇǓɁ3@X-ĭyēį́ůǓ;ÇǓ
5ȒŀÇǓƝǃ̯fŀůǓȍ̯ÇǓůǓǘ	
(®ɟĝȳ̨¶ǖǙß'̯ÇǓĶɳňǤʋ̥̯wƘ$ò̯(
6$ʁy6Ǔɀ̯fůǓȍǓɀòȬ$ʁy6ǓɀƘ̨
3.3.2. 线程有哪些基本状态?
 
Java ůǓĭy*žĪùŶ$ǡD(ğ  6 _ɡƚ»ɡƚ
̭âɇ̪Java ü:ʭǓɅȏ̫4.1.4 Ǫ̮̆
            }
        }
try (Scanner scanner = new Scanner(new File("test.txt"))) {
    while (scanner.hasNext()) {
        System.out.println(scanner.nextLine());
    }
} catch (FileNotFoundException fnfe) {
    fnfe.printStackTrace();
}
38
JavaGuide

---

ůǓ*žĪùüʿğǔɡƚfő1ņŘʁyɡƚeƆƮ̨
Java ůǓɡƚ¼̅g âƈ̭âɇ̪Java ü:ʭǓɅȏ̫4.1.4 Ŏ̮̰
Ũâ(67̰
ůǓǟǇeJĞ­ğ NEW̭Ǉ̮
̭Ǉ̮ ɡƚ̯ƊE start() päJ?Ďĭy̯ůǓ$
£ğ READY̭(ĭy̮
̭(ĭy̮ ɡƚ̨(ĭyɡƚůǓ¤! cpu $̭timeslice̮J
ğ RUNNING̭ĭy̮
̭ĭy̮ ɡƚ̨
ɳňǤʘȯ Java ɸ̂k̭JVM̮ READY ; RUNNING ɡƚ̯ĞD
RUNNABLE ɡƚ̭âɇ̰HowToDoInJava̰Java Thread Life Cycle and Thread
States̮̯6 Java ňǤɖ­hɡƚǤȔ RUNNABLḘĭy̮
̭ĭy̮ ɡƚ ̨
39
JavaGuide

![Java基础知识篇 第39页插图](../assets/images/Java基础知识篇_p39_1_478a5a97.png)

![Java基础知识篇 第39页插图](../assets/images/Java基础知识篇_p39_2_d2cb542e.png)

---

¡ůǓʁy wait()päeJ̯ůǓÇÃ WAITING̭zŝ̮
̭zŝ̮ɡƚ̨ÇÃzŝɡƚůǓ
ėǸű»IůǓébqƩ˩iĭyɡƚ̯f TIME_WAITING(×$zŝ
×$zŝ) ɡƚ
®¡zŝɡƚȒ̆|×$Ǟġ̯±gé) sleep（long millis）päń
wait（long millis）pä(6­ Java ůǓȧ TIMED WAITING ɡƚ̨¡×$$
ƇJ Java ůǓ­˩i RUNNABLE ɡƚ̨¡ůǓƊEŷpä$̯/	¤½
˛Fɯ ̯ůǓ­ÇÃ BLOCKEḒ˭˚̮
̭˭˚̮ ɡƚ̨ůǓʁy Runnable 
run()päeJ­ÇÃ TERMINATEḒĿȦ̮
̭ĿȦ̮ ɡƚ̨
3.4. ⽂件与 I\O 流
 
3.4.1. Java 中 IO 流分为⼏种?
 
ɈĚººā3̯(63ʄÃº;ʄ7º̱
ɈĚɳēöɁ3̯(6Ɂ3ŻŎº;Ż́º̱
ɈĚºǙÍɁ3ŎMº;ğ«º̨
Java Io ºǦ˽ǁ 40 Ȏ̯¦Ȏ,.ɞǾ̯¬Ȥ.	ɍȍ̯fȝʎČeǗ
ŤďǌəǑň̯ Java I0 º 40 Ȏ¶g  4 ǴǫȎȒȎʮ*7̨
InputStream/Reader: 	ʄÃºȒȎ̯ĻŻŎʄÃº̯JĻŻ́ʄÃ
º̨
OutputStream/Writer: 	ʄ7ºȒȎ̯ĻŻŎʄ7º̯JĻŻ́ʄ7
º̨
Ɉɳpƅ3Ȏðˁâ̰
40
JavaGuide

![Java基础知识篇 第40页插图](../assets/images/Java基础知识篇_p40_1_58fdb5b0.png)

---

Ɉɳ<ǫ3Ȏðˁâ̰
41
JavaGuide

![Java基础知识篇 第41页插图](../assets/images/Java基础知识篇_p41_1_08a43f00.jpeg)

---

3.4.1.1. 既然有了字节流,为什么还要有字符流?
 
ÊêŔḚ̂ŵ~ÓǲŹ+ ʍ:Ġÿô̯më5-ǗʦēöŻŎ̯
ŵ~ÓǲŹ+ ʍ:Ġÿô̯më5-ǗʦēöŻŎ̯
=T"
=T" I/O ºɳ3ŻŎºɳ;Ż́ºɳì̲
ºɳ3ŻŎºɳ;Ż́ºɳì̲
iȫ̰Ż́ºŨ Java ɸ̂k­ŻŎ÷Ʈ!̯Êê7)Ǔ+ŕŤď˳
$̯üȝ̯gl%bSʭŘȎǣ.ĤŅ7WǾŘÊę̂6̯ I/O ºƟˌĵʇ
ĊÿɳŻ́ÿă̯pŪ%Ą$<Ż́Çyºɳ̨glļǊ~Ó̧âzʾÀ
~ÓEŻŎº±ǳ̯gl˽ǁŻ́rıEŻ́º±ǳ̨
3.4.1.2. BIO,NIO,AIO 有什么区别?
 
BIO (Blocking I/O): ŷ˭˚ I/O Ȩƅ̯ĲǼǲ½ŹÃŢɕ˭˚ůǓò
zŝ»²@̨^]śÿĲģ¥j̭-ēk 1000̮Fɯ ̯_Ȩǣ±
ǳ̯(6LnśÿèŁK I/O üȝʭǓȨǣƼē̯E)Ƶ
ʡňǤ)Ȩ́ǞºzÊę̂ůǓˣZ˼ɜ̯(6˄ȹ¦ňǤ
ğ«śÿńÅĘ̨¬̯¡<àƒʱŧŋƒĳśÿ$£̯ĥǤ BIO Ȩ
ǣRs̨Č̯%ė_Xjƌ I/O ğ«Ȩǣý<Xjü:
æ̨
NIO (Non-blocking/New I/O): NIO _ŷŤ˭˚ I/O Ȩǣ̯ Java 1.4
ȰÃ NIO ̓ɪ̯<ý java.nio ĩ̯ĵʇ Channel , Selector̯Bu!er zǴ
ǫ̨NIO  N (6«Ħ Non-blocking̯ēȴ New̨ĞƎĮā˄ȹ
̯ȒéS I/O ɳpą̈ NIO ĵʇ¢ĥǤ BIO Ȩǣ Socket ;
ServerSocket ®<ý SocketChannel ; ServerSocketChannel h_
ǈÿŻéSW,h_éSƎĮ˭˚;Ť˭˚h_Ȩƅ̨˭˚ȨƅıEÄĥ
ǤƎĮ`̯±ǳƼē̯¬¯;(ű¯̱Ť˭˚Ȩƅ°¢e®
42
JavaGuide

![Java基础知识篇 第42页插图](../assets/images/Java基础知识篇_p42_1_2539ba1f.jpeg)

---

Ƣ̨<ǉɛȨ́ǉü:ýEǓɀ̯(6ıEŷ˭˚ I/O ĵŐ?:ƙɨ;X
ŜǷ¯̱<jɛȨ́jü:̭ ʍ̮ýE̯ýıE NIO Ť˭˚Ȩƅ?
:
AIO (Asynchronous I/O): AIO  NIO 2̨ Java 7 ȰÃ NIO ũÇě
NIO 2,ĞɺŷŤ˭˚ IO Ȩǣ̨ɺŷ IO ȒQÓ;iƊkġW̯
ýEɳeJĊÿ˩i̯ʺ˚=O̯¡JƔğ«²@̯ɳňǤéb®
ýůǓÇyJŦɳ̨AIO ɺŷ IO ˱Ź̯ȗZ NIO  ʍɳ̯ĵʇ
Ť˭˚pä̯¬ NIO  IO y+ŷ̨< NIO '̯%ĉǋů
Ǔ IO ɳƣƪ$̯!éb̯ÿ1ŨůǓyÇy IO ɳ̯IO ɳ
ŷ̨Əː ®·ƨǭ̯:WŮ' AIO ýE+.Ƅ̯̋
Netty eʯÁıE) AIO̯)cȶ̨
4. 参考
 
https://stackoverﬂow.com/questions/1906445/what-is-the-di!erence-b
etween-jdk-and-jre
https://www.educba.com/oracle-vs-openjdk/
https://stackoverﬂow.com/questions/22358071/di!erences-between-orac
le-jdk-and-openjdk?answertab=active#tab-top
5. 公众号
 
gl8$·ŁX~þ6ǁ3xƟǩr̯(6·Ł¨ɆĮ̇
̪Java Áǂź̫
Áǂź̫: Ũ~˥̛*èÁf*̪Java Áǂź̫V2.0 PDF ě¨
ɆİJƔiƶ "Java Áǂź
Áǂź" ī(Ɨĸî½̬
Java çǓęŢƪYſƨɇ
çǓęŢƪYſƨɇ: ¦ Java çǓęďEYſƨɇ¨ɆİJƔiƶ·ʶŻ “1” ī
(ƗĸRǈÎ¤½̨
43
JavaGuide

![Java基础知识篇 第43页插图](../assets/images/Java基础知识篇_p43_1_af7b1251.jpeg)