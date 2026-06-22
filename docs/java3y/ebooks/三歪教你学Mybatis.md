---
title: 三歪教你学Mybatis
source: Java3y/基础知识原创电子书/Mybatis 电子书/三歪教你学Mybatis.pdf
pages: 92
converted_at: 2026-06-22 22:29:35
---

# 三歪教你学Mybatis

ڹ᥺
Mybatisفᳪ
1. ՋԍฎMyBatis
2. ԅՋԍ౯ժᥝአMybatisҘ
3. Mybatisள᭛فᳪ
3.1 ੕ف୏ݎ۱
3.2 ٵ॓ၥᦶૡ֢
3.3 ڠୌmybatisᯈᗝ෈կ
3.4 ᖫٟૡٍᔄၥᦶฎވ឴ݐکᬳള
3.5 ڠୌਫ֛Өฉ੘ىᔮ෈կ
3.6 ᖫٟDAO
4. Mybatisૡ֢ၞᑕ
5. ਠ౮CRUD඙֢
5.1 ीے਍ኞ
5.2໑ഝIDັᧃහഝ
5.3 ັᧃಅํහഝ
5.4 ໑ഝidڢᴻ
5.5 ץද
5.6 ੜᕡᜓ
5.7Mybatisړᶭ
6. ۖாSQL
6.1 ۖாັᧃ
6.2 ۖாๅෛ
6.3 ۖாڢᴻ
6.4 ۖாൊف
7. فᳪ௛ᕮ
Mybatisᯈᗝמ௳
1. ฉ੘෈կ
1.1ܛ֖ᒧ
1.2 ԆᲫኞ౮ᒽኼ
1.2.1 UUID
1.3 ԆᲫᬬࢧ
1.4 resultMap
1.5 resultMap޾resultType܄ڦ
1.6 ֵአresultMap
1.7 resultType޾resultMapአဩ௛ᕮ
1.8Mybatisฉ੘෈կ॒ቘᇙྛਁᒧ
2. ᯈᗝ෈կ
2.1ڦݷ
2.2Mapperے᫹
2.3୊᬴ے᫹
2.4 ୊᬴ے᫹ၥᦶ
3. ᯈᗝፘى௛ᕮ
ىᘶฉ੘
1. Mybatis̓ग़ᤒᬳള̈́
1.1Ӟ੒Ӟ
1.1.1ᦡᦇᤒғ

---

1.1.2ਫ֛
1.1.3 ฉ੘෈կ
1.1.4 DAO੶
1.2 Ӟ੒ग़
1.2.1ᦡᦇහഝପᤒ
1.2.2ਫ֛
1.2.3ฉ੘෈կSQL᧍ݙ
1.2.4DAO
1.3ग़੒ग़
1.3.1 හഝପᤒ
1.3.2ਫ֛
1.3.3ฉ੘෈կ
1.3.4DAO
2. ىᘶฉ੘௛ᕮ
ᖨਂ+Mapperդቘ+ᭋݻૡᑕ
1. ڹ᥺
2. Mybatisᖨਂ
2.1 MybatisӞᕆᖨਂ
2.2 Mybatisԫᕆᖨਂ
2.3Mybatisԫᕆᖨਂᯈᗝ
2.4 ັᧃᕮຎฉ੘ጱpojoଧڜ۸
2.5 ᐬአԫᕆᖨਂ
2.6 ڬෛᖨਂ
2.7 ԧᥴMybatisᖨਂጱӞԶ݇හ
3.mybatis޾ehcacheᖨਂ໛ຝෆݳ
3.1ෆݳjar۱
3.2 ehcache.xmlᯈᗝמ௳
3.3ଫአ࣋วӨੴᴴ௔
3.3.1 ଫአ࣋ว
3.3.2ੴᴴ௔
4. Mapperդቘොୗ
4.1 Mapper୏ݎᥢ᝜
4.2Mapperդቘᬬࢧ꧊ᳯ᷌
5. Mybatisᥴ٬JDBCᖫᑕጱᳯ᷌
6.Mybatisᭋݻૡᑕ
6.1 ץදpom.xml෈կ
6.2generatorConﬁg.xmlᯈᗝ෈կ
6.3 ֵአൊկྍṈ
6.4๋ݸኞ౮դᎱ
7.๜ᒍ௛ᕮ
MybatisෆݳSpring
1. MybatisӨSpringෆݳ
1.1੕فjar۱
1.2 ڠୌᤒ
1.3 ڠୌਫ֛
1.4 ڠୌਫ֛Өᤒጱฉ੘෈կ
1.5 ڠୌMybatisฉ੘෈կᯈᗝሾह
1.6 ᯈᗝSpring໐ஞᬦᄁ࢏̓Ԟฎے᫹௛ᯈᗝ෈կ̈́
1.7 ᯈᗝහഝପמ௳̵Ԫۓ

---

1.8 ڠୌDao̵Service̵Action
1.9JSPᶭᶎၥᦶ
2. ௛ᕮ
Mybatisଉᥠᶎᦶ᷌
1. #{}޾${} ጱ܄ڦฎՋԍҘ
2.୮ਫ֛ᔄӾጱં௔ݷ޾ᤒӾጱਁྦྷݷӧӞ໏ ҅ெԍې Ҙ
3. ই֜឴ݐᛔۖኞ౮ጱ(Ԇ)Ძ꧊?
4. ࣁmapperӾই֜փ᭓ग़ӻ݇හ?
5. Mybatisۖாsqlฎ؉ՋԍጱҘ᮷ํߺԶۖாsqlҘᚆᓌᬿӞӥۖாsqlጱಗᤈܻቘӧҘ
6. MybatisጱXmlฉ੘෈կӾ҅ӧݶጱXmlฉ੘෈կ҅idฎވݢզ᯿॔Ҙ
7. ԅՋԍ᧔Mybatisฎ܎ᛔۖORMฉ੘ૡٍҘਙӨقᛔۖጱ܄ڦࣁߺ᯾Ҙ
8. ᭗ଉӞӻXmlฉ੘෈կ҅᮷տٟӞӻDaoളݗӨԏ੒ଫ҅᧗ᳯ҅ᬯӻDaoളݗጱૡ֢ܻቘฎՋԍҘDaoള
ݗ᯾ጱොဩ҅݇හӧݶ෸҅ොဩᚆ᯿᫹ހҘ
9. MybatisྲIBatisྲ᫾य़ጱپӻදᬰฎՋԍ
10. ളݗᕬਧํپᐿਫሿොୗ,ړڦฎெԍਫሿጱ?
11. Mybatisฎই֜ᬰᤈړᶭጱҘړᶭൊկጱܻቘฎՋԍҘ
12. ᓌᬿMybatisጱൊկᬩᤈܻቘ҅զ݊ই֜ᖫٟӞӻൊկ
13. Mybatisฎވඪ೮୊᬴ے᫹Ҙইຎඪ೮҅ਙጱਫሿܻቘฎՋԍҘ
14. Mybatis᮷ํߺԶExecutorಗᤈ࢏Ҙਙժԏᳵጱ܄ڦฎՋԍҘ
15. MyBatisӨHibernateํߺԶӧݶҘ
ڹ᥺
 
ᬯӻ෈໩ጱٖ਻ᕍಋ಑҅ইຎమᥝ፡ๅग़ጱଗᨵ෈ᒍ҅ىဳ౯ጱلռݩғJava3y̶ํๅग़ጱܻڠದ๞෈
ᒍ޾ଗᨵѺ
 
ፓڹዙᇰ॒ԭዙᇰๅෛPDFӾ҅ݝᥝฎJavaݸᒒጱᎣᦩ҅᮷տํѺཻᬨ๶౯لռݩ؛ๅѺஙמ൤
ᔱғJava3y
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺلռݩํ౯ጱᘶᔮොୗ

![三歪教你学Mybatis 第3页插图](../assets/images/三歪教你学Mybatis_p3_1_3c233a1a.jpeg)

---

Javaᔜᗦᚏࢶ
Java਍ԟ᪠ᕚ
୏ݎଉአૡٍ
ᔜᗦܻڠኪৼԡ
ࣁلռݩӥࢧ॔̿888̀ܨݢ឴ݐѺѺ
 
਍ԟӧᚆፖፓ҅᪙፳౯҅տᦏ֦Ԫ܎ۑ׭
 
෈໩꧋ᦜᵋ఺փඎ҅֕ӧᚆץදձٖ֜਻̶
 
ኪৼԡጱෆቘԞฎꂁӧ਻ฃ҅ইຎ֦ᥧ஑ํଆۗ҅మᥝ಑ᩝ֢ᘏ҅ᮎԍݢզ᭗ᬦᬯӻතྃᎱ಑ᩝ౯҅ᰂ
᷐ӧ᯿ᥝ҅ஞ఺๋᯿ᥝ̶Ԇᥝฎ౯ݢզ᭗ᬦᬯӻ಑ᩝఘ٭๶ᶼᦇय़ਹ੒ᬯ๜ኪৼԡጱᦧհ҅ࢃࢃ
 
 
 
Mybatisفᳪ
 
1. ՋԍฎMyBatis
 
MyBatis ๜ฎapacheጱӞӻ୏რᶱፓiBatis, 2010ଙᬯӻᶱፓኧapache software foundation ᬢ
ᑏکԧgoogle code҅ଚӬදݷԅMyBatis̶ฎӞӻचԭJavaጱ೮ԋ੶໛ຝ
2. ԅՋԍ౯ժᥝአMybatisҘ
 
෫ᦞฎMybatis̵Hibernate᮷ฎORMጱӞᐿਫሿ໛ຝ҅᮷ฎ੒JDBCጱӞᐿ੗ᤰѺ

![三歪教你学Mybatis 第4页插图](../assets/images/三歪教你学Mybatis_p4_1_08125413.png)

![三歪教你学Mybatis 第4页插图](../assets/images/三歪教你学Mybatis_p4_2_a7b96e96.jpeg)

![三歪教你学Mybatis 第4页插图](../assets/images/三歪教你学Mybatis_p4_3_46627a5a.jpeg)

---

کፓڹԅྊ҅౯ժ૪ᕪࣁ೮ԋ੶Ӿ਍ԧپᐿದ๞ԧ...
Hibernate
jdbc
SpringDAO
ᮎ౯ժԅࠨᬮᥝ਍MybatisޫҘҘҘሿࣁMybatisࣁӱٖय़ᤈٌ᭲҅ᮎԅࠨ՜ᚆᮎԍᅉޫҘҘ
HibernateฎӞӻྲ᫾ᘌ෯ጱ໛ຝ҅አᬦ՜ጱݶ਍᮷Ꭳ᭲҅ݝᥝ֦տአ҅አ᩸๶܈ړᛥ๐...ࠨsqlդᎱ᮷
ӧአٟ...֕ฎޫ҅ਙԞฎํጱᗌᅩғғ॒ቘ॔๥ӱۓ෸҅ᅎၚଶ૧, ॔๥ጱHQLᵙٟᵙቘᥴֺ҅ইग़ᤒ
ັᧃጱHQL᧍ݙ
ᘒJDBCஉ਻ฃቘᥴ҅੪ᮎԍپӻࢴਧጱྍṈ҅੪ฎ୏ݎ᩸๶ॡἋᅸԧ҅ࢩԅՋԍ᮷ᥝ౯ժᛔ૩ଗ..
 
౯ժݢզᦊԅ҅Mybatis੪ฎjdbc޾HibernateԏᳵጱӞӻଘᤍᅩ...ླᒌሿࣁӱኴ᮷ฎአᬯӻ໛ຝ҅౯
ժԞӧᚆӧ਍ޚѺ
3. Mybatisள᭛فᳪ
 
ٌਫ౯ժ૪ᕪ਍ᬦԧHibernateԧ҅੒ԭMybatisفᳪٌਫ੪ᶋଉᔄ֒ጱ̶ࢩྌ੪உᓌܔ੪ᚆഩൎच๜ጱ
୏ݎԧ...
3.1 ੕ف୏ݎ۱
 
ๅෛғইຎአMavenጱݶ਍҅ᬯ᯾୚فmavenׁᩢ੪অԧ
੕فMybatis୏ݎ۱
mybatis-3.1.1.jar
commons-logging-1.1.1.jar
log4j-1.2.16.jar
cglib-2.2.2.jar

![三歪教你学Mybatis 第5页插图](../assets/images/三歪教你学Mybatis_p5_1_ce09a6f1.jpeg)

---

asm-3.3.1.jar
੕فmysql/oracle୏ݎ۱
mysql-connector-java-5.1.7-bin.jar
Oracle 11g 11.2.0.1.0 JDBC_ojdbc6.jar
3.2 ٵ॓ၥᦶૡ֢
 
ڠୌӞୟᤒ
ڠୌਫ֛ғ
create table students(
  id  int(5) primary key,
  name varchar(10),
  sal double(8,2)
);
/**
 * Created by ozc on 2017/7/21.
 */
public class Student {
    private Integer id;
    private String name;
    private Double sal;
    public Student() {
    }
    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Double getSal() {
        return sal;

---

3.3 ڠୌmybatisᯈᗝ෈կ
 
ڠୌmybatisጱᯈᗝ෈կ҅ᯈᗝහഝପጱמ௳....හഝପ౯ժݢզᯈᗝग़ӻ҅֕ฎἕᦊጱݝᚆአӞӻ...
    }
    public void setSal(Double sal) {
        this.sal = sal;
    }
}
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
  
  
  <!-- ے᫹ᔄ᪠ஆӥጱં௔෈կ -->
  <properties resource="db.properties"/>
  <!-- ᦡᗝӞӻἕᦊጱᬳളሾहמ௳ -->
  <environments default="mysql_developer">
    <!-- ᬳളሾहמ௳҅ݐӞӻձ఺ࠔӞጱݷਁ -->
    <environment id="mysql_developer">
      <!-- mybatisֵአjdbcԪۓᓕቘොୗ -->
      <transactionManager type="jdbc"/>
      <!-- mybatisֵአᬳള࿰ොୗ๶឴ݐᬳള -->
      <dataSource type="pooled">
        <!-- ᯈᗝӨහഝପԻ԰ጱ4ӻ஠ᥝં௔ -->
        <property name="driver" value="${mysql.driver}"/>
        <property name="url" value="${mysql.url}"/>
        <property name="username" value="${mysql.username}"/>
        <property name="password" value="${mysql.password}"/>
      </dataSource>
    </environment>
    
    
    <!-- ᬳളሾहמ௳҅ݐӞӻձ఺ࠔӞጱݷਁ -->
    <environment id="oracle_developer">
      <!-- mybatisֵአjdbcԪۓᓕቘොୗ -->
      <transactionManager type="jdbc"/>
      <!-- mybatisֵአᬳള࿰ොୗ๶឴ݐᬳള -->
      <dataSource type="pooled">
        <!-- ᯈᗝӨහഝପԻ԰ጱ4ӻ஠ᥝં௔ -->
        <property name="driver" value="${oracle.driver}"/>
        <property name="url" value="${oracle.url}"/>
        <property name="username" value="${oracle.username}"/>

---

3.4 ᖫٟૡٍᔄၥᦶฎވ឴ݐکᬳള
 
ֵአMybatisጱAPI๶ڠୌӞӻૡٍᔄ҅᭗ᬦmybatisᯈᗝ෈կӨහഝପጱמ௳҅஑کConnection੒᨝
        <property name="password" value="${oracle.password}"/>
      </dataSource>
    </environment>
  </environments>
  
  
</configuration>
package cn.itcast.javaee.mybatis.util;
import java.io.IOException;
import java.io.Reader;
import java.sql.Connection;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
/**
 * ૡٍᔄ
 * @author AdminTC
 */
public class MybatisUtil {
  private static ThreadLocal<SqlSession> threadLocal = new 
ThreadLocal<SqlSession>();
  private static SqlSessionFactory sqlSessionFactory;
  /**
   * ے᫹֖ԭsrc/mybatis.xmlᯈᗝ෈կ
   */
  static{
    try {
      Reader reader = Resources.getResourceAsReader("mybatis.xml");
      sqlSessionFactory = new SqlSessionFactoryBuilder().build(reader);
    } catch (IOException e) {
      e.printStackTrace();
      throw new RuntimeException(e);
    }
  }
  /**
   * ᐬྊक़ኴ᭗ᬦnewොဩڠୌ 
   */
  private MybatisUtil(){}
  /**
   * ឴ݐSqlSession
   */

---

3.5 ڠୌਫ֛Өฉ੘ىᔮ෈կ
 
ᯈᗝਫ֛Өᤒጱฉ੘ىᔮ
  public static SqlSession getSqlSession(){
    //՗୮ڹᕚᑕӾ឴ݐSqlSession੒᨝
    SqlSession sqlSession = threadLocal.get();
    //ইຎSqlSession੒᨝ԅᑮ
    if(sqlSession == null){
      //ࣁSqlSessionFactoryᶋᑮጱఘ٭ӥ҅឴ݐSqlSession੒᨝
      sqlSession = sqlSessionFactory.openSession();
      //ਖ਼SqlSession੒᨝Ө୮ڹᕚᑕᕬਧࣁӞ᩸
      threadLocal.set(sqlSession);
    }
    //ᬬࢧSqlSession੒᨝
    return sqlSession;
  }
  /**
   * ىᳮSqlSessionӨ୮ڹᕚᑕړ୏
   */
  public static void closeSqlSession(){
    //՗୮ڹᕚᑕӾ឴ݐSqlSession੒᨝
    SqlSession sqlSession = threadLocal.get();
    //ইຎSqlSession੒᨝ᶋᑮ
    if(sqlSession != null){
      //ىᳮSqlSession੒᨝
      sqlSession.close();
      //ړ୏୮ڹᕚᑕӨSqlSession੒᨝ጱىᔮ҅ፓጱฎᦏGCੱ෱ࢧත
      threadLocal.remove();
    }
  } 
  /**
   * ၥᦶ
   */
  public static void main(String[] args) {
    Connection conn = MybatisUtil.getSqlSession().getConnection();
    System.out.println(conn!=null?"ᬳള౮ۑ":"ᬳള०ᨳ");
  }
}
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!-- namespaceં௔ฎݷᑍᑮᳵ҅஠ᶳࠔӞ -->
<mapper namespace="cn.javaee.mybatis.Student">  
  
  <!-- resultMapຽᓋ:ฉ੘ਫ֛Өᤒ

---

ሿࣁ౯ժ૪ᕪํԧMybatisጱᯈᗝ෈կ޾ᤒӨਫ֛ԏڹጱฉ੘෈կԧ҅ࢩྌ౯ժᥝਖ਼ᯈᗝ෈կ޾ฉ੘෈
կىᘶ᩸๶
ࣁၥᦶᔄӤ҅౯ժฎݢզ឴ݐ஑کᬳളጱ
3.6 ᖫٟDAO
 
     typeં௔ғᤒᐏਫ֛ق᪠ஆݷ
     idં௔ғԅਫ֛Өᤒጱฉ੘ݐӞӻձ఺ጱࠔӞጱݷਁ
  -->
  <resultMap type="student" id="studentMap">
    <!-- idຽᓋ:ฉ੘ԆᲫં௔
       resultຽᓋғฉ੘ᶋԆᲫં௔
         propertyં௔:ਫ֛ጱં௔ݷ
         columnં௔ғᤒጱਁྦྷݷ  
    -->             
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="sal" column="sal"/>
  </resultMap>
</mapper>
  <mappers>
    <mapper resource="StudentMapper.xml"/>
  </mappers>
public class StudentDao {
    public void add(Student student) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        sqlSession.insert();

![三歪教你学Mybatis 第10页插图](../assets/images/三歪教你学Mybatis_p10_1_dccc1ccc.png)

---

کሿࣁԅྊ҅౯ժਫ֛Өᤒጱฉ੘෈կՐՐฉ੘ԧਫ֛ં௔Өᤒጱਁྦྷጱىᔮ...
౯ժࣁHibernateӾইຎమᥝൊفහഝՋԍጱ҅ݝᥝ᧣አsave()ොဩ੪ᤈԧ̶Hibernateฎᛔۖ۸੽ᠰധ
ԧහഝପጱ૧୑҅ᘒ౯ժMybatisฎᵱᥝᛔ૩ಋۖᖫٟSQLդᎱጱ...
ᮎԍSQLդᎱฎٟࣁߺ᯾ጱޫҘҘҘกดࣈ҅౯ժ֢ԅӞӻ໛ຝ҅ӧݢᚆࣁᑕଧӾٟSQL҅౯ժฎࣁਫ
֛Өᤒጱฉ੘෈կӾٟጱѺ
Mybatisਫ֛Өᤒጱฉ੘෈կӾ൉׀ԧinsertຽᓋ̓SQLդᎱᇆྦྷ̈́׀౯ժֵአ
ࣁᑕଧӾ᧣አฉ੘෈կጱSQLդᎱᇆྦྷ
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        Student student = new Student(1, "zhongfucheng", 10000D);
        studentDao.add(student);
    }
}
  //ࣁJDBCӾ౯ժ᭗ଉֵአ?ݩ֢ԅܛ֖ᒧ҅ᘒࣁMybatisӾ҅౯ժฎֵአ#{}֢ԅܛ֖ᒧ
  //parameterType౯ժ೰ਧԧփف݇හጱᔄࣳ
  //#{}ਫᴬӤ੪ฎ᧣አԧStudentં௔ጱgetොဩ
  <insert id="add" parameterType="Student">
    INSERT INTO ZHONGFUCHENG.STUDENTS (ID, NAME, SAL) VALUES (#{id},#{name},#
{sal});
  </insert>
    public void add(Student student) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            sqlSession.insert("StudentID.add", student);
            sqlSession.commit();
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();

---

꧊஑ဳ఺ጱฎғMybatisӾጱԪۓฎἕᦊ୏ސጱ҅ࢩྌ౯ժࣁਠ౮඙֢զݸ҅ᵱᥝ౯ժಋ݄ۖ൉ԻԪ
ۓѺ
4. Mybatisૡ֢ၞᑕ
 
᭗ᬦReader੒᨝᧛ݐMybatisฉ੘෈կ
᭗ᬦSqlSessionFactoryBuilder੒᨝ڠୌSqlSessionFactory੒᨝
឴ݐ୮ڹᕚᑕጱSQLSession
Ԫۓἕᦊ୏ސ
᭗ᬦSQLSession᧛ݐฉ੘෈կӾጱ඙֢ᖫݩ҅՗ᘒ᧛ݐSQL᧍ݙ
൉ԻԪۓ
ىᳮᩒრ
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
        }
    }

![三歪教你学Mybatis 第12页插图](../assets/images/三歪教你学Mybatis_p12_1_9ef93dcf.jpeg)

![三歪教你学Mybatis 第12页插图](../assets/images/三歪教你学Mybatis_p12_2_3c233a1a.jpeg)

---

5. ਠ౮CRUD඙֢
 
౯ժࣁӤᶎӾ૪ᕪᓌܔᎣ᭲ԧMybatisฎெԍֵአጱզ݊ૡ֢ၞᑕԧ҅ᬯེ౯ժֵአMybatis๶ਠ౮
CRUDጱ඙ེ֢҅ٚ૥ࢴMybatisጱ୏ݎྍṈզ݊ӞԶᕡᜓ
۱Өᔄԏᳵጱᕮ຅
5.1 ीے਍ኞ
 
ᯈᗝ෈կ
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
  <!-- ے᫹ᔄ᪠ஆӥጱં௔෈կ -->
  <properties resource="db.properties"/>
  <!-- ᦡᗝӞӻἕᦊጱᬳളሾहמ௳ -->
  <environments default="mysql_developer">
    <!-- ᬳളሾहמ௳҅ݐӞӻձ఺ࠔӞጱݷਁ -->
    <environment id="mysql_developer">
      <!-- mybatisֵአjdbcԪۓᓕቘොୗ -->
      <transactionManager type="jdbc"/>
      <!-- mybatisֵአᬳള࿰ොୗ๶឴ݐᬳള -->
      <dataSource type="pooled">
        <!-- ᯈᗝӨහഝପԻ԰ጱ4ӻ஠ᥝં௔ -->
        <property name="driver" value="${mysql.driver}"/>
        <property name="url" value="${mysql.url}"/>
        <property name="username" value="${mysql.username}"/>
        <property name="password" value="${mysql.password}"/>
      </dataSource>
    </environment>
    
    <!-- ᬳളሾहמ௳҅ݐӞӻձ఺ࠔӞጱݷਁ -->
    <environment id="oracle_developer">
      <!-- mybatisֵአjdbcԪۓᓕቘොୗ -->

![三歪教你学Mybatis 第13页插图](../assets/images/三歪教你学Mybatis_p13_1_13432531.png)

---

ฉ੘෈կ
ൊفහഝ
      <transactionManager type="jdbc"/>
      <!-- mybatisֵአᬳള࿰ොୗ๶឴ݐᬳള -->
      <dataSource type="pooled">
        <!-- ᯈᗝӨහഝପԻ԰ጱ4ӻ஠ᥝં௔ -->
        <property name="driver" value="${oracle.driver}"/>
        <property name="url" value="${oracle.url}"/>
        <property name="username" value="${oracle.username}"/>
        <property name="password" value="${oracle.password}"/>
      </dataSource>
    </environment>
  </environments>
  <mappers>
    <mapper resource="zhongfucheng/StudentMapper.xml"/>
  </mappers>
</configuration>
<!-- namespaceં௔ฎݷᑍᑮᳵ҅஠ᶳࠔӞ -->
<mapper namespace="StudentID">
  
  <!-- resultMapຽᓋ:ฉ੘ਫ֛Өᤒ 
     typeં௔ғᤒᐏਫ֛ق᪠ஆݷ
     idં௔ғԅਫ֛Өᤒጱฉ੘ݐӞӻձ఺ጱࠔӞጱݷਁ
  -->
  <resultMap type="zhongfucheng.Student" id="studentMap">
    <!-- idຽᓋ:ฉ੘ԆᲫં௔
       resultຽᓋғฉ੘ᶋԆᲫં௔
         propertyં௔:ਫ֛ጱં௔ݷ
         columnં௔ғᤒጱਁྦྷݷ
    -->
    <id property="id" column="id"/>
    <result property="name" column="name"/>
    <result property="sal" column="sal"/>
  </resultMap>
  <insert id="add" parameterType="zhongfucheng.Student">
    INSERT INTO ZHONGFUCHENG.STUDENTS (ID, NAME, SAL) VALUES (#{id},#{name},#
{sal});
  </insert>
</mapper>

---

5.2໑ഝIDັᧃහഝ
 
ीےselectຽᓋ
public class StudentDao {
    public void add(Student student) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            sqlSession.insert("StudentID.add", student);
            sqlSession.commit();
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        Student student = new Student(3, "zhong3", 10000D);
        studentDao.add(student);
    }
}

![三歪教你学Mybatis 第15页插图](../assets/images/三歪教你学Mybatis_p15_1_1072664e.png)

---

ັᧃڊ๶ጱᕮຎฎӞӻStudent੒᨝҅౯ժ᧣አSelectOneොဩ
5.3 ັᧃಅํහഝ
 
  <!--
    ັᧃ໑ഝid
    resultMapᬯӻં௔դᤒฎᬬࢧ꧊ᔄࣳ҅ᬬࢧ꧊ጱᔄࣳฎStudent҅੪ฎӤᶎਫ֛ᔄࣳ
  -->
  <select id="findById" parameterType="int" resultMap="studentMap">
    SELECT * FROM STUDENTS WHERE id = #{id};
  </select>
    public Student findById(int id) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            return sqlSession.selectOne("StudentID.findById",id);
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        Student student = studentDao.findById(1);
        System.out.println(student.getName());
    }

![三歪教你学Mybatis 第16页插图](../assets/images/三歪教你学Mybatis_p16_1_6488c76d.png)

---

౯ժັᧃڊ๶ጱᕮຎӧܔܔݝํӞӻ੒᨝ԧ҅ࢩྌ౯ժֵአጱฎSelectListᬯӻොဩ
5.4 ໑ഝidڢᴻ
 
᧣አdeleteොဩڢᴻ
  <!--
    ັᧃಅํහഝ
    ᬬࢧ꧊ᔄࣳᦖ᭲ቘฎList<Student>ጱ҅֕౯ժݝᥝٟᵞݳӾጱᔄࣳ੪ᤈԧ
  -->
  <select id="findAll" resultMap="studentMap">
    SELECT * FROM STUDENTS;
  </select>
  public List<Student> findAll() throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            return sqlSession.selectList("StudentID.findAll");
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        List<Student> students = studentDao.findAll();
        System.out.println(students.size());
    }
  <!--໑ഝidڢᴻ-->
  <delete id="delete" parameterType="int">
    DELETE FROM STUDENTS WHERE id=#{id};
  </delete>
    public void delete(int id ) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL

---

5.5 ץද
 
ັᧃڊ੒ଫጱ੒᨝҅੒ٌᬰᤈץද
            sqlSession.delete("StudentID.delete", id);
            sqlSession.commit();
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        studentDao.delete(1);
    }
  <!--ๅෛ-->
  <update id="update" parameterType="zhongfucheng.Student">
    update students set name=#{name},sal=#{sal} where id=#{id};
  </update>
    public void update(Student student ) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            sqlSession.update("StudentID.update", student);
            sqlSession.commit();
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;

![三歪教你学Mybatis 第18页插图](../assets/images/三歪教你学Mybatis_p18_1_50bcbc5d.png)

---

5.6 ੜᕡᜓ
 
5.7Mybatisړᶭ
 
ړᶭฎӞӻᶋଉਫአጱದ๞ᅩ҅౯ժԞ๶਍ԟӞӥֵአMybatisฎெԍړᶭጱ...
౯ժጱړᶭฎᵱᥝग़ӻ݇හጱ҅ଚӧฎ؟౯ժԏڹጱֺৼӾݝํӞӻ݇හ̶୮ᵱᥝളතग़ӻ݇හጱ෸
ײ҅౯ժֵአMapᵞݳ๶ᤰ᫹Ѻ
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        Student student = studentDao.findById(2);
        student.setName("fucheng");
        student.setSal(2000D);
        studentDao.update(student);
    }
  <!-- 
    ဳ఺ғᬯӻinsert/update/deleteຽᓋݝฎӞӻཛྷ຃҅ࣁ؉඙֢෸ٌ҅ਫฎզSQL᧍ݙԅ໐ஞጱ
         ܨࣁ؉ी/ڢ/෸҅insert/update/deleteຽᓋݢ᭗አ҅
         ֕؉ັᧃ෸ݝᚆአselectຽᓋ
         ౯ժ൉׶Ջԍ඙֢੪አՋԍຽᓋ
  --> 
    public List<Student>  pagination(int start ,int end) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL

![三歪教你学Mybatis 第19页插图](../assets/images/三歪教你学Mybatis_p19_1_6f794592.png)

---

ᮎԍࣁਫ֛Өᤒฉ੘෈կӾ҅౯ժളතጱ݇හ੪ฎmapᵞݳ
6. ۖாSQL
 
            /**
             * ኧԭ౯ժጱ݇හ᩻ᬦԧӷӻ҅ᘒොဩӾݝํӞӻObject݇හතᵞ
             * ࢩྌ౯ժֵአMapᵞݳ๶ᤰ᫹౯ժጱ݇හ
             */
            Map<String, Object> map = new HashMap();
            map.put("start", start);
            map.put("end", end);
            return sqlSession.selectList("StudentID.pagination", map);
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        List<Student> students = studentDao.pagination(0, 3);
        for (Student student : students) {
            System.out.println(student.getId());
        }
    }
  <!--ړᶭັᧃ-->
  <select id="pagination" parameterType="map" resultMap="studentMap">
    /*໑ഝkeyᛔۖತک੒ଫMapᵞݳጱvalue*/
    select * from students limit #{start},#{end};
  </select>

![三歪教你学Mybatis 第20页插图](../assets/images/三歪教你学Mybatis_p20_1_23d5b382.png)

---

֜ԅۖாSQLҘҘࢧᶶӞӥ౯ժԏڹٟጱSSHᶱፓӾ҅ํग़๵կັᧃጱఘ٭҅ইӥࢶ
౯ժ୮෸ڟ୏ত؉ጱ෸ײ҅ฎᵱᥝࣁControllerӾڣෙSQLฎވ૪ᕪํ๵կԧ҅ࢩԅSQL᧍ݙᵱᥝ೪ള᩸
๶....ᬯ໏ଗጱᦾ҅੪ᶋଉ਻ฃڊᲙጱ̶
ইӥጱդᎱ҅ইຎํग़ӻ๵կጱᦾ҅ᮎԍ೪ള᩸๶உ਻ฃڊᲙѺ
ݸ๶҅౯ժᥧ஑ᬯ໏ӧঅ҅ԭฎ੪ӫᳪٟԧӞӻັᧃۗಋᔄғ
  public String listUI() {
        //ັᧃ᧍ݙ
        String hql = "FROM Info i ";
        List<Object> objectList  = new ArrayList<>();
        //໑ഝinfoฎވԅnull๶ڣෙฎވฎ๵կັᧃ̶ইຎinfoԅᑮ҅ᮎԍฎັᧃಅํ̶
        if (info != null) {
            if (StringUtils.isNotBlank(info.getTitle())) {
                hql += "where i.title like ?";
                objectList.add("%" + info.getTitle() + "%");
            }
        }
        infoList = infoServiceImpl.findObjects(hql,objectList);
        ActionContext.getContext().getContextMap().put("infoTypeMap", 
Info.INFO_TYPE_MAP);
        return "listUI";
    }
package zhongfucheng.core.utils;
import java.util.ArrayList;
import java.util.List;

![三歪教你学Mybatis 第21页插图](../assets/images/三歪教你学Mybatis_p21_1_55dd2e34.jpeg)

---

/**
 * Created by ozc on 2017/6/7.
 */
public class QueryHelper {
    private String fromClause = "";
    private String whereClause = "";
    private String orderbyClause = "";
    private List<Object> objectList;
    public static String ORDER_BY_ASC = "asc";
    public static String ORDER_BY_DESC = "desc";
    //FROMৼݙݝڊሿӞེ
    /**
     * ຅ୌFROMਁݙ҅ଚᦡᗝັᧃߺୟᤒ
     * @param aClass አಁమᥝ඙֢ጱᔄࣳ
     * @param alias  ڦݷ
     */
    public QueryHelper(Class aClass, String alias) {
        fromClause = "  FROM " + aClass.getSimpleName() + "  " + alias;
    }
    //WHEREਁݙݢզႲےग़ӻ๵կ҅֕WHEREىᲫਁݝڊሿӞེ
    /**
     * ຅ୌWHEREਁݙ
     * @param condition
     * @param objects
     * @return
     */
    public QueryHelper addCondition(String condition, Object... objects) {
        //ইຎ૪ᕪํਁᒧԧ҅ᮎԍ੪᧔ก૪ᕪํWHEREىᲫਁԧ
        if (whereClause.length() > 0) {
            whereClause += " AND  " + condition;
        } else {
            whereClause += " WHERE" + condition;
        }
        //ࣁႲےັᧃ๵կጱ෸ײ҅?੒ଫጱັᧃ๵կ꧊
        if (objects == null) {
            objectList = new ArrayList<>();
        }
        for (Object object : objects) {
            objectList.add(object);
        }
        return this;

---

ᬯ໏Ӟ๶ጱᦾ҅౯ժ੪ӧአᛔ૩ಋۖ೪ളԧ҅ᕳ౯ժጱັᧃۗಋᔄ݄೪ള੪অԧ̶
ᘒইຎ౯ժֵአMybatisጱᦾ҅੪ݢզع݄ັᧃۗಋᔄԧ̶ࢩԅMybatisٖ᮱੪ํۖாSQLጱۑᚆ̓ۖ
ாSQL੪ฎᛔۖ೪ളSQL᧍ݙ̈́Ѻ
6.1 ۖாັᧃ
 
    }
    /**
     *
     * @param property ᥝഭଧጱં௔
     * @param order ฎ܋ଧᬮฎᴳଧ
     * @return
     */
    public QueryHelper orderBy(String property, String order) {
        //ইຎ૪ᕪํਁᒧԧ҅ᮎԍ੪᧔ก૪ᕪํORDERىᲫਁԧ
        if (orderbyClause.length() > 0) {
            orderbyClause += " ,  " + property +"   " + order;
        } else {
            orderbyClause += "  ORDER BY " + property+"   " + order;
        }
        return this;
    }
    /**
     * ᬬࢧHQL᧍ݙ
     */
    public String returnHQL() {
        return fromClause + whereClause + orderbyClause;
    }
    /**
     * ஑ک݇හڜᤒ
     * @return
     */
    public List<Object> getObjectList() {
        return objectList;
    }
}
  <!--ग़๵կັᧃ̓ۖாSQL̈́-->
  <!--տᛔۖᕟݳ౮ӞӻྋଉጱWHEREਁݙ-->
  <!--name꧊տ՗mapӾ੔ತ-->
  <select id="findByCondition" resultMap="studentMap" parameterType="map">
    select * from students

---

ັᧃڊ๶ੜԭ9000ࣘጱՈ
    <where>
      <if test="name!=null">
        and name=#{name}
      </if>
      <if test="sal!=null">
        and sal < #{sal}
      </if>
    </where>
  </select>
   public List<Student> findByCondition(String name,Double sal) throws 
Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            /**
             * ኧԭ౯ժጱ݇හ᩻ᬦԧӷӻ҅ᘒොဩӾݝํӞӻObject݇හතᵞ
             * ࢩྌ౯ժݢզֵአMapᵞݳ๶ᤰ᫹౯ժጱ݇හ
             */
            Map<String, Object> map = new HashMap();
            map.put("name", name);
            map.put("sal", sal);
            return sqlSession.selectList("StudentID.findByCondition", map);
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        List<Student> students = studentDao.findByCondition(null,9000D);
        for (Student student : students) {
            System.out.println(student.getId() + "---" + student.getName() + 
"----" + student.getSal());
        }
    }

---

6.2 ۖாๅෛ
 
ᕳڊӣӻๅෛጱਁྦྷ
  <!--ۖாๅෛ-->
  <!--ӧᥝ஫ԧ᭖ݩ-->
  <update id="updateByConditions" parameterType="map">
    update students
    <set>
      <if test="name!=null">
         name = #{name},
      </if>
      <if test="sal!=null">
         sal = #{sal},
      </if>
    </set>
    where id = #{id}
  </update>

![三歪教你学Mybatis 第25页插图](../assets/images/三歪教你学Mybatis_p25_1_62668bf3.png)

![三歪教你学Mybatis 第25页插图](../assets/images/三歪教你学Mybatis_p25_2_2b79aaca.jpeg)

---

public void updateByConditions(int id,String name,Double sal) throws 
Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            /**
             * ኧԭ౯ժጱ݇හ᩻ᬦԧӷӻ҅ᘒොဩӾݝํӞӻObject݇හතᵞ
             * ࢩྌ౯ժֵአMapᵞݳ๶ᤰ᫹౯ժጱ݇හ
             */
            Map<String, Object> map = new HashMap();
            map.put("id", id);
            map.put("name", name);
            map.put("sal", sal);
            sqlSession.update("StudentID.updateByConditions", map);
            sqlSession.commit();
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        studentDao.updateByConditions(2,"haha",500D);
    }

---

6.3 ۖாڢᴻ
 
զڹ౯ժֵአJDBCԞঅ҅HibernateԞঅ҅మᥝಢᰁڢᴻጱ෸ײ҅௛ฎֵአጱฎ஗ሾڢᴻ̶ᘒ౯ժሿࣁ
ֵአጱฎMybatis҅SQL᧍ݙฎᛔ૩ٟጱ̶ಅզ౯ժݢզٟӥইӥጱSQL๶ᬰᤈڢᴻ
ᘒ౯ժጱMybatis݈ඪ೮ۖாSQL,ಅզڢᴻ᩸๶੪ᶋଉො׎ԧѺ
delete from students where id in (?,?,?,?);
  <delete id="deleteByConditions" parameterType="int">
    <!-- foreachአԭᬽդහᕟزᔰ
       openᤒᐏ୏তᒧݩ

![三歪教你学Mybatis 第27页插图](../assets/images/三歪教你学Mybatis_p27_1_9dbd32d1.png)

![三歪教你学Mybatis 第27页插图](../assets/images/三歪教你学Mybatis_p27_2_3714c726.jpeg)

---

ڢᴻᖫݩԅ2҅3҅4ጱᦕ୯
       closeᤒᐏᕮ๳ᒧݳ
       separatorᤒᐏزᔰᳵጱړᵍᒧ
       itemᤒᐏᬽդጱහᕟ҅ં௔꧊ݢզձ఺҅֕൉׶Өොဩጱහᕟݷፘݶ
       #{ids}ᤒᐏහᕟӾጱྯӻزᔰ꧊
     -->
    delete from students where id in
     <foreach collection="array" open="(" close=")" separator="," item="ids">
       #{ids}
     </foreach>
  </delete>
    public void deleteByConditions(int... ids) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            /**
             * ኧԭ౯ժጱ݇හ᩻ᬦԧӷӻ҅ᘒොဩӾݝํӞӻObject݇හතᵞ
             * ࢩྌ౯ժֵአMapᵞݳ๶ᤰ᫹౯ժጱ݇හ
             */
            sqlSession.delete("StudentID.deleteByConditions", ids);
            sqlSession.commit();
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        studentDao.deleteByConditions(2,3,4);
    }

---

6.4 ۖாൊف
 
 
౯ժᥝమۖாൊفጱᦾ҅੪ྲٌ՜ጱDML᧍ݙᑖங॔๥Ӟᅩ҅ࢩԅਙํӷ᮱ړฎӧᏟਧጱ҅ଘଉጱSQL
᧍ݙฎᬯ໏ጱғ
 
SQLդᎱࣘฎӧᚆ؟ԏڹᮎ໏ଆ౯ժᛔ݄ۖᴻग़֟ጱ᭖ݩጱ҅ࢩྌ౯ժᵱᥝֵአtrimຽᓋ๶ᛔ૩ಋ݄ۖ
ᴻ...
ᖫٟinsertSQL᧍ݙጱ෸ײ҅ӧᥝ஫ԧٟ()ೡݩ̶
insert into student(id,name,sal) values(?,?,?)

![三歪教你学Mybatis 第29页插图](../assets/images/三歪教你学Mybatis_p29_1_7d3f80ba.jpeg)

![三歪教你学Mybatis 第29页插图](../assets/images/三歪教你学Mybatis_p29_2_80ad8c90.png)

---

ၥᦶӣӻӧݶٖ਻ጱහഝ
    <!--SQLᇆྦྷἕᦊฎӧଆ౯ժᛔۖኞ౮ݳᭇጱSQL҅ࢩྌᵱᥝ౯ժᛔ૩ಋۖᴻ݄᭖ݩ-->
    <sql id="key">
        <trim suffixOverrides=",">
            <if test="id!=null">
                id,
            </if>
            <if test="id!=null">
                name,
            </if>
            <if test="id!=null">
                sal,
            </if>
        </trim>
    </sql>
    <sql id="value">
        <trim suffixOverrides=",">
            <if test="id!=null">
                #{id},
            </if>
            <if test="id!=null">
                #{name},
            </if>
            <if test="id!=null">
                #{sal},
            </if>
        </trim>
    </sql>
    <!--ۖாൊف-->
    <insert id="insertByConditions" parameterType="zhongfucheng.Student">
  
    insert into students (<include refid="key"/>) values
        (<include refid="value"/>)
  </insert>
    public void insertByConditions(Student student) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            sqlSession.insert("StudentID.insertByConditions", student);

---

7. فᳪ௛ᕮ
 
Mybatisጱٵ॓ૡ֢ӨHibernate૧ӧग़҅᮷ᵱᥝӞӻ௛ᯈᗝ෈կ̵Ӟӻฉ੘෈կ̶
MybatisጱSQLSessionૡٍᔄֵአThreadLocal๶੒ᕚᑕӾጱSession๶ᬰᤈᓕቘ̶
MybatisጱԪۓἕᦊฎ୏ސጱ҅ᵱᥝ౯ժಋ݄ۖ൉ԻԪۓ̶
MybatisጱSQL᧍ݙฎᵱᥝಋٟጱ҅ࣁᑕଧӾ᭗ᬦฉ੘෈կጱ޸ݷᑮᳵ.sql᧍ݙጱid๶ᬰᤈ᧣አ!
ࣁMybatisӾ҅ीڢදັ᮷ฎMybatisᵱᥝ౯ժᛔ૩ٟSQL᧍ݙጱ҅ᆐݸࣁᑕଧӾ᧣አܨݢԧ̶SQL
ኧԭฎ౯ժᛔ૩ٟጱ҅ԭฎ੪ፘ੒HibernateᅎၚӞԶ̶
ইຎᵱᥝփفग़ӻ݇හጱᦾ҅ᮎԍ౯ժӞᛱࣁฉ੘෈կӾአMap๶ളත̶
            sqlSession.commit();
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        studentDao.insertByConditions(new Student(55, null, null));//name޾sal
ԅᑮ
        studentDao.insertByConditions(new Student(66, "haxi", null));//salԅᑮ
        studentDao.insertByConditions(new Student(77, null, 3999d));//nameԅᑮ
    }

![三歪教你学Mybatis 第31页插图](../assets/images/三歪教你学Mybatis_p31_1_65ea3002.png)

---

ኧԭ౯ժࣁ୏ݎӾտᕪଉአک๵կັᧃ҅ࣁԏڹ҅౯ժฎֵአັᧃۗಋ๶ଆ౯ժਠ౮੒SQLጱ೪ള
ጱ̶ᘒMybatisጱᦾ҅౯ժฎᛔ૩ಋٟSQLդᎱጱ̶
MybatisԞඪ೮ӞԶڣෙຽᓋ҅ԭฎ౯ժ੪ݢզ᭗ᬦᬯԶຽᓋ๶ਠ౮ۖாCRUDጱ඙֢ԧ̶
꧊஑ဳ఺ጱฎ҅౯ժጱsqlᇆྦྷդᎱฎᵱᥝ౯ժᛔ૩ಋ݄ۖړۆ҅ݩጱ̶
 
 
Mybatisᯈᗝמ௳
 
 
1. ฉ੘෈կ
 
ࣁmapper.xml෈կӾᯈᗝஉग़ጱsql᧍ݙ҅ಗᤈྯӻsql᧍ݙ෸҅੗ᤰԅMappedStatement੒᨝҅
mapper.xmlզstatementԅܔ֖ᓕቘsql᧍ݙ
Statementጱਫᴬ֖ᗝ੪ᒵԭnamespace+StatementId
1.1ܛ֖ᒧ

![三歪教你学Mybatis 第32页插图](../assets/images/三歪教你学Mybatis_p32_1_54b944c6.png)

![三歪教你学Mybatis 第32页插图](../assets/images/三歪教你学Mybatis_p32_2_3c233a1a.jpeg)

---

ࣁMybatisӾ҅ํӷᐿܛ֖ᒧ
#{} ᥴຉփ᭓ᬰ๶ጱ݇හහഝ
${} ੒փ᭓ᬰ๶ጱ݇හܻ໏೪ളࣁSQLӾ
1.2 ԆᲫኞ౮ᒽኼ
 
ইຎ౯ժࣁHibernateӾ҅୮౯ժൊفහഝጱ෸ײ҅౯ժฎݢզᭌೠฎUUIDᒽኼጱ...
ᮎԍࣁMybatisฎெԍ؉ጱޫҘҘ
1.2.1 UUID
 
1.3 ԆᲫᬬࢧ
 
ইຎ౯ժӞᛱൊفහഝጱᦾ҅ইຎ౯ժమᥝᎣ᭲ڟڟൊفጱහഝጱԆᲫฎग़੝҅౯ժݢզ᭗ᬦզӥጱො
ୗ๶឴ݐ
ᵱ࿢ғuser੒᨝ൊفکහഝପݸ҅ෛᦕ୯ጱԆᲫᥝ᭗ᬦuser੒᨝ᬬࢧ҅᭗ᬦuser឴ݐԆᲫ꧊̶
ᥴ٬௏᪠ғ᭗ᬦLAST_INSERT_ID()឴ݐڟൊفᦕ୯ጱᛔीԆᲫ꧊҅ࣁinsert᧍ݙಗᤈݸ҅ಗᤈselect 
LAST_INSERT_ID()੪ݢզ឴ݐᛔीԆᲫ̶
mysql:
oracle:ғضັᧃଧڜ஑کԆᲫ҅ਖ਼ԆᲫᦡᗝکuser੒᨝Ӿ҅ਖ਼user੒᨝ൊفහഝପ̶
  <!-- mysqlጱuuidኞ౮ԆᲫ -->
  <insert id="insertUser" parameterType="cn.mybatis.po.User">
    <selectKey keyProperty="id" order="BEFORE" resultType="string">
      select uuid()
    </selectKey>
    
    INSERT INTO USER(id,username,birthday,sex,address) VALUES(#{id},#
{username},#{birthday},#{sex},#{address})
  </insert> 
  <insert id="insertUser" parameterType="cn.mybatis.po.User">
    <selectKey keyProperty="id" order="AFTER" resultType="int">
      select LAST_INSERT_ID()
    </selectKey>
    INSERT INTO USER(username,birthday,sex,address) VALUES(#{username},#
{birthday},#{sex},#{address})
  </insert>

---

Ԟݢզࣁselect ຽᓋӥٟզӥጱં௔ғ
 
1.4 resultMap
 
ํጱ෸ײ҅౯ժ፡ڦጱฉ੘෈կ҅ݢᚆ፡ӧکզӥᬯԍӞྦྷդᎱғ
ࢩԅ҅ইຎ౯ժጱහഝᤒጱਁྦྷ޾JavaBeanጱં௔ݷᑍฎፘݶ෸҅౯ժ੪ӧአӤᶎᮎྦྷդᎱԧ̶
Mybatisտᛔۖଆ౯ժ಩ᬬࢧጱᕮຎᬰᤈ੗ᤰ౮JavaBean
ᮎ୮౯ժහഝᤒጱਁྦྷ޾JavaBeanጱં௔ݷᑍӧฎፘݶ෸҅౯ժ੪ᵱᥝֵአresultMap҅Ԟ੪ฎӤᶎ
ᮎྦྷդᎱ
୮ᆐԧ҅ࣁྋଉఘ٭ӥڜݷ޾JavaBeanጱં௔ݷӞᛱ᮷ฎӧݶጱ҅ࢩྌᬮฎᵱᥝresultMapጱ̶
1.5 resultMap޾resultType܄ڦ
 
  <!-- oracle
  ࣁಗᤈinsertԏڹಗᤈselect ଧڜ.nextval() from dualݐڊଧڜ๋य़꧊҅ਖ਼꧊ᦡᗝکuser੒
᨝ ጱidં௔
   -->
  <insert id="insertUser" parameterType="cn.mybatis.po.User">
    <selectKey keyProperty="id" order="BEFORE" resultType="int">
      select ଧڜ.nextval() from dual
    </selectKey>
    
    INSERT INTO USER(id,username,birthday,sex,address) VALUES( ଧڜ.nextval(),#
{username},#{birthday},#{sex},#{address})
  </insert> 
< select useGeneratedKeys="true" keyProperty="id"  keyColumn="id" />
  <resultMap id="userListResultMap" type="user" >
    <!-- ڜݷ
    id_,username_,birthday_
    idғᥝฉ੘ᕮຎᵞጱࠔ Ӟຽᦩ ҅ᑍԅԆᲫ
    columnғᕮຎᵞጱڜݷ
    propertyғtype೰ਧጱߺӻં௔Ӿ
     -->
     <id column="id_" property="id"/>
     <!-- result੪ฎฦ᭗ڜጱฉ੘ᯈᗝ -->
     <result column="username_" property="username"/>
     <result column="birthday_" property="birthday"/>
  
  </resultMap>

---

resultType ғ೰ਧᬌڊᕮຎጱᔄࣳҁpojo̵ᓌܔᔄ̵ࣳhashmap..҂҅ਖ਼sqlັᧃᕮຎฉ੘ԅjava੒᨝ 
̶
ֵአresultTypeဳ఺ғsqlັᧃጱڜݷᥝ޾resultType೰ਧpojoጱં௔ݷፘݶ҅೰ਧፘݶ ં௔ොݢ
ฉ੘౮ۑ҅ইຎsqlັᧃጱڜݷᥝ޾resultType೰ਧpojoጱં௔ݷق᮱ӧፘݶ҅listӾ෫ဩڠୌpojo
੒᨝ጱ̶
resultMapғਖ਼sqlັᧃᕮຎฉ੘ԅjava੒᨝̶
ইຎsqlັᧃڜݷ޾๋ᕣᥝฉ੘ጱpojoጱં௔ݷӧӞᛘֵ҅አresultMapਖ਼ڜݷ޾pojoጱં௔ݷ؉
Ӟӻ੒ଫىᔮ ҁڜݷ޾ં௔ݷฉ੘ᯈᗝ҂
1.6 ֵአresultMap
 
1.7 resultType޾resultMapአဩ௛ᕮ
 
resultTypeғ
֢አғਖ਼ັᧃᕮຎೲᆙsqlڜݷpojoં௔ݷӞᛘ௔ฉ੘کpojoӾ̶
࣋ݳғଉᥠӞԶกᕡᦕ୯ጱ઀ᐏ҅ਖ਼ىᘶັᧃמ௳ق᮱઀ᐏࣁᶭᶎ෸҅ྌ෸ݢፗളֵአresultType
ਖ਼ྯӞ๵ᦕ୯ฉ੘کpojoӾ҅ࣁڹᒒᶭᶎ᭭ܲlistҁlistӾฎpojo҂ܨݢ̶
resultMapғ
ֵአassociation޾collectionਠ౮Ӟ੒Ӟ޾Ӟ੒ग़ṛᕆฉ੘̶
  <resultMap id="userListResultMap" type="user" >
    <!-- ڜݷ
    id_,username_,birthday_
    idғᥝฉ੘ᕮຎᵞጱࠔ Ӟຽᦩ ҅ᑍԅԆᲫ
    columnғᕮຎᵞጱڜݷ
    propertyғtype೰ਧጱߺӻં௔Ӿ
     -->
     <id column="id_" property="id"/>
     <!-- result੪ฎฦ᭗ڜጱฉ੘ᯈᗝ -->
     <result column="username_" property="username"/>
     <result column="birthday_" property="birthday"/>
  
  </resultMap>

![三歪教你学Mybatis 第35页插图](../assets/images/三歪教你学Mybatis_p35_1_b19ac389.png)

![三歪教你学Mybatis 第35页插图](../assets/images/三歪教你学Mybatis_p35_2_abbb0647.png)

---

associationғ
֢አғਖ਼ىᘶັᧃמ௳ฉ੘کӞӻpojoᔄӾ̶
࣋ݳғԅԧො׎឴ݐىᘶמ௳ݢզֵአassociationਖ਼ىᘶᦈܔฉ੘ԅpojo҅ྲইғັᧃᦈܔ݊ى
ᘶአಁמ௳̶
collectionғ
֢አғਖ਼ىᘶັᧃמ௳ฉ੘کӞӻlistᵞݳӾ̶
࣋ݳғԅԧො׎឴ݐىᘶמ௳ݢզֵአcollectionਖ਼ىᘶמ௳ฉ੘کlistᵞݳӾ҅ྲইғັᧃአಁ๦
ᴴ᝜ࢱཛྷࣘ޾ۑᚆ҅ݢֵአcollectionਖ਼ཛྷࣘ޾ۑᚆڜᤒฉ੘کlistӾ̶
Collectionࣁڹᶎঅ؟ଚဌํአᬦ҅ӥᶎ੪፡Ӟӥਙጱአဩғ
OrderӨOrderDetailsىᔮ
package cn.mybatis.po;
import java.io.Serializable;
import java.util.Date;
import java.util.List;
public class Orders implements Serializable {
    private Integer id;
    private Integer userId;
    private String number;
    private Date createtime;
    private String note;
    
    //ىᘶአಁמ௳
    private User user;
    
    //ᦈܔกᕡ
    private List<Orderdetail> orderdetails;
   
    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public Integer getUserId() {
        return userId;

---

}
    public void setUserId(Integer userId) {
        this.userId = userId;
    }
    public String getNumber() {
        return number;
    }
    public void setNumber(String number) {
        this.number = number == null ? null : number.trim();
    }
    public Date getCreatetime() {
        return createtime;
    }
    public void setCreatetime(Date createtime) {
        this.createtime = createtime;
    }
    public String getNote() {
        return note;
    }
    public void setNote(String note) {
        this.note = note == null ? null : note.trim();
    }
  public User getUser() {
    return user;
  }
  public void setUser(User user) {
    this.user = user;
  }
  public List<Orderdetail> getOrderdetails() {
    return orderdetails;
  }
  public void setOrderdetails(List<Orderdetail> orderdetails) {
    this.orderdetails = orderdetails;
  } 
    
}

---

SQL᧍ݙ
resultMap
ӞᛱࣈֵአresultMapտग़Ӟᅩ̶
1.8Mybatisฉ੘෈կ॒ቘᇙྛਁᒧ
 
ᒫӞᐿොဩғ
አԧ᫨Ԏਁᒧ಩>޾<๊ഘധ੪OKԧ
   <!-- Ӟ੒ग़ັᧃֵአreusltMapਠ౮
  ັᧃᦈܔىᘶັᧃᦈܔกᕡ
   -->
   <select id="findOrderAndOrderDetails" resultMap="orderAndOrderDetails" >
      SELECT 
    orders.*,
    user.username,
    user.sex ,
    orderdetail.id orderdetail_id,
    orderdetail.items_num,
    orderdetail.items_id
  FROM
    orders,
    USER,
    orderdetail
  WHERE orders.user_id = user.id  AND orders.id = orderdetail.orders_id
   </select>
  <!-- Ӟ੒ग़҅ັᧃᦈܔ݊ᦈܔกᕡ -->
  <resultMap type="orders" id="orderAndOrderDetails" 
extends="ordersUserResultMap">
    <!-- ฉ੘ᦈܔמ௳҅޾አಁמ௳҅ᬯ᯾ֵአᖀಥordersUserResultMap -->
    
    <!-- ฉ੘ᦈܔกᕡמ௳ 
    propertyғᥝਖ਼ىᘶמ௳ฉ੘کordersጱߺӻં௔Ӿ
    ofTypeғᵞݳӾpojoጱᔄࣳ
    -->
    <collection property="orderdetails" ofType="cn.mybatis.po.Orderdetail">
      <!-- idғىᘶמ௳ᦈܔกᕡጱࠔ Ӟຽᦩ
      propertyғOrderdetailጱં௔ݷ
        -->
      <id column="orderdetail_id" property="id"/>
      <result column="items_num" property="itemsNum"/>
      <result column="items_id" property="itemsId"/>
    </collection>
  
  </resultMap>

---

ᒫԫᐿොဩғ
<![CDATA[ ]]>
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
2. ᯈᗝ෈կ
 
2.1ڦݷ
 
typeAliasesڦݷғ

![三歪教你学Mybatis 第39页插图](../assets/images/三歪教你学Mybatis_p39_1_2a13ce9e.jpeg)

![三歪教你学Mybatis 第39页插图](../assets/images/三歪教你学Mybatis_p39_2_3c233a1a.jpeg)

---

ᛔਧԎڦݷғ
2.2Mapperے᫹
 
  <!-- ਧԎ ڦݷ -->
  <typeAliases>
    <!--
    ܔӻڦݷጱਧԎ
    aliasғڦݷ҅typeғڦݷฉ੘ጱᔄࣳ  -->
    <!-- <typeAlias type="cn.mybatis.po.User" alias="user"/> -->
    <!-- ಢᰁڦݷਧԎ
    ೰ਧ۱᪠ஆ҅ᛔۖಚൈ۱ӥᬟጱpojo҅ਧԎڦݷ҅ڦݷἕᦊԅᔄݷҁḒਁྮੜٟ౲य़ٟ҂
     -->
    <package name="cn.mybatis.po"/>
    
  </typeAliases>
  <mappers>

![三歪教你学Mybatis 第40页插图](../assets/images/三歪教你学Mybatis_p40_1_18a8cff1.png)

---

2.3୊᬴ے᫹
 
ࣁᬰᤈහഝັᧃ෸҅ԅԧ൉ṛහഝପັᧃ௔ᚆ҅ੱᰁֵአܔᤒັᧃ҅ࢩԅܔᤒັᧃྲग़ᤒىᘶັᧃ᭛ଶ
ᥝள̶
ইຎັᧃܔᤒ੪ݢզჿ᪃ᵱ࿢҅Ӟ୏তضັᧃܔᤒ҅୮ᵱᥝىᘶמ௳෸҅ٚىᘶັᧃ҅୮ᵱᥝىᘶמ௳
ٚັᧃᬯӻݞ୊᬴ے᫹̶
ࣁMybatisӾ୊᬴ے᫹੪ฎࣁresultMapӾᯈᗝٍ֛ጱ୊᬴ے᫹..
ࣁMybatisጱ෈կӾᯈᗝقੴ୊᬴ے᫹
2.4 ୊᬴ے᫹ၥᦶ
 
    <!-- ᭗ᬦresource୚አmapperጱฉ੘෈կ -->
    <mapper resource="sqlmap/User.xml" />
    <!-- <mapper resource="mapper/UserMapper.xml" /> -->
    <!-- ᭗ᬦclass୚አmapperളݗ 
    classғᯈᗝmapperളݗقᴴਧݷ
    ᥝ࿢ғᵱᥝmapper.xml޾mapper.javaݶݷଚӬࣁӞӻፓ୯ Ӿ
    -->
    <!-- <mapper class="cn.mybatis.mapper.UserMapper"/> -->
    <!-- ಢᰁmapperᯈᗝ 
    ᭗ᬦpackageᬰᤈᛔۖಚൈ۱ӥᬟጱmapperളݗ҅
    ᥝ࿢ғᵱᥝmapper.xml޾mapper.javaݶݷଚӬࣁӞӻፓ୯ Ӿ
    
    -->
    <package name="cn.mybatis.mapper"/>
  </mappers>
  <!-- قੴᯈᗝ݇හ -->
  <settings>
    <!-- ୊᬴ے᫹௛୏ى -->
    <setting name="lazyLoadingEnabled" value="true" />  
    <!-- ᦡᗝೲᵱے᫹ -->
    <setting name="aggressiveLazyLoading" value="false" />
  </settings>

![三歪教你学Mybatis 第41页插图](../assets/images/三歪教你学Mybatis_p41_1_15d91f3c.png)

---

୮ᵱᥝአಁ෸᧣አ OrdersᔄӾጱgetUser()ොဩಗᤈ୊᬴ے᫹ ҅ݻහഝପݎڊsql̶
ኧԭฎ੒Userᬰᤈ୊᬴ے᫹҅ᮎԍ౯ժݝᥝັᧃOrdersፘىጱמ௳ܨݢԧ
ֵአresultMap๶ᯈᗝ୊᬴ے᫹
   <!-- Ӟ੒Ӟັᧃ୊᬴ے᫹
   ୏তݝັᧃᦈܔ҅੒አಁמ௳ᬰᤈ୊᬴ے᫹ 
    -->
   <select id="findOrderUserListLazyLoading" 
resultMap="orderCustomLazyLoading">
     SELECT 
      orders.*
    FROM
      orders
   </select>
  <!-- Ӟ੒Ӟັᧃ୊᬴ے᫹ ጱᯈᗝ -->
  <resultMap type="orders" id="orderCustomLazyLoading">
    <!-- ਠ౮ԧᦈܔמ௳ጱฉ੘ᯈᗝ -->
    <!-- idғᦈܔىᘶአಁັᧃጱࠔ Ӟ ຽᦩ -->
    <id column="id" property="id" />
    <result column="user_id" property="userId" />
    <result column="number" property="number" />
    <result column="createtime" property="createtime" />
    <result column="note" property="note" />
    <!--
    ᯈᗝአಁמ௳ጱ୊᬴ے᫹
      selectғ୊᬴ے᫹ಗᤈጱsqlಅࣁጱstatementጱid҅ইຎӧࣁݶӞӻnamespaceᵱᥝے
namespace
      sqlғ໑ഝአಁidັᧃአಁמ௳̓column੪ฎ݇හ̈́
      columnғىᘶັᧃጱڜ
      property:ਖ਼ىᘶັᧃጱአಁמ௳ᦡᗝکOrdersጱߺӻં௔ -->
    <!--୮ᵱᥝuserහഝጱ෸ײ҅ਙ੪տ಩columnಅ೰ਧጱuser_idփ᭓ᬦ݄ᕳ
cn.mybatis.mapper.UserMapper.findUserById֢ԅ݇හ๶ັᧃහഝ-->
    <association property="user"
      select="cn.mybatis.mapper.UserMapper.findUserById" column="user_id">
</association>
  </resultMap>

---

3. ᯈᗝፘى௛ᕮ
 
ࣁᑕଧӾ᧣አጱSQL᧍ݙฎኧฉ੘෈կጱ޸եᑮᳵ+sqlᇆྦྷጱidಅᕟ౮ጱ̶ਙٖ᮱տኞ౮Ӟӻ
Statement੒᨝ጱ̶
ࣁֵአڦݷጱ෸ײ҅ݢզ೰ਧ۱ݷ҅ࣁֵአ௛ᯈᗝ෈կے᫹ฉ੘෈կ෸҅Ԟݢզ೰ਧ۱ݷ̶
ԆᲫইຎᵱᥝᬬࢧጱᦾֵ҅አselectKey ຽᓋܨݢ̶UUIDԞݢզᬬࢧ̶ࣁOracleጱᦾ҅ฎֵአଧ
ڜ๶ᬬࢧᛔۖीᳩጱԆᲫጱ̶
ܛ֖ᒧํӷᐿ҅Ӟᐿฎᥴຉփ᭓ᬰ๶ጱ݇හහഝ̵Ӟᐿฎܻ໏ᬌڊփ᭓ᬰ๶ጱහഝ̶

![三歪教你学Mybatis 第43页插图](../assets/images/三歪教你学Mybatis_p43_1_7178a4c6.png)

![三歪教你学Mybatis 第43页插图](../assets/images/三歪教你学Mybatis_p43_2_5936744a.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
ىᘶฉ੘
 
 
1. Mybatis̓ग़ᤒᬳള̈́
 
౯ժࣁ਍ԟHibernateጱ෸ײ҅ইຎᤒၿ݊کӷୟጱᦾ҅ᮎԍ౯ժฎࣁฉ੘෈կӾֵአ<set> .. <many-
to-one> ᒵຽᓋਖ਼ٌጱฉ੘ં௔ىᘶ᩸๶ጱ...ᮎԍࣁ౯ժMybatisӾ݈ெԍ؉ޫҘҘҘ
ض๶ࢧᶶӞӥ౯ժSQL99ጱ᧍ဩғ
Ӟ҂ٖᬳളҁᒵ꧊ᬳള҂ғັᧃਮಁনݷ҅ᦈܔᖫݩ҅ᦈܔհ໒
    ---------------------------------------------------
    select c.name,o.isbn,o.price
    from customers c inner join orders o
    where c.id = o.customers_id;
    ---------------------------------------------------
    select c.name,o.isbn,o.price
    from customers c join orders o
    where c.id = o.customers_id; 
    ---------------------------------------------------
    select c.name,o.isbn,o.price
    from customers c,orders o
    where c.id = o.customers_id;
    ---------------------------------------------------
    select c.name,o.isbn,o.price
    from customers c join orders o
    on c.id = o.customers_id;
    ---------------------------------------------------

![三歪教你学Mybatis 第44页插图](../assets/images/三歪教你学Mybatis_p44_1_3c233a1a.jpeg)

---

ኧԭ౯ժMybatisӾଚဌํ؟Hibernateᬯ໏قᛔۖ۸ጱ҅ࢩྌ౯ժฎဌํ<set> .. <many-to-one> ᒵ
ຽᓋጱ҅౯ժᬮฎֵአಋٟSQL᧍ݙ๶ֵ౯ժጱىᘶં௔ᬳള᩸๶...
 
1.1Ӟ੒Ӟ
 
ᵱ࿢ғ਍ኞ޾᫝ղᦤ
    ဳ఺ғٖᬳളҁᒵ꧊ᬳള҂ݝᚆັᧃڊग़ୟᤒӾ҅ᬳളਁྦྷፘݶጱᦕ୯
ԫ҂क़ᬳളғೲਮಁړᕟ҅ັᧃྯӻਮಁጱনݷ޾ᦈܔහ
    ---------------------------------------------------
    ૢक़ᬳളғ
    select c.name,count(o.isbn)
    from  customers c left outer join orders o
    on c.id = o.customers_id
    group by c.name; 
    ---------------------------------------------------
    ݦक़ᬳളғ
    select c.name,count(o.isbn)
    from  orders o right outer join customers c   
    on c.id = o.customers_id
    group by c.name; 
    ---------------------------------------------------
    ဳ఺ғक़ᬳള෬ᚆັᧃڊग़ୟᤒӾ҅ᬳളਁྦྷፘݶጱᦕ୯Ҕ݈ᚆ໑ഝӞො҅ਖ਼ݚӞොӧᒧݳፘݶᦕ୯
୩ᤈັᧃڊ๶
ӣ҂ᛔᬳളғ࿢ڊAAጱᘌ຃ฎEE
    ---------------------------------------------------
    ٖᛔᬳളғ
    select users.ename,boss.ename
    from emps users inner join emps boss 
    on users.mgr = boss.empno;
    ---------------------------------------------------
    क़ᛔᬳളғ
    select users.ename,boss.ename
    from emps users left outer join emps boss 
    on users.mgr = boss.empno;
    ---------------------------------------------------
    ဳ఺ғᛔᬳളฎਖ਼Ӟୟᤒ҅᭗ᬦڦݷጱොୗ҅፡֢ग़ୟᤒݸ҅ٚᬰᤈᬳള̶
    ᬯ෸ጱᬳളܨݢզ᯻አٖᬳള݈҅ݢզ᯻አक़ᬳള

---

1.1.1ᦡᦇᤒғ
 
1.1.2ਫ֛
 
--mysql
create table cards(
  cid int(5) primary key,
  cnum varchar(10)
);
create table students(
  sid int(5) primary key,
  sname varchar(10),
  scid int(5),
  constraint scid_fk foreign key(scid) references cards(cid)
);
insert into cards(cid,cnum) values(1,'111');
insert into students(sid,sname,scid) values(1,'ߢߢ',1);
select * from cards;
select * from students;
/**
 * ᫝ղᦤ(ܔො)
 * @author AdminTC

![三歪教你学Mybatis 第46页插图](../assets/images/三歪教你学Mybatis_p46_1_cb63d426.jpeg)

---

*/
public class Card {
  private Integer id;
  private String num;
  public Card(){}
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public String getNum() {
    return num;
  }
  public void setNum(String num) {
    this.num = num;
  }
}
/**
 * ਍ኞ(ܔො)
 * @author AdminTC
 */
public class Student {
  private Integer id;
  private String name;
  private Card card;//ىᘶં௔
  public Student(){}
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public Card getCard() {
    return card;
  }
  public void setCard(Card card) {
    this.card = card;
  }
}

---

1.1.3 ฉ੘෈կ
 
ኧԭ౯ժํӷӻਫ֛҅ࢩྌ౯ժտํӷӻฉ੘෈կ
 
Studentฉ੘෈կ
Cardฉ੘෈կ
1.1.4 DAO੶
 
ሿࣁ౯మ໑ഝ਍ኞጱᖫݩັᧃ਍ኞጱמ௳޾᫝ղᦤמ௳Ѻ
 
ኧԭᧆັᧃ፳᯿ฎັᧃ਍ኞጱמ௳҅ԭฎ౯ժࣁ਍ኞጱฉ੘෈կӾٟSQL᧍ݙ
 
ೲᆙᵱ࿢҅౯ժٟڊ๶ጱSQL᧍ݙฎᬯ໏ৼጱ̶
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="studentNamespace">
  
  <resultMap type="zhongfucheng2.Student" id="studentMap">
    <id property="id" column="sid"/>
    <result property="name" column="sname"/>
  </resultMap>
</mapper>
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cardNamespace">
  
  <resultMap type="zhongfucheng2.Card" id="cardMap">
    <id property="id" column="cid"/>
    <result property="num" column="cnum"/>
  </resultMap>  
  
</mapper>

---

౯๶፡Ӟӥັᧃᕮຎғ
౯ժጱਫ֛Өฉ੘ᤒӾ҅Studentਫ֛ฎဌํىᘶٌ՜ጱਁྦྷጱ҅ՐՐฎٟڊԧᧆਫ֛ጱᛔଃጱં௔̶
กดࣈ҅౯ժStudentฎӧᚆ੗ᤰᬬࢧጱᕮຎ҅ࢩྌ౯ժᵱᥝਖ਼ىᘶં௔ᬰᤈىᘶ᩸๶Ѻ
౯ժىᘶԧզݸ҅Studentਫ֛੪ᚆड़੗ᤰᬬࢧጱᕮຎԧ
select * from zhongfucheng.students s,zhongfucheng.cards c where c.cid = 
s.scid and sid=1;
  <resultMap type="zhongfucheng2.Student" id="studentMap">
    <id property="id" column="sid"/>
    <result property="name" column="sname"/>
  </resultMap>
  <resultMap type="zhongfucheng2.Student" id="studentMap">
    <id property="id" column="sid"/>
    <result property="name" column="sname"/>
    <!--
      propertyٟጱฎࣁStudentਫ֛Ӿٟىᘶਁྦྷጱં௔ݒᰁݷᑍ
      resultMapٟጱฎฉ੘෈կӾጱ޸ݷᑮᳵ.id
    -->
    <association property="card" resultMap="cardNamespace.cardMap"/>
  </resultMap>
  <resultMap type="zhongfucheng2.Student" id="studentMap">
    <id property="id" column="sid"/>
    <result property="name" column="sname"/>
    <!--
      propertyٟጱฎࣁStudentਫ֛Ӿٟىᘶਁྦྷጱં௔ݒᰁݷᑍ

![三歪教你学Mybatis 第49页插图](../assets/images/三歪教你学Mybatis_p49_1_c60a6dd6.png)

---

ັᧃᖫݩԅ1ጱ਍ኞמ௳̓۱ೡ᫝ղᦤᖫݩ̈́
 
      resultMapٟጱฎฉ੘෈կӾጱ޸ݷᑮᳵ.id
    -->
    <association property="card" resultMap="cardNamespace.cardMap"/>
  </resultMap>
  <select id="findById" parameterType="int" resultMap="studentMap">
    select * from zhongfucheng.students s,zhongfucheng.cards c where c.cid = 
s.scid and sid=#{id};
  </select>
    public Student findById(int id) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            return sqlSession.selectOne("studentNamespace.findById", id);
          /*  sqlSession.commit();*/
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        Student student = studentDao.findById(1);
        System.out.println(student.getId() + "----" + student.getName() + "---
-" + student.getCard().getNum());
    }

![三歪教你学Mybatis 第50页插图](../assets/images/三歪教你学Mybatis_p50_1_3c4566c1.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
1.2 Ӟ੒ग़
 
ᵱ࿢ғӞӻቔᕆํग़ӻ਍ኞ,ັᧃjava਍ᑀํߺԶ਍ኞמ௳

![三歪教你学Mybatis 第51页插图](../assets/images/三歪教你学Mybatis_p51_1_d088d9fd.png)

![三歪教你学Mybatis 第51页插图](../assets/images/三歪教你学Mybatis_p51_2_3c233a1a.jpeg)

---

1.2.1ᦡᦇහഝପᤒ
 
1.2.2ਫ֛
 
create table grades(
  gid int(5) primary key,
  gname varchar(10)
);
create table students(
  sid int(5) primary key,
  sname varchar(10),
  sgid int(5),
  constraint sgid_fk foreign key(sgid) references grades(gid)
);
insert into grades(gid,gname) values(1,'java');
insert into students(sid,sname,sgid) values(1,'ߢߢ',1);
insert into students(sid,sname,sgid) values(2,'޲޲',1);
select * from grades;
select * from students;
package zhongfucheng2;

![三歪教你学Mybatis 第52页插图](../assets/images/三歪教你学Mybatis_p52_1_b2901c71.jpeg)

---

import java.util.ArrayList;
import java.util.List;
/**
 * ਍ᑀ(ܔො)
 * @author AdminTC
 */
public class Grade {
  private Integer id;
  private String name;
  private List<Student> studentList = new ArrayList<Student>();//ىᘶં௔
  public Grade(){}
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public List<Student> getStudentList() {
    return studentList;
  }
  public void setStudentList(List<Student> studentList) {
    this.studentList = studentList;
  }
}
package zhongfucheng2;
/**
 * ਍ኞ(ग़ො)
 * @author AdminTC
 */
public class Student {
  private Integer id;
  private String name;
  private Grade grade;//ىᘶં௔
  public Student(){}
  public Integer getId() {
    return id;
  }

---

1.2.3ฉ੘෈կSQL᧍ݙ
 
  public void setId(Integer id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public Grade getGrade() {
    return grade;
  }
  public void setGrade(Grade grade) {
    this.grade = grade;
  }
}
<mapper namespace="studentNamespace">
  
  <resultMap type="zhongfucheng2.Student" id="studentMap">
    <id property="id" column="sid"/>
    <result property="name" column="sname"/>
  </resultMap>
  <!--ັᧃᭌץጱjava਍ᑀํग़੝֖਍ኞ-->
  <!--ኧԭ౯ժݝᥝັᧃ਍ኞጱݷਁ҅ᘒ౯ժጱਫ֛studentMapݢզ੗ᤰ਍ኞጱݷਁ҅ᮎԍ౯ժᬬࢧ
studentMapܨݢ҅ଚӧᵱᥝٚىᘶک਍ᑀᤒ-->
  <select id="findByGrade" parameterType="string" resultMap="studentMap">
    select s.sname,s.sid from zhongfucheng.students s,zhongfucheng.grades g 
WHERE s.sgid=g.gid and g.gname=#{name};
  </select>
</mapper>
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">

---

1.2.4DAO
 
 
<mapper namespace="gradeNamespace">
  
  <resultMap type="zhongfucheng2.Grade" id="gradeMap">
    <id property="id" column="gid"/>
    <result property="name" column="gname"/>
  </resultMap>
</mapper>
public List<Student> findByGrade(String  grade) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            return sqlSession.selectList("studentNamespace.findByGrade", 
grade);
          /*  sqlSession.commit();*/
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        List<Student> student = studentDao.findByGrade("java");
        for (Student student1 : student) {
            System.out.println(student1.getName());
        }
    }

---

1.3ग़੒ग़
 
ᵱ࿢ғ਍ኞ޾᧞ᑕ
1.3.1 හഝପᤒ
 
create table students(
  sid int(5) primary key,
  sname varchar(10)
);
create table courses(
  cid int(5) primary key,
  cname varchar(10)
);
create table middles(
  msid int(5),
  mcid int(5),
  primary key(msid,mcid)
);

![三歪教你学Mybatis 第56页插图](../assets/images/三歪教你学Mybatis_p56_1_7d38837f.png)

![三歪教你学Mybatis 第56页插图](../assets/images/三歪教你学Mybatis_p56_2_c907c087.jpeg)

---

1.3.2ਫ֛
 
insert into students(sid,sname) values(1,'ߢߢ');
insert into students(sid,sname) values(2,'޲޲');
insert into courses(cid,cname) values(1,'java');
insert into courses(cid,cname) values(2,'android');
insert into middles(msid,mcid) values(1,1);
insert into middles(msid,mcid) values(1,2);
insert into middles(msid,mcid) values(2,1);
insert into middles(msid,mcid) values(2,2);
select * from students;
select * from courses;
select * from middles;
package cn.itcast.javaee.mybatis.many2many;
import java.util.ArrayList;
import java.util.List;
/**
 * ᧞ᑕ(ग़ො)
 * @author AdminTC
 */
public class Course {
  private Integer id;
  private String name;
  private List<Student> studentList = new ArrayList<Student>();//ىᘶં௔
  public Course(){}
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public List<Student> getStudentList() {
    return studentList;
  }
  public void setStudentList(List<Student> studentList) {

---

1.3.3ฉ੘෈կ
 
    this.studentList = studentList;
  }
}
package cn.itcast.javaee.mybatis.many2many;
import java.util.ArrayList;
import java.util.List;
/**
 * ਍ኞ(ग़ො)
 * @author AdminTC
 */
public class Student {
  private Integer id;
  private String name;
  private List<Course> courseList = new ArrayList<Course>();//ىᘶં௔
  public Student(){}
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public List<Course> getCourseList() {
    return courseList;
  }
  public void setCourseList(List<Course> courseList) {
    this.courseList = courseList;
  }
}
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">

---

<mapper namespace="courseNamespace">
  
  <resultMap type="cn.itcast.javaee.mybatis.many2many.Course" id="courseMap">
    <id property="id" column="cid"/>
    <result property="name" column="cname"/>
  </resultMap>  
  
  
  
  <!-- ັᧃߢߢᭌ਍ԧߺԶ᧞ᑕ -->
  <select id="findAllByName" parameterType="string" resultMap="courseMap">
    select c.cid,c.cname
    from students s inner join middles m
    on s.sid = m.msid
    inner join courses c
    on m.mcid = c.cid
    and s.sname = #{name}
  </select>
  
</mapper>
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="studentNamespace">
  
  <resultMap type="cn.itcast.javaee.mybatis.many2many.Student" 
id="studentMap">
    <id property="id" column="sid"/>
    <result property="name" column="sname"/>
  </resultMap>  
  
  <select id="findAllByCourseName" parameterType="string" 
resultMap="studentMap">
    select s.sname
    from students s inner join middles m
    on s.sid = m.msid 
    inner join courses c
    on m.mcid = c.cid
    and c.cname = #{name}
  </select>
  
</mapper>

---

1.3.4DAO
 
package cn.itcast.javaee.mybatis.many2many;
import java.util.List;
import org.apache.ibatis.session.SqlSession;
import cn.itcast.javaee.mybatis.util.MybatisUtil;
/**
 * ೮ԋ੶
 * @author AdminTC
 */
public class StudentCourseDao {
  /**
   * ັᧃߢߢᭌ਍ԧߺԶ᧞ᑕ
   * @param name ᤒᐏ਍ኞጱনݷ
   */
  public List<Course> findAllByName(String name) throws Exception{
    SqlSession sqlSession = null;
    try{
      sqlSession = MybatisUtil.getSqlSession();
      return sqlSession.selectList("courseNamespace.findAllByName",name);
    }catch(Exception e){
      e.printStackTrace();
      throw e;
    }finally{
      MybatisUtil.closeSqlSession();
    }
  }
  /**
   * ັᧃjava᧞ᑕํߺԶ਍ኞᭌץ
   * @param name ᤒᐏ਍ኞጱ᧞ᑕ
   */
  public List<Student> findAllByCourseName(String name) throws Exception{
    SqlSession sqlSession = null;
    try{
      sqlSession = MybatisUtil.getSqlSession();
      return 
sqlSession.selectList("studentNamespace.findAllByCourseName",name);
    }catch(Exception e){
      e.printStackTrace();
      throw e;
    }finally{
      MybatisUtil.closeSqlSession();
    }

---

2. ىᘶฉ੘௛ᕮ
 
੒ԭMybatisጱग़ᤒᬳള੪ᶋଉᓌܔԧ҅ኧԭSQL᧍ݙقฎኧ౯ժᛔ૩ٟ҅ইຎ౯ժᬬࢧጱහഝᔄࣳࣁ
୮ڹጱਫ֛Ӿฎӧड़੗ᤰጱᦾ҅ᮎԍ౯ժݝᥝٚىᘶ੒ଫጱฉ੘ં௔੪ᤈԧѺ
  }
  
  public static void main(String[] args) throws Exception{
    StudentCourseDao dao = new StudentCourseDao();
    List<Course> courseList = dao.findAllByName("ߢߢ");
    System.out.print("ߢߢᭌ਍ԧ" + courseList.size()+"ӻ᧞ᑕ,ړڦฎғ");
    for(Course c : courseList){
      System.out.print(c.getName()+" ");
    }
    System.out.println("\n----------------------------------------------------
-");
    List<Student> studentList = dao.findAllByCourseName("android");
    System.out.println("ᭌץԧandroid᧞ᑕጱ਍ኞํ"+studentList.size()+"ӻ҅ړڦ
ฎғ");
    for(Student s : studentList){
      System.out.print(s.getName()+" ");
    }
  }
}

![三歪教你学Mybatis 第61页插图](../assets/images/三歪教你学Mybatis_p61_1_0b0f5a40.jpeg)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
 
ᖨਂ+Mapperդቘ+ᭋݻૡᑕ
 
 
1. ڹ᥺
 
๜෈ԆᥝᦖᥴMybatisጱզӥᎣᦩᅩғ
Mybatisᖨਂ
Ӟᕆᖨਂ
ԫᕆᖨਂ
ӨEhcacheෆݳ
Mapperդቘ
ֵአMapperդቘ੪ӧአٟਫሿᔄԧ
ᭋݻૡᑕ
ᛔۖኞ౮դᎱ
2. Mybatisᖨਂ
 
ᖨਂጱ఺Ԏਖ਼አಁᕪଉັᧃጱහഝනࣁᖨਂҁٖਂ҂Ӿ҅አಁ݄ັᧃහഝ੪ӧአ՗ᏺፏӤ(ىᔮࣳහഝପ
හഝ෈կ)ັᧃ҅՗ᖨਂӾັᧃ҅՗ᘒ൉ṛັᧃපሲ҅ᥴ٬ԧṛଚݎᔮᕹጱ௔ᚆᳯ̶᷌

![三歪教你学Mybatis 第62页插图](../assets/images/三歪教你学Mybatis_p62_1_3c233a1a.jpeg)

---

mybatis൉׀Ӟᕆᖨਂ޾ԫᕆᖨਂ

![三歪教你学Mybatis 第63页插图](../assets/images/三歪教你学Mybatis_p63_1_a204ab29.png)

---

mybatisӞᕆᖨਂฎӞӻSqlSessionᕆڦ҅sqlsessionݝᚆᦢᳯᛔ૩ጱӞᕆᖨਂጱහഝ
ԫᕆᖨਂฎ᪜sqlSession҅ฎmapperᕆڦጱᖨਂ҅੒ԭmapperᕆڦጱᖨਂӧݶጱsqlsessionฎ
ݢզوՁጱ̶
፡ਠӤᶎ੒Mybatisጱᖨਂጱᥴ᯽҅౯ժݎሿMybatisጱᖨਂ޾Hibernateጱᖨਂฎຄԅፘ֒ጱ..
 
2.1 MybatisӞᕆᖨਂ
 
 
MybatisጱӞᕆᖨਂܻቘғ
ᒫӞེݎڊӞӻັᧃsql҅sqlັᧃᕮຎٟفsqlsessionጱӞᕆᖨਂӾ҅ᖨਂֵአጱහഝᕮ຅ฎӞӻ
map<key,value>
keyғhashcode+sql+sqlᬌف݇හ+ᬌڊ݇හҁsqlጱࠔӞຽᦩ҂

![三歪教你学Mybatis 第64页插图](../assets/images/三歪教你学Mybatis_p64_1_4d92af56.png)

![三歪教你学Mybatis 第64页插图](../assets/images/三歪教你学Mybatis_p64_2_302aa4cb.png)

---

valueғአಁמ௳
ݶӞӻsqlsessionེٚݎڊፘݶጱsql҅੪՗ᖨਂӾݐӧᩳහഝପ̶ইຎӷེӾᳵڊሿcommit඙֢ҁץ
ද̵Ⴒے̵ڢᴻ҂҅๜sqlsessionӾጱӞᕆᖨਂ܄ऒق᮱Ⴔᑮ҅ӥེ݄ٚᖨਂӾັᧃӧکಅզᥝ՗හഝ
ପັᧃ҅՗හഝପັᧃکٟٚفᖨਂ̶
 
MybatisӞᕆᖨਂ꧊஑ဳ఺ጱࣈොғ
Mybatisἕᦊ੪ฎඪ೮Ӟᕆᖨਂጱ҅ଚӧᵱᥝ౯ժᯈᗝ.
mybatis޾springෆݳݸᬰᤈmapperդቘ୏ݎ҅ӧඪ೮Ӟᕆᖨਂ҅mybatis޾springෆݳ҅spring
ೲᆙmapperጱཛྷ຃݄ኞ౮mapperդቘ੒᨝҅ཛྷ຃Ӿࣁ๋ݸᕹӞىᳮsqlsession̶
2.2 Mybatisԫᕆᖨਂ
 
ԫᕆᖨਂܻቘғ
ԫᕆᖨਂጱ᝜ࢱฎmapperᕆڦҁmapperݶӞӻ޸ݷᑮᳵ҂҅mapperզ޸ݷᑮᳵԅܔ֖ڠୌᖨਂහ
ഝᕮ຅҅ᕮ຅ฎmap<key̵value>̶

![三歪教你学Mybatis 第65页插图](../assets/images/三歪教你学Mybatis_p65_1_883f2b3b.png)

![三歪教你学Mybatis 第65页插图](../assets/images/三歪教你学Mybatis_p65_2_70a1352e.png)

---

2.3Mybatisԫᕆᖨਂᯈᗝ
 
ᵱᥝ౯ժࣁMybatisጱᯈᗝ෈կӾᯈᗝԫᕆᖨਂ
Ӥᶎ૪ᕪ᧔ԧ҅ԫᕆᖨਂጱ᝜ࢱฎmapperᕆڦጱ҅ࢩྌ౯ժጱMapperইຎᥝֵአԫᕆᖨਂ҅ᬮᵱᥝ
ࣁ੒ଫጱฉ੘෈կӾᯈᗝ..
2.4 ັᧃᕮຎฉ੘ጱpojoଧڜ۸
 
mybatisԫᕆᖨਂᵱᥝਖ਼ັᧃᕮຎฉ੘ጱpojoਫሿ java.io.serializableളݗ҅ইຎӧਫሿڞಲڊ୑ଉғ
ԫᕆᖨਂݢզਖ਼ٖਂጱහഝٟکᏺፏ҅ਂࣁ੒᨝ጱଧڜ۸޾ݍଧڜ۸҅ಅզᥝਫሿjava.io.serializable
ളݗ̶
ইຎᕮຎฉ੘ጱpojoӾᬮ۱ೡԧpojo҅᮷ᥝਫሿjava.io.serializableളݗ̶
2.5 ᐬአԫᕆᖨਂ
 
੒ԭݒ۸᷇ሲ᫾ṛጱsql҅ᵱᥝᐬአԫᕆᖨਂғ
ࣁstatementӾᦡᗝuseCache=falseݢզᐬአ୮ڹselect᧍ݙጱԫᕆᖨਂ҅ܨྯེັᧃ᮷տݎڊsql݄
ັᧃ҅ἕᦊఘ٭ฎtrue҅ܨᧆsqlֵአԫᕆᖨਂ̶̵̵
2.6 ڬෛᖨਂ
 
  <!-- قੴᯈᗝ݇හ -->
  <settings>
    <!-- ୏ސԫᕆᖨਂ -->
    <setting name="cacheEnabled" value="true"/>
  </settings>
  <cache/>
org.apache.ibatis.cache.CacheException: Error serializing object. 
 Cause:java.io.NotSerializableException: cn.itcast.mybatis.po.User
<select id="findOrderListResultMap" resultMap="ordersUserMap" 
useCache="false">

![三歪教你学Mybatis 第66页插图](../assets/images/三歪教你学Mybatis_p66_1_b606b2c0.png)

---

ํጱݶ਍کᬯ᯾ݢᚆտํӞӻወᳯғԅՋԍᖨਂ౯ժ᮷ฎࣁັᧃ᧍ݙӾᯈᗝҘҘᘒֵአीڢදጱ෸ײ҅
ᖨਂἕᦊ੪տᤩႴᑮ̓ڬෛԧ̈́ҘҘҘ
ᖨਂٌਫ੪ฎԅ౯ժጱັᧃ๐ۓጱ҅੒ԭीڢදᘒ᥺҅ইຎ౯ժጱᖨਂכਂԧीڢදݸጱහഝ҅ᮎԍٚ
ེ᧛ݐ෸੪տ᧛کᚍහഝԧѺ
౯ժࣁᇙਧጱఘ٭ӥ҅ᬮݢզܔᇿᯈᗝڬෛᖨਂ̓֕ӧୌᦓֵአ̈́ﬂushCache҅ἕᦊฎጱtrue
2.7 ԧᥴMybatisᖨਂጱӞԶ݇හ
 
mybatisጱcache݇හݝᭇአԭmybatisᖌಷᖨਂ̶
 
  <update id="updateUser" parameterType="cn.itcast.mybatis.po.User" 
flushCache="false">
    update user set username=#{username},birthday=#{birthday},sex=#
{sex},address=#{address} where id=#{id}
  </update>
flushIntervalҁڬෛᳵᵍ҂ݢզᤩᦡᗝԅձ఺ጱྋෆහ҅ᘒӬਙժդᤒӞӻݳቘጱྺᑁ୵ୗጱ෸ᳵྦྷ̶
ἕᦊఘ٭ฎӧᦡᗝ҅Ԟ੪ฎဌํڬෛᳵᵍ҅ᖨਂՐՐ᧣አ᧍ݙ෸ڬෛ̶
sizeҁ୚አහፓ҂ݢզᤩᦡᗝԅձ఺ྋෆහ҅ᥝᦕ֦֘ᖨਂጱ੒᨝හፓ޾֦ᬩᤈሾहጱݢአٖਂᩒრහ
ፓ̶ἕᦊ꧊ฎ1024̶
readOnlyҁݝ᧛҂ં௔ݢզᤩᦡᗝԅtrue౲false̶ݝ᧛ጱᖨਂտᕳಅํ᧣አᘏᬬࢧᖨਂ੒᨝ጱፘݶਫ
̶ֺࢩྌᬯԶ੒᨝ӧᚆᤩץද̶ᬯ൉׀ԧஉ᯿ᥝጱ௔ᚆս̶۠ݢ᧛ٟጱᖨਂտᬬࢧᖨਂ੒᨝ጱ೩ᨬҁ᭗ᬦଧ
ڜ۸҂̶ᬯտౌӞԶ҅֕ฎਞق҅ࢩྌἕᦊฎfalse̶
ইӥֺৼғ
<cache  eviction="FIFO"  flushInterval="60000"  size="512"  readOnly="true"/>
ᬯӻๅṛᕆጱᯈᗝڠୌԧӞӻ FIFO ᖨਂ,ଚྯᵍ 60 ᑁڬෛ,ਂහᕮຎ੒᨝౲ڜᤒጱ 512 ӻ୚አ,ᘒӬ
ᬬࢧጱ੒᨝ᤩᦊԅฎݝ᧛ጱ,ࢩྌࣁӧݶᕚᑕӾጱ᧣አᘏԏᳵץදਙժտ੕ᛘ٫ᑱ̶ݢአጱතࢧᒽኼํ, ἕ
ᦊጱฎ LRU:
1.LRU – ๋ᬪ๋੝ֵአጱ:ᑏᴻ๋ᳩ෸ᳵӧᤩֵአጱ੒᨝̶
2.FIFO – ضᬰضڊ:ೲ੒᨝ᬰفᖨਂጱᶲଧ๶ᑏᴻਙժ̶
3.SOFT – ᫫୚አ:ᑏᴻचԭ࣯࣍ࢧත࢏ᇫா޾᫫୚አᥢڞጱ੒᨝̶
4.WEAK – ୧୚አ:ๅᑌຄࣈᑏᴻचԭ࣯࣍තᵞ࢏ᇫா޾୧୚አᥢڞጱ੒᨝̶

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
3.mybatis޾ehcacheᖨਂ໛ຝෆݳ
 
ehcacheฎӫᳪአԭᓕቘᖨਂጱ҅MybatisጱᖨਂԻኧehcacheᓕቘտๅے஑୮..
ࣁmybatisӾ൉׀Ӟӻcacheളݗ҅ݝᥝਫሿcacheളݗ੪ݢզ಩ᖨਂහഝᅎၚጱᓕቘ᩸๶̶

![三歪教你学Mybatis 第68页插图](../assets/images/三歪教你学Mybatis_p68_1_9759acba.png)

![三歪教你学Mybatis 第68页插图](../assets/images/三歪教你学Mybatis_p68_2_3c233a1a.jpeg)

---

3.1ෆݳjar۱
 
ๅෛғইຎᶱፓฎmaven҅አmaven੪অԧ
mybatis-ehcache-1.0.2.jar
ehcache-core-2.6.5.jar
ehcache੒cacheളݗጱਫሿᔄғ

![三歪教你学Mybatis 第69页插图](../assets/images/三歪教你学Mybatis_p69_1_623b4954.png)

---

3.2 ehcache.xmlᯈᗝמ௳
 
ᬯӻxmlᯈᗝ෈կฎᯈᗝقੴጱᖨਂᓕቘොໜ
ইຎ౯ժMapperమܔᇿ೜ํӞԶᇙ௔҅ᵱᥝࣁmapper.xmlӾܔᇿᯈᗝ
<ehcache xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="../config/ehcache.xsd">
  <!--diskStoreғᖨਂහഝ೮ԋ۸ጱፓ୯ ࣈ࣎  -->
  <diskStore path="F:\develop\ehcache" />
  <defaultCache 
    maxElementsInMemory="1000" 
    maxElementsOnDisk="10000000"
    eternal="false" 
    overflowToDisk="false" 
    diskPersistent="true"
    timeToIdleSeconds="120"
    timeToLiveSeconds="120" 
    diskExpiryThreadIntervalSeconds="120"
    memoryStoreEvictionPolicy="LRU">
  </defaultCache>
</ehcache>

![三歪教你学Mybatis 第70页插图](../assets/images/三歪教你学Mybatis_p70_1_78a8aab3.png)

---

3.3ଫአ࣋วӨੴᴴ௔
 
3.3.1 ଫአ࣋ว
 
੒ັᧃ᷇ሲṛ҅ݒ۸᷇ሲ֗ጱහഝୌᦓֵአԫᕆᖨਂ̶
੒ԭᦢᳯग़ጱັᧃ᧗࿢Ӭአಁ੒ັᧃᕮຎਫ෸௔ᥝ࿢ӧṛ҅ྌ෸ݢ᯻አmybatisԫᕆᖨਂದ๞ᴳ֗හഝ
ପᦢᳯᰁ҅൉ṛᦢᳯ᭛ଶ
ӱۓ࣋วྲইғ
ᘙ෸᫾ṛጱᕹᦇړຉsql̵
ኪᦾᨴܔັᧃsqlᒵ̶
ਫሿොဩইӥғ᭗ᬦᦡᗝڬෛᳵᵍ෸ᳵ҅ኧmybatisྯᵍӞྦྷ෸ᳵᛔۖႴᑮᖨਂ҅໑ഝහഝݒ۸᷇ሲᦡ
ᗝᖨਂڬෛᳵᵍﬂushInterval҅ྲইᦡᗝԅ30ړᰦ̵60ړᰦ̵24ੜ෸ᒵ҅໑ഝᵱ࿢ᘒਧ̶
3.3.2ੴᴴ௔
 
mybatisੴᴴ௔
mybatisԫᕆᖨਂ੒ᕡᔉଶጱහഝᕆڦጱᖨਂਫሿӧঅ҅ྲইইӥᵱ࿢ғ੒ࠟߝמ௳ᬰᤈᖨਂ҅ኧԭࠟ
ߝמ௳ັᧃᦢᳯᰁय़҅֕ฎᥝ࿢አಁྯེ᮷ᚆັᧃ๋ෛጱࠟߝמ௳҅ྌ෸ইຎֵአmybatisጱԫᕆᖨਂ
੪෫ဩਫሿ୮Ӟӻࠟߝݒ۸෸ݝڬෛᧆࠟߝጱᖨਂמ௳ᘒӧڬෛٌਙࠟߝጱמ௳҅ࢩԅmybaitsጱԫᕆ
ᖨਂ܄ऒզmapperԅܔ֖ښړ҅୮Ӟӻࠟߝמ௳ݒ۸տਖ਼ಅํࠟߝמ௳ጱᖨਂහഝق᮱Ⴔᑮ̶ᥴ٬ྌ
ᔄᳯ᷌ᵱᥝࣁӱۓ੶໑ഝᵱ࿢੒හഝํᰒ੒௔ᖨਂ̶
4. Mapperդቘොୗ
 
Mapperդቘොୗጱ఺௏੪ฎғᑕଧާݝᵱᥝٟdaoളݗ҅daoളݗਫሿ੒᨝ኧmybatisᛔۖኞ౮դቘ
੒᨝̶
ᕪᬦ౯ժӤᶎጱپᓤܗ෈҅౯ժݢզݎሿ౯ժጱDaoImplฎ܈ړ᯿॔ጱ...
1 daoጱਫሿᔄӾਂࣁ᯿॔դᎱ҅ෆӻmybatis඙֢ጱᬦᑕդᎱཛྷ຃᯿॔ҁضڠୌsqlsession̵᧣አ
sqlsessionጱොဩ̵ىᳮsqlsession҂
2̵daoጱਫሿ ᔄӾਂࣁᏝᖫᎱ҅᧣አsqlsessionොဩ෸ਖ਼statementጱidᏝᖫᎱ̶
զڹጱ᯿॔դᎱ޾ᏝᖫᎱইӥғ
  <!-- ܔ֖ғྺᑁ -->
  <cache type="org.mybatis.caches.ehcache.EhcacheCache">
    <property name="timeToIdleSeconds" value="12000"/>
        <property name="timeToLiveSeconds" value="3600"/>
        <!-- ݶehcache݇හmaxElementsInMemory -->
    <property name="maxEntriesLocalHeap" value="1000"/>
    <!-- ݶehcache݇හmaxElementsOnDisk -->
        <property name="maxEntriesLocalDisk" value="10000000"/>
        <property name="memoryStoreEvictionPolicy" value="LRU"/>
  </cache>

---

4.1 Mapper୏ݎᥢ᝜
 
మᥝMybatisଆ౯ժᛔۖኞ౮Mapperդቘጱᦾ҅౯ժᵱᥝ᭽஗զӥጱᥢ᝜ғ
1̵mapper.xmlӾnamespace೰ਧԅmapperളݗጱقᴴਧݷ
ྌྍṈፓጱғ᭗ᬦmapper.xml޾mapper.javaᬰᤈىᘶ̶
2̵mapper.xmlӾstatementጱid੪ฎmapper.javaӾොဩݷ
3̵mapper.xmlӾstatementጱparameterType޾mapper.javaӾොဩᬌف݇හᔄࣳӞᛘ
4̵mapper.xmlӾstatementጱresultType޾mapper.javaӾොဩᬬࢧ꧊ᔄࣳӞᛘ.
ེٚ᧔กғstatement੪ฎ౯ժࣁmapper.xml෈կӾ޸ݷᑮᳵ+sql೰ਧጱid
4.2Mapperդቘᬬࢧ꧊ᳯ᷌
 
mapperളݗොဩᬬࢧ꧊ғ
ইຎฎᬬࢧጱܔӻ੒᨝҅ᬬࢧ꧊ᔄࣳฎpojoᔄࣳ҅ኞ౮ጱդቘ੒᨝ٖ᮱᭗ᬦselectOne឴ݐᦕ୯
ইຎᬬࢧ꧊ᔄࣳฎᵞݳ੒᨝҅ኞ౮ጱդቘ੒᨝ٖ᮱᭗ᬦselectList឴ݐᦕ୯̶
5. Mybatisᥴ٬JDBCᖫᑕጱᳯ᷌
 
1̵හഝପ᱾ളڠୌ̵᯽න᷇ᔺ᭜౮ᔮᕹᩒრၵᩇ՗ᘒ୽ߥᔮᕹ௔ᚆ҅ইຎֵአහഝପ᱾ള࿰ݢᥴ٬ྌ
ᳯ̶᷌
public class StudentDao {
    public void add(Student student) throws Exception {
        //஑کᬳള੒᨝
        SqlSession sqlSession = MybatisUtil.getSqlSession();
        try{
            //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
            sqlSession.insert("StudentID.add", student);
            sqlSession.commit();
        }catch(Exception e){
            e.printStackTrace();
            sqlSession.rollback();
            throw e;
        }finally{
            MybatisUtil.closeSqlSession();
        }
    }
    public static void main(String[] args) throws Exception {
        StudentDao studentDao = new StudentDao();
        Student student = new Student(3, "zhong3", 10000D);
        studentDao.add(student);
    }
}

---

ᥴ٬ғࣁSqlMapConﬁg.xmlӾᯈᗝහഝ᱾ള࿰ֵ҅አᬳള࿰ᓕቘහഝପ᱾ള̶
2̵Sql᧍ݙٟࣁդᎱӾ᭜౮դᎱӧฃᖌಷ҅ਫᴬଫአsqlݒ۸ጱݢᚆ᫾य़҅sqlݒۖᵱᥝදݒjavaդᎱ̶
ᥴ٬ғਖ਼Sql᧍ݙᯈᗝࣁXXXXmapper.xml෈կӾӨjavaդᎱړᐶ̶
3̵ݻsql᧍ݙփ݇හἋᅸ҅ࢩԅsql᧍ݙጱwhere๵կӧӞਧ҅ݢᚆग़Ԟݢᚆ੝҅ܛ֖ᒧᵱᥝ޾݇හӞӞ
੒ଫ̶
ᥴ٬ғMybatisᛔۖਖ਼java੒᨝ฉ੘ᛗsql᧍ݙ҅᭗ᬦstatementӾጱparameterTypeਧԎᬌف
݇හጱᔄ̶ࣳ
4̵੒ᕮຎᵞᥴຉἋᅸ҅sqlݒ۸੕ᛘᥴຉդᎱݒ۸҅Ӭᥴຉڹᵱᥝ᭭ܲ҅ইຎᚆਖ਼හഝପᦕ୯੗ᤰ౮
pojo੒᨝ᥴຉྲ᫾ො׎̶
ᥴ٬ғMybatisᛔۖਖ਼sqlಗᤈᕮຎฉ੘ᛗjava੒᨝҅᭗ᬦstatementӾጱresultTypeਧԎᬌڊᕮ
ຎጱᔄ̶ࣳ
6.Mybatisᭋݻૡᑕ
 
 
MybatisᭋݻૡᑕਫᴬӤ੪ฎమᛔۖኞ౮੒ଫጱդᎱ҅ӧአᛔ૩ٟ੒ଫጱฉ੘෈կ޾ളݗҁ݈؎ౡԧ҂
 
׵ᰄܗ෈ғhttp://blog.csdn.net/for_my_life/article/details/51228098
6.1 ץදpom.xml෈կ
 
ݻᧆૡᑕႲےᭋݻૡᑕൊկ..
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>asdf</groupId>
    <artifactId>asdf</artifactId>
    <version>1.0-SNAPSHOT</version>
    <build>
        <finalName>zhongfucheng</finalName>
        <plugins>
            <plugin>
                <groupId>org.mybatis.generator</groupId>
                <artifactId>mybatis-generator-maven-plugin</artifactId>
                <version>1.3.2</version>
                <configuration>
                    <verbose>true</verbose>
                    <overwrite>true</overwrite>

---

6.2generatorConﬁg.xmlᯈᗝ෈կ
 
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE generatorConfiguration
        PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
        "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">
<generatorConfiguration>
    <!--
        <properties resource="conn.properties" />
          -->
    <!-- ॒ቘ1҅ᬯ᯾ጱjar۱֖ᗝݢᚆᵱᥝץද -->
    <classPathEntry location="C:\mybatisMaven\lib\mysql-connector-java-5.1.7-
bin.jar"/>
    <!-- ೰ਧᬩᤈሾहฎmybatis3ጱᇇ๜ -->
    <context id="testTables" targetRuntime="MyBatis3">
        <commentGenerator>
            <!-- ฎވݐၾဳ᯽ -->
            <property name="suppressAllComments" value="true" />
            <!-- ฎވኞ౮ဳ᯽դ෸ᳵ౿ -->
            <property name="suppressDate" value="true" />
        </commentGenerator>
        <!-- ॒ቘ2   jdbc ᬳളמ௳҅፡፡ପฎވਂࣁ -->
        <jdbcConnection driverClass="com.mysql.jdbc.Driver"
                        connectionURL="jdbc:mysql://localhost:3306/scm?
useUnicode=true&characterEncoding=UTF-8" userId="root" password="root">
        </jdbcConnection>
        <!--॒ቘ3   targetPackage೰ਧཛྷࣳࣁኞ౮ࣁߺӻ۱ ,targetProject೰ਧᶱፓጱ
src,-->
        <javaModelGenerator targetPackage="zhongfucheng.entity"
                            targetProject="src/main/java">
            <!-- ݄ᴻਁྦྷڹݸᑮ໒ -->
            <property name="trimStrings" value="false" />
        </javaModelGenerator>
        <!--॒ቘ4   ᯈᗝSQLฉ੘෈կኞ౮מ௳ -->
        <sqlMapGenerator targetPackage="zhongfucheng.dao"
                         targetProject="src/main/java" />
        <!-- ॒ቘ5   ᯈᗝdaoളݗኞ౮מ௳-->

---

6.3 ֵአൊկྍṈ
 
 
6.4๋ݸኞ౮դᎱ
 
ইຎ੒౯ժӤᶎgeneratorConﬁg.xmlᯈᗝጱ۱מ௳ӧႴ༩ጱᦾ҅ᮎԍݢզ፡Ӟӥ౯ժጱਠෆᶱፓᕮ຅
ࢶ...
ࢩԅ౯ժࣁIdeaӥฎӧአٟ੒ଫጱૡᑕݷਁጱ҅ᘒࣁeclipseฎํૡᑕݷਁጱ̶
        <javaClientGenerator type="XMLMAPPER" targetPackage="zhongfucheng.dao" 
targetProject="src/main/java" />
        <table tableName="account" domainObjectName="Account"/>
        <table tableName="supplier" domainObjectName="Supplier"/>
    </context>
</generatorConfiguration>

![三歪教你学Mybatis 第75页插图](../assets/images/三歪教你学Mybatis_p75_1_3a6fe995.png)

---

7.๜ᒍ௛ᕮ
 
MybatisጱӞᕆᖨਂฎsqlSessionᕆڦጱ̶ݝᚆᦢᳯᛔ૩ጱsqlSessionٖጱᖨਂ̶ইຎMybatisӨ
Springෆݳԧ҅SpringտᛔۖىᳮsqlSessionጱ̶ಅզӞᕆᖨਂտ०පጱ̶
Ӟᕆᖨਂጱܻቘฎmapᵞݳ҅Mybatisἕᦊ੪ඪ೮Ӟᕆᖨਂ
ԫᕆᖨਂฎMapperᕆڦጱ̶ݝᥝࣁMapper޸ݷᑮᳵӥ᮷ݢզֵአԫᕆᖨਂ̶ᵱᥝ౯ժᛔ૩ಋۖ
݄ᯈᗝԫᕆᖨਂ
Mybatisጱᖨਂ౯ժݢզֵአEhcache໛ຝ๶ᬰᤈᓕቘ҅EhcacheਫሿCacheളݗ੪դᤒֵአ
Ehcache๶ሾहMybatisᖨਂ̶
ኧԭԏڹٟጱDaoImplฎํᶋଉग़ጱᏝᖫᎱጱ̶ݢզֵአMapperդቘጱොୗ๶ᓌ۸୏ݎ
޸ݷᑮᳵᥝӨJavaBeanጱقᔄݷፘݶ
sqlᇆྦྷ᧍ݙጱidᥝӨDaoളݗጱොဩݷፘݶ
ොဩጱ݇හ޾ᬬࢧ꧊ᥝӨSQLᇆྦྷጱളත݇හᔄࣳ޾ᬬࢧᔄࣳፘݶ̶

![三歪教你学Mybatis 第76页插图](../assets/images/三歪教你学Mybatis_p76_1_19c67137.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
MybatisෆݳSpring
 
 
1. MybatisӨSpringෆݳ
 
෬ᆐ౯ժ૪ᕪ਍ԧMybatisጱच๜୏ݎԧ҅ളӥ๶੪ฎMybatisӨSpringጱෆݳԧѺ
զӥֵአጱฎOracleහഝପ๶ᬰᤈၥᦶ
1.1੕فjar۱
 
ๅෛғইຎአMavenጱᦾ҅ፗളֵአMaven੪অԧ
aopalliance.jar
asm-3.3.1.jar

![三歪教你学Mybatis 第77页插图](../assets/images/三歪教你学Mybatis_p77_1_2a13ce9e.jpeg)

![三歪教你学Mybatis 第77页插图](../assets/images/三歪教你学Mybatis_p77_2_3c233a1a.jpeg)

---

aspectjweaver.jar
c3p0-0.9.1.2.jar
cglib-2.2.2.jar
commons-logging.jar
log4j-1.2.16.jar
mybatis-3.1.1.jar
mybatis-spring-1.1.1.jar
mysql-connector-java-5.1.7-bin.jar
ojdbc5.jar
org.springframework.aop-3.0.5.RELEASE.jar
org.springframework.asm-3.0.5.RELEASE.jar
org.springframework.beans-3.0.5.RELEASE.jar
org.springframework.context-3.0.5.RELEASE.jar
org.springframework.core-3.0.5.RELEASE.jar
org.springframework.expression-3.0.5.RELEASE.jar
org.springframework.jdbc-3.0.5.RELEASE.jar
org.springframework.orm-3.0.5.RELEASE.jar
org.springframework.transaction-3.0.5.RELEASE.jar
org.springframework.web.servlet-3.0.5.RELEASE.jar
org.springframework.web-3.0.5.RELEASE.jar     
 
1.2 ڠୌᤒ
 
1.3 ڠୌਫ֛
 
create table emps(
  eid number(5) primary key,
  ename varchar2(20),
  esal number(8,2),
  esex varchar2(2)
);
package entity;
/**
 * ާૡ
 * @author AdminTC
 */
public class Emp {
  private Integer id;
  private String name;
  private Double sal;
  private String sex;
  public Emp(){}
  public Emp(Integer id, String name, Double sal, String sex) {

---

1.4 ڠୌਫ֛Өᤒጱฉ੘෈կ
 
    this.id = id;
    this.name = name;
    this.sal = sal;
    this.sex = sex;
  }
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public Double getSal() {
    return sal;
  }
  public void setSal(Double sal) {
    this.sal = sal;
  }
  public String getSex() {
    return sex;
  }
  public void setSex(String sex) {
    this.sex = sex;
  }
}
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="empNamespace">
  
  <resultMap type="entity.Emp" id="empMap">
    <id property="id" column="eid"/>
    <result property="name" column="ename"/>
    <result property="sal" column="esal"/>
    <result property="sex" column="esex"/>
  </resultMap>  
  
  <!-- ीےާૡ -->

---

1.5 ڠୌMybatisฉ੘෈կᯈᗝሾह
 
හഝପጱמ௳ԻኧSpringᓕቘѺMybatisᯈᗝ෈կᨮᨱے᫹੒ଫฉ੘෈կܨݢ
1.6 ᯈᗝSpring໐ஞᬦᄁ࢏̓Ԟฎے᫹௛ᯈᗝ෈կ̈́
 
1.7 ᯈᗝහഝପמ௳̵Ԫۓ
 
  <insert id="add" parameterType="entity.Emp">
    insert into emps(eid,ename,esal,esex) values(#{id},#{name},#{sal},#{sex})
  </insert>
  
</mapper>
  <mappers>
    <mapper resource="zhongfucheng/entity/EmpMapper.xml"/>
  </mappers>
</configuration>
    <!-- ໐ஞspringmvc໐ஞഴګ࢏ -->
    <servlet>
        <servlet-name>DispatcherServlet</servlet-name>
        <servlet-
class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>classpath:spring.xml</param-value>
        </init-param>
    </servlet>
    <servlet-mapping>
        <servlet-name>DispatcherServlet</servlet-name>
        <url-pattern>*.action</url-pattern>
    </servlet-mapping>
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:tx="http://www.springframework.org/schema/tx"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xmlns:context="http://www.springframework.org/schema/context"

---

xsi:schemaLocation="http://www.springframework.org/schema/beans 
http://www.springframework.org/schema/beans/spring-beans.xsd 
http://www.springframework.org/schema/tx 
http://www.springframework.org/schema/tx/spring-tx.xsd 
http://www.springframework.org/schema/aop 
http://www.springframework.org/schema/aop/spring-aop.xsd 
http://www.springframework.org/schema/context 
http://www.springframework.org/schema/context/spring-context.xsd">
    <!-- ᯈᗝC3P0ᬳള࿰,ፓጱғᓕቘහഝପᬳള -->
    <bean id="comboPooledDataSourceID" 
class="com.mchange.v2.c3p0.ComboPooledDataSource">
        <property name="driverClass" value="oracle.jdbc.driver.OracleDriver"/>
        <property name="jdbcUrl" 
value="jdbc:oracle:thin:@127.0.0.1:1521:ZHONGFUCHENG"/>
        <property name="user" value="scott"/>
        <property name="password" value="tiger"/>
    </bean>
    <!-- ᯈᗝSqlSessionFactoryBean҅ፓጱғے᫹mybaitsᯈᗝ෈կ޾ฉ੘෈կ҅ܨ๊դܻ
Mybatisૡٍᔄጱ֢አ -->
    <bean id="sqlSessionFactoryBeanID" 
class="org.mybatis.spring.SqlSessionFactoryBean">
        <property name="configLocation" value="classpath:mybatis.xml"/>
        <property name="dataSource" ref="comboPooledDataSourceID"/>
    </bean>
    <!-- ᯈᗝMybatisጱԪۓᓕቘ࢏҅ܨࢩԅMybatisବ੶አጱฎJDBCԪۓᓕԪ࢏҅ಅզࣁᬯ᯾ׁᆐᯈ
ᗝJDBCԪۓᓕቘ࢏ -->
    <bean id="dataSourceTransactionManagerID" 
class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
        <property name="dataSource" ref="comboPooledDataSourceID"/>
    </bean>
    <!-- ᯈᗝԪۓ᭗Ꭳ҅ܨᦏߺԶොဩᵱᥝԪۓඪ೮ -->
    <tx:advice id="tx" transaction-manager="dataSourceTransactionManagerID">
        <tx:attributes>
            <tx:method name="*" propagation="REQUIRED"/>
        </tx:attributes>
    </tx:advice>
    <!-- ᯈᗝԪۓڔᶎ҅ܨᦏߺԶ۱ӥጱᔄᵱᥝԪۓ -->
    <aop:config>
        <aop:pointcut id="pointcut" expression="execution(* 
zhongfucheng.service.*.*(..))"/>
        <aop:advisor advice-ref="tx" pointcut-ref="pointcut"/>

---

1.8 ڠୌDao̵Service̵Action
 
    </aop:config>
    <!--ಚൈဳᥴ-->
    <context:component-scan base-package="zhongfucheng"/>
</beans>
@Repository
public class EmpDao {
    @Autowired
    private SqlSessionFactory sqlSessionFactory;
    /**
     * ीےާૡ
     */
    public void add(Emp emp) throws Exception {
        SqlSession sqlSession = sqlSessionFactory.openSession();
        sqlSession.insert("empNamespace.add", emp);
        sqlSession.close();
    }
}
@Service
public class EmpService {
    @Autowired
    private zhongfucheng.dao.EmpDao empDao;
    public void addEmp(Emp emp) throws Exception {
        empDao.add(emp);
    }
}
  
@Controller
@RequestMapping("/emp")
public class EmpAction {
    @Autowired
    private EmpService empService;

---

1.9JSPᶭᶎၥᦶ
 
    @RequestMapping("/register")
    public void register(Emp emp) throws Exception {
        empService.addEmp(emp);
        System.out.println("ဳٙ౮ۑ");
    }
}
<%@ page language="java" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>ާૡဳٙ</title>
  </head>
  <body>
  <form action="${pageContext.request.contextPath}/emp/register.action" 
method="POST">
    <table border="2" align="center">
      <tr>
        <th>ᖫݩ</th>
        <td><input type="text" name="id"></td>
      </tr>
      <tr>
        <th>নݷ</th>
        <td><input type="text" name="name"></td>
      </tr>
      <tr>
        <th>ᡈ࿜</th>
        <td><input type="text" name="sal"></td>
      </tr>
      <tr>
        <th>௔ڦ</th>
        <td>
          <input type="radio" name="sex" value="ካ"/>ካ
          <input type="radio" name="sex" value="ঀ" checked/>ঀ
        </td>
      </tr>
      <tr>
        <td colspan="2" align="center">
          <input type="submit" value="ဳٙ"/>
        </td>
      </tr>
    </table>
  </form>   
  </body>

---

2. ௛ᕮ
 
web.xmlے᫹Springᯈᗝ෈կ
Springᯈᗝ෈կᯈᗝහഝᬳള࿰҅SessionFactory̵Ԫۓ̵ಚൈဳᥴ
Mybatis௛ᯈᗝ෈կ̵ਫ֛զ݊ፘ੒ଫጱฉ੘෈կ
ਖ਼ฉ੘෈կےفک௛ᯈᗝ෈կӾ̶
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
Mybatisଉᥠᶎᦶ᷌
 
1. #{}޾${}ጱ܄ڦฎՋԍҘ
 
</html>

![三歪教你学Mybatis 第84页插图](../assets/images/三歪教你学Mybatis_p84_1_42ffcf91.jpeg)

![三歪教你学Mybatis 第84页插图](../assets/images/三歪教你学Mybatis_p84_2_3c233a1a.jpeg)

---

#{}޾${}ጱ܄ڦฎՋԍҘ
ࣁMybatisӾ҅ํӷᐿܛ֖ᒧ
#{} ᥴຉփ᭓ᬰ๶ጱ݇හහഝ
${}੒փ᭓ᬰ๶ጱ݇හܻ໏೪ളࣁSQLӾ
#{} ฎᶼᖫᦲ॒ቘ҅${}ฎਁᒧԀ๊ഘ̶
ֵአ#{}ݢզํපጱᴠྊSQLဳف҅൉ṛᔮᕹਞق௔̶
2.୮ਫ֛ᔄӾጱં௔ݷ޾ᤒӾጱਁྦྷݷӧӞ໏ ҅ெԍې Ҙ  
୮ਫ֛ᔄӾጱં௔ݷ޾ᤒӾጱਁྦྷݷӧӞ໏ ҅ெԍې Ҙ
ᒫ1ᐿғ ᭗ᬦࣁັᧃጱsql᧍ݙӾਧԎਁྦྷݷጱڦݷ҅ᦏਁྦྷݷጱڦݷ޾ਫ֛ᔄጱં௔ݷӞᛘ
ᒫ2ᐿғ ᭗ᬦ<resultMap> ๶ฉ੘ਁྦྷݷ޾ਫ֛ᔄં௔ݷጱӞӞ੒ଫጱىᔮ 
౯ᦊԅᒫԫᐿොୗտঅӞᅩ̶
3. ই֜឴ݐᛔۖኞ౮ጱ(Ԇ)Ძ꧊?
 
ই֜឴ݐᛔۖኞ౮ጱ(Ԇ)Ძ꧊?
ইຎ౯ժӞᛱൊفහഝጱᦾ҅ইຎ౯ժమᥝᎣ᭲ڟڟൊفጱහഝጱԆᲫฎग़੝҅౯ժݢզ᭗ᬦզӥጱො
ୗ๶឴ݐ
 
ᵱ࿢ғuser੒᨝ൊفکහഝପݸ҅ෛᦕ୯ጱԆᲫᥝ᭗ᬦuser੒᨝ᬬࢧ҅᭗ᬦuser឴ݐԆᲫ꧊̶
  <select id=”selectorder” parametertype=”int” 
resultetype=”me.gacl.domain.order”> 
       select order_id id, order_no orderno ,order_price price form orders 
where order_id=#{id}; 
    </select> 
 <select id="getOrder" parameterType="int" resultMap="orderresultmap">
        select * from orders where order_id=#{id}
    </select>
   <resultMap type=”me.gacl.domain.order” id=”orderresultmap”> 
        <!–አidં௔๶ฉ੘ԆᲫਁྦྷ–> 
        <id property=”id” column=”order_id”> 
        <!–አresultં௔๶ฉ੘ᶋԆᲫਁྦྷ҅propertyԅਫ֛ᔄં௔ݷ҅columnԅහഝᤒӾጱં௔–
> 
        <result property = “orderno” column =”order_no”/> 
        <result property=”price” column=”order_price” /> 
    </reslutMap>

---

ᥴ٬௏᪠ғ᭗ᬦLAST_INSERT_ID()឴ݐڟൊفᦕ୯ጱᛔीԆᲫ꧊҅ࣁinsert᧍ݙಗᤈݸ҅ಗᤈselect 
LAST_INSERT_ID()੪ݢզ឴ݐᛔीԆᲫ̶
mysql:
oracle:ਫሿ௏᪠ғضັᧃଧڜ஑کԆᲫ҅ਖ਼ԆᲫᦡᗝکuser੒᨝Ӿ҅ਖ਼user੒᨝ൊفහഝପ̶
Ԟݢզࣁselect ຽᓋӥٟզӥጱં௔ғ
4. ࣁmapperӾই֜փ᭓ग़ӻ݇හ?
 
ࣁmapperӾই֜փ᭓ग़ӻ݇හ?
ᒫӞᐿғֵአܛ֖ᒧጱ௏మ
ࣁฉ੘෈կӾֵአ#{0},#{1}դᤒփ᭓ᬰ๶ጱᒫپӻ݇හ
ֵአ@paramဳᥴ:๶޸ݷ݇හ 
#{0},#{1} ොୗ
  <insert id="insertUser" parameterType="cn.itcast.mybatis.po.User">
    <selectKey keyProperty="id" order="AFTER" resultType="int">
      select LAST_INSERT_ID()
    </selectKey>
    INSERT INTO USER(username,birthday,sex,address) VALUES(#{username},#
{birthday},#{sex},#{address})
  </insert>
  <!-- oracle
  ࣁಗᤈinsertԏڹಗᤈselect ଧڜ.nextval() from dualݐڊଧڜ๋य़꧊҅ਖ਼꧊ᦡᗝکuser੒
᨝ ጱidં௔
   -->
  <insert id="insertUser" parameterType="cn.itcast.mybatis.po.User">
    <selectKey keyProperty="id" order="BEFORE" resultType="int">
      select ଧڜ.nextval() from dual
    </selectKey>
    
    INSERT INTO USER(id,username,birthday,sex,address) VALUES( ଧڜ.nextval(),#
{username},#{birthday},#{sex},#{address})
  </insert> 
< select useGeneratedKeys="true" keyProperty="id"  keyColumn="id" />

---

@paramဳᥴොୗ
ᒫԫᐿғֵአMapᵞݳ֢ԅ݇හ๶ᤰ᫹
//੒ଫጱxml,#{0}դᤒളතጱฎdao੶ӾጱᒫӞӻ݇හ҅#{1}դᤒdao੶Ӿᒫԫ݇හ҅ๅग़݇හӞᛘஃݸ
ےܨݢ̶
<select id="selectUser"resultMap="BaseResultMap">  
    select *  fromuser_user_t   whereuser_name = #{0} anduser_area=#{1}  
</select>  
    public interface usermapper { 
         user selectuser(@param(“username”) string username, 
         @param(“hashedpassword”) string hashedpassword); 
        }
 <select id=”selectuser” resulttype=”user”> 
         select id, username, hashedpassword 
         from some_table 
         where username = #{username} 
         and hashedpassword = #{hashedpassword} 
    </select>
    try{
              //ฉ੘෈կጱ޸ݷᑮᳵ.SQLᇆྦྷጱID҅੪ݢզ᧣አ੒ଫጱฉ੘෈կӾጱSQL
              /**
               * ኧԭ౯ժጱ݇හ᩻ᬦԧӷӻ҅ᘒොဩӾݝํӞӻObject݇හතᵞ
               * ࢩྌ౯ժֵአMapᵞݳ๶ᤰ᫹౯ժጱ݇හ
               */
              Map<String, Object> map = new HashMap();
              map.put("start", start);
              map.put("end", end);
              return sqlSession.selectList("StudentID.pagination", map);
          }catch(Exception e){
              e.printStackTrace();
              sqlSession.rollback();
              throw e;
          }finally{
              MybatisUtil.closeSqlSession();
          }

---

5. Mybatisۖாsqlฎ؉ՋԍጱҘ᮷ํߺԶۖாsqlҘᚆᓌ
ᬿӞӥۖாsqlጱಗᤈܻቘӧҘ
 
Mybatisۖாsqlฎ؉ՋԍጱҘ᮷ํߺԶۖாsqlҘᚆᓌᬿӞӥۖாsqlጱಗᤈܻቘӧҘ
Mybatisۖாsqlݢզᦏ౯ժࣁXmlฉ੘෈կٖ҅զຽᓋጱ୵ୗᖫٟۖாsql҅ਠ౮᭦ᬋڣෙ޾ۖா
೪ളsqlጱۑᚆ̶
Mybatis൉׀ԧ9ᐿۖாsqlຽᓋғtrim|where|set|foreach|if|choose|when|otherwise|bind̶
ٌಗᤈܻቘԅֵ҅አOGNL՗sql݇හ੒᨝Ӿᦇᓒᤒᬡୗጱ꧊҅໑ഝᤒᬡୗጱ꧊ۖா೪ളsql҅զྌ
๶ਠ౮ۖாsqlጱۑᚆ̶
 
6. MybatisጱXmlฉ੘෈կӾ҅ӧݶጱXmlฉ੘෈կ҅id
ฎވݢզ᯿॔Ҙ
 
MybatisጱXmlฉ੘෈կӾ҅ӧݶጱXmlฉ੘෈կ҅idฎވݢզ᯿॔Ҙ
ইຎᯈᗝԧnamespaceᮎԍ୮ᆐฎݢզ᯿॔ጱ҅ࢩԅ౯ժጱStatementਫᴬӤ੪ฎnamespace+id
ইຎဌํᯈᗝnamespaceጱᦾ҅ᮎԍፘݶጱid੪տ੕ᛘᥟፍԧ̶
7. ԅՋԍ᧔Mybatisฎ܎ᛔۖORMฉ੘ૡٍҘਙӨقᛔۖ
ጱ܄ڦࣁߺ᯾Ҙ
 
ԅՋԍ᧔Mybatisฎ܎ᛔۖORMฉ੘ૡٍҘਙӨقᛔۖጱ܄ڦࣁߺ᯾Ҙ
HibernateંԭقᛔۖORMฉ੘ૡֵٍ҅አHibernateັᧃىᘶ੒᨝౲ᘏىᘶᵞݳ੒᨝෸҅ݢզ໑
ഝ੒᨝ىᔮཛྷࣳፗള឴ݐ҅ಅզਙฎقᛔۖጱ̶
ᘒMybatisࣁັᧃىᘶ੒᨝౲ىᘶᵞݳ੒᨝෸҅ᵱᥝಋۖᖫٟsql๶ਠ౮҅ಅզ҅ᑍԏԅ܎ᛔۖ
ORMฉ੘ૡ̶ٍ
8. ᭗ଉӞӻXmlฉ੘෈կ҅᮷տٟӞӻDaoളݗӨԏ੒
ଫ҅᧗ᳯ҅ᬯӻDaoളݗጱૡ֢ܻቘฎՋԍҘDaoളݗ᯾
ጱොဩ҅݇හӧݶ෸҅ොဩᚆ᯿᫹ހҘ
 
  <!--ړᶭັᧃ-->
  <select id="pagination" parameterType="map" resultMap="studentMap">
    /*໑ഝkeyᛔۖತک੒ଫMapᵞݳጱvalue*/
    select * from students limit #{start},#{end};
  </select>

---

᭗ଉӞӻXmlฉ੘෈կ҅᮷տٟӞӻDaoളݗӨԏ੒ଫ҅᧗ᳯ҅ᬯӻDaoളݗጱૡ֢ܻቘฎՋԍҘ
Daoളݗ᯾ጱොဩ҅݇හӧݶ෸҅ොဩᚆ᯿᫹ހҘ
Daoളݗ҅੪ฎՈժଉ᧔ጱMapperളݗ҅ളݗጱقᴴݷ҅੪ฎฉ੘෈կӾጱnamespaceጱ꧊҅ള
ݗጱොဩݷ҅੪ฎฉ੘෈կӾMappedStatementጱid꧊҅ളݗොဩٖጱ݇හ҅੪ฎփ᭓ᕳsqlጱ݇
හ̶
Mapperളݗฎဌํਫሿᔄጱ҅୮᧣አളݗොဩ෸҅ളݗقᴴݷ+ොဩݷ೪ളਁᒧԀ֢ԅkey꧊҅ݢ
ࠔӞਧ֖ӞӻMappedStatement
Ԉֺғ
Daoളݗ᯾ጱොဩ҅ฎӧᚆ᯿᫹ጱ҅ࢩԅฎقᴴݷ+ොဩݷጱכਂ޾੔ತᒽኼ̶
Daoളݗጱૡ֢ܻቘฎJDKۖாդቘ҅Mybatisᬩᤈ෸տֵአJDKۖாդቘԅDaoളݗኞ౮դቘproxy੒
᨝҅դቘ੒᨝proxyտೝ౼ളݗොဩ҅᫨ᘒಗᤈMappedStatementಅդᤒጱsql҅ᆐݸਖ਼sqlಗᤈᕮຎ
ᬬࢧ̶
ᧇఘݢ݇ᘍғ
https://www.cnblogs.com/soundcode/p/6497291.html
9. MybatisྲIBatisྲ᫾य़ጱپӻදᬰฎՋԍ
 
MybatisྲIBatisྲ᫾य़ጱپӻදᬰฎՋԍ
a.ํളݗᕬਧ,۱ೡဳᥴᕬਧsql޾xmlᕬਧSql ,
b.ۖாsqlኧܻ๶ጱᜓᅩᯈᗝݒ౮OGNLᤒᬡୗ,
c. ࣁӞ੒Ӟ,Ӟ੒ग़ጱ෸ײ୚ᬰԧassociation,ࣁӞ੒ग़ጱ෸ײ୚فԧcollectionᜓᅩ,ӧᬦ᮷ฎࣁ
resultMap᯾ᶎᯈᗝ
10. ളݗᕬਧํپᐿਫሿොୗ,ړڦฎெԍਫሿጱ?
 
ളݗᕬਧํپᐿਫሿොୗ,ړڦฎெԍਫሿጱ?
ളݗᕬਧํӷᐿਫሿොୗғ
Ӟᐿฎ᭗ᬦဳᥴᕬਧ,੪ฎࣁളݗጱොဩӤᶎےӤ@Select@Updateᒵဳᥴ᯾ᶎ۱ތSql᧍ݙ๶ᕬਧ
ݚक़Ӟᐿ੪ฎ᭗ᬦxml᯾ᶎٟSQL๶ᕬਧ,ࣁᬯᐿఘ٭ӥ,ᥝ೰ਧxmlฉ੘෈կ᯾ᶎጱnamespace஠
ᶳԅളݗጱق᪠ஆݷ.
11. Mybatisฎই֜ᬰᤈړᶭጱҘړᶭൊկጱܻቘฎՋ
ԍҘ
 
com.mybatis3.mappers.StudentDao.findStudentById҅
ݢզࠔӞತکnamespaceԅcom.mybatis3.mappers.StudentDaoӥᶎid = findStudentByIdጱ
MappedStatement̶ࣁMybatisӾ҅ྯӞӻ<select>̵<insert>̵<update>̵<delete>ຽᓋ҅᮷
տᤩᥴຉԅӞӻMappedStatement੒᨝̶

---

Mybatisฎই֜ᬰᤈړᶭጱҘړᶭൊկጱܻቘฎՋԍҘ
MybatisֵአRowBounds੒᨝ᬰᤈړᶭ҅ਙฎᰒ੒ResultSetᕮຎᵞಗᤈጱٖਂړᶭ҅ᘒᶋᇔቘړᶭ҅
ݢզࣁsqlٖፗളԡٟଃํᇔቘړᶭጱ݇හ๶ਠ౮ᇔቘړᶭۑᚆ҅Ԟݢզֵአړᶭൊկ๶ਠ౮ᇔቘړᶭ̶
ړᶭൊկጱच๜ܻቘฎֵአMybatis൉׀ጱൊկളݗ҅ਫሿᛔਧԎൊկ҅ࣁൊկጱೝ౼ොဩٖೝ౼இಗ
ᤈጱsql҅ᆐݸ᯿ٟsql҅໑ഝdialectො᥺҅Ⴒے੒ଫጱᇔቘړᶭ᧍ݙ޾ᇔቘړᶭ݇හ̶
Ԉֺғ select * from student҅ೝ౼sqlݸ᯿ٟԅғselect t.* from ҁselect * from 
student҂t limit 0҅10
ړᶭൊկֵአ݇ᘍᩒාғ
https://www.cnblogs.com/kangoroo/p/7998433.html
http://blog.csdn.net/yuchao2015/article/details/55001182
https://www.cnblogs.com/ljdblog/p/6725094.html
12. ᓌᬿMybatisጱൊկᬩᤈܻቘ҅զ݊ই֜ᖫٟӞӻൊ
կ
 
ᓌᬿMybatisጱൊկᬩᤈܻቘ҅զ݊ই֜ᖫٟӞӻൊկ
MybatisՐݢզᖫٟᰒ੒ParameterHandler̵ResultSetHandler̵StatementHandler̵
Executorᬯ4ᐿളݗጱൊկ҅MybatisֵአJDKጱۖாդቘ҅ԅᵱᥝೝ౼ጱളݗኞ౮դቘ੒᨝զਫሿള
ݗොဩೝ౼ۑᚆ҅ྯ୮ಗᤈᬯ4ᐿളݗ੒᨝ጱොဩ෸҅੪տᬰفೝ౼ොဩٍ֛҅੪ฎInvocationHandler
ጱinvoke()ොဩ҅୮ᆐ҅ݝտೝ౼ᮎԶ֦೰ਧᵱᥝೝ౼ጱොဩ̶
ਫሿMybatisጱInterceptorളݗଚٟ॔intercept()ොဩ҅ᆐݸࣁᕳൊկᖫٟဳᥴ҅೰ਧᥝೝ౼ߺӞӻള
ݗጱߺԶොဩܨݢ҅ᦕ֘҅ڦ஫ԧࣁᯈᗝ෈կӾᯈᗝ֦ᖫٟጱൊկ̶
13. Mybatisฎވඪ೮୊᬴ے᫹Ҙইຎඪ೮҅ਙጱਫሿܻ
ቘฎՋԍҘ
 
Mybatisฎވඪ೮୊᬴ے᫹Ҙইຎඪ೮҅ਙጱਫሿܻቘฎՋԍҘ
MybatisՐඪ೮associationىᘶ੒᨝޾collectionىᘶᵞݳ੒᨝ጱ୊᬴ے᫹҅association೰ጱ੪ฎӞ੒
Ӟ҅collection೰ጱ੪ฎӞ੒ग़ັᧃ̶ࣁMybatisᯈᗝ෈կӾ҅ݢզᯈᗝฎވސአ୊᬴ے᫹
lazyLoadingEnabled=true|false̶
ਙጱܻቘฎֵ҅አCGLIBڠୌፓຽ੒᨝ጱդቘ੒᨝҅୮᧣አፓຽොဩ෸҅ᬰفೝ౼࢏ොဩ҅ྲই᧣አ
a.getB().getName()҅ೝ౼࢏invoke()ොဩݎሿa.getB()ฎnull꧊҅ᮎԍ੪տܔᇿݎᭆԪضכਂঅጱັᧃ
ىᘶB੒᨝ጱsql҅಩BັᧃӤ๶҅ᆐݸ᧣አa.setB(b)҅ԭฎaጱ੒᨝bં௔੪ํ꧊ԧ҅ള፳ਠ౮
a.getB().getName()ොဩጱ᧣አ̶ᬯ੪ฎ୊᬴ے᫹ጱच๜ܻቘ̶
୮ᆐԧ҅ӧطฎMybatis҅پԒಅํጱ۱ೡHibernate҅ඪ೮୊᬴ے᫹ጱܻቘ᮷ฎӞ໏ጱ̶
14. Mybatis᮷ํߺԶExecutorಗᤈ࢏Ҙਙժԏᳵጱ܄ڦ
ฎՋԍҘ
 
Mybatis᮷ํߺԶExecutorಗᤈ࢏Ҙਙժԏᳵጱ܄ڦฎՋԍҘ

---

Mybatisํӣᐿच๜ጱExecutorಗᤈ࢏҅SimpleExecutor̵ReuseExecutor̵BatchExecutor̶
SimpleExecutorғྯಗᤈӞེupdate౲select҅੪୏ސӞӻStatement੒᨝҅አਠᒈڰىᳮ
Statement੒᨝̶
ReuseExecutorғಗᤈupdate౲select҅զsql֢ԅkeyັತStatement੒᨝҅ਂࣁ੪ֵአ҅ӧਂࣁ
੪ڠୌ҅አਠݸ҅ӧىᳮStatement੒᨝҅ᘒฎනᗝԭMap<String, Statement>ٖ҅׀ӥӞֵེ
አ̶ᓌ᥺ԏ҅੪ฎ᯿ֵ॔አStatement੒᨝̶
BatchExecutorғಗᤈupdateҁဌํselect҅JDBCಢ॒ቘӧඪ೮select҂҅ਖ਼ಅํsql᮷Ⴒےکಢ॒
ቘӾҁaddBatch()҂҅ᒵஇᕹӞಗᤈҁexecuteBatch()҂҅ਙᖨਂԧग़ӻStatement੒᨝҅ྯӻ
Statement੒᨝᮷ฎaddBatch()ਠླݸ҅ᒵஇ᭑ӞಗᤈexecuteBatch()ಢ॒ቘ̶ӨJDBCಢ॒ቘ
ፘݶ̶
֢አ᝜ࢱғExecutorጱᬯԶᇙᅩ҅᮷Ӹ໒ᴴګࣁSqlSessionኞ޸ޮ๗᝜ࢱ̶ٖ
15. MyBatisӨHibernateํߺԶӧݶҘ
 
MyBatisӨHibernateํߺԶӧݶҘ
Mybatis޾hibernateӧݶ҅ਙӧਠقฎӞӻORM໛ຝ҅ࢩԅMyBatisᵱᥝᑕଧާᛔ૩ᖫٟSql᧍ݙ҅ӧ
ᬦmybatisݢզ᭗ᬦXML౲ဳᥴොୗᅎၚᯈᗝᥝᬩᤈጱsql᧍ݙ҅ଚਖ਼java੒᨝޾sql᧍ݙฉ੘ኞ౮๋ᕣಗ
ᤈጱsql๋҅ݸਖ਼sqlಗᤈጱᕮຎٚฉ੘ኞ౮java੒᨝̶ 
Mybatis਍ԟᳪད֗҅ᓌܔฃ਍҅ᑕଧާፗളᖫٟܻኞாsql҅ݢӸ໒ഴګsqlಗᤈ௔ᚆ҅ᅎၚଶṛ҅ᶋଉ
ᭇݳ੒ىᔮහഝཛྷࣳᥝ࿢ӧṛጱ᫫կ୏ݎֺ҅ই԰ᘶᗑ᫫կ̵մӱᬩ០ᔄ᫫կᒵ҅ࢩԅᬯᔄ᫫կᵱ࿢ݒ
۸᷇ᔺ҅Ӟ֕ᵱ࿢ݒ۸ᥝ࿢౮ຎᬌڊᬥ᭛̶֕ฎᅎၚጱڹ൉ฎmybatis෫ဩ؉کහഝପ෫ى௔҅ইຎᵱ
ᥝਫሿඪ೮ग़ᐿහഝପጱ᫫կڞᵱᥝᛔਧԎग़ॺsqlฉ੘෈կ҅ૡ֢ᰁय̶़ 
Hibernate੒᨝/ىᔮฉ੘ᚆێ୩҅හഝପ෫ى௔অ҅੒ԭىᔮཛྷࣳᥝ࿢ṛጱ᫫կҁֺইᵱ࿢ࢴਧጱਧګ
۸᫫կ҂ইຎአhibernate୏ݎݢզᜓ፜உग़դᎱ҅൉ṛපሲ̶֕ฎHibernateጱᗌᅩฎ਍ԟᳪདṛ҅ᥝ
ᔜ᭗ᳪདๅṛ҅ᘒӬெԍᦡᦇO/Rฉ੘҅ࣁ௔ᚆ޾੒᨝ཛྷࣳԏᳵই֜๦ᤍ҅զ݊ெ໏አঅHibernateᵱ
ᥝٍํஉ୩ጱᕪḵ޾ᚆێ಍ᤈ̶ 
௛ԏ҅ೲᆙአಁጱᵱ࿢ࣁํᴴጱᩒრሾहӥݝᥝᚆ؉ڊᖌಷ௔̵ಘ઀௔ᜉঅጱ᫫կຝ຅᮷ฎঅຝ຅҅ಅ
զ໛ຝݝํᭇݳ಍ฎ๋অ̶

![三歪教你学Mybatis 第91页插图](../assets/images/三歪教你学Mybatis_p91_1_42ffcf91.jpeg)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y

![三歪教你学Mybatis 第92页插图](../assets/images/三歪教你学Mybatis_p92_1_3c233a1a.jpeg)