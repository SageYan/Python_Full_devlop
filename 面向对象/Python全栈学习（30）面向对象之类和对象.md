[TOC]



# Python全栈学习（30）面向对象之类和对象

## 类的定义

```python
类的定义是对显示事务的抽象过程和能力，类是一个对象/实例的模板，也是一个特殊的对象/实例（因为Pythobn中一切皆对象，所以类本身也是一个对象）
```

## 类有两种作用：属性引用和实例化

### 属性引用

```python
class Person:
    role = 'person'
    def __init__(self,name,sex,job,hp,weapon,ad):
        self.name = name
        self.sex = sex
        self.job = job
        self.hp = hp
        self.weapon = weapon
        self.ad = ad
    def rub(self,dog):
        dog.hp -= self.ad
        print('%s给%s搓了澡,%s掉了%s点血,%s当前血量%s' % (self.name,dog.name,self.ad,dog.name,dog.hp))

print(Person.role)
print(Person.rub)

'''
person
<function Person.rub at 0x0000019E70FFD400>
'''
```

### 类属性的查看

```python
一：我们定义的类的属性到底存到哪里了？有两种方式查看
dir(类名)：查出的是一个名字列表
类名.__dict__:查出的是一个字典，key为属性名，value为属性值

二：特殊的类属性
类名.__name__# 类的名字(字符串)
类名.__doc__# 类的文档字符串,查看注释
类名.__base__# 类的第一个父类
类名.__bases__# 类所有父类构成的元组
类名.__dict__# 类的字典属性
类名.__module__# 类定义所在的模块
类名.__class__# 实例对应的类(仅新式类中)  <class 'type'>
```



### 类的实例化——实例化一个对象

```python
语法：对象名 = 类名(参数)
alex = Person('alex','male','worker',250,'sword',1)

#万能的点 "."
#对象属性的查看
print(alex,alex.__dict__)
print(alex.ad)
#对象属性的增加
alex.money = 2000 
#对象属性的修改
alex.name = 'alexSB'
#对象属性的删除
del alex.sex
print(alex.money,alex.__dict__)

'''
<__main__.Person object at 0x000001C7CBF645F8> {'ad': 1, 'job': 'worker', 'hp': 250, 'sex': 'male', 'weapon': 'sword', 'name': 'alex'}
1
2000 {'ad': 1, 'job': 'worker', 'hp': 250, 'money': 2000, 'weapon': 'sword', 'name': 'alexSB'}
'''

其实实例化一个对象总共发生了三件事：
　　1，在内存中开辟了一个对象空间。
　　2，自动执行类中的__init__方法，并将这个对象空间（内存地址）传给了__init__方法的第一个位置参数self。
　　3，在__init__ 方法中通过self给对象空间添加属性。
```

## 对象的相关知识

```python
#对象是关于类而实际存在的一个例子，即实例

#对象/实例只有一种作用：属性引用
```

### 使用对象操作类中的方法

绑定方法的调用方式

```python
对象.绑定方法() = 类名.绑定方法(对象)
```



```python
class Person:
    role = 'person'
    def __init__(self,name,sex,job,hp,weapon,ad):
        self.name = name
        self.sex = sex
        self.job = job
        self.hp = hp
        self.weapon = weapon
        self.ad = ad
    def rub(self,dog):
        dog.hp -= self.ad
        print('%s给%s搓了澡,%s掉了%s点血,%s当前血量%s' % (self.name,dog.name,dog.name,self.ad,dog.name,dog.hp))


class Dog:
    def __init__(self,name,ad,kind,hp):
        self.name=name
        self.ad=ad
        self.kind=kind
        self.hp = hp

    def bite(self,person):
        person.hp -= self.ad
        print('%s咬了%s,%s掉了%s点血,%s当前血量%s' % (self.name,person.name,person.name,self.ad,person.name,person.hp))

alex = Person('alex', 'male', 'worker', 250, 'sword', 1)
egg = Dog('egg',20,'二哈',340)

egg.bite(alex)
print(alex.hp)
'''
egg咬了alex,alex掉了20点血,alex当前血量230
230
'''
```

## 类的属性

```tex
1 公有属性/静态属性
2 成员属性/实例属性
3 私有属性
```

### 静态属性

```python
'''
直接定义在class下的属性就是公有属性/类属性，比如下面那个Person类中的nationality属性。
“公有”的意思是这个属性是这个类的所有实例对象共同所有的，因此默认情况下这个属性值值保留一份，而不会为该类的每个实例都保存一份。
'''

import uuid


class Person(object):
    nationality = 'China'
    test = [1,2]

    def __init__(self, name):
        self.name = name
        self.__id = str(uuid.uuid1())

    def hello(self):
        print('Hi, i am %s, from %s， my id is %s' % (self.name, self.nationality, self.__id))

    def get_and_print_id(self):
        print(self.__id)
        return self.__id

tom = Person('tom')
jack = Person('jack')
tom.nationality = 'India'
print(tom.nationality,jack.nationality)

del tom.nationality
Person.nationality='USA'
print(tom.nationality,jack.nationality)

'''
India China
USA USA
'''
#公有属性/静态属性 可以直接通过类直接访问，也可以直接通过实例进行访问；
#通过类的某个实例对公有属性进行修改，实际上对为该实例添加了一个与类的公有属性名称相同的成员属性，对真正的公有属性是没有影响的，因此它不会影响其他实例获取的该公有属性的值；
#通过类对公有属性进行修改，必然是会改变公有属性原有的值，他对该类所有的实例是都有影响的。
PS:
对于可变数据类型来说，例如列表。
对列表中的值进行修改不会改变列表的内存地址，只会改变内部元素的内存地址。不会影响从对象到类的指针。所以使用类和对象去修改是共享的，赋值是独立的。

tom.test.append(3)
print(Person.test,tom.test)
del tom.test[0]
print(Person.test,tom.test)
tom.test = [4,5,6]
print(Person.test,tom.test)

'''
[1, 2, 3] [1, 2, 3]
[2, 3] [2, 3]
[2, 3] [4, 5, 6]
'''
```

### 实例属性

```python
'''
成员属性，又称成员变量 或 实例属性，也就是说这些属性是 该类的每个实例对象单独持有的属性。成员属性需要在类的__init__方法中进行声明，比如上面的Person类中定义的name属性就是一个成员属性。
'''

- 成员属性可以直接通过实例对象来访问和更改；
- 成员属性是每个实例对象独有的，某个实例对象的成员属性被更改不会影响其他实例对象的相同属性的值；
- 成员属性的值不能通过类来访问和修改；
```

### 私有属性

```python
'''
私有属性和成员属性一样，是在__init__方法中进行声明，但是属性名需要以双下划线__开头，比如上面定义的Person中的__id属性。私有属性是一种特殊的成员属性，它只允许在实例对象的内部（成员方法或私有方法中）访问，而不允许在实例对象的外部通过实例对象或类来直接访问，也不能被子类继承。
'''
print(Person.__id)
print(tom.__id)
'''
AttributeError: 'Person' object has no attribute '__id'
'''

#访问方式
1 专门的成员方法返回该私有变量的值
tom.get_and_print_id()
2 通过 实例对象._类名__私有变量名 的方式来访问
print(tom._Person__id)

#私有变量不能通过类直接访问；
#私有变量也不能通过实例对象直接访问；
#私有变量可以通过成员方法进行访问。
```

### 小结

```python
公有属性、成员属性 和 私有属性 的受保护等级是依次递增的；
私有属性 和 成员属性 是存放在已实例化的对象中的，每个对象都会保存一份；
公有属性是保存在类中的，只保存一份；
哪些属性应该是公有属性的，哪些属性应该是私有属性 需要根据具体业务需求来确定。
```

### 举例说明

```python
1)
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

'''
日本
英国
英国
'''

2)#静态变量可变数据类型
class A:
    Country = ['中国']     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
a.Country[0] = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

'''
['日本']
['日本']
['日本']
'''

3) 实例变量的名字与静态变量无关
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
        self.Country = country
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

'''
日本
泰国
英国
'''

4)# a.Country属于动态变量，绑定在方法中
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def Country(self):
        return self.Country

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
print(a.Country)
print(a.Country())
'''
<bound method A.Country of <__main__.A object at 0x000001FE6F8B42E8>>
<bound method A.Country of <__main__.A object at 0x000001FE6F8B42E8>>
'''
```



## 组合

**组合：将一个类的对象封装到另一个类的对象的属性中，就叫组合。**

```python
基于圆形类实现一个圆环类,要求接收参数 外圆半径和内圆半径
# 完成方法 :计算环形面积和环形周长
# 要求,借助组合,要求组合圆形类的对象完成需求

from math import pi

class Circle:
    def __init__(self,r):
        self.r =r

    def area(self):
        area = pi * self.r ** 2
        return area

    def perimeter(self):
        perimeter = 2*pi*self.r
        return perimeter

class ring:
    def __init__(self,o_r,i_r):
        #使用三元表达式
        self.o_r,self.i_r = (o_r,i_r) if float(o_r) > float(i_r) else (i_r,o_r) 
        #outer_r,inner_r = (outer_r,inner_r) if outer_r > inner_r else (inner_r,outer_r)
        self.o_c = Circle(self.o_r)
        self.i_c = Circle(self.i_r)

    def area(self):
        area = self.o_c.area() - self.i_c.area()
        return area

    def peri(self):
        peri = self.o_c.perimeter() - self.i_c.perimeter()
        return  peri

r1 = ring(10,121)
print(r1.area() ,r1.o_r)
```

## 作业

```python
# 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
# 登陆成功之后才创建用户对象
# 设计一个方法 修改密码
        
import os
def login(username,passwd,filepath='userinfo'):
    with open(filepath,encoding='utf-8') as f1:
        for line in f1:
            user,pwd = line.strip().split('|')
            if username == user and passwd == pwd:
                return True
        else:
            return False

class User:
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd

    def change_pwd(self):
        oldpwd = input("请输入原密码：").strip()
        newpwd = input("请输入新密码：").strip()

        flag = False
        with open('userinfo',encoding='utf-8') as f1 ,open('userinfo.bak','w',encoding='utf-8') as f2:
            for line in f1:
                user,pwd = line.strip().split('|')
                if self.username == user and oldpwd == pwd and self.passwd == oldpwd :
                    line = "{}|{}\n".format(self.username,newpwd)
                    flag = True
                f2.write(line)

        os.remove('userinfo')
        os.rename('userinfo.bak','userinfo')
        return  flag


if __name__ == '__main__':
    username = input("请输入用户名：").strip()
    passwd = input("请输入密码：").strip()

    if login(username,passwd):
        print('登录成功')
        obj = User(username,passwd)
        if obj.change_pwd():print("密码修改成功")        
```

