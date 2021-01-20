[TOC]



# Python全栈学习（33）反射

## 什么是反射

```python
python面向对象的反射：通过字符串的形式操作对象的相关属性。python中一切皆对象（都可以使用反射）
```

## 五个反射函数

### hasattr

```python
#判断对象中是否有这个方法或变量

class Person(object):
    def __init__(self,name):
        self.__name = name

    def talk(self):
        print("{} is talking".format(self.__name))

sage = Person("Sage")
print(hasattr(sage,"name"))
print(hasattr(sage,"__name"))
print(hasattr(sage,"_Person__name"))
print(hasattr(Person,"talk"))

'''
False
False
True
True
'''
```

### getattr

```python
#获取对象中的方法或变量的内存地址
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("eating")

sage = Person("Sage",31)
amy = Person("Amy",5)

r1 = getattr(sage,"name")
r2 = getattr(amy,"age")
f1 = getattr(sage,"eat")

print('{} is {} years old'.format(r1,r2))
f1()
'''
Sage is 5 years old
eating
'''

#反射导入模块中的方法，变量
import demo
p = getattr(demo,"Python")
func = getattr(demo,"rule")
print(func("sage"))
print(p,demo.Python)


# 反射当前执行的py文件 - 脚本
def func():
    print("from main")

import sys
print(sys.modules.get('__main__').func,func)
sys.modules.get('__main__').func()

'''
<function func at 0x000002298571D1E0> <function func at 0x000002298571D1E0>
from main
'''
```

### setattr

```python
# 为对象添加变量或者方法

def func(name):
    print("%s is talking" % name)

def func_obj(obj):
    print("{} is from obj".format(obj.name)) #obj.name 为了初始化对象准备

class Person(object):
    def __init__(self,name):
        self.name = name

sage = Person("SAGE")

setattr(sage,"talk",func) #将func函数添加到对象sage中，命名为talk
setattr(sage,"talk2",func_obj)
setattr(sage,"age",31)

print(sage.__dict__)
sage.talk("AMY")
sage.talk2(sage) # 额外添加的方法，手动传入对象
print(sage.age)

'''
{'age': 31, 'name': 'SAGE', 'talk2': <function func_obj at 0x0000020AE1CBD400>, 'talk': <function func at 0x0000020AE1CBD378>}
AMY is talking
SAGE is from obj
31
'''
```

### delattr

```python
# 删除对象中的变量。注意：不能删除方法

class User(object):

    def __init__(self,name,password):
        self.name = name
        self.pwd = password

    def login(self):
        print("Login successfully")

booboo = User("BOOBOO",123)
delattr(booboo,"pwd")
delattr(booboo,"login") #报错
print(booboo.pwd)       #报错
```

### callable

```python
#判断对象是否可调用
class A:
    def __init__(self):
        self.name = "BOOBOO"

    def func(self):
        return self.name


a = A()

if hasattr(a, "func"):
    if callable(getattr(a, "func")):
        print(getattr(a, "func")())
```



## 反射例子

```python
#利用反射来减少条件判断
class Payment(object):
    def pay(self):
        raise NotImplementedError("请在子类中定义同名方法pay")

class Alipay(Payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money

    def pay(self):
        print("%s通过支付宝支付了%s元"%(self.name,self.money))

class Wechat(Payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money

    def pay(self):
        print("%s通过微信支付了%s元"%(self.name,self.money))

class Apple(Payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money

    def pay(self):
        print("%s通过applepay支付了%s元"%(self.name,self.money))

def pay(name,money,method): #不使用反射，需要多次条件判断
    if method == 'Alipay':
        Alipay(name,money).pay()
    elif method == "Wechat":
        Wechat(name,money).pay()
    elif method == "Apple":
        Apple(name,money).pay()

import sys
def pay2(name,money,method):
    if hasattr(sys.modules["__main__"],method):
        className = getattr(sys.modules['__main__'],method)
        obj = className(name,money)
        obj.pay()
    else:print("输入有误")

pay2("Sage",90,"Alipay2")
pay("Amy",10,"Wechat")


#eg2

class File(object):
    lst = [("读文件", "read"), ("写文件", "write"),
           ('删除文件', 'remove'), ('文件重命名', 'rename'),
           ('复制', 'copy'), ('移动文件', 'move')]

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self):
        print('in write func')

    def read(self):
        print('in read func')

    def remove(self):
        print('in remove func')

    def rename(self):
        print('in rename func')

    def copy(self):
        print('in copy func')

    def move(self):
        print('in 移动文件 func')

f = File("test")
while True:
    for index,opt in enumerate(f.lst,1):
        print(index,opt[0])
    num = int(input("PLS input your operation :").strip())
    if hasattr(f,File.lst[num-1][1]):
        getattr(f,File.lst[num-1][1])()
```

## 反射作业

```python
'''
用反射完成
写一个python脚本,在cmd里执行,实现：
python xxx.py 用户名 密码 cp 文件路径 目的地址
python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
python xxx.py alex sb rm D:\python_22\day22
python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23
'''

import os
import sys
import shutil
class OsCmd:
    def __init__(self):
        self.user = "alex"
        self.pwd = "sb"
    def cp(self):
        if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
            filename = os.path.basename(sys.argv[4])
            newpath = os.path.join(sys.argv[5],filename)
            shutil.copy2(sys.argv[4],newpath)
            

        else:print("wrong path input!")

    def rename(self):
        if os.path.exists(sys.argv[4]) and os.path.exists(os.path.dirname(sys.argv[5])):
            os.rename(sys.argv[4], sys.argv[5])
            print("rename到{}命令执行成功".format(sys.argv[5]))
        else:
            print("wrong path input!")

oscmd = OsCmd()
if getattr(oscmd,"user") == sys.argv[1] and getattr(oscmd,"pwd") == sys.argv[2] and len(sys.argv) == 6:
    getattr(oscmd,sys.argv[3])()
```

