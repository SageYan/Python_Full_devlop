[toc]

# Python全栈学习（21）内置函数

## 了解即可的函数

```json
all()
any()
bytes()
callable() 
chr()
complex()
divmod()
eval() 
exec()
format()
frozenset()
globals()
hash()
help()
id()
input()
int()
iter()
locals()
next()
oct()
ord()
pow()
repr()
round()
```

eval：执行字符串类型的代码，并返回最终结果

```python
print(eval('4 + 4'))
eval("print('666')")

'''
8
666
'''
```

exec:执行字符串类型的代码

```python
msg = '''
for i in range(7):
    print(i)
'''

exec(msg)

# 网络传输的str input 输入的时候,sql注入等等绝对不能使用eval exec
```

hash：获取一个对象（可哈希对象：int，str，bool，tuple）的哈希值

help：函数用于查看函数或模块用途的详细说明

```python
print(help(list))
print(help(str.split))
```

callable：函数用于检查一个对象是否是可调用的

```python
name = 'alex'
def func():
    pass
print(callable(name))  # False
print(callable(func))  # True
```

int、float、complex：数字类型

```python
print(int(3.89))
```

**bin**：将十进制转换成二进制并返回

**oct**：将十进制转化成八进制字符串并返回

**hex**：将十进制转化成十六进制字符串并返回

```python
print(bin(18),type(bin(11)))
print(oct(99),type(oct(99)))
print(hex(100),type(hex(99)))

'''
0b10010 <class 'str'>
0o143 <class 'str'>
0x64 <class 'str'>
'''
```

divmod：以元组的形式返回商和余数

```python
print(divmod(10,3),type(divmod(22,7)))

#(3, 1) <class 'tuple'>
```

**round**：四舍五入保留小数位数

```python
print(round(3.14159265, 3)) #保留三位小数
```

pow：幂运算以及取余数

```python
print(pow(2,3),pow(2,3,3))
#8 2
```

***bytes***：返回一个新的 bytes 对象

```python
s = "SAGE YAN 严"
b = s.encode('utf-8')
print(b)

b1 = bytes(s,encoding='gbk')
print(b1)

'''
b'SAGE YAN \xe4\xb8\xa5'
b'SAGE YAN \xd1\xcf'
'''
```

ord：输入字符找该字符编码的位置

chr: 根据ascii/Unicode编码字符位置找对应字符 

```python
print(ord('a'),ord('找'))
#97 25214

print(chr(97),chr(25214))
#a 找
```

**repr**:返回一个对象的string形式（原形毕露）

```python
s = 'AMY'
msg = 'I am %s' % s
print(repr(msg))

# 'I am AMY'
```

all：可迭代对象中，全都是True才是True

any：可迭代对象中，有一个True 就是True

print 分隔打印

```python
print(1,2,3,4 ,sep='?')
# 1?2?3?4

print(1,end='')
print('amy')
# 1amy
```

**abs**：绝对值

```python
print(abs(-1111))
```

sum：求和

```python
l1 = [i for i in range(100)]
print(sum(l1,120)) #1+ ..+ 99 + 120
```

**reversed**：返回的是一个翻转的迭代器

```python
l1 = [i for i in range(7)]
l2 = list(reversed(l1))
print(reversed(l1),l2)
# <list_reverseiterator object at 0x000001E6FA5E5BA8> [6, 5, 4, 3, 2, 1, 0]

l1 = [i for i in range(7)]
l1.reverse()
print(l1)
# list 内部方法 [6, 5, 4, 3, 2, 1, 0]

```

**zip**：拉链方法

```python
l1 = [1,2,3,4,5]
tu1 = ('amy', 'sage', 'booboo')
s1 = 'family'

z1 = zip(l1,tu1,s1)
print(z1, list(z1))

# <zip object at 0x00000171ACDC5388> [(1, 'amy', 'f'), (2, 'sage', 'a'), (3, 'booboo', 'm')]
```

***min max sorted*** ：key的用法

```python
#绝对值最小的数
l1 = [100,-1,-9,-1230]
print(min(l1,key=abs))


#字典value最小的数
dic1 = {'a': 3, 'b': 2, 'c': 1}
print(min(dic1,key=lambda x : dic1[x]))

#年龄最大的人和按照年龄从大到小排序
people=[
    {'name':'SAGE', 'age':30},
    {'name':'BOOBOO', 'age':29},
    {'name':'AMY','age':4},
    {'name':'ZHUNAINAI','age':55},
]

print(max(people, key=lambda x:x['age'] )['name'])
print(sorted(people, key=lambda x:x['age'] ,reverse=True))

'''
-1
c
ZHUNAINAI
[{'age': 55, 'name': 'ZHUNAINAI'}, {'age': 30, 'name': 'SAGE'}, {'age': 29, 'name': 'BOOBOO'}, {'age': 4, 'name': 'AMY'}]
'''
```

***filter***：相当于列表推导式的筛选模式

```python
mv_people = ["sage", "da shi_", "rao_", "sb_"]
l1 = [i for i in mv_people if 's' not in i]
ret = filter(lambda x:'s' not in x ,mv_people)
print(l1,ret,list(ret),sep=' || ')

#filter 返回的是迭代器
#['rao_'] || <filter object at 0x000002814E724160> || ['rao_']
```

***map***：相当于列表推导式的循环模式

```python
l1 = [i**2 for i in range(1,7)]
ret = map(lambda x:x**2,range(1,7))
print(l1,ret,list(ret),sep=' || ')

#[1, 4, 9, 16, 25, 36] || <map object at 0x00000201CB00B4A8> || [1, 4, 9, 16, 25, 36]
```

***reduce***：

```python
from functools import reduce

l1 = [4,2,3,1]
def func(x,y):
    return 10*x + y

res = reduce(func,l1)
'''
    第一次：x  y  : 4  3    10*x + y =    记录：43
    第二次：x = 43    y = 2 10*x + y =   记录：432
    第三次  x = 432   y = 1 .......
'''
print(res)
```