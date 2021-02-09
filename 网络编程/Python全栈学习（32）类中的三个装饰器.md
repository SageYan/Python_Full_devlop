[TOC]



# Python全栈学习（35）网络编程知识储备

## 参考知识

https://www.cnblogs.com/linhaifeng/articles/5937962.html

```python
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    @property
    def area(self):
        return pi * self.r ** 2


ring = Circle(12)
#property把area方法伪装成属性
print(ring.area)


import time
class Person:
    def __init__(self,name,birth):
        self.name = name
        self.birth = birth
    @property
    def age(self):
        return time.localtime().tm_year - self.birth

Sage = Person('Sage',1989)
print(Sage.age)

#为什么要用property
将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的，这种特性的使用方式遵循了 统一访问的原则
```

### 二、和私有属性合作，提供对外接口

```python
class Goods:
    discount = 0.75
    def __init__(self,name,originPrice):
        self.name = name
        self.__price = originPrice
    @property
    def price(self):
        return self.__price * self.discount

    @price.setter
    def price(self,newvalue):
        if isinstance(newvalue,int):
            self.__price = newvalue

    @price.deleter
    def price(self):
        
        #del self.__price
        raise TypeError("不能删除此属性")


apple = Goods('apple',100)
print(apple.price)

apple.price = 120
print(apple.price)

del apple.price
print(apple.__dict__)
```

## classmethod

```python
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
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
