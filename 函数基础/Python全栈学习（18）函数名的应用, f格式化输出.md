[TOC]



# Python全栈学习（18）函数名的应用, f格式化输出

## 函数名

### 1 函数名指向的是函数的内存地址

```python
def func(a,b):
    return  a + b

print(func,type(func))
#<function func at 0x000001BAD8CAD1E0> <class 'function'>
```

### 2 函数名就是变量（风湿理论）

```python
def func():
    print('in func')

def func1():
    print('in func1')

func1 = func
func1() #in func
```

### 3 函数名可以作为容器类数据类型的元素

```python
def func1():
    print('in func1')

def func2():
    print('in func2')

def func3():
    print('in func3')

l1 = [func1,func2,func3]
for i in l1:
    i()
```

### 4 函数名可以作为函数的参数

```python
def func1():
    print('in func1')

def func2(f):
    print('in func2')
    f()

func2(func1)
#in func2
#in func1
```

### 5 函数名可以作为函数的返回值

```python
def func1():
    print('in func1')

def func2(f):
    print('in func2')
    return f

ret = func2(func1)
ret()  # ret, f, func1 都是指向的func1这个函数的内存地址
```

## f-strings格式化输出

```python
# %s format
name = '太白'
age = 18
msg = '我叫%s,今年%s' %(name,age)
msg1 = '我叫{},今年{}'.format(name,age)

# 新特性：格式化输出
msg = f'我叫{name},今年{age}'
'''
#可以加表达式
dic = {'name':'alex','age': 73}
msg = f'我叫{dic["name"]},今年{dic["age"]}'
print(msg)

count = 7
print(f'最终结果：{count**2}')

# 结合函数写：
def _sum(a,b):
    return a + b
msg = f'最终的结果是：{_sum(10,20)}'
print(msg)
''' 
注意：
# ! , : { } ;这些标点不能出现在{} 这里面。
```

