[TOC]

# Python全栈学习（14）文件的基本操作



## 文件的一般处理操作：r w a

### 文件的读取：r

```python
#文件读的一般流程：打开文件句柄-->处理-->关闭文件句柄
f = open("sage", 'r', encoding='utf-8') #open函数默认以操作系统的编码进行解码
data = f.read()
#print(data)  
#注意文件读取是以光标的形式推进 若在read之后再readline是无法读取数据的

print('第1行', f.readline(), end='') #readline逐行读取文件
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(type(f.readline()))  #文件逐行读取是字符串


print(f.readlines())  #readlines以list的形式读取文件
print(type(f.readlines()))

f.close()
```

### 文件写入：w

```python
file = open("cong", 'w', encoding='utf-8')
#file.write("hi I am sage!")
#file.write('\nhaha\nnizhidaoma\nhaha\n')

file.writelines(["sage:18\n", "yan is cong", "hahahda"])
file.writelines(["sage:18\n", "yan is cong", "hahahda", 12]) #文件只能够以字符串的形式写入
print(file.writable())
file.close()
```



### 文件的追加 ：a

```python
file = open("cong", "a", encoding="utf-8")
file.writelines(["\n新的内容\n", 'hahaha\n'])
file.close()
```

## 文件的其他处理

```python
#可读可写：r+
#这里的写是用追加的形式写

file = open("cong", 'r+', encoding='utf-8')
data = file.read()
print(data)
file.writelines(["\n新的内容\n", 'hahaha123\n'])
file.close()


#文件的修改
s1 = slice(1,9)
s_file = open("cong", 'r', encoding='utf-8')
data = s_file.readlines()
for i in data:
    print(i)
s_file.close()

d_file = open('cong', 'w', encoding='utf-8')
d_file.writelines(data[s1])
d_file.close()

#利用with 减少close文件句柄动作
with open('cong', 'r', encoding='utf-8') as s_file,\
        open('cong_new', 'w', encoding='utf-8') as d_file:
    data = s_file.read()
    d_file.write(data)
```

