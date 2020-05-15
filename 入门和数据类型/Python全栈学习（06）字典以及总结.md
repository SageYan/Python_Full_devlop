[toc]

# Python全栈学习（6）字典以及总结

## 字典初识

+ 为何需要字典

```python
   1. 列表可以存储大量的数据类型，但是如果数据量大的话，他的查询速度比较慢。
   2. 列表只能按照顺序存储，数据与数据之间关联性不强。
   所以针对于上的缺点，说咱们需要引入另一种容器型的数据类型，解决上面的问题，这就需要dict字典。
```

+ 数据类型分类（可变与不可变）

```
    不可变（可哈希）的数据类型：int，str，bool，tuple。

    可变（不可哈希）的数据类型：list，dict，set。
```

* 字典如何构成

```python
--字典是Python语言中的映射类型，他是以{}括起来，里面的内容是以键值对的形式储存的：

  Key: 不可变（可哈希）的数据类型.并且键是唯一的，不重复的。(通常是字符和数字，bool和tuple几乎不用)
  Value:任意数据(int，str，bool，tuple，list，dict，set)，包括后面要学的实例对象等。
      
 　
  在Python3.5版本（包括此版本）之前，字典是无序的。
  在Python3.6版本之后，字典会按照初建字典时的顺序排列(即第一次插入数据的顺序排序)。

  字典的优点：查询速度快，存储关联性强
　字典也有缺点：他的缺点就是内存消耗巨大（以空间换时间）
```



## 字典的创建方式

### 元组的拆包

```python
dic = dict(((1,'sage'),(2,'python'),(3,'amy')))
print(dic)
```

### 键值对

```python
dic = dict(name='sage',hobby='books',age='18')
print(dic)
```

### 官方写法

```python
dic = dict({'one': 1, 'two': 2, 'three': 3})
print(dic)  # {'one': 1, 'two': 2, 'three': 3}
```



## 字典的增删改查

### 增

```python
方式一：
有则改之无则加之
dic = dict(name='sage',hobby='books',age='18')
dic['gender'] = 'male'
print(dic)
dic['age'] = 30
print(dic)

#{'name': 'sage', 'hobby': 'books', 'age': '18', 'gender': 'male'}
#{'name': 'sage', 'hobby': 'books', 'age': 30, 'gender': 'male'}

方式二：
#setdefault
有则不变无则增加
dic = dict(name='sage',hobby='books',age='18')
dic.setdefault('wife','booboo')
print(dic)
dic.setdefault('age','20')
print(dic)

#{'name': 'sage', 'hobby': 'books', 'age': '18', 'wife': 'booboo'}
#{'name': 'sage', 'hobby': 'books', 'age': '18', 'wife': 'booboo'}
```



### 删

```python
1  pop
#按照键值对删除，有返回值；
#可以通过设置默认值来避免无key值报错

dic = dict(name='sage',hobby='books',age='18')
ret = dic.pop('age')
print(ret,dic)


ret1 = dic.pop('wife','NO WIFE')
print(ret1,dic)

#18 {'name': 'sage', 'hobby': 'books'}
#NO WIFE {'name': 'sage', 'hobby': 'books'}


2  del
del(dic['age'])

3 clear
dic.clear()
```



### 改

```python
#通过键值对
dic['age'] = 30
```



### 查

```python
方法一：
#根据key找value
get #可以设置默认返回值，避免报错

dic = dict(name='sage',hobby='books',age='18',love_list=['python','boo','amy'])
print(dic.get('love_list'))
print(dic.get('akk','查无此件'))

结果：
['python', 'boo', 'amy']
查无此件


方法二：
keys()
dic = dict(name='sage',hobby='books',age='18',love_list=['python','boo','amy'])
print(dic.keys())

values()
dic = dict(name='sage',hobby='books',age='18',love_list=['python','boo','amy'])
print(dic.values())

items()
for key,value in dic.items():
  print(key,value)
结果：
name sage
hobby books
age 18
love_list ['python', 'boo', 'amy']
```



### 相关练习

```python
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic['k4'] = 'v4'
print(dic)
#请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic['k1'] = 'alex'
#请在k3对应的值中追加一个元素 44，输出修改后的字典
#dic['k3'].append(44)
dic.get('k3').append(44)
print(dic)

#请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic['k3'].insert(0,18)
print(dic)

#将字符串msg = "k :1|k1:2|k2:3|k3: 4" 转化为字典 {'k': 1, 'k1': 2, 'k2': 3, 'k3': 4}
msg = "k :1|k1:2|k2:3|k3: 4"

dic = {}
li = msg.strip().split("|")
for i in  li:
    key ,value = i.split(":")
    dic[key.strip()]=int(value.strip())
print(dic)

# 有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
msg = "k: 1|k1:2|k2:3 |k3 :4"
print( msg.split("|"))
dic1 = {}
for i in msg.split("|"):
    k1,v1=i.split(":")
    dic1[k1.strip()]=int(v1)
print(dic1)

"""
商品列表：
  goods = [
		{"name": "电脑", "price": 1999},
		{"name": "鼠标", "price": 10},
		{"name": "游艇", "price": 20},
		{"name": "美女", "price": 998}
	]
要求:
1：页面显示 序号 + 商品名称 + 商品价格，如：
      1 电脑 1999
      2 鼠标 10
	  ...
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。
"""
goods = [
		{"name": "电脑", "price": 1999},
		{"name": "鼠标", "price": 10},
		{"name": "游艇", "price": 20},
		{"name": "美女", "price": 998}
	]
for i in range(len(goods)):
    print("{} {} {}".format(i+1,goods[i]["name"],goods[i]["price"]))

while 1:
    goods_id = input("请输入商品号：").strip()
    if goods_id.upper() == "Q":
        break
    elif goods_id.isdecimal() :
        if  int(goods_id) <= len(goods):
            print(goods[int(goods_id)-1]["name"],goods[int(goods_id)-1]["price"])
        else:
            print("超出范围，请重新输入")
    else :
        print("输入有误，重新输入")
```



##  **字典的嵌套** 

一层层剥洋葱

```python
dic = {
    'name':'汪峰',
    'age':48,
    'wife':[{'name':'国际章','age':38}],
    'children':{'girl_first':'小苹果','girl_second':'小怡','girl_three':'顶顶'}
}

#获取汪峰的名字。
print(dic.get('name'))

#获取这个字典：{'name':'国际章','age':38}。
print(dic.get('wife')[0])

#获取汪峰妻子的名字。
print(dic.get('wife')[0].get('name'))

#获取汪峰的第三个孩子名字。
print(dic.get('children').get('girl_three'))
```

