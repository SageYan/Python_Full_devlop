[TOC]

# Python全栈学习（9）函数局部变量和全局变量

## 定义

```python
#全局变量与局部变量
#函数即变量
name = 'SAGE'
def chang_name():
    name = 'haha'
    print(name)

chang_name()
print(name)    #打印全局变量

#内置函数修改全局变量
def gb_name():
    global name
    name = "SDBU"
    print("gb",name)
gb_name()
print(name)
```

## 注意点及规则

```python
如果函数的内容无global关键字，
  - 有声明局部变量
    NAME = ["产品经理","廖波湿"]
    def qupengfei():
        NAME = "自己"
        print('我要搞', NAME)
    qupengfei()
  - 无声明局部变量
    NAME = ["产品经理","廖波湿"]
    def qupengfei():
        NAME.append('XXOO')
        print('我要搞', NAME)
    qupengfei()

如果函数的内容有global关键字
  - 有声明局部变量
    NAME = ["产品经理","廖波湿"]
    def qupengfei():
        global NAME
        NAME = "自己"
        print('我要搞', NAME)
    qupengfei()
    
	#错误示例：
    NAME = ["产品经理","廖波湿"]
    def qupengfei():
        NAME = "自己"
        global NAME
        print('我要搞', NAME)
    qupengfei()
  - 无声明局部变量
    NAME = ["产品经理","廖波湿"]
    def qupengfei():
        global NAME
        NAME = ["阿毛"]
        NAME.append('XXOO')
        print('我要搞', NAME)
    qupengfei()

######## 全局变量变量名大写
######## 局部变量变量名小写

# 优先读取局部变量，能读取全局变量，无法对全局变量重新赋值 NAME=“fff”，但是对于可变类型，可以对内部元素进行操作
# 如果函数中有global关键字，变量本质上就是全局的那个变量，可读取可赋值 NAME=“fff”

```

## 嵌套

```python
NAME = '海风'

def huangwei():
    name = "黄伟"
    print(name)
    def liuyang():
        name = "刘洋"
        print(name)
        def nulige():
            name = '沪指花'
            print(name)
        print(name)
        nulige()
    liuyang()
    print(name)

huangwei()
黄伟
刘洋
刘洋
沪指花
黄伟


name = "刚娘"

def weihou():
    name = "陈卓"
    def weiweihou():
        nonlocal name   # nonlocal，指定上一级变量，如果没有就继续往上直到找到为止
        name = "冷静"

    weiweihou()
    print(name)

print(name)
weihou()
print(name)
# 刚娘
# 冷静
# 刚娘
```

## 风湿理论

```python
风湿理论：函数即变量

#报错 bar未定义
def foo():
    print('from foo')
    bar()

foo()

# def bar():
#     print('from bar')
# def foo():
#     print('from foo')
#     bar()
#
# foo()



# def foo():
#     print('from foo')
#     bar()
#
# def bar():
#     print('from bar')
# foo()

#报错 bar未定义
def foo():
    print('from foo')
    bar()

foo()

def bar():
    print('from bar')
    
    
    
1 name = "刚娘"

2 def weihou():
    4.1 name = "陈卓"
    4.2 def weiweihou():
        	4.3.1 nonlocal name   # nonlocal，指定上一级变量，如果没有就继续往上直到找到为止
        	4.3.2 name = "冷静"

    4.3 weiweihou()
    4.4 print(name)  --nonlocal 冷静

3 print(name)  --刚娘
4 weihou()  --调用内存函数代码
5 print(name) --刚娘
# 刚娘
# 冷静
# 刚娘
```

