[TOC]

# Python全栈学习（19）迭代器

## 可迭代对象

### 定义

**在python中，但凡内部含有__iter__方法的对象，都是可迭代对象**

### 判断方法

```python
s1 = 'Sage is a good man'
print("__iter__" in dir(s1))
```

### 小结

- 字面意思：可以进行循环更新的一个实实在在值。

- 专业角度： 内部含有`'__iter__'`方法的对象，可迭代对象。

- 判断一个对象是不是可迭代对象： `'__iter__'`  in dir(对象)

- str list tuple dict set range 等都是可迭代对象

- 优点：

  1. 存储的数据直接能显示，比较直观。
  2. 拥有的方法比较多，操作方便。

- 缺点：

  1. 占用内存。
  2. 可迭代对象不能迭代取值（除去索引，key以外）。

  #需要先将可迭代对象转化成迭代器，然后再进行取值

## 迭代器

### 定义

**在python中，内部含有'__Iter__'方法并且含有'__next__'方法的对象就是迭代器。**

### 判断该对象是否是迭代器

```python
with open('文件1',encoding='utf-8',mode='w') as f1:
    print(('__iter__' in dir(f1)) and ('__next__' in dir(f1)))
```

### 使用内置函数iter() 或者 对象方法__iter__把可迭代对象转换成迭代器

```python
l1 = [1, 2, 3, 4]
obj = iter(l1)
obj2 = l1.__iter__()
print(type(obj),type(obj2))

#<class 'list_iterator'> <class 'list_iterator'>
```

### 迭代器的取值:next()

```python
l2 = ["sage" ,30 , "MASTER"]
itor = iter(l2)
print(next(itor))
print(next(itor))
print(next(itor))

'''
sage
30
MASTER
'''
```

### while循环模拟for循环机制

```python
l1 = [11,22,33,44,55,66,77,88,99,1111,1133,15652]
l1_iter = iter(l1)
while 1:
    try:
        print(next(l1_iter))
    except StopIteration:
        break
```

### 可迭代对象与迭代器的对比

```python
-  可迭代对象是一个操作方法比较多，比较直观，存储数据相对少（几百万个对象，8G内存是可以承受的）的一个数据集。
-  当你侧重于对于数据可以灵活处理，并且内存空间足够，将数据集设置为可迭代对象是明确的选择。
-  是一个非常节省内存，可以记录取值位置，可以直接通过循环+next方法取值，但是不直观，操作方法比较单一的数据集。
-  当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择。
```

### 小结

+ 字面意思：更新迭代，器：工具：可更新迭代的工具。
+ 专业角度：内部含有`'__iter__'`方法并且含有`'__next__'`方法的对象就是迭代器。
+ 优点：
  1. 节省内存。
  2. 惰性机制，next一次，取一个值。
+ 缺点：
  + 速度慢。
  + 不走回头路。