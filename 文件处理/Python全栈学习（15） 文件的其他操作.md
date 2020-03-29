[TOC]

# Python全栈学习（15）文件的其他操作



## 文件b模式操作

```python
#'字符串'---------encode---------》bytes
#bytes---------decode---------》'字符串'
f=open('test11.py','rb',encoding='utf-8') #b的方式不能指定编码
f=open('test11.py','rb') #b的方式不能指定编码

读rb：
f = open("cong",'rb')
data = f.read()
s = data.decode('utf-8')
print(s)
f.close()

写wb：
f = open('test01','wb')
f.write('sage是严聪\r\n哈哈\r\nis yan'.encode('utf-8'))
f.write(bytes('sage 是是是',encoding='utf-8'))
f.close()
```

## 文件操作的其他方法

### closed、encoding、flush

```python
f = open('test01','r',encoding='utf-8')
print(f.closed)
print(f.encoding)  #文件的打开的编码方式
print(f.readlines())
f.flush()     #刷新内存中内容到磁盘
结果如下：
False
utf-8
['sage是严聪\n', '哈哈\n', 'is yanhaha']
```

### 读取文件中的换行符号（和操作系统相关）

```python
#除了read，其余处理文件的方法都是以字节计数，read是以字符计数
f1 = open('test01', 'r+', encoding='utf-8', newline='') #读取文件中真正的换行符号（与操作系统平台有关）
print(f.tell())  #光标所在的位置，以字节计算
f.readline()
print(f.tell())  #光标所在的位置，以字节计算
print(f1.readlines())
f1.close 
结果如下：
0
15
['哈哈\r\n', 'is yanhaha']
```

### 移动光标的位置seek，截断文件truncate

```python
#移动光标的位置seek
f2 = open('test01', 'r+', encoding='utf-8', newline='')
f2.seek(5)  
print(f2.tell())
print(f2.readlines())  #报错，可见seek移动光标是以字节为单位，导致解码错误
f2.close()


f3 = open('test01', 'r+', encoding='utf-8', newline='')
print(f3.read(10))  #以字符个数计，读取前10个字符
f3.close()
结果如下：
sage是严聪
哈

#从开头开始算，将文件只保留从0-10个字节的内容，文件必须以写方式打开，但是w和w+除外（直接w的方式打开文件，文件被清空）
f.truncate(10) 
```

### seek的补充

```python
f=open('seek.txt','r',encoding='utf-8')
print(f.tell())
f.seek(10)
print(f.tell())
f.seek(3)  #默认相对位置是文件起始位置
print(f.tell())
结果：
10
3


f = open('12.txt','rb')  #要以相对位置移动光标 文件必须以b的模式打开
f.seek(10,1)
print(f.tell())
f.seek(3,1)    #参数1表示以相对的方式
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
```

## 读取文件的最后一行

```python
方式一：
f = open('12.txt','rb')
data = f.readlines()
print(data[-1].decode('utf-8'))

方式二：

f=open('日志文件','rb')


循环文件的推荐方式，不会将文件一次性读入内存
for i in f:
	print(i) 

for i in f:
    offs=-10
    while True:
        f.seek(offs,2)
        data=f.readlines()
        if len(data) > 1:
            print('文件的最后一行是%s' %(data[-1].decode('utf-8')))
            break
        offs*=2
```

