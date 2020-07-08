[toc]

# Python全栈学习（21）内置函数练习题

#### 1. 求出50以内能被3整除的数的平方，并放入到一个列表中

```python
l1 = list(map(lambda x:x**2, filter(lambda x:x%3 == 0,range(0,50))))

l2 = [i**2 for i in range(0,50) if i % 3 == 0]
```

#### 2.有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白'],将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']

```json
l1 = ['alex', 'WuSir', '老男孩', '太白']
l2 = [i + str(l1.index(i)) for i in l1]
```

#### 3.用列表完成笛卡尔积

```python
#构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型)。
colors = ['black', 'white','yellow']
sizes = ['S', 'M', 'L']

lst = [(i,j) for i in colors for j in sizes]
print(lst)
```

#### 4.看代码写结果

```python
def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test()  #生成器内存地址
for n in [1,10]:
    g = (add(n, i) for i in g)

print(list(g))


'''
1. 代码运行到 for n in ...
   生成两个生成器表达式，并不执行内部代码
2. list(g)
   a. 执行最近的生成器表达式 (add(n, i) for i in g) #n = 10，递归等待 i
   b. 执行1中的第一个生成器表达式g = (add(n, i) for i in g) # 此时n不是1而是10，递归等待 i in g
   c. 执行g = test() # g = (0,1,2,3) ,向上一层返回结果
   d. 以上各层接受结果得到最终结果 [20, 21, 22, 23]
'''
#关于函数的递归举例
递归总结：
1 递归必须有一个明确的执行结果
2 每次进入更深一层的递归，问题的规模要比上一次递归要小
3 递归的效率不高，会导致内存溢出

import time

person_list=['alex','wupeiqi','linhaifeng','zsc']
def ask_way(person_list):
    print('-'*60)
    if len(person_list) == 0:
        return '根本没人知道'
    person=person_list.pop(0)
    if person == 'linhaifeng':
        return '%s说:我知道,老男孩就在沙河汇德商厦,下地铁就是' %person

    print('hi 美男[%s],敢问路在何方' % person)
    print('%s回答道:我不知道,但念你慧眼识猪,你等着,我帮你问问%s...' % (person, person_list))
    time.sleep(100)
    res=ask_way(person_list)


    print('%s问的结果是: %res' %(person,res))
    return res

res=ask_way(person_list)
print(res)
```

#### 5.map fliter sorted 练习

```python
# 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中结果：list一下[9110.0, 27161.0,......]
# 还是上面的字典，用filter过滤出单价大于100的股票。
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]

ret = map(lambda x : x['shares'] * x['price'],portfolio)
print(list(ret))

ret2 = filter(lambda x : x['price'] > 100 ,portfolio)
print(list(ret2))


#将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
l1 = [ {'sales_volumn': 0},
{'sales_volumn': 108},
{'sales_volumn': 337},
{'sales_volumn': 475},
{'sales_volumn': 396},
{'sales_volumn': 172},
{'sales_volumn': 9},
{'sales_volumn': 58},
{'sales_volumn': 272},
{'sales_volumn': 456},
{'sales_volumn': 440},
{'sales_volumn': 239}]

print(sorted(l1,key=lambda x: x['sales_volumn'],reverse=True))



# 写一个函数完成三次登陆功能：
# 用户的用户名密码从一个文件register中取出。
# register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
# 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# 登陆成功返回True。
def get_username_password():
    username_dict = {}
    with open('register',encoding='utf-8') as f1:
        for it in f1:
            lst = it.strip().split('|')
            username_dict[lst[0].strip()] = lst[1].strip()
    return username_dict

def login():
    count = 1
    dic1 = get_username_password()
    while count < 4:
        username = input('pls input your username:').strip()
        passwd = input('pls input your password:').strip()

        if username in dic1 and passwd == dic1[username]:
            print("Login success!")
            return True
        else:
            print("Pls input agin!")

        count += 1

login()
```

