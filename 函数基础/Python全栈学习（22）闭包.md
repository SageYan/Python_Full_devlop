[TOC]



# Python全栈学习（22）闭包

## **闭包的定义**

1. 闭包是嵌套在函数中的函数。

2. 闭包必须是内层函数对外层函数的变量（非全局变量）的引用。

```python
# 被引用的非全局变量也称作自由变量，这个自由变量会与内层函数产生一个绑定关系，
# 自由变量不会在函数调用之后，从内存中消失。
# 闭包的作用：保证数据的安全。
```

例子：

```python
def make_avg():
    l1 = []  
    def inner_avg(newvalue):
        l1.append(newvalue)   #l1 自由变量
        return sum(l1)/len(l1)  
    return inner_avg
test = make_avg()             #inner_avg
print(test(101))
print(test(102))
print(test(1000))

'''
    l1 = []    
    def inner_avg(newvalue):
        l1.append(newvalue)   #l1 自由变量
        return sum(l1)/len(l1)  
    return inner_avg
**这一部分叫做闭包，l1称之为自由变量**
'''
```

## 闭包的判断方法

### "\__code__.co_freevars"

```python
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager
avg = make_averager()
avg(100)
avg(102)
#1. 查看函数的自由变量
print(avg.__code__.co_freevars) #('series',)
#2. 查看函数的局部变量
print(avg.__code__.co_varnames) #('new_value', 'total')

#3. cell_contents 自由变量具体的值
print(avg.__closure__[0].cell_contents) #[100, 102]
```

