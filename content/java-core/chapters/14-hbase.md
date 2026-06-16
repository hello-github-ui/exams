<!-- page: 183 -->

# 14. Hbase

#### 14.1.1. 概念
base 是分布式、面向列的开源数据库(其实准确的说是面向列族)。HDFS 为 Hbase 提供可靠的
底层数据存储服务,MapReduce 为 Hbase 提供高性能的计算能力,Zookeeper 为 Hbase 提供
稳定服务和 Failover 机制,因此我们说 Hbase 是一个通过大量廉价的机器解决海量数据的高速存
储和读取的分布式数据库解决方案。

#### 14.1.2. 列式存储
列方式所带来的重要好处之一就是,由于查询中的选择规则是通过列来定义的,因此整个数据库
是自动索引化的。
这里的列式存储其实说的是列族存储,Hbase 是根据列族来存储数据的。列族下面可以有非常多
的列,列族在创建表的时候就必须指定。为了加深对 Hbase 列族的理解,下面是一个简单的关系
型数据库的表和 Hbase 数据库的表:

<!-- page: 184 -->

#### 14.1.3. Hbase 核心概念

##### 14.1.3.1. Column Family 列族
Column Family 又叫列族,Hbase 通过列族划分数据的存储,列族下面可以包含任意多的列,实
现灵活的数据存取。Hbase 表的创建的时候就必须指定列族。就像关系型数据库创建的时候必须
指定具体的列是一样的。Hbase 的列族不是越多越好,官方推荐的是列族最好小于或者等于3。我
们使用的场景一般是 1 个列族。

##### 14.1.3.2. Rowkey(Rowkey 查询,Rowkey 范围扫描,全表扫描)
Rowkey 的概念和 mysql 中的主键是完全一样的,Hbase 使用 Rowkey 来唯一的区分某一行的数
据。Hbase 只支持 3 中查询方式:基于 Rowkey 的单行查询,基于 Rowkey 的范围扫描,全表扫
描。

##### 14.1.3.3. Region 分区
 Region:Region 的概念和关系型数据库的分区或者分片差不多。Hbase 会将一个大表的数
据基于 Rowkey 的不同范围分配到不通的 Region 中,每个 Region 负责一定范围的数据访问
和存储。这样即使是一张巨大的表,由于被切割到不通的region,访问起来的时延也很低。

##### 14.1.3.4. TimeStamp 多版本
 TimeStamp 是实现 Hbase 多版本的关键。在 Hbase 中使用不同的 timestame 来标识相同
rowkey 行对应的不通版本的数据。在写入数据的时候,如果用户没有指定对应的
timestamp,Hbase 会自动添加一个 timestamp,timestamp 和服务器时间保持一致。在
Hbase 中,相同 rowkey 的数据按照 timestamp 倒序排列。默认查询的是最新的版本,用户
可同指定 timestamp 的值来读取旧版本的数据。

#### 14.1.4. Hbase 核心架构
Hbase 是由 Client、Zookeeper、Master、HRegionServer、HDFS 等几个组建组成。

<!-- page: 185 -->

##### 14.1.4.1. Client:
 Client 包含了访问 Hbase 的接口,另外 Client 还维护了对应的 cache 来加速 Hbase 的
访问,比如 cache 的.META.元数据的信息。

##### 14.1.4.2. Zookeeper:
 Hbase 通过 Zookeeper 来做 master 的高可用、RegionServer 的监控、元数据的入口
以及集群配置的维护等工作。具体工作如下:

## 1. 通过 Zoopkeeper 来保证集群中只有 1 个 master 在运行,如果 master 异
常,会通过竞争机制产生新的 master 提供服务

## 2. 通过 Zoopkeeper 来监控 RegionServer 的状态,当 RegionSevrer 有异常的
时候,通过回调的形式通知 Master RegionServer 上下限的信息

## 3. 通过 Zoopkeeper 存储元数据的统一入口地址。

##### 14.1.4.3. Hmaster
 master 节点的主要职责如下:

## 1. 为 RegionServer 分配 Region

## 2. 维护整个集群的负载均衡

## 3. 维护集群的元数据信息发现失效的 Region,并将失效的 Region 分配到正常
RegionServer 上当 RegionSever 失效的时候,协调对应 Hlog 的拆分

##### 14.1.4.4. HregionServer
 HregionServer 直接对接用户的读写请求,是真正的“干活”的节点。它的功能概括如
下:

## 1. 管理 master 为其分配的 Region

<!-- page: 186 -->

## 2. 处理来自客户端的读写请求

## 3. 负责和底层 HDFS 的交互,存储数据到 HDFS

## 4. 负责 Region 变大以后的拆分

## 5. 负责 Storefile 的合并工作

##### 14.1.4.5. Region 寻址方式(通过 zookeeper .META)
第 1 步:Client 请求 ZK 获取.META.所在的 RegionServer 的地址。
第 2 步:Client 请求.META.所在的 RegionServer 获取访问数据所在的 RegionServer 地
址,client 会将.META.的相关信息 cache 下来,以便下一次快速访问。
第 3 步:Client 请求数据所在的 RegionServer,获取所需要的数据。

##### 14.1.4.6. HDFS
 HDFS 为 Hbase 提供最终的底层数据存储服务,同时为 Hbase 提供高可用(Hlog 存储在
HDFS)的支持。

<!-- page: 187 -->

#### 14.1.5. Hbase 的写逻辑

##### 14.1.5.1. Hbase 的写入流程
从上图可以看出氛围 3 步骤:
获取 RegionServer
第 1 步:Client 获取数据写入的 Region 所在的 RegionServer
请求写 Hlog
第 2 步:请求写 Hlog, Hlog 存储在 HDFS,当 RegionServer 出现异常,需要使用 Hlog 来
恢复数据。
请求写 MemStore
第 3 步:请求写 MemStore,只有当写 Hlog 和写 MemStore 都成功了才算请求写入完成。
MemStore 后续会逐渐刷到 HDFS 中。

##### 14.1.5.2. MemStore 刷盘
为了提高 Hbase 的写入性能,当写请求写入 MemStore 后,不会立即刷盘。而是会等到一
定的时候进行刷盘的操作。具体是哪些场景会触发刷盘的操作呢?总结成如下的几个场景:

<!-- page: 188 -->

全局内存控制

## 1. 这个全局的参数是控制内存整体的使用情况,当所有memstore 占整个 heap 的最大比
例的时候,会触发刷盘的操作。这个参数是
hbase.regionserver.global.memstore.upperLimit,默认为整个 heap 内存的 40%。
但这并不意味着全局内存触发的刷盘操作会将所有的 MemStore 都进行输盘,而是通过
另外一个参数 hbase.regionserver.global.memstore.lowerLimit 来控制,默认是整个
heap 内存的 35%。当 flush 到所有 memstore 占整个 heap 内存的比率为 35%的时
候,就停止刷盘。这么做主要是为了减少刷盘对业务带来的影响,实现平滑系统负载的
目的。
MemStore 达到上限

## 2. 当 MemStore 的大小达到 hbase.hregion.memstore.flush.size 大小的时候会触发刷
盘,默认 128M 大小
RegionServer 的 Hlog 数量达到上限

## 3. 前面说到 Hlog 为了保证 Hbase 数据的一致性,那么如果 Hlog 太多的话,会导致故障
恢复的时间太长,因此 Hbase 会对 Hlog 的最大个数做限制。当达到 Hlog 的最大个数
的时候,会强制刷盘。这个参数是 hase.regionserver.max.logs,默认是 32 个。
手工触发

## 4. 可以通过 hbase shell 或者 java api 手工触发 flush 的操作。
关闭 RegionServer 触发

## 5. 在正常关闭 RegionServer 会触发刷盘的操作,全部数据刷盘后就不需要再使用 Hlog 恢
复数据。
Region 使用 HLOG 恢复完数据后触发

## 6. :当 RegionServer 出现故障的时候,其上面的 Region 会迁移到其他正常的
RegionServer 上,在恢复完 Region 的数据后,会触发刷盘,当刷盘完成后才会提供给
业务访问。

#### 14.1.6. HBase vs Cassandra
HBase Cassandra
语言 Java Java
出发点 BigTable BigTable and Dynamo
License Apache Apache
Protocol HTTP/REST (also Thrift) Custom, binary (Thrift)
数据分布 表划分为多个 region 存在不同 region
server 上
改进的一致性哈希(虚拟节点)
存储目标 大文件 小文件
一致性 强一致性 最终一致性,Quorum NRW 策略
架构 master/slave p2p
高可用性 NameNode 是 HDFS 的单点故障点 P2P 和去中心化设计,不会出现单点故障
伸缩性 Region Server 扩容,通过将自身发布到
Master,Master 均匀分布 Region
扩容需在 Hash Ring 上多个节点间调整数据分布

<!-- page: 189 -->

读写性能 数据读写定位可能要通过最多 6 次的网
络 RPC,性能较低。
数据读写定位非常快
数据冲突处理 乐观并发控制(optimistic concurrency
control)
向量时钟
临时故障处理 Region Server 宕机,重做 HLog 数据回传机制:某节点宕机,hash 到该节点的新数据自
动路由到下一节点做 hinted handoff,源节点恢复后,推
送回源节点。
永久故障恢复 Region Server 恢复,master 重新给其
分配 region
Merkle 哈希树,通过 Gossip 协议同步 Merkle Tree,维
护集群节点间的数据一致性
成员通信及错误检测 Zookeeper 基于 Gossip
CAP 1,强一致性,0 数据丢失。2,可用性
低。3,扩容方便。
1,弱一致性,数据可能丢失。2,可用性高。3,扩容方
便。
