[TOC]



# Python全栈学习（4） 列表 元祖

## 列表

### list类中提供的方法 

```python
 1. 原来值最后追加
 对象.方法(..)   # li对象调用append方法
 li.append(5)
 li.append("alex")
 li.append([1234,2323])
 print(li)
 
 2. 清空列表
 li.clear()
 print(li)

 3. 拷贝，浅拷贝
 v = li.copy()
 print(v)
 
 4. 计算元素出现的次数
 v = li.count(22)
 print(v)

 5. 扩展原列表，参数：可迭代对象
 li = [11, 22, 33, 22, 44]
 li.append([9898,"不得了"])
 [11, 22, 33, 22, 44, [9898, '不得了']]

 li.extend([9898,"不得了"])
 for i in [9898,"不得了"]:
     li.append(i)
 [11, 22, 33, 22, 44, 9898, '不得了']

 li.extend("不得了")
 print(li)

 6. 根据值获取当前值索引位置（左边优先）
 li = [11, 22, 33, 22, 44]
 v= li.index(22)
 print(v)

 7. 在指定索引位置插入元素
 li = [11, 22, 33, 22, 44]
 li.insert(0,99)
 print(li)

 8、 删除某个值(1.指定索引；2. 默认最后一个)，并获取删除的值
 li = [11, 22, 33, 22, 44]
 v = li.pop()
 print(li)
 print(v)

 li = [11, 22, 33, 22, 44]
 v = li.pop(1)
 print(li)
 print(v)
 9. 删除列表中的指定值，左边优先
 li = [11, 22, 33, 22, 44]
 li.remove(22)
 print(li)
 PS: pop remove del li[0]    del li[7:9]   clear

 10 将当前列表进行翻转
 li = [11, 22, 33, 22, 44]
 li.reverse()
 print(li)

 11 列表的排序
 li = [11,44, 22, 33, 22]
 li.sort()
 li.sort(reverse=True)
 print(li)
## 欠
 cmp
 key
 sorted
```



### list中的常用用法

1. 列表格式[]

2. 列表中可以嵌套任何类型，中括号括起来，逗号分割每个元素，列表中的元素可以是 数字，字符串,列表，布尔值..所有的都能放进去

```python
1.索引取值
print(li[3])
2. 切片，切片结果也是列表
print(li[3:-1])

3. for循环
   while循环

for item in li:
   print(item)

4. 列表元素，可以被修改

 li = [1, 12, 9, "age", ["石振文", ["19", 10], "庞麦郎"], "alex", True]

############## 索引################
修改
li[1] = 120
print(li)
li[1] = [11,22,33,44]
print(li)

删除,第一种方式
del li[1]
print(li)
############## 切片################
修改
li[1:3] = [120,90]
print(li)
删除
del li[2:6]
print(li)

5.in 操作
li = [1, 12, 9, "age", ["石振文", ["19", 10], "庞麦郎"], "alex", True]
v1 = "石振文" in li
print(v1)
v2 = "age" in li
print(v2)


6. 操作list当中的元素
li = [1, 12, 9, "age", ["石振文", ["19", 10], "庞麦郎"], "alex", True]
print(li[4][1][0])


7. 转换
字符串转换列表   
s = "pouaskdfauspdfiajsdkfj"
new_li = list(s)
print(new_li)

列表转换成字符串，
需要自己写for循环一个一个处理： 既有数字又有字符串
li = [11,22,33,"123","alex"]
# r = str(li) # '[11,22,33,"123","alex"]'
# print(r)


s = ""
for i in li:
    s = s + str(i)
print(s)

直接使用字符串join方法：列表中的元素只有字符串
li = ["123","alex"]
v = "".join(li)
print(v)

#补充：字符串创建后，不可修改
 列表，有序；元素可以被修改

```

### 元祖提供的方法

元组，元素不可被修改，不能被增加或者删除

```python
# tu = (11,22,33,44)
# tu.count(22),获取指定元素在元组中出现的次数
# tu.index(22)

 1. 书写格式
 tu = (111,"alex",(11,22),[(33,44)],True,33,44,)
 一般写元组的时候，推荐在最后加入 ,
 元素不可被修改，不能被增加或者删除
 
 2. 索引
 v = tu[0]
 print(v)

 3. 切片
 v = tu[0:2]
 print(v)

 4. 可以被for循环，可迭代对象
 for item in tu:
     print(item)

 5. 转换
 s = "asdfasdf0"
 li = ["asdf","asdfasdf"]
 tu = ("asdf","asdf")

 v = tuple(s)
 print(v)

 v = tuple(li)
 print(v)

 v = list(tu)
 print(v)

 v = "_".join(tu)
 print(v)

 li = ["asdf","asdfasdf"]
 li.extend((11,22,33,))
 print(li)

 6.元组的一级元素不可修改/删除/增加
 tu = (111,"alex",(11,22),[(33,44)],True,33,44,)
 # 元组，有序
 # v = tu[3][0][0]
 # print(v)
 # v=tu[3]
 # print(v)
 tu[3][0] = 567
 print(tu)
```

