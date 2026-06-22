---
title: 三歪教你学JDBC
source: Java3y/基础知识原创电子书/JDBC电子书/三歪教你学JDBC.pdf
pages: 64
converted_at: 2026-06-22 22:29:28
---

# 三歪教你学JDBC

ڹ᥺
JDBCفᳪ
1.ՋԍฎJDBC
2.ԅՋԍ౯ժᥝአJDBC
3.ᓌܔ඙֢JDBC
4.Connection੒᨝
5.Statement੒᨝
6.ResultSet੒᨝
7.ٟӞӻᓌܔૡٍᔄ
JDBCֵአጱӞԶᕡᜓ
1.PreparedStatement੒᨝
2.ಢ॒ቘ
3.॒ቘय़෈๜޾ԫᬰګහഝ
3.1 MYSQL
3.2 Oracle
4.឴ݐහഝପጱᛔۖԆᲫڜ
4.1 ԅՋԍᥝ឴ݐහഝପጱᛔۖԆᲫڜහഝ?
5.᧣አහഝପጱਂؙᬦᑕ
Ԫۓ+زහഝ+ද᭜ૡٍᔄ
1.Ԫۓ
1.1 savapoint
1.2 Ԫۓጱᵍᐶᕆڦ
2.زහഝ
2.1 Ջԍฎزහഝ
2.2 ԅՋԍ౯ժᥝአزහഝ
3.ද᭜JDBCૡٍᔄ
3.1 ीڢද
3.2 ັᧃ
හഝପᬳള࿰+DBUtils+ړᶭ
1.හഝପᬳള࿰
1.1Ջԍฎහഝପᬳള࿰
1.2ԅՋԍ౯ժᥝֵአහഝପᬳള࿰
1.3ই֜ᛔ૩ᖫٟӞӻᬳള࿰
1.4DBCP
1.5 C3P0
1.6 Tomcatහഝრ
1.7 Druid
2. ֵአdbutils໛ຝ
2.1DbUtilsᔄ
2.2QueryRunnerᔄ
2.3ResultSetHandlerളݗ
3.ړᶭ
3.1Oracleਫሿړᶭ
3.2Mysqlਫሿړᶭ
3.3ֵአJDBCᬳളහഝପਫሿړᶭ
ᶎᦶ᷌
1. JDBC඙֢හഝପጱྍṈ Ҙ

---

2. JDBCӾጱStatement ޾PreparedStatement҅CallableStatementጱ܄ڦҘ
3. JDBCӾय़හഝᰁጱړᶭᥴ٬ොဩ?
4. ᧔᧔හഝପᬳള࿰ૡ֢ܻቘ޾ਫሿොໜҘ
5. JavaӾই֜ᬰᤈԪۓጱ॒ቘ?
6. ץදJDBCդᎱᨶᰁ
7. ٟڊӞྦྷJDBCᬳള๜๢MySQLහഝପጱդᎱ
8. JDBCฎই֜ਫሿJavaᑕଧ޾JDBCḝۖጱຂᘠݳጱҘ
9. execute҅executeQuery҅executeUpdateጱ܄ڦฎՋԍҘ
10. PreparedStatementጱᗌᅩฎՋԍ҅ெԍᥴ٬ᬯӻᳯ᷌Ҙ
11. JDBCጱᚍ᧛ฎՋԍҘߺᐿහഝପᵍᐶᕆڦᚆᴠྊᚍ᧛Ҙ
12. Ջԍฎଝ᧛҅ߺᐿᵍᐶᕆڦݢզᴠྊଝ᧛Ҙ
13. JDBCጱDriverManagerฎአ๶؉ՋԍጱҘ
14. JDBCጱResultSetฎՋԍҘ
15. ํߺԶӧݶጱResultSetҘ
16. JDBCጱDataSourceฎՋԍ҅ํՋԍঅ॒
17 .ই֜᭗ᬦJDBCጱDataSource޾Apache TomcatጱJNDI๶ڠୌᬳള࿰Ҙ
18. ApacheጱDBCPฎՋԍҘ
19. ଉᥠጱJDBC୑ଉํߺԶҘ
20. JDBCӾਂࣁߺԶӧݶᔄࣳጱᲁҘ
21. java.util.Date޾java.sql.DateํՋԍ܄ڦҘ
22. SQLWarningฎՋԍ҅ࣁᑕଧӾই֜឴ݐSQLWarningҘ
23. ইຎjava.sql.SQLException: No suitable driver foundᧆெԍېҘ
24. JDBCጱRowSetฎՋԍ҅ํߺԶӧݶጱRowSetҘ
25. ՋԍฎJDBCጱ๋֯ਫ᪢Ҙ
 
ڹ᥺
 
ᬯӻ෈໩ጱٖ਻ᕍಋ಑҅ইຎమᥝ፡ๅग़ጱଗᨵ෈ᒍ҅ىဳ౯ጱلռݩғJava3y̶ํๅग़ጱܻڠದ๞෈
ᒍ޾ଗᨵѺ
 
ፓڹዙᇰ॒ԭዙᇰๅෛPDFӾ҅ݝᥝฎJavaݸᒒጱᎣᦩ҅᮷տํѺཻᬨ๶౯لռݩ؛ๅѺஙמ൤
ᔱғJava3y
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺلռݩํ౯ጱᘶᔮොୗ

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
 
 
 
JDBCفᳪ

![三歪教你学JDBC 第3页插图](../assets/images/三歪教你学JDBC_p3_1_46627a5a.jpeg)

![三歪教你学JDBC 第3页插图](../assets/images/三歪教你学JDBC_p3_2_a7b96e96.jpeg)

![三歪教你学JDBC 第3页插图](../assets/images/三歪教你学JDBC_p3_3_3c233a1a.jpeg)

![三歪教你学JDBC 第3页插图](../assets/images/三歪教你学JDBC_p3_4_08125413.png)

---

1.ՋԍฎJDBC
 
JDBCقᑍԅғJava Data Base Connectivity,ਙฎݢզಗᤈSQL᧍ݙጱJava API
2.ԅՋԍ౯ժᥝአJDBC
 
૱ᶎӤํᶋଉग़ጱහഝପ҅๜๶౯ժฎᵱᥝ໑ഝӧݶጱහഝପ਍ԟӧݶጱAPI҅sunلݪԅԧᓌ۸
ᬯӻ඙֢҅ਧԎԧJDBC API̓ളݗ̈́
sunلݪݝฎ൉׀ԧJDBC API̓ളݗ̈́҅හഝପܯࠟᨮᨱਫሿ̶
੒ԭ౯ժ๶᧔҅඙֢හഝପ᮷ฎࣁJDBC API̓ളݗ̈́Ӥֵ҅አӧݶጱහഝପ҅ݝᥝአහഝପܯࠟ
൉׀ጱහഝପḝۖᑕଧܨݢ
ᬯय़य़ᓌ۸ԧ౯ժጱ਍ԟ౮๜
3.ᓌܔ඙֢JDBC
 
ྍṈ:
1. ੕فMySQL౲ᘏOracleḝۖ۱
2. ᤰ᫹හഝପḝۖᑕଧ
3. ឴ݐکӨහഝପᬳള
4. ឴ݐݢզಗᤈSQL᧍ݙጱ੒᨝
5. ಗᤈSQL᧍ݙ
6. ىᳮᬳള
 
        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;
        try {
            /*
            * ے᫹ḝۖํӷᐿොୗ
            *
            * 1ғտ੕ᛘḝۖտဳٙӷེ҅ᬦଶׁᩢԭmysqlጱapi҅ᚙᐶጱmysqlጱ୏ݎ۱҅ᑕଧڞ
෫ဩᖫᦲ
            * 2ғḝۖݝտے᫹Ӟེ҅ӧᵱᥝׁᩢٍ֛ጱḝۖ҅ᅎၚ௔ṛ
            *
            * ౯ժӞᛱ᮷ฎֵአᒫԫᐿොୗ
            * */
            //1.
            //DriverManager.registerDriver(new com.mysql.jdbc.Driver());
            //2.
            Class.forName("com.mysql.jdbc.Driver");

---

//឴ݐӨහഝପᬳളጱ੒᨝-Connetcion
            connection = 
DriverManager.getConnection("jdbc:mysql://localhost:3306/zhongfucheng", 
"root", "root");
            //឴ݐಗᤈsql᧍ݙጱstatement੒᨝
            statement = connection.createStatement();
            //ಗᤈsql᧍ݙ,೭کᕮຎᵞ
            resultSet = statement.executeQuery("SELECT * FROM users");
            //᭭ܲᕮຎᵞ҅஑کහഝ
            while (resultSet.next()) {
                System.out.println(resultSet.getString(1));
                System.out.println(resultSet.getString(2));
            }
            
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            /*
            * ىᳮᩒრ҅ݸ᧣አጱضىᳮ
            *
            * ىᳮԏڹ҅ᥝڣෙ੒᨝ฎވਂࣁ
            * */
            if (resultSet != null) {
                try {
                    resultSet.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (statement != null) {
                try {
                    statement.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (connection != null) {
                try {

---

Ӥᶎ౯ժ૪ᕪᓌܔֵአJDBC݄ັᧃහഝପጱහഝԧ҅ളӥ๶౯ժ݄ԧᥴӞӥӤᶎդᎱአکጱ੒᨝
4.Connection੒᨝
 
ਮಁᒒӨහഝପಅํጱԻ԰᮷ฎ᭗ᬦConnection๶ਠ౮ጱ̶
ଉአጱොဩғ
 
                    connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
//ڠୌݻහഝପݎᭆsqlጱstatement੒᨝̶
createcreateStatement()
//ڠୌݻහഝପݎᭆᶼᖫᦲsqlጱPrepareSatement੒᨝̶
prepareStatement(sql) 
//ڠୌಗᤈਂؙᬦᑕጱcallableStatement੒᨝
prepareCall(sql)
//ᦡᗝԪۓᛔۖ൉Ի
setAutoCommit(boolean autoCommit)
//൉ԻԪۓ
commit()
//ࢧ჻Ԫۓ
rollback()

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
5.Statement੒᨝
 
Statement੒᨝አԭݻහഝପݎᭆSql᧍ݙ҅੒හഝପጱीڢදັ᮷ݢզ᭗ᬦྌ੒᨝ݎᭆsql᧍ݙਠ౮̶
Statement੒᨝ጱଉአොဩғ
//ັᧃ
executeQuery(String sql)
//ीڢද
executeUpdate(String sql)
//ձ఺sql᧍ݙ᮷ݢզ҅֕ฎፓຽӧกᏟ҅உ੝አ
execute(String sql)

![三歪教你学JDBC 第7页插图](../assets/images/三歪教你学JDBC_p7_1_9759acba.png)

![三歪教你学JDBC 第7页插图](../assets/images/三歪教你学JDBC_p7_2_3c233a1a.jpeg)

---

6.ResultSet੒᨝
 
ResultSet੒᨝դᤒSql᧍ݙጱಗᤈᕮຎ҅୮Statement੒᨝ಗᤈexecuteQuery()෸҅տᬬࢧӞӻ
ResultSet੒᨝
ResultSet੒᨝ᖌಷԧӞӻහഝᤈጱ჋ຽ̓ᓌܔቘᥴ౮೰ᰒ̈́҅᧣አResultSet.next()ොဩ҅ݢզᦏ჋ຽ
೰ݻٍ֛ጱහഝᤈ҅ᬰᤈ឴ݐᧆᤈጱහഝ
 
ଉአොဩғ
7.ٟӞӻᓌܔૡٍᔄ
 
//಩ग़๵ጱsql᧍ݙනᬰݶӞӻಢ॒ቘӾ
addBatch(String sql)
//ݻහഝପݎᭆӞಢsql᧍ݙಗᤈ
executeBatch()
//឴ݐձ఺ᔄࣳጱහഝ
getObject(String columnName)
//឴ݐ೰ਧᔄࣳጱහഝ̓ݱᐿᔄࣳ҅ັ፡APḮ
getString(String columnName)
//੒ᕮຎᵞᬰᤈ჻ۖັ፡ጱොဩ
next()
Previous()
absolute(int row)
beforeFirst()
afterLast()

---

᭗ᬦӤᶎጱቘᥴ҅౯ժ૪ᕪᚆड़ֵአJDBC੒හഝପጱහഝᬰᤈीڢදັԧ҅౯ժݎሿ҅෫ᦞीڢදັ᮷
ᵱᥝᬳളහഝପ҅ىᳮᩒრ҅ಅզ౯ժ಩ᬳളහഝପ҅᯽නᩒრጱ඙֢ುݐکӞӻૡٍᔄ
    /*
    * ᬳളහഝପጱdriver҅url҅username҅password᭗ᬦᯈᗝ෈կ๶ᯈᗝ҅ݢզीےᅎၚ௔
    * ୮౯ժᵱᥝڔഘහഝପጱ෸ײ҅ݝᵱᥝࣁᯈᗝ෈կӾදզӤጱמ௳ܨݢ
    *
    * */
    private static String  driver = null;
    private static String  url = null;
    private static String  username = null;
    private static String password = null;
    static {
        try {
            //឴ݐᯈᗝ෈կጱ᧛فၞ
            InputStream inputStream = 
UtilsDemo.class.getClassLoader().getResourceAsStream("db.properties");
            Properties properties = new Properties();
            properties.load(inputStream);
            //឴ݐᯈᗝ෈կጱמ௳
            driver = properties.getProperty("driver");
            url = properties.getProperty("url");
            username = properties.getProperty("username");
            password = properties.getProperty("password");
            //ے᫹ḝۖᔄ
            Class.forName(driver);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url,username,password);
    }
    public static void release(Connection connection, Statement statement, 
ResultSet resultSet) {
        
        if (resultSet != null) {

---

try {
                resultSet.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (statement != null) {
            try {
                statement.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (connection != null) {
            try {
                connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

![三歪教你学JDBC 第10页插图](../assets/images/三歪教你学JDBC_p10_1_2a13ce9e.jpeg)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
JDBCֵአጱӞԶᕡᜓ
 
 
1.PreparedStatement੒᨝
 
PreparedStatement੒᨝ᖀಥStatement੒᨝҅ਙྲStatement੒᨝ๅ୩य़ֵ҅አ᩸๶ๅᓌܔ
1. Statement੒᨝ᖫᦲSQL᧍ݙ෸҅ইຎSQL᧍ݙํݒᰁ҅੪ᵱᥝֵአړᵍᒧ๶ᵍ୏҅ইຎݒᰁᶋଉ
ग़҅੪տֵSQLݒ஑ᶋଉ॔๥̶PreparedStatementݢզֵአܛ֖ᒧ҅ᓌ۸sqlጱᖫٟ
2. Statementտ᷇ᔺᖫᦲSQL̶PreparedStatementݢ੒SQLᬰᤈᶼᖫᦲ҅൉ṛපሲ҅ᶼᖫᦲጱ
SQLਂؙࣁPreparedStatement੒᨝Ӿ
3. PreparedStatementᴠྊSQLဳف̶̓Statement᭗ᬦړᵍᒧ'++',ᖫٟ࿞ᒵୗ҅ݢզӧᵱᥝੂᎱ
੪ᬰفහഝପ̈́
        //ཛྷ೙ັᧃidԅ2ጱמ௳
        String id = "2";
        Connection connection = UtilsDemo.getConnection();
        String sql = "SELECT * FROM users WHERE id = ?";
        PreparedStatement preparedStatement = 
connection.preparedStatement(sql);
        //ᒫӞӻ݇හᤒᐏᒫپӻܛ֖ᒧ̓Ԟ੪ฎ?ݩ̈́҅ᒫԫӻ݇හᤒᐏ꧊ฎग़੝
        preparedStatement.setString(1,id);
        ResultSet resultSet = preparedStatement.executeQuery();

![三歪教你学JDBC 第11页插图](../assets/images/三歪教你学JDBC_p11_1_3c233a1a.jpeg)

---

2.ಢ॒ቘ
 
୮ᵱᥝݻහഝପݎᭆӞಢSQL᧍ݙಗᤈ෸҅ଫ᭿عݻහഝପӞ๵๵ݎᭆಗᤈ҅᯻አಢ॒ቘզ൉܋ಗᤈප
ሲ
ಢ॒ቘํӷᐿොୗғ
1. Statement
2. PreparedStatement
᭗ᬦexecuteBath()ොဩಢᰁ॒ቘಗᤈSQL᧍ݙ҅ᬬࢧӞӻint[]හᕟ҅ᧆහᕟդᤒݱݙSQLጱᬬࢧ꧊
 
զӥդᎱฎզStatementොୗਫሿಢ॒ቘ
        if (resultSet.next()) {
            System.out.println(resultSet.getString("name"));
        }
        //᯽නᩒრ
        UtilsDemo.release(connection, preparedStatement, resultSet);
        /*
        * Statementಗᤈಢ॒ቘ
        *
        * սᅩғ
        *       ݢզݻහഝପݎᭆӧݶጱSQL᧍ݙ
        * ᗌᅩғ
        *       SQLဌํᶼᖫᦲ
        *       Ր݇හӧݶጱSQL҅ᵱᥝ᯿ٟ॔ग़๵SQL
        * */
        Connection connection = UtilsDemo.getConnection();
        Statement statement = connection.createStatement();
        String sql1 = "UPDATE users SET name='zhongfucheng' WHERE id='3'";
        String sql2 = "INSERT INTO users (id, name, password, email, 
birthday)" +
                " VALUES('5','nihao','123','ss@qq.com','1995-12-1')";
        //ਖ਼sqlႲےکಢ॒ቘ
        statement.addBatch(sql1);
        statement.addBatch(sql2);
        //ಗᤈಢ॒ቘ
        statement.executeBatch();

---

զӥොୗզPreparedStatementොୗਫሿಢ॒ቘ
        //Ⴔᑮಢ॒ቘጱsql
        statement.clearBatch();
        UtilsDemo.release(connection, statement, null);
        /*
        * PreparedStatementಢ॒ቘ
        *   սᅩғ
        *       SQL᧍ݙᶼᖫᦲԧ
        *       ੒ԭݶӞᐿᔄࣳጱSQL᧍ݙ҅ӧአᖫٟஉग़๵
        *   ᗌᅩғ
        *       ӧᚆݎᭆӧݶᔄࣳጱSQL᧍ݙ
        *
        * */
        Connection connection = UtilsDemo.getConnection();
        String sql = "INSERT INTO test(id,name) VALUES (?,?)";
        PreparedStatement preparedStatement = 
connection.prepareStatement(sql);
        for (int i = 1; i <= 205; i++) {
            preparedStatement.setInt(1, i);
            preparedStatement.setString(2, (i + "zhongfucheng"));
            //Ⴒےکಢ॒ቘӾ
            preparedStatement.addBatch();
            if (i %2 ==100) {
                //ಗᤈಢ॒ቘ
                preparedStatement.executeBatch();
                //Ⴔᑮಢ॒ቘ̓ইຎහഝᰁॡय़҅ಅํහഝਂفಢ॒ቘٖ҅ਂᙗਧფڊ̈́
                preparedStatement.clearBatch();
            }
        }
        //ӧฎಅํጱ%2==100҅ۃӥጱٚಗᤈӞེಢ॒ቘ
        preparedStatement.executeBatch();
        //ٚႴᑮ
        preparedStatement.clearBatch();
        UtilsDemo.release(connection, preparedStatement, null);

---

3.॒ቘय़෈๜޾ԫᬰګහഝ
 
clob޾blob
clobአԭਂؙय़෈๜
blobአԭਂؙԫᬰګහഝ
 
3.1 MYSQL
 
MySQLਂؙय़෈๜ฎአTest̓դ๊clob̈́҅Test݈ړԅ4ᔄ
TINYTEXT
TEXT
MEDIUMTEXT
LONGTEXT 
ݶቘblobԞํᬯ4ᔄ
 
ӥᶎአJDBCᬳളMySQLහഝପ݄඙֢य़෈๜හഝ޾ԫᬰګහഝ
/*
*አJDBC඙֢MySQLහഝପ݄඙֢य़෈๜හഝ
*
*setCharacterStream(int parameterIndex,java.io.Reader reader,long length)
*ᒫԫӻ݇හളතጱฎӞӻၞ੒᨝҅ࢩԅय़෈๜ӧଫᧆአString๶ളත҅Stringॡय़տ੕ᛘٖਂფڊ
*ᒫӣӻ݇හളතጱฎ෈կጱय़ੜ
*
* */
public class Demo5 {
    @Test
    public void add() {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;

---

try {
            connection = JdbcUtils.getConnection();
            String sql = "INSERT INTO test2 (bigTest) VALUES(?) ";
            preparedStatement = connection.prepareStatement(sql);
            //឴ݐک෈կጱ᪠ஆ
            String path = 
Demo5.class.getClassLoader().getResource("BigTest").getPath();
            File file = new File(path);
            FileReader fileReader = new FileReader(file);
            //ᒫӣӻ݇හ҅ኧԭၥᦶጱMysqlᇇ๜ᬦ֗҅ಅզݝᚆአintᔄࣳጱ̶ṛᇇ๜ጱӧᵱᥝᬰᤈ
୩᫨
            preparedStatement.setCharacterStream(1, fileReader, (int) 
file.length());
            if (preparedStatement.executeUpdate() > 0) {
                System.out.println("ൊف౮ۑ");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(connection, preparedStatement, null);
        }
    }
    /*
    * ᧛ݐय़෈๜හഝ҅᭗ᬦResultSetӾጱgetCharacterStream()឴ݐၞ੒᨝හഝ
    * 
    * */
    @Test
    public void read() {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        try {
            connection = JdbcUtils.getConnection();
            String sql = "SELECT * FROM test2";
            preparedStatement = connection.prepareStatement(sql);
            resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {

---

Reader reader = resultSet.getCharacterStream("bigTest");
                FileWriter fileWriter = new FileWriter("d:\\abc.txt");
                char[] chars = new char[1024];
                int len = 0;
                while ((len = reader.read(chars)) != -1) {
                    fileWriter.write(chars, 0, len);
                    fileWriter.flush();
                }
                fileWriter.close();
                reader.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(connection, preparedStatement, resultSet);
        }
        
    }
/*
* ֵአJDBCᬳളMYsqlහഝପ඙֢ԫᬰګහഝ
* ইຎ౯ժᥝአහഝପਂؙӞӻय़ᥤ᷇ጱ෸ײ҅හഝପฎਂؙӧکጱ̶
* ᵱᥝᦡᗝmax_allowed_packet҅Ӟᛱ౯ժӧֵአහഝପ݄ਂؙӞӻᥤ᷇
* */
public class Demo6 {
    @Test
    public void add() {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        try {
            connection = JdbcUtils.getConnection();
            String sql = "INSERT INTO test3 (blobtest) VALUES(?)";
            preparedStatement = connection.prepareStatement(sql);

---

//឴ݐ෈կጱ᪠ஆ޾෈կ੒᨝
            String path = 
Demo6.class.getClassLoader().getResource("1.wmv").getPath();
            File file = new File(path);
            //᧣አොဩ
            preparedStatement.setBinaryStream(1, new FileInputStream(path), 
(int)file.length());
            if (preparedStatement.executeUpdate() > 0) {
                System.out.println("Ⴒے౮ۑ");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(connection, preparedStatement, null);
        }
    }
    @Test
    public void read() {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        try {
            connection = JdbcUtils.getConnection();
            String sql = "SELECT * FROM test3";
            preparedStatement = connection.prepareStatement(sql);
            resultSet = preparedStatement.executeQuery();
            //ইຎ᧛ݐکහഝ҅੪಩හഝٟکᏺፏӥ
            if (resultSet.next()) {
                InputStream inputStream = 
resultSet.getBinaryStream("blobtest");
                FileOutputStream fileOutputStream = new 
FileOutputStream("d:\\aa.jpg");
                int len = 0;

---

3.2 Oracle
 
ӥᶎአJDBCᬳളOracleහഝପ݄඙֢य़෈๜හഝ޾ԫᬰګහഝ
                byte[] bytes = new byte[1024];
                while ((len = inputStream.read(bytes)) > 0) {
                    fileOutputStream.write(bytes, 0, len);
                }
                fileOutputStream.close();
                inputStream.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(connection, preparedStatement, null);
        }
    }
//ֵአJDBCᬳളOracleහഝପ඙֢ԫᬰګහഝ
    
/*
* ੒ԭOracleහഝପ޾Mysqlහഝପฎํಅӧݶጱ̶
* 1.OracleਧԎԧBLOBਁྦྷ҅֕ฎᬯӻਁྦྷӧฎ፥ྋࣈਂؙԫᬰګහഝ
* 2.ݻᬯӻਁྦྷਂӞӻBLOB೰ᰒ҅឴ݐکOracleጱBLOB੒᨝,಩ԫᬰګහഝනکᬯӻ೰ᰒ᯾ᶎ,೰ᰒ೰ݻ
BLOBਁྦྷ
* 3.ᵱᥝԪۓඪ೮
*
* */
public class Demo7 {
    @Test
    public void add() {
        Connection connection = null;
        PreparedStatement preparedStatement = null;

---

ResultSet resultSet = null;
        try {
            connection = UtilsDemo.getConnection();
            //୏ސԪۓ
            connection.setAutoCommit(false);
            //ൊفӞӻBLOB೰ᰒ
            String sql = "insert into test4(id,image) values(?,empty_blob())";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, 1);
            preparedStatement.executeUpdate();
            //಩BLOB೰ᰒັᧃڊ๶,஑کBLOB੒᨝
            String sql2 = "select image from test4 where id= ? for update";
            preparedStatement = connection.prepareStatement(sql2);
            preparedStatement.setInt(1, 1);
            resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                //஑کBlob੒᨝--୮౮ฎOracleጱBlob,ӧฎJDBCጱ,ಅզᥝ୩᫨[੕ጱฎ
oracle.sql.BLOB۱]
                BLOB  blob = (BLOB) resultSet.getBlob("image");
                //ٟفԫᬰګහഝ
                OutputStream outputStream = blob.getBinaryOutputStream();
                //឴ݐک᧛ݐ෈կ᧛فၞ
                InputStream inputStream = 
Demo7.class.getClassLoader().getResourceAsStream("01.jpg");
                int len=0;
                byte[] bytes = new byte[1024];
                while ((len = inputStream.read(bytes)) > 0) {
                    outputStream.write(bytes, 0, len);
                }
                outputStream.close();
                inputStream.close();
        connection.setAutoCommit(true);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {

---

UtilsDemo.release(connection, preparedStatement, null);
        }
    }
    @Test
    public void find() {
        
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        try {
            connection = UtilsDemo.getConnection();
            String sql = "SELECT * FROM test4 WHERE id=1";
            preparedStatement = connection.prepareStatement(sql);
            resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                //឴ݐکBLOB੒᨝
                BLOB blob = (BLOB) resultSet.getBlob("image");
                //ਖ਼හഝ᧛ݐکᏺፏӤ
                InputStream inputStream = blob.getBinaryStream();
                FileOutputStream fileOutputStream = new 
FileOutputStream("d:\\zhongfucheng.jpg");
                int len=0;
                byte[] bytes = new byte[1024];
                while ((len = inputStream.read(bytes)) > 0) {
                    fileOutputStream.write(bytes, 0, len);
                }
                inputStream.close();
                fileOutputStream.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            UtilsDemo.release(connection, preparedStatement, null);

---

੒ԭJDBCᬳളOracleහഝପ඙֢CLOBහഝ,౯੪ӧٚ᯿॔ԧ,඙֢᪙BLOBپԒፘݶ
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
4.឴ݐහഝପጱᛔۖԆᲫڜ
 
4.1 ԅՋԍᥝ឴ݐහഝପጱᛔۖԆᲫڜහഝ?
 
ଫአ࣋ว:
ํӞୟᘌ૵ᤒ҅Ӟୟ਍ኞᤒ̶ሿࣁ๶ԧӞӻෛጱᘌ૵҅਍ኞᥝ᪙፳ෛᘌ૵Ӥ᧞̶
        }
    }
}

![三歪教你学JDBC 第21页插图](../assets/images/三歪教你学JDBC_p21_1_3c233a1a.jpeg)

![三歪教你学JDBC 第21页插图](../assets/images/三歪教你学JDBC_p21_2_ef0028f9.png)

---

౯ḒضᥝᎣ᭲ᘌ૵ጱidᖫݩฎग़੝҅਍ኞ಍ᚆᎣ᭲᪙፳ߺӻᘌ૵਍ԟ̓਍ኞक़Ძ݇ᆙᘌ૵ԆᲫ̶̈́
5.᧣አහഝପጱਂؙᬦᑕ
 
᧣አਂؙᬦᑕጱ᧍ဩғ
᧣አڍහጱ᧍ဩғ
    @Test
    public void test() {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        try {
            connection = JdbcUtils.getConnection();
            String sql = "INSERT INTO test(name) VALUES(?)";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, "ouzicheng");
            if (preparedStatement.executeUpdate() > 0) {
                //឴ݐکᛔۖԆᲫڜጱ꧊
                resultSet = preparedStatement.getGeneratedKeys();
                if (resultSet.next()) {
                    int id = resultSet.getInt(1);
                    System.out.println(id);
                }
            }
            
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(connection, preparedStatement, null);
        }
  {call <procedure-name>[(<arg1>,<arg2>, ...)]}

---

ইຎฎOutputᔄࣳጱ҅ᮎԍࣁJDBC᧣አጱ෸ײฎᥝဳٙጱ̶ইӥդᎱಅᐏғ
  {?= call <procedure-name>[(<arg1>,<arg2>, ...)]}
/*
    jdbc᧣አਂؙᬦᑕ
  delimiter $$
    CREATE PROCEDURE demoSp(IN inputParam VARCHAR(255), INOUT inOutParam 
varchar(255))
    BEGIN
        SELECT CONCAT('zyxw---', inputParam) into inOutParam;
    END $$
  delimiter ;
*/
//౯ժࣁJDBC᧣አਂؙᬦᑕ,੪؟ࣁ᧣አොဩӞ໏
public class Demo9 {
    public static void main(String[] args) {
        Connection connection = null;
        CallableStatement callableStatement = null;
        try {
            connection = JdbcUtils.getConnection();
            
            callableStatement = connection.prepareCall("{call demoSp(?,?)}");
            callableStatement.setString(1, "nihaoa");
            
            //ဳٙᒫ2ӻ݇හ,ᔄࣳฎVARCHAR
            callableStatement.registerOutParameter(2, Types.VARCHAR);
            callableStatement.execute();
            
      //឴ݐփڊ݇හ[឴ݐਂؙᬦᑕ᯾ጱ꧊]
            String result = callableStatement.getString(2);
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            try {
                connection.close();
                callableStatement.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

---

݇ᘍᩒාғ
    }
------------------------------------------------------------------------------
----ᬦᑕ
#ץදmysql᧍ݙጱᕮຎᒧԅ//
mysql > delimiter //
#ਧԎӞӻᬦᑕ҅឴ݐusersᤒ௛ᦕ୯හ҅ਖ਼10ᦡᗝکݒᰁcountӾ
create procedure simpleproc(out count int)
begin
    select count(id) into count from users;
end
//
#ץදmysql᧍ݙጱᕮຎᒧԅ;
mysql > delimiter ;
#᧣አᬦᑕ҅ਖ਼ᕮຎᥟᕳݒᰁa҅@ฎਧԎݒᰁጱᒧݩ
call simpleproc(@a);
#ดᐏݒᰁaጱ꧊
select @a;
//զӥฎJava᧣አMysqlጱᬦᑕ
  String sql = "{call simpleproc(?)}";
  Connection conn = JdbcUtil.getConnection();
  CallableStatement cstmt = conn.prepareCall(sql);
  cstmt.registerOutParameter(1,Types.INTEGER);
  cstmt.execute();
  Integer count = cstmt.getInt(1);
  System.out.println("وํ" + count + "Ո");
------------------------------------------------------------------------------
----ڍහ
#ץදmysql᧍ݙጱᕮຎᒧԅ//
mysql > delimiter //
#ਧԎӞӻڍහ҅ਠ౮ਁᒧԀ೪ള
create function hello( s char(20) ) returns char(50) 
return concat('hello҅',s,'!');
//

---

#ץදmysql᧍ݙጱᕮຎᒧԅ;
mysql > delimiter ;
#᧣አڍහ
select hello('world');
//զӥฎJava᧣አMysqlጱڍහ
  String sql = "{? = call hello(?)}";
  Connection conn = JdbcUtil.getConnection();
  CallableStatement cstmt = conn.prepareCall(sql);
  cstmt.registerOutParameter(1,Types.VARCHAR);
  cstmt.setString(2,"zhaojun");
  cstmt.execute();
  String value = cstmt.getString(1);
  System.out.println(value);
  JdbcUtil.close(cstmt);
  JdbcUtil.close(conn);

![三歪教你学JDBC 第25页插图](../assets/images/三歪教你学JDBC_p25_1_9ef93dcf.jpeg)

![三歪教你学JDBC 第25页插图](../assets/images/三歪教你学JDBC_p25_2_3c233a1a.jpeg)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
Ԫۓ+زහഝ+ද᭜ૡٍᔄ
 
 
1.Ԫۓ
 
ӞӻSESSIONಅᬰᤈጱಅํๅෛ඙֢ᥝԍӞ᩸౮ۑ҅ᥝԍӞ᩸०ᨳ
Ԉӻֺৼ:AݻB᫨ᨴ҅᫨ᨴᬯӻၞᑕӾইຎڊሿᳯ᷌҅Ԫۓݢզᦏහഝ௩॔౮ܻ๶Ӟ໏̓Aᨴಁጱ᰸ဌ
ݒ҅Bᨴಁጱ᰸Ԟဌݒ̶̈́
 
Ԫֺ᧔กғ
՗Ӥᶎ፡҅౯ժጱᏟݢզݎሿAݻB᫨ᨴ҅౮ۑԧ̶ݢฎইຎAݻB᫨ᨴጱᬦᑕӾڊሿԧᳯ᷌ޫҘӥᶎཛྷ
೙Ӟӥ
    /*
    * ౯ժ๶ཛྷ೙AݻBᨴݩ᫨ᨴጱ࣋ว
    *   A޾Bᨴಁ᮷ํ1000ࣘ҅ሿࣁ౯ᦏAᨴಁݻBᨴݩ᫨500ࣘ᰸
    *
    * */
            //JDBCἕᦊጱఘ٭ӥฎىᳮԪۓጱ҅ӥᶎ౯ժ፡፡ىᳮԪۓ݄඙֢᫨ᨴ඙֢ํՋԍᳯ᷌
            //Aᨴಁٺ݄500ࣘ
            String sql = "UPDATE a SET money=money-500 ";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.executeUpdate();
            //Bᨴಁग़ԧ500ࣘ
            String sql2 = "UPDATE b SET money=money+500";
            preparedStatement = connection.prepareStatement(sql2);
            preparedStatement.executeUpdate();

---

ดᆐ҅ӤᶎդᎱฎտಲڊ୑ଉጱ҅౯ժٚ๶ັᧃӞӥහഝ̶Aᨴಁ੝ԧ500ࣘ᰸҅Bᨴಁጱ᰸ဌํीے̶
ᬯกดฎӧݳቘጱ̶
 
౯ժݢզ᭗ᬦԪۓ๶ᥴ٬Ӥᶎڊሿጱᳯ᷌
      //Aᨴಁٺ݄500ࣘ
            String sql = "UPDATE a SET money=money-500 ";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.executeUpdate();
      
      //ᬯ᯾ཛྷ೙ڊሿᳯ᷌
            int a = 3 / 0;
            String sql2 = "UPDATE b SET money=money+500";
            preparedStatement = connection.prepareStatement(sql2);
            preparedStatement.executeUpdate();
      //୏ސԪۓ,੒හഝጱ඙֢੪ӧտᒈܨኞප̶
            connection.setAutoCommit(false);
            
            //Aᨴಁٺ݄500ࣘ
            String sql = "UPDATE a SET money=money-500 ";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.executeUpdate();
            //ࣁ᫨ᨴᬦᑕӾڊሿᳯ᷌
            int a = 3 / 0;
            //Bᨴಁग़500ࣘ
            String sql2 = "UPDATE b SET money=money+500";
            preparedStatement = connection.prepareStatement(sql2);
            preparedStatement.executeUpdate();
            
            //ইຎᑕଧᚆಗᤈکᬯ᯾҅ဌํಲڊ୑ଉ҅౯ժ੪൉Իහഝ
            connection.commit();
      //ىᳮԪۓ̓ᛔۖ൉Ի̈́
      connection.setAutoCommit(true);
            
        } catch (SQLException e) {
            try {
                //ইຎڊሿԧ୑ଉ҅੪տᬰکᬯ᯾๶҅౯ժ੪಩Ԫۓࢧ჻̓ਖ਼හഝݒ౮ܻ๶ᮎ໏̈́
                connection.rollback();

---

ӤᶎጱᑕଧԞӞ໏ಲڊԧ୑ଉ҅Aᨴಁ᰸ဌํٺ੝҅Bᨴಁጱ᰸Ԟဌํीے̶
ဳ఺ғ୮Connection᭬کӞӻ๚॒ቘጱSQLException෸҅ᔮᕹտᶋྋଉᭅڊ҅ԪۓԞտᛔۖࢧ჻҅֕
ইຎᑕଧഔ឴کԧ୑ଉ҅ฎᵱᥝࣁcatchӾดୗࢧ჻Ԫۓጱ̶
 
1.1 savapoint
 
౯ժᬮݢզֵአsavepointᦡᗝӾᳵᅩ̶ইຎࣁ຤ࣈොڊᲙԧ҅౯ժᦡᗝӾᳵᅩ҅ࢧ჻کڊᲙԏڹܨ
ݢ̶
ଫአ࣋วғሿࣁ౯ժᥝᓒӞ᭲හ਍᷌҅ᓒکݸᶎݎሿᓒᲙහԧ̶ڹᶎጱᬩᓒ᮷ฎྋᏟጱ҅౯ժӧݢᚆ᯿
१ٚᓒ̓ፗളrollback๋̈́҅অጱ؉ဩ੪ฎࣁכᦤڹᶎᓒ੒ጱఘ٭ӥ҅ᦡᗝӞӻכਂᅩ̶՗כਂᅩ୏ত
᯿ෛᓒ̶
ဳ఺ғsavepointӧտᕮ๳୮ڹԪۓ҅ฦ᭗൉Ի޾ࢧ჻᮷տᕮ๳୮ڹԪۓጱ
1.2 Ԫۓጱᵍᐶᕆڦ
 
හഝପਧԎԧ4ӻᵍᐶᕆڦғ
1. Serializable̓ݢ᭿عᚍ᧛҅ӧݢ᯿॔᧛҅ᡦ᧛̈́
2. Repeatable read̓ݢ᭿عᚍ᧛҅ӧݢ᯿॔᧛̈́
3. Read committed̓ݢ᭿عᚍ᧛̈́
4. Read uncommitted̓ᕆڦ๋֗҅Ջԍ᮷᭿عӧԧ̈́
ړڦ੒ଫConnectionᔄӾጱ4ӻଉᰁ
1. TRANSACTION_READ_UNCOMMITTED
2. TRANSACTION_READ_COMMITTED
3. TRANSACTION_REPEATABLE_READ
4. TRANSACTION_SERIALIZABLE
ᚍ᧛ғӞӻԪۓ᧛ݐکݚक़ӞӻԪۓ๚൉Իጱහഝ
ֺৼғAݻB᫨ᨴ҅Aಗᤈԧ᫨ᨴ᧍ݙ҅֕Aᬮဌํ൉ԻԪۓ҅B᧛ݐහഝ҅ݎሿᛔ૩ᨴಁ᰸ݒग़ԧѺB᪙
A᧔҅౯૪ᕪතک᰸ԧ̶Aࢧ჻Ԫۓ̓rollback̈́҅ᒵBٚັ፡ᨴಁጱ᰸෸҅ݎሿ᰸ଚဌํग̶़
ӧݢ᯿॔᧛ғӞӻԪۓ᧛ݐکݚक़ӞӻԪۓ૪ᕪ൉Իጱහഝ҅Ԟ੪ฎ᧔ӞӻԪۓݢզ፡کٌ՜Ԫۓಅ؉
ጱץද
                //ىᳮԪۓ̓ᛔۖ൉Ի̈́
                connection.setAutoCommit(true);
            } catch (SQLException e1) {
                e1.printStackTrace();
            }

---

ဳғAັᧃහഝପ஑کහഝ҅B݄ץදහഝପጱහഝ҅੕ᛘAग़ེັᧃහഝପጱᕮຎ᮷ӧӞ໏̓ܧਸ਼ғA
ྯེັᧃጱᕮຎ᮷ฎݑBጱ୽ߥጱ҅ᮎԍAັᧃڊ๶ጱמ௳੪ဌํ఺௏ԧ̈́
ᡦ᧛(ଝ᧛)ғฎ೰ࣁӞӻԪۓٖ᧛ݐکԧڦጱԪۓൊفጱහഝ҅੕ᛘڹݸ᧛ݐӧӞᛘ̶
ဳғ޾ӧݢ᯿॔᧛ᔄ֒҅֕ᡦ᧛(ଝ᧛)տ᧛کٌ՜Ԫۓጱൊفጱහഝ҅੕ᛘڹݸ᧛ݐӧӞᛘ
ᓌܔ௛ᕮғᚍ᧛ฎӧݢ਻தጱ҅ӧݢ᯿॔᧛޾ᡦ᧛ࣁӞਧጱఘ٭ӥฎݢզጱ̓؉ᕹᦇጱᙗਧ੪ӧᤈ̶̈́
2.زහഝ
 
2.1 Ջԍฎزහഝ
 
زහഝٌਫ੪ฎහഝପ҅ᤒ҅ڜጱਧԎמ௳
2.2 ԅՋԍ౯ժᥝአزහഝ
 
ܨֵ౯ժٟԧӞӻᓌܔૡٍᔄ҅౯ժጱդᎱᬮฎᶋଉ̶ٞ֟੒ԭीڢදᘒ᥺҅ݝํSQL޾݇හฎӧݶ
ጱ҅౯ժԅ֜ӧ಩ᬯԶፘݶጱդᎱುݐ౮ӞӻොဩҘ੒ԭັᧃᘒ᥺҅ӧݶጱਫ֛ັᧃڊ๶ጱᕮຎᵞฎӧ
Ӟ໏ጱ̶౯ժᥝֵአزහഝ឴ݐᕮຎᵞጱמ௳҅಍ᚆ੒ᕮຎᵞᬰᤈ඙̶֢
 
ParameterMetaData   --݇හጱزහഝ
ResultSetMetaData   --ᕮຎᵞጱزහഝ
DataBaseMetaData   --හഝପጱزහഝ

![三歪教你学JDBC 第29页插图](../assets/images/三歪教你学JDBC_p29_1_2e4b8626.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
3.ද᭜JDBCૡٍᔄ
 
ᳯ᷌ғ౯ժ੒හഝପጱीڢදັ᮷ᥝᬳളහഝପ҅ىᳮᩒრ҅឴ݐPreparedSteatment੒᨝҅឴ݐ
Connection੒᨝ྌᔄጱ඙֢҅ᬯ໏ጱդᎱ᯿॔ሲฎຄṛጱ҅ಅզ౯ժᥝ੒ૡٍᔄᬰᤈी୩
3.1 ीڢද
 
    //౯ժݎሿ҅ीڢදݝํSQL᧍ݙ޾փفጱ݇හฎӧᎣ᭲ጱᘒ૪҅ಅզᦏ᧣አᧆොဩጱՈփ᭓ᬰ๶
  
  //ኧԭփ᭓ᬰ๶ጱ݇හฎݱᐿᔄࣳጱ҅ᘒӬහፓฎӧᏟਧጱ҅ಅզֵአObject[]
    
    public static void update(String sql, Object[] objects) {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        try {
            connection = getConnection();
            preparedStatement = connection.prepareStatement(sql);
            //໑ഝփ᭓ᬰ๶ጱ݇හ҅ᦡᗝSQLܛ֖ᒧጱ꧊
            for (int i = 0; i < objects.length; i++) {
                preparedStatement.setObject(i + 1, objects[i]);
            }
            //ಗᤈSQL᧍ݙ
            preparedStatement.executeUpdate();

![三歪教你学JDBC 第30页插图](../assets/images/三歪教你学JDBC_p30_1_3c233a1a.jpeg)

---

3.2 ັᧃ
 
ളݗғ
        } catch (Exception e) {
            e.printStackTrace();
    /*
        1:੒ԭັᧃ᧍ݙ๶᧔҅౯ժӧᎣ᭲੒ᕮຎᵞᬰᤈՋԍ඙֢̓ଉአጱ੪ฎ಩හഝ੗ᤰ౮ӞӻBean
੒᨝҅੗ᤰ౮ӞӻListᵞݳ̈́
        2:౯ժݢզਧԎӞӻളݗ҅ᦏ᧣አᘏ಩ളݗጱਫሿᔄփ᭓ᬰ๶
        3:ᬯ໏ളݗ᧣አጱොဩ੪ฎ᧣አᘏփ᭓ᬰ๶ਫሿᔄጱොဩ̶̓ᒽኼཛྷୗ̈́
    */
    //ᬯӻොဩጱᬬࢧ꧊ฎձ఺ᔄࣳጱ҅ಅզਧԎԅObject̶
    public static Object query(String sql, Object[] objects, ResultSetHandler 
rsh) {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        try {
            connection = getConnection();
            preparedStatement = connection.prepareStatement(sql);
            //໑ഝփ᭓ᬰ๶ጱ݇හ҅ᦡᗝSQLܛ֖ᒧጱ꧊
            if (objects != null) {
                for (int i = 0; i < objects.length; i++) {
                    preparedStatement.setObject(i + 1, objects[i]);
                }
            }
            resultSet = preparedStatement.executeQuery();
            //᧣አ᧣አᘏփ᭓ᬰ๶ਫሿᔄጱොဩ҅੒ᕮຎᵞᬰᤈ඙֢
            return rsh.hanlder(resultSet);
  }

---

ਫሿᔄғ
 
  /*
  * ਧԎ੒ᕮຎᵞ඙֢ጱളݗ҅᧣አᘏమᥝ੒ᕮຎᵞᬰᤈՋԍ඙֢҅ݝᥝਫሿᬯӻളݗܨݢ
  * */
  public interface ResultSetHandler {
       Object hanlder(ResultSet resultSet);
  
  }
//ളݗਫሿᔄ҅੒ᕮຎᵞ੗ᤰ౮ӞӻBean੒᨝
public class BeanHandler implements ResultSetHandler {
    //ᥝ੗ᤰ౮ӞӻBean੒᨝҅ḒضᥝᎣ᭲BeanฎՋԍ҅ᬯӻԞฎ᧣አᘏփ᭓ᬰ๶ጱ̶
    private Class clazz;
    public BeanHandler(Class clazz) {
        this.clazz = clazz;
    }
    @Override
    public Object hanlder(ResultSet resultSet) {
        try {
            //ڠୌփᬰ੒᨝ጱਫֺ۸
            Object bean = clazz.newInstance();
            if (resultSet.next()) {
                //೭کᕮຎᵞزහഝ
                ResultSetMetaData resultSetMetaData = resultSet.getMetaData();
                for (int i = 0; i < resultSetMetaData.getColumnCount(); i++) {
                    //឴ݐکྯڜጱڜݷ
                    String columnName = resultSetMetaData.getColumnName(i+1);
                    //឴ݐکྯڜጱහഝ
                    String columnData = resultSet.getString(i+1);
                    //ᦡᗝBeanં௔
                    Field field = clazz.getDeclaredField(columnName);

---

̓ᒽኼཛྷୗ̈́ᓌܔቘᥴғ
౯ժଚӧᎣ᭲᧣አᘏమ੒ᕮຎᵞᬰᤈெԍ໏ጱ඙֢҅ԭฎᦏ᧣አᘏ಩మᥝ؉ጱ඙֢੒᨝փ᭓ᬦ๶
౯ժݝᥝአփ᭓ᬦ๶ጱ੒᨝੒ᕮຎᵞᬰᤈ੗ᤰ੪অԧ̶ 
ᛗԭ᧣አᘏտփ᭓Ջԍ੒᨝ᬦ๶҅ᧆ੒᨝ᥝਫሿՋԍොဩ̶౯ժݢզֵአളݗ๶੒ٌᥢ᝜
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
                    field.setAccessible(true);
                    field.set(bean,columnData);
                }
                //ᬬࢧBean੒᨝
                return bean;
            }

![三歪教你学JDBC 第33页插图](../assets/images/三歪教你学JDBC_p33_1_54b944c6.png)

![三歪教你学JDBC 第33页插图](../assets/images/三歪教你学JDBC_p33_2_3c233a1a.jpeg)

---

හഝପᬳള࿰+DBUtils+ړᶭ
 
 
1.හഝପᬳള࿰
 
1.1Ջԍฎහഝପᬳള࿰
 
ᓌܔ๶᧔ғහഝପᬳള࿰੪ฎ൉׀ᬳളጱ̶̶̶
1.2ԅՋԍ౯ժᥝֵአහഝପᬳള࿰
 
හഝପጱᬳളጱୌᒈ޾ىᳮฎᶋଉၾᘙᩒრጱ
᷇ᔺࣈ಑୏̵ىᳮᬳള᭜౮ᔮᕹ௔ᚆ֗ӥ
1.3ই֜ᛔ૩ᖫٟӞӻᬳള࿰
 
1. ᖫٟᬳള࿰ᵱਫሿjava.sql.DataSourceളݗ
2. ڠୌಢᰁጱConnectionአLinkedListכਂ̓෬ᆐฎӻ࿰҅୮ᆐአᵞݳכਂ̵̵LinkedListବ੶ฎ
᱾ᤒ҅੒ीڢ௔ᚆ᫾অ̈́
3. ਫሿgetConnetion()҅ᦏgetConnection()ྯེ᧣አ҅᮷ฎࣁLinkedListӾݐӞӻConnectionᬬ
ࢧᕳአಁ
4. ᧣አConnection.close()ොဩ҅ConnctionᬬࢧᕳLinkedList
    private static LinkedList<Connection> list = new LinkedList<>();
    
    //឴ݐᬳളݝᵱᥝӞེ੪ड़ԧ҅ಅզአstaticդᎱࣘ
    static {
        //᧛ݐ෈կᯈᗝ
        InputStream inputStream = 
Demo1.class.getClassLoader().getResourceAsStream("db.properties");
        Properties properties = new Properties();
        try {
            properties.load(inputStream);
            String url = properties.getProperty("url");
            String username = properties.getProperty("username");
            String driver = properties.getProperty("driver");
            String password = properties.getProperty("password");
            //ے᫹ḝۖ
            Class.forName(driver);
            //឴ݐग़ӻᬳള҅כਂࣁLinkedListᵞݳӾ
            for (int i = 0; i < 10; i++) {
                Connection connection = DriverManager.getConnection(url, 
username, password);

---

౯ժ૪ᕪਠ౮ڹӣྍԧ҅ሿࣁᳯ᷌๶ԧ̶౯ժ᧣አConncetion.close()ොဩ҅ฎ಩හഝପጱᇔቘᬳളى
ധ҅ᘒӧฎᬬࢧᕳLinkedListጱ
ᥴ٬௏᪠ғ
1. ٟӞӻConnectionৼᔄ҅ᥟፍclose()ොဩ
2. ٟӞӻConnection۱ᤰᔄ҅ी୩close()ොဩ
3. አۖாդቘ҅ᬬࢧӞӻդቘ੒᨝ڊ݄҅ೝ౼close()ොဩጱ᧣አ҅੒close()ी୩
ړຉᒫӞӻ௏᪠ғ
Connectionฎ᭗ᬦහഝପḝۖے᫹ጱ҅כਂԧහഝጱמ௳̶ٟӞӻৼᔄConnection҅newڊ੒
᨝҅ৼᔄጱConnction෫ဩፗളᖀಥᆿᔄጱහഝמ௳҅Ԟ੪ฎ᧔ৼᔄጱConnectionฎ෫ဩᬳളහ
ഝପጱ҅ๅڦ᧨ᥟፍclose()ොဩԧ̶
ړຉᒫԫӻ௏᪠ғ
ٟӞӻConnection۱ᤰᔄ̶
1. ٟӞӻᔄ҅ਫሿӨᤩी୩੒᨝ጱፘݶളݗ̓Connectionളݗ̈́
2. ਧԎӞӻݒᰁ҅೰ݻᤩी୩ጱ੒᨝
3. ਧԎ຅᭜ොဩ҅ളතᤩी୩੒᨝
4. ᥟፍమी୩ጱොဩ
5. ੒ԭӧమी୩ጱොဩ҅ፗള᧣አᤩी୩੒᨝ጱොဩ
ᬯӻ௏᪠๜᫝ฎဌՋԍྷየጱ҅੪ฎਫሿളݗ෸҅ොဩॡग़ԧѺ҅ಅզ౯ժԞӧֵአྌොဩ
                list.add(connection);
            }
            
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    //᯿ٟConnectionොဩ҅አಁ឴ݐᬳളଫᧆ՗LinkedListӾᕳ՜
    @Override
    public Connection getConnection() throws SQLException {
        System.out.println(list.size());
        System.out.println(list);
       //ضڣෙLinkedListฎވਂࣁᬳള
       return list.size() > 0 ? list.removeFirst() : null; 
    }

---

ړຉᒫӣӻ௏᪠դᎱਫሿғ
౯ժӤᶎ૪ᕪᚆड़ᓌܔᖫٟӞӻᕚᑕ࿰ԧ̶ӥᶎ౯ժ๶ֵአӞӥ୏რහഝପᬳള࿰
1.4DBCP
 
ֵአDBCPහഝრጱྍṈғ
    @Override
    public Connection getConnection() throws SQLException {
        if (list.size() > 0) {
            final Connection connection = list.removeFirst();
            //፡፡࿰ጱय़ੜ
            System.out.println(list.size());
            //ᬬࢧӞӻۖாդቘ੒᨝
            return (Connection) 
Proxy.newProxyInstance(Demo1.class.getClassLoader(), 
connection.getClass().getInterfaces(), new InvocationHandler() {
                @Override
                public Object invoke(Object proxy, Method method, Object[] 
args) throws Throwable {
                    //ইຎӧฎ᧣አcloseොဩ҅੪ೲᆙྋଉጱ๶᧣አ
                    if (!method.getName().equals("close")) {
                        method.invoke(connection, args);
                    } else {
                        //ᬰکᬯ᯾๶҅᧔ก᧣አጱฎcloseොဩ
                        list.add(connection);
                        //ٚ፡፡࿰ጱय़ੜ
                        System.out.println(list.size());
                    }
                    return null;
                }
            });
        }
        return null;
    }

---

1. ੕فӷӻjar۱̓Commons-dbcp.jar޾Commons-pool.jar̈́
2. ᧛ݐᯈᗝ෈կ
3. ឴ݐBasicDataSourceFactory੒᨝
4. ڠୌDataSource੒᨝
    private static DataSource dataSource = null;
    static {
        try {
            //᧛ݐᯈᗝ෈կ
            InputStream inputStream = 
Demo3.class.getClassLoader().getResourceAsStream("dbcpconfig.properties");
            Properties properties = new Properties();
            properties.load(inputStream);
            //឴ݐૡܯ੒᨝
            BasicDataSourceFactory basicDataSourceFactory = new 
BasicDataSourceFactory();
            dataSource = basicDataSourceFactory.createDataSource(properties);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static Connection getConnection() throws SQLException {
        return dataSource.getConnection();
    }
    //ᬯ᯾᯽නᩒრӧฎ಩හഝପጱᇔቘᬳള᯽නԧ҅ฎ಩ᬳള୭ᬮᕳᬳള࿰̓ᬳള࿰ጱConnectionٖ
᮱ᛔ૩؉অԧ̈́
    public static void release(Connection conn, Statement st, ResultSet rs) {
        if (rs != null) {
            try {
                rs.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
            rs = null;
        }
        if (st != null) {
            try {
                st.close();
            } catch (Exception e) {
                e.printStackTrace();

---

1.5 C3P0
 
C3P0හഝრጱ௔ᚆๅᙯӞᓉ҅ଚӬਙݢզֵአXMLᯈᗝ෈կᯈᗝמ௳Ѻ
ྍṈғ
1. ੕ف୏ݎ۱̓c3p0-0.9.2-pre1.jar̈́޾̓mchange-commons-0.2.jar̈́
2. ੕فXMLᯈᗝ෈կ̓ݢզࣁᑕଧӾᛔ૩ӞӻӞӻᯈ҅C3P0ጱdocӾጱConﬁgurationํXML෈կጱ
Ԫֺ̈́
3. newڊComboPooledDataSource੒᨝
1.6 Tomcatහഝრ
 
Tomcat๐ۓ࢏Ԟᕳ౯ժ൉׀ԧᬳള࿰ٖ҅᮱ٌਫ੪ฎDBCP
ྍṈғ
1. ࣁMETA-INFፓ୯ӥᯈᗝcontext.xml෈կ̓෈կٖ਻ݢզࣁtomcatἕᦊᶭᶎጱ JNDI Resourcesӥ
Conﬁgure Tomcat's Resource Factoryತک̈́
2. ੕فMysql౲oracle୏ݎ۱کtomcatጱlibፓ୯ӥ
3. ڡত۸JNDI->឴ݐJNDI਻࢏->༄ᔱզXXXԅݷਁࣁJNDI਻࢏ਂනጱᬳള࿰
            }
        }
        if (conn != null) {
            try {
                conn.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    private static ComboPooledDataSource comboPooledDataSource = null;
    static {
        //ইຎ౯Ջԍ᮷ӧ೰ਧ҅੪ฎֵአXMLἕᦊጱᯈᗝ҅ᬯ᯾౯೰ਧጱฎoracleጱ
        comboPooledDataSource = new ComboPooledDataSource("oracle");
    }
    public static Connection getConnection() throws SQLException {
        return comboPooledDataSource.getConnection();
    }

---

context.xml෈կጱᯈᗝғ
 
1.7 Druid
 
ݢզ፡፡෈໩҅ሿࣁᬯӻහഝପᬳള࿰አ஑ꂁग़ጱғhttps://github.com/alibaba/druid
<Context>
  <Resource name="jdbc/EmployeeDB"
            auth="Container"
            type="javax.sql.DataSource"
            
            username="root"
            password="root"
            driverClassName="com.mysql.jdbc.Driver"
            url="jdbc:mysql://localhost:3306/zhongfucheng"
            maxActive="8"
            maxIdle="4"/>
</Context>
        try {
      //ڡত۸JNDI਻࢏
            Context initCtx = new InitialContext();
      //឴ݐکJNDI਻࢏
            Context envCtx = (Context) initCtx.lookup("java:comp/env");
      //ಚൈզjdbc/EmployeeDBݷਁᕬਧࣁJNDI਻࢏ӥጱᬳള࿰
            DataSource ds = (DataSource)
                    envCtx.lookup("jdbc/EmployeeDB");
            Connection conn = ds.getConnection();
            System.out.println(conn);
        }

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
2. ֵአdbutils໛ຝ
 
dbutilsਙฎ੒JDBCጱᓌܔ੗ᤰ҅ຄय़ᓌ۸jdbcᖫᎱጱૡ֢ᰁ
2.1DbUtilsᔄ
 
൉׀ԧىᳮᬳള҅ᤰ᫹JDBCḝۖ҅ࢧ჻൉ԻԪۓᒵොဩጱૡٍᔄ̓ྲ᫾੝ֵአ҅ࢩԅ౯ժ਍ԧᬳള࿰҅
੪ଫᧆֵአᬳള࿰ᬳളහഝପ̈́
2.2QueryRunnerᔄ
 
ᧆᔄᓌ۸ԧSQLັᧃ҅ᯈݳResultSetHandlerֵአ҅ݢզਠ౮य़᮱ړጱහഝପ඙֢҅᯿᫹ԧᦜग़ጱັ
ᧃ҅ๅෛ҅ಢ॒ቘොဩ̶य़य़ٺ੝ԧդᎱᰁ
2.3ResultSetHandlerളݗ
 
ᧆളݗᥢ᝜ԧ੒ResultSetጱ඙֢҅ᥝ੒ᕮຎᵞᬰᤈՋԍ඙֢҅փفResultSetHandlerളݗጱਫሿᔄܨ
ݢ̶

![三歪教你学JDBC 第40页插图](../assets/images/三歪教你学JDBC_p40_1_7178a4c6.png)

![三歪教你学JDBC 第40页插图](../assets/images/三歪教你学JDBC_p40_2_3c233a1a.jpeg)

---

ArrayHandlerғ಩ᕮຎᵞӾጱᒫӞᤈහഝ᫨౮੒᨝හᕟ̶
ArrayListHandlerғ಩ᕮຎᵞӾጱྯӞᤈහഝ᮷᫨౮Ӟӻහᕟ҅ٚਂනکListӾ̶
BeanHandlerғਖ਼ᕮຎᵞӾጱᒫӞᤈහഝ੗ᤰکӞӻ੒ଫጱJavaBeanਫֺӾ̶
BeanListHandlerғਖ਼ᕮຎᵞӾጱྯӞᤈහഝ᮷੗ᤰکӞӻ੒ଫጱJavaBeanਫֺӾ҅ਂනکList
᯾̶
ColumnListHandlerғਖ਼ᕮຎᵞӾ຤ӞڜጱහഝਂනکListӾ̶
KeyedHandler(name)ғਖ਼ᕮຎᵞӾጱྯӞᤈහഝ᮷੗ᤰکӞӻMap᯾҅ٚ಩ᬯԶmapٚਂکӞӻ
map᯾ٌ҅keyԅ೰ਧጱkey̶
MapHandlerғਖ਼ᕮຎᵞӾጱᒫӞᤈහഝ੗ᤰکӞӻMap᯾҅keyฎڜݷ҅value੪ฎ੒ଫጱ꧊̶
MapListHandlerғਖ਼ᕮຎᵞӾጱྯӞᤈහഝ᮷੗ᤰکӞӻMap᯾҅ᆐݸٚਂනکList
ScalarHandler ਖ਼ResultSetጱӞӻڜکӞӻ੒᨝Ӿ̶
 
ֵአDbUtils໛ຝ੒හഝପጱCRUD
/*
* ֵአDbUtils໛ຝ੒හഝପጱCRUD
* ಢ॒ቘ
*
* */
public class Test {
    @org.junit.Test
    public void add() throws SQLException {
        //ڠୌڊQueryRunner੒᨝
        QueryRunner queryRunner = new QueryRunner(JdbcUtils.getDataSource());
        String sql = "INSERT INTO student (id,name) VALUES(?,?)";
        //౯ժݎሿquery()ොဩํጱᵱᥝփفConnection੒᨝҅ํጱӧᵱᥝփف
        //܄ڦғ֦փفConnection੒᨝ฎᵱᥝ֦๶ᲀྪᧆConnection֦҅ӧփف҅ኧᑕଧଆ֦಩
Connectionනࢧکᬳള࿰Ӿ
        queryRunner.update(sql, new Object[]{"100", "zhongfucheng"});
    }
    @org.junit.Test
    public void query()throws SQLException {
        //ڠୌڊQueryRunner੒᨝
        QueryRunner queryRunner = new QueryRunner(JdbcUtils.getDataSource());
        String sql = "SELECT * FROM student";
        List list = (List) queryRunner.query(sql, new 
BeanListHandler(Student.class));
        System.out.println(list.size());

---

3.ړᶭ
 
ړᶭದ๞ฎᶋଉଉᥠጱ҅ࣁ൤ᔱ୚කӥ൤ᔱᶭᶎ҅ӧݢᚆ಩ق᮱හഝ᮷ดᐏࣁӞӻᶭᶎ᯾ᬟ̶ಅզ౯ժ
አکԧړᶭದ๞̶
3.1Oracleਫሿړᶭ
 
    }
    @org.junit.Test
    public void delete() throws SQLException {
        //ڠୌڊQueryRunner੒᨝
        QueryRunner queryRunner = new QueryRunner(JdbcUtils.getDataSource());
        String sql = "DELETE FROM student WHERE id='100'";
        queryRunner.update(sql);
    }
    @org.junit.Test
    public void update() throws SQLException {
        //ڠୌڊQueryRunner੒᨝
        QueryRunner queryRunner = new QueryRunner(JdbcUtils.getDataSource());
        String sql = "UPDATE student SET name=? WHERE id=?";
        queryRunner.update(sql, new Object[]{"zhongfuchengaaa", 1});
    }
    @org.junit.Test
    public void batch() throws SQLException {
        //ڠୌڊQueryRunner੒᨝
        QueryRunner queryRunner = new QueryRunner(JdbcUtils.getDataSource());
        String sql = "INSERT INTO student (name,id) VALUES(?,?)";
        Object[][] objects = new Object[10][];
        for (int i = 0; i < 10; i++) {
            objects[i] = new Object[]{"aaa", i + 300};
        }
        queryRunner.batch(sql, objects);
    }
}
  /*
    Oracleړᶭ᧍ဩғ
      @lineSize---ྯᶭดᐏහഝᤈහ
      @currentPage----୮ڹಅࣁᶭ

---

Oracleړᶭܻቘᓌܔᥴ᯽ғ
3.2Mysqlਫሿړᶭ
 
  
  */
  SELECT *FROM (
      SELECT ڜݷ,ڜݷ,ROWNUM rn
      FROM ᤒݷ
      WHERE ROWNUM<=(currentPage*lineSize)) temp
  
  WHERE temp.rn>(currentPage-1)*lineSize;
  /*
    Oracleړᶭғ
      OracleጱړᶭׁᩢԭROWNUMᬯӻ։ڜ҅ROWNUMԆᥝ֢አ੪ฎԾኞᤈݩ̶
  
    ړᶭܻቘғ
      1ғৼັᧃັڊڹnᤈහഝ҅ROWNUMԾኞڹNᤈጱᤈݩ
      2ғֵአৼັᧃԾኞROWNUMጱᤈݩ҅᭗ᬦक़᮱ጱᓀᭌڊమᥝጱහഝ
  
    ֺৼғ
      ౯ሿࣁᥢਧྯᶭดᐏ5ᤈහഝ̓lineSize=5̈́҅౯ᥝັᧃᒫ2ᶭጱහഝ̓currentPage=2̈́
      ဳғ̓੒ᆙ፳᧍ဩ๶፡̈́
  
    ਫሿғ
      1ғৼັᧃັڊڹ10๵හഝ̓ROWNUM<=10̈́
      2ғक़᮱ᓀᭌڊݸᶎ5๵හഝ̓ROWNUM>5̈́
    3ғᬯ໏౯ժ੪ݐکԧݸᶎ5๵ጱහഝ
  */
  /*
    Mysqlړᶭ᧍ဩғ
    @start---؇ᑏᰁ҅ӧᦡᗝ੪ฎ՗0୏ত̓Ԟ੪ฎ(currentPage-1)*lineSizë́
    @length---ᳩଶ҅ݐग़੝ᤈහഝ
  
  */
  SELECT *
  FROM ᤒݷ
  LIMIT [START], length;
  
  /*
    ֺৼғ
      ౯ሿࣁᥢਧྯᶭดᐏ5ᤈහഝ҅౯ᥝັᧃᒫ2ᶭጱහഝ

---

௛ᕮғ
Mysql՗(currentPage-1)*lineSize୏তݐහഝ҅ݐlineSize๵හഝ
Oracleض឴ݐcurrentPagelineSize๵හഝ҅՗(currentPage-1)lineSize୏তݐහഝ
3.3ֵአJDBCᬳളහഝପਫሿړᶭ
 
ӥᶎฎଉᥠጱړᶭࢶᇆ
ᯈݳࢶᇆ҅፡ӥ౯ժጱᵱ࿢ฎՋԍғ
1. ᓒڊํग़੝ᶭጱහഝ҅ดᐏࣁᶭᶎӤ
2. ໑ഝᶭᎱ҅՗හഝପดᐏፘ੒ଫጱහഝ̶
 
ړຉғ
1. ᓒڊํग़੝ᶭහഝᬯฎᶋଉᓌܔጱ̓ࣁහഝପӾັᧃํग़੝๵ᦕ୯֦҅ྯᶭดᐏग़੝๵ᦕ୯҅੪ݢ
զᓒڊํग़੝ᶭහഝԧ̈́
2. ֵአMysql౲Oracleጱړᶭ᧍ဩܨݢ
᭗ᬦӤᶎړຉ҅౯ժտݎሿᵱᥝአک4ӻݒᰁ
currentPage--୮ڹᶭ̓ኧአಁ٬ਧጱ̈́
totalRecord--௛හഝහ̓ັᧃᤒݢᎣ̈́
lineSize--ྯᶭดᐏහഝጱහᰁ̓ኧ౯ժ୏ݎՈާ٬ਧ̈́
pageCount--ᶭහ̓totalRecord޾lineSize٬ਧ̈́
  
    ړຉғ
      1ғᒫ2ᶭጱහഝٌਫ੪ฎ՗ᒫ6๵හഝ୏ত҅ݐ5๵
  
    ਫሿғ
      1ғstartԅ5̓؇ᑏᰁ՗0୏ত̈́
      2ғlengthԅ5
*/
        //ྯᶭดᐏ3๵හഝ
        int lineSize = 3;
        //௛ᦕ୯හ
        int totalRecord = getTotalRecord();
        //؃ᦡአಁ೰ਧጱฎᒫ2ᶭ

![三歪教你学JDBC 第44页插图](../assets/images/三歪教你学JDBC_p44_1_3532ae09.png)

---

int currentPage = 2;
        //Ӟوํग़੝ᶭ
        int pageCount = getPageCount(totalRecord, lineSize);
        //ֵአՋԍහഝପᬰᤈړᶭ҅ᦕ஑ᥝࣁJdbcUtilsӾදᯈᗝ
        List<Person> list = getPageData2(currentPage, lineSize);
        for (Person person : list) {
            System.out.println(person);
        }
    }
    //ֵአJDBCᬳളMysqlහഝପਫሿړᶭ
    public static List<Person> getPageData(int currentPage, int lineSize) 
throws SQLException {
        //՗ߺӻ֖ᗝ୏তݐහഝ
        int start = (currentPage - 1) * lineSize;
        QueryRunner queryRunner = new QueryRunner(JdbcUtils.getDataSource());
        String sql = "SELECT name,address  FROM person LIMIT ?,?";
        List<Person> persons = (List<Person>) queryRunner.query(sql, new 
BeanListHandler(Person.class), new Object[]{start, lineSize});
        return persons;
    }
    //ֵአJDBCᬳളOracleහഝପਫሿړᶭ
    public static List<Person> getPageData2(int currentPage, int lineSize) 
throws SQLException {
        //՗ߺӻ֖ᗝ୏তݐහഝ
        int start = (currentPage - 1) * lineSize;
        //᧛ݐڹN๵හഝ
        int end = currentPage * lineSize;
        QueryRunner queryRunner = new QueryRunner(JdbcUtils.getDataSource());
        String sql = "SELECT " +
                "  name, " +
                "  address " +
                "FROM ( " +
                "  SELECT " +
                "    name, " +
                "    address , " +
                "    ROWNUM rn " +
                "  FROM person " +

---

"  WHERE ROWNUM <= ? " +
                ")temp WHERE temp.rn>?";
        List<Person> persons = (List<Person>) queryRunner.query(sql, new 
BeanListHandler(Person.class), new Object[]{end, start});
        return persons;
    }
    public static int getPageCount(int totalRecord, int lineSize) {
        //ᓌܔᓒဩ
        //return (totalRecord - 1) / lineSize + 1;
        //ྌᓒဩྲ᫾অቘᥴ҅಩හഝդդᬰ݄੪Ꭳ᭲ԧ̶
        return totalRecord % lineSize == 0 ? (totalRecord / lineSize) : 
(totalRecord / lineSize) + 1;
    }
    public static int  getTotalRecord() throws SQLException {
        //ֵአDbUtils໛ຝັᧃහഝପᤒӾํग़੝๵හഝ
        QueryRunner queryRunner = new QueryRunner(JdbcUtils.getDataSource());
        String sql = "SELECT COUNT(*) FROM person";
        Object o = queryRunner.query(sql, new ScalarHandler());
        String ss = o.toString();
        int  s = Integer.parseInt(ss);
        return s;
    }

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
 
ᶎᦶ᷌
 
 
1. JDBC඙֢හഝପጱྍṈ Ҙ
 
JDBC඙֢හഝପጱྍṈ Ҙ
1. ဳٙහഝପḝ̶ۖ 
2. ୌᒈහഝପᬳള̶ 
3. ڠୌӞӻStatement̶ 
4. ಗᤈSQL᧍ݙ̶ 
5. ॒ቘᕮຎᵞ̶ 
6. ىᳮහഝପᬳള
դᎱইӥғ

![三歪教你学JDBC 第47页插图](../assets/images/三歪教你学JDBC_p47_1_3c233a1a.jpeg)

![三歪教你学JDBC 第47页插图](../assets/images/三歪教你学JDBC_p47_2_9ef93dcf.jpeg)

---

Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;
        try {
            /*
            * ے᫹ḝۖํӷᐿොୗ
            *
            * 1ғտ੕ᛘḝۖտဳٙӷེ҅ᬦଶׁᩢԭmysqlጱapi҅ᚙᐶጱmysqlጱ୏ݎ۱҅ᑕଧڞ
෫ဩᖫᦲ
            * 2ғḝۖݝտے᫹Ӟེ҅ӧᵱᥝׁᩢٍ֛ጱḝۖ҅ᅎၚ௔ṛ
            *
            * ౯ժӞᛱ᮷ฎֵአᒫԫᐿොୗ
            * */
            //1.
            //DriverManager.registerDriver(new com.mysql.jdbc.Driver());
            //2.
            Class.forName("com.mysql.jdbc.Driver");
            //឴ݐӨහഝପᬳളጱ੒᨝-Connetcion
            connection = 
DriverManager.getConnection("jdbc:mysql://localhost:3306/zhongfucheng", 
"root", "root");
            //឴ݐಗᤈsql᧍ݙጱstatement੒᨝
            statement = connection.createStatement();
            //ಗᤈsql᧍ݙ,೭کᕮຎᵞ
            resultSet = statement.executeQuery("SELECT * FROM users");
            //᭭ܲᕮຎᵞ҅஑کහഝ
            while (resultSet.next()) {
                System.out.println(resultSet.getString(1));
                System.out.println(resultSet.getString(2));
            }
            
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            /*

---

2. JDBCӾጱStatement ޾PreparedStatement҅
CallableStatementጱ܄ڦҘ
 
JDBCӾጱStatement ޾PreparedStatementጱ܄ڦҘ
܄ڦғ
PreparedStatementฎᶼᖫᦲጱSQL᧍ݙ҅පሲṛԭStatement̶ 
PreparedStatementඪ೮?඙֢ᒧ҅ፘ੒ԭStatementๅےᅎၚ̶ 
PreparedStatementݢզᴠྊSQLဳف҅ਞق௔ṛԭStatement̶
CallableStatementᭇአԭಗᤈਂؙᬦᑕ̶
3. JDBCӾय़හഝᰁጱړᶭᥴ٬ොဩ?
 
JDBCӾय़හഝᰁጱړᶭᥴ٬ොဩ?
๋অጱېဩฎڥአsql᧍ݙᬰᤈړᶭ҅ᬯ໏ྯེັᧃڊጱᕮຎᵞӾ੪ݝ۱ތ຤ᶭጱහഝٖ਻̶
            * ىᳮᩒრ҅ݸ᧣አጱضىᳮ
            *
            * ىᳮԏڹ҅ᥝڣෙ੒᨝ฎވਂࣁ
            * */
            if (resultSet != null) {
                try {
                    resultSet.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (statement != null) {
                try {
                    statement.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (connection != null) {
                try {
                    connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }

---

mysql᧍ဩғ
oracle᧍ဩғ
4. ᧔᧔හഝପᬳള࿰ૡ֢ܻቘ޾ਫሿොໜҘ
 
᧔᧔හഝପᬳള࿰ૡ֢ܻቘ޾ਫሿොໜҘ
ૡ֢ܻቘғ
๐ۓ࢏ސۖ෸տୌᒈӞਧහᰁጱ࿰ᬳള҅ଚӞፗᖌ೮ӧ੝ԭྌහፓጱ࿰ᬳള̶ਮಁᒒᑕଧᵱᥝᬳള
෸҅࿰ḝۖᑕଧտᬬࢧӞӻ๚ֵአጱ࿰ᬳളଚਖ਼ٌᤒᦕԅ஬̶ইຎ୮ڹဌํᑮᳳᬳള҅࿰ḝۖᑕଧ
੪ෛୌӞਧහᰁጱᬳള҅ෛୌᬳളጱහᰁํᯈᗝ݇හ٬ਧ̶୮ֵአጱ࿰ᬳള᧣አਠ౮ݸ҅࿰ḝۖᑕ
ଧਖ਼ྌᬳളᤒᦕԅᑮᳳٌ҅՜᧣አ੪ݢզֵአᬯӻᬳള̶
ਫሿොໜғᬳള࿰ֵአᵞݳ๶ᬰᤈᤰ᫹҅ᬬࢧጱConnectionฎܻতConnectionጱդቘ҅դቘ
Connectionጱcloseොဩ҅୮᧣አcloseොဩ෸҅ӧฎ፥ྋىᬳള҅ᘒฎ಩ਙդቘጱConnection੒᨝
නࢧکᬳള࿰Ӿ҅ᒵஇӥӞེ᯿॔ڥአ̶
 
ٍ֛դᎱғ
    SELECT *
    FROM ᤒݷ
    LIMIT [START], length;
    
    SELECT *FROM (
        SELECT ڜݷ,ڜݷ,ROWNUM rn
        FROM ᤒݷ
        WHERE ROWNUM<=(currentPage*lineSize)) temp
    
    WHERE temp.rn>(currentPage-1)*lineSize;
 @Override
    public Connection getConnection() throws SQLException {
        if (list.size() > 0) {
            final Connection connection = list.removeFirst();
            //፡፡࿰ጱय़ੜ
            System.out.println(list.size());
            //ᬬࢧӞӻۖாդቘ੒᨝

---

5. JavaӾই֜ᬰᤈԪۓጱ॒ቘ?
 
JavaӾই֜ᬰᤈԪۓጱ॒ቘ?
1. Ԫۓฎ֢ԅܔӻ᭦ᬋૡ֢ܔزಗᤈጱӞᔮڜ඙̶֢
2. Ӟӻ᭦ᬋૡ֢ܔز஠ᶳํࢥӻં௔҅ᑍԅܻৼ௔̵Ӟᛘ௔̵ᵍᐶ௔޾೮ԋ௔ (ACID) ં௔҅ݝํᬯ
໏಍ᚆ౮ԅӞӻԪۓ
ConnectionᔄӾ൉׀ԧ4ӻԪۓ॒ቘොဩ:
setAutoCommit(Boolean autoCommit):ᦡᗝฎވᛔۖ൉ԻԪۓ,ἕᦊԅᛔۖ൉Ի,ܨԅtrue,᭗ᬦᦡ
ᗝfalseᐬྊᛔۖ൉ԻԪۓ; 
commit():൉ԻԪۓ; 
rollback():ࢧ჻Ԫۓ.
savepoint:כਂᅩ
ဳ఺ғsavepointӧտᕮ๳୮ڹԪۓ҅ฦ᭗൉Ի޾ࢧ჻᮷տᕮ๳୮ڹԪۓጱ
6. ץදJDBCդᎱᨶᰁ
 
            return (Connection) 
Proxy.newProxyInstance(Demo1.class.getClassLoader(), 
connection.getClass().getInterfaces(), new InvocationHandler() {
                @Override
                public Object invoke(Object proxy, Method method, Object[] 
args) throws Throwable {
                    //ইຎӧฎ᧣አcloseොဩ҅੪ೲᆙྋଉጱ๶᧣አ
                    if (!method.getName().equals("close")) {
                        method.invoke(connection, args);
                    } else {
                        //ᬰکᬯ᯾๶҅᧔ก᧣አጱฎcloseොဩ
                        list.add(connection);
                        //ٚ፡፡࿰ጱय़ੜ
                        System.out.println(list.size());
                    }
                    return null;
                }
            });
        }
        return null;
    }

---

ӥᬿᑕଧฎӞྦྷᓌܔጱचԭJDBCጱහഝପᦢᳯդᎱ,ਫሿԧզӥۑᚆ:՗හഝପӾັᧃproductᤒӾ
ጱಅํᦕ୯,ᆐݸ಑ܦᬌڊکഴګݣ.ᧆդᎱᨶᰁ᫾֗,ইဌํྋᏟ॒ቘ୑ଉ,ᬳളਁᒧԀզ”ṹහ”ጱ୵
ୗፗളਂࣁԭդᎱӾᒵ,᧗አ֦ጱ௏᪠᯿ෛᖫٟᑕଧ,ਠ౮ፘݶጱۑᚆ,൉ṛդᎱᨶᰁ.
ܻ๶ጱդᎱғ
ץදݸጱդᎱғ
public void printProducts(){
    Connection c = null;
    Statements s = null;
    ResultSet r = null;
    try{
c=DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:sid","username
","password");
        s=c.createStatement();
        r=s.executeQuery("select id, name, price from product");
        System.out.println("Id\tName\tPrice");
        while(r.next()){
            int x = r.getInt("id");
            String y = r.getString("name");
            float z = r.getFloat("price");
            System.out.println(x + "\t" + y + "\t" + z);
        }
    } catch(Exception e){
    }
}
class Constant{
    public static final String URL="jdbc:oracle:thin:@127.0.0.1:1521:sid";
    public static final String USERNAME="username";
    public static final String PASSWORD="password";
}
class DAOException extends Exception{
    public DAOException(){
        super();
    }
    public DAOException(String msg){
        super(msg);
    }
}
public class Test{

---

ץදᅩғ
url̵passwordᒵמ௳ӧଫᧆፗളֵአਁᒧԀ“ٟྒ”҅ݢզֵአଉᰁդ๊
catchӾଫᧆࢧ჻Ԫۓ҅ಲڊRuntimeExceptionԞฎࢧ჻ԪۓጱӞᐿොဩ
ىᳮᩒრ
7. ٟڊӞྦྷJDBCᬳള๜๢MySQLහഝପጱդᎱ
 
ٟڊӞྦྷJDBCᬳള๜๢MySQLහഝପጱդᎱ
    public void printProducts() throws DAOException{
        Connection c = null;
        Statement s = null;
        ResultSet r = null;
        try{
            c = 
DriverManager.getConnection(Constant.URL,Constant.USERNAME,Constant.PASSWORD);
            s = c.createStatement();
            r = s.executeQuery("select id,name,price from product");
            System.out.println("Id\tName\tPrice");
            while(r.next()){
                int x = r.getInt("id");
                String y = r.getString("name");
                float z = r.getFloat("price");
                System.out.println(x + "\t" + y + "\t" + z);
            }
        } catch (SQLException e){
            throw new DAOException("හഝପ୑ଉ");
        } finally {
            try{
                r.close();
                s.close();
                c.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
Class.forName("com.mysql.jdbc.Driver");
String url="jdbc:mysql://localhost/test";
Stirng user='root';
String password='root';
Connection conn = DriverManager.getConnection(url,user,password);

---

8. JDBCฎই֜ਫሿJavaᑕଧ޾JDBCḝۖጱຂᘠݳጱҘ
 
JDBCฎই֜ਫሿJavaᑕଧ޾JDBCḝۖጱຂᘠݳጱҘ
᭗ᬦګਧളݗ҅හഝପܯࠟ๶ਫሿ̶౯ժݝᥝ᭗ᬦളݗ᧣አܨݢ̶ᵋ׎፡ӞӻᓌܔጱJDBCᐏֺ֦҅տݎ
ሿಅํ඙֢᮷ฎ᭗ᬦJDBCളݗਠ౮ጱ҅ᘒḝۖݝํࣁ᭗ᬦClass.forNameݍ੘๢ګ๶ے᫹ጱ෸ײ಍տ
ڊሿ̶
9. execute҅executeQuery҅executeUpdateጱ܄ڦฎ
ՋԍҘ
 
execute҅executeQuery҅executeUpdateጱ܄ڦฎՋԍҘ
Statementጱexecute(String query)ොဩአ๶ಗᤈձ఺ጱSQLັᧃ҅ইຎັᧃጱᕮຎฎӞӻ
ResultSet҅ᬯӻොဩ੪ᬬࢧtrue̶ইຎᕮຎӧฎResultSet҅ྲইinsert౲ᘏupdateັᧃ҅ਙ੪տ
ᬬࢧfalse̶౯ժݢզ᭗ᬦਙጱgetResultSetොဩ๶឴ݐResultSet҅౲ᘏ᭗ᬦgetUpdateCount()ො
ဩ๶឴ݐๅෛጱᦕ୯๵හ̶
StatementጱexecuteQuery(String query)ളݗአ๶ಗᤈselectັᧃ҅ଚӬᬬࢧResultSet̶ܨֵັ
ᧃӧکᦕ୯ᬬࢧጱResultSetԞӧտԅnull̶౯ժ᭗ଉֵአexecuteQuery๶ಗᤈັᧃ᧍ݙ҅ᬯ໏ጱ
ᦾইຎփᬰ๶ጱฎinsert౲ᘏupdate᧍ݙጱᦾ҅ਙտಲڊᲙ᧏מ௳ԅ “executeQuery method can 
not be used for update”ጱjava.util.SQLException̶
StatementጱexecuteUpdate(String query)ොဩአ๶ಗᤈinsert౲ᘏupdate/deleteҁDML҂᧍
ݙ҅౲ᘏ ՋԍԞӧᬬࢧDDL᧍ݙ̶ᬬࢧ꧊ฎintᔄࣳ҅ইຎฎDML᧍ݙጱᦾ҅ਙ੪ฎๅෛጱ๵හ҅
ইຎฎDDLጱᦾ҅੪ᬬࢧ0̶
ݝํ୮֦ӧᏟਧฎՋԍ᧍ݙጱ෸ײ಍ଫᧆֵአexecute()ොဩ҅ވڞଫᧆֵአexecuteQuery౲ᘏ
executeUpdateොဩ̶

![三歪教你学JDBC 第54页插图](../assets/images/三歪教你学JDBC_p54_1_b6d2079a.jpeg)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y
10. PreparedStatementጱᗌᅩฎՋԍ҅ெԍᥴ٬ᬯӻᳯ
᷌Ҙ
 
PreparedStatementጱᗌᅩฎՋԍ҅ெԍᥴ٬ᬯӻᳯ᷌Ҙ
 
PreparedStatementጱӞӻᗌᅩฎ҅౯ժӧᚆፗളአਙ๶ಗᤈin๵կ᧍ݙҔᵱᥝಗᤈIN๵կ᧍ݙጱᦾ҅
ӥᶎํӞԶᥴ٬ොໜғ
ړڦᬰᤈܔ๵ັᧃ——ᬯ໏؉௔ᚆஉ૧҅ӧവគ̶
ֵአਂؙᬦᑕ——ᬯݐ٬ԭහഝପጱਫሿ҅ӧฎಅํහഝପ᮷ඪ೮̶
ۖாኞ౮PreparedStatement——ᬯฎӻঅېဩ҅֕ฎӧᚆՁݑPreparedStatementጱᖨਂଃ๶
ጱঅ॒ԧ̶
ࣁPreparedStatementັᧃӾֵአNULL꧊——ইຎ֦Ꭳ᭲ᬌفݒᰁጱ๋य़ӻහጱᦾ҅ᬯฎӻӧᲙ
ጱېဩ҅ಘ઀Ӟӥᬮݢզඪ೮෫ᴴ݇හ̶
 
11. JDBCጱᚍ᧛ฎՋԍҘߺᐿහഝପᵍᐶᕆڦᚆᴠྊᚍ
᧛Ҙ
 
JDBCጱᚍ᧛ฎՋԍҘߺᐿහഝପᵍᐶᕆڦᚆᴠྊᚍ᧛Ҙ
ᚍ᧛ғӞӻԪۓ᧛ݐکݚक़ӞӻԪۓ๚൉Իጱහഝ
ֺৼғAݻB᫨ᨴ҅Aಗᤈԧ᫨ᨴ᧍ݙ҅֕Aᬮဌํ൉ԻԪۓ҅B᧛ݐහഝ҅ݎሿᛔ૩ᨴಁ᰸ݒग़ԧѺB᪙
A᧔҅౯૪ᕪතک᰸ԧ̶Aࢧ჻Ԫۓ̓rollback̈́҅ᒵBٚັ፡ᨴಁጱ᰸෸҅ݎሿ᰸ଚဌํग̶़
ӥᶎጱӣᐿӻᵍᐶᕆڦ᮷ݢզᴠྊғ
Serializable̓TRANSACTION_SERIALIZABLË́
Repeatable read̓TRANSACTION_REPEATABLE_READ̈́

![三歪教你学JDBC 第55页插图](../assets/images/三歪教你学JDBC_p55_1_3c233a1a.jpeg)

---

Read committed̓TRANSACTION_READ_COMMITTED̈́
12. Ջԍฎଝ᧛҅ߺᐿᵍᐶᕆڦݢզᴠྊଝ᧛Ҙ
 
Ջԍฎଝ᧛҅ߺᐿᵍᐶᕆڦݢզᴠྊଝ᧛Ҙ
ฎ೰ࣁӞӻԪۓٖ᧛ݐکԧڦጱԪۓൊفጱහഝ҅੕ᛘڹݸ᧛ݐӧӞᛘ̶
ݝํTRANSACTION_SERIALIZABLEᵍᐶᕆڦ಍ᚆᴠྊԾኞଝ᧛̶
13. JDBCጱDriverManagerฎአ๶؉ՋԍጱҘ
 
JDBCጱDriverManagerฎአ๶؉ՋԍጱҘ 
JDBCጱDriverManagerฎӞӻૡܯᔄ҅౯ժ᭗ᬦਙ๶ڠୌහഝପᬳള̶
୮JDBCጱDriverᔄᤩے᫹ᬰ๶෸҅ਙտᛔ૩ဳٙکDriverManagerᔄ᯾ᶎ
ᆐݸ౯ժտ಩හഝପᯈᗝמ௳փ౮DriverManager.getConnection()ොဩ҅DriverManagerտֵ
አဳٙکਙ᯾ᶎጱḝۖ๶឴ݐහഝପᬳള҅ଚᬬࢧᕳ᧣አጱᑕଧ̶
 
14. JDBCጱResultSetฎՋԍҘ
 
JDBCጱResultSetฎՋԍ?
ࣁັᧃහഝପݸտᬬࢧӞӻResultSet҅ਙ੪؟ฎັᧃᕮຎᵞጱӞୟහഝᤒ̶ 
ResultSet੒᨝ᖌಷԧӞӻ჋ຽ҅೰ݻ୮ڹጱහഝᤈ̶୏তጱ෸ײᬯӻ჋ຽ೰ݻጱฎᒫӞᤈ̶ইຎ
᧣አԧResultSetጱnext()ොဩ჋ຽտӥᑏӞᤈ҅ইຎဌํๅग़ጱහഝԧ҅next()ොဩտᬬࢧfalse̶
ݢզࣁfor஗ሾӾአਙ๶᭭ܲහഝᵞ̶ 
ἕᦊጱResultSetฎӧᚆๅෛጱ҅჋ຽԞݝᚆஃӥᑏ̶Ԟ੪ฎ᧔֦ݝᚆ՗ᒫӞᤈک๋ݸӞᤈ᭭ܲӞ
̶᭭ӧᬦԞݢզڠୌݢզࢧ჻౲ᘏݢๅෛጱResultSet
୮ኞ౮ResultSetጱStatement੒᨝ᥝىᳮ౲ᘏ᯿ෛಗᤈ౲ฎ឴ݐӥӞӻResultSetጱ෸ײ҅
ResultSet੒᨝Ԟտᛔۖىᳮ̶ 
ݢզ᭗ᬦResultSetጱgetterොဩ҅փفڜݷ౲ᘏ՗1୏তጱଧݩ๶឴ݐڜහഝ̶ 
15. ํߺԶӧݶጱResultSetҘ
 
ํߺԶӧݶጱResultSetҘ
໑ഝڠୌStatement෸ᬌف݇හጱӧݶ҅տ੒ଫӧݶᔄࣳጱResultSet̶ইຎ֦፡ӥConnectionጱො
ဩ֦҅տݎሿcreateStatement޾prepareStatementොဩ᯿᫹ԧ҅զඪ೮ӧݶጱResultSet޾ଚݎᔄ
̶ࣳ
ӞوํӣᐿResultSet੒᨝̶
ResultSet.TYPE_FORWARD_ONLYғᬯฎἕᦊጱᔄࣳ҅ਙጱ჋ຽݝᚆஃӥᑏ̶
ResultSet.TYPE_SCROLL_INSENSITIVEғ჋ຽݢզӤӥᑏۖ҅Ӟ෮ਙڠୌݸ҅හഝପ᯾ጱහഝٚ
ݎኞץද҅੒ਙ๶᧔ฎ᭐กጱ̶ 
ResultSet.TYPE_SCROLL_SENSITIVEғ჋ຽݢզӤӥᑏۖ҅ইຎኞ౮ݸහഝପᬮݎኞԧץද඙
֢҅ਙฎᚆड़ఽᎣکጱ̶

---

ResultSetํӷᐿଚݎᔄ̶ࣳ
ResultSet.CONCUR_READ_ONLY:ResultSetฎݝ᧛ጱ҅ᬯฎἕᦊᔄ̶ࣳ
ResultSet.CONCUR_UPDATABLE:౯ժݢզֵአResultSetጱๅෛොဩ๶ๅෛ᯾ᶎጱහഝ̶
16. JDBCጱDataSourceฎՋԍ҅ํՋԍঅ॒
 
JDBCጱDataSourceฎՋԍ҅ํՋԍঅ॒
DataSourceܨහഝრ҅ਙฎਧԎࣁjavax.sqlӾጱӞӻളݗ҅᪙DriverManagerፘྲ҅ਙጱۑᚆᥝๅ୩
य̶़౯ժݢզአਙ๶ڠୌහഝପᬳള҅୮ᆐḝۖጱਫሿᔄտਫᴬ݄ਠ౮ᬯӻૡ̶֢ᴻԧᚆڠୌᬳളक़҅
ਙᬮ൉׀ԧইӥጱᇙ௔ғ
ᖨਂPreparedStatementզ׎ๅளጱಗᤈ
ݢզᦡᗝᬳള᩻෸෸ᳵ
൉׀෭பᦕ୯ጱۑᚆ
ResultSetय़ੜጱ๋य़ᴇ꧊ᦡᗝ
᭗ᬦJNDIጱඪ೮҅ݢզԅservlet਻࢏൉׀ᬳള࿰ጱۑᚆ
17 .ই֜᭗ᬦJDBCጱDataSource޾Apache Tomcatጱ
JNDI๶ڠୌᬳള࿰Ҙ
 
ই֜᭗ᬦJDBCጱDataSource޾Apache TomcatጱJNDI๶ڠୌᬳള࿰Ҙ
 
Tomcat๐ۓ࢏Ԟᕳ౯ժ൉׀ԧᬳള࿰ٖ҅᮱ٌਫ੪ฎDBCP
ྍṈғ
1. ࣁMETA-INFፓ୯ӥᯈᗝcontext.xml෈կ̓෈կٖ਻ݢզࣁtomcatἕᦊᶭᶎጱ JNDI Resourcesӥ
Conﬁgure Tomcat's Resource Factoryತک̈́
2. ੕فMysql౲oracle୏ݎ۱کtomcatጱlibፓ୯ӥ
3. ڡত۸JNDI->឴ݐJNDI਻࢏->༄ᔱզXXXԅݷਁࣁJNDI਻࢏ਂනጱᬳള࿰
context.xml෈կጱᯈᗝғ
<Context>
  <Resource name="jdbc/EmployeeDB"
            auth="Container"
            type="javax.sql.DataSource"
            
            username="root"
            password="root"
            driverClassName="com.mysql.jdbc.Driver"
            url="jdbc:mysql://localhost:3306/zhongfucheng"
            maxActive="8"
            maxIdle="4"/>
</Context>

---

18. ApacheጱDBCPฎՋԍҘ
 
ApacheጱDBCPฎՋԍ
 
ইຎአDataSource๶឴ݐᬳളጱᦾ҅᭗ଉ឴ݐᬳളጱդᎱ޾ḝۖᇙਧጱDataSourceฎᔲᘠݳጱ̶ݚ
क़҅ᴻԧᭌೠDataSourceጱਫሿᔄ҅ۃӥጱդᎱच๜᮷ฎӞ໏ጱ̶
ApacheጱDBCP੪ฎአ๶ᥴ٬ᬯԶᳯ᷌ጱ҅ਙ൉׀ጱDataSourceਫሿ౮ԅԧଫአᑕଧ޾ӧݶJDBCḝۖ
ᳵጱӞӻು᨝੶̶ApacheጱDBCPପׁᩢcommons-poolପ҅ಅզᥝᏟכਙժ᮷ࣁ᮱ᗟ᪠ஆӥ̶
ֵአDBCPහഝრጱྍṈғ
1. ੕فӷӻjar۱̓Commons-dbcp.jar޾Commons-pool.jar̈́
2. ᧛ݐᯈᗝ෈կ
3. ឴ݐBasicDataSourceFactory੒᨝
4. ڠୌDataSource੒᨝
        try {
      //ڡত۸JNDI਻࢏
            Context initCtx = new InitialContext();
      //឴ݐکJNDI਻࢏
            Context envCtx = (Context) initCtx.lookup("java:comp/env");
      //ಚൈզjdbc/EmployeeDBݷਁᕬਧࣁJNDI਻࢏ӥጱᬳള࿰
            DataSource ds = (DataSource)
                    envCtx.lookup("jdbc/EmployeeDB");
            Connection conn = ds.getConnection();
            System.out.println(conn);
        } 
    private static DataSource dataSource = null;
    static {
        try {
            //᧛ݐᯈᗝ෈կ
            InputStream inputStream = 
Demo3.class.getClassLoader().getResourceAsStream("dbcpconfig.properties");
            Properties properties = new Properties();
            properties.load(inputStream);

---

//឴ݐૡܯ੒᨝
            BasicDataSourceFactory basicDataSourceFactory = new 
BasicDataSourceFactory();
            dataSource = basicDataSourceFactory.createDataSource(properties);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static Connection getConnection() throws SQLException {
        return dataSource.getConnection();
    }
    //ᬯ᯾᯽නᩒრӧฎ಩හഝପጱᇔቘᬳള᯽නԧ҅ฎ಩ᬳള୭ᬮᕳᬳള࿰̓ᬳള࿰ጱConnectionٖ
᮱ᛔ૩؉অԧ̈́
    public static void release(Connection conn, Statement st, ResultSet rs) {
        if (rs != null) {
            try {
                rs.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
            rs = null;
        }
        if (st != null) {
            try {
                st.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        if (conn != null) {
            try {
                conn.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

---

19. ଉᥠጱJDBC୑ଉํߺԶҘ
 
ଉᥠጱJDBC୑ଉํߺԶҘ
ํզӥᬯԶғ
java.sql.SQLException——ᬯฎJDBC୑ଉጱचᔄ̶
java.sql.BatchUpdateException——୮ಢ॒ቘ඙֢ಗᤈ०ᨳጱ෸ײݢᚆտಲڊᬯӻ୑ଉ̶ᬯݐ٬
ԭٍ֛ጱJDBCḝۖጱਫሿ҅ਙԞݢᚆፗളಲڊचᔄ୑ଉjava.sql.SQLException̶
java.sql.SQLWarning——SQL඙֢ڊሿጱᦄޞמ௳̶
java.sql.DataTruncation——ਁྦྷ꧊ኧԭ຤Զᶋྋଉܻࢩᤩ౼ෙԧҁӧฎࢩԅ᩻ᬦ੒ଫਁྦྷᔄࣳጱ
ᳩଶᴴګ҂̶
 
ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y

![三歪教你学JDBC 第60页插图](../assets/images/三歪教你学JDBC_p60_1_b6d2079a.jpeg)

![三歪教你学JDBC 第60页插图](../assets/images/三歪教你学JDBC_p60_2_3c233a1a.jpeg)

---

20. JDBCӾਂࣁߺԶӧݶᔄࣳጱᲁҘ
 
JDBCӾਂࣁߺԶӧݶᔄࣳጱᲁ?
՗ଠԎӤᦖ҅ํӷᐿᲁ๢ګ๶ᴠྊग़ӻአಁݶ෸඙֢୚᩸ጱහഝഖ̶ࣕ
Ԕᥡᲁ——ݝํ୮ๅෛහഝጱ෸ײ಍տᲁਧᦕ୯̶ 
ఓᥡᲁ——՗ັᧃکๅෛ޾൉Իෆӻᬦᑕ᮷տ੒හഝᦕ୯ᬰᤈےᲁ̶
21. java.util.Date޾java.sql.DateํՋԍ܄ڦҘ
 
java.util.Date޾java.sql.DateํՋԍ܄ڦҘ
java.util.Date۱ތ෭๗޾෸ᳵ҅ᘒjava.sql.Dateݝ۱ތ෭๗מ௳҅ᘒဌํٍ֛ጱ෸ᳵמ௳̶ইຎ֦మ಩
෸ᳵמ௳ਂؙࣁහഝପ᯾҅ݢզᘍᡤֵአTimestamp౲ᘏDateTimeਁྦྷ
22. SQLWarningฎՋԍ҅ࣁᑕଧӾই֜឴ݐ
SQLWarningҘ
 
SQLWarningฎՋԍ҅ࣁᑕଧӾই֜឴ݐSQLWarningҘ
SQLWarningฎSQLExceptionጱৼᔄ҅᭗ᬦConnection, Statement, ResultጱgetWarningsොဩ᮷
ݢզ឴ݐکਙ̶ SQLWarningӧտӾෙັᧃ᧍ݙጱಗᤈ҅ݝฎአ๶൉ᐏአಁਂࣁፘىጱᦄޞמ௳̶
23. ইຎjava.sql.SQLException: No suitable driver
foundᧆெԍېҘ
 
ইຎjava.sql.SQLException: No suitable driver foundᧆெԍېҘ
ইຎ֦ጱSQL URLԀ໒ୗӧྋᏟጱᦾ҅੪տಲڊᬯ໏ጱ୑ଉ̶ӧᓕฎֵአDriverManagerᬮฎJNDIහഝ
რ๶ڠୌᬳള᮷ํݢᚆಲڊᬯᐿ୑ଉ̶ਙጱ୑ଉ຾፡᩸๶տ؟ӥᶎᬯ໏̶

---

ᥴ٬ᬯᔄᳯ᷌ጱොဩ੪ฎ҅༄ັӥ෭ப෈կ҅؟Ӥᶎጱᬯӻ෭பӾ҅URLԀ
ฎ'jdbc:mysql://localhost:3306/UserDB҅ݝᥝ಩ਙද౮jdbc:mysql://localhost:3306/UserDB੪অ
ԧ̶
24. JDBCጱRowSetฎՋԍ҅ํߺԶӧݶጱRowSetҘ
 
JDBCጱRowSetฎՋԍ҅ํߺԶӧݶጱRowSetҘ
RowSetአԭਂؙັᧃጱහഝᕮຎ҅޾ResultSetፘྲ҅ਙๅٍᅎၚ௔̶RowSetᖀಥᛔResultSet҅ࢩྌ
ResultSetᚆଗጱ҅ਙժԞᚆ҅ᘒResultSet؉ӧکጱ҅ਙժᬮฎݢզ̶RowSetളݗਧԎࣁjavax.sql۱
᯾̶
RowSet൉׀ጱ᷐क़ጱᇙ௔ํғ
൉׀ԧJava Beanጱۑᚆ҅ݢզ᭗ᬦsettter޾getterොဩ๶ᦡᗝ޾឴ݐં௔̶RowSetֵአԧ
JavaBeanጱԪկḝۖཛྷࣳ҅ਙݢզᕳဳٙጱᕟկݎᭆԪկ᭗Ꭳ҅ྲই჋ຽጱᑏۖ҅ᤈጱीڢද҅
զ݊RowSetٖ਻ጱץදᒵ̶
RowSet੒᨝ἕᦊฎݢ჻ۖ҅ݢๅෛጱ҅ࢩྌইຎහഝପᔮᕹӧඪ೮ResultSetਫሿᔄ֒ጱۑᚆ҅
ݢզֵአRowSet๶ਫሿ̶
RowSetړԅӷय़ᔄғ
A. ᬳളࣳRowSet——ᬯᔄ੒᨝Өහഝପᬰᤈᬳള҅޾ResultSetஉᔄ̶֒JDBCളݗݝ൉׀ԧӞᐿ
ᬳളࣳRowSet҅javax.sql.rowset.JdbcRowSet҅ਙጱຽٵਫሿฎ
com.sun.rowset.JdbcRowSetImpl̶ 
B. ᐶᕚࣳRowSet——ᬯᔄ੒᨝ӧᵱᥝ޾හഝପᬰᤈᬳള҅ࢩྌਙժๅ᫷ᰁᕆ҅ๅ਻ฃଧڜ۸̶ਙ
ժᭇአԭࣁᗑᕶᳵփ᭓හഝ̶
org.apache.tomcat.dbcp.dbcp.SQLNestedException: Cannot create JDBC driver of 
class 'com.mysql.jdbc.Driver' for connect URL 
''jdbc:mysql://localhost:3306/UserDB'
    at 
org.apache.tomcat.dbcp.dbcp.BasicDataSource.createConnectionFactory(BasicDataS
ource.java:1452)
    at 
org.apache.tomcat.dbcp.dbcp.BasicDataSource.createDataSource(BasicDataSource.j
ava:1371)
    at 
org.apache.tomcat.dbcp.dbcp.BasicDataSource.getConnection(BasicDataSource.java
:1044)
java.sql.SQLException: No suitable driver found for 
'jdbc:mysql://localhost:3306/UserDB
    at java.sql.DriverManager.getConnection(DriverManager.java:604)
    at java.sql.DriverManager.getConnection(DriverManager.java:221)
    at com.journaldev.jdbc.DBConnection.getConnection(DBConnection.java:24)
    at com.journaldev.jdbc.DBConnectionTest.main(DBConnectionTest.java:15)
Exception in thread "main" java.lang.NullPointerException
    at com.journaldev.jdbc.DBConnectionTest.main(DBConnectionTest.java:16)

---

ํࢥᐿӧݶጱᐶᕚࣳRowSetጱਫሿ̶
CachedRowSet——ݢզ᭗ᬦ՜ժ឴ݐᬳള҅ಗᤈັᧃଚ᧛ݐResultSetጱහഝک
RowSet᯾̶౯ժݢզࣁᐶᕚ෸੒හഝᬰᤈᖌಷ޾ๅෛ҅ᆐݸ᯿ෛᬳളکහഝପ᯾҅ଚࢧ
ٟදۖጱහഝ̶
WebRowSetᖀಥᛔCachedRowSet——՜ݢզ᧛ٟXML෈໩̶
JoinRowSetᖀಥᛔWebRowSet——ਙӧአᬳളහഝପ੪ݢզಗᤈSQLጱjoin඙̶֢
FilteredRowSetᖀಥᛔWebRowSet——౯ժݢզአਙ๶ᦡᗝᬦᄁᥢڞ҅ᬯ໏ݝํᭌӾ
ጱහഝ಍ݢᥠ̶
 
25. ՋԍฎJDBCጱ๋֯ਫ᪢Ҙ
 
̴ՋԍฎJDBCጱ๋֯ਫ᪢Ҙ
හഝପᩒრฎᶋଉ෼ᩃጱ҅አਠԧଫᧆੱளىᳮਙ̶Connection, Statement, ResultSetᒵJDBC੒
᨝᮷ํcloseොဩ҅᧣አਙ੪অԧ̶
ِ౮ࣁդᎱӾดୗىᳮധResultSet҅Statement҅Connectionጱԟబ҅ইຎ֦አጱฎᬳള࿰ጱ
ᦾ҅ᬳളአਠݸտනࢧ࿰᯾҅֕ฎဌํىᳮጱResultSet޾Statement੪տ᭜౮ᩒრအᄋԧ̶
ࣁﬁnallyࣘӾىᳮᩒრ҅כᦤܨ׎ڊԧ୑ଉԞᚆྋଉىᳮ̶
य़ᰁᔄ֒ጱັᧃଫ୮ֵአಢ॒ቘਠ౮̶
ੱᰁֵአPreparedStatementᘒӧฎStatement҅զ᭿عSQLဳف҅ݶ෸ᬮᚆ᭗ᬦᶼᖫᦲ޾ᖨਂ
๢ګ൉܋ಗᤈጱපሲ̶
ইຎ֦ᥝਖ਼य़ᰁහഝ᧛فکResultSetӾ҅ଫᧆݳቘጱᦡᗝfetchSizeզ׎൉܋௔ᚆ̶
֦አጱහഝପݢᚆဌํඪ೮ಅํጱᵍᐶᕆڦ҅አԏڹض՚ᕡᏟᦊӥ̶
හഝପᵍᐶᕆڦ᩼ṛ௔ᚆ᩼૧҅Ꮯכ֦ጱහഝପᬳളᦡᗝጱᵍᐶᕆڦฎ๋սጱ̶
ইຎࣁWEBᑕଧӾڠୌහഝପᬳള๋҅অ᭗ᬦJNDIֵአJDBCጱහഝრ҅ᬯ໏ݢզ੒ᬳളᬰᤈ᯿
አ̶
ইຎ֦ᵱᥝᳩ෸ᳵ੒ResultSetᬰᤈ඙֢ጱᦾ҅ੱᰁֵአᐶᕚጱRowSet̶

![三歪教你学JDBC 第63页插图](../assets/images/三歪教你学JDBC_p63_1_2e4b8626.png)

---

ইຎ෈໩Ӿํձ֜ጱӧ౜ጱᳯ᷌҅᮷ݢզፗള๶ತ౯ᧃᳯ҅౯Ԕ఺ଆ֦ۗժѺஙמ൤Java3yلռݩํ౯
ጱᘶᔮොୗ̶ๅग़ܻڠದ๞෈ᒍݢىဳ౯ጱGitHubғhttps://github.com/ZhongFuCheng3y/3y

![三歪教你学JDBC 第64页插图](../assets/images/三歪教你学JDBC_p64_1_3c233a1a.jpeg)