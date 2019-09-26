[TOC]

# Python全栈学习（1）

## 入门

### 变量的申明

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
name = "sage"
```

变量的作用：昵称，其代指内存里某个地址中保存的内容

#### 变量定义的规则

```python
变量名只能是 字母、数字或下划线的任意组合
变量名的第一个字符不能是数字
以下关键字不能声明为变量名
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 流程控制和缩进

打印 1到10除去7的整数

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
i=1
while i < 11 :
        if i != 7:
                print(i)
        i = i+1
```

打印 1..100的整数和

```python
#!/usr/bin/env
# -*- coding: utf-8 -*-

i = 1
s = 0
while i < 101:
        s = s+i
        i = i+1
print(s)
```

 打印 1-2+3-4..99的和

```python
#!/usr/bin/env
# -*- coding: utf-8 -*-

i = 1
s = 0
while i < 100:
        if i%2 == 1:
                a = i
        else:
                a = 0-i
        s = s + a
        i = i + 1
print(s)
```

用户用户名密码输入有机会尝试三次

```python
#!/usr/bin/env
# -*- coding: utf-8 -*-

import getpass

i = 1
while i < 4:

        name = raw_input("请输入用户名：")
        pwd = getpass.getpass("请输入密码：")
        if name == "sage" and pwd == "123":
                print "welcome"
                i = 100
        else:
                print "用户名密码错误！"
                i = i + 1
```

```shell
[root@sage python_scripts]# python up3.py 
请输入用户名：djakjd
请输入密码：
用户名密码错误！
请输入用户名：adada
请输入密码：
用户名密码错误！
请输入用户名：huhuhuhu
请输入密码：
用户名密码错误！
[root@sage python_scripts]# python up3.py 
请输入用户名：sage
请输入密码：
welcome
```