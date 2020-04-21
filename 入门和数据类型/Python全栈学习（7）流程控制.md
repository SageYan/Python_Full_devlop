[TOC]

# 流程控制

## 条件判断 if

```python
if 条件:
    满足条件执行代码
elif 条件:
    上面的条件不满足就走这个
elif 条件:
    上面的条件不满足就走这个
elif 条件:
    上面的条件不满足就走这个    
else:
    上面所有的条件不满足就走这段
```

## 无限循环while

需要重复之前的动作，输入用户名密码，考虑到while循环

1. ### 结构以及原理

```python
while 条件：
	循环体

​``` 
满足条件，进入循环体，执行循环体到底部。
再次进行条件判断，满足条件，再次进入循环体。。。
周而复始
​```
```

2. ### 打断循环的方式

```python
1 改变条件
flag 标志位
例如1：

flag = True
while flag:
    flag = False
    print('狼的诱惑')
    print('我们不一样')
    print('月亮之上')
    print('庐州月')
    print('人间')
#执行循环体一次后，改变了条件（标志位），不满足条件，不执行循环体
例如2：
i = 1
while i < 101:    #条件每循环一次都会发生改变
    print(i)
    i = i +1
    
    
2 break
#循环当中遇到break ，直接退出循环
例如： #打印1~100之内的所有偶数
count = 2
while True:
    print(count)
    count = count +2
    if count > 100:
        break
#或者        
count = 1
while count < 101:
    if count % 2 == 0:
        print(count)
    count = count +1
    
 
3 continue 退出本次循环，执行下次循环（相当于循环体碰到循环体底部）

flag = True
while flag:
    print('Sage')
    print('fight')
    flag = False
    continue  #跳到下次循环 下面的代码不再执行
    print("until dead!")
执行结果
Sage
fight

4 系统命令
```

3. ### 补充：else...break

```python
# while else： while 循环如果被break打断，则不执行else语句
count = 1
while count < 5:
    print(count)
    if count == 2:
        break
    count = count + 1
else:
    print(666)
#执行结果：
1
2

例如： 用户名密码尝试三次
count = 1
while count <= 3:
    username = input('用户名')
    password = input('密码')
    code = 'qwer'
    your_code = input('验证码：')
    if your_code == code:
        if username == 'alex' and password == '123':
            print('登录成功')
            break
        else:
            print('用户名或者密码错误')
    else:
        print('验证码错误')
    count = count + 1
```

