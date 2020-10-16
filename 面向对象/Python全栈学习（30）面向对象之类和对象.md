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

## 类命名空间与对象、实例的命名空间