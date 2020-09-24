[TOC]

# Python全栈学习（27）函数递归

## 什么是递归

```python
#如果一个函数在内部调用自身本身，这个函数就是递归函数

def cal(n):
    if n == 1:
        return n
    else:
        return n + cal(n-1)
    
ret = cal(5)
print(ret)

递归的特性：

　　1、递归函数必须有一个明确的结束条件。
　　2、每进入更深一层的递归时，问题规模相对于上一次递归都应减少
　　3、相邻两次重复之间有紧密的联系，前一次要为后一次做准备（通常前一次的输出就作为后一次的输入）。
　　4、递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）
```

## 递归函数优缺点

```python
　　#递归函数的优点：定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
　　#递归函数的缺点：使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
```

### 如何修改递归的最大深度

```python
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

#2000
```

## 递归函数练习

```python
1 阶乘
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(7))


2 os模块:查看一个文件夹下的所有文件
import os
def show_dir(path):
    res = os.listdir(path)
    for i in res:
        abs_path = os.path.join(path,i)
        if os.path.isdir(abs_path):
            show_dir(abs_path)
        else:
            print(abs_path)
show_dir(r'E:\sagepy\env')

#利用walk
def showdir(path):
    for a, b, c in os.walk(path):  # a代表所在根目录;b代表根目录下所有文件夹(以列表形式存在);c代表根目录下所有文件
        for i in c:
            print(i)
showdir(r'E:\sagepy\env')


3 os模块:计算一个文件夹下所有文件的大小
#利用walk
def walk_dir_size(path):
    '''
    使用os.walk获取文件大小
    :param path: 文件路径
    :return: 文件大小
    '''
    import os
    ret = os.walk(path)#返回一个对象
    file_size = 0 #初始化文件大小为零
    for base_path,dir_list,file_list in ret:
        '''
        base_path:文件路径
        dir_list：文件夹列表
        file_list：文件列表
        '''
        for file_name in file_list:
            file_path = os.path.join(base_path,file_name)
            size = os.path.getsize(file_path)
            file_size += size
    return file_size

ret = walk_dir_size('E:\\')
print(ret)

#利用递归函数
import os
def dir_size(path):
    size = 0
    dir_lst = os.listdir(path)

    for name in dir_lst:
        abs_path = os.path.join(path,name)
        if os.path.isfile(abs_path):
            size += os.path.getsize(abs_path)

        else:
            size += dir_size(abs_path)
    return size

print(dir_size(r'E:\sagepy\env'))

4 fibonacci数列
#直观，效率低下
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#在函数返回的时候，调用自身本身《不能包含表达式，上式中含有+表达式》，提升效率
def fibonacci(n, a=1, b=1):
    if n <= 2:
        return b
    else:
        a, b = b, a + b
        return fibonacci(n - 1, a, b)
#循环，效率最高
def fibonacci(n):
    a, b = 1, 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b
```

### 递归说明举例

```python
#遍历此三级菜单，输入b返回上级菜单，输入q退出
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


def read_menu(dic):
    flag = True
    while flag:
        for loc in dic:
            print(loc)
        key = input(">>>").strip()
        if dic.get(key):
            dic = dic.get(key)
            flag = read_menu(dic)
        elif key.upper() == "B": 
            return True
        elif key.upper() == "Q":
            return False

def menu_func(menu):
    while True:
        for name in menu:
            print(name)
        key = input('>>>').strip()  
        if menu.get(key):
            dic = menu[key]
            flag = menu_func(dic)    
            if not flag: return False
        elif key.upper() == 'B': return True
        elif key.upper() == 'Q': return False
PS：
递推：像上边递归实现所拆解，递归每一次都是基于上一次进行下一次的执行，这叫递推
回溯：则是在遇到终止条件，则从最后往回返一级一级的把值返回来，这叫回溯
# 很容易理解 最内层函数判断条件为B 返回True到外层，外层函数再次执行。执行结果就是返回上级菜单
```

## 



