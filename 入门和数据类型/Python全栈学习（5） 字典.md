[TOC]

# Python全栈学习（5）字典以及总结

## 字典方法

```python
 dict
 dict
 dic = {
     "k1": 'v1',
     "k2": 'v2'
 }
 1 根据序列，创建字典，并指定统一的值
 v = dict.fromkeys(["k1",123,"999"],123)
 print(v)

 2 根据Key获取值，key不存在时，可以指定默认值（None）
 v = dic['k11111']
 print(v)  #不存在相关的key 会报错
 
 #使用get方法避免报错，可以指定返回默认值
 v = dic.get('k1',111111)
 print(v)

 3 删除并获取值
 dic = {
     "k1": 'v1',
     "k2": 'v2'
 }
 v = dic.pop('k1',90)
 print(dic,v)
 k,v = dic.popitem()
 print(dic,k,v)

 4 设置值
 #已存在，不设置，获取当前key对应的值
 #不存在，设置，获取当前key对应的值
 dic = {
     "k1": 'v1',
     "k2": 'v2'
 }
 v = dic.setdefault('k1111','123')
 print(dic,v)

 5 更新
 dic = {
     "k1": 'v1',
     "k2": 'v2'
 }
 dic.update({'k1': '111111','k3': 123})
 print(dic)
 dic.update(k1=123,k3=345,k5="asdf")
 print(dic)

 6 keys()  7 values()   8 items()   get   update
```

## 字典特点

```python
 1、基本机构
 info = {
     "k1": "v1", # 键值对
     "k2": "v2"
 }
 2 字典的value可以是任何值
 info = {
     "k1": 18,
     "k2": True,
     "k3": [
         11,
         [],
         (),
         22,
         33,
         {
             'kk1': 'vv1',
             'kk2': 'vv2',
             'kk3': (11,22),
         }
     ],
     "k4": (11,22,33,44)
 }
 print(info)

 3 布尔值(1,0)可以作为key、列表、字典不能作为字典的key
 info ={
     1: 'asdf',
     "k1": 'asdf',
     True: "123",
     # [11,22]: 123
     (11,22): 123,
     # {'k1':'v1'}: 123

 }
 print(info)

 4 字典无序

 info = {
     "k1": 18,
     "k2": True,
     "k3": [
         11,
         [],
         (),
         22,
         33,
         {
             'kk1': 'vv1',
             'kk2': 'vv2',
             'kk3': (11,22),
         }
     ],
     "k4": (11,22,33,44)
 }
 print(info)

 5、索引方式找到指定元素
 info = {
     "k1": 18,
     2: True,
     "k3": [
         11,
         [],
         (),
         22,
         33,
         {
             'kk1': 'vv1',
             'kk2': 'vv2',
             'kk3': (11,22),
         }
     ],
     "k4": (11,22,33,44)
 }
 # v = info['k1']
 # print(v)
 # v = info[2]
 # print(v)
 v = info['k3'][5]['kk3'][0]
 print(v)

 6 字典支持 del 删除
 info = {
     "k1": 18,
     2: True,
     "k3": [
         11,
         [],
         (),
         22,
         33,
         {
             'kk1': 'vv1',
             'kk2': 'vv2',
             'kk3': (11,22),
         }
     ],
     "k4": (11,22,33,44)
 }
 del info['k1']

 del info['k3'][5]['kk1']
 print(info)

 7 for循环
 dict
 info = {
     "k1": 18,
     2: True,
     "k3": [
         11,
         [],
         (),
         22,
         33,
         {
             'kk1': 'vv1',
             'kk2': 'vv2',
             'kk3': (11,22),
         }
     ],
     "k4": (11,22,33,44)
 }
 for item in info:
     print(item)

 for item in info.keys():
     print(item)

 for item in info.values():
     print(item)

 for item in info.keys():
     print(item,info[item])

 for k,v in info.items():
     print(k,v)
```

## 总结

### 数据类型常用方法

```python
# 一、数字
# int(..)
# 二、字符串
# replace/find/join/strip/startswith/split/upper/lower/format
# tempalte = "i am {name}, age : {age}"
# # v = tempalte.format(name='alex',age=19)
# v = tempalte.format(**{"name": 'alex','age': 19})
# print(v)
# 三、列表
# append、extend、insert
# 索引、切片、循环
# 四、元组
# 忽略
# 索引、切片、循环         一级元素不能被修改
# 五、字典
# get/update/keys/values/items
# for,索引

# dic = {
#     "k1": 'v1'
# }

# v = "k1" in dic
# print(v)

# v = "v1" in dic.values()
# print(v)
# 六、布尔值
# 0 1
# bool(...)
# None ""  () []  {} 0 ==> False
```

