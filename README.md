# advance-python
python高级编程和异步io并发编程

### 笔记
1. 一切皆对象，Object是最顶层的基类，type的基类也是object。
2. type>class>object。类是由type对象创建的，对象是由类对象创建的
3. gil会根据执行的字节码行数以及时间片释放gil，gil在遇到io的操作时候主动释放
4. 对于io操作来说，多线程和多进程性能差别不大
5. 在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等
6. 资源竞争导致死锁
7. 耗cpu的操作，用多进程编程， 对于io操作来说， 使用多线程编程，进程切换代价要高于线程
8. 协程 -> 有多个入口的函数， 可以暂停的函数， 可以暂停的函数(可以向暂停的地方传入值)

