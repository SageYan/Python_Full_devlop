[TOC]



# Python全栈学习（31）面向对象之三大特性

## 三大特性：继承 封装 多态

## 继承 

### 定义

```python
继承关系的类之间是有层级的。
被继承的类被称为 父类、基类 或 超类 ；继承的类被称为 子类 或 派生类
```

### 作用

```python
1 增加了类的耦合性（耦合性不宜多，宜精）。
2 减少了重复代码。
3 使得代码更加规范化，合理化。
```

### **继承与重用性**

 通过继承的方式新建类B，让B继承A，B会‘遗传’A的所有属性(数据属性和函数属性)，实现代码重用 

```python
class  Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("{} is eating !".format(self.name))

    def drink(self):
        print("%s is drinking" % self.name)

    def sleep(self):
        print("{} is sleeping".format(self.name))


class Cat(Animal):
    def climb_tree(self):
        print("{} is climbing tree".format(self.name))

class Dog(Animal):
    def keep_house(self):
        print("{} is keeping house!".format(self.name))


amy = Cat('Amy')
# amy实例化，开辟空间,空间里有一个指向Cat类指针
# 实例化需要调用“init”方法,对象在自己的空间中找init没找到,到Cat类中找init也没找到,直到在找父类Animal中的init
sage = Dog('Sage')
amy.climb_tree()
sage.keep_house()
```



### 继承与派生

子类想要调用父类的方法的同时还想执行自己的同名方法 :父类名.方法名(self) 或  super().func(参数) 

```python
class Amimal:
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.hp = 100
        self.mp = 100

    def eat(self):
        print("%s is eating %s" % (self.name, self.food))

    def drink(self):
        print('%s is drinking' % self.name)

    def sleep(self):
        print('%s is sleeping' % self.name)


class Cat(Amimal):
    def eat(self):
        self.hp += 100
        Amimal.eat(self)

    def climb_tree(self):  #派生：猫有爬树技能
        print("{} is climbing tree".format(self.name))
        Amimal.drink(self)


class Dog(Amimal):
    def eat(self):
        self.mp += 30
        #Amimal.eat(self)
        super().eat()

    def house_keep(self):
        print('%s is keeping the house' % self.name)


amy = Cat("Amy","fish")
sage = Dog("Sage", 'meat')

amy.eat()
sage.eat()

print(amy.__dict__)
print(sage.__dict__)

'''
Amy is eating fish
Sage is eating meat
{'hp': 200, 'name': 'Amy', 'mp': 100, 'food': 'fish'}
{'hp': 100, 'name': 'Sage', 'mp': 130, 'food': 'meat'}
'''
```

#### 思考题

```python
class Foo:
    def __init__(self):
        self.func()

    def func(self):
        print("in foo!")

class Son(Foo):
    def func(self):
        print("in son!")


Son() #in son!

PS：执行过程
遵循LGB原则，实例化调用“init”方法，对象空间Son()中没有,通过类指针到类Son中去寻找。
类Son中也没有，到父类Foo中调用“init”方法，初始化self,执行func函数。
此时self指向的是对象空间Son()，而对象空间中没有func函数，于是在类空间Son中寻找，找到执行func。
```

#### 子类定制个性的属性

```python
class Aminal:
    def __init__(self,name,food):
        self.name = name
        self.food = food

    def eat(self):
        print('%s is eating %s'%(self.name,self.food))



class Cat(Aminal):
    def __init__(self,name,food,eye):
        Aminal.__init__(self,name,food) # 调用了父类的初始化,去完成一些通用属性的初始化
        self.eye =eye # 派生属性


amy = Cat('amy','fish','blue')

print(amy.__dict__)
'''
{'name': 'amy', 'eye': 'blue', 'food': 'fish'}
'''
```

### 多继承

一个类有多个父类,在调用父类方法的时候,按照继承顺序,先继承的就先寻找

#### 新式类与经典类

```python
# 只要继承object类就是新式类
# 不继承object类的都是经典类

PS：
python3 所有的类都继承object类,都是新式类
在python2中 不继承object的类都是经典类，继承object类的就是新式类了

例子：
# 在python2中,不主动继承object类
class A:pass         # 经典类
class B(object):pass # 新式类
# 在python3中，都继承object类，不存在经典类
class A:pass         # 新式类
class B(object):pass # 新式类
```

#### 继承顺序

```python
1 单继承
对于单继承来说，新式类和经典类的继承顺序都是深度优先

2 多继承
经典类：深度优先
新式类：广度优先

例子：
class A:
    def func(self):
        print('A')


class B(A):
    pass
    #def func(self):
     #   print('B')

class C(A):
    pass
    def func(self):
       print('C')

class D(B,C):
    pass
   # def func(self):
   #     print('D')

D().func()
print(D.mro()) #在新式类中使用mro来查看继承顺序
'''
C
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
'''

PS：
新式类采用c3算法来安排继承顺序。
c3算法如下：
A(O) = [AO]
B(A) = [BAO]
C(A) = [CAO]
D(B) = [DBAO]
E(C) = [ECAO]
#继承顺序规则
F => [DBAO] + [ECAO]
FD     => [BAO] + [ECAO]
FDB    => [AO] + [ECAO]
FDBE   => [AO] + [CAO]
FDBEC  => [AO] + [AO]
FDBECA => [O] + [O]
FDBECAO
```

### 抽象类

抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化。约束它的所有子类必须实现一些和它同名的方法。

#### 自定义抽象类

```python
1. #没有使用抽象类约束，导致归一化设计报错
class Alipay:
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def pay(self):
        dic = {'uname':self.name,'price':self.money}
        print('%s通过支付宝支付%s钱成功'% (dic['uname'],dic['price']))


class Wechat:
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def pay(self):
        dic = {'username':self.name,'money':self.money}
        print('%s通过微信支付%s钱成功' % (self.name,self.money))


class Apple:
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def fuqian(self):
        dic = {'user':self.name,'num':self.money}
        print('%s通过苹果支付%s钱成功' % (self.name,self.money))

# 归一化设计函数
def pay(name,price,method):
    if method == 'Alipay':
        Alipay(name,price).pay()
    elif method == 'Wechat':
        Wechat(name,price).pay()
    elif method == 'Apple':
        Apple(name,price).pay()

pay('Sage',90,'Alipay')
pay('Boo',100,'Wechat')
pay('Amy',20,'Apple')

'''
Sage通过支付宝支付90钱成功
Traceback (most recent call last):
Boo通过微信支付100钱成功
  File "D:/python学习/venv/Scripts/20201118.py", line 61, in <module>
    pay('Amy',20,'Apple')
  File "D:/python学习/venv/Scripts/20201118.py", line 57, in pay
    Apple(name,price).pay()
AttributeError: 'Apple' object has no attribute 'pay'
'''

2. #通过自定义抽象类来约束子类开发规范

class payment:
    def pay(self):
        raise NotImplementedError('请在子类中重写同名pay方法')

class Alipay(payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def pay(self):
        dic = {'uname':self.name,'price':self.money}
        print('%s通过支付宝支付%s钱成功'% (dic['uname'],dic['price']))

class Wechat(payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def pay(self):
        dic = {'username':self.name,'money':self.money}
        print('%s通过微信支付%s钱成功' % (self.name,self.money))


class Apple(payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def fuqian(self):
        dic = {'user':self.name,'num':self.money}
        print('%s通过苹果支付%s钱成功' % (self.name,self.money))


def pay(name,price,method):
    if method == 'Alipay':
        Alipay(name,price).pay()
    elif method == 'Wechat':
        Wechat(name,price).pay()
    elif method == 'Apple':
        Apple(name,price).pay()

pay('Sage',90,'Alipay')
pay('Boo',100,'Wechat')
pay('Amy',20,'Apple')

'''
Sage通过支付宝支付90钱成功
Traceback (most recent call last):
Boo通过微信支付100钱成功
  File "D:/python学习/venv/Scripts/20201119.py", line 41, in <module>
    pay('Amy',20,'Apple')
  File "D:/python学习/venv/Scripts/20201119.py", line 37, in pay
    Apple(name,price).pay()
  File "D:/python学习/venv/Scripts/20201119.py", line 3, in pay
    raise NotImplementedError('请在子类中重写同名pay方法')
NotImplementedError: 请在子类中重写同名pay方法
'''
```

#### abc模块

```python
from abc import ABCMeta,abstractmethod
class payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self):
        raise NotImplementedError('请在子类中重写同名pay方法')


class Alipay(payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def pay(self):
        dic = {'uname':self.name,'price':self.money}
        print('%s通过支付宝支付%s钱成功'% (dic['uname'],dic['price']))

class Wechat(payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def pay(self):
        dic = {'username':self.name,'money':self.money}
        print('%s通过微信支付%s钱成功' % (self.name,self.money))


class Apple(payment):
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def fuqian(self):
        dic = {'user':self.name,'num':self.money}
        print('%s通过苹果支付%s钱成功' % (self.name,self.money))


def pay(name,price,method):
    if method == 'Alipay':
        Alipay(name,price).pay()
    elif method == 'Wechat':
        Wechat(name,price).pay()
    elif method == 'Apple':
        Apple(name,price).pay()

Apple('Sage',307)
#约束力强,依赖abc模块 若违反约束，子类不能实例化
'''
TypeError: Can't instantiate abstract class Apple with abstract methods pay
'''
```

### super方法

```python
#定义
super() 函数是用于调用父类(超类)的一个方法。
super是按照mro顺序来寻找当前类的下一个类，MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

example：
class A(object):
    def fun(self):
        print("A")

class B(A):
    def fun(self):
        super().fun()
        print('B')


class C(A):
    def fun(self):
        super().fun()
        print("C")

class D(B,C):
    def fun(self):
        super().fun()
        print("D")


D().fun()

'''
A C B D
'''
#语法
Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx； 在py2的经典类中,并不支持使用super

class User(object):
    def __init__(self,name):
        self.name = name

class Vip(User):
    def __init__(self,name,level):
        #super(Vip, self).__init__(name) #py2 py3都支持此写法
        #User.__init__(self,name)
        super().__init__(name) #py3的写法
        self.level = level
Sage = Vip('Sage',100)
print(Sage.__dict__)

```



### 练习

```python
# Queue队列 : 先进先出 FIFO(FIRST IN FIRST OUT)
# Stack队列 ：先进后出 FILO
1. 方法一
class Queue:
    def __init__(self):
        self.l = []
    def put(self,item):
        self.l.append(item)
    def get(self):
        return self.l.pop(0)

class Stack:
    def __init__(self):
        self.l=[]
    def put(self,item):
        self.l.append(item)
    def get(self):
        return  self.l.pop()

2. 方法二
class Foo():
    def __init__(self):
        self.l = []
    def put(self,item):
        self.l.append(item)

class Queue(Foo):
    def get(self):
        return self.l.pop(0)

class Stack(Foo):
    def get(self):
        return self.l.pop()
3. 方法三
class Foo:
    def __init__(self):
        self.l = []
    def put(self,item):
        self.l.append(item)
    def get(self):
        return self.l.pop() if self.index else self.l.pop(0)

class Queue(Foo):
    def __init__(self):
        self.index = 0
        Foo.__init__(self)

class Stack(Foo):
    def __init__(self):
        self.index =1
        Foo.__init__(self)
4. 方法四
class Foo:
    def __init__(self):
        self.l = []

    def put(self,item):
        self.l.append(item)
    def get(self):
        return self.l.pop()


class Queue(Foo):
    def get(self):
        return self.l.pop(0)
class Stack(Foo):
    pass


#自定义Pickle,借助pickle模块来完成简化的dump和load
import pickle
class mypickle:
    def __init__(self,path):
        self.path = path

    def dump(self,obj):
        with open(self.path,'ab') as f:
            pickle.dump(obj,f)

    def load(self):
        with open(self.path,'rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break


class Course:
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price

python = Course('python','6 moneth',21800)
linux = Course('linux','5 moneth',19800)
go = Course('go','4 moneth',12800)


mypic = mypickle('picfile')
# mypic.dump(python)
# mypic.dump(linux)
for i in mypic.load():
    print(i.__dict__)
'''
{'price': 21800, 'period': '6 moneth', 'name': 'python'}
{'price': 19800, 'period': '5 moneth', 'name': 'linux'}
'''

import json
class myjson:
    def __init__(self,path):
        self.file = path

    def dump(self,obj):
        with open(self.file,'a',encoding='utf-8') as f:
            f.write(json.dumps(obj)+'\n')

    def load(self):
        with open(self.file,'r',encoding='utf-8') as f:
            for i in f:
                yield json.loads(i.strip())
```

## 多态

```python
简单来说，多态就是在子类中覆写父类的方法。这样做的好处是同样名称的方法在不同的子类中会有不同的行为。
多态最核心的思想就是，父类的引用可以指向子类的对象，多态之所以是这样的是因为基于一个事实：子类就是父类。

#关于多态的一些重要说明：
1.当使用多态方式调用方法时，首先检查父类中是否有此方法，如果没有则编译错误，如果有则再去调用子类重写（Override）【如果重写的话】的此方法，没有重写的话，还是调用从父类继承过来的方法。

2.多态是一种运行期的行为，不是编译期行为！在编译期间它只知道是一个引用，只有到了执行期，引用才知道指向的是谁。这就是所谓的“软绑定”。多态是一项让程序员“将改变的事物和未改变的事物分离开来”重要技术。

```

### 举例说明

```python
import abc
class File(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def click(self):
        pass

class Text(File):
    def click(self):
        print('open file!')

class Exefile(File):
    def click(self):
        print('execute file!')

t = Text()
e = Exefile()
#判断一个变量是否是某个类型可以用isinstance()判断,type不适合判断父类子类关系
print(isinstance(t,File))
print(isinstance(e,File))
print(type(t) is File)
print(type(t) is Text)
#可见所有对象都是File类型
'''
True
True
False
True
'''



#实例中的叫方法，类中的叫函数
from types import FunctionType,MethodType
# FunctionType : 函数
# MethodType : 方法
print(isinstance(t.click, FunctionType))
print(isinstance(Text.click,MethodType))
print(isinstance(t.click, MethodType))
print(isinstance(Text.click,FunctionType))
print(t.click)
print(Text.click)
'''
False
False
True
True
<bound method Text.click of <__main__.Text object at 0x0000020C198E7EF0>>
<function Text.click at 0x0000020C197C39D8>
'''
```

### 鸭子类型

```python
鸭子类型是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

import abc
class File(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def click(self):
        pass

class Text(File):
    def click(self):
        print('open file!')

class Exefile(File):
    def click(self):
        print('execute file!')


class Video:
    def click(self):
        print("video play!")

def click_file(filename):
    filename.click()


t = Text()
e = Exefile()
v = Video()


click_file(t)
click_file(e)
click_file(v)
'''
open file!
execute file!
video play!
'''

#我们可以使用一个函数 click_file() 来访问不同 File 子类中的相同方法。但其实对于上面的 click_file() 函数来说，传入的参数并不一定需要是 File 类型的，只需要保证传入的对象有一个 click() 方法即可
```

## 封装

### 定义以及意义

```python
【封装】
	隐藏对象的属性和实现细节，仅对外提供公共访问方式。

【好处】 
1. 将变化隔离； 
2. 便于使用；
3. 提高复用性； 
4. 提高安全性；

【封装原则】
      1. 将不需要对外提供的内容都隐藏起来；
      2. 把属性都隐藏，提供公共方法对其访问。
```

### 私有变量和私有方法

 ***在python中用双下划线开头的方式将属性隐藏起来（设置成私有的）*** 

**私有变量**

```python
# 类中所有双下划线开头的变量 如__x都会自动变形成：_类名__x的形式：
class User:
    __nation = "China"
    def __init__(self,name,pwd):
        self.name = name
        self.__pwd = pwd

Sage = User('sage','123')
Sage = User('sage','123')
print(User.__dict__)
print(User._User__nation)
print(Sage.__dict__)
print(Sage._User__pwd)
'''
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'User' objects>, '_User__nation': 'China', '__doc__': None, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__init__': <function User.__init__ at 0x000001A2840B37B8>}

China

{'_User__pwd': '123', 'name': 'sage'}

123
'''

这种自动变形的特点：
1.类中定义的__x只能在内部使用，如self.__x，引用的就是变形的结果。
2.这种变形其实正是针对外部的变形，在外部是无法通过__x这个名字访问到的。
3.在子类定义的__x不会覆盖在父类定义的__x，因为子类中变形成了：_子类名__x,而父类中变形成了：_父类名__x，即双下滑线开头的属性在继承给子类时，子类是无法覆盖的。
```

**私有方法**

```python
#在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
class Foo(object):
    def __init__(self):
        self.__func()

    def __func(self):
        print("From Foo!")

class Son(Foo):
    def __func(self):
        print("From Son!!")

Son()
'''
From Foo!
'''

#调用私有方法（通访问私有变量）
办法1：通过一个专门的成员方法调用
办法2：通过 实例对象._类名__私有方法() 的方式来调用
import hashlib
class User(object):
    def __init__(self,name,pwd):
        self.name = name
        self.__pwd = pwd #私有实例变量

    def __get_md5(self): #私有方法
        md5 = hashlib.md5(self.name.encode('utf-8'))
        md5.update(self.__pwd.encode('utf-8'))
        return md5.hexdigest()
    def get_pwd(self):
        return self.__get_md5()

amy = User('Amy','7456!!')
print(amy.get_pwd())
#print(amy._User__get_md5())
'''
19de44a5ed8482f4b1d3b0018a479887
'''
```

### **封装与扩展性**

```python
封装在于明确区分内外，使得类实现者可以修改封装内的东西而不影响外部调用者的代码；
而外部使用用者只知道一个接口(函数)，只要接口（函数）名、参数不变，使用者的代码永远无需改变。
这就提供一个良好的合作基础——或者说，只要接口这个基础约定不变，则代码改变不足为虑。
```

eg：

```python
>>>类的设计者
class Room(object):
    def __init__(self,name,owner,len,width,hight):
        self.name = name
        self.owner = owner
        self.__len = len
        self.__wid = width
        self.__hig = hight

    def tell_room(self):
        return self.__wid * self.__len
>>>类的调用者
r1 = Room("bedroom",'Sage', 10,10,3)
print(r1.tell_room())

class Room(object):
    def __init__(self,name,owner,len,width,hight):
        self.name = name
        self.owner = owner
        self.__len = len
        self.__wid = width
        self.__hig = hight

    def tell_room(self):
        return self.__wid * self.__len * self.__hig 

#类的设计者，轻松的扩展了功能，而类的使用者完全不需要改变自己的代码
#对于仍然在使用tell_area接口的人来说，根本无需改动自己的代码，就可以用上新功能
r1 = Room("bedroom",'Sage', 10,10,3)
print(r1.tell_room())
```

