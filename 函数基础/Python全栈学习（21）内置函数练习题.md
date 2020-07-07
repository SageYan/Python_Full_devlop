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

