[TOC]

# 迭代器和生成器

## 迭代器

### 迭代器协议

```
迭代器协议是指：对象必须提供一个next方法，执行该方法要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代 （只能往后走不能往前退）。

协议是一种约定，可迭代对象实现了迭代器协议，python的内部工具（如for循环，sum，min，max函数等)使用迭代器协议访问对象。
```

### 可迭代对象

```
可迭代对象：实现了迭代器协议的对象（如何实现：对象内部定义一个__iter__()方法）
```



### for循环机制

```
for循环的本质：循环所有对象，全都是使用迭代器协议。
for循环就是基于迭代器协议提供了一个统一的可以遍历所有对象的方法，即在遍历之前，先调用对象的__iter__方法将其转换成一个迭代器，然后使用迭代器协议去实现循环访问，这样所有的对象就都可以通过for循环来遍历了。

值得注意的是：
列表，字符串，元组，字典，集合，文件对象等本质上来说都不是可迭代对象，在使用for循环的时候内部是先调用他们内部的__iter__方法，使他们变成了可迭代对象。
然后在使用可迭代对象的_next_方法依次循环元素，当元素循环完时，会触发StopIteration异常，for循环会捕捉到这种异常，终止迭代。
```



```python
for循环 工作机制
例子：
#  先调用__iter__方法   i_l=l.__iter_()  再调用__next__方法 i_l.__next__()

x='hello'
print(dir(x))  #没有__next__方法
iter_test=x.__iter__()

print(iter_test)
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())

#结果
C:\Users\yancong\.virtualenvs\hellobooboo\Scripts\python.exe C:/Users/yancong/PycharmProjects/yancong/file_b.py
Traceback (most recent call last):
  File "C:/Users/yancong/PycharmProjects/yancong/file_b.py", line 11, in <module>
    print(iter_test.__next__())
StopIteration
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
<str_iterator object at 0x0000024192A770C8>
h
e
l
l
o

Process finished with exit code 1

```

### 可进行for循环访问的对象的三种访问方式以及其局限

```python
#for循环访问
l=[1,2,3]
for i in l:  #i_l=l.__iter_()  i_l.__next__()
    print(i)

#索引访问 对集合,字典，文件等无需对象无法访问
index=0
while index < len(l):
    print(l[index])
    index+=1

#迭代器协议访问
iter_l=l.__iter__() #遵循迭代器协议，生成可迭代对象
print(iter_l.__next__())
print(iter_l.__next__())

--对文件的可迭代协议访问--
f=open('test1','r+')
iter_f=f.__iter__()
print(iter_f)
print(iter_f.__next__(),end='')
print(iter_f.__next__(),end='')

##结果##
<_io.TextIOWrapper name='test1' mode='r+' encoding='cp936'>
dadas
adsada



#用while去模拟for循环做的事情
l = {1,2,4}
diedai_l=l.__iter__()
while True:
    try:
        print(diedai_l.__next__())
    except StopIteration:
        print('迭代完毕了,循环终止了')
        break
##结果##
1
2
4
迭代完毕了,循环终止了
```





## 生成器

### 什么是生成器

```python
生成器类似于一种数据类型，这种数据类型自动实现了迭代器协议（其他的数据类型需要调用自己内置的__iter__方法），所以生成器就是可迭代对象



生成器分类及在python中的表现形式：（Python有两种不同的方式提供生成器）

1.生成器函数：常规函数定义，但是，使用yield语句而不是return语句返回结果。yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次重它离开的地方继续执行
2.生成器表达式：类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表，按需取出对象


##优点
Python使用生成器对延迟操作提供了支持。所谓延迟操作，是指在需要的时候才产生结果，而不是立即产生结果。这也是生成器的主要好处。
```

### 生成器函数

```python
def test():
    yield 1
    yield 2
    yield 3
g=test()
print('来自函数',g)
# print(g.__next__())
# print(g.__next__())

#结果
来自函数 <generator object test at 0x000001FC95960C48>


def test():
    for i in range(7):
        yield i

t = test()
#yield的唤醒方式
print(t.__next__())
print(t.send('hahahah'))
print(next(t))

```

### 生成器表达式

```python
#三元表达式
name='alex'
name='linhaifeng'
res='SB' if name == 'alex' else '帅哥'
print(res)

#列表解析
egg_list = []
for i in range(10):
    egg_list.append('鸡蛋%s' % i)
print(egg_list)


l=['鸡蛋%s' %i for i in range(10)]
l1=['鸡蛋%s' %i for i in range(10) if i > 5 ]
# l1=['鸡蛋%s' %i for i in range(10) if i > 5 else i] #没有四元表达式
l2=['鸡蛋%s' %i for i in range(10) if i < 5] #没有四元表达式


#生成器表达式
laomuji = ('鸡蛋%s' % i for i in range(10) )
print(laomuji)
print(laomuji.__next__())
print(laomuji.__next__())
print(laomuji.__next__()) 
```

### 生成器表达式优点举例

```python
l=[1,2,3,34]


# print(sum(l))  #l列表直接加载到内存，内存使用效率下降

## 使用生成器表达式
# print(sum())
# print(sum(i for i in range(10000000000000)))   #(i for i in range(10000000000000)) 生成器表达式 不会直接加载列表到内存

```

