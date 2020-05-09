[TOC]

# Python全栈学习（7） 集合

## 集合定义

```python
集合是无序的，不重复的数据集合，它里面的元素是可哈希的(不可变类型)，但是集合本身是不可哈希（所以集合做不了字典的键）的。
```

## 集合作用

```python
列表的去重
关系测试：交集，并集，差集等
```

## 集合的创建

```python
set1 = set({1,2})
print(set1)

set2 = {1,'a','sage'}
print(set2)
```

## 集合的增删改查

### 集合的增加

```python
s1 = {'cong', 'SA', 'Boo', 'Amy'}
#单个元素增加
s1.add(123)
#迭代增加
s1.update(['11', 'Sage', 'Yan'])
print(s1)
```

### 集合的删除

```python
s1 = {'cong', 'SA', 'Boo', 'Amy'}
#删除一个元素
s1.remove('cong')  删除元素不存在会报错
s.discard('sbbbb') 删除元素不存在不会报错
#随机删除一个元素
s1.pop()
print(s1)
#清空
s1.clear()
print(s1)
#删除集合
del s1
```

### 集合的变相修改

```python
s1 = {'cong', 'SA', 'Boo', 'Amy'}
s1.discard('SA')
s1.add('SA_new')
print(s1)
```

## 集合的关系运算

### 交集

```python
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))  # {4, 5}
```

### 并集

```python
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7,8}
print(set2.union(set1))  # {1, 2, 3, 4, 5, 6, 7,8}
```

### 差集

```python
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 - set2)  # {1, 2, 3}
print(set1.difference(set2))  # {1, 2, 3}
```

### 交叉补集

```python
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}
```

### 子集与超集

```python
set1 = {1,2,3}
set2 = {1,2,3,4,5,6}

print(set1 < set2)
print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。

print(set2 > set1)
print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集。
```

## 定义不可变集合

```
s=frozenset('hello')
print(s)
```

