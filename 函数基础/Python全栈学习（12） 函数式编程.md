[TOC]

# Python全栈学习（12）函数式编程

编程方法论：
面向过程
函数式
面向对象

## 特点

```python
1 不可变数据 ：不用变量保存状态
2 第一类变量：函数即变量
3 尾调用：在函数的最后一步进入递归
```

## 高阶函数

```python
1)函数接收的参数是一个函数名  
2) 返回值中包含函数

把函数当作参数传给另外一个函数
def foo(n):
    print(n)

def bar(name):
    print("My name is %s" % name)
foo(bar)
foo(bar("sage"))

--结果
<function bar at 0x00000247C589F2F0>
My name is sage
None


返回值中包含函数
def bar():
    print('from bar')
def foo():
    print('from foo')
    return bar

foo()
foo()()
--结果
from foo
from foo
from bar

def hanle():
    print('from handle')
    return hanle
h=hanle()
h()



def test1():
    print('from test1')
def test2():
    print('from handle')
    return test1()

test2()
--结果
from handle
from test1
```

## 尾调用

```python
1 在函数的最后一步调用bar
def bar(n):
    return n

def foo(x):
    return bar(x)

2 非尾调用，需等待函数bar()的调用结果
def bar(n):
    return n

def foo():
    return bar(x) + 1	
```





