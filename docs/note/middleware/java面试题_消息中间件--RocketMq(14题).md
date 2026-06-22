---
title: java面试题_消息中间件--RocketMq(14题)
source: Note/java面试题_消息中间件--RocketMq(14题).pdf
pages: 4
converted_at: 2026-06-22 22:28:52
---

# java面试题_消息中间件--RocketMq(14题)

http://jm.taobao.org/2017/01/12/rocketmq-quick-start-in-10-minutes/
1. 中⼩小型公司⾸首选RabbitMQ：管理理界⾯面简单，⾼高并发。
2. ⼤大型公司可以选择RocketMQ：更更⾼高并发，可对rocketmq进⾏行行定制化开发。
3. ⽇日志采集功能，⾸首选kafka，专为⼤大数据准备。
1. 消息可靠性：
影响消息可靠性的情况：
i. Broker正常关闭
ii. Broker异常Crash
iii. OS Crash
iv. 机器器掉电，但是能⽴立即恢复供电情况。
v. 机器器⽆无法开机（可能是cpu、主板、内存等关键设备损坏）
vi. 磁盘设备损坏。
1、(1)、(2)、(3)、(4)四种情况都属于硬件资源可⽴立即恢复情况，RocketMQ在这四种情况下能保证消息不不丢，或
者丢失少量量数据（依赖刷盘⽅方式是同步还是异步）。
2、(5)、(6)属于单点故障，且⽆无法恢复，⼀一旦发⽣生，在此单点上的消息全部丢失。RocketMQ在这两种情况下，
通过异步复制，可保证99%的消息不不丢，但是仍然会有极少量量的消息可能丢失。通过同步双写技术可以完全避免单点，同步双
写势必会影响性能，适合对消息可靠性要求极⾼高的场合，例例如与Money相关的应⽤用。
2. 消息低延迟：
在消息不不堆积情况下，消息到达Broker后，能⽴立刻到达Consumer。RocketMQ使⽤用⻓长轮询Pull⽅方式，可保证消息⾮非常
实时，消息实时性不不低于Push。
3. 每个消息⾄至少投递⼀一次：
RocketMQ Consumer先pull消息到本地，消费完成后，才向服务器器返回ack，如果没有消费⼀一定不不会ack消息，所以
RocketMQ可以很好的⽀支持此特性。
4. 每个消息只消费⼀一次：
1、前提：
i. 发送消息阶段，不不允许发送重复的消息。
ii. 消费消息阶段，不不允许消费重复的消息。
2、只有以上两个条件都满⾜足情况下，才能认为消息是“Exactly Only Once”，⽽而要实现以上两点，在分布式系统环境
下，不不可避免要产⽣生巨⼤大的开销。所以RocketMQ为了了追求⾼高性能，并不不保证此特性，要求在业务上进⾏行行去重，也就是说消费
消息要做到幂等性。RocketMQ虽然不不能严格保证不不重复，但是正常情况下很少会出现重复发送、消费情况，只有⽹网络异常，
Consumer启停等异常情况下会出现消息重复。
5. Broker的Buffer满了了怎么办？
a. 下⾯面是CORBA Notification规范中处理理⽅方式：
i. RejectNewEvents 拒绝新来的消息，向Producer返回RejectNewEvents错误码。
ii. 按照特定策略略丢弃已有消息
1. AnyOrder - Any event may be discarded on overflow. This is the default setting for this property.
2. FifoOrder - The first event received will be the first discarded.
3. LifoOrder - The last event received will be the first discarded.
特性
ActiveMQ
RabbitMQ
RocketMQ
kafka
开发语⾔言
java
erlang
java
scala
单机吞吐量量
万级
万级
10万级
10万级
时效性
ms级
us级
ms级
ms级以内
可⽤用性
⾼高(主从架构)
⾼高(主从架构)
⾮非常⾼高(分布式架构)
⾮非常⾼高(分布式架构)
功能特性
成熟的产品，在很多公司
得到应⽤用；有较多的⽂文
档；各种协议⽀支持较好
基于erlang开发，所以并
发能⼒力力很强，性能极其
好，延时很低;管理理界⾯面较
丰富
MQ功能⽐比较完备，扩展
性佳
只⽀支持主要的MQ功能
像⼀一些消息查询，消
溯等功能没有提供，
是为⼤大数据准备的，
数据领域应⽤用⼴广。
微信公众号：Java架构师进阶编程

![java面试题_消息中间件--RocketMq(14题) 第1页插图](../assets/images/java面试题_消息中间件--RocketMq(14题)_p1_1_0b055075.png)

---

4. PriorityOrder - Events should be discarded in priority order, such that lower priority events will be 
discarded before higher priority events.
5. DeadlineOrder - Events should be discarded in the order of shortest expiry deadline first.
b.  RocketMQ没有内存Buffer概念，RocketMQ的队列列都是持久化磁盘，数据定期清除。
对于此问题的解决思路路，RocketMQ同其他MQ有⾮非常显著的区别，RocketMQ的内存Buffer抽象成⼀一个⽆无限
⻓长度的队列列，不不管有多少数据进来都能装得下，这个⽆无限是有前提的，Broker会定期删除过期的数据，例例如Broker只保存3天
的消息，那么这个Buffer虽然⻓长度⽆无限，但是3天前的数据会被从队尾删除。
此问题的本质原因是⽹网络调⽤用存在不不确定性，即既不不成功也不不失败的第三种状态，所以才产⽣生了了消息重复性
问题。
6. 回溯消息：
a. 回溯消费是指Consumer已经消费成功的消息，由于业务上需求需要重新消费，要⽀支持此功能，Broker在向
Consumer投递成功消息后，消息仍然需要保留留。并且重新消费⼀一般是按照时间维度，例例如由于Consumer系统故障，
恢复后需要重新消费1⼩小时前的数据，那么Broker要提供⼀一种机制，可以按照时间维度来回退消费进度。
b. RocketMQ⽀支持按照时间回溯消费，时间维度精确到毫秒，可以向前回溯，也可以向后回溯。
7. 消息堆积：
a. 消息中间件的主要功能是异步解耦，还有个重要功能是挡住前端的数据洪峰，保证后端系统的稳定性，这就要求消
息中间件具有⼀一定的消息堆积能⼒力力，消息堆积分以下两种情况：
i. 消息堆积在内存Buffer，⼀一旦超过内存Buffer，可以根据⼀一定的丢弃策略略来丢弃消息，如CORBA Notification规
范中描述。适合能容忍丢弃消息的业务，这种情况消息的堆积能⼒力力主要在于内存Buffer⼤大⼩小，⽽而且消息堆积后，
性能下降不不会太⼤大，因为内存中数据多少对于对外提供的访问能⼒力力影响有限。
ii. 消息堆积到持久化存储系统中，例例如DB，KV存储，⽂文件记录形式。 当消息不不能在内存Cache命中时，要不不可
避免的访问磁盘，会产⽣生⼤大量量读IO，读IO的吞吐量量直接决定了了消息堆积后的访问能⼒力力。
b. 评估消息堆积能⼒力力主要有以下四点：
i. 消息能堆积多少条，多少字节？即消息的堆积容量量。
ii. 消息堆积后，发消息的吞吐量量⼤大⼩小，是否会受堆积影响？
iii. 消息堆积后，正常消费的Consumer是否会受影响？
iv. 消息堆积后，访问堆积在磁盘的消息时，吞吐量量有多⼤大？
8. 分布式事务：
1. 已知的⼏几个分布式事务规范，如XA，JTA等。其中XA规范被各⼤大数据库⼚厂商⼴广泛⽀支持，如Oracle，Mysql等。其中
XA的TM实现佼佼者如Oracle Tuxedo，在⾦金金融、电信等领域被⼴广泛应⽤用。
2. 分布式事务涉及到两阶段提交问题，在数据存储⽅方⾯面的⽅方⾯面必然需要KV存储的⽀支持，因为第⼆二阶段的提交回滚需
要修改消息状态，⼀一定涉及到根据Key去查找Message的动作。RocketMQ在第⼆二阶段绕过了了根据Key去查找Message
的问题，采⽤用第⼀一阶段发送Prepared消息时，拿到了了消息的Offset，第⼆二阶段通过Offset去访问消息，并修改状态，
Offset就是数据的地址。
3. RocketMQ这种实现事务⽅方式，没有通过KV存储做，⽽而是通过Offset⽅方式，存在⼀一个显著缺陷，即通过Offset更更改
数据，会令系统的脏⻚页过多，需要特别关注。
9. 定时消息：
a. 定时消息是指消息发到Broker后，不不能⽴立刻被Consumer消费，要到特定的时间点或者等待特定的时间后才能被消
费。
b. 如果要⽀支持任意的时间精度，在Broker层⾯面，必须要做消息排序，如果再涉及到持久化，那么消息排序要不不可避免
的产⽣生巨⼤大性能开销。
c. RocketMQ⽀支持定时消息，但是不不⽀支持任意时间精度，⽀支持特定的level，例例如定时5s，10s，1m等。
10. 消息重试：
Consumer消费消息失败后，要提供⼀一种重试机制，令消息再消费⼀一次。Consumer消费消息失败通常可以认为有以下
⼏几种情况：
i. 由于消息本身的原因，例例如反序列列化失败，消息数据本身⽆无法处理理（例例如话费充值，当前消息的⼿手机号被注
销，⽆无法充值）等。这种错误通常需要跳过这条消息，再消费其他消息，⽽而这条失败的消息即使⽴立刻重试消费，
99%也不不成功，所以最好提供⼀一种定时重试机制，即过10s秒后再重试。
ii. 由于依赖的下游应⽤用服务不不可⽤用，例例如db连接不不可⽤用，外系统⽹网络不不可达等。遇到这种错误，即使跳过当前失
败的消息，消费其他消息同样也会报错。这种情况建议应⽤用sleep 30s，再消费下⼀一条消息，这样可以减轻Broker
重试消息的压⼒力力。
微信公众号：Java架构师进阶编程

---

11. RocketMq是什什么？
上图是⼀一个典型的消息中间件收发消息的模型，RocketMQ也是这样的设计，简单说来，RocketMQ具有以下特点：
是⼀一个队列列模型的消息中间件，具有⾼高性能、⾼高可靠、⾼高实时、分布式特点。
Producer、Consumer、队列列都可以分布式。
Producer向⼀一些队列列轮流发送消息，队列列集合称为Topic，Consumer如果做⼴广播消费，则⼀一个consumer实例例消费
这个Topic对应的所有队列列，如果做集群消费，则多个Consumer实例例平均消费这个topic对应的队列列集合。
能够保证严格的消息顺序
提供丰富的消息拉取模式
⾼高效的订阅者⽔水平扩展能⼒力力
实时的消息订阅机制
亿级消息堆积能⼒力力
较少的依赖
12. RocketMq物理理部署结构
Name Server是⼀一个⼏几乎⽆无状态节点，可集群部署，节点之间⽆无任何信息同步。
Broker部署相对复杂，Broker分为Master与Slave，⼀一个Master可以对应多个Slave，但是⼀一个Slave只能对应⼀一个
Master，Master与Slave的对应关系通过指定相同的BrokerName，不不同的BrokerId来定义，BrokerId为0表示
Master，⾮非0表示Slave。Master也可以部署多个。每个Broker与Name Server集群中的所有节点建⽴立⻓长连接，定时注
册Topic信息到所有Name Server。
Producer与Name Server集群中的其中⼀一个节点（随机选择）建⽴立⻓长连接，定期从Name Server取Topic路路由信息，
并向提供Topic服务的Master建⽴立⻓长连接，且定时向Master发送⼼心跳。Producer完全⽆无状态，可集群部署。
Consumer与Name Server集群中的其中⼀一个节点（随机选择）建⽴立⻓长连接，定期从Name Server取Topic路路由信
息，并向提供Topic服务的Master、Slave建⽴立⻓长连接，且定时向Master、Slave发送⼼心跳。Consumer既可以从Master
订阅消息，也可以从Slave订阅消息，订阅规则由Broker配置决定。
13. RocketMq逻辑结构
微信公众号：Java架构师进阶编程

![java面试题_消息中间件--RocketMq(14题) 第3页插图](../assets/images/java面试题_消息中间件--RocketMq(14题)_p3_1_8fa16315.png)

![java面试题_消息中间件--RocketMq(14题) 第3页插图](../assets/images/java面试题_消息中间件--RocketMq(14题)_p3_2_eb0c5acf.png)

---

1、Producer Group
⽤用来表示⼀一个发送消息应⽤用，⼀一个Producer Group下包含多个Producer实例例，可以是多台机器器，也可以是⼀一台机
器器的多个进程，或者⼀一个进程的多个Producer对象。⼀一个Producer Group可以发送多个Topic消息，Producer Group
作⽤用如下：
1. 标识⼀一类Producer
2. 可以通过运维⼯工具查询这个发送消息应⽤用下有多个Producer实例例
3. 发送分布式事务消息时，如果Producer中途意外宕机，Broker会主动回调Producer Group内的任意⼀一台机器器
来确认事务状态。
2、Consumer Group
⽤用来表示⼀一个消费消息应⽤用，⼀一个Consumer Group下包含多个Consumer实例例，可以是多台机器器，也可以是多个
进程，或者是⼀一个进程的多个Consumer对象。⼀一个Consumer Group下的多个Consumer以均摊⽅方式消费消息，如果
设置为⼴广播⽅方式，那么这个Consumer Group下的每个实例例都消费全量量数据。
14. RocketMq数据存储结构
如上图所示，RocketMQ采取了了⼀一种数据与索引分离的存储⽅方法。有效降低⽂文件资源、IO资源，内存资源的损耗。即
便便是阿⾥里里这种海海量量数据，⾼高并发场景也能够有效降低端到端延迟，并具备较强的横向扩展能⼒力力。
 
微信公众号：Java架构师进阶编程

![java面试题_消息中间件--RocketMq(14题) 第4页插图](../assets/images/java面试题_消息中间件--RocketMq(14题)_p4_1_2fb3ce99.png)

![java面试题_消息中间件--RocketMq(14题) 第4页插图](../assets/images/java面试题_消息中间件--RocketMq(14题)_p4_2_72cb9017.png)