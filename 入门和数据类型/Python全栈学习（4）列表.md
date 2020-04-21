[TOC]

# Python全栈学习（4）列表

## 列表的索引，切片

```python
1. 索引
li = [100, '太白', True, [1, 2, 3]]
# print(li[0], type(li[0]))
# print(li[1],type(li[1]))
# print(li[-1])

2. 切片
li = [1, 3, 2, "a", 4, "b", 5, "c"]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
l1 = li[:3]
print(l1)

# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
print(li[3:6])
# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
print(li[1:-2:2])
# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
print(li[-3::-2])

```

## 列表的增删改查

+ ### 列表的创建

```python
# 方式一
l1 = [1, 2, 'Alex']

# 方式二
l1 = list()
l1 = list('fhdsjkafsdafhsdfhsdaf')
print(l1)

# 方式三：列表推导式
```



+ ### 列表的增加

```python
#1 append 附加
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
l1.append("Sage")
print(l1.append("Sage"))  #打印append动作，None
print(l1)

例如：
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
while 1:
    name = input("请输入新员工姓名,按Q或者退出")
    if name.upper() == 'Q':
        print("程序退出")
        break
    else:
        l1.append(name)
print(l1)

#2 insert 索引插入
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
l1.insert(2,'boy')
print(l1)


#3 extend 迭代着追加
l1 = ['sage','is', 'a','good','man']
l1.extend('like')
print(l1)
//['sage', 'is', 'a', 'good', 'man', 'l', 'i', 'k', 'e']//
```

+ ### 列表的删除

```python
#1 pop 按照索引删除
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
v = l1.pop(-2)  #可以变量接受pop的值
print(l1,v)
// ['太白', '女神', 'xiao', '闫龙'] 吴老师//

l1.pop()  # 默认删除最后一个

#2 remove  指定元素删除,如果有重名元素，默认删除从左数第一个
l1.remove('xiao')
print(l1) 

#3 clear 清空列表

#4 del 按照索引删除
del l1[-1]
       #按照切片(步长)删除
del l1[::2]
```

+ ### 列表的修改

```python
#1 索引修改
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
l1[2] = 'Sage'
print(l1)
#2 切片修改
l1[2:] = ['sage','alss','99','ss','000']
print(l1)
#3 加上步长，修改的元素个数必须对等
l1[::2] = 'aaaaaaaaa'
print(l1) 
//报错：
ValueError: attempt to assign sequence of size 9 to extended slice of size 4
//
```

+ ### 列表查看

```python
1.索引取值
print(li[3])
2. 切片，切片结果也是列表
print(li[3:-1])

3. for循环
   while循环

for item in li:
   print(item)
```

## 列表的嵌套

```python
l1 = [1, 2, 'tadfsafsdafibfdsgfdgfdgfdai', [1, 'alex', 3,]]
#将l1中的'taibai'变成大写并放回原处。
l1[2] = l1[2].upper()
print(l1)
#给小列表[1,'alex',3,]追加一个元素,'老男孩教育'
l1[-1].append('old')
print(l1)
#将列表中的'alex'通过字符串拼接的方式在列表中变成'alexsb'
l1[-1][1] += 'sb'
print(l1)
```

