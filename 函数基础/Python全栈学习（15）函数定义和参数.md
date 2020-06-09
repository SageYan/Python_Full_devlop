[TOC]



# Python全栈学习（15）函数定义和参数

## 函数的初识

+ 函数：以功能（完成一件事）为导向，登录，注册，len，一个函数就是一个功能， 随调随用
+ 函数的优点：
  + 减少代码的重复性
  + 增强了代码的可读性

## 函数的结构与调用

```python
def meet():
    print('打开tantan')
    print('左滑一下')
    print('右滑一下')
    print('找美女')
    print('悄悄话....')
    print('约....走起...')
meet()
meet()
meet()
```

+ 结构： def 关键字，定义函数。
      meet 函数名：与变量设置相同，具有可描述性。
      函数体 ：缩进。函数中尽量不要出现 print

+ 函数什么时候执行？
  + 当函数遇到      **函数名()**  函数才会执行 !

## 函数的返回值

### return 在函数中遇到return直接结束函数

```python
def meet():
    print('打开tantan')
    print('左滑一下')
    print('右滑一下')
    print('找美女')
    return '妹子一枚'
    print('悄悄话....')
    print('约....走起...')
    
meet() #将数据返回给函数的执行者，调用者 meet()
'''
结果：
打开tantan
左滑一下
右滑一下
找美女
'''

```

### return 返回多个元素 是以元组的形式返回给函数的执行者

```python
def meet():
    print('打开tantan')
    print('左滑一下')
    print('右滑一下')
    print('找美女')
    return '妹子一枚' ,[2,3],{1,2,3,4}
    print('悄悄话....')
    print('约....走起...')


ret = meet()
print(ret,type(ret))
'''
结果：
打开tantan
左滑一下
右滑一下
找美女
('妹子一枚', [2, 3], {1, 2, 3, 4}) <class 'tuple'>
'''
```

### 总结

```powershell
1.遇到return,函数结束,return下面的（函数内）的代码不会执行。
2.return 会给函数的执行者返回值:
如果return后面什么都不写，或者函数中没有return,则返回的结果是None
如果return后面写了一个值,返回给调用者这个值
如果return后面写了多个结果,返回给调用者一个tuple(元组),调用者可以直接使用元组的解构获取多个变量。
```

## 函数参数

```python
函数的参数可以从两个角度划分：
1.形参
写在函数声明的位置的变量叫形参,形式上的一个完整.表示这个函数需要xxx
2.实参
在函数调用的时候给函数传递的值.加实参,实际执行的时候给函数传递的信息.表示给函数xxx

##函数的传参就是函数将实际参数交给形式参数的过程.
```

### 实参

#### 位置参数

位置参数就是从左至右，实参与形参一一对应,顺序一致

```python
def date(sex, age, hobby):

    print('设置筛选条件：性别: %s，年龄：%s,爱好：%s' %(sex, age, hobby))

date('女','25~30','唱歌')
date('人妖','20~25','萝莉音')

#三元运算符  简写简单的if...else...
def compare(a,b):
	return a if a > b else b

print(compare(0.1,0.199))
```

#### 关键字参数

要求一一对应，顺序不要求

```python
def date(sex, age, hobby):
    print("拿出手机")
    print("打开陌陌")
    print('设置筛选条件：性别: %s，年龄：%s,爱好：%s' %(sex, age, hobby))
    print("找个漂亮的妹子")
    print("问她,约不约啊!")
    print("ok 走起")
date(hobby='唱歌',sex='女',age='25~30',)
```

#### 混合参数

混合参数一定要记住：关键字参数一定在位置参数后面

```python
def meet(sex,age,skill,hight,weight,):
    print('进行筛选：性别：%s,年龄：%s,技术：%s,身高：%s,体重%s' %(sex,age,skill,hight,weight))
    return '筛选结果：性别：%s,体重%s' %(sex,weight)

print(meet('女',25,weight=100,hight=174,skill='python技术好的'))
```

### 形参

#### 位置参数

位置参数其实与实参角度的位置参数是一样的，就是按照位置从左至右，一一对应

#### 默认参数

注意:必须先声明在位置参数,才能声明关键字参数

```python
#在函数声明的时候, 就可以给出函数参数的默认值. 默认值参数一般是这个参数使用率较高，才会设置默认值参数

def stu_info(name, age, sex='男'):
    print("录入学生信息")
    print(name, age, sex)
    print("录入完毕")

stu_info("张强", 18)
```

#### 万能参数

动态参数分为两种:动态接受位置参数 *args，动态接收关键字参数**kwargs

##### *args

```python
#函数定义时，*代表聚合。 他将所有的位置参数聚合成一个元组，赋值给了 args
def eat(*args):
    print(args)
    print('我请你吃：%s,%s,%s,%s,%s,%s' % args)

eat('蒸羊羔', '蒸熊掌', '蒸鹿邑','烧花鸭','烧雏鸡','烧子鹅')
#传入函数中数量不定的int型数据，函数计算所有数的和并返回
def my_sum(*args):
    return sum(args)

print(my_sum(1,2,3,4,5))
```

##### **kwargs

```python
# 函数的定义时： ** 将所有的关键字参数聚合到一个字典中，将这个字典赋值给了kwargs.
def func(**kwargs):
    print(kwargs)
func(name='alex',age=73,sex='laddyboy')
#{'age': 73, 'name': 'alex', 'sex': 'laddyboy'}
```

#### 仅限关键字参数

仅限关键字参数是python3x更新的新特性，他的位置要放在*args后面，**kwargs前面（如果有**kwargs），也就是默认参数的位置，它与默认参数的前后顺序无所谓，它只接受关键字传的参数：

```python
def func(a,b,*args,sex='male',c,**kwargs):
    print(a,b)
    print(args)
    print(sex)
    print(c)
    print(kwargs)

func(1,2,3,4,sex='female',name='Boo',c='enter',age=30)
'''
1 2
(3, 4)
female
enter
{'age': 30, 'name': 'Boo'}
'''
#形参角度最终的顺序：位置参数,*args,默认参数，仅限关键字参数，**kwargs
```



#### *的作用

##### 函数定义中，*起到聚合的作用

##### 函数调用时，*起到打散作用

```python
s1 = "SAGE"
l1 = ['sage','boo','amy']
tu1 = ('a', 'good', 'person',)
dic1 = {'name':'sage', 'hobby':'IT', 'wife':'Booboo'}
dic2 = {'gril':'Amy', 'study':'English', 'height':110}

def stars(*args, **kwargs):
    print(args)
    print(kwargs)

stars(*s1,*l1,*tu1,**dic1,**dic2)

#('S', 'A', 'G', 'E', 'sage', 'boo', 'amy', 'a', 'good', 'person')
#{'wife': 'Booboo', 'name': 'sage', 'study': 'English', 'height': 110, 'gril': 'Amy', 'hobby': 'IT'}
```

##### *处理剩余的元素

```python
a,*_,b=[1,2,3,4,5,90,100]
print(a,b)

#1 100
```

#### 形参角度的参数的顺序

##### 形参角度最终的顺序：位置参数,*args,默认参数，仅限关键字参数，**kwargs

