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

#### 子类想要调用父类的方法的同时还想执行自己的同名方法 :父类名.方法名(self) 或  super().func(参数) 

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

