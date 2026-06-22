---
title: 10、linux命令(14题)
source: 各大公司面试题库/面试题库（368题）/10、linux命令(14题).pdf
pages: 3
converted_at: 2026-06-22 22:29:13
---

# 10、linux命令(14题)

1. 使⽤用两种命令创建⼀一个⽂文件？
a. touch a.txt
b. vi a.txt
c. mkdir abc
d. cat > a.txt 建⽴立⼀一⽂文件，然后把接下来的键盘输⼊入写⼊入⽂文件，直到按Ctrl+D为⽌止.
2. 硬链接和软连接的区别？
a. 硬链接：
1、⽂文件有相同的 inode 及 data block；
2、只能对已存在的⽂文件进⾏行行创建；
3、不不能交叉⽂文件系统进⾏行行硬链接的创建；
4、不不能对⽬目录进⾏行行创建，只可对⽂文件创建；
5、删除⼀一个硬链接⽂文件并不不影响其他有相同 inode 号的⽂文件。
b. 软链接：
1、软链接有⾃自⼰己的⽂文件属性及权限等；
2、可对不不存在的⽂文件或⽬目录创建软链接；
3、软链接可交叉⽂文件系统；
4、软链接可对⽂文件或⽬目录创建；
5、创建软链接时，链接计数 i_nlink 不不会增加；
6、删除软链接并不不影响被指向的⽂文件，但若被指向的原⽂文件被删除，则相关软连接被称为死链接（即 dangling 
link，若被指向路路径⽂文件被重新创建，死链接可恢复为正常的软链接）。
3. linux常⽤用命令有哪些？
1
查找关闭端⼝口进程 netstat -nlp | grep :3306 kill pid
2
删除⽂文件 rm -rf
3
查找⽇日志 cat xx.log | grep 'xxx' | more
4
解压tar.gz tar -xzvf file.tar.gz
5
创建⽂文件 touch filename cat > filename
6
修改⽂文件 vi
4. 怎么查看⼀一个java线程的资源耗⽤用？
linux下，所有的java内部线程，其实都对应了⼀个进程id，也就是说，linux上的jvm将java程序中的线程映射为操作系统进
程。
1
1、jps -lvm或者ps -ef | grep java查看当前机器器上运⾏行行的Java应⽤用进程
2
2、top -Hp pid可以查看Java所有线程的资源耗⽤用
3
4、printf "%x\n" pid等到线程ID的16进制
4
5、jstack Java应⽤用进程ID | grep 线程ID的16进制
5. Load过⾼高的可能性有哪些？
cpu load的飙升，⼀一⽅方⾯面可能和full gc的次数增⼤大有关，⼀一⽅方⾯面可能和死循环有关系
6. /etc/hosts⽂文件什什么作⽤用？
在当前主机给ip设置别名，通过该别名可以访问到该ip地址，通过别名、ip访问的效果是⼀一样的
7. 如何快速的将⼀一个⽂文本中的"abc"转换成"xyz"？
1
vi filename编辑⽂文本，按Esc键，输⼊入:%s/abc/xyz/g
8. 如何在log⽂文件中搜索找出error的⽇日志？
1
cat xx.log | grep 'error'
9. 发现硬盘空间不不够，如何快速找出占⽤用空间最⼤大的⽂文件?
1
find . -type f -size +100M | xargs du -h | sort -nr
10. Java服务端问题排查（OOM，CPU⾼高，Load⾼高，类冲突）？
a. https://blog.csdn.net/and1kaney/article/details/51214219
b. 业务⽇日志相关：
i. less或者more

---

ii. grep
iii. tail -f filename
ps:切忌vim直接打开⼤⽇志⽂件，因为会直接加载到内存的
c. 数据库相关：
i. 登录线上库，show processlist查看数据库连接情况
d. jvm相关：
i. jps显示java进程
ii. jinfo实时查看和调整jvm参数
iii. jstat监控jvm各种运⾏行行状态信息；
iv. jstack(Stack Trace for Java)命令⽤用于⽣生成JVM进程当前时刻的线程的调⽤用堆栈，可以⽤用来定位线程间死锁、
锁等待、等待外部资源等
v. jmap(Memory Map for Java) 命令⽤用于⽣生成堆转储快照dump⽂文件，除了了这种⽅方式还可以通过-
XX:HeapDumpOnOutOfMemoryError参数，可以在虚拟机发⽣生OOM的时候⾃自动⽣生成堆的dump⽂文件，或者kill -3 
命令发出进程退出信号"吓唬"⼀一下虚拟机，也能拿到dump⽂文件。
e. oom问题：
i. 配置了了-XX:+HeapDumpOnOutOfMemoryError, 在发⽣生OOM的时候会在-XX:HeapDumpPath⽣生成堆的dump⽂文
件，结合MAT，可以对dump⽂文件进⾏行行分析，查找出发⽣生OOM的原因。
ii. 另外⼿手动dump堆快照，可以使⽤用命令jmap -dump:format=b,file=file_name pid 或者kill -3 pid
f. 死锁：
i. jps -v
ii. jstack -l pid
g. 线程block、线程数暴暴涨：
i. jstack -l pid |wc -l
ii. jstack -l pid |grep "BLOCKED"|wc -l
iii. jstack -l pid |grep "Waiting on condition"|wc -l
线程block问题⼀般是等待io、等待⽹络、等待监视器锁等造成，可能会导致请求超时、造成造成线程数暴涨导致系统502
等。
h. 服务器器问题：
i. cpu：top
ii. 内存：
1. free -m -c10 -s1：
a. -m：以MB为单位显示，其他的有-k -g -b
b. -s: 间隔多少秒持续观察内存使⽤用状况
c. -c:观察多少次
2. vmstat 1 10：1表示每隔1s输出⼀一次,10 表示输出10次
a. r: 运⾏行行队列列中进程数量量，这个值也可以判断是否需要增加CPU。（⻓长期⼤大于1）
b. b: 等待IO的进程数量量。
i. io：
i. iostat -m 1 10：
1. -m：某些使⽤用block为单位的列列强制使⽤用MB为单位
2. 1 10：数据显示每隔1秒刷新⼀一次，共显示10次

![10、linux命令(14题) 第2页插图](../assets/images/10、linux命令(14题)_p2_1_dfa70bb0.png)

![10、linux命令(14题) 第2页插图](../assets/images/10、linux命令(14题)_p2_2_67ee4896.png)

---

j. ⽹网络：
i. netstat -antp：
1. -a (all)显示所有选项，默认不不显示LISTEN相关
2. -t (tcp)仅显示tcp相关选项
3. -u (udp)仅显示udp相关选项
4. -n 拒绝显示别名，能显示数字的全部转化成数字。
5. -l 仅列列出有在 Listen (监听) 的服服务状态
6. -p 显示建⽴立相关链接的程序名
11. Java常⽤用问题排查⼯工具及⽤用法（top,iostat,vmstat,sar,tcpdump,jvisualvm,jmap,jconsole）
https://blog.csdn.net/xad707348125/article/details/51985854
12. Thread dump⽂文件如何分析（Runnable，锁，代码栈，操作系统线程id关联）
a. Thread Dump 能诊断的问题
i. 查找内存泄露露，常⻅见的是程序⾥里里load⼤大量量的数据到缓存；
ii. 发现死锁线程；
b. 如何抓取Thread Dump信息：
i. ⼀一般当服务器器挂起,崩溃或者性能底下时,就需要抓取服务器器的线程堆栈(Thread Dump)⽤用于后续的分析. 在实际
运⾏行行中，往往⼀一次 dump的信息，还不不⾜足以确认问题。为了了反映线程状态的动态变化，需要接连多次做
threaddump，每次间隔10-20s，建议⾄至少产⽣生三次 dump信息，如果每次 dump都指向同⼀一个问题，我们才确
定问题的典型性。
ii. linux命令获取：
1
ps –ef  | grep java
2
kill -3 <pid>
iii. jdk⾃自带⼯工具获取：
1
jps 或 ps –ef|grepjava (获取PID)
2
jstack [-l ]<pid> | tee -a jstack.log  (获取ThreadDump)
c. 分析：https://blog.csdn.net/rachel_luo/article/details/8920596
13. 如何查看Java应⽤用的线程信息？
通过top命令拿到线程的pid后使⽤用jstack命令
14. 计数？
1
wc -l

![10、linux命令(14题) 第3页插图](../assets/images/10、linux命令(14题)_p3_1_69bf5475.png)