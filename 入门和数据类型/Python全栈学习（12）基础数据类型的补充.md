[TOC]

# 基础数据类型的补充

## 字符串

### 1 首字母大写，其余变小写

```python
name = "sAgeYan"
print(name.capitalize())

#Sageyan
```

### 2 大小写翻转

```python
name = "sAgeYan"
print(name.swapcase())

#SaGEyAN
```

### 3 每个单词的首字母大写

```python
msg= 'taibai say3hi'
print(msg.title())

#Taibai Say3Hi
```

### 4 居中

```python
a1 = "boo"
print(a1.center(20,"%"))

#%%%%%%%%boo%%%%%%%%%
```

5打印索引位

```python
# find :通过元素找索引，找到第一个就返回，找不到 返回-1
# index:通过元素找索引，找到第一个就返回，找不到 报错

msg = "hello everyone i am sage"
print(msg.find("e",7,10))
print(msg.index("o",7,12))

#8
#11
```

## 元组

### 1 元组中如果只有一个元素，并且没有逗号，那么它不是元组，它与改元素的数据类型一致

```python
tu1 = (2,3,4)
tu2 = (2)
tu3 = ('太白')
tu4 = ([1,2,3])
tu5 = (1,)

print(type(tu1), type(tu2),type(tu3),type(tu4),type(tu5))

#<class 'tuple'> <class 'int'> <class 'str'> <class 'list'> <class 'tuple'>
```

### 2 计数

```python
tu = (1,2,3,3,3,2,2,3,)
print(tu.count(2))
```

### 3 索引

```python
#index 打印元素索引位，元素不存在则报错
tu = ('太白', '日天', '太白')
print(tu.index('太白'))
```



## 列表

### 1  计数 索引

```python
l1 = ['太白', '123', '女神', '大壮']
print(l1.count("123"), l1.index('大壮'))

#1 3
```

### 2  排序

```python
l2 = [5, 4, 3, 7, 8, 6, 1, 9]
#正序
l2.sort()
print(l2)
#倒序
l2.sort(reverse=True)
print(l2)
```

### 3 翻转

```python
l1 = ['太白', '123', '女神', '大壮']
l1.reverse()
print(l1)

#['大壮', '女神', '123', '太白']
```

4 列表的相加 和数字相乘

```python
# 列表可以相加
# l1 = [1, 2, 3]
# l2 = [1, 2, 3, '太白', '123', '女神']
# print(l1 + l2)

# 列表与数字相乘
# l1 = [1, 'daf', 3]
# l2 = l1*3
# print(l2)
```



### 5  循环一个列表的时，最好不要改变列表的大小，会影响最终的结果

```python
l1 = [11, 22, 33, 44, 55]
# 索引为奇数对应的元素删除

#错误做法
for i in range(len(l1)):
    if i % 2 == 1:
        l1.pop(i)
print(l1)

'''
IndexError: pop index out of range
'''
#原因：pop动作改变了列表的结构，导致后续索引不能正确定位对应元素

#正确做法
1 直接删除
del l1[1::2]
print(l1)

2 倒序删除
for i in range(len(l1)-1,-1,-1):
    if i % 2 == 1:
        l1.pop(i) #pop出尾部元素，不影响列表前面的结构
print(l1)

3 思维转换
new_l1 = []
for i in range(len(l1)):
    if i % 2 == 0:    #取出所有偶数位的元素--》代表删除了所有奇数位元素
        new_l1.append(l1[i])  
l1 = new_l1
print(l1)
```

## 字典

### 1 update

```python
#变量赋值更新
dic = {'name': 'Sage', 'age': 18}
dic.update(book='python', gf='boo', weight='60')
print(dic)
'''
有则改之，无则添加
'''
dic.update(name='Amy')
print(dic)


#元组拆包更新
dic.update(((1, "a",), (2, "abc",)))
print(dic)

#用字典更新字典
'''
有则改之，无则添加
'''
dic2 = {"name":"BOOBOO", "bf":"Sage", "weight":75}
dic.update(dic2)
print(dic2)
print(dic)

'''
{'name': 'Sage', 'book': 'python', 'gf': 'boo', 'age': 18, 'weight': '60'}
{'book': 'python', 'weight': '60', 'gf': 'boo', 'name': 'Amy', 'age': 18}
{'book': 'python', 'weight': '60', 2: 'abc', 'gf': 'boo', 1: 'a', 'name': 'Amy', 'age': 18}
{'name': 'BOOBOO', 'bf': 'Sage', 'weight': 75}
{'book': 'python', 'weight': 75, 2: 'abc', 'bf': 'Sage', 'gf': 'boo', 1: 'a', 'name': 'BOOBOO', 'age': 18}
'''
```

### 2 fromkeys

```python
#迭代，循环生产键值对
dic = dict.fromkeys("Sage", "man")
print(dic)

dic1 = dict.fromkeys([1,2,3,4,] ,[])
print(dic1)
dic1[1].append("Boo")  #所有键指向相同的内存地址 
print(dic1)
'''
{'g': 'man', 'a': 'man', 'e': 'man', 'S': 'man'}
{1: [], 2: [], 3: [], 4: []}
{1: ['Boo'], 2: ['Boo'], 3: ['Boo'], 4: ['Boo']}
'''
```

### 3 循环一个字典时，如果改变这个字典的大小，就会报错

```python
dic = {'k1': '太白', 'k2': 'barry', 'k3': '白白', 'age': 18}
# 将字典中键含有'k'元素的键值对删除。

for i in dic:
    if "k" in i:
        dic.pop(i)
print(dic)
'''
RuntimeError: dictionary changed size during iteration
'''
for i in list(dic.keys()):  #生成列表与原始字典无关了
    if "k" in i:
        dic.pop(i)
print(dic)

```

## 练习题
```python
lst = ['周星星', '周扒皮', '马化腾', '周慧']
for i in lst:
    if i.strip()[0] == '周':
        lst.remove(i)
print(lst)
#['周扒皮', '马化腾'] 
# 注意for循环改变list的大小，导致结果有误
for i in range(len(lst)-1, -1, -1):
    if lst[i].strip()[0] == '周':
        lst.pop(i)
print(lst)
# ['马化腾']

#车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (选做题)
cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
local = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南','京': '北京'}

# 期望结果: {'⿊⻰江':2, '⼭东': 1, '北京': 1}
# 思想：循环创建字典键值对，不存在就创建，存在即增加计数
dic = {}
for car in cars:
    if local[car.strip()[0]] not in dic.keys():
        dic[local[car.strip()[0]]] = 1
    else:
        dic[local[car.strip()[0]]] += 1
print(dic)

#简化
dic = {}
for car in cars:
    dic[local[car.strip()[0]]] = dic.get(local[car.strip()[0]],0) + 1
print(dic)
```
