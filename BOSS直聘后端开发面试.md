# BOSS直聘后端开发面试题

## 目录
1. [自我介绍+项目介绍](#1-自我介绍项目介绍)
2. [线程池bean如何热更新的，有什么问题？如何解决的？](#2-线程池bean如何热更新的有什么问题如何解决的)
3. [线程池核心参数？](#3-线程池核心参数)
4. [你们线程池用什么拒绝策略？](#4-你们线程池用什么拒绝策略)
5. [场景题：服务启动时预热一批数据放进内存，你会怎么实现？](#5-场景题服务启动时预热一批数据放进内存你会怎么实现)
6. [Spring自动装配是怎么实现的？](#6-spring自动装配是怎么实现的比如说怎么识别出来要加载哪些-bean-的)
7. [场景题：mysql表预计100G但实际占200G可能原因？](#7-场景题假如-mongodb-或者说-mysql-有一张表看数据预计是-100g但实际上占的存储空间可能达到-200g可能是什么原因)
8. [mysql有哪几种日志？](#8-mysql-有哪几种日志)
9. [缓存和数据库怎么保证数据一致性问题？](#9-缓存和数据库怎么保证数据一致性问题)
10. [Spring的@transaction注解失效的场景有哪些？](#10-spring-的-transaction-注解失效的场景有哪些)
11. [你们项目中grpc有没有用到注册中心，怎么来管理微服务的？](#11-你们项目中-grpc-有没有用到注册中心怎么来管理微服务的)
12. [redis能不能实现发布订阅？但为什么不推荐去做？](#12-redis能不能实现发布订阅但为什么不推荐去做)
13. [redis为什么快？](#13-redis-为什么快)
14. [grpc和http的区别？](#14-grpc-和-http-的区别)
15. [redis实现分布式锁会遇到哪些问题？](#15-redis-实现分布式锁会遇到哪些问题)

---

## 1. 自我介绍+项目介绍

> 略（根据个人实际情况回答）

---

## 2. 线程池bean如何热更新的，有什么问题？如何解决的？

### 问题分析
线程池热更新指的是在不重启应用的情况下动态修改线程池参数。

### 解决方案

**方案一：使用配置文件+@RefreshScope**
```java
@RefreshScope
@Configuration
public class ThreadPoolConfig {
    @Value("${thread.pool.core-size:10}")
    private int coreSize;

    @Bean
    public ThreadPoolExecutor threadPoolExecutor() {
        return new ThreadPoolExecutor(
            coreSize,
            coreSize * 2,
            60L,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(1000)
        );
    }
}
```

**方案二：自定义线程池管理Bean**
```java
@Component
public class DynamicThreadPoolManager {
    private volatile ThreadPoolExecutor threadPool;

    public void updateThreadPool(int coreSize, int maxSize) {
        // 创建新的线程池，替换旧的
        ThreadPoolExecutor newPool = new ThreadPoolExecutor(
            coreSize, maxSize, 60L, TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(1000),
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
        this.threadPool = newPool;
    }
}
```

**存在的问题：**
- 正在执行的任务会被中断
- 已提交但未执行的任务需要妥善处理
- 正在等待的队列任务如何迁移

### 最佳实践
- 使用 Apache Commons Pool 或 Alibaba Sentinel 提供的动态线程池
- 监控线程池状态，及时发现问题

---

## 3. 线程池核心参数？

| 参数 | 说明 |
|------|------|
| `corePoolSize` | 核心线程数，线程池维护的最小线程数 |
| `maximumPoolSize` | 最大线程数，线程池允许的最大线程数 |
| `keepAliveTime` | 空闲线程存活时间，非核心线程闲置时的超时时长 |
| `unit` | keepAliveTime 的时间单位 |
| `workQueue` | 任务队列，用于存放等待执行的任务 |
| `threadFactory` | 线程工厂，用于创建新线程 |
| `handler` | 拒绝策略，当线程池和队列都满了时的处理策略 |

**线程池拒绝策略：**
- `AbortPolicy`：直接抛出异常（默认）
- `CallerRunsPolicy`：由调用线程执行
- `DiscardPolicy`：直接丢弃任务
- `DiscardOldestPolicy`：丢弃队列中最老的任务

---

## 4. 你们线程池用什么拒绝策略？

通常推荐使用 `CallerRunsPolicy`，原因：

1. **不会丢失任务**：由调用线程执行，保证任务不丢失
2. **实现限流**：当线程池饱和时，调用方线程执行任务会变慢，自然实现限流
3. **避免资源耗尽**：不会像 `DiscardPolicy` 那样静默丢弃任务

```java
new ThreadPoolExecutor.CallerRunsPolicy()
```

如果对性能要求较高，可以考虑自定义策略：
- 记录被拒绝的任务到消息队列
- 监控告警通知运维

---

## 5. 场景题：服务启动时预热一批数据放进内存，你会怎么实现？

### 方案一：使用@PostConstruct
```java
@Component
public class DataPreloader {
    @Autowired
    private SomeService someService;

    @PostConstruct
    public void preload() {
        List<Data> dataList = someService.loadDataFromDB();
        CacheManager.putAll(dataList);
    }
}
```

### 方案二：使用ApplicationRunner或CommandLineRunner
```java
@Component
public class DataPreloader implements ApplicationRunner {
    @Override
    public void run(ApplicationArguments args) {
        // 预热逻辑
        warmUp();
    }
}
```

### 方案三：使用启动探针/健康检查
配合 K8s startupProbe 或 Spring Boot Actuator，确保预热完成后再接收流量。

### 注意事项
1. 预热数据量不能太大，避免 OOM
2. 预热过程要可监控、可回滚
3. 考虑预热失败的重试机制
4. 分布式环境下只需一个实例预热即可

---

## 6. Spring自动装配是怎么实现的？

### 实现原理

Spring 自动装配主要通过以下步骤实现：

**1. 扫描阶段**
- `ComponentScan` 扫描带有 `@Component`、`@Service`、`@Repository`、`@Controller` 等注解的类
- 将 Bean 定义注册到 `BeanDefinitionRegistry`

**2. 解析阶段**
- 处理 `@Autowired`、`@Inject`、`@Resource` 等注解
- `AutowiredAnnotationBeanPostProcessor` 负责处理 `@Autowired`

**3. 注入阶段**
- `InstantiationAwareBeanPostProcessor` 在 bean 实例化前后进行处理
- 通过反射设置依赖的 bean 属性

### 关键类
- `AutowiredAnnotationBeanPostProcessor`：处理自动装配注解
- `CommonAnnotationBeanPostProcessor`：处理 JSR-250 注解（如 `@Resource`）
- `DefaultListableBeanFactory`：Bean 工厂，负责管理 bean 注册

### 识别要加载的Bean
1. 扫描指定包路径
2. 解析 `@ComponentScan` 配置
3. 根据注解过滤器识别候选组件
4. 注册到 BeanDefinitionMap

---

## 7. 场景题：mysql表预计100G但实际占200G可能原因？

### 可能原因

**1. 数据碎片**
- 表大量更新、删除后产生碎片
- 解决方案：`OPTIMIZE TABLE` 或 `ALTER TABLE ... ENGINE=InnoDB`

**2. 稀疏列**
- 大量 NULL 值或变长字段（VARCHAR）未压缩
- InnoDB 行格式存在一定开销

**3. 索引膨胀**
- 索引数据比实际数据还大
- 解决方案：定期分析并删除无用索引

**4. 存储格式**
- InnoDB 使用 B+树存储，每页16KB，存在内部碎片
- 主键索引和辅助索引的存储开销

**5. 事务回滚**
- 未提交事务占用 undo log 空间
- 长事务导致 undo 空间膨胀

**6. 临时表和排序**
- 大结果集排序生成临时表
- `sort_buffer_size` 不足时使用磁盘

### MySQL是行存储吗？
是的，InnoDB 是**聚簇索引（Clustered Index）**，按主键顺序存储数据行。但需要注意：
- 每个 InnoDB 表都有一个主键
- 如果没有显式主键，会使用唯一非空列或隐藏主键
- 辅助索引存储主键值而非行指针

---

## 8. mysql有哪几种日志？

| 日志类型 | 作用 |
|----------|------|
| **binlog** | 记录所有写操作，用于主从复制和数据恢复 |
| **redo log** | 保证事务持久性，崩溃恢复 |
| **undo log** | 提供 MVCC 和事务回滚 |
| **error log** | 记录启动、运行、停止时的错误 |
| **slow query log** | 记录慢查询 |
| **general log** | 记录所有SQL操作（生产环境慎用） |

### binlog 使用场景

**1. 主从复制**
- 主库记录 binlog
- 从库通过 IO 线程拉取 binlog
- 从库 SQL 线程回放 binlog

**2. 数据恢复**
- 利用 binlog 进行 point-in-time 恢复
- 恢复指定时间点的数据

**3. 数据同步**
- 订阅 binlog 实现数据同步（如 Canal）

### 除了主从复制外的其他场景

**数据恢复（Point-in-Time Recovery）**
```bash
# 恢复流程
mysqlbinlog --stop-datetime="2024-01-01 12:00:00" binlog.000001 | mysql
```

**变更数据捕获（CDC）**
- Alibaba Canal
- Debezium
- Maxwell

---

## 9. 缓存和数据库怎么保证数据一致性问题？

### 方案一：Cache Aside（旁路缓存）常用

**读操作：**
1. 先读缓存
2. 缓存命中则返回
3. 缓存未命中，读数据库
4. 写入缓存
5. 返回数据

**写操作：**
1. 先更新数据库
2. 删除缓存

### 方案二：Read/Write Through

**写操作：** 先更新缓存，缓存自动更新数据库
**读操作：** 先读缓存，缓存未命中则由缓存服务加载数据

### 方案三：Write Behind

先写缓存，异步批量更新数据库

---

### Redis成功之前事务回滚了，Redis里是脏数据怎么办？

**问题分析：**
Redis 的事务使用 `MULTI/EXEC`，但 Redis 不支持回滚（与关系型数据库不同）。

**解决方案：**

1. **使用 Lua 脚本保证原子性**
```lua
-- Lua 脚本保证读写原子性
local function updateAndSet(key, value, dbKey)
    -- 先操作数据库
    db:update(dbKey, value)
    -- 再设置缓存
    redis:set(key, value)
end
```

2. **使用分布式锁**
```java
public void updateWithLock(String key, Object value) {
    String lockKey = "lock:" + key;
    String lockValue = UUID.randomUUID().toString();

    try {
        // 获取分布式锁
        if (redisTemplate.opsForValue().setIfAbsent(lockKey, lockValue, 10, TimeUnit.SECONDS)) {
            // 先更新数据库
            userDAO.update(value);
            // 删除缓存
            redisTemplate.delete(key);
        }
    } finally {
        // 释放锁
        redisTemplate.delete(lockKey);
    }
}
```

3. **延迟双删**
```java
public void updateWithDelayDelete(String key, Object value) {
    // 1. 先更新数据库
    userDAO.update(value);
    // 2. 删除缓存
    redisTemplate.delete(key);

    // 3. 延迟一段时间后再删除（解决并发问题）
    Thread.sleep(100);
    redisTemplate.delete(key);
}
```

---

## 10. Spring的@transaction注解失效的场景有哪些？

### 1. 方法内部调用
```java
// 失效示例
public class UserService {
    public void update() {
        this.insert(); // 内部调用，不经过代理
    }

    @Transactional
    public void insert() {
        // 不会生效！
    }
}
```
**解决：** 注入自身或使用 AopContext.currentProxy()

### 2. 异常被catch捕获
```java
@Transactional
public void update() {
    try {
        // 操作
    } catch (Exception e) {
        // 异常被捕获，未抛出
    }
}
```
**解决：** 重新抛出异常或不使用 try-catch

### 3. 异常类型不匹配
```java
@Transactional(rollbackFor = RuntimeException.class)
public void update() throws Exception {
    throw new Exception(); // 默认只回滚 RuntimeException
}
```
**解决：** 配置 `rollbackFor = Exception.class`

### 4. 传播属性问题
```java
@Transactional(propagation = Propagation.NOT_SUPPORTED)
public void update() {
    // NOT_SUPPORTED 会挂起当前事务
}
```

### 5. 非public方法
```java
@Transactional
void update() { // private 方法，事务不生效
}
```

### 6. 同一个类中无事务方法调用有事务方法

### 7. 多数据源配置问题

---

## 11. 你们项目中grpc有没有用到注册中心，怎么来管理微服务的？

### 常用方案

**1. Consul**
- HashiCorp 提供的服务发现工具
- 支持健康检查
- 提供 KV 存储

**2. Nacos**
- Alibaba 出品
- 支持配置中心和服务发现
- 国产，文档完善

**3. Etcd**
- CoreOS 出品
- 基于 Raft 协议
- 高可用

**4. Zookeeper**
- 传统方案
- CP 模型，保证一致性

### 服务注册与发现流程
```
服务启动 → 注册自身信息(IP:Port) → 注册中心
                                      ↓
                              健康检查
                                      ↓
服务调用 → 查询注册中心 → 获取服务地址列表 → 负载均衡 → 调用
```

### grpc 集成示例
```protobuf
syntax = "proto3";
package user;
service UserService {
    rpc GetUser (GetUserRequest) returns (UserResponse);
}
```

### 负载均衡
- 客户端负载均衡：grpc 客户端直接选择
- 服务端负载均衡：L4/L7 负载均衡器

---

## 12. redis能不能实现发布订阅？但为什么不推荐去做？

### 可以实现发布订阅
```bash
PUBLISH channel message
SUBSCRIBE channel
```

```java
redisTemplate.convertAndSend("channel", "message");
```

### 不推荐的原因

**1. 没有消息持久化**
- 消息发送后，如果订阅者不在线，消息丢失

**2. 没有 ACK 确认**
- 消息发送后无法确认是否被消费

**3. 没有消息堆积**
- 内存 unbounded，可能导致 OOM

**4. 无法实现消息消费跟踪**
- 无法知道哪些消息被消费

**5. 没有消息重试机制**

**6. 客户端断线重连问题**
- 需要手动处理

### 替代方案

**1. 专业消息队列**
- RabbitMQ
- Kafka
- RocketMQ
- Apache Pulsar

**2. Redis Streams（5.0+）**
```bash
XADD mystream * sensor-id 1234 temperature 19.8
XREAD COUNT 2 STREAMS mystream 0
```
- 支持持久化
- 支持消费组
- 支持 ACK

---

## 13. redis为什么快？

### 1. 内存存储
- 所有数据在内存中，O(1) 访问时间

### 2. 单线程模型
- 避免上下文切换
- 避免锁竞争
- 纯内存操作非常快

### 3. IO多路复用
- 使用 epoll/select/kqueue
- 单线程处理大量并发连接

### 4. 高效数据结构
- SDS（简单动态字符串）：O(1) 长度获取
- ZipList：压缩列表，小数据友好
- QuickList：结合链表和压缩列表
- 跳表：有序集合实现

### 5. 定制内存分配
-jemalloc/tcmalloc

---

## 14. grpc和http的区别？

### grpc vs HTTP

| 特性 | grpc | HTTP |
|------|------|------|
| 协议 | HTTP/2 | HTTP/1.1/2/3 |
| 传输格式 | Protocol Buffers | JSON/XML |
| 代码生成 | 自动生成 | 无 |
| 严格模式 | 必须定义 .proto | 灵活 |
| 流式通信 | 支持 | 受限 |
| 浏览器支持 | 需要 grpc-web | 原生支持 |
| 性能 | 更高 | 一般 |

### protobuf vs JSON

**protobuf 优点：**
- 体积小（序列化后）
- 解析快
- 类型安全
- 强类型定义

**protobuf 示例：**
```protobuf
message User {
    int32 id = 1;
    string name = 2;
    string email = 3;
}
```

### 场景题：传50M文件用grpc还是http？

**推荐 HTTP，原因：**
1. grpc 单个消息有大小限制（通常 4MB）
2. 50M 文件需要流式传输，grpc 流式实现复杂
3. HTTP 生态更成熟，CDN 支持更好

**如果用 grpc 传输：**
- 使用 server streaming 或 client streaming
- 需要分片传输
- 实现复杂，不推荐

---

## 15. redis实现分布式锁会遇到哪些问题？

### 1. 原子性问题
**问题：** `SET key value NX EX` 之前的方式不原子

**解决：** 使用 `SET key value NX EX timeout`

```java
String lockKey = "order:lock:" + orderId;
String lockValue = UUID.randomUUID().toString();

// 原子性加锁
Boolean success = redisTemplate.opsForValue()
    .setIfAbsent(lockKey, lockValue, 10, TimeUnit.SECONDS);
```

### 2. 锁误删问题
**问题：** 线程A超时释放了线程B的锁

**解决：** 只释放自己的锁（验证 value）
```java
if (lockValue.equals(redisTemplate.opsForValue().get(lockKey))) {
    redisTemplate.delete(lockKey);
}
```

### 3. 可重入问题
**解决：** 使用 ThreadLocal 存储重入计数
```java
private static ThreadLocal<Map<String, Integer>> lockCount = ThreadLocal.withInitial(HashMap::new);
```

### 4. 锁超时导致的安全问题
**问题：** 任务未执行完，锁已释放

**解决：**
- watchdog 机制（如 Redisson）
- 锁续期

### 5. 主从切换问题
**问题：** 主节点加锁后宕机，从节点晋升，锁丢失

**解决：**
- RedLock 算法（需多个独立 Redis 节点）
- 或使用 Redisson 的看门狗机制

### 6. 公平锁问题
**解决：** 使用有序队列实现公平锁

### Redisson 示例
```java
RLock lock = redissonClient.getLock("myLock");
try {
    // 等待100秒，锁定30秒自动释放
    lock.tryLock(100, 30, TimeUnit.SECONDS);
    // 业务逻辑
} finally {
    lock.unlock();
}
```
