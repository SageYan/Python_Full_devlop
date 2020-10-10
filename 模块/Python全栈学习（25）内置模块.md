[TOC]



# Python全栈学习（25）内置模块

## 常用内置模块

### random

```python
此模块提供了和随机数获取相关的方法：

- random.random():获取[0.0,1.0)范围内的浮点数
- random.randint(a,b):获取[a,b]范围内的一个整数
- random.uniform(a,b):获取[a,b)范围内的浮点数
- random.shuffle(x):把参数指定的数据中的元素打乱。参数必须是一个可变的数据类型。
- random.sample(x,k):从x中随机抽取k个数据，组成一个列表返回。
                         
eg:
import random
print(random.random())
print(random.randint(2,100))
print(random.uniform(1,2))

lst = [i for i in range(10)]
random.shuffle(lst)
print(lst)

print(random.sample((1,23,14,100,) ,3))
```

### time

```python
封装了获取时间戳和字符串形式的时间的一些方法。
time.time():获取时间戳
time.gmtime([seconds]):获取格式化时间对象:是九个字段组成的
time.localtime([seconds]):获取格式化时间对象:是九个字段组成的
time.mktime(t):时间对象 --transfer-- 时间戳
time.strftime(format[,t]):把时间对象格式化成字符串
time.strptime(str,format):把时间字符串转换成时间对象
    
eg:
import time
print(time.time())
print(time.gmtime(1596445126.8665192))
print(time.localtime(1596445126.8665192))

t1 = time.localtime(1596445126.8665192)
print(time.mktime(t1))

print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1200)))

print(time.strptime("2018-10-10 14:23:10", "%Y-%m-%d %H:%M:%S"))

'''
1596446532.4223676
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=3, tm_hour=8, tm_min=58, tm_sec=46, tm_wday=0, tm_yday=216, tm_isdst=0)
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=3, tm_hour=16, tm_min=58, tm_sec=46, tm_wday=0, tm_yday=216, tm_isdst=0)
1596445126.0
2020-08-03 17:22:12
1970-01-01 08:20:00
time.struct_time(tm_year=2018, tm_mon=10, tm_mday=10, tm_hour=14, tm_min=23, tm_sec=10, tm_wday=2, tm_yday=283, tm_isdst=-1)
'''

```

### os

和操作系统相关的模块。主要是文件，目录的操作

```python
1 删除文件 重命名文件
import os
os.remove(r'E:\sagepy\env\20200731\cong.txt')
os.rename('aa','hello.txt')

2 删除目录，目录必须为空
os.removedirs(r'E:\sagepy\env\20200731\test')
#删除不为空的目录
import shutil
shutil.rmtree(r'E:\sagepy\env\20200731\tet2')

3 os.path
3.1 文件名与路径名的字符串操作
# 获取路径名，文件名，不判断存在否
print(os.path.dirname('/root/a/b/c/abc'))
print(os.path.basename('e:/a/b/c/text'))
#分割路径与文件 
print(os.path.split(r'E:\yanc\sage\test\1.py'))
#拼接路径
print(os.path.join('d:\\','world','I','am','Sage'))

'''
/root/a/b/c
text
('E:\\yanc\\sage\\test', '1.py')
d:\world\I\am\Sage
'''

3.2 文件的时间属性 与 绝对路径
print(os.path.getatime('exams.py')) #访问时间
print(os.path.getctime('exams.py')) #创建时间
print(os.path.getmtime('exams.py')) #修改时间
print(os.path.getsize(r'E:\sagepy\env\20200731\exams.py')) #文件大小
print(os.path.abspath('exams.py')) #不是以 / 开头,默认当前路径
print(os.path.abspath('/exams.py')) #/开头的路径,默认是在当前盘符下

'''
1596448541.496073
1596448541.496073
1596448541.496073
4896
E:\sagepy\env\20200731\exams.py
E:\exams.py
'''
3.3 判断
print(os.path.isabs('/sage.txt')) #不会确认存在否
print(os.path.isdir(r'E:\sagepy\env\20200731'))
print(os.path.isfile(r'E:\sagepy\env\20200731'))
print(os.path.exists(r'/hello.txt')) 

'''
True
True
False
False
'''
```

### sys

和解释器操作相关的模块
主要两个方面:
	解释器执行时获取参数: sys.argv[x]
	解释器执行时寻找模块的路径: sys.path

```python
'''
inner module.py 的内容如下
'''
import sys
print("脚本名:",sys.argv[0])      # 脚本名
print("第一个参数:",sys.argv[1])      # 第一个参数
print("第二个参数:",sys.argv[2])      # 第二个参数

print('\n\nPython 路径为：', sys.path, '\n')

#用脚本的方式运行 inner module.py
python "inner module.py" 'a'  'Amy'

结果：
'''
脚本名: inner module.py
第一个参数: 'a'
第二个参数: 'Amy'

Python 路径为： ['E:\\sagepy\\env\\20200731', 'D:\\software\\python35\\python35.zip', 'D:\\software\\python35\\DLLs', 'D:\\software\\python35\\lib', 'D:\\software\\python35', 'D:\\software\\python35\\lib\\site-packages']
'''

```

### json

```python
JavaScript Object Notation:java脚本兑现标记语言：
已经成为一种简单的数据交换格式。

序列化: 将其他数据格式转换成json字符串的过程
反序列化: 将json字符串转换其他数据类型的过程
    
#序列化模块就是将一个常见的数据结构转化成一个特殊的序列，并且这个特殊的序列还可以反解回去。它的主要用途：文件读写数据，网络传输数据。
```

```python
#用于网络传输：dumps loads

import json

dic1 = {'name':'sage', 'age':30, 'hobby':'sleep'}
str1 = json.dumps(dic1)
print(str1, type(str1))

dic2 = json.loads(str1)
print(dic2, type(dic2))
'''
{"name": "sage", "hobby": "sleep", "age": 30} <class 'str'>
{'name': 'sage', 'hobby': 'sleep', 'age': 30} <class 'dict'>
注意：
#集合 Object of type 'set' is not JSON serializable
'''

#用于文件写读：dump load

import json

with open('json.txt','wt',encoding='utf-8') as f1:
    json.dump([1,2,3],f1)

with open('json.txt','r',encoding='utf-8') as f2:
    res = json.load(f2)
print(res,type(res))

'''
[1, 2, 3] <class 'list'>
'''

#PS: json序列化存储多个数据到同一个文件中
#对于json序列化，存储多个数据到一个文件中是有问题的，默认一个json文件只能存储一个json数据，但是也可以解决:

import json

with open('json.txt', 'a', encoding='utf-8') as f3:
    f3.write(json.dumps([1, 2, 3, ]) + '\n', )
    f3.write(json.dumps({'name':'oldboy2'}) + '\n')
    f3.write(json.dumps([1, 'SAGE', 3, ]) + '\n')

import json

with open('json.txt', 'r', encoding='utf-8') as f4:
    #print(json.loads(f4.readline()))
    for x in f4:
        obj = json.loads(x.strip())
        print(obj,type(obj))
'''
[1, 2, 3] <class 'list'>
{'name': 'oldboy2'} <class 'dict'>
[1, 'SAGE', 3] <class 'list'>
'''
```

### pickle

```python
'''
只能是Python语言遵循的一种数据转化格式，只能在python语言中使用。
支持Python所有的数据类型包括实例化对象。
'''
1. 用于网络传输：dumps loads
import pickle
dic = {1:'sage', 2:'amy', 3:'Boo',}
b1 = pickle.dumps(dic)
print(b1,type(b1))

d1 = pickle.loads(b1)
print(d1,type(d1))
'''
b'\x80\x03}q\x00(K\x01X\x04\x00\x00\x00sageq\x01K\x02X\x03\x00\x00\x00amyq\x02K\x03X\x03\x00\x00\x00Booq\x03u.' <class 'bytes'>
{1: 'sage', 2: 'amy', 3: 'Boo'} <class 'dict'>
'''

#序列化函数对象
import pickle
def func1(name):
    return name

by1 = pickle.dumps(func1)
print(by1, type(by1)) #b'\x80\x03c__main__\nfunc1\nq\x00.' <class 'bytes'>

2. 用于文件写读：dump load
import pickle

name = 'SAGE'
hobby_list = ['reading', 'films', 'studying']
fa_dic = {'wife': 'boo', 'daughter': 'amy'}
mem_set = set('Hello')
#pickle可以多次对同一个文件序列化
with open('pickle.txt', mode='ab') as f1:
    pickle.dump(name, f1)
    pickle.dump(hobby_list, f1)
    pickle.dump(fa_dic, f1)
    pickle.dump(mem_set, f1)


import pickle
with open('pickle.txt','rb') as f2:
    print(pickle.load(f2))
    print(pickle.load(f2))
    print(pickle.load(f2))
    print(pickle.load(f2))
    print(pickle.load(f2)) #EOFError: Ran out of input
#优化：
with open('pickle.txt','rb') as f2:
    while True:
        try:
            print(pickle.load(f2))

        except EOFError:
            break
'''
SAGE
['reading', 'films', 'studying']
{'daughter': 'amy', 'wife': 'boo'}
{'H', 'e', 'o', 'l'}
'''
```



#### json,pickle的比较

```python
json:
1.不是所有的数据类型都可以序列化.结果是字符串.
2.不能多次对同一个文件序列化.
3.json数据可以跨语言

pickle:
1.所有python类型都能序列化,结果是字节串.
2.可以多次对同一个文件序列化
3.不能跨语言.
```

### hashlib

初识

```python
#加密和校验使用
特点：
1. bytes类型数据 ---> 通过hashlib算法 ---> 固定长度的字符串
2. 可以把一个大的数据,切分成不同块,分别对不同的块进行加密,再汇总的结果,和直接对整体数据加密的结果是一致的
3. 单向加密,不可逆
4. 原始数据的一点小的变化,将导致结果的非常大的差异,'雪崩'效应.
```

```python
#分片加密与整体加密结果相同
import hashlib

gmd5 = hashlib.md5()
gmd5.update('Sage'.encode('utf-8'))
gmd5.update('amy'.encode('utf-8'))
print(gmd5.hexdigest())

hmd5 = hashlib.md5()
hmd5.update("Sageamy".encode('utf-8'))
print(hmd5.hexdigest())
'''
ed3c1695843b8fe174a561f3b463637f
ed3c1695843b8fe174a561f3b463637f 
'''
#动态加盐，提高安全性
 '在创建加密对象时,可以指定参数,称为salt'
import hashlib

username = 'SageYanAmy Boo'
gmd5 = hashlib.md5(username[::2].encode('utf-8'))
gmd5.update("密码:123456".encode('utf-8'))
print(gmd5.hexdigest())

#校验版本
import hashlib
def file_check(file_path):
    with open(file_path,mode='rb') as f1:
        sha256 = hashlib.sha256()
        while 1:
            cont = f1.read(1024)
            if cont:
                sha256.update(cont)
            else:
                return sha256.hexdigest()

print(file_check('D:\software\python35\python.exe'))
```

#### 注册，登录程序与加密，校验

```python
def get_md5(username,passwd):
    m = hashlib.md5(username[::-1].encode('utf-8'))
    m.update(username.encode('utf-8'))
    m.update(passwd.encode('utf-8'))
    return m.hexdigest()


def register(username,passwd):
    # 加密
    res = get_md5(username,passwd)
    # 写入文件
    with open('login',mode='at',encoding='utf-8') as f:
        f.write(res)
        f.write('\n')

    # username:xxxxxx

def login(username,passwd):
    # 获取当前登录信息的加密结果
    res = get_md5(username, passwd)
    # 读文件,和其中的数据进行对比
    with open('login',mode='rt',encoding='utf-8') as f:
        for line in f:
            if res == line.strip():
                return True
        else:
            return False

while True:
    op = int(input("1.注册 2.登录 3.退出"))
    if op == 3 :
        break
    elif op == 1:
        username = input("输入用户名:")
        passwd = input("输入密码:")
        register(username,passwd)
    elif op == 2:
        username = input("输入用户名:")
        passwd = input("输入密码:")
        res = login(username,passwd)
        if res:
            print('登录成功')
        else:
            print('登录失败')
```

### collections

```python
1. namedtuple
from collections import namedtuple
#namedtuple('名称', [属性list])
rectangle = namedtuple('rectangle',['length','width'])
r = rectangle(10,18)
print(r,r.length,r[1])
'''
rectangle(length=10, width=18) 10 18
'''

2. defautldict
l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
mydic = {}
for x in l1:
    if x > 66:
        if "k1" not in mydic:
            mydic['k1'] = []#手动添加key以及对应的value
        mydic['k1'].append(x)
    else:
        if "k2" not in mydic:
            mydic['k2'] = []
        mydic['k2'].append(x)
print(mydic)



from collections import defaultdict
l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
#使用dict时，如果引用的Key不存在，就会抛出KeyError。
#如果希望key不存在时，添加该key值，并且赋予默认值，就可以用defaultdict。
my_dict = defaultdict(list, )
for x in l1:
    if x > 66:
        my_dict['k1'].append(x) 
    else:
        my_dict['k2'].append(x)
print(my_dict, type(my_dict))

3. Counter
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。

from collections import Counter
c = Counter([1,1,1,2,3,4,12,1,1,13])
print(c)
print(c.most_common(2))

'''
Counter({1: 5, 2: 1, 3: 1, 4: 1, 12: 1, 13: 1})
[(1, 5), (2, 1)]
'''
```

### shutil

```python
#shutil 主要用来处理操作系统文件，路径的复制，压缩，重命名，删除等操作
import shutil
#复制文件
shutil.copy2(r'E:\sagepy\env\20200924\execute.py',r'E:\sagepy\env\20200924\execute2.py')
#复制目录以及目录下的文件
shutil.copytree(r'E:\sagepy\env\20200731',r'E:\sagepy\env\20200294\0731',ignore=shutil.ignore_patterns('*.py'))
#删除目录树
shutil.rmtree(r'E:\sagepy\env\20200294')
#重命名
shutil.move(r'E:\sagepy\env\20200924\惹出.py',r'E:\sagepy\env\20200924\exue.py')
#统计空间使用情况
total, used, free = shutil.disk_usage("e:\\")
print("e盘总量：{:.2f}GB，使用量：{:.2f}GB，空闲：{:.2f}GB".format(total/1024/1024/1024,used/1024/1024/1024,free/1024/1024/1024))
#解压缩
shutil.make_archive(r'E:\sagepy\env\20200731\520','zip',r'E:\sagepy\env\520')
shutil.unpack_archive(r'E:\sagepy\env\20200924\520.zip',r'E:\sagepy\env\20200924\520_out')

```

