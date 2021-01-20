[TOC]



# Python全栈学习（34）面向对象魔术方法

## \__new__

### 作用机制

```
1. __new__是用来创建实例对象的
2. 是静态方法，作用在__init__之前
3. 决定是否调用 __init__方法
```

### 举例说明

```python
**example 1**
class A:
    def __new__(cls, *args, **kwargs):
        o = super(A, cls).__new__(cls)
        print("call {} and {} at new".format(cls, o))
        return o

    def __init__(self):
        print("call {} at init".format(self))


a = A()
'''
call <class '__main__.A'> and <__main__.A object at 0x00000254BBC7B780> at new
call <__main__.A object at 0x00000254BBC7B780> at init
'''

**example 2**
class Boo(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)
    def __init__(self):
        print("From Boo")

class Amy(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(Boo,*args, **kwargs) #制造了Boo的实例对象
    def __init__(self):
        print("It is Amy ")

boo = Boo()
print(type(boo))
amy = Amy()
print(type(amy))

'''
From Boo
<class '__main__.Boo'>
<class '__main__.Boo'>
'''

**example 3 **设计模式--单例模式**
**只会创建一次self的空间**
class Baby:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


booboo = Baby("BOOBOO", 30)
amy = Baby("AMY", 5)
print(booboo, amy)
'''
<__main__.Baby object at 0x000002981DC45588> <__main__.Baby object at 0x000002981DC45588>
'''

class Baby2:
    def __init__(self, name, age):
        self.name = name
        self.age = age


booboo2 = Baby2("BOOBOO", 30)
amy2 = Baby2("AMY", 5)
print(booboo2, amy2)
'''
<__main__.Baby2 object at 0x000002981DC455C0> <__main__.Baby2 object at 0x000002981DC45630>
'''
```

## \__call__

### 作用机制

```python
1 __call__功能类似于在类中重载()运算符，使得类实例对象可以像调用普通函数一样，以“对象()”的形式使用。
2 python中，凡是可以将()直接应用到自身执行的，都成为 “可调用对象”。包括：自定义函数，内置函数，类实例对象等。
```

### 举例说明

```python
class Python:
    def __call__(self, name, time):
        print("{}的时间是{}".format(name,time))

Python()("python","2 months")
p1 = Python()
p1("C","3 months")
p1.__call__("GO","2 months")

'''
python的时间是2 months
C的时间是3 months
GO的时间是2 months
'''

#对于可调用对象，实际上 “名称()” 可以理解为 “名称.__call__()”的简写
```

### 用\__call__弥补hasattr的短板

```python
class Cpython:
    def __init__(self):
        self.name = "Cpython学习课程"
        self.addr = "https://www.cnblogs.com/bingabcd/p/6691730.html"

    def say(self):
        print("I am learning {}".format(self.name))


cpython = Cpython()

if hasattr(cpython, "name"):
    print(hasattr(cpython.name, "__call__"))
    print(callable(cpython.name))
if hasattr(cpython, "say"):
    print(hasattr(cpython.say, "__call__"))
    cpython.say.__call__()
   
'''
False
False
True
I am learning Cpython学习课程
'''
```

## \__str__  & \__repr__

### 作用以及区别

```python
#作用
__repr__ 和 __str__都是用来描述对象的信息

#区别
__repr__的目标是准确性，是让开发者使用的。在交互模式下提示回应
__str__的目标是可读性，是让用户使用的。主要用来打印操作
```

### 举例说明

```python
#__str__ 来描述类的信息
#打印一个对象、进行字符串拼接、str(对象) 总是调用这个对象的__str__方法，如果找不到__str__, 就调用__repr__方法
class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

    def __str__(self):
        return ','.join([self.name, str(self.price), self.period])


python = Course("python", 20000, "6 months")
go = Course("go", 13000, "5 months")
linux = Course("linux", 4000, "2 months")

lst = [python, go, linux]

for idx,course in enumerate(lst,1):
    print(idx, course)
    
    
'''
1 python,20000,6 months
2 go,13000,5 months
3 linux,4000,2 months
'''
#用%r进行字符串拼接，或者用 repr(对象) 的时候总是调用这个对象的__repr__方法
class Pyth:
    def __init__(self):
        self.lst = []

    def append(self, name):
        self.lst.append(name)

    def __str__(self):
        return "NOT LST"

    def __repr__(self):
        return str(self.lst)


py22 = Pyth()
py22.append("Sage")
print(py22)
print("Our class %s" % py22)
print("Our class %r" % py22)
'''
NOT LST
Our class NOT LST
Our class ['Sage']
'''

# __repr__ = __str__ 开发者模式和用户模式连用
>>> class Pyth:
...     def __init__(self):
...         self.lst = []
...     def append(self, name):
...         self.lst.append(name)
...     def __str__(self):
...         return "NOT LST"
...
'''
>>> py24=Pyth()
>>> py24
<__main__.Pyth object at 0x000001C637853E80> #__str__只能显示内存地址
'''


class Pyth:
    def __init__(self):
        self.lst = []
    def append(self, name):
        self.lst.append(name)
    def __str__(self):
        return "NOT LST"
    def __repr__(self):
        return str(self.lst)
    __repr__ = __str__
'''
交互模式：
>>> py22.append('AA')
>>> py22
NOT LST # __repr__ = __str__的作用
'''

```

## \__len__

### 作用

```python
__len__:是的len()可以处理实例对象。
```

### 举例说明

```python
class Stu:
    def __init__(self,*args):
        self.names = args

    def __len__(self):
        return len(self.names)

ss = Stu("AMY","SAGE","LUCAS")
print(len(ss))  #3


class Fib:
    def __init__(self,num):
        a, b, l = 0, 1, []
        for n in range(num):
            l.append(a)
            a,b = b, a+b
        self.numbers = l

    def __str__(self):
        return str(self.numbers)
    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print(f)
print(len(f))
'''
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
10
'''
```

