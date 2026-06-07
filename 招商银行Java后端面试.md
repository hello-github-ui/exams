# 招商银行Java后端面试题

## 目录

- [1. 请做一下自我介绍](#1-请做一下自我介绍)
- [2. redis的基本数据类型有哪些？](#2-redis-的基本数据类型有哪些)
- [3. 缓存穿透及防范](#3-缓存穿透及防范)
- [4. 热点数据失效时的并发处理](#4-热点数据失效时的并发处理)
- [5. redis故障恢复期间的缓存保护](#5-redis故障恢复期间的缓存保护)
- [6. MySQL及存储引擎](#6-mysql及存储引擎)
- [7. Spring请求处理流程](#7-spring中处理一个请求会经过哪些模块处理)
- [8. HashMap和ConcurrentHashMap](#8-java中-hashmap-和-concurrenthashmap-有什么区别)
- [9. 一致性哈希](#9-什么是一致性哈希)
- [10. 设计模式](#10-用过哪些设计模式)
- [11. 线程创建方式](#11-线程的创建方式有哪些)
- [12. 线程池核心参数和工作流程](#12-线程池核心参数和工作流程)
- [13. A和B服务交互方案](#13-ab服务交互设计方案)
- [14. 两个大集合找重复元素](#14-两个大集合找重复元素)
- [15. 编程题：找到字符串中所有字母异位词](#15-编程题找到字符串中所有字母异位词)

---

## 1. 请做一下自我介绍

> 略（根据个人实际情况回答）

---

## 2. redis的基本数据类型有哪些？

Redis 有 5 种基本数据类型：

| 数据类型 | 结构 | 使用场景 | 示例命令 |
|----------|------|----------|----------|
| **String** | 字符串 | 缓存、计数器、分布式锁 | `SET`, `GET`, `INCR` |
| **Hash** | 哈希表 | 存储对象、购物车 | `HSET`, `HGET`, `HGETALL` |
| **List** | 列表 | 消息队列、排行榜、栈 | `LPUSH`, `RPOP`, `LRANGE` |
| **Set** | 集合 | 标签、好友关系、去重 | `SADD`, `SMEMBERS`, `SINTER` |
| **Zset** | 有序集合 | 排行榜、延时队列 | `ZADD`, `ZRANGE`, `ZREVRANGE` |

### 详细说明

**String**
```bash
SET key value
GET key
INCR count        # 原子递增
DECR count        # 原子递减
SETEX key 3600 value  # 设置过期时间
```

**Hash**
```bash
HSET user:1 name "Alice" age "25"
HGET user:1 name
HGETALL user:1
```

**List**
```bash
LPUSH mylist "a"      # 左边插入
RPUSH mylist "b"      # 右边插入
LRANGE mylist 0 -1    # 获取所有
```

**Set**
```bash
SADD tags "java" "redis"
SMEMBERS tags         # 获取所有成员
SINTER set1 set2       # 交集
```

**Zset**
```bash
ZADD leaderboard 100 "Alice"
ZADD leaderboard 90 "Bob"
ZRANGE leaderboard 0 -1 WITHSCORES  # 按分数升序
```

### 特殊数据类型

| 数据类型 | 说明 | 使用场景 |
|----------|------|----------|
| **Bitmap** | 位图 | 用户签到、活跃用户统计 |
| **HyperLogLog** | 基数统计 | UV 统计 |
| **Geospatial** | 地理位置 | 附近的人 |
| **Stream** | 日志流 | 消息队列（5.0+） |

---

## 3. 缓存穿透及防范

### 问题描述
大量请求查询不存在的 key，全部穿透到数据库，导致数据库压力暴增。

### 解决方案

#### 方案一：布隆过滤器

```java
// 使用 Google Guava BloomFilter
BloomFilter<String> bloomFilter = BloomFilter.create(
    Funnels.stringFunnel(StandardCharsets.UTF_8),
    1000000,  // 预期插入数量
    0.01      // 误判率
);

// 初始化时将所有存在的 key 加入布隆过滤器
for (String key : existingKeys) {
    bloomFilter.put(key);
}

// 查询时先检查布隆过滤器
public String get(String key) {
    if (!bloomFilter.mightContain(key)) {
        return null;  // 一定不存在，直接返回
    }
    // 可能存在，继续查询缓存和数据库
    return queryFromCacheOrDB(key);
}
```

**布隆过滤器放在哪一层？**
- 放在 Redis 缓存层之前
- 请求先到 BloomFilter，如果不存在直接返回，不查 Redis 和 DB

#### 方案二：缓存空值

```java
public String get(String key) {
    // 先查缓存
    String value = redis.get(key);
    if (value != null) {
        return value;
    }

    // 查数据库
    value = db.query(key);
    if (value == null) {
        // 缓存空值，避免重复查数据库
        redis.setex(key, 5 * 60, "NULL");  // 短过期时间
    } else {
        redis.setex(key, 1 * 60 * 60, value);
    }
    return value;
}
```

#### 方案三：白名单/黑名单

```java
// 维护一个白名单，只允许白名单中的 key 查询
Set<String> whitelist = new HashSet<>();

public String get(String key) {
    if (!whitelist.contains(key)) {
        return null;
    }
    // 正常查询
}
```

### 误判后数据库被打爆的问题

**解决方案：**

1. **限制查询频率**
```java
// 使用计数器限制单个 key 的查询频率
String rateLimitKey = "rate_limit:" + key;
Long count = redis.incr(rateLimitKey);
if (count == 1) {
    redis.expire(rateLimitKey, 1);  // 1秒过期
}
if (count > 100) {  // 超过阈值直接返回
    return null;
}
```

2. **使用锁保护**
```java
public String getWithLock(String key) {
    String value = redis.get(key);
    if (value != null) {
        return value;
    }

    // 获取分布式锁
    String lockKey = "lock:" + key;
    if (redis.setnx(lockKey, "1", 10)) {
        try {
            // 查询数据库并回填缓存
            value = db.query(key);
            if (value != null) {
                redis.setex(key, 3600, value);
            }
        } finally {
            redis.delete(lockKey);
        }
    } else {
        // 等待其他线程查询结果
        Thread.sleep(100);
        return redis.get(key);
    }
    return value;
}
```

3. **多级缓存**
```
请求 → 布隆过滤器 → 本地缓存 → Redis → 数据库
```

---

## 4. 热点数据失效时的并发处理

### 问题描述
热点数据刚好失效，瞬间大量请求同时查数据库，可能造成数据库压力过大。

### 解决方案

#### 方案一：分布式锁

```java
public String getWithLock(String key) {
    String value = redis.get(key);
    if (value != null) {
        return value;
    }

    String lockKey = "lock:" + key;
    String lockValue = UUID.randomUUID().toString();

    try {
        // 尝试获取锁
        if (redis.setnx(lockKey, lockValue, 10, TimeUnit.SECONDS)) {
            // 获取到锁，查询数据库
            value = db.query(key);
            if (value != null) {
                redis.setex(key, 3600, value);
            }
        } else {
            // 没获取到锁，短暂等待后重试
            Thread.sleep(50);
            return redis.get(key);
        }
    } finally {
        // 只释放自己的锁
        if (lockValue.equals(redis.get(lockKey))) {
            redis.delete(lockKey);
        }
    }
    return value;
}
```

#### 方案二：本地锁 + 单一写

```java
private ReentrantLock localLock = new ReentrantLock();
private ConcurrentHashMap<String, String> localCache = new ConcurrentHashMap<>();

public String get(String key) {
    // 先查本地缓存
    String value = localCache.get(key);
    if (value != null) {
        return value;
    }

    // 尝试获取本地锁
    localLock.lock();
    try {
        // 双重检查
        value = localCache.get(key);
        if (value == null) {
            value = queryFromRedisOrDB(key);
            localCache.put(key, value);
        }
    } finally {
        localLock.unlock();
    }
    return value;
}
```

#### 方案三：热点数据永不过期

```java
public String get(String key) {
    String value = redis.get(key);

    if (value == null) {
        // 异步查询并回填
        queryAndCache(key);
        return db.query(key);  // 返回旧值或默认值
    }

    // 使用异步线程更新缓存
    String ttl = redis.ttl(key);
    if (ttl < 300) {  // 剩余5分钟时异步更新
        asyncUpdateCache(key);
    }

    return value;
}
```

#### 方案四：逻辑过期

```java
class CacheEntry<T> {
    T value;
    long expireTime;  // 逻辑过期时间
}

public T getWithLogicalExpire(String key) {
    CacheEntry<T> entry = redis.get(key);

    if (entry == null) {
        return queryFromDB(key);
    }

    if (entry.expireTime < System.currentTimeMillis()) {
        // 已逻辑过期，开启异步更新
        threadPool.execute(() -> {
            T newValue = queryFromDB(key);
            entry.value = newValue;
            entry.expireTime = System.currentTimeMillis() + 3600000;
            redis.set(key, entry);
        });
    }

    return entry.value;
}
```

### 锁的粒度

**Redis 锁 vs 本地锁：**

| 特性 | Redis 分布式锁 | 本地锁 |
|------|---------------|--------|
| 作用域 | 跨 JVM | 单 JVM |
| 性能 | 稍慢（网络开销） | 快 |
| 复杂度 | 高 | 低 |
| 可靠性 | 高（需 Redisson 等） | 低 |

**推荐：Redis 分布式锁**
- 本地锁只能锁住单个 JVM，无法解决分布式场景
- Redis 锁可以跨进程、跨机器

### 锁超时了怎么办？

1. **设置合理的锁超时时间**
```java
// 锁超时时间 = 业务预估时间 + buffer
redis.setnx(lockKey, value, 30, TimeUnit.SECONDS);
```

2. **使用 watchdog 机制（Redisson）**
```java
RLock lock = redissonClient.getLock(key);
lock.tryLock(100, 30, TimeUnit.SECONDS);
// Redisson 会自动续期
```

3. **兜底策略**
```java
public String get(String key) {
    try {
        return queryFromRedisOrDB(key);
    } catch (Exception e) {
        // 锁超时等异常，走兜底逻辑
        return getFromBackup(key);
    }
}
```

---

## 5. redis故障恢复期间的缓存保护

### 问题描述
Redis 故障恢复需要 1 分钟，这期间所有请求穿透到数据库，可能打爆数据库。

### 解决方案

#### 方案一：本地缓存

```java
private LoadingCache<String, String> localCache = Caffeine.newBuilder()
    .maximumSize(10000)
    .expireAfterWrite(5, TimeUnit.MINUTES)
    .build(key -> queryFromDB(key));

public String get(String key) {
    // 先查本地缓存
    String value = localCache.get(key);
    if (value != null) {
        return value;
    }

    // 本地缓存也没有，查数据库
    return queryFromDB(key);
}
```

#### 方案二：多级缓存

```
请求 → L1(本地缓存) → L2(Redis) → DB
```

```java
private LoadingCache<String, String> l1Cache = Caffeine.newBuilder()
    .maximumSize(1000)
    .expireAfterWrite(1, TimeUnit.MINUTES)
    .build(key -> {
        // L1 未命中，查 Redis
        String value = redis.get(key);
        if (value == null) {
            value = queryFromDB(key);
            redis.setex(key, 3600, value);
        }
        return value;
    });

public String get(String key) {
    return l1Cache.get(key);
}
```

#### 方案三：熔断降级

```java
public String getWithCircuitBreaker(String key) {
    if (redis.isDown()) {
        // Redis 不可用，走降级
        return getFromLocalCacheOrDB(key);
    }

    try {
        return redis.get(key);
    } catch (Exception e) {
        // Redis 异常，触发熔断
        redisCircuitBreaker.recordFailure();
        return getFromLocalCacheOrDB(key);
    }
}
```

#### 方案四：请求限流

```java
// 使用计数器限流
String rateLimitKey = "rate_limit:global";
Long count = redis.incr(rateLimitKey);
if (count == 1) {
    redis.expire(rateLimitKey, 1);
}

// 如果超过阈值，说明 Redis 可能有压力
if (count > 10000) {
    // 触发限流保护
    throw new RateLimitException("请求过于频繁");
}
```

#### 方案五：预热热点数据

```java
// 启动时预热热点数据
@PostConstruct
public void warmUp() {
    List<String> hotKeys = getHotKeysFromConfig();
    for (String key : hotKeys) {
        String value = db.query(key);
        redis.setex(key, 3600, value);
        localCache.put(key, value);
    }
}
```

#### 最佳实践组合

```
1. 本地缓存（L1）+ Redis（L2）+ DB（L3）
2. 热点数据永不过期 + 异步更新
3. 熔断降级 + 请求限流
4. 定期预热 + 监控告警
```

---

## 6. MySQL及存储引擎

### MySQL 简介

MySQL 是开源关系型数据库，最流行的数据库之一。

### 存储引擎

| 存储引擎 | 事务支持 | 锁粒度 | 外键 | 应用场景 |
|----------|----------|--------|------|----------|
| **InnoDB** | 支持 | 行级锁 | 支持 | 默认首选 |
| **MyISAM** | 不支持 | 表级锁 | 不支持 | 只读、表统计 |
| **MEMORY** | 不支持 | 表级锁 | 不支持 | 临时表、缓存 |
| **Archive** | 不支持 | 行级锁 | 不支持 | 日志、归档 |

### InnoDB vs MyISAM

| 特性 | InnoDB | MyISAM |
|------|--------|--------|
| **事务** | 支持 | 不支持 |
| **外键** | 支持 | 不支持 |
| **锁** | 行级锁 | 表级锁 |
| **MVCC** | 支持 | 不支持 |
| **崩溃恢复** | 自动恢复 | 需手动修复 |
| **全文索引** | 5.6+ 支持 | 支持 |
| **索引** | 聚簇索引 | 非聚簇索引 |
| **COUNT** | 较慢（需扫描） | 快（存储记录数） |

### 为什么 InnoDB 选择 B+树作为索引？

**B+树 vs B树：**

| 特性 | B树 | B+树 |
|------|-----|------|
| 数据存储 | 所有节点都存储数据 | 只有叶子节点存储数据 |
| 叶子节点 | 不相连 | 通过链表相连 |
| 范围查询 | 需要中序遍历 | 只需遍历链表 |
| 高度 | 较高 | 较低（IO次数少） |

**B+树的优势：**
1. **IO 次数少**：非叶子节点不存储数据，可以容纳更多索引
2. **范围查询快**：叶子节点链表相连
3. **查询稳定**：所有查询都需要到叶子节点

### 数据库三范式

**第一范式（1NF）：原子性**
- 每个列都是不可分割的原子值
- 示例：`地址` 应拆分为 `省`、`市`、`区`

**第二范式（2NF）：唯一性**
- 消除部分依赖
- 主键与非主键字段必须完全依赖主键
- 示例：学号+课程号为主键，成绩依赖两者，但学生姓名只依赖学号

**第三范式（3NF）：独立性**
- 消除传递依赖
- 非主键字段不能依赖其他非主键字段
- 示例：学号 → 班级号 → 班级名（传递依赖）

### 数据库设计为什么要遵循三范式？

**优点：**
1. 减少数据冗余
2. 避免数据更新异常（插入、删除、更新）
3. 提高数据一致性

**缺点：**
1. 查询时可能需要多表连接，性能较差
2. 实现复杂

**反范式化：**
- 为了性能，可以适当冗余
- 用空间换时间

---

## 7. Spring中处理一个请求会经过哪些模块处理

### 请求处理流程

```
请求 → Filter → DispatcherServlet → HandlerMapping → HandlerAdapter
                                                              ↓
                                                         Handler
                                                              ↓
                                                      HandlerInterceptor
                                                              ↓
                                                         ViewResolver
                                                              ↓
                                                           View
                                                              ↓
                                                         响应
```

### 详细步骤

**1. Filter（过滤器）**
- 字符编码过滤
- 安全过滤
- 请求日志

**2. DispatcherServlet（前端控制器）**
- 统一入口
- 协调各组件工作

**3. HandlerMapping（处理器映射）**
- 根据 URL 找到对应的 Handler（Controller）
- 实现类：`RequestMappingHandlerMapping`、`BeanNameUrlHandlerMapping`

**4. HandlerAdapter（处理器适配器）**
- 执行 Handler
- 处理参数绑定

**5. Handler（Controller）**
- 业务逻辑处理
- 返回 ModelAndView

**6. HandlerInterceptor（拦截器）**
- `preHandle`：前置处理
- `postHandle`：后置处理
- `afterCompletion`：完成处理

**7. ViewResolver（视图解析器）**
- 解析视图名
- 如 `InternalResourceViewResolver`

**8. View（视图）**
- 渲染页面
- 如 JSP、Thymeleaf

### Spring 中的类和执行顺序

**启动时执行的方法/注解：**

| 顺序 | 类/注解 | 执行的时机 |
|------|---------|------------|
| 1 | 静态代码块 | 类加载时 |
| 2 | 构造方法 | 实例化时 |
| 3 | `@PostConstruct` | Bean 初始化后 |
| 4 | `InitializingBean.afterPropertiesSet()` | Bean 初始化后 |
| 5 | `@Bean(initMethod)` | Bean 初始化后 |

### 执行顺序验证

```java
public class LifeCycleDemo {

    static {
        System.out.println("1. 静态代码块");
    }

    private String name;

    public LifeCycleDemo() {
        System.out.println("2. 构造方法");
    }

    @PostConstruct
    public void init() {
        System.out.println("3. @PostConstruct");
    }

    @Autowired
    public void autowire(SomeBean someBean) {
        System.out.println("4. @Autowired");
    }
}
```

**执行顺序：静态代码块 > 构造方法 > @Autowired > @PostConstruct**

---

## 8. Java中 HashMap 和 ConcurrentHashMap 有什么区别

### 主要区别

| 特性 | HashMap | ConcurrentHashMap |
|------|---------|-------------------|
| **线程安全** | 不安全 | 安全 |
| **锁机制** | 无 | CAS + synchronized |
| **null 支持** | Key 和 Value 都可为 null | Key 和 Value 都不能为 null |
| **性能** | 高（单线程） | 高（多线程） |
| **实现** | 数组+链表+红黑树 | 数组+链表+红黑树 |
| **迭代** | fail-fast | 弱一致迭代 |

### JDK 1.7 vs 1.8 的区别

#### HashMap

| 特性 | 1.7 | 1.8 |
|------|-----|-----|
| 数据结构 | 数组+链表 | 数组+链表+红黑树 |
| 插入方式 | 头插法 | 尾插法 |
| 扩容 | 重新 hash | 重新 hash |
| 死循环问题 | 可能（头插法） | 已修复 |

#### ConcurrentHashMap

| 特性 | 1.7 | 1.8 |
|------|-----|-----|
| 锁机制 | Segment 分段锁 | CAS + synchronized |
| 锁粒度 | Segment（数组级别） | 数组每个位置 |
| 数据结构 | Segment + HashEntry | Node + TreeNode |
| 并发度 | 16（默认） | 数组长度 |

### JDK 1.8 ConcurrentHashMap 详解

```java
// 核心数据结构
transient Node<K,V>[] table;

// Node 结构
static class Node<K,V> implements Map.Entry<K,V> {
    final int hash;
    final K key;
    volatile V val;
    volatile Node<K,V> next;
}

// 核心方法
public V put(K key, V value) {
    return putVal(key, value, false);
}

final V putVal(K key, V value, boolean onlyIfAbsent) {
    if (key == null || value == null) throw new NullPointerException();

    int hash = spread(key.hashCode());
    int binCount = 0;

    for (Node<K,V>[] tab = table;;) {
        Node<K,V> f; int n, i, fh;
        if (tab == null || (n = tab.length) == 0) {
            // 初始化
            tab = initTable();
        } else if ((f = tabAt(tab, i = (n - 1) & hash)) == null) {
            // CAS 添加新节点
            if (casTabAt(tab, i, null, new Node<K,V>(hash, key, value, null))) {
                break;
            }
        } else {
            // 链表或红黑树处理
            synchronized (f) {
                // ...
            }
        }
    }
    return null;
}
```

### 为什么 ConcurrentHashMap 不支持 null？

1. **避免二义性**：无法区分 null 是"不存在"还是"值就是 null"
2. **并发安全**：避免 NPE 和并发修改的组合问题
3. **与 HashMap 的一致性**：设计决策

---

## 9. 什么是一致性哈希？

### 普通哈希的问题

```
服务器数 = 3
key % 3 = 0 → Server A
key % 3 = 1 → Server B
key % 3 = 2 → Server C

问题：服务器数量变化时，大量 key 需要重新分配
```

### 一致性哈希原理

```
将哈希值空间组织成环形：0 ~ 2^32-1

                    Server A (hash=100)
                       ↑
    Server C (hash=300) ←  ←  Server B (hash=200)
```

**特点：**
- 每个服务器映射到环上某个位置
- key 顺时针找到第一个服务器

### 虚拟节点

为每个服务器创建多个虚拟节点，提高分布均匀性。

```
Server A: A1, A2, A3
Server B: B1, B2, B3
Server C: C1, C2, C3
```

### 一致性哈希 vs 普通哈希

| 特性 | 普通哈希 | 一致性哈希 |
|------|----------|------------|
| 扩缩容影响 | 所有 key 重新分配 | 只影响部分 key |
| 数据分布 | 可能不均匀 | 均匀（虚拟节点） |
| 适用场景 | 固定数量服务器 | 动态扩缩容 |
| 复杂度 | 简单 | 较复杂 |

### Java 实现

```java
public class ConsistentHash<T> {
    private final HashFunction hashFunction;
    private final Map<Integer, T> circle = new HashMap<>();
    private final Map<T, List<Integer>> virtualNodes = new HashMap<>();

    public ConsistentHash(HashFunction hashFunction, int virtualNodes) {
        this.hashFunction = hashFunction;
        // 为每个物理节点创建虚拟节点
        for (T node : nodes) {
            add(node, virtualNodes);
        }
    }

    public void add(T node, int virtualNodes) {
        for (int i = 0; i < virtualNodes; i++) {
            int hash = hashFunction.hash(node.toString() + ":" + i);
            circle.put(hash, node);
            virtualNodes.computeIfAbsent(node, k -> new ArrayList<>()).add(hash);
        }
    }

    public T get(String key) {
        if (circle.isEmpty()) {
            return null;
        }
        int hash = hashFunction.hash(key);
        // 找到第一个大于等于 hash 的节点
        Map.Entry<Integer, T> entry = circle.ceilingEntry(hash);
        if (entry == null) {
            entry = circle.firstEntry();
        }
        return entry.getValue();
    }
}
```

---

## 10. 用过哪些设计模式？

### 常见设计模式分类

| 分类 | 模式 |
|------|------|
| **创建型** | 单例、工厂、抽象工厂、建造者、原型 |
| **结构型** | 适配器、装饰器、代理、桥接、组合、外观 |
| **行为型** | 策略、观察者、模板方法、职责链、迭代器、命令 |

### 常用设计模式举例

**1. 单例模式**
```java
public class Singleton {
    private static volatile Singleton instance;
    private Singleton() {}
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

**2. 工厂模式**
```java
public interface Product {}
public class ProductA implements Product {}
public class ProductB implements Product {}

public class Factory {
    public Product create(String type) {
        if ("A".equals(type)) {
            return new ProductA();
        } else if ("B".equals(type)) {
            return new ProductB();
        }
        throw new IllegalArgumentException();
    }
}
```

**3. 策略模式**
```java
public interface PayStrategy {
    void pay(double amount);
}

public class AlipayStrategy implements PayStrategy {
    public void pay(double amount) { /* 支付宝支付 */ }
}

public class WechatPayStrategy implements PayStrategy {
    public void pay(double amount) { /* 微信支付 */ }
}

public class Order {
    private PayStrategy strategy;
    public void setStrategy(PayStrategy strategy) {
        this.strategy = strategy;
    }
    public void pay(double amount) {
        strategy.pay(amount);
    }
}
```

**4. 装饰器模式**
```java
public interface DataReader {
    String read();
}

public class FileReader implements DataReader {
    public String read() { return "file data"; }
}

public class BufferedReader extends FileReader {
    private FileReader reader;
    public BufferedReader(FileReader reader) {
        this.reader = reader;
    }
    public String read() {
        return "buffered:" + reader.read();
    }
}
```

**5. 代理模式**
```java
public interface Subject {
    void request();
}

public class RealSubject implements Subject {
    public void request() { /* 真实逻辑 */ }
}

public class ProxySubject implements Subject {
    private RealSubject real;
    public void request() {
        if (real == null) {
            real = new RealSubject();
        }
        // 前置处理
        System.out.println("before");
        real.request();
        // 后置处理
        System.out.println("after");
    }
}
```

**6. 观察者模式**
```java
public interface Observer {
    void update(String message);
}

public class Subject {
    private List<Observer> observers = new ArrayList<>();
    public void attach(Observer observer) { observers.add(observer); }
    public void notifyAll(String message) {
        for (Observer o : observers) {
            o.update(message);
        }
    }
}
```

---

## 11. 线程的创建方式有哪些？

### 三种创建方式

**1. 继承 Thread 类**
```java
public class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread running");
    }
}

new MyThread().start();
```

**2. 实现 Runnable 接口**
```java
public class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Runnable running");
    }
}

new Thread(new MyRunnable()).start();
```

**3. 实现 Callable 接口**
```java
public class MyCallable implements Callable<String> {
    @Override
    public String call() throws Exception {
        return "Callable result";
    }
}

FutureTask<String> task = new FutureTask<>(new MyCallable());
new Thread(task).start();
String result = task.get();  // 获取返回值
```

### Runnable vs Callable

| 特性 | Runnable | Callable |
|------|----------|----------|
| 返回值 | 无 | 有（泛型） |
| 异常 | 不能抛出受检异常 | 可以抛出受检异常 |
| 执行 | 通过 Thread 执行 | 通过 FutureTask + Thread |
| 方法名 | run() | call() |

### 其他创建方式

**线程池创建**
```java
ExecutorService executor = Executors.newFixedThreadPool(10);
executor.submit(() -> {
    System.out.println("线程池执行");
});
```

**CompletableFuture（异步编程）**
```java
CompletableFuture.supplyAsync(() -> "result")
    .thenApply(result -> result + " processed");
```

---

## 12. 线程池核心参数和工作流程

### 核心参数

| 参数 | 说明 |
|------|------|
| `corePoolSize` | 核心线程数 |
| `maximumPoolSize` | 最大线程数 |
| `keepAliveTime` | 空闲线程存活时间 |
| `unit` | 时间单位 |
| `workQueue` | 任务队列 |
| `threadFactory` | 线程工厂 |
| `handler` | 拒绝策略 |

### 线程池工作流程

```
                    新任务提交
                        ↓
                核心线程数未满？
                   ↙    ↘
                 是          否
                  ↓          ↓
           创建核心线程      队列未满？
           执行任务          ↙    ↘
                          是      否
                            ↓      ↓
                      加入队列    最大线程数未满？
                                 ↙    ↘
                               是      否
                                ↓      ↓
                         创建线程    执行拒绝策略
                         执行任务
```

### 拒绝策略

| 策略 | 行为 |
|------|------|
| `AbortPolicy` | 抛出 RejectedExecutionException |
| `CallerRunsPolicy` | 由调用线程执行 |
| `DiscardPolicy` | 静默丢弃 |
| `DiscardOldestPolicy` | 丢弃最老的任务 |

### 创建线程池的方式

```java
// 常见线程池
ExecutorService fixed = Executors.newFixedThreadPool(10);  // 固定大小
ExecutorService cached = Executors.newCachedThreadPool();   // 可扩展
ExecutorService single = Executors.newSingleThreadExecutor(); // 单线程
ExecutorService scheduled = Executors.newScheduledThreadPool(10); // 定时任务
```

### 线程池参数配置

```java
// 自定义线程池
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    8,                      // corePoolSize
    16,                     // maximumPoolSize
    60L,                    // keepAliveTime
    TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(1000),  // 队列容量
    new ThreadFactory() {
        private AtomicInteger count = new AtomicInteger(1);
        @Override
        public Thread newThread(Runnable r) {
            return new Thread(r, "my-pool-" + count.getAndIncrement());
        }
    },
    new ThreadPoolExecutor.CallerRunsPolicy()  // 拒绝策略
);
```

### 合理配置线程池

**CPU 密集型：**
- `corePoolSize = CPU核心数 + 1`
- 避免 CPU 等待

**IO 密集型：**
- `corePoolSize = CPU核心数 * 2`
- CPU 大部分时间在等待 IO

---

## 13. A和B服务交互设计方案

### 方案一：同步 HTTP/REST 调用

**A 调用 B，B 执行完后返回结果。**

```java
// A 服务
@RestController
public class AController {
    @Autowired
    private RestTemplate restTemplate;

    public String callB(String param) {
        return restTemplate.postForObject("http://B-service/b/api", param, String.class);
    }
}

// B 服务
@RestController
public class BController {
    @PostMapping("/b/api")
    public String process(@RequestBody String param) {
        // 执行业务逻辑
        return "result";
    }
}
```

**问题：** 如果 B 执行时间长，A 会一直等待，可能超时。

---

### 方案二：异步消息队列

**A 发送消息到 MQ，B 异步处理，结果通过回调或轮询获取。**

```java
// A 服务 - 发送请求
public String callB(String param) {
    String requestId = UUID.randomUUID().toString();
    mq.send("b.request.queue", new Request(requestId, param));

    // 方式1：轮询获取结果
    for (int i = 0; i < 30; i++) {
        Result result = redis.get("result:" + requestId);
        if (result != null) {
            return result.getData();
        }
        Thread.sleep(1000);
    }

    return "timeout";
}

// B 服务 - 接收请求
@RabbitListener(queues = "b.request.queue")
public void processRequest(Request request) {
    // 执行业务逻辑
    Result result = doProcess(request.getParam());

    // 回传结果
    redis.setex("result:" + request.getRequestId(), 3600, result);
}
```

**优点：** 解耦、A 不阻塞
**缺点：** 延迟、需处理消息丢失

---

### 方案三：异步回调

**A 发送请求后立即返回，B 处理完成后回调 A。**

```java
// A 服务
@RestController
public class AController {
    @PostMapping("/a/submit")
    public String submit(@RequestBody Req req, @RequestParam callbackUrl) {
        req.setCallbackUrl(myCallbackUrl);
        mq.send("b.request.queue", req);
        return "已提交，任务ID：" + req.getTaskId();
    }

    @PostMapping("/a/callback")
    public void callback(@RequestBody Result result) {
        // 保存 B 返回的结果
        saveResult(result);
    }
}

// B 服务
@RestController
public class BController {
    @PostMapping("/b/process")
    public String process(@RequestBody Req req) {
        Result result = doProcess(req);
        // 回调 A
        restTemplate.postForObject(req.getCallbackUrl(), result, Void.class);
        return "处理完成";
    }
}
```

---

### 方案四：响应式编程

**使用 WebClient 进行非阻塞调用。**

```java
// A 服务
@Autowired
private WebClient webClient;

public Mono<String> callB(String param) {
    return webClient.post()
        .uri("http://B-service/b/api")
        .bodyValue(param)
        .retrieve()
        .bodyToMono(String.class)
        .timeout(Duration.ofSeconds(30));
}

// 调用
callB("param").subscribe(result -> {
    // 处理结果
});
```

---

### 方案对比

| 方案 | 实时性 | 复杂度 | 可靠性 | 适用场景 |
|------|--------|--------|--------|----------|
| 同步 HTTP | 高 | 低 | 低 | 短任务 |
| 消息队列 | 中 | 中 | 高 | 长任务 |
| 异步回调 | 中 | 中 | 高 | 异步处理 |
| 响应式 | 高 | 高 | 中 | 高并发 |

---

## 14. 两个大集合找重复元素

### 问题分析
两个集合很大，无法一次性加载到内存，需要使用算法和数据结构优化。

### 方案一：外部排序 + 归并

**思路：** 分批读取、排序、归并。

```java
public Set<Integer> findDuplicates(List<Integer> list1, List<Integer> list2) {
    Set<Integer> result = new HashSet<>();

    // 1. 对两个集合分别排序
    list1.sort(Integer::compareTo);
    list2.sort(Integer::compareTo);

    // 2. 归并找重复
    int i = 0, j = 0;
    while (i < list1.size() && j < list2.size()) {
        int a = list1.get(i);
        int b = list2.get(j);

        if (a.equals(b)) {
            result.add(a);
            i++;
            j++;
        } else if (a < b) {
            i++;
        } else {
            j++;
        }
    }

    return result;
}
```

---

### 方案二：布隆过滤器

**思路：** 用空间换时间，但可能有误判。

```java
public Set<String> findDuplicatesBloomFilter(List<String> list1, List<String> list2) {
    // 将较小的集合放入布隆过滤器
    BloomFilter<String> bf = BloomFilter.create(Funnels.stringFunnel(Charsets.UTF_8), list1.size());

    for (String item : list1) {
        bf.put(item);
    }

    Set<String> result = new HashSet<>();
    for (String item : list2) {
        if (bf.mightContain(item)) {
            result.add(item);
        }
    }

    return result;
}
```

---

### 方案三：分块处理

**思路：** 根据 hash 将数据分块，减少内存使用。

```java
public Set<Integer> findDuplicatesByChunk(List<Integer> list1, List<Integer> list2, int chunkSize) {
    Set<Integer> result = ConcurrentHashMap.newKeySet();

    // 将 list1 分块处理
    List<List<Integer>> chunks = Lists.partition(list1, chunkSize);

    for (List<Integer> chunk : chunks) {
        Set<Integer> chunkSet = new HashSet<>(chunk);

        for (Integer item : list2) {
            if (chunkSet.contains(item)) {
                result.add(item);
            }
        }
    }

    return result;
}
```

---

### 方案四：HashSet 分批加载

**思路：** 逐批读取一个集合到 HashSet，再遍历另一个集合。

```java
public Set<Integer> findDuplicatesByBatch(
        Iterator<Integer> iterator1,
        Iterator<Integer> iterator2,
        int batchSize) {

    Set<Integer> result = new HashSet<>();
    Set<Integer> batch = new HashSet<>();

    // 逐批从 iterator1 读取
    while (iterator1.hasNext()) {
        batch.add(iterator1.next());
        if (batch.size() >= batchSize) {
            // 用这批数据去 iterator2 中查找
            findInIterator(iterator2, batch, result);
            batch.clear();
        }
    }

    // 处理剩余数据
    if (!batch.isEmpty()) {
        findInIterator(iterator2, batch, result);
    }

    return result;
}

private void findInIterator(Iterator<Integer> iterator, Set<Integer> batch, Set<Integer> result) {
    while (iterator.hasNext()) {
        Integer item = iterator.next();
        if (batch.contains(item)) {
            result.add(item);
        }
    }
}
```

---

### 方案五：数据库处理

**思路：** 将数据导入数据库，用 SQL 查询。

```sql
-- 假设有两个表 list1 和 list2
SELECT DISTINCT a.id
FROM list1 a
INNER JOIN list2 b ON a.id = b.id;
```

---

### 方案对比

| 方案 | 时间复杂度 | 空间复杂度 | 准确性 | 适用场景 |
|------|------------|------------|--------|----------|
| 外部排序 | O(n log n) | O(1) | 100% | 有序数据 |
| 布隆过滤器 | O(n) | O(1) | 有误判 | 可容忍误判 |
| 分块处理 | O(n*m/chunkSize) | O(chunkSize) | 100% | 内存受限 |
| HashSet分批 | O(n) | O(chunkSize) | 100% | 流数据 |
| 数据库 | O(n) | O(1) | 100% | 已入库数据 |

---

## 15. 编程题：找到字符串中所有字母异位词

### 问题描述
给定字符串 s 和 p，找到 s 中所有是 p 异位词的起始索引。

**示例：**
```
输入: s = "cbaebabacd", p = "abc"
输出: [0, 6]

解释:
- 索引 0: "cba" 是 "abc" 的异位词
- 索引 6: "bac" 是 "abc" 的异位词
```

### 解法一：滑动窗口

```java
public List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();

    if (s == null || p == null || s.length() < p.length()) {
        return result;
    }

    int[] pCount = new int[26];  // p 的字符计数
    int[] sCount = new int[26];  // 滑动窗口的字符计数

    // 初始化 p 的计数
    for (char c : p.toCharArray()) {
        pCount[c - 'a']++;
    }

    int windowSize = p.length();

    // 遍历 s
    for (int i = 0; i <= s.length() - windowSize; i++) {
        // 更新窗口字符计数
        if (i == 0) {
            // 第一个窗口
            for (int j = 0; j < windowSize; j++) {
                sCount[s.charAt(j) - 'a']++;
            }
        } else {
            // 滑动窗口：移除左边字符，加入右边字符
            sCount[s.charAt(i - 1) - 'a']--;
            sCount[s.charAt(i + windowSize - 1) - 'a']++;
        }

        // 比较两个计数数组
        if (matches(pCount, sCount)) {
            result.add(i);
        }
    }

    return result;
}

private boolean matches(int[] arr1, int[] arr2) {
    for (int i = 0; i < 26; i++) {
        if (arr1[i] != arr2[i]) {
            return false;
        }
    }
    return true;
}
```

**复杂度：**
- 时间：O(n * 26) = O(n)
- 空间：O(1)

---

### 解法二：优化的滑动窗口（减少比较）

```java
public List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();

    if (s.length() < p.length()) {
        return result;
    }

    int[] count = new int[26];
    int required = p.length();  // 需要匹配的字符数
    int left = 0, right = 0;

    // 初始化 p 的字符计数
    for (char c : p.toCharArray()) {
        count[c - 'a']++;
    }

    while (right < s.length()) {
        char rightChar = s.charAt(right);
        if (count[rightChar - 'a'] > 0) {
            required--;
        }
        count[rightChar - 'a']--;
        right++;

        // 当需要的字符数变为0时，检查是否形成异位词
        if (required == 0) {
            if (right - left == p.length()) {
                result.add(left);
            }
        }

        // 窗口大小等于 p 长度时，左边界右移
        if (right - left == p.length()) {
            char leftChar = s.charAt(left);
            if (count[leftChar - 'a'] >= 0) {
                required++;
            }
            count[leftChar - 'a']++;
            left++;
        }
    }

    return result;
}
```

**简化版本：**

```java
public List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();
    int[] needs = new int[26];
    int[] window = new int[26];

    for (char c : p.toCharArray()) {
        needs[c - 'a']++;
    }

    int left = 0, right = 0, valid = 0;

    while (right < s.length()) {
        char c = s.charAt(right++);
        if (needs[c - 'a'] > 0) {
            window[c - 'a']++;
            if (window[c - 'a'] <= needs[c - 'a']) {
                valid++;
            }
        }

        while (right - left >= p.length()) {
            if (valid == p.length()) {
                result.add(left);
            }

            char d = s.charAt(left++);
            if (needs[d - 'a'] > 0) {
                if (window[d - 'a'] <= needs[d - 'a']) {
                    valid--;
                }
                window[d - 'a']--;
            }
        }
    }

    return result;
}
```

---

### 测试

```java
public static void main(String[] args) {
    Solution solution = new Solution();

    System.out.println(solution.findAnagrams("cbaebabacd", "abc"));
    // 输出: [0, 6]

    System.out.println(solution.findAnagrams("abab", "ab"));
    // 输出: [0, 1, 2]
}
```
