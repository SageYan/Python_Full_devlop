[TOC]

# 编码进阶

## 原则

```powershell
1. 不同的密码本之间能否互相识别？不能。
2. 数据在内存中全部是以Unicode编码的，但是当你的数据用于网络传输或者存储到硬盘中，必须是以非Unicode编码（utf-8,gbk等等）
#注释 
'''
bytes类型也称作字节文本，他的主要用途就是网络的数据传输，与数据存储。
所以
内存Unicode编码 --> bytes非unicode编码 --> 传输、存储 解码
'''
```

## bytes的表现形式

### 英文

```python
str： 'hello '
​	内存中的编码方式： Unicode
​	表现形式： 'hello'

bytes ： 
​	内存中的编码方式： 非Unicode
​	表现形式：b'hello'

#代码
s1 = "Sage"
b1 = b'Sage'
print(s1,b1)
#Sage b'Sage'
```

### 中文

```python
	str： 
​		内存中的编码方式： Unicode
​		表现形式：'中国'

​	bytes ： 
​		内存中的编码方式： 非Unicode  # Utf-8
​		表现形式：b'\xe4\xb8\xad\xe5\x9b\xbd'  

#代码
s1 = "严聪"
b1 = s1.encode("utf-8") #编码
print(b1,s1)
#b'\xe4\xb8\xa5\xe8\x81\xaa' 严聪
s2 = b1.decode("utf-8") #解码
print(s2)
#严聪
```

### 不同编码的转换

```python
# gbk ---> utf-8
b1 = b'\xd6\xd0\xb9\xfa'
s = b1.decode('gbk') #以gbk解码
# print(s)

b2 = s.encode('utf-8') #以utf-8重新编码
print(b2) 
# b'\xe4\xb8\xad\xe5\x9b\xbd'
```

