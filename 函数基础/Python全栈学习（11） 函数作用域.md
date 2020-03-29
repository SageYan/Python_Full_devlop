[TOC]

# Python全栈学习（11）函数作用域

## 作用域理解

```python
def yan():
    print("yan is yan cong!")

def sage():
    print("sage is yan!")
    return yan
res = sage()

print(res)
print(res())  #加上()执行函数，用print显示return的结果


结果：
<function yan at 0x0000013DDDB07F28> #print(函数名) 返回内存地址
-----------
sage is yan!
yan is yan cong!
None   #函数 yan()没有return值默认返回NONE

```

## 作用域与函数调用位置关系无关

```python
#函数的作用域只跟函数声明时定义的作用域有关，跟函数的调用位置无任何关系

name = "boo boo"
def boo():
    name = "AMY"
    def sage():
        name = "xiao ci"
        def amy():
            print("amy 的name是%s" % name)
        return amy
    return sage

boo()()()
amy 的name是xiao ci

a1 = boo()
print(a1)

a2 = a1()
print(a2)

a3 = a2()
print(a3)

<function boo.<locals>.sage at 0x000001D9AD24F2F0>
<function boo.<locals>.sage.<locals>.amy at 0x000001D9AD24F268>
amy 的name是xiao ci
None
```





