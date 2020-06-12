[toc]



# Python全栈学习（17）默认参数，局部作用域补充，以及global nonlocal关键字

## 默认参数补充

默认参数指向的是可变的数据类型，无论修改多少次这个默认参数，都是针对同一（**结构性数据+指针数组**）。除非指向新的（**结构性数据+指针数组**）。

```python
def func(a, list= []):
    list.append(a)
    return list
ret1 = func(10,)  # ret = [10,]
ret2 = func(20,[])  # [20,]
ret3 = func(100,)  # ret3 = [10,100]
print(ret1)  # [10,100] 此**结构性数据+指针数组**所指向的内容，调用函数两次，被修改两次
print(ret2)  # [20,]
print(ret3)  # [10,100]
```

## 局部作用域补充

1. 在函数中，如果你定义了一个变量，但是在定义这个变量之前对其引用了，那么解释器认为：语法问题。你应该在使用之前先定义。
2. 局部作用域对全局作用域的变量（此变量只能是不可变的数据类型）只能进行引用，而不能进行改变

```python
count = 1
def cou():
    #print(count) #放开，不报错
    #count = 3 #放开 报错 没定义
    #count = count +1 同上
    return count #不报错
#cou()
print(cou())
```

## global关键字

作用：

1. 在局部作用域声明一个全局变量
2. 修改一个全局变量

```python
#在局部作用域声明一个全局变量
def func():
    global a
    a = 3
func()
print(a)

#修改一个全局变量
count = 1
def search():
    global count
    count = 2
search()
print(count)
```

## nonlocal关键字

1. 不能够操作全局变量
2. 局部作用域：内层函数对外层函数的局部变量进行修改

```python
#局部作用域：内层函数对外层函数的局部变量进行修改。
 def wrapper():
     count = 1
     def inner():
         nonlocal count
         count += 1
     print(count) #1
     inner() #修改外层变量
     print(count) #2
 wrapper()
```

