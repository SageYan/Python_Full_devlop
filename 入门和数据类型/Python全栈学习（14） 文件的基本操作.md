[TOC]

# Python全栈学习（14）文件的基本操作

## 1 文件操作的初识

### 文件操作三部曲

1 打开文件
2 对文件句柄进行相应的操作
3 关闭文件

```python
f1 = open(r'E:\python_project\teaching_plan\day08 课堂笔记以及代码\day08\Sage.txt',mode="r",encoding='utf-8')
content = f1.read()
print(content)
f1.close()

#Sage is 啊 啊啊啊  good man
```

### 代码解释

```perl
open 内置函数，open底层调用的是操作系统的接口。

f1,变量-->文件句柄。 对文件进行的任何操作，都得通过文件句柄的方式。
encoding:可以不写，不写参数，默认编码本：操作系统的默认的编码
windows: gbk
linux： utf-8
mac ： utf-8

f1.close() 关闭文件句柄。
```

## 2 文件的读

### r , rb, r+,r+b 四种模式

```python
#全部读取
f_r = open('SageYan', mode='r', encoding='utf-8')
content = f_r.read()
print(content)
f_r.close()

#按照**字符**个数读取
f_r = open('SageYan', mode='r', encoding='utf-8')
content = f_r.read(12)
print(content)
f_r.close()

#逐行读取
f_r = open('SageYan', mode='r', encoding='utf-8')
content = f_r.readline()
content2 = f_r.readline()
content3 = f_r.readline()
print(content)
print(content2)
print(content3)
f_r.close()

#readlines 读取成列表
f_r = open('SageYan', mode='r', encoding='utf-8')
content = f_r.readlines()
print(content)
f_r.close()

#文件句柄是迭代器，使用for循环遍历，减少内存开销
f_r = open('SageYan', mode='r', encoding='utf-8')
for  line in f_r:
    print(line)
f_r.close()

#rb打开图片，视频等文件
f_b = open("美女2.jpg", mode='rb')
con = f_b.read()
print(con)
f_b.close()
```

## 3 文件的写

### w,wb, w+,w+b 四种模式

```python
# 没有文件，创建文件，写入内容
# 如果文件存在，先清空原文件内容，在写入新内容
f_w = open('file_write', 'w', encoding='utf-8')
f_w.write("随便嘻嘻嘻xxx")
f_w.close()

#wb 操作图片
f_r = open('美女2.jpg','rb')
content = f_r.read()
f_r.close()

f_w = open('123.jpg','wb')
f_w.write(content)
f_w.close()
```

## 4 文件的追加

### a, ab, a+,a+b 四种模式

```python
# 没有文件创建文件，追加内容
f_a = open("append_txt.txt", 'a',encoding='utf-8')
f_a.write("你好啊！ 旅行者！")
f_a.close()
# 有文件，在原文件的最后面追加内容
f_a = open("append_txt.txt", 'a',encoding='utf-8')
f_a.write("\n你好啊！ 旅行者！\n愿大地母亲忽悠着你！")
f_a.close()
```

## 5 文件操作的其他模式  r+

```python
# 读并追加
f1 = open("append_txt.txt", mode='r+', encoding='utf-8')
f1.read() #光标移到到文件尾
f1.write("\n你好啊！朋友！") 
f1.close()

#光标在文件头 直接从文件头开始写
f1 = open("append_txt.txt", mode='r+', encoding='utf-8')
f1.write("hello old friend!")
print(f1.read())
f1.close()
#报字母和中文的编码字节不匹配的错！字母一个字节，中文三个字节
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa1 in position 0: invalid start byte
```

## 6 文件操作的其他功能

### 小结

```powershell
三个大方向： 
读，四种模式： r rb r+ r+b
写，四种模式 :  w,wb, w+,w+b 
追加 四种模式:  a, ab, a+,a+b

相应的功能：对文件句柄的操作：read read(n) readline() readlines() write() 
```

### 其他功能 tell()  seek()  flush()

```python
#除了read，其余处理文件的方法都是以字节计数，read是以字符计数
#tell()
f1 = open('file_write', 'r', encoding='utf-8')
print(f1.tell())
con = f1.read()
print(f1.tell()) #获取光标的位置 单位字节
f1.close()

#seek() 调整光标的位置,单位字节
f1 = open('file_write', 'r', encoding='utf-8')
f1.seek(10)
print(f1.read())
f1.close()

'''
f=open('seek.txt','r',encoding='utf-8')
print(f.tell())
f.seek(10)
print(f.tell())
f.seek(3)  #默认相对位置是文件起始位置,默认省略0
print(f.tell())
结果：
10
3


f = open('12.txt','rb')  #需要以相对位置移动光标 文件必须以b的模式打开
f.seek(10,1)
print(f.tell())
f.seek(3,1)    #参数1表示以相对移动的方式
print(f.tell())
f.close()
结果：
10
13

f = open('12.txt','rb')
f.seek(-12,2)   #2：从文件末尾移动光标
print(f.tell()) 
f.close()
结果：
250
'''

#flush 强制刷新
f1 = open('强制刷新.txt', 'w', encoding='utf-8')
f1.write("哈哈\nbullshit!")
f1.flush()
f1.close()
```

### 利用seek()打印文件的最后一行

```python
方式一：
f = open('12.txt','rb')
data = f.readlines() #以列表的形式读入文件， 浪费内存
print(data[-1].decode('utf-8'))


方式二：

f=open('日志文件','rb')

#循环文件的推荐方式，不会将文件一次性读入内存
for i in f:
	print(i) 

for i in f:  #逐行读取，不会全部加载整个文件
    offs=-10
    while True:
        f.seek(offs,2)
        data=f.readlines()
        if len(data) > 1:
            print('文件的最后一行是%s' %(data[-1].decode('utf-8')))
            break
        offs*=2
```



## 7 with打开文件句柄

```python
with open('file_write','r',encoding='utf-8') as f1 ,\
    open('强制刷新.txt', 'w', encoding='utf-8') as  f2:
    print(f1.read())
    f2.write("hello")
# 优点： 不用手动关闭文件句柄,可以同时打开多个文件句柄
# 缺点：待续
```

## 8 文件操作的改

### 文件修改过程

```perl
1 以读的模式打开原文件。
2 以写的模式创建一个新文件。
3 将原文件的内容读出来修改成新内容，写入新文件。
4 将原文件删除。
5 将新文件重命名成原文件
```

### 过程代码

```python
#low版
import os

with open('强制刷新.txt', 'r', encoding='utf-8') as f1,\
    open('new', 'w', encoding='utf-8') as f2:
    content = f1.read()
    new_con = content.replace('SAGE', 'BOOBOO')
    f2.write(new_con)
os.remove('强制刷新.txt')
os.rename('new', '强制刷新.txt')

#进阶版
import os
with open('强制刷新.txt', 'r', encoding='utf-8') as f1,\
    open('new', 'w', encoding='utf-8') as f2:
    for line in f1:
        line = line.replace('BOO', 'AMY')
        f2.write(line)
os.remove('强制刷新.txt')
os.rename('new', '强制刷新.txt')

# 关闭文件句柄，再次以w模式打开此文件时，才会清空文件。
with open('文件的写', encoding='utf-8',mode='w') as f1:
     for i in range(9):
         f1.write('恢复贷款首付款')  #不会清空文件
```

## 9 练习题
```python
# 文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
# apple 10 100
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3


# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
#[{'name':'apple','price':10,'amount':3,'year': 2019},{'name':'tesla','price':1000000,'amount':1}......]

#方法一：
l1 = []
with open('a', 'r', encoding='utf-8') as f1:
    for line in f1:

        line_lst = line.strip().split()
        dic = {"name":line_lst[0], 'price':line_lst[1], 'amount':line_lst[2]}
        l1.append(dic)
print(l1)
#分析： 可拓展性差，文件a新增字段，代码修改严重


l1 = []
name_lst = ['name', 'price', 'amount', 'year']
#创建name_lst 与处理过程解绑耦合性
with open('a', 'r', encoding='utf-8') as f1:
    for line in f1:

        line_lst = line.strip().split()
        dic = {}
        for i in range(len(name_lst)):
            dic[name_lst[i]] = line_lst[i]
#取出name_lst字段做key，文件内容做value，生成目标字典
        l1.append(dic)
print(l1)

#2.通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3,year:2012},{'name':'tesla','price':1000000,'amount':1}......]
'''
name:apple price:10 amount:3 year:2012
name:tesla price:100000 amount:1 year:2013
name:te1 price:120000 amount:3 year:2020
name:te2a price:200000 amount:4 year:2023
'''

l1 = []
l2 = ['name', 'price', 'amount', 'year']
for line in open('a1',encoding='utf-8'):

    line_lst = line.strip().split()
    dic1 = {}
    for i in range(len(l2)):

        dic1[l2[i]] = line_lst[i].split(":")[1]
    l1.append(dic1)
print(l1)


#3.通过代码，将其构建成这种数据类型：[{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]
'''
序号 部门 人数 平均年龄 备注
1 python 30 26 单身狗
2 Linux 26 30 没对象
3 运营部 20 24 女生多
'''
l1 = []
with open('a2',encoding='utf-8') as f1:
    l2 = f1.readline().strip().split()
    for line in f1:
        line_lst = line.strip().split()
        dic1 = {}
        for i in range(len(l2)):
            dic1[l2[i]] = line_lst[i]
        l1.append(dic1)

print(l1)
```
