[TOC]

# Python全栈学习（13）内置函数



## 内置函数 map filter reduce

### map函数的用法

```python
#传统方法
def sqer(a):
    return a**2

def amy_p(n):
    return "amy"*n

def fac(fun, arr):
    res = []
    for i in arr:
        res.append(fun(i))
    return res

--函数名作为形参传入--
print(fac(sqer, lis1))
print(fac(amy_p, lis1))
print('匿名函数lambda用法', fac(lambda x: x*"amy", lis1))

#注意python3 map函数结果作为迭代器对象处理，和python2不同，需要list格式化处理结果
#map处理方法：
#map(函数/处理逻辑,可迭代对象)
print("map函数用法", list(map(lambda x: x*"amy", lis1)))
print(list(map(lambda x: x.upper(), "sage Is a good Person!")))
```

### filter函数的用法

```python
#低端写法
mv_people = ["sage", "da shi_", "rao_", "sb_"]

def ends(n):
    return n.endswith("_")


def s_in(s):
    return "s" in s


def filter_test(func, ls):
    good = []
    for i in ls:
        if not func(i):
            good.append(i)
    return good

print(filter_test(ends, mv_people))
print(filter_test(s_in, mv_people))

#高级写法
print("内置函数处理", list(filter(lambda x: "s" not in x, mv_people)))
```



### reduce函数的用法

```python
num_l = [4,2,3,100]
def times(x,y):
    return x*y

def plus(x,y):
    return x+y

def foo(func,array,init_num=None):
    if init_num is None:
        res = array.pop(0)
    else:
        res = init_num
        for i in array:
            res = func(res,i)
    return res
print(foo(times,num_l,10))
#print(foo(plus,num_l))

from functools import reduce

######################################
print(reduce(lambda x,y: x*y,num_l,10))
```

## 小结

```python
#map()处理序列中的每个元素，得到的结果是一个‘列表’，该‘列表’元素个数及位置与原来一样.

#filter遍历序列中的每个元素，判断每个元素得到布尔值，如果是True则留下来

people = [
    {'name':"sage",'age':30},
    {'name':"booboo",'age':29},
    {'name':"amy",'age':4}
]

print(list(filter(lambda x:x['age']==4,people)))

#reduce:处理一个序列，然后把序列进行合并操作
from functools import reduce
print(reduce(lambda x,y:x+y,range(100),100))
print(reduce(lambda x,y:x+y,range(1,101)))
```

## 其他内置函数

```python
#abs取绝对值
print(abs(-1))
print(abs(1))

#all any判断可迭代对象的布尔值
print(all([1,2,'1']))
print(all([1,2,'1','']))
print(all(''))
结果：
True
False
True

print(any([0,'']))
print(any([0,'',1]))
结果：
True
True

# bin 十进制转化二进制
print(bin(3))

#bool 空，None，0的布尔值为False，其余都为True
print(bool(''))
print(bool(None))
print(bool(0))



#bytes 编码函数
print(bytes("我是sage", encoding="big5").decode("big5"))
print(bytes("你好啊", encoding='gbk').decode('Shift_JIS'))
结果：
我是sage
ﾄ羲ﾃｰ｡
用什么编码，就用什么解码，否则乱码
print(bytes(name,encoding='ascii'))#ascii不能编码中文

# ascii编码 
print(chr(46))

# dir显示对象方法 
print(dir(dict))

# divmod 取商 和 余数 
print(divmod(10,3))

#eval 把字符串中的数据结构提取
#eval 把字符串中的数学运算计算
dic={'name':'alex'}
dic_str=str(dic)
print(eval(dic_str)['name'])

print(eval('(1*2-99/12)**2'))
结果：39.0625

#可hash的数据类型即不可变数据类型，不可hash的数据类型即可变数据类型
#不管长度如何，hash后的结果长度固定
print(hash('12sdfdsaf3123123sdfasdfasdfasdfasdfasdfasdfasdfasfasfdasdf'))
print(hash('12sdfdsaf31231asdfasdfsadfsadfasdfasdf23'))
结果：
2805671929765069611
2268372707527818833

name='alex'
print(hash(name))
print(hash(name))


print('--->before',hash(name))
name='sb'
print('=-=>after ',hash(name))
结果：
3452244503409062987
3452244503409062987 #在程序同一次执行过程当中，hash的结果不变
--->before 3452244503409062987
=-=>after  6527733516412922001 #中途变量改变，hash结果变化




# 查看帮助 
print(help(all))


#进制转换
print(bin(10))#10进制->2进制
print(hex(12))#10进制->16进制
print(oct(12))#10进制->8进制


# 判断对象实例
print(isinstance(1,int))
print(isinstance('abc',str))
print(isinstance([],list))
print(isinstance({},dict))
print(isinstance({1,2},set))

name = "sage"

def test():
    age = 30
    print(globals()) #打印全局变量
    print(locals())  #打印局部变量

test()

print(__file__) #打印全局变量__file__内容
```





