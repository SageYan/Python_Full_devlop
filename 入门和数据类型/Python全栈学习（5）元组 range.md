[TOC]



# Python全栈学习（5）元组 range

## 元组提供的方法

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
 
 #元组拆包#
 a,b = (1,2)
 
 #list unpack
l = [1,23,4,5,6,7,8,9,10]
a,*_,b  = l
print(a,b)
 
```
## range常用方法
```python
r = range(10)
#索引
print(r[1])

#步长
for i in range(1,101,2):
    print(i)

#倒叙
for i in range(101,8,-3):
    print(i)

#利用for循环，利用range将l1列表的所有索引依次打印出来
l1 = [1, 2, 3, 'alex', '太白', 2, 3, 4, 66,]
for i in range(len(l1)):
    print(l1[i],i)
```
