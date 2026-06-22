---
title: 【美团】Java 岗 154 道面试题
source: Note/【美团】Java 岗 154 道面试题.pdf
pages: 12
converted_at: 2026-06-22 22:28:48
---

# 【美团】Java 岗 154 道面试题

【美团】Java 岗154 道面试题
Java 集合22 题
1.
ArrayList 和Vector 的区别。
2.
说说ArrayList，Vector，LinkedList 的存储性能和特性。
3.
快速失败(fail-fast) 和安全失败(fail-safe) 的区别是什么？
4.
HashMap 的数据结构。
5.
HashMap 的工作原理是什么？
6.
Hashmap 什么时候进行扩容呢？
7.
List、Map、Set 三个接口，存取元素时，各有什么特点？
8.
Set 里的元素是不能重复的，那么用什么方法来区分重复与否呢？是用==
还是equals()? 它们有何区别？
9.
两个对象值相同(x.equals(y) == true)，但却可有不同的hash code，这句
话对不对？
10. Heap 和Stack 有什么区别。
11. Java 集合类框架的基本接口有哪些？
12. HashSet 和TreeSet 有什么区别？
13. HashSet 的底层实现是什么？
14. LinkedHashMap 的实现原理？
15. 为什么集合类没有实现Cloneable 和Serializable 接口？
16. 什么是迭代器(Iterator)？
微信公众号：Java架构师进阶编程

![【美团】Java 岗 154 道面试题 第1页插图](../assets/images/【美团】Java_岗_154_道面试题_p1_1_0b055075.png)

---

17. Iterator 和ListIterator 的区别是什么？
18. 数组(Array) 和列表(ArrayList) 有什么区别？什么时候应该使用Array 而
不是ArrayList？
19. Java 集合类框架的最佳实践有哪些？
20. Set 里的元素是不能重复的，那么用什么方法来区分重复与否呢？是用==
还是equals()？它们有何区别？
21. Comparable 和Comparator 接口是干什么的？列出它们的区别。
22. Collection 和Collections 的区别。
JVM 与调优21 题
23. Java 类加载过程？
24. 描述一下JVM 加载Class 文件的原理机制?
25. Java 内存分配。
26. GC 是什么? 为什么要有GC？
27. 简述Java 垃圾回收机制
28. 如何判断一个对象是否存活？（或者GC 对象的判定方法）
29. 垃圾回收的优点和原理。并考虑2 种回收机制
微信公众号：Java架构师进阶编程

---

30. 垃圾回收器的基本原理是什么？垃圾回收器可以马上回收内存吗？有什么
办法主动通知虚拟机进行垃圾回收？
31. Java 中会存在内存泄漏吗，请简单描述
32. 深拷贝和浅拷贝。
33. System.gc() 和Runtime.gc() 会做什么事情？
34. finalize() 方法什么时候被调用？析构函数(finalization) 的目的是什么？
35. 如果对象的引用被置为null，垃圾收集器是否会立即释放对象占用的内存？
36. 什么是分布式垃圾回收（DGC）？它是如何工作的？
37. 串行（serial）收集器和吞吐量（throughput）收集器的区别是什么？
38. 在Java 中，对象什么时候可以被垃圾回收？
39. 简述Java 内存分配与回收策率以及Minor GC 和Major GC。
40. JVM 的永久代中会发生垃圾回收么？
41. Java 中垃圾收集的方法有哪些？
42. 什么是类加载器，类加载器有哪些？
43. 类加载器双亲委派模型机制？
微信公众号：Java架构师进阶编程

---

并发编程28 题
44. Synchronized 用过吗，其原理是什么？
45. 你刚才提到获取对象的锁，这个“锁”到底是什么？如何确定对象的锁？
46. 什么是可重入性，为什么说Synchronized 是可重入锁？
47. JVM 对Java 的原生锁做了哪些优化？
48. 为什么说Synchronized 是非公平锁？
49. 什么是锁消除和锁粗化？
50. 为什么说Synchronized 是一个悲观锁？乐观锁的实现原理又是什么？什
么是CAS，它有什么特性？
51. 乐观锁一定就是好的吗？
52. 跟Synchronized 相比，可重入锁ReentrantLock 其实现原理有什么不
同？
53. 那么请谈谈AQS 框架是怎么回事儿？
54. 请尽可能详尽地对比下Synchronized 和ReentrantLock 的异同。
55. ReentrantLock 是如何实现可重入性的？
56. 除了ReetrantLock，你还接触过JUC 中的哪些并发工具？
57. 请谈谈ReadWriteLock 和StampedLock。
58. 如何让Java 的线程彼此同步？你了解过哪些同步器？请分别介绍下。
59. CyclicBarrier 和CountDownLatch 看起来很相似，请对比下呢？
微信公众号：Java架构师进阶编程

---

60. Java 线程池相关问题
61. Java 中的线程池是如何实现的？
62. 创建线程池的几个核心构造参数？
63. 线程池中的线程是怎么创建的？是一开始就随着线程池的启动创建好的
吗？
64. 既然提到可以通过配置不同参数创建出不同的线程池，那么Java 中默认实
现好的线程池又有哪些呢？请比较它们的异同
65. 如何在Java 线程池中提交线程？
66. 什么是Java 的内存模型，Java 中各个线程是怎么彼此看到对方的变量
的？
67. 请谈谈volatile 有什么特点，为什么它能保证变量对所有线程的可见性？
68. 既然volatile 能够保证线程间的变量可见性，是不是就意味着基于volatile
变量的运算就是并发安全的？
69. 请对比下volatile 对比Synchronized 的异同。
70. 请谈谈ThreadLocal 是怎么解决并发安全的？
71. 很多人都说要慎用ThreadLocal，谈谈你的理解，使用ThreadLocal 需要
注意些什么？
Spring 25 题
微信公众号：Java架构师进阶编程

---

72. 什么是Spring 框架？Spring 框架有哪些主要模块？
73. 使用Spring 框架能带来哪些好处？
74. 什么是控制反转(IOC)？什么是依赖注入？
75. 请解释下Spring 框架中的IoC？
76. BeanFactory 和ApplicationContext 有什么区别？
77. Spring 有几种配置方式？
78. 如何用基于XML 配置的方式配置Spring？
79. 如何用基于Java 配置的方式配置Spring？
80. 怎样用注解的方式配置Spring？
81. 请解释Spring Bean 的生命周期？
82. Spring Bean 的作用域之间有什么区别？
83. 什么是Spring inner beans？
84. Spring 框架中的单例Beans 是线程安全的么？
85. 请举例说明如何在Spring 中注入一个Java Collection？
86. 如何向Spring Bean 中注入一个Java.util.Properties？
87. 请解释Spring Bean 的自动装配？
88. 请解释自动装配模式的区别？
89. 如何开启基于注解的自动装配？
90. 请举例解释@Required 注解？
91. 请举例解释@Autowired 注解？
92. 请举例说明@Qualifier 注解？
93. 构造方法注入和设值注入有什么区别？
微信公众号：Java架构师进阶编程

---

94. Spring 框架中有哪些不同类型的事件？
95. FileSystemResource 和ClassPathResource 有何区别？
96. Spring 框架中都用到了哪些设计模式？
设计模式10 题
97. 请列举出在JDK 中几个常用的设计模式？
98. 什么是设计模式？你是否在你的代码里面使用过任何设计模式？
99. Java 中什么叫单例设计模式？请用Java 写出线程安全的单例模式
100.
在Java 中，什么叫观察者设计模式（observer design pattern）？
101.
使用工厂模式最主要的好处是什么？在哪里使用？
102.
举一个用Java 实现的装饰模式(decorator design pattern)？它是作用
于对象层次还是类层次？
103.
在Java 中，为什么不允许从静态方法中访问非静态变量？
104.
设计一个ATM 机，请说出你的设计思路？
微信公众号：Java架构师进阶编程

---

105.
在Java 中，什么时候用重载，什么时候用重写？
106.
举例说明什么情况下会更倾向于使用抽象类而不是接口
SpringBoot 22 题
107.
什么是Spring Boot？
108.
Spring Boot 有哪些优点？
109.
什么是JavaConfig？
110.
如何重新加载Spring Boot 上的更改，而无需重新启动服务器？
微信公众号：Java架构师进阶编程

---

111.
Spring Boot 中的监视器是什么？
112.
如何在Spring Boot 中禁用Actuator 端点安全性？
113.
如何在自定义端口上运行Spring Boot 应用程序？
114.
什么是YAML？
115.
如何实现Spring Boot 应用程序的安全性？
116.
如何集成Spring Boot 和ActiveMQ？
117.
如何使用Spring Boot 实现分页和排序？
118.
什么是Swagger？你用Spring Boot 实现了它吗？
119.
什么是Spring Profiles？
120.
什么是Spring Batch？
121.
什么是FreeMarker 模板？
122.
如何使用Spring Boot 实现异常处理？
123.
您使用了哪些starter maven 依赖项？
124.
什么是CSRF 攻击？
125.
什么是WebSockets？
126.
什么是AOP？
127.
什么是Apache Kafka？
128.
我们如何监视所有Spring Boot 微服务？
微信公众号：Java架构师进阶编程

---

Netty10 题
129.
BIO、NIO 和AIO 的区别？
130.
NIO 的组成？
131.
Netty 的特点？
132.
Netty 的线程模型？
133.
TCP 粘包/拆包的原因及解决方法？
134.
了解哪几种序列化协议？
135.
如何选择序列化协议？
136.
Netty 的零拷贝实现？
137.
Netty 的高性能表现在哪些方面？
138.
NIOEventLoopGroup 源码？
微信公众号：Java架构师进阶编程

---

Redis 16 题
139.
什么是redis?
140.
Reids 的特点
141.
Redis 支持的数据类型
142.
Redis 是单进程单线程的
143.
虚拟内存
144.
Redis 锁
145.
读写分离模型
146.
数据分片模型
147.
Redis 的回收策略
148.
使用Redis 有哪些好处？
149.
redis 相比memcached 有哪些优势？
150.
redis 常见性能问题和解决方案
微信公众号：Java架构师进阶编程

---

151.
MySQL 里有2000w 数据，redis 中只存20w 的数据，如何保证redis
中的数据都是热点数据245
152.
Memcache 与Redis 的区别都有哪些？
153.
Redis 常见的性能问题都有哪些？如何解决？
154.
Redis 最适合的场景
微信公众号：Java架构师进阶编程