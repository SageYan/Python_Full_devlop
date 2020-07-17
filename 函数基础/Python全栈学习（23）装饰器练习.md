[TOC]



# Python全栈学习（23）装饰器练习

### 编写装饰器,在每次执行被装饰函数之前打印一句'每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码'。

```python
def wapper(func):
    def inner(*args,**kwagrgs):
        print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
        ret = func(*args,**kwagrgs)
        return ret
    return inner

@wapper
def f1():
    print("f1 is my name")

f1()
```

### 为函数写一个装饰器，把函数的返回值 +100 然后再返回

```python
def wapper(func):

    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        return ret + 100
    return inner

@wapper
def f2():
    return 20

print(f2())
```

### 请实现一个装饰器，通过一次调用是函数重复执行5次

```python
def wapper(func):

    def inner(*args,**kwargs):
        for i in range(5):
            ret = func(*args,**kwargs)
        return ret
    return inner

@wapper
def f3():
    print("I am f3")

f3()
```

### 请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中

```python
'''
可用代码：
import time
struct_time = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 当前时间节点

def wrapper():
    pass

def func1(f):
    print(f.__name__)
func1(wrapper)
函数名通过： 函数名.__name__获取
'''

import time
def wapper(func):
    def inner(*args,**kwargs):
        with open('log','a',encoding='utf8') as f1:
            struct_time = time.localtime()
            f1.write('在{}时间，调用了函数{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S",struct_time), func.__name__))
        ret = func(*args,**kwargs)
        return ret
    return inner

@wapper
def f4():
    print("in F4")

f4()
time.sleep(4)
f4()
time.sleep(5)
f4()
```

