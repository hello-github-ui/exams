# 招商证券Java笔试题及答案

## 目录

- [一、Java 基础知识题（30 分）](#一java-基础知识题30-分)
  - [1. Java中的基本数据类型有哪些？](#1-java中的基本数据类型有哪些)
  - [2. 请解释Java中的多态性，并举例说明](#2-请解释java中的多态性并举例说明)
  - [3. List、Set和Map的区别是什么？](#3-listset和map的区别是什么)
  - [4. 请解释Java中的异常处理机制](#4-请解释java中的异常处理机制)
  - [5. 请简述Java中的垃圾回收机制](#5-请简述java中的垃圾回收机制)
  - [6. 请解释Java中的volatile关键字](#6-请解释java中的volatile关键字)
- [二、Java 编程题（30 分）](#二java-编程题30-分)
  - [1. 判断字符串是否是回文串](#1-实现一个方法判断一个字符串是否是回文串)
  - [2. 实现线程安全的单例模式](#2-实现一个单例模式要求线程安全且高效)
  - [3. 找出整数数组中的最大值和最小值](#3-实现一个方法找出一个整数数组中的最大值和最小值)
  - [4. 反转链表](#4-实现一个方法将一个链表反转)
  - [5. 实现线程安全的计数器](#5-实现一个线程安全的计数器类)
  - [6. 二叉树层序遍历](#6-实现一个方法将一个二叉树进行层序遍历)
- [三、数据结构和算法题（20 分）](#三数据结构和算法题20-分)
  - [1. 什么是二叉搜索树？](#1-请解释什么是二叉搜索树)
  - [2. 请解释快速排序](#2-请解释快速排序的算法思想)
  - [3. 什么是哈希表？](#3-请解释什么是哈希表)
  - [4. 什么是动态规划？](#4-请解释什么是动态规划并举例说明)

---

## 一、Java 基础知识题（30 分）

### 1. Java中的基本数据类型有哪些？

Java 中有 8 种基本数据类型：

| 数据类型 | 关键字 | 占用字节 | 取值范围 | 默认值 |
|----------|--------|----------|----------|--------|
| 字节型 | `byte` | 1 | -128 ~ 127 | 0 |
| 短整型 | `short` | 2 | -32768 ~ 32767 | 0 |
| 整型 | `int` | 4 | -2147483648 ~ 2147483647 | 0 |
| 长整型 | `long` | 8 | -9223372036854775808 ~ 9223372036854775807 | 0L |
| 浮点型 | `float` | 4 | 3.4e-38 ~ 3.4e+38 | 0.0f |
| 双精度浮点型 | `double` | 8 | 1.7e-308 ~ 1.7e+308 | 0.0d |
| 字符型 | `char` | 2 | 0 ~ 65535（Unicode） | '\u0000' |
| 布尔型 | `boolean` | 1 | true / false | false |

**注意：**
- String 是引用类型，不是基本数据类型
- 整数默认是 int 类型
- 浮点数默认是 double 类型

---

### 2. 请解释Java中的多态性，并举例说明

多态是面向对象编程的三大特性之一，指同一操作作用于不同对象可以产生不同的行为。

#### 多态的分类

**1. 编译时多态（静态多态）**
- 通过方法重载（Overload）实现
- 在编译时确定调用哪个方法

```java
public class Calculator {
    // 方法重载
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public String add(String a, String b) {
        return a + b;
    }
}

// 使用
Calculator calc = new Calculator();
calc.add(1, 2);        // 调用 int 版本
calc.add(1.0, 2.0);    // 调用 double 版本
calc.add("Hello", "World"); // 调用 String 版本
```

**2. 运行时多态（动态多态）**
- 通过方法重写（Override）和向上转型实现
- 在运行时确定调用哪个方法

```java
// 父类
public class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

// 子类
public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}

public class Cat extends Animal {
    @Override
    public void sound() {
        System.out.println("Cat meows");
    }
}

// 使用
Animal dog = new Dog();  // 向上转型
Animal cat = new Cat();  // 向上转型
dog.sound();  // 输出: Dog barks
cat.sound();  // 输出: Cat meows
```

#### 多态的必要条件
1. 继承关系
2. 子类重写父类方法
3. 父类引用指向子类对象

---

### 3. List、Set和Map的区别是什么？

| 特性 | List | Set | Map |
|------|------|-----|-----|
| **继承结构** | Collection 子接口 | Collection 子接口 | 独立接口 |
| **元素特性** | 有序、可重复 | 无序、不可重复 | Key无序、不可重复；Value可重复 |
| **访问方式** | 索引访问、按内容查找 | 按内容查找 | Key访问、按Value查找 |
| **null处理** | 可存储null | 可存储一个null（HashSet） | Key可为null，Value也可为null |
| **常用实现** | ArrayList, LinkedList, Vector | HashSet, TreeSet, LinkedHashSet | HashMap, TreeMap, LinkedHashMap |

#### List 常用实现类

**ArrayList**
- 基于动态数组
- 随机访问效率高 O(1)
- 插入删除效率低 O(n)

**LinkedList**
- 基于双向链表
- 插入删除效率高 O(1)
- 随机访问效率低 O(n)

**Vector**
- 线程安全的 ArrayList
- 已过时，不推荐使用

#### Set 常用实现类

**HashSet**
- 基于 HashMap
- 无序
- 查找、插入、删除 O(1)

**LinkedHashSet**
- 保持插入顺序
- 基于 LinkedHashMap

**TreeSet**
- 基于红黑树
- 有序
- 查找、插入、删除 O(log n)

#### Map 常用实现类

**HashMap**
- 键值对映射
- 允许 null 键和 null 值
- 非线程安全

**LinkedHashMap**
- 保持插入顺序

**TreeMap**
- 基于红黑树
- Key 有序

**Hashtable**
- 线程安全的 HashMap
- 已过时，不推荐使用

```java
// 示例
List<String> list = new ArrayList<>();
list.add("A");
list.add("B");
list.add("A");  // 允许重复

Set<String> set = new HashSet<>();
set.add("A");
set.add("B");
set.add("A");  // 不允许重复，只保留一个 "A"

Map<String, Integer> map = new HashMap<>();
map.put("A", 1);
map.put("B", 2);
map.put("A", 3);  // 替换 A 的值
```

---

### 4. 请解释Java中的异常处理机制

#### 异常体系结构

```
Throwable
├── Error（错误）
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── ...
└── Exception（异常）
    ├── RuntimeException（运行时异常）
    │   ├── NullPointerException
    │   ├── IndexOutOfBoundsException
    │   ├── ClassCastException
    │   └── ...
    └── IOException（受检异常）
        ├── FileNotFoundException
        ├── SQLException
        └── ...
```

#### Checked Exception vs Unchecked Exception

**Checked Exception（受检异常）**
- 编译器强制要求处理的异常
- 继承自 `Exception` 但不是 `RuntimeException`
- 如 `IOException`、`SQLException`
- 必须用 try-catch 捕获或 throws 声明

**Unchecked Exception（非受检异常）**
- 编译器不强制要求处理的异常
- 继承自 `RuntimeException`
- 如 `NullPointerException`、`ArrayIndexOutOfBoundsException`
- 可以选择处理，也可以不处理

#### 异常处理关键字

```java
try {
    // 可能抛出异常的代码
    int result = 10 / 0;
} catch (ArithmeticException e) {
    // 捕获特定异常
    System.out.println("除数不能为零");
} catch (Exception e) {
    // 捕获所有异常
    e.printStackTrace();
} finally {
    // 无论是否异常都会执行
    // 通常用于释放资源
    System.out.println("finally 块执行");
}
```

#### 自定义异常

```java
public class BusinessException extends RuntimeException {
    private int errorCode;

    public BusinessException(String message) {
        super(message);
    }

    public BusinessException(int errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public int getErrorCode() {
        return errorCode;
    }
}
```

#### 异常处理原则
1. 不要捕获 Throwable（除非特殊要求）
2. 不要捕获后不做任何处理
3. 尽量捕获具体异常类型
4. finally 块中不要写 return
5. 不要用异常处理代替业务逻辑判断

---

### 5. 请简述Java中的垃圾回收机制

#### 垃圾回收算法

**1. 标记-清除（Mark-Sweep）**
- 标记所有存活对象
- 清除所有未标记对象
- 缺点：产生内存碎片

**2. 复制（Copying）**
- 将内存分为两块
- 每次只使用一块
- 存活对象复制到另一块后清空
- 缺点：内存利用率低

**3. 标记-整理（Mark-Compact）**
- 标记存活对象
- 整理碎片，将存活对象移到一端
- 缺点：效率较低

**4. 分代收集（Generational Collection）**
- 根据对象存活周期分代
- 分为 Young Generation、Old Generation、Permanent Generation

#### Java 内存分代

| 分代 | 对象特点 | 回收算法 |
|------|----------|----------|
| **Eden 区** | 新创建的对象 | Minor GC |
| **Survivor 区** | 存活一段时间的对象 | Minor GC |
| **Old 区** | 长期存活的对象 | Major/Full GC |
| **Metaspace** | 类元数据 | - |

#### 垃圾收集器

**Young 区收集器**
- Serial：单线程，用于 Client 模式
- ParNew：Serial 的多线程版本
- Parallel Scavenge：关注吞吐量

**Old 区收集器**
- Serial Old：Serial 的老年代版本
- Parallel Old：Parallel Scavenge 的老年代版本
- CMS：并发标记清除，追求最短停顿时间
- G1：大内存分 Region，追求停顿时间可预测

#### 手动触发垃圾回收

```java
// 不推荐手动触发，Java 虚拟机会自行决定
System.gc();  // 建议执行 GC，不保证立即执行
Runtime.getRuntime().gc();
```

#### 内存分配原则
1. 对象优先在 Eden 区分配
2. 大对象直接进入老年代
3. 长期存活对象进入老年代
4. 动态年龄判断

---

### 6. 请解释Java中的volatile关键字

#### volatile 的作用

**1. 保证可见性**
- 一个线程对 volatile 变量的修改，对其他线程立即可见
- 写操作会立即刷新到主内存
- 读操作直接从主内存读取

```java
public class VolatileDemo {
    volatile boolean flag = false;

    // 线程 A
    public void writer() {
        flag = true;  // 写入主内存
    }

    // 线程 B
    public void reader() {
        if (flag) {  // 从主内存读取
            // 一定能读到最新值
        }
    }
}
```

**2. 禁止指令重排序**
- 防止编译器/CPU 对代码进行重排序
- 保证程序执行顺序按照代码编写顺序

```java
// volatile 防止指令重排序
volatile boolean init = false;

// 线程 A
public void init() {
    obj = new Object();  // 步骤 1
    init = true;         // 步骤 2（volatile 保证之前的操作已完成）
}

// 线程 B
public void use() {
    if (init) {          // 步骤 3
        obj.doSomething(); // 步骤 4
    }
}
```

#### volatile 与 synchronized 的区别

| 特性 | volatile | synchronized |
|------|----------|--------------|
| 原子性 | 不保证 | 保证 |
| 可见性 | 保证 | 保证 |
| 有序性 | 禁止重排序 | 保证 |
| 阻塞 | 不支持 | 支持 |
| 性能 | 高 | 低 |

#### volatile 的使用场景

**1. 状态标志**
```java
volatile boolean shutdown = false;
public void shutdown() {
    shutdown = true;
}
```

**2. 双重检查锁定（Double-Checked Locking）**
```java
public class Singleton {
    private volatile static Singleton instance;

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

**注意：**
- volatile 不能保证原子性，如 `i++` 操作
- 对于复合操作，需要使用 synchronized 或原子类

---

## 二、Java 编程题（30 分）

### 1. 实现一个方法判断一个字符串是否是回文串

```java
/**
 * 判断字符串是否是回文串
 * 回文串：正读和反读都相同的字符串
 *
 * @param s 待判断的字符串
 * @return 是否是回文串
 */
public static boolean isPalindrome(String s) {
    if (s == null || s.isEmpty()) {
        return true;
    }

    // 双指针法
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        // 跳过非字母数字字符（如果需要忽略大小写和特殊字符）
        while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
            left++;
        }
        while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
            right--;
        }

        // 忽略大小写比较
        if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

// 测试
public static void main(String[] args) {
    System.out.println(isPalindrome("A man, a plan, a canal: Panama"));  // true
    System.out.println(isPalindrome("race a car"));  // false
    System.out.println(isPalindrome(""));  // true
}
```

**其他解法：**

```java
// 解法二：反转字符串比较
public static boolean isPalindrome2(String s) {
    String reversed = new StringBuilder(s).reverse().toString();
    return s.equals(reversed);
}

// 解法三：栈
public static boolean isPalindrome3(String s) {
    Stack<Character> stack = new Stack<>();
    for (char c : s.toCharArray()) {
        stack.push(c);
    }
    StringBuilder sb = new StringBuilder();
    while (!stack.isEmpty()) {
        sb.append(stack.pop());
    }
    return s.equals(sb.toString());
}
```

---

### 2. 实现一个单例模式要求线程安全且高效

```java
/**
 * 双重检查锁定的单例模式
 * 线程安全且高效
 */
public class Singleton {
    // volatile 防止指令重排序
    private static volatile Singleton instance;

    // 私有构造函数
    private Singleton() {
        // 防止反射创建多个实例
        if (instance != null) {
            throw new IllegalStateException("Instance already created");
        }
    }

    public static Singleton getInstance() {
        // 第一次检查，避免不必要的同步
        if (instance == null) {
            synchronized (Singleton.class) {
                // 第二次检查，确保在多线程环境下只创建一个实例
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }

    // 防止反序列化创建多个实例
    protected Object readResolve() {
        return getInstance();
    }
}
```

**其他实现方式：**

```java
/**
 * 饿汉式（静态常量）
 * 类加载时就初始化，没有线程安全问题
 */
public class SingletonHungry {
    private static final SingletonHungry INSTANCE = new SingletonHungry();

    private SingletonHungry() {}

    public static SingletonHungry getInstance() {
        return INSTANCE;
    }
}

/**
 * 饿汉式（静态代码块）
 */
public class SingletonHungry2 {
    private static SingletonHungry2 INSTANCE;

    static {
        INSTANCE = new SingletonHungry2();
    }

    private SingletonHungry2() {}

    public static SingletonHungry2 getInstance() {
        return INSTANCE;
    }
}

/**
 * 静态内部类（推荐）
 * 既延迟加载，又保证线程安全
 */
public class SingletonInner {
    private SingletonInner() {}

    private static class Holder {
        private static final SingletonInner INSTANCE = new SingletonInner();
    }

    public static SingletonInner getInstance() {
        return Holder.INSTANCE;
    }
}

/**
 * 枚举单例（最安全）
 * 防止反射和反序列化攻击
 */
public enum SingletonEnum {
    INSTANCE;

    public void doSomething() {
        // 业务方法
    }
}
```

---

### 3. 实现一个方法找出一个整数数组中的最大值和最小值

```java
/**
 * 找出整数数组中的最大值和最小值
 */
public static int[] findMaxAndMin(int[] arr) {
    if (arr == null || arr.length == 0) {
        throw new IllegalArgumentException("数组不能为空");
    }

    int max = arr[0];
    int min = arr[0];

    for (int i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }

    return new int[]{min, max};
}

// 使用数组返回
public static int[] findMaxAndMin2(int[] arr) {
    int[] result = new int[2];
    result[0] = Integer.MAX_VALUE;  // min
    result[1] = Integer.MIN_VALUE; // max

    for (int num : arr) {
        result[0] = Math.min(result[0], num);
        result[1] = Math.max(result[1], num);
    }
    return result;
}

// 使用自定义类返回
public static class MinMax {
    private int min;
    private int max;

    public MinMax(int min, int max) {
        this.min = min;
        this.max = max;
    }

    public int getMin() { return min; }
    public int getMax() { return max; }

    @Override
    public String toString() {
        return "MinMax{min=" + min + ", max=" + max + "}";
    }
}

public static MinMax findMaxAndMin3(int[] arr) {
    if (arr == null || arr.length == 0) {
        throw new IllegalArgumentException("数组不能为空");
    }

    int min = arr[0];
    int max = arr[0];

    for (int i = 1; i < arr.length; i++) {
        min = Math.min(min, arr[i]);
        max = Math.max(max, arr[i]);
    }

    return new MinMax(min, max);
}

// 测试
public static void main(String[] args) {
    int[] arr = {3, 1, 4, 1, 5, 9, 2, 6};
    int[] result = findMaxAndMin(arr);
    System.out.println("最小值: " + result[0] + ", 最大值: " + result[1]);

    MinMax mm = findMaxAndMin3(arr);
    System.out.println(mm);  // MinMax{min=1, max=9}
}
```

---

### 4. 实现一个方法将一个链表反转

```java
/**
 * 单链表节点
 */
class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

/**
 * 反转链表
 */
public class LinkedListReverse {

    /**
     * 迭代法反转链表
     * 时间复杂度：O(n)
     * 空间复杂度：O(1)
     */
    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode next = curr.next;  // 保存下一个节点
            curr.next = prev;           // 反转指针
            prev = curr;                // prev 前进
            curr = next;                // curr 前进
        }

        return prev;  // 新的头节点
    }

    /**
     * 递归法反转链表
     * 时间复杂度：O(n)
     * 空间复杂度：O(n)（调用栈）
     */
    public static ListNode reverseListRecursive(ListNode head) {
        // 基本情况
        if (head == null || head.next == null) {
            return head;
        }

        // 递归反转后续节点
        ListNode newHead = reverseListRecursive(head.next);

        // 将当前节点的下一个节点的 next 指向当前节点
        head.next.next = head;
        head.next = null;

        return newHead;
    }

    /**
     * 打印链表
     */
    public static void printList(ListNode head) {
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val);
            if (curr.next != null) {
                System.out.print(" -> ");
            }
            curr = curr.next;
        }
        System.out.println();
    }

    // 测试
    public static void main(String[] args) {
        // 创建链表: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1,
                      new ListNode(2,
                      new ListNode(3,
                      new ListNode(4,
                      new ListNode(5)))));

        System.out.println("原链表:");
        printList(head);

        System.out.println("迭代反转后:");
        ListNode reversed = reverseList(head);
        printList(reversed);

        // 创建新链表测试递归
        ListNode head2 = new ListNode(1,
                       new ListNode(2,
                       new ListNode(3)));
        System.out.println("原链表:");
        printList(head2);

        System.out.println("递归反转后:");
        ListNode reversed2 = reverseListRecursive(head2);
        printList(reversed2);
    }
}
```

**图解迭代过程：**
```
初始: 1 -> 2 -> 3 -> 4 -> 5 -> null
      prev=null, curr=1

第1步: null <- 1    2 -> 3 -> 4 -> 5 -> null
      prev=1, curr=2

第2步: null <- 1 <- 2    3 -> 4 -> 5 -> null
      prev=2, curr=3

...

最终: null <- 1 <- 2 <- 3 <- 4 <- 5
                              prev=5 (新的头节点)
```

---

### 5. 实现一个线程安全的计数器类

```java
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.ReentrantLock;

/**
 * 线程安全的计数器类
 * 支持增加、减少和获取当前值
 */
public class ThreadSafeCounter {

    // 方案一：使用 synchronized
    private int countSynchronized = 0;

    public synchronized void incrementSync() {
        countSynchronized++;
    }

    public synchronized void decrementSync() {
        countSynchronized--;
    }

    public synchronized int getSync() {
        return countSynchronized;
    }

    // 方案二：使用 ReentrantLock
    private int countLock = 0;
    private final ReentrantLock lock = new ReentrantLock();

    public void incrementLock() {
        lock.lock();
        try {
            countLock++;
        } finally {
            lock.unlock();
        }
    }

    public void decrementLock() {
        lock.lock();
        try {
            countLock--;
        } finally {
            lock.unlock();
        }
    }

    public int getLock() {
        lock.lock();
        try {
            return countLock;
        } finally {
            lock.unlock();
        }
    }

    // 方案三：使用 AtomicInteger（推荐）
    private AtomicInteger atomicCount = new AtomicInteger(0);

    public void increment() {
        atomicCount.incrementAndGet();
    }

    public void decrement() {
        atomicCount.decrementAndGet();
    }

    public int get() {
        return atomicCount.get();
    }

    // 方案四：使用 LongAdder（高并发场景推荐）
    private LongAdder longAdderCount = new LongAdder();

    public void incrementAdder() {
        longAdderCount.increment();
    }

    public void decrementAdder() {
        longAdderCount.decrement();
    }

    public long getAdder() {
        return longAdderCount.sum();
    }

    // 测试
    public static void main(String[] args) throws InterruptedException {
        ThreadSafeCounter counter = new ThreadSafeCounter();

        // 测试 AtomicInteger 方案
        int threadCount = 100;
        Thread[] threads = new Thread[threadCount];

        // 启动100个线程，每个线程增加1000次
        for (int i = 0; i < threadCount; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 1000; j++) {
                    counter.increment();
                }
            });
            threads[i].start();
        }

        // 等待所有线程完成
        for (Thread t : threads) {
            t.join();
        }

        System.out.println("最终计数: " + counter.get());
        System.out.println("期望值: " + (threadCount * 1000));
        System.out.println("测试" + (counter.get() == threadCount * 1000 ? "通过" : "失败"));
    }
}
```

**各方案对比：**

| 方案 | 适用场景 | 性能 |
|------|----------|------|
| synchronized | 低并发 | 一般 |
| ReentrantLock | 需要公平锁/可打断锁 | 较好 |
| AtomicInteger | 低到中并发 | 较好 |
| LongAdder | 高并发 | 最好 |

---

### 6. 实现一个方法将一个二叉树进行层序遍历

```java
import java.util.*;

/**
 * 二叉树节点
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/**
 * 二叉树层序遍历
 */
public class BinaryTreeLevelOrder {

    /**
     * 层序遍历（广度优先搜索 BFS）
     * 使用队列实现
     *
     * @param root 二叉树根节点
     * @return 按层返回的结果列表
     */
    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();  // 当前层的节点数
            List<Integer> currentLevel = new ArrayList<>();

            // 处理当前层的所有节点
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);

                // 将子节点加入队列
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            result.add(currentLevel);
        }

        return result;
    }

    /**
     * 层序遍历（逐行打印）
     */
    public static void levelOrderPrint(TreeNode root) {
        if (root == null) {
            return;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int level = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            System.out.print("第 " + (level + 1) + " 层: ");

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                System.out.print(node.val + " ");

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            System.out.println();
            level++;
        }
    }

    /**
     * 层序遍历（之字形打印，即第一行从左到右，第二行从右到左）
     */
    public static List<List<Integer>> levelOrderZigzag(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean leftToRight = true;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();

                if (leftToRight) {
                    currentLevel.add(node.val);
                } else {
                    currentLevel.add(0, node.val);  // 头部插入，实现逆序
                }

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            result.add(currentLevel);
            leftToRight = !leftToRight;
        }

        return result;
    }

    // 测试
    public static void main(String[] args) {
        /*
         * 构建二叉树:
         *           1
         *         /   \
         *        2     3
         *       / \     \
         *      4   5     6
         */
        TreeNode root = new TreeNode(1,
            new TreeNode(2,
                new TreeNode(4),
                new TreeNode(5)),
            new TreeNode(3,
                null,
                new TreeNode(6)));

        System.out.println("层序遍历:");
        List<List<Integer>> result = levelOrder(root);
        for (int i = 0; i < result.size(); i++) {
            System.out.println("第 " + (i + 1) + " 层: " + result.get(i));
        }

        System.out.println("\n逐行打印:");
        levelOrderPrint(root);

        System.out.println("\n之字形打印:");
        List<List<Integer>> zigzag = levelOrderZigzag(root);
        for (int i = 0; i < zigzag.size(); i++) {
            System.out.println("第 " + (i + 1) + " 层: " + zigzag.get(i));
        }
    }
}
```

**输出结果：**
```
层序遍历:
第 1 层: [1]
第 2 层: [2, 3]
第 3 层: [4, 5, 6]

逐行打印:
第 1 层: 1 
第 2 层: 2 3 
第 3 层: 4 5 6 

之字形打印:
第 1 层: [1]
第 2 层: [3, 2]
第 3 层: [6, 5, 4]
```

---

## 三、数据结构和算法题（20 分）

### 1. 请解释什么是二叉搜索树

#### 定义

二叉搜索树（Binary Search Tree，BST）是一种特殊的二叉树，具有以下性质：

1. **左子树上所有节点的值都小于根节点的值**
2. **右子树上所有节点的值都大于根节点的值**
3. **左右子树也分别是二叉搜索树**

#### 示意图

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

#### 时间复杂度

| 操作 | 平均时间复杂度 | 最坏时间复杂度 |
|------|---------------|---------------|
| 查找 | O(log n) | O(n) |
| 插入 | O(log n) | O(n) |
| 删除 | O(log n) | O(n) |
| 前驱/后继 | O(log n) | O(n) |

**最坏情况：** 当BST退化成链表时（插入顺序有序），时间复杂度变为 O(n)。

#### 查找操作
```java
public TreeNode search(TreeNode root, int target) {
    if (root == null || root.val == target) {
        return root;
    }

    if (target < root.val) {
        return search(root.left, target);
    } else {
        return search(root.right, target);
    }
}
```

#### 插入操作
```java
public TreeNode insert(TreeNode root, int val) {
    if (root == null) {
        return new TreeNode(val);
    }

    if (val < root.val) {
        root.left = insert(root.left, val);
    } else if (val > root.val) {
        root.right = insert(root.right, val);
    }
    // 如果值相等，默认不插入（可自定义处理）

    return root;
}
```

#### 删除操作
```java
public TreeNode delete(TreeNode root, int val) {
    if (root == null) {
        return null;
    }

    if (val < root.val) {
        root.left = delete(root.left, val);
    } else if (val > root.val) {
        root.right = delete(root.right, val);
    } else {
        // 找到要删除的节点
        if (root.left == null) return root.right;
        if (root.right == null) return root.left;

        // 左右子树都存在，找后继节点（最小节点）
        TreeNode successor = findMin(root.right);
        root.val = successor.val;
        root.right = delete(root.right, successor.val);
    }
    return root;
}

private TreeNode findMin(TreeNode node) {
    while (node.left != null) {
        node = node.left;
    }
    return node;
}
```

---

### 2. 请解释快速排序的算法思想

#### 算法思想

快速排序是一种分治算法，通过选择一个**基准元素（pivot）**，将数组分为两部分：
- 左半部分所有元素都小于等于 pivot
- 右半部分所有元素都大于等于 pivot

然后递归地对左右两部分进行排序。

#### 图解过程

```
原始数组: [6, 3, 8, 2, 9, 1]

选择 pivot = 6（最后一个元素）

第一轮分区:
[3, 2, 1]  [6]  [8, 9]
   <6         >6

继续递归排序:
[1] [2] [3]  [6]  [8] [9]

最终结果: [1, 2, 3, 6, 8, 9]
```

#### 代码实现

```java
public class QuickSort {

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // 分区，返回 pivot 的最终位置
            int pivotIndex = partition(arr, low, high);

            // 递归排序左半部分
            quickSort(arr, low, pivotIndex - 1);

            // 递归排序右半部分
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        // 选择最后一个元素作为 pivot
        int pivot = arr[high];

        // i 用于跟踪小于 pivot 元素的边界
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                // 交换 arr[i] 和 arr[j]
                swap(arr, i, j);
            }
        }

        // 将 pivot 放到正确位置
        swap(arr, i + 1, high);
        return i + 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {6, 3, 8, 2, 9, 1, 5, 7};
        System.out.println("排序前: " + Arrays.toString(arr));

        quickSort(arr, 0, arr.length - 1);

        System.out.println("排序后: " + Arrays.toString(arr));
    }
}
```

#### 时间复杂度分析

| 情况 | 时间复杂度 | 说明 |
|------|------------|------|
| **最好** | O(n log n) | pivot 刚好将数组平分 |
| **最坏** | O(n²) | pivot 是最大或最小值（数组有序） |
| **平均** | O(n log n) | 随机情况下接近最好情况 |

#### 空间复杂度
- **最好/平均：** O(log n)（递归栈深度）
- **最坏：** O(n)（递归栈深度）

#### 优化策略

1. **随机选择 pivot**：避免最坏情况
2. **三数取中**：选择左中右三个数的中位数作为 pivot
3. **小数组使用插入排序**：数据量小时，插入排序更快
4. **尾递归优化**：减少递归栈深度

```java
// 优化：随机选择 pivot
private static int partitionOptimized(int[] arr, int low, int high) {
    // 随机选择 pivot 并与最后一个元素交换
    Random random = new Random();
    int randomIndex = low + random.nextInt(high - low + 1);
    swap(arr, randomIndex, high);

    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, high);
    return i + 1;
}
```

---

### 3. 请解释什么是哈希表

#### 定义

哈希表（Hash Table）是一种根据关键码（Key）直接访问值（Value）的数据结构。它通过**哈希函数**将键映射到表中的位置（称为槽或桶）来访问记录。

#### 工作原理

```
键 (Key)  →  哈希函数  →  槽位 (Index)  →  值 (Value)
   "name"    →    hash()   →      2        →   "Alice"
   "age"     →    hash()   →      5        →   "25"
```

#### 哈希函数

**常见哈希函数：**
1. **除法取余法**：`h(key) = key % m`
2. **乘法散列法**：`h(key) = floor(m * (key * A % 1))`
3. **直接寻址法**：`h(key) = key`
4. **数字分析法**：选取键的一部分进行运算

**好的哈希函数特点：**
- 计算速度快
- 均匀分布，减少冲突
- 确定性强（相同输入产生相同输出）

#### 哈希冲突

**定义：** 两个不同的键经过哈希函数计算后得到相同的索引。

**解决方法：**

**1. 开放寻址法（Open Addressing）**
- 线性探测：`h(key, i) = (hash(key) + i) % m`
- 平方探测：`h(key, i) = (hash(key) + i²) % m`
- 双重哈希：`h(key, i) = (hash1(key) + i * hash2(key)) % m`

```
线性探测示例：
hash("name") = 2 (已被占用)
尝试 3, 4, 5... 直到找到空槽
```

**2. 链地址法（Separate Chaining）**
- 每个槽位维护一个链表
- 冲突的元素插入对应槽位的链表中

```
Index 0: → ["city"] → ["country"]
Index 1: → ["age"]
Index 2: → ["name"]
...
```

**Java 中的实现：**
- `HashMap` 使用链地址法 + 红黑树（当链表长度超过8时转换为红黑树）

#### 时间复杂度

| 操作 | 平均时间复杂度 | 最坏时间复杂度 |
|------|---------------|---------------|
| 查找 | O(1) | O(n) |
| 插入 | O(1) | O(n) |
| 删除 | O(1) | O(n) |

**最坏情况：** 所有键都哈希到同一个槽位，退化成链表。

#### Java 中的哈希表实现

```java
// HashMap 核心原理
public class HashMapDemo {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();

        // 插入
        map.put("apple", 1);
        map.put("banana", 2);

        // 查找
        Integer value = map.get("apple");

        // HashMap 的关键参数
        // - initial capacity：初始容量（默认16）
        // - load factor：负载因子（默认0.75）
        // - threshold = capacity * load factor
    }
}
```

---

### 4. 请解释什么是动态规划，并举例说明

#### 定义

动态规划（Dynamic Programming，DP）是一种将复杂问题分解为更小子问题来求解的算法思想。

**核心思想：**
1. **最优子结构**：问题的最优解由其子问题的最优解构成
2. **重叠子问题**：子问题会被重复计算

#### 动态规划 vs 分治法

| 特性 | 动态规划 | 分治法 |
|------|----------|--------|
| 子问题关系 | 子问题可能重叠 | 子问题相互独立 |
| 求解顺序 | 自底向上（利用之前结果） | 通常自顶向下 |
| 存储 | 存储子问题结果 | 不存储 |

#### 动态规划解题步骤

1. **确定 dp 数组及下标含义**
2. **确定递推公式**
3. **dp 数组初始化**
4. **确定遍历顺序**
5. **举例推导 dp 数组**

#### 经典例题

**例题1：斐波那契数列**

```java
// 普通递归（指数级时间）
public int fibRecursive(int n) {
    if (n <= 1) return n;
    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// 动态规划（O(n)时间）
public int fibDP(int n) {
    if (n <= 1) return n;

    int[] dp = new int[n + 1];
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}

// 空间优化
public int fibOptimized(int n) {
    if (n <= 1) return n;

    int prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        int sum = prev + curr;
        prev = curr;
        curr = sum;
    }

    return curr;
}
```

**例题2：爬楼梯**

> 题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。有多少种不同的方法可以爬到楼顶？

```java
public int climbStairs(int n) {
    if (n <= 2) return n;

    int[] dp = new int[n + 1];
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}
```

**例题3：背包问题**

> 题目：给定 n 种物品，每种物品有重量和价值，求解将哪些物品装入背包可使价值总和最大。

```java
public int knapsack(int[] weights, int[] values, int capacity) {
    int n = weights.length;
    int[][] dp = new int[n + 1][capacity + 1];

    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                // 选择：取或不取，取较大值
                dp[i][w] = Math.max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}
```

**例题4：最长公共子序列**

```java
public int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length();
    int n = text2.length();

    int[][] dp = new int[m + 1][n + 1];

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[m][n];
}
```

#### 一维 DP 与二维 DP

**一维 DP（只依赖前一个状态）：**
- 斐波那契数列
- 爬楼梯
- 连续子数组最大和

**二维 DP（依赖两个前状态）：**
- 背包问题
- 最长公共子序列
- 编辑距离
