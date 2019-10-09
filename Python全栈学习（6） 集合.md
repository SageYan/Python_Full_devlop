[TOC]

# Python全栈学习（6）集合

## 集合方法

```python
 集合的定义
s=set('hello')
print(s)

s=set(['alex','alex','sb'])
print(s)

s={1,2,3,4,5,6}

常用操作方法
#添加
s.add('s')
s.add('3')
s.add(3)
print(s)

s.clear()
print(s)

#复制
s1=s.copy()

s={'sb',1,2,3,4,5,6}
#随机删
# s.pop()

#指定删除
s.remove('sb')
s.remove('hellol') #删除元素不存在会报错
s.discard('sbbbb')#删除元素不存在不会报错
print(s)


python_l=['lcg','szw','zjw','lcg']
linux_l=['lcg','szw','sb']
p_s=set(python_l)
l_s=set(linux_l)
#求交集
print(p_s,l_s)
print(p_s.intersection(l_s))
print(p_s&l_s)
或者
py_lin = []
for i in python1:
    if i in linux:
        py_lin.append(i)
print(py_lin)

#求并集
print(p_s.union(l_s))
print(p_s|l_s)

#差集
print('差集',p_s-l_s)
print(p_s.difference(l_s))
print('差集',l_s-p_s)
print(l_s.difference(p_s))





#交叉补集
# print('交叉补集',p_s.symmetric_difference(l_s))
# print('交叉补集',p_s^l_s)


#差集更新
python_l=['lcg','szw','zjw','lcg']
linux_l=['lcg','szw','sb']
p_s=set(python_l)
l_s=set(linux_l)
print(p_s,l_s)
# print('差集',p_s-l_s)
# p_s=p_s-l_s
p_s.difference_update(l_s)
print(p_s)

#是否非交集
s1={1,2}
s2={2,3,5}
print(s1.isdisjoint(s2))

#判断子集
s1={1,2}
s2={1,2,3}
print(s1.issubset(s2))#s1 是s2 的子集
print(s2.issubset(s1))#False

print(s2.issuperset(s1))#s1 是s2 的父集

#更新update
s1={1,2}
s2={1,2,3}
# s1.update(s2) #更新多个值

# s1.add(1,2,3,4) #更新一个值
# s1.union(s2) #不更新

print(s1)


#定义不可变集合
s=frozenset('hello')
print(s)

#去重
names=['alex','alex','wupeiqi']

names=list(set(names))
print(names)
```

