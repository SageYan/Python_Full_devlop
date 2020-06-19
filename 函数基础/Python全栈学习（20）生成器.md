[TOC]

# Python全栈学习（20）生成器

## 初识

生成器：python社区，生成器与迭代器看成是一种，生成器的本质就是迭代器。

区别：迭代器都是Python给你提供的已经写好的工具或者通过数据转化得来的，（比如文件句柄，iter([1,2,3])。生成器是需要我们自己用python代码构建的工具。

## 创建生成器的三种方式

1. 通过生成器函数

2. 通过生成器推导式

　　3. python内置函数或者模块提供（其实1,3两种本质上差不多，都是通过函数的形式生成，只不过1是自己写的生成器函数，3是python提供的生成器函数而已）

### 生成器函数

```python
def gen():
    print('start:')
    yield 'sage'
    print("Hi booboo")
    yield 'Hi Sage'
    print("Hi Amy")
    yield 'HAHA'

ret = gen()
print(next(ret))
print(next(ret))
print(next(ret))
#当程序运行完最后一个yield,那么后面继续运行next()程序会报错，一个yield对应一个next，next超过yield数量，就会报错，与迭代器一样。
```

#### yield与return的区别

​    return一般在函数中只设置一个，他的作用是终止函数，并且给函数的执行者返回值。

​    yield在生成器函数中可设置多个，他并不会终止函数，next会获取对应yield生成的元素。

#### 练习题

```python
#普通函数，占用内存
def baozi():
    l1 = []
    for i in range(1,5001):
        l1.append('包子{}号'.format(i))
    return l1
ret = baozi()
print(ret)

#生成器函数，惰性取值,而且还可以保留上次的位置。
def gen_baozi():
    for i in range(1, 5001):
        yield '包子{}号'.format(i)
ret2=gen_baozi()

for num in range(200):
    print(next(ret2))
```

#### yield from

```python
#yield from 将l1这个列表变成了迭代器返回
def test():
    l1 = [1,2,3,4,5,]
    yield from l1 
ret = test()
print(ret)
print(next(ret))
print(next(ret))
print(next(ret))
'''
<generator object test at 0x000002594A4CC150>
1
2
3
'''

def func():
    lst1 = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
    lst2 = ['馒头', '花卷', '豆包', '大饼']
    yield from lst1
    yield from lst2

g = func()
for i in g:
    print(i)
```

#### send()

**send和next()区别:**

​    相同点：

​      send 和 next()都可以让生成器对应的yield向下执行一次。

​      都可以获取到yield生成的值。

​    不同点：

​      第一次获取yield值只能用next不能用send（可以用send(None)）。

​      send可以给上一个yield置传递值。

```python
def gen(name):
    print('{} ready to eat'.format(name))
    while 1:
        food = yield
        print('{} start to eat {}'.format(name,food))

dog = gen('alex')

# 还可以给上一个yield发送值
next(dog) # 第一次必须用next让指针停留在第一个yield后面
dog.send('骨头')
dog.send('狗粮')
dog.send('香肠')

'''
alex ready to eat
alex start to eat 骨头
alex start to eat 狗粮
alex start to eat 香肠
'''
```

### 生成器推导式

#### 列表推导式

**列表推导式分为两种模式：**

  1.循环模式：[变量(加工的变量) for 变量 in iterable]

  2.筛选模式: [变量(加工的变量) for 变量 in iterable if 条件]

```python
#循环模式
print([i**2 for i in range(2,11,2)])
print(['python{}期'.format(i) for i in range(1,101)])

#筛选模式
print([i for i in range(1, 31) if i % 3 == 0])

l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
print([i for i in l if len(i) >= 3])

names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
print([i for lst in names for i in lst if i.count('e') == 2])
```

#### 生成器表达式

生成器表达式和列表推导式的语法上一模一样,只是把 [] 换成 () 就行了

```python
gen = (i**2 for i in range(3000) if i%7 == 5)
print(gen)

print(next(gen))
print(next(gen))
```

**生成器表达式和列表推导式的区别**

```json
1 列表推导式比较耗内存,所有数据一次性加载到内存。而.生成器表达式遵循迭代器协议，逐个产生元素。
2 得到的值不一样,列表推导式得到的是一个列表.生成器表达式获取的是一个生成器
3 列表推导式一目了然，生成器表达式只是一个内存地址。
```

#### 字典推导式

```python
lst1 = ['jay','jj','meet']
lst2 = ['周杰伦','林俊杰','郭宝元']
dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
print(dic)

#{'jay': '周杰伦', 'meet': '郭宝元', 'jj': '林俊杰'}
```

#### 集合推导式

```python
lst = [1,2,3,-1,-3,-7,9]
s = {abs(i) for i in lst} #abs 去负号
print(s)
```

