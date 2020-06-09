[TOC]

# Python全栈学习（16）名称空间，作用域与高阶函数

## 名称空间

```python
python分为三个空间：
# 内置名称空间（builtins.py）
# 全局名称空间（当前py文件）
# 局部名称空间（函数，函数执行时才开辟）
'''
三个空间的加载顺序为：
内置命名空间(程序运行伊始加载)->全局命名空间(程序运行中：从上到下加载)->局部命名空间(程序运行中：调用时才加载

取值顺序（就近原则）LEGB原则 单向不可逆
'''
```
## 作用域

### 作用域就是作用范围, 按照生效范围来看分为全局作用域和局部作用域

```python
# 全局作用域 ：内置名称空间 全局名称空间
# 局部作用域：局部名称空间

1. 局部作用域可以引用全局作用域的变量
day = "Friday"
def foo():
    a = 666
    print(day)
#print(a) #报错，无法打印局部变量
foo()

2. 局部作用域不能改变全局变量(包括外层变量)
count = 1
def foo():
    count += 1
    print(count)

foo()
#报错，local variable 'count' referenced before assignment
```


## globals()   locals()

```python
a = 1
b = 2
def func():
    name = 'alex'
    age = 73
    print(globals())  # 返回的是字典：字典里面的键值对：全局作用域的所有内容。
    print(locals())  # 返回的是字典：字典里面的键值对：当前作用域的所有的内容。

func()
'''
{'__cached__': None, '__doc__': None, '__spec__': None, '__package__': None, 'b': 2, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001536F395AC8>, '__name__': '__main__', '__file__': 'E:/sagepy/env/20200609/area.py', '__builtins__': <module 'builtins' (built-in)>, 'foo': <function foo at 0x000001536F3FD1E0>, 'a': 1}

{'name': 'Sage'}
'''
```

## 高阶函数

```python
1 name = "刚娘"

2 def weihou():
    4.1 name = "陈卓"
    4.2 def weiweihou():
        	4.3.1 nonlocal name   # nonlocal，指定上一级变量，如果没有就继续往上直到找到为止
        	4.3.2 name = "冷静"

    4.3 weiweihou()
    4.4 print(name)  --nonlocal 冷静

3 print(name)  --刚娘
4 weihou()  --调用内存函数代码
5 print(name) --刚娘
# 刚娘
# 冷静
# 刚娘

'''
global关键字有两个作用：
1 声明一个全局变量
2 在局部作用域想要对全局作用域的全局变量进行修改时，需要用到 global(限于字符串，数字)

nonlocal的总结：
1 不能更改全局变量。
2 在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，并且引用的哪层，从那层及以下此变量全部发生改变
'''
```

