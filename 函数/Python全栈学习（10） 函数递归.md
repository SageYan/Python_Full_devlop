[TOC]

# Python全栈学习（10）函数递归

## 递归举例

```python
def calc(n):
    print(n)
    if int(n / 2) == 0:
        return n
    res=calc(int(n / 2))
    return res


res=calc(10)
print(res)


##########################################################################################
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

## 递归说明

```python
递归总结：
1 递归必须有一个明确的执行结果
2 每次进入更深一层的递归，问题的规模要比上一次递归要小
3 递归的效率不高，会导致内存溢出
```

## 匿名函数

```python
func = lambda x:x**x
print(func(11))


n = lambda name:name+"_XX_!!"
print(n("bobo"))

he = lambda x, y, z : x** y** z
print(he(3,2,4))

plus = lambda a, b, c : (a+1, b*c)
print(plus(1,2,3))
```



