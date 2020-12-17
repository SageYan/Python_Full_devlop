[TOC]



# Python全栈学习（29）面向对象思想初识

## 楔子

```python
'''
使用函数模拟【面向对象】的思维方式
'''

def Person(name, gender, job, hp, weapon, ad, level=0):
    def rub(dog): #定义一个内部有归属的函数
        dog['hp'] -= dic['ad']
        print('{}攻击了{}，{}掉了{}血'.format(dic['name'], dog['name'], dog['name'], dic['ad']))

    dic = {
        'name': name,
        'gender': gender,
        'job': job,
        'hp': hp,
        'weapon': weapon,
        'ad': ad,
        'skill': rub,
    }

    return dic


def Dog(name, kind, hp, ad):
    def bite(person):
        person['hp'] -= dic['ad']
        print('{}攻击了{}，{}掉了{}血'.format(dic['name'], person['name'], person['name'], dic['ad']))

    dic = {
        'name': name,
        'hp': hp,
        'kind': kind,
        'ad': ad,
        'skill': bite,
    }

    return dic


alex = Person('alex', 'male', '搓澡工', 250, '搓澡巾', 1)
little = Dog('little', '泰迪', 400, 100)

alex['skill'](little)

'''
alex攻击了little，little掉了1血
'''
```

## 面向对象的概念

### "面向对象（OOP）"是什么？

```scala
常见的编程范式有：
面向过程编程：OPP（Procedure Oriented Programing）
面向对象编程：OOP（Object Oriented Programing）
函数式编程：(Functional Programing)

面向过程编程的步骤：
1）分析出解决问题所需要的步骤；
2）用函数把这些步骤一次实现；
3）一个一个地调用这些函数来解决问题；

面向对象编程的步骤：
1）把构成问题的事务分解、抽象成各个对象；
2）结合这些对象的共有属性，抽象出类；
3）类层次化结构设计--继承 和 合成；
4）用类和实例进行设计和实现来解决问题。
```

### 面向对象编程的特点

```python
面向对象编程达到了软件工程的3个目标：重用性、灵活性、扩展性，而这些目标是通过以下几个主要特点实现的：

封装： 可以隐藏实现细节，使代码模块化
继承： 可以通过扩展已存在的类来实现代码重用，避免重复编写相同的代码
多态： 封装和继承的目的都是为了实现 代码重用， 而多态是为了实现 接口重用，使得类在继承和派生的时候能够保证任何一个类的实例都能正确调用约定好的属性和方法。简单来说，就是为了约定相同的属性和方法名称
```

### 面向对象编程的使用场景

```python
我们知道，Python既可以面向过程编程，也可以面向对象编程。那么什么场景下应该使用面向对象编程呢？如果我们仅仅是写一个简单的脚本来跑一些简单的任务，我们直接用面向过程编程就好了，简单，快速。当我们需要实现一个复杂的系统时，或者以下场景下，就需要使用面向对象编程：

场景1： 当多个函数需要传入多个共同的参数时，可以将这些函数封装到一个类中，并将这些参数提取为这个类的属性；
场景2： 当需要根据一个模板来创建某些东西时，可以通过类来完成。
```
