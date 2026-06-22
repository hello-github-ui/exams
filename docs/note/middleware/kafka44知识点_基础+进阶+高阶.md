---
title: kafka44知识点（基础+进阶+高阶）
source: Note/kafka44知识点（基础+进阶+高阶）.pdf
pages: 31
converted_at: 2026-06-22 22:28:38
---

# kafka44知识点（基础+进阶+高阶）

Kafka 基础篇
1.Kafka 的用途有哪些？使用场景如何？
消息系统：Kafka 和传统的消息系统（也称作消息中间件）都具备系统解耦、冗余存储、
流量削峰、缓冲、异步通信、扩展性、可恢复性等功能。与此同时，Kafka 还提供了大多数
消息系统难以实现的消息顺序性保障及回溯消费的功能。
存储系统：Kafka 把消息持久化到磁盘，相比于其他基于内存存储的系统而言，有效地降
低了数据丢失的风险。也正是得益于Kafka 的消息持久化功能和多副本机制，我们可以把
Kafka 作为长期的数据存储系统来使用，只需要把对应的数据保留策略设置为“永久”或启
用主题的日志压缩功能即可。
流式处理平台：Kafka 不仅为每个流行的流式处理框架提供了可靠的数据来源，还提供了
一个完整的流式处理类库，比如窗口、连接、变换和聚合等各类操作。
2.Kafka 中的ISR、AR 又代表什么？ISR 的伸缩又指什么
分区中的所有副本统称为AR（Assigned Replicas）。所有与leader 副本保持一定程度同
步的副本（包括leader 副本在内）组成ISR（In-Sync Replicas），ISR 集合是AR 集合
中的一个子集。
ISR 的伸缩：
leader 副本负责维护和跟踪ISR 集合中所有follower 副本的滞后状态，当follower 副
本落后太多或失效时，leader 副本会把它从ISR 集合中剔除。如果OSR 集合中有
follower 副本“追上”了leader 副本，那么leader 副本会把它从OSR 集合转移至ISR
集合。默认情况下，当leader 副本发生故障时，只有在ISR 集合中的副本才有资格被选
举为新的leader，而在OSR 集合中的副本则没有任何机会（不过这个原则也可以通过修改
相应的参数配置来改变）。
replica.lag.time.max.ms ：这个参数的含义是Follower 副本能够落后Leader 副本的
最长时间间隔，当前默认值是10 秒。
unclean.leader.election.enable：是否允许Unclean 领导者选举。开启Unclean 领导者
选举可能会造成数据丢失，但好处是，它使得分区Leader 副本一直存在，不至于停止对外
提供服务，因此提升了高可用性。
3.Kafka 中的HW、LEO、LSO、LW 等分别代表什么？
HW 是High Watermark 的缩写，俗称高水位，它标识了一个特定的消息偏移量（offset），
消费者只能拉取到这个offset 之前的消息。
LSO 是LogStartOffset，一般情况下，日志文件的起始偏移量logStartOffset 等于第一个
日志分段的baseOffset，但这并不是绝对的，logStartOffset 的值可以通过

---

DeleteRecordsRequest 请求(比如使用KafkaAdminClient 的deleteRecords()方法、使用
kafka-delete-records.sh 脚本、日志的清理和截断等操作进行修改。
如上图所示，它代表一个日志文件，这个日志文件中有9 条消息，第一条消息的offset
（LogStartOffset）为0，最后一条消息的offset 为8，offset 为9 的消息用虚线框表示，
代表下一条待写入的消息。日志文件的HW 为6，表示消费者只能拉取到offset 在0 至5
之间的消息，而offset 为6 的消息对消费者而言是不可见的。
LEO 是Log End Offset 的缩写，它标识当前日志文件中下一条待写入消息的offset，上
图中offset 为9 的位置即为当前日志文件的LEO，LEO 的大小相当于当前日志分区中最后
一条消息的offset 值加1。分区ISR 集合中的每个副本都会维护自身的LEO，而ISR 集
合中最小的LEO 即为分区的HW，对消费者而言只能消费HW 之前的消息。
LW 是Low Watermark 的缩写，俗称“低水位”，代表AR 集合中最小的logStartOffset 值。
副本的拉取请求(FetchRequest，它有可能触发新建日志分段而旧的被清理，进而导致
logStartOffset 的增加)和删除消息请求(DeleteRecordRequest)都有可能促使LW 的增
长。
4.Kafka 中是怎么体现消息顺序性的？
可以通过分区策略体现消息顺序性。
分区策略有轮询策略、随机策略、按消息键保序策略。
按消息键保序策略：一旦消息被定义了Key，那么你就可以保证同一个Key 的所有消息都
进入到相同的分区里面，由于每个分区下的消息处理都是有顺序的，故这个策略被称为按消
息键保序策略
List<PartitionInfo> partitions = cluster.partitionsForTopic(topic);return
Math.abs(key.hashCode()) % partitions.size();

![kafka44知识点（基础+进阶+高阶） 第2页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p2_1_f36c1592.jpeg)

---

5.Kafka 中的分区器、序列化器、拦截器是否了解？它们之
间的处理顺序是什么？

序列化器：生产者需要用序列化器（Serializer）把对象转换成字节数组才能通过
网络发送给Kafka。而在对侧，消费者需要用反序列化器（Deserializer）把从Kafka
中收到的字节数组转换成相应的对象。

分区器：分区器的作用就是为消息分配分区。如果消息ProducerRecord 中没有指
定partition 字段，那么就需要依赖分区器，根据key 这个字段来计算partition
的值。

Kafka 一共有两种拦截器：生产者拦截器和消费者拦截器。

生产者拦截器既可以用来在消息发送前做一些准备工作，比如按照某个规则
过滤不符合要求的消息、修改消息的内容等，也可以用来在发送回调逻辑前做一些
定制化的需求，比如统计类工作。

消费者拦截器主要在消费到消息或在提交消费位移时进行一些定制化的操
作。
消息在通过send() 方法发往broker 的过程中，有可能需要经过拦截器（Interceptor）、
序列化器（Serializer）和分区器（Partitioner）的一系列作用之后才能被真正地发往
broker。拦截器（下一章会详细介绍）一般不是必需的，而序列化器是必需的。消息经过序
列化之后就需要确定它发往的分区，如果消息ProducerRecord 中指定了partition 字段，
那么就不需要分区器的作用，因为partition 代表的就是所要发往的分区号。
处理顺序：拦截器->序列化器->分区器
KafkaProducer 在将消息序列化和计算分区之前会调用生产者拦截器的onSend() 方法来
对消息进行相应的定制化操作。
然后生产者需要用序列化器（Serializer）把对象转换成字节数组才能通过网络发送给
Kafka。
最后可能会被发往分区器为消息分配分区。

---

6.Kafka 生产者客户端的整体结构是什么样子的？
整个生产者客户端由两个线程协调运行，这两个线程分别为主线程和Sender 线程（发送线
程）。
在主线程中由KafkaProducer 创建消息，然后通过可能的拦截器、序列化器和分区器的作
用之后缓存到消息累加器（RecordAccumulator，也称为消息收集器）中。
Sender 线程负责从RecordAccumulator 中获取消息并将其发送到Kafka 中。
RecordAccumulator 主要用来缓存消息以便Sender 线程可以批量发送，进而减少网络传输
的资源消耗以提升性能。
7.Kafka 生产者客户端中使用了几个线程来处理？分别是什
么？
整个生产者客户端由两个线程协调运行，这两个线程分别为主线程和Sender 线程（发送线
程）。在主线程中由KafkaProducer 创建消息，然后通过可能的拦截器、序列化器和分区

![kafka44知识点（基础+进阶+高阶） 第4页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p4_1_3594baa2.jpeg)

---

器的作用之后缓存到消息累加器（RecordAccumulator，也称为消息收集器）中。Sender 线
程负责从RecordAccumulator 中获取消息并将其发送到Kafka 中。
8.Kafka 的旧版Scala 的消费者客户端的设计有什么缺陷？
老版本的Consumer Group 把位移保存在ZooKeeper 中。Apache ZooKeeper 是一个分布式
的协调服务框架，Kafka 重度依赖它实现各种各样的协调管理。将位移保存在ZooKeeper 外
部系统的做法，最显而易见的好处就是减少了Kafka Broker 端的状态保存开销。
ZooKeeper 这类元框架其实并不适合进行频繁的写更新，而Consumer Group 的位移更新却
是一个非常频繁的操作。这种大吞吐量的写操作会极大地拖慢ZooKeeper 集群的性能
9.“消费组中的消费者个数如果超过topic 的分区，那么就
会有消费者消费不到数据”这句话是否正确？如果正确，那
么有没有什么hack 的手段？
一般来说如果消费者过多，出现了消费者的个数大于分区个数的情况，就会有消费者分配不
到任何分区。
开发者可以继承AbstractPartitionAssignor 实现自定义消费策略，从而实现同一消费组内
的任意消费者都可以消费订阅主题的所有分区：
public class BroadcastAssignor extends AbstractPartitionAssignor{
@Override
public String name() {
return "broadcast";
}
private Map<String, List<String>> consumersPerTopic(
Map<String, Subscription> consumerMetadata) {
（具体实现请参考RandomAssignor 中的consumersPerTopic()方法）
}
@Override
public Map<String, List<TopicPartition>> assign(
Map<String, Integer> partitionsPerTopic,
Map<String, Subscription> subscriptions) {

---

Map<String, List<String>> consumersPerTopic =
consumersPerTopic(subscriptions);
Map<String, List<TopicPartition>> assignment = new HashMap<>();
//Java8
subscriptions.keySet().forEach(memberId ->
assignment.put(memberId, new ArrayList<>()));
//针对每一个主题，为每一个订阅的消费者分配所有的分区
consumersPerTopic.entrySet().forEach(topicEntry->{
String topic = topicEntry.getKey();
List<String> members = topicEntry.getValue();
Integer numPartitionsForTopic = partitionsPerTopic.get(topic);
if (numPartitionsForTopic == null || members.isEmpty())
return;
List<TopicPartition> partitions = AbstractPartitionAssignor
.partitions(topic, numPartitionsForTopic);
if (!partitions.isEmpty()) {
members.forEach(memberId ->
assignment.get(memberId).addAll(partitions));
}
});
return assignment;
}
}
注意组内广播的这种实现方式会有一个严重的问题—默认的消费位移的提交会失效。
消费者提交消费位移时提交的是当前消费到的最新消息的offset 还是offset+1?#
在旧消费者客户端中，消费位移是存储在ZooKeeper 中的。而在新消费者客户端中，消费
位移存储在Kafka 内部的主题__consumer_offsets 中。
当前消费者需要提交的消费位移是offset+1

---

10.有哪些情形会造成重复消费？
1.
Rebalance
一个consumer 正在消费一个分区的一条消息，还没有消费完，发生了rebalance(加入了一
个consumer)，从而导致这条消息没有消费成功，rebalance 后，另一个consumer 又把这条
消息消费一遍。
2.
消费者端手动提交
如果先消费消息，再更新offset 位置，导致消息重复消费。
3.
消费者端自动提交
设置offset 为自动提交，关闭kafka 时，如果在close 之前，调用consumer.unsubscribe()
则有可能部分offset 没提交，下次重启会重复消费。
4.
生产者端
生产者因为业务问题导致的宕机，在重启之后可能数据会重发
那些情景下会造成消息漏消费？#
1.
自动提交
设置offset 为自动定时提交，当offset 被自动定时提交时，数据还在内存中未处理，此时
刚好把线程kill 掉，那么offset 已经提交，但是数据未处理，导致这部分内存中的数据丢
失。
2.
生产者发送消息
发送消息设置的是fire-and-forget（发后即忘），它只管往Kafka 中发送消息而并不关
心消息是否正确到达。不过在某些时候（比如发生不可重试异常时）会造成消息的丢失。这
种发送方式的性能最高，可靠性也最差。
3.
消费者端
先提交位移，但是消息还没消费完就宕机了，造成了消息没有被消费。自动位移提交同理
4.
acks 没有设置为all
如果在broker 还没把消息同步到其他broker 的时候宕机了，那么消息将会丢失
12.KafkaConsumer 是非线程安全的，那么怎么样实现多线
程消费？
1.
线程封闭，即为每个线程实例化一个KafkaConsumer 对象

---

一个线程对应一个KafkaConsumer 实例，我们可以称之为消费线程。一个消费线程可以消
费一个或多个分区中的消息，所有的消费线程都隶属于同一个消费组。
1.
消费者程序使用单或多线程获取消息，同时创建多个消费线程执行消息处理逻辑。
获取消息的线程可以是一个，也可以是多个，每个线程维护专属的KafkaConsumer 实例，
处理消息则交由特定的线程池来做，从而实现消息获取与消息处理的真正解耦。具体架构如
下图所示：
两个方案对比：

![kafka44知识点（基础+进阶+高阶） 第8页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p8_1_238aee30.jpeg)

![kafka44知识点（基础+进阶+高阶） 第8页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p8_2_9e175909.jpeg)

![kafka44知识点（基础+进阶+高阶） 第8页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p8_3_83be2ec2.jpeg)

---

13.简述消费者与消费组之间的关系
1.
Consumer Group 下可以有一个或多个Consumer 实例。这里的实例可以是一个单独
的进程，也可以是同一进程下的线程。在实际场景中，使用进程更为常见一些。
2.
Group ID 是一个字符串，在一个Kafka 集群中，它标识唯一的一个Consumer
Group。
3.
Consumer Group 下所有实例订阅的主题的单个分区，只能分配给组内的某个
Consumer 实例消费。这个分区当然也可以被其他的Group 消费。
14.当你使用kafka-topics.sh 创建（删除）了一个topic 之
后，Kafka 背后会执行什么逻辑？
在执行完脚本之后，Kafka 会在log.dir 或log.dirs 参数所配置的目录下创建相应的主
题分区，默认情况下这个目录为/tmp/kafka-logs/。
在ZooKeeper 的/brokers/topics/目录下创建一个同名的实节点，该节点中记录了该主题
的分区副本分配方案。示例如下：
[zk: localhost:2181/kafka(CONNECTED) 2] get /brokers/topics/topic-create
{"version":1,"partitions":{"2":[1,2],"1":[0,1],"3":[2,1],"0":[2,0]}}
15.topic 的分区数可不可以增加？如果可以怎么增加？如
果不可以，那又是为什么？
可以增加，使用kafka-topics 脚本，结合--alter 参数来增加某个主题的分区数，命令
如下：
bin/kafka-topics.sh --bootstrap-server broker_host:port --alter --topic
<topic_name> --partitions <新分区数>
当分区数增加时，就会触发订阅该主题的所有Group 开启Rebalance。
首先，Rebalance 过程对Consumer Group 消费过程有极大的影响。在Rebalance 过程中，
所有Consumer 实例都会停止消费，等待Rebalance 完成。这是Rebalance 为人诟病的一
个方面。
其次，目前Rebalance 的设计是所有Consumer 实例共同参与，全部重新分配所有分区。
其实更高效的做法是尽量减少分配方案的变动。
最后，Rebalance 实在是太慢了。

---

16.topic 的分区数可不可以减少？如果可以怎么减少？如
果不可以，那又是为什么？
不支持，因为删除的分区中的消息不好处理。如果直接存储到现有分区的尾部，消息的时间
戳就不会递增，如此对于Spark、Flink 这类需要消息时间戳（事件时间）的组件将会受到
影响；如果分散插入现有的分区，那么在消息量很大的时候，内部的数据复制会占用很大的
资源，而且在复制期间，此主题的可用性又如何得到保障？与此同时，顺序性问题、事务性
问题，以及分区和副本的状态机切换问题都是不得不面对的。
17.创建topic 时如何选择合适的分区数？
在Kafka 中，性能与分区数有着必然的关系，在设定分区数时一般也需要考虑性能的因素。
对不同的硬件而言，其对应的性能也会不太一样。
可以使用Kafka 本身提供的用于生产者性能测试的kafka-producer- perf-test.sh 和用
于消费者性能测试的kafka-consumer-perf-test.sh 来进行测试。
增加合适的分区数可以在一定程度上提升整体吞吐量，但超过对应的阈值之后吞吐量不升反
降。如果应用对吞吐量有一定程度上的要求，则建议在投入生产环境之前对同款硬件资源做
一个完备的吞吐量相关的测试，以找到合适的分区数阈值区间。
分区数的多少还会影响系统的可用性。如果分区数非常多，如果集群中的某个broker 节点
宕机，那么就会有大量的分区需要同时进行leader 角色切换，这个切换的过程会耗费一笔
可观的时间，并且在这个时间窗口内这些分区也会变得不可用。
分区数越多也会让Kafka 的正常启动和关闭的耗时变得越长，与此同时，主题的分区数越
多不仅会增加日志清理的耗时，而且在被删除时也会耗费更多的时间。
Kakfa 进阶篇
1.Kafka 目前有哪些内部topic，它们都有什么特征？各自
的作用又是什么？
__consumer_offsets：作用是保存Kafka 消费者的位移信息
__transaction_state：用来存储事务日志消息
2.优先副本是什么？它有什么特殊的作用？
所谓的优先副本是指在AR 集合列表中的第一个副本。
理想情况下，优先副本就是该分区的leader 副本，所以也可以称之为preferred leader。

---

Kafka 要确保所有主题的优先副本在Kafka 集群中均匀分布，这样就保证了所有分区的
leader 均衡分布。以此来促进集群的负载均衡，这一行为也可以称为“分区平衡”。
3.Kafka 有哪几处地方有分区分配的概念？简述大致的过程
及原理
1.
生产者的分区分配是指为每条消息指定其所要发往的分区。可以编写一个具体的类
实现org.apache.kafka.clients.producer.Partitioner 接口。
2.
消费者中的分区分配是指为消费者指定其可以消费消息的分区。Kafka 提供了消费
者客户端参数partition.assignment.strategy 来设置消费者与订阅主题之间的分区分配
策略。
3.
分区副本的分配是指为集群制定创建主题时的分区副本分配方案，即在哪个broker
中创建哪些分区的副本。kafka-topics.sh 脚本中提供了一个replica-assignment 参数来
手动指定分区副本的分配方案。
4.简述Kafka 的日志目录结构
Kafka 中的消息是以主题为基本单位进行归类的，各个主题在逻辑上相互独立。每个主题又
可以分为一个或多个分区。不考虑多副本的情况，一个分区对应一个日志（Log）。为了防
止Log 过大，Kafka 又引入了日志分段（LogSegment）的概念，将Log 切分为多个
LogSegment，相当于一个巨型文件被平均分配为多个相对较小的文件。

![kafka44知识点（基础+进阶+高阶） 第11页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p11_1_c3ba1e24.jpeg)

---

Log 和LogSegment 也不是纯粹物理意义上的概念，Log 在物理上只以文件夹的形式存储，
而每个LogSegment 对应于磁盘上的一个日志文件和两个索引文件，以及可能的其他文件
（比如以“.txnindex”为后缀的事务索引文件）
5.Kafka 中有那些索引文件？
每个日志分段文件对应了两个索引文件，主要用来提高查找消息的效率。
偏移量索引文件用来建立消息偏移量（offset）到物理地址之间的映射关系，方便快速定位
消息所在的物理文件位置
时间戳索引文件则根据指定的时间戳（timestamp）来查找对应的偏移量信息。
6.如果我指定了一个offset，Kafka 怎么查找到对应的消
息？
Kafka 是通过seek() 方法来指定消费的，在执行seek() 方法之前要去执行一次poll()方
法，等到分配到分区之后会去对应的分区的指定位置开始消费，如果指定的位置发生了越界，
那么会根据auto.offset.reset 参数设置的情况进行消费。
7.如果我指定了一个timestamp，Kafka 怎么查找到对应的
消息？
Kafka 提供了一个offsetsForTimes() 方法，通过timestamp 来查询与此对应的分区位
置。offsetsForTimes() 方法的参数timestampsToSearch 是一个Map 类型，key 为待查
询的分区，而value 为待查询的时间戳，该方法会返回时间戳大于等于待查询时间的第一
条消息对应的位置和时间戳，对应于OffsetAndTimestamp 中的offset 和timestamp 字
段。
8.聊一聊你对Kafka 的Log Retention 的理解
日志删除（Log Retention）：按照一定的保留策略直接删除不符合条件的日志分段。
我们可以通过broker 端参数log.cleanup.policy 来设置日志清理策略，此参数的默认值
为“delete”，即采用日志删除的清理策略。
1.基于时间
日志删除任务会检查当前日志文件中是否有保留时间超过设定的阈值（retentionMs）来寻
找可删除的日志分段文件集合（deletableSegments）retentionMs 可以通过broker 端参
数log.retention.hours、log.retention.minutes 和log.retention.ms 来配置，其中
log.retention.ms 的优先级最高，log.retention.minutes 次之，log.retention.hours 最
低。默认情况下只配置了log.retention.hours 参数，其值为168，故默认情况下日志分
段文件的保留时间为7 天。

---

删除日志分段时，首先会从Log 对象中所维护日志分段的跳跃表中移除待删除的日志分段，
以保证没有线程对这些日志分段进行读取操作。然后将日志分段所对应的所有文件添加上
“.deleted”的后缀（当然也包括对应的索引文件）。最后交由一个以“delete-file”命
名的延迟任务来删除这些以“.deleted”为后缀的文件，这个任务的延迟执行时间可以通过
file.delete.delay.ms 参数来调配，此参数的默认值为60000，即1 分钟。
2.基于日志大小
日志删除任务会检查当前日志的大小是否超过设定的阈值（retentionSize）来寻找可删除
的日志分段的文件集合（deletableSegments）。
retentionSize 可以通过broker 端参数log.retention.bytes 来配置，默认值为-1，表
示无穷大。注意log.retention.bytes 配置的是Log 中所有日志文件的总大小，而不是单
个日志分段（确切地说应该为.log 日志文件）的大小。单个日志分段的大小由broker 端
参数log.segment.bytes 来限制，默认值为1073741824，即1GB。
这个删除操作和基于时间的保留策略的删除操作相同。
3.基于日志起始偏移量
基于日志起始偏移量的保留策略的判断依据是某日志分段的下一个日志分段的起始偏移量
baseOffset 是否小于等于logStartOffset，若是，则可以删除此日志分段。
如上图所示，假设logStartOffset 等于25，日志分段1 的起始偏移量为0，日志分段2
的起始偏移量为11，日志分段3 的起始偏移量为23，通过如下动作收集可删除的日志分段
的文件集合deletableSegments：
从头开始遍历每个日志分段，日志分段1 的下一个日志分段的起始偏移量为11，小于
logStartOffset 的大小，将日志分段1 加入deletableSegments。
日志分段2 的下一个日志偏移量的起始偏移量为23，也小于logStartOffset 的大小，将
日志分段2 加入deletableSegments。
日志分段3 的下一个日志偏移量在logStartOffset 的右侧，故从日志分段3 开始的所有日
志分段都不会加入deletableSegments。
收集完可删除的日志分段的文件集合之后的删除操作同基于日志大小的保留策略和基于时
间的保留策略相同

![kafka44知识点（基础+进阶+高阶） 第13页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p13_1_ba271736.jpeg)

---

9.聊一聊你对Kafka 的Log Compaction 的理解#
日志压缩（Log Compaction）：针对每个消息的key 进行整合，对于有相同key 的不同
value 值，只保留最后一个版本。
如果要采用日志压缩的清理策略，就需要将log.cleanup.policy 设置为“compact”，并
且还需要将log.cleaner.enable （默认值为true）设定为true。
如下图所示，Log Compaction 对于有相同key 的不同value 值，只保留最后一个版本。
如果应用只关心key 对应的最新value 值，则可以开启Kafka 的日志清理功能，Kafka 会
定期将相同key 的消息进行合并，只保留最新的value 值。
10.聊一聊你对Kafka 底层存储的理解
页缓存
页缓存是操作系统实现的一种主要的磁盘缓存，以此用来减少对磁盘I/O 的操作。具体来
说，就是把磁盘中的数据缓存到内存中，把对磁盘的访问变为对内存的访问。
当一个进程准备读取磁盘上的文件内容时，操作系统会先查看待读取的数据所在的页（page）
是否在页缓存（pagecache）中，如果存在（命中）则直接返回数据，从而避免了对物理磁
盘的I/O 操作；如果没有命中，则操作系统会向磁盘发起读取请求并将读取的数据页存入
页缓存，之后再将数据返回给进程。

![kafka44知识点（基础+进阶+高阶） 第14页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p14_1_975db2bc.jpeg)

---

同样，如果一个进程需要将数据写入磁盘，那么操作系统也会检测数据对应的页是否在页缓
存中，如果不存在，则会先在页缓存中添加相应的页，最后将数据写入对应的页。被修改过
后的页也就变成了脏页，操作系统会在合适的时间把脏页中的数据写入磁盘，以保持数据的
一致性。
用过Java 的人一般都知道两点事实：对象的内存开销非常大，通常会是真实数据大小的几
倍甚至更多，空间使用率低下；Java 的垃圾回收会随着堆内数据的增多而变得越来越慢。
基于这些因素，使用文件系统并依赖于页缓存的做法明显要优于维护一个进程内缓存或其他
结构，至少我们可以省去了一份进程内部的缓存消耗，同时还可以通过结构紧凑的字节码来
替代使用对象的方式以节省更多的空间。
此外，即使Kafka 服务重启，页缓存还是会保持有效，然而进程内的缓存却需要重建。这
样也极大地简化了代码逻辑，因为维护页缓存和文件之间的一致性交由操作系统来负责，这
样会比进程内维护更加安全有效。
零拷贝
除了消息顺序追加、页缓存等技术，Kafka 还使用零拷贝（Zero-Copy）技术来进一步提升
性能。所谓的零拷贝是指将数据直接从磁盘文件复制到网卡设备中，而不需要经由应用程序
之手。零拷贝大大提高了应用程序的性能，减少了内核和用户模式之间的上下文切换。对
Linux 操作系统而言，零拷贝技术依赖于底层的sendfile() 方法实现。对应于Java 语言，
FileChannal.transferTo() 方法的底层实现就是sendfile() 方法。
11.聊一聊Kafka 的延时操作的原理
Kafka 中有多种延时操作，比如延时生产，还有延时拉取（DelayedFetch）、延时数据删除
（DelayedDeleteRecords）等。
延时操作创建之后会被加入延时操作管理器（DelayedOperationPurgatory）来做专门的处
理。延时操作有可能会超时，每个延时操作管理器都会配备一个定时器（SystemTimer）来
做超时管理，定时器的底层就是采用时间轮（TimingWheel）实现的。
12 聊一聊Kafka 控制器的作用
在Kafka 集群中会有一个或多个broker，其中有一个broker 会被选举为控制器（Kafka
Controller），它负责管理整个集群中所有分区和副本的状态。当某个分区的leader 副本
出现故障时，由控制器负责为该分区选举新的leader 副本。当检测到某个分区的ISR 集
合发生变化时，由控制器负责通知所有broker 更新其元数据信息。当使用kafka-topics.sh
脚本为某个topic 增加分区数量时，同样还是由控制器负责分区的重新分配。

---

13.Kafka 的旧版Scala 的消费者客户端的设计有什么缺
陷？
如上图，旧版消费者客户端每个消费组（）在ZooKeeper 中都维护了一个/consumers//ids 路径，在
此路径下使用临时节点记录隶属于此消费组的消费者的唯一标识（consumerIdString），
/consumers//owner 路径下记录了分区和消费者的对应关系，/consumers//offsets 路径下记录了此消
费组在分区中对应的消费位移。
每个消费者在启动时都会在/consumers//ids 和/brokers/ids 路径上注册一个监听器。当
/consumers//ids 路径下的子节点发生变化时，表示消费组中的消费者发生了变化；当/brokers/ids 路
径下的子节点发生变化时，表示broker 出现了增减。这样通过ZooKeeper 所提供的Watcher，每个
消费者就可以监听消费组和Kafka 集群的状态了。
这种方式下每个消费者对ZooKeeper 的相关路径分别进行监听，当触发再均衡操作时，一个消费组下的
所有消费者会同时进行再均衡操作，而消费者之间并不知道彼此操作的结果，这样可能导致Kafka 工作在
一个不正确的状态。与此同时，这种严重依赖于ZooKeeper 集群的做法还有两个比较严重的问题。
1.
羊群效应（Herd Effect）：所谓的羊群效应是指ZooKeeper 中一个被监听的节点变化，大量的
Watcher 通知被发送到客户端，导致在通知期间的其他操作延迟，也有可能发生类似死锁的情况。
2.
脑裂问题（Split Brain）：消费者进行再均衡操作时每个消费者都与ZooKeeper 进行通信以判
断消费者或broker 变化的情况，由于ZooKeeper 本身的特性，可能导致在同一时刻各个消费者获取的
状态不一致，这样会导致异常问题发生。

![kafka44知识点（基础+进阶+高阶） 第16页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p16_1_9d880674.jpeg)

---

14.消费再均衡的原理是什么？（提示：消费者协调器和消
费组协调器）
就目前而言，一共有如下几种情形会触发再均衡的操作：

有新的消费者加入消费组。

有消费者宕机下线。消费者并不一定需要真正下线，例如遇到长时间的GC、网络延迟导致消费
者长时间未向GroupCoordinator 发送心跳等情况时，GroupCoordinator 会认为消费者已经下线。

有消费者主动退出消费组（发送LeaveGroupRequest 请求）。比如客户端调用了unsubscrib
le() 方法取消对某些主题的订阅。

消费组所对应的GroupCoorinator 节点发生了变更。

消费组内所订阅的任一主题或者主题的分区数量发生变化。
GroupCoordinator 是Kafka 服务端中用于管理消费组的组件。而消费者客户端中的
ConsumerCoordinator 组件负责与GroupCoordinator 进行交互。
第一阶段（FIND_COORDINATOR）
消费者需要确定它所属的消费组对应的GroupCoordinator 所在的broker，并创建与该broker 相互通
信的网络连接。如果消费者已经保存了与消费组对应的GroupCoordinator 节点的信息，并且与它之间
的网络连接是正常的，那么就可以进入第二阶段。否则，就需要向集群中的某个节点发送
FindCoordinatorRequest 请求来查找对应的GroupCoordinator，这里的“某个节点”并非是集群中的
任意节点，而是负载最小的节点。
第二阶段（JOIN_GROUP）
在成功找到消费组所对应的GroupCoordinator 之后就进入加入消费组的阶段，在此阶段的消费者会向
GroupCoordinator 发送JoinGroupRequest 请求，并处理响应。
选举消费组的leader
如果消费组内还没有leader，那么第一个加入消费组的消费者即为消费组的leader。如果某一时刻
leader 消费者由于某些原因退出了消费组，那么会重新选举一个新的leader
选举分区分配策略
1.
收集各个消费者支持的所有分配策略，组成候选集candidates。
2.
每个消费者从候选集candidates 中找出第一个自身支持的策略，为这个策略投上一票。
3.
计算候选集中各个策略的选票数，选票数最多的策略即为当前消费组的分配策略。
第三阶段（SYNC_GROUP）

---

leader 消费者根据在第二阶段中选举出来的分区分配策略来实施具体的分区分配，在此之后需要将分配的
方案同步给各个消费者，通过GroupCoordinator 这个“中间人”来负责转发同步分配方案的。
第四阶段（HEARTBEAT）
进入这个阶段之后，消费组中的所有消费者就会处于正常工作状态。在正式消费之前，消费者还需要确定
拉取消息的起始位置。假设之前已经将最后的消费位移提交到了GroupCoordinator，并且
GroupCoordinator 将其保存到了Kafka 内部的__consumer_offsets 主题中，此时消费者可以通过
OffsetFetchRequest 请求获取上次提交的消费位移并从此处继续消费。
消费者通过向GroupCoordinator 发送心跳来维持它们与消费组的从属关系，以及它们对分区的所有权
关系。只要消费者以正常的时间间隔发送心跳，就被认为是活跃的，说明它还在读取分区中的消息。心跳
线程是一个独立的线程，可以在轮询消息的空档发送心跳。如果消费者停止发送心跳的时间足够长，则整
个会话就被判定为过期，GroupCoordinator 也会认为这个消费者已经死亡，就会触发一次再均衡行为。
15.Kafka 中的幂等是怎么实现的？
为了实现生产者的幂等性，Kafka 为此引入了producer id（以下简称PID）和序列号（sequence
number）这两个概念。
每个新的生产者实例在初始化的时候都会被分配一个PID，这个PID 对用户而言是完全透明的。对于每
个PID，消息发送到的每一个分区都有对应的序列号，这些序列号从0 开始单调递增。生产者每发送一条
消息就会将<PID，分区> 对应的序列号的值加1。
broker 端会在内存中为每一对<PID，分区> 维护一个序列号。对于收到的每一条消息，只有当它的序
列号的值（SN_new）比broker 端中维护的对应的序列号的值（SN_old）大1（即SN_new = SN_old
+ 1）时，broker 才会接收它。如果SN_new< SN_old + 1，那么说明消息被重复写入，broker 可以直
接将其丢弃。如果SN_new> SN_old + 1，那么说明中间有数据尚未写入，出现了乱序，暗示可能有消
息丢失，对应的生产者会抛出OutOfOrderSequenceException，这个异常是一个严重的异常，后续的诸
如send()、beginTransaction()、commitTransaction() 等方法的调用都会抛出IllegalStateException
的异常。

![kafka44知识点（基础+进阶+高阶） 第18页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p18_1_dc0db5de.jpeg)

---

Kafka 高级篇
1.Kafka 中的事务是怎么实现的？
Kafka 中的事务可以使应用程序将消费消息、生产消息、提交消费位移当作原子操作来处理，
同时成功或失败，即使该生产或消费会跨多个分区。
生产者必须提供唯一的transactionalId，启动后请求事务协调器获取一个PID，
transactionalId 与PID 一一对应。
每次发送数据给<Topic, Partition>前，需要先向事务协调器发送
AddPartitionsToTxnRequest，事务协调器会将该<Transaction, Topic, Partition>存于
__transaction_state 内，并将其状态置为BEGIN。
在处理完AddOffsetsToTxnRequest 之后，生产者还会发送TxnOffsetCommitRequest 请求
给GroupCoordinator，从而将本次事务中包含的消费位移信息offsets 存储到主题
__consumer_offsets 中
一旦上述数据写入操作完成，应用程序必须调用KafkaProducer 的commitTransaction 方法
或者abortTransaction 方法以结束当前事务。无论调用commitTransaction() 方法还是
abortTransaction() 方法，生产者都会向TransactionCoordinator 发送EndTxnRequest
请求。
TransactionCoordinator 在收到EndTxnRequest 请求后会执行如下操作：
1.
将PREPARE_COMMIT 或PREPARE_ABORT 消息写入主题__transaction_state
2.
通过WriteTxnMarkersRequest 请求将COMMIT 或ABORT 信息写入用户所使用的
普通主题和__consumer_offsets
3.
将COMPLETE_COMMIT 或COMPLETE_ABORT 信息写入内部主题
__transaction_state 标明该事务结束
在消费端有一个参数isolation.level，设置为“read_committed”，表示消费端应用不可
以看到尚未提交的事务内的消息。如果生产者开启事务并向某个分区值发送3 条消息msg1、
msg2 和msg3，在执行commitTransaction() 或abortTransaction() 方法前，设置为
“read_committed”的消费端应用是消费不到这些消息的，不过在KafkaConsumer 内部会
缓存这些消息，直到生产者执行commitTransaction() 方法之后它才能将这些消息推送给
消费端应用。反之，如果生产者执行了abortTransaction() 方法，那么KafkaConsumer 会
将这些缓存的消息丢弃而不推送给消费端应用。
2.失效副本是指什么？有那些应对措施？
正常情况下，分区的所有副本都处于ISR 集合中，但是难免会有异常情况发生，从而某些
副本被剥离出ISR 集合中。在ISR 集合之外，也就是处于同步失效或功能失效（比如副本
处于非存活状态）的副本统称为失效副本，失效副本对应的分区也就称为同步失效分区，即
under-replicated 分区。

---

Kafka 从0.9.x 版本开始就通过唯一的broker 端参数replica.lag.time.max.ms 来抉
择，当ISR 集合中的一个follower 副本滞后leader 副本的时间超过此参数指定的值时
则判定为同步失败，需要将此follower 副本剔除出ISR 集合。replica.lag.time.max.ms
参数的默认值为10000。
在0.9.x 版本之前，Kafka 中还有另一个参数replica.lag.max.messages（默认值为
4000），它也是用来判定失效副本的，当一个follower 副本滞后leader 副本的消息数超
过replica.lag.max.messages 的大小时，则判定它处于同步失效的状态。它与
replica.lag.time.max.ms 参数判定出的失效副本取并集组成一个失效副本的集合，从而进
一步剥离出分区的ISR 集合。
Kafka 源码注释中说明了一般有这几种情况会导致副本失效：
follower 副本进程卡住，在一段时间内根本没有向leader 副本发起同步请求，比
如频繁的Full GC。
follower 副本进程同步过慢，在一段时间内都无法追赶上leader 副本，比如I/
O 开销过大。
如果通过工具增加了副本因子，那么新增加的副本在赶上leader 副本之前也都是
处于失效状态的。
如果一个follower 副本由于某些原因（比如宕机）而下线，之后又上线，在追赶
上leader 副本之前也处于失效状态。
应对措施
我们用UnderReplicatedPartitions 代表leader 副本在当前Broker 上且具有失效副本的分
区的个数。
如果集群中有多个Broker 的UnderReplicatedPartitions 保持一个大于0 的稳定值时，一
般暗示着集群中有Broker 已经处于下线状态。这种情况下，这个Broker 中的分区个数与集
群中的所有UnderReplicatedPartitions（处于下线的Broker 是不会上报任何指标值的）
之和是相等的。通常这类问题是由于机器硬件原因引起的，但也有可能是由于操作系统或者
JVM 引起的。
如果集群中存在Broker 的UnderReplicatedPartitions 频繁变动，或者处于一个稳定的大
于0 的值（这里特指没有Broker 下线的情况）时，一般暗示着集群出现了性能问题，通常
这类问题很难诊断，不过我们可以一步一步的将问题的范围缩小，比如先尝试确定这个性能
问题是否只存在于集群的某个Broker 中，还是整个集群之上。如果确定集群中所有的
under-replicated 分区都是在单个Broker 上，那么可以看出这个Broker 出现了问题，进
而可以针对这单一的Broker 做专项调查，比如：操作系统、GC、网络状态或者磁盘状态（比
如：iowait、ioutil 等指标）。
3.多副本下，各个副本中的HW 和LEO 的演变过程
某个分区有3 个副本分别位于broker0、broker1 和broker2 节点中，假设broker0 上的
副本1 为当前分区的leader 副本，那么副本2 和副本3 就是follower 副本，整个消息追
加的过程可以概括如下：

---

1.
生产者客户端发送消息至leader 副本（副本1）中。
2.
消息被追加到leader 副本的本地日志，并且会更新日志的偏移量。
3.
follower 副本（副本2 和副本3）向leader 副本请求同步数据。
4.
leader 副本所在的服务器读取本地日志，并更新对应拉取的follower 副本的信
息。
5.
leader 副本所在的服务器将拉取结果返回给follower 副本。
6.
follower 副本收到leader 副本返回的拉取结果，将消息追加到本地日志中，并更
新日志的偏移量信息。
某一时刻，leader 副本的LEO 增加至5，并且所有副本的HW 还都为0。
之后follower 副本（不带阴影的方框）向leader 副本拉取消息，在拉取的请求中会带有
自身的LEO 信息，这个LEO 信息对应的是FetchRequest 请求中的fetch_offset。leader
副本返回给follower 副本相应的消息，并且还带有自身的HW 信息，如上图（右）所示，
这个HW 信息对应的是FetchResponse 中的high_watermark。
此时两个follower 副本各自拉取到了消息，并更新各自的LEO 为3 和4。与此同时，
follower 副本还会更新自己的HW，更新HW 的算法是比较当前LEO 和leader 副本中传
送过来的HW 的值，取较小值作为自己的HW 值。当前两个follower 副本的HW 都等于0
（min(0,0) = 0）。

![kafka44知识点（基础+进阶+高阶） 第21页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p21_1_3e5bf866.jpeg)

---

接下来follower 副本再次请求拉取leader 副本中的消息，如下图（左）所示。
此时leader 副本收到来自follower 副本的FetchRequest 请求，其中带有LEO 的相关
信息，选取其中的最小值作为新的HW，即min(15,3,4)=3。然后连同消息和HW 一起返回
FetchResponse 给follower 副本，如上图（右）所示。注意leader 副本的HW 是一个很
重要的东西，因为它直接影响了分区数据对消费者的可见性。
两个follower 副本在收到新的消息之后更新LEO 并且更新自己的HW 为3
（min(LEO,3)=3）。
4.Kafka 在可靠性方面做了哪些改进？（HW,
LeaderEpoch）
HW
HW 是High Watermark 的缩写，俗称高水位，它标识了一个特定的消息偏移量（offset），
消费者只能拉取到这个offset 之前的消息。
分区ISR 集合中的每个副本都会维护自身的LEO，而ISR 集合中最小的LEO 即为分区的
HW，对消费者而言只能消费HW 之前的消息。
leader epoch
leader epoch 代表leader 的纪元信息（epoch），初始值为0。每当leader 变更一次，
leader epoch 的值就会加1，相当于为leader 增设了一个版本号。
每个副本中还会增设一个矢量<LeaderEpoch => StartOffset>，其中StartOffset 表示当
前LeaderEpoch 下写入的第一条消息的偏移量。

![kafka44知识点（基础+进阶+高阶） 第22页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p22_1_f80f6fee.jpeg)

---

假设有两个节点A 和B，B 是leader 节点，里面的数据如图：
A 发生重启，之后A 不是先忙着截断日志而是先发送OffsetsForLeaderEpochRequest 请求
给B，B 作为目前的leader 在收到请求之后会返回当前的LEO（LogEndOffset，注意图中LE0
和LEO 的不同），与请求对应的响应为OffsetsForLeaderEpochResponse。如果A 中的
LeaderEpoch（假设为LE_A）和B 中的不相同，那么B 此时会查找LeaderEpoch 为LE_A+1
对应的StartOffset 并返回给A
如上图所示，A 在收到2 之后发现和目前的LEO 相同，也就不需要截断日志了，以此来保
护数据的完整性。
再如，之后B 发生了宕机，A 成为新的leader，那么对应的LE=0 也变成了LE=1，对应
的消息m2 此时就得到了保留。后续的消息都可以以LE1 为LeaderEpoch 陆续追加到A
中。这个时候A 就会有两个LE，第二LE 所记录的Offset 从2 开始。如果B 恢复了，那么
就会从A 中获取到LE+1 的Offset 为2 的值返回给B。

![kafka44知识点（基础+进阶+高阶） 第23页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p23_1_6b625ebe.jpeg)

![kafka44知识点（基础+进阶+高阶） 第23页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p23_2_6ebaa94a.jpeg)

![kafka44知识点（基础+进阶+高阶） 第23页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p23_3_46b69020.jpeg)

---

再来看看LE 如何解决数据不一致的问题：
当前A 为leader，B 为follower，A 中有2 条消息m1 和m2，而B 中有1 条消息m1。
假设A 和B 同时“挂掉”，然后B 第一个恢复过来并成为新的leader。
之后B 写入消息m3，并将LEO 和HW 更新至2，如下图所示。注意此时的LeaderEpoch 已
经从LE0 增至LE1 了。
紧接着A 也恢复过来成为follower 并向B 发送OffsetsForLeaderEpochRequest 请求，
此时A 的LeaderEpoch 为LE0。B 根据LE0 查询到对应的offset 为1 并返回给A，A 就
截断日志并删除了消息m2，如下图所示。之后A 发送FetchRequest 至B 请求来同步数
据，最终A 和B 中都有两条消息m1 和m3，HW 和LEO 都为2，并且LeaderEpoch 都为LE1，
如此便解决了数据不一致的问题。

![kafka44知识点（基础+进阶+高阶） 第24页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p24_1_e03a26ed.jpeg)

![kafka44知识点（基础+进阶+高阶） 第24页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p24_2_9a4991f4.jpeg)

![kafka44知识点（基础+进阶+高阶） 第24页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p24_3_bf1c9392.jpeg)

---

5.为什么Kafka 不支持读写分离？
因为这样有两个明显的缺点：
1.
数据一致性问题。数据从主节点转到从节点必然会有一个延时的时间窗口，这个时
间窗口会导致主从节点之间的数据不一致。
2.
延时问题。数据从写入主节点到同步至从节点中的过程需要经历网络→主节点内存
→主节点磁盘→网络→从节点内存→从节点磁盘这几个阶段。对延时敏感的应用而言，主写
从读的功能并不太适用。
对于Kafka 来说，必要性不是很高，因为在Kafka 集群中，如果存在多个副本，经过合理的
配置，可以让leader 副本均匀的分布在各个broker 上面，使每个broker 上的读写负载都
是一样的。
6.Kafka 中的延迟队列怎么实现
在发送延时消息的时候并不是先投递到要发送的真实主题（real_topic）中，而是先投递到
一些Kafka 内部的主题（delay_topic）中，这些内部主题对用户不可见，然后通过一个自
定义的服务拉取这些内部主题中的消息，并将满足条件的消息再投递到要发送的真实的主题
中，消费者所订阅的还是真实的主题。
如果采用这种方案，那么一般是按照不同的延时等级来划分的，比如设定5s、10s、30s、
1min、2min、5min、10min、20min、30min、45min、1hour、2hour 这些按延时时间递增的
延时等级，延时的消息按照延时时间投递到不同等级的主题中，投递到同一主题中的消息的
延时时间会被强转为与此主题延时等级一致的延时时间，这样延时误差控制在两个延时等级
的时间差范围之内（比如延时时间为17s 的消息投递到30s 的延时主题中，之后按照延时时
间为30s 进行计算，延时误差为13s）。虽然有一定的延时误差，但是误差可控，并且这样
只需增加少许的主题就能实现延时队列的功能。

![kafka44知识点（基础+进阶+高阶） 第25页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p25_1_53e654cd.jpeg)

---

发送到内部主题（delay_topic_*）中的消息会被一个独立的DelayService 进程消费，这
个DelayService 进程和Kafka broker 进程以一对一的配比进行同机部署（参考下图），
以保证服务的可用性。
针对不同延时级别的主题，在DelayService 的内部都会有单独的线程来进行消息的拉取，
以及单独的DelayQueue（这里用的是JUC 中DelayQueue）进行消息的暂存。与此同时，
在DelayService 内部还会有专门的消息发送线程来获取DelayQueue 的消息并转发到真
实的主题中。从消费、暂存再到转发，线程之间都是一一对应的关系。如下图所示，
DelayService 的设计应当尽量保持简单，避免锁机制产生的隐患。
为了保障内部DelayQueue 不会因为未处理的消息过多而导致内存的占用过大，
DelayService 会对主题中的每个分区进行计数，当达到一定的阈值之后，就会暂停拉取该
分区中的消息。
因为一个主题中一般不止一个分区，分区之间的消息并不会按照投递时间进行排序，
DelayQueue 的作用是将消息按照再次投递时间进行有序排序，这样下游的消息发送线程就
能够按照先后顺序获取最先满足投递条件的消息。

![kafka44知识点（基础+进阶+高阶） 第26页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p26_1_89484fff.jpeg)

![kafka44知识点（基础+进阶+高阶） 第26页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p26_2_b6dad0aa.jpeg)

---

7.Kafka 中怎么实现死信队列和重试队列？
死信可以看作消费者不能处理收到的消息，也可以看作消费者不想处理收到的消息，还可以
看作不符合处理要求的消息。比如消息内包含的消息内容无法被消费者解析，为了确保消息
的可靠性而不被随意丢弃，故将其投递到死信队列中，这里的死信就可以看作消费者不能处
理的消息。再比如超过既定的重试次数之后将消息投入死信队列，这里就可以将死信看作不
符合处理要求的消息。
重试队列其实可以看作一种回退队列，具体指消费端消费消息失败时，为了防止消息无故丢
失而重新将消息回滚到broker 中。与回退队列不同的是，重试队列一般分成多个重试等级，
每个重试等级一般也会设置重新投递延时，重试次数越多投递延时就越大。
理解了他们的概念之后我们就可以为每个主题设置重试队列，消息第一次消费失败入重试队
列Q1，Q1 的重新投递延时为5s，5s 过后重新投递该消息；如果消息再次消费失败则入重
试队列Q2，Q2 的重新投递延时为10s，10s 过后再次投递该消息。
然后再设置一个主题作为死信队列，重试越多次重新投递的时间就越久，并且需要设置一个
上限，超过投递次数就进入死信队列。重试队列与延时队列有相同的地方，都需要设置延时
级别。
8.Kafka 中怎么做消息审计？
消息审计是指在消息生产、存储和消费的整个过程之间对消息个数及延迟的审计，以此来检
测是否有数据丢失、是否有数据重复、端到端的延迟又是多少等内容。
目前与消息审计有关的产品也有多个，比如Chaperone（Uber）、Confluent Control Center、
Kafka Monitor（LinkedIn），它们主要通过在消息体（value 字段）或在消息头（headers
字段）中内嵌消息对应的时间戳timestamp 或全局的唯一标识ID（或者是两者兼备）来实
现消息的审计功能。
内嵌timestamp 的方式主要是设置一个审计的时间间隔time_bucket_interval（可以自定
义设置几秒或几分钟），根据这个time_bucket_interval 和消息所属的timestamp 来计
算相应的时间桶（time_bucket）。
内嵌ID 的方式就更加容易理解了，对于每一条消息都会被分配一个全局唯一标识ID。如
果主题和相应的分区固定，则可以为每个分区设置一个全局的ID。当有消息发送时，首先
获取对应的ID，然后内嵌到消息中，最后才将它发送到broker 中。消费者进行消费审计
时，可以判断出哪条消息丢失、哪条消息重复。
9.Kafka 中怎么做消息轨迹？
消息轨迹指的是一条消息从生产者发出，经由broker 存储，再到消费者消费的整个过程中，
各个相关节点的状态、时间、地点等数据汇聚而成的完整链路信息。生产者、broker、消费

---

者这3 个角色在处理消息的过程中都会在链路中增加相应的信息，将这些信息汇聚、处理之
后就可以查询任意消息的状态，进而为生产环境中的故障排除提供强有力的数据支持。
对消息轨迹而言，最常见的实现方式是封装客户端，在保证正常生产消费的同时添加相应的
轨迹信息埋点逻辑。无论生产，还是消费，在执行之后都会有相应的轨迹信息，我们需要将
这些信息保存起来。
我们同样可以将轨迹信息保存到Kafka 的某个主题中，比如下图中的主题trace_topic。
生产者在将消息正常发送到用户主题real_topic 之后（或者消费者在拉取到消息消费之
后）会将轨迹信息发送到主题trace_topic 中。
10. 怎么计算Lag ？( 注意read_uncommitted 和
read_committed 状态下的不同)#
如果消费者客户端的isolation.level 参数配置为“read_uncommitted”（默认）,它对应
的Lag 等于HW – ConsumerOffset 的值，其中ConsumerOffset 表示当前的消费位移。
如果这个参数配置为“read_committed”，那么就要引入LSO 来进行计算了。LSO 是
LastStableOffset 的缩写,它对应的Lag 等于LSO – ConsumerOffset 的值。

首先通过DescribeGroupsRequest 请求获取当前消费组的元数据信息，当然在这之
前还会通过FindCoordinatorRequest 请求查找消费组对应的GroupCoordinator。

接着通过OffsetFetchRequest 请求获取消费位移ConsumerOffset。

然后通过KafkaConsumer 的endOffsets(Collection partitions)方法（对应于
ListOffsetRequest 请求）获取HW（LSO）的值。

最后通过HW 与ConsumerOffset 相减得到分区的Lag，要获得主题的总体Lag
只需对旗下的各个分区累加即可。

![kafka44知识点（基础+进阶+高阶） 第28页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p28_1_732ed080.jpeg)

---

11.Kafka 有哪些指标需要着重关注？
比较重要的Broker 端JMX 指标：

BytesIn/BytesOut：即Broker 端每秒入站和出站字节数。你要确保这组值不要接
近你的网络带宽，否则这通常都表示网卡已被“打满”，很容易出现网络丢包的情形。

NetworkProcessorAvgIdlePercent：即网络线程池线程平均的空闲比例。通常来说，
你应该确保这个JMX 值长期大于30%。如果小于这个值，就表明你的网络线程池非常
繁忙，你需要通过增加网络线程数或将负载转移给其他服务器的方式，来给该Broker
减负。

RequestHandlerAvgIdlePercent：即I/O 线程池线程平均的空闲比例。同样地，如
果该值长期小于30%，你需要调整I/O 线程池的数量，或者减少Broker 端的负载。

UnderReplicatedPartitions：即未充分备份的分区数。所谓未充分备份，是指并非
所有的Follower 副本都和Leader 副本保持同步。一旦出现了这种情况，通常都表明
该分区有可能会出现数据丢失。因此，这是一个非常重要的JMX 指标。

ISRShrink/ISRExpand：即ISR 收缩和扩容的频次指标。如果你的环境中出现ISR
中副本频繁进出的情形，那么这组值一定是很高的。这时，你要诊断下副本频繁进出I
SR 的原因，并采取适当的措施。

ActiveControllerCount：即当前处于激活状态的控制器的数量。正常情况下，Con
troller 所在Broker 上的这个JMX 指标值应该是1，其他Broker 上的这个值是0。
如果你发现存在多台Broker 上该值都是1 的情况，一定要赶快处理，处理方式主要
是查看网络连通性。这种情况通常表明集群出现了脑裂。脑裂问题是非常严重的分布式
故障，Kafka 目前依托ZooKeeper 来防止脑裂。但一旦出现脑裂，Kafka 是无法保证
正常工作的。
12.Kafka 的那些设计让它有如此高的性能？
1.分区
kafka 是个分布式集群的系统，整个系统可以包含多个broker，也就是多个服务器实例。每
个主题topic 会有多个分区，kafka 将分区均匀地分配到整个集群中，当生产者向对应主题
传递消息，消息通过负载均衡机制传递到不同的分区以减轻单个服务器实例的压力。
一个Consumer Group 中可以有多个consumer，多个consumer 可以同时消费不同分区的消
息，大大的提高了消费者的并行消费能力。但是一个分区中的消息只能被一个Consumer
Group 中的一个consumer 消费。
2.网络传输上减少开销

---

批量发送：
在发送消息的时候，kafka 不会直接将少量数据发送出去，否则每次发送少量的数据会增加
网络传输频率，降低网络传输效率。kafka 会先将消息缓存在内存中，当超过一个的大小或
者超过一定的时间，那么会将这些消息进行批量发送。
端到端压缩：
当然网络传输时数据量小也可以减小网络负载，kafaka 会将这些批量的数据进行压缩，将
一批消息打包后进行压缩，发送broker 服务器后，最终这些数据还是提供给消费者用，所
以数据在服务器上还是保持压缩状态，不会进行解压，而且频繁的压缩和解压也会降低性能，
最终还是以压缩的方式传递到消费者的手上。
3.顺序读写
kafka 将消息追加到日志文件中，利用了磁盘的顺序读写，来提高读写效率。
4.零拷贝技术
零拷贝将文件内容从磁盘通过DMA 引擎复制到内核缓冲区，而且没有把数据复制到socket
缓冲区，只是将数据位置和长度信息的描述符复制到了socket 缓存区，然后直接将数据传
输到网络接口，最后发送。这样大大减小了拷贝的次数，提高了效率。kafka 正是调用linux
系统给出的sendfile 系统调用来使用零拷贝。Java 中的系统调用给出的是
FileChannel.transferTo 接口。
5. 优秀的文件存储机制
如果分区规则设置得合理，那么所有的消息可以均匀地分布到不同的分区中，这样就可以实
现水平扩展。不考虑多副本的情况，一个分区对应一个日志（Log）。为了防止Log 过大，
Kafka 又引入了日志分段（LogSegment）的概念，将Log 切分为多个LogSegment，相当于
一个巨型文件被平均分配为多个相对较小的文件，这样也便于消息的维护和清理。

---

Kafka 中的索引文件以稀疏索引（sparse index）的方式构造消息的索引，它并不保证每个消息在索引文
件中都有对应的索引项。每当写入一定量（由broker 端参数log.index.interval.bytes 指定，默认值为
4096，即4KB）的消息时，偏移量索引文件和时间戳索引文件分别增加一个偏移量索引项和时间戳索引
项，增大或减小log.index.interval.bytes 的值，对应地可以增加或缩小索引项的密度。

![kafka44知识点（基础+进阶+高阶） 第31页插图](../assets/images/kafka44知识点_基础+进阶+高阶_p31_1_c3ba1e24.jpeg)