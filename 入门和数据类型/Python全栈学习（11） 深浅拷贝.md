[TOC]

# Python全栈学习（11） 深浅拷贝

## 赋值运算

```python
l1 = [1,2,3,['barry','alex']]
l2 = l1

l1[0] = 111
print(l1)  # [111, 2, 3, ['barry', 'alex']]
print(l2)  # [111, 2, 3, ['barry', 'alex']]

l1[3][0] = 'wusir'
print(l1)  # [111, 2, 3, ['wusir', 'alex']]
print(l2)  # [111, 2, 3, ['wusir', 'alex']]

注释：
对于赋值运算来说，l1与l2指向的是同一个内存地址，所以他们是完全一样的。

```



## 浅拷贝

```python
l1 = [1, '太白', True, (1,2,3), [22, 33]]
l2 = l1.copy()

print(id(l1), id(l2))  #1558057699848 1558057725320
#PS:
​```
列表（可变数据类型）的在内存中的表现形式是，不保留实际数据，而是以槽位的形式保留实际数据对应的内存地址。
因此浅拷贝后会内存中会开辟出一个新的列表，而槽位中对应的内存地址和原始列表相同。
​```
print(id(l1[0]), id(l2[0])) #1437598160 1437598160
print(id(l1[-1]), id(l2[-1])) #1558057722824 1558057722824
#槽位指向的内存地址一致

l1[0] = 123
print(l1, l2)
l1[-1].append('abc')
print(l1, l2)
#结果：
[123, '太白', True, (1, 2, 3), [22, 33]] [1, '太白', True, (1, 2, 3), [22, 33]]
PS：
​```
l1修改了0位槽位保留的 “不可变数据类型的内存地址” 指向，不影响l2的0槽位保存的内存地址指向。
​```
[123, '太白', True, (1, 2, 3), [22, 33, 'abc']] [1, '太白', True, (1, 2, 3), [22, 33, 'abc']]
​```
对于可变数据类型的修改，并不会改变内存地址的指向。因此,l1和l2都收到影响。
​```
```



## 深拷贝

```python
import copy
l1 = [1, 'alex', True, (1,2,3), [22, 33]]
l2 = copy.deepcopy(l1)
print(id(l1), id(l2))  # 2788324482440 2788324483016
print(id(l1[0]),id(l2[0]))  # 1470562768 1470562768
print(id(l1[-1]),id(l2[-1]))  # 2788324482632 2788324482696
#注释：
​```
对于深copy来说，列表是在内存中重新创建的，列表中可变的数据类型是重新创建的，列表中的不可变的数据类型是公用的。
​```
print(id(l1[-2]),id(l2[-2]))  # 2788323047752 2788323047752
```

## 相关练习
```python
#可变数据类型 内存地址不变
v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
v2 = v1
v1['k1'] = 'wupeiqi'
v1['k2'].append(4)
print(v2)
# {'k2': [1, 2, 3, 4], 'k1': 'wupeiqi'}
#不可变数据类型 内存地址变化
a1 = 'aaa'
a2 = a1
a1 = 'aaa2'
print(a2)
# aaa

#列表槽位对应数据内存地址
v1 = '好嗨哟'
v2 = [1, 2, 3, 4, v1]  # v2[-1] = v1
v1 = "人生已经到达了巅峰"
print(v2)
#[1, 2, 3, 4, '好嗨哟']

#同上
info = [1, 2, 3]
userinfo = {'account': info, 'num': info, 'money': info} #key指向实际数据内存地址，而非info变量
info.append(9)
print(userinfo)
info = "题怎么这么多"  #info 指向的内存地址变了
print(userinfo)

#可变不可变数据类型变量变化总结
data = {}
for i in range(10):
    data['user'] = i
print(data)

data_list = []
for i in range(10):
    data = {}  #把字典清空
    data['user'] = i
    data_list.append(data)
print(data_list)

data_list = []
for i in range(10):
    #data = {}
    data['user'] = i #循环更新data字典
    data_list.append(data)
print(data_list)

data_list = []
for i in range(10):
    data = {}
data['user'] = i #循环结束执行赋值
data_list.append(data)
print(data_list)
#结果
{'user': 9}
[{'user': 0}, {'user': 1}, {'user': 2}, {'user': 3}, {'user': 4}, {'user': 5}, {'user': 6}, {'user': 7}, {'user': 8}, {'user': 9}]
[{'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}]
[{'user': 9}]
```
