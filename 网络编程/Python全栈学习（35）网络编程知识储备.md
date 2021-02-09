[TOC]



# Python全栈学习（35）网络编程知识储备

## 参考知识

https://www.cnblogs.com/linhaifeng/articles/5937962.html

## 网络通信原理

### 1 互联网的本质就是一系列的网络协议

```python
互联网协议的功能：定义计算机如何接入internet，以及接入internet的计算机通信的标准
```

### 2 osi七层协议

```python
应表会传网数物
```

### 3 tcp/ip五层模型讲解

```python
我们将应用层，表示层，会话层并作应用层，从tcp／ip五层协议的角度来阐述每层的由来与功能，搞清楚了每层的主要协议
就理解了整个互联网通信的原理。

每层都运行特定的协议，越往上越靠近用户，越往下越靠近硬件
```

3.1 物理层

```python
物理层功能：主要是基于电器特性发送高低电压(电信号)，高电压对应数字1，低电压对应数字0
```

3.2 数据链路层

```python
数据链路层的功能：定义了电信号的分组方式(以太网协议)

以太网协议规定
 	一组电信号构成一个数据包，叫做‘帧’
 	每一数据帧分成：报头head和数据data两部分

#head包含：(固定18个字节)
	发送者／源地址，6个字节 (MAC地址)
	接收者／目标地址，6个字节
	数据类型，6个字节
#data包含：(最短46字节，最长1500字节)
	数据包的具体内容

#以太网协议采用最原始的方式，广播的方式进行通信
```

3.3 网络层

```python
互联网是由一个个彼此隔离的小的局域网组成的，那么如果所有的通信都采用以太网的广播方式，那么一台机器发送的包全世界都会收到，这就不仅仅是效率低的问题了，这会是一种灾难。
因此：
#网络层功能：引入一套新的地址用来区分不同的广播域／子网，这套地址即网络地址

ip协议：
议的作用主要有两个，一个是为每一台计算机分配IP地址，另一个是确定哪些地址在同一个子网络。

```



### 一、不用实例化对象,就直接使用类在外部修改类的静态变量

```python
class Goods:
    __discount = 0.8
    def __init__(self,price):
        self.price = price * self.__discount

    @classmethod
    def change_dis(cls,discount):
        cls.__discount = discount

Goods.change_dis(0.85)
print(Goods(100).price)
```

### 二、把一个对象绑定的方法 修改成一个类方法

```python
import time
class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def today(cls):
        tm = time.localtime()
        date = cls(tm.tm_mday,tm.tm_mon,tm.tm_year)
        return date

today = Date.today()
print(today.day,"Today is {}-{}-{}".format(today.year,today.month,today.day))

#22 Today is 2020-12-22
```

## staticmethod

### 被装饰的方法会成为一个静态方法

```python
class User:
    pass
    @staticmethod
    def login(a,b):      
        # 本身是一个普通的函数,被挪到类的内部执行,那么直接给这个函数添加@staticmethod装饰器就可以了
        # 在函数的内部既不会用到self变量,也不会用到cls类
        print('登录的逻辑',a,b)
```

## 小结

```python
class A:
    country = '中国'
    def func(self):
        print(self.__dict__)
    @classmethod
    def clas_func(cls):
        print(cls)
    @staticmethod
    def stat_func():
        print('普通函数')
    @property
    def name(self):
        return 'wahaha'
    
# 能定义到类中的内容
# 静态变量 是个所有的对象共享的变量  有对象\类调用 但是不能重新赋值
# 绑定方法 是个自带self参数的函数    由对象调用
# 类方法   是个自带cls参数的函数     由对象\类调用
# 静态方法 是个啥都不带的普通函数    由对象\类调用
# property属性 是个伪装成属性的方法  由对象调用 但不加括号
```
