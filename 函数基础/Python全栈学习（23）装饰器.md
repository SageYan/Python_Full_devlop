[TOC]



# Python全栈学习（23）装饰器

## **装饰器的定义**

### 开放封闭原则

```python
# 开放封闭原则：
开放：对代码的拓展开放的。
封闭：对源码的修改是封闭的。
```

### 装饰器初识

```python
# 装饰器：完全遵循开放封闭原则。
# 装饰器： 在不改变原函数的代码以及调用方式的前提下，为其增加新的功能。
# 装饰器就是一个函数。
```

#### 版本1：语法糖，标准版的装饰器

```python
import time

def timer(f):
    def inner():
        start_time = time.time()
        f()
        stop_time = time.time()
        print("函数的运行时间是：{}秒".format(stop_time - start_time))
    return inner

@timer  #index = timmer(index)
def index():
    time.sleep(0.5)
    print("Welcome!")


index()

```

#### 版本2：被装饰函数带返回值

```python
import time

def timer(func):
    def inner():
        s_t = time.time()
        res = func()
        end_t = time.time()
        print("函数运行的时间是：{}秒".format(end_t - s_t))
        return res
    return inner


@timer
def Sage():
    time.sleep(0.4)
    print("Sage is a good man!")
    return "Amy is his daughter!"
Sage()
```

#### 版本3：被装饰函数带参数

```python
import time

def timmer(func):
    def inner(*args,**kwargs):
        '''
        # 函数的定义中：* 聚合  args=("BOOBOO",5)
        '''
        
        s_t = time.time()
        res = func(*args,**kwargs)
        
        '''
        # 函数的执行：* 打散 func(*args) = func(*("BOOBOO",5))
        '''
        
        e_t = time.time()
        print("函数的运行时间是：{}秒".format(e_t - s_t))
        return  res
    return inner

@timmer
def amy(name,age):
    time.sleep(0.8)
    print("Amy is a wonderful gril and her mom is {} and she is {} years old.".format(name,age))
    return "Sage is a good man!"

amy("BOOBOO",5)
```

#### 装饰器标准结构

```python
def wrapper(f):
    def inner(*args,**kwargs):
        '''添加额外的功能：执行被装饰函数之前的操作'''
        ret = f(*args,**kwargs)
        ''''添加额外的功能：执行被装饰函数之后的操作'''
        return ret
    return inner
```

