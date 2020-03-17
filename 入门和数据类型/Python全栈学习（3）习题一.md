[TOC]



# Python学习（3）

## 习题一

1、执行 Python 脚本的两种方式
2、简述位、字节的关系
3、简述 ascii、unicode、utf-8、gbk 的关系
4、请写出 “李杰” 分别用 utf-8 和 gbk 编码所占的位数
5、Pyhton 单行注释和多行注释分别用什么？
6、声明变量注意事项有那些？
7、如有一下变量 n1	=	5，请使用 int 的提供的方法，得到该变量最少可以用多少个二进制位表示？

```python
n1 = 5
print(n1.bit_length())
```

8、布尔值分别有什么？
9、阅读代码，请写出执行结果
				
```python
a	=	"alex"
b	=	a.capitalize()
print(a)
print(b)
请写出输出结果：
```
10、写代码，有如下变量，请按照要求实现每个功能
	    name	=	"	aleX"
a.	 移除 name 变量对应的值两边的空格，并输入移除后的内容
b.	 判断 name 变量对应的值是否以 "al"	 开头，并输出结果
c.	 判断 name 变量对应的值是否以 "X"	 结尾，并输出结果
d.	 将 name 变量对应的值中的 “l” 替换为 “p”，并输出结果
e.	 将 name 变量对应的值根据 “l” 分割，并输出结果。
		
f.	 请问，上一题 e	 分割之后得到值是什么类型（可选）？
g.	 将 name 变量对应的值变大写，并输出结果
h.	 将 name 变量对应的值变小写，并输出结果
i.	 请输出 name 变量对应的值的第 2 个字符？
j.	 请输出 name 变量对应的值的前 3 个字符？
k.	 请输出 name 变量对应的值的后 2 个字符？
l.	 请输出 name 变量对应的值中 “e” 所在索引位置？
m.	 获取子序列，仅不包含最后一个字符。如： oldboy	 则获取 oldbo;	root则获取 roo

```python
name = "    aleX"
name = name.strip()
print(name.startswith("al"))
print(name.endswith("X"))
print(name.replace("l","p"))
print(name.partition("l"))
print(name.split("l"))
print(name.upper())
print(name.lower())
print(name[1])
print(name[0:3])
print(name[-2:])
print(name.find("e"))
print(name[0:-1])
```



21、字符串是否可迭代对象？如可以请使用 for 循环每一个元素？

```python
for i in "dhakhdka":
    print(i)
```

22、请用代码实现：
				 a.	 利用下划线将列表的每一个元素拼接成字符串，li	 ＝ "alexericrain"
				 b.	 利用下划线将列表的每一个元素拼接成字符串，li	 ＝ ['alex',	'eric',	'rain']	 	 	 （可选）

```python
li = "aliecsadad"
print("_".join(li))

li = ['alex','eric','rain']
print("_".join(li))
```



23、Python2 中的 range 和 Python3 中的 range 的区别？
24、实现一个整数加法计算器：
				 如：content	=	input('请输入内容：')	 	 	 #	 如： 5+9	 或 5+	9	 或 5	+	9	

```python
contant = input(">>>")
print(int(contant[0])+int(contant[-1]))
```



25、计算用户输入的内容中有几个十进制小数？几个字母？
				 如：content	=	input('请输入内容：')	 	 	 #	 如：asduiaf878123jkjsfd-213928

```python
num = 0
count = 0
con = input(">>>")
for i in con:
    if i.isdecimal():
        num = num + 1
    elif i.isalpha():
        count = count + 1
print("数字有：{0}个，字母有：{1}个".format(num,count))
```



26、简述 int	 和 9	 等数字	 	 以及	 	 str	 和 "xxoo"	 等字符串的关系？
27、制作趣味模板程序
	    需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实
		如：敬爱可亲的 xxx，最喜欢在 xxx 地方干 xxx

```python
user = input(">>>")
time = input(">>>")
hobby = input(">>>")
print("敬爱可亲的{0},最喜欢在{1}地方,干{2}".format(user,time,hobby))
```



28、制作随机验证码，不区分大小写。
	   流程：
	   用户执行程序
	   给用户显示需要输入的验证码
	   用户输入的值,用户输入的值和显示的值相同时现实正确信息；否则继续生成随机验证码继续等待用户输入

```python
def check_code():
    import random
    checkcode = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp = chr(random.randint(65,90))
        else:
            temp = random.randint(0,9)
        checkcode += str(temp)
    return  checkcode

code = check_code()
print(code)
user_code = input("请输入验证码：")
while True:
    if user_code == code:
        print("验证成功！")
        break
    else:
        code.upper() = check_code()
        print(code)
        user_code = input("请输入验证码：")
```





​												

29、开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符：
				 如 "苍老师"	"东京热"，则将内容替换为 ***

```python
con = input(">>>")
if "fuck" in con or "suck" in con:
    con_new1 = con.replace("fuck","***")
    con_new2 = con_new1.replace("suck","***")
print(con_new2)

```



30、制作表格
				 循环提示用户输入：用户名、密码、邮箱 （要求用户输入的长度不超过 20 个字符，如果超过则只有前 20 个字符有效）
				 如果用户输入 q 或 Q	 表示不再继续输入，将用户输入的内容以表格形式打印

```python
table = ""
print("输入用户名密码邮箱，可以按q或者Q退出")
while True:
    user = input("请输入用户名》")
    if user == "q" or user == "Q":
        break
    elif len(user) > 20:
        user = user[0:19]
    pwd = input("请输入密码》")
    if pwd == "q" or pwd == "Q":
        break
    elif len(pwd) > 20:
        pwd = pwd[0:19]
    mail = input("请输入邮箱》")
    if mail == "q" or mail == "Q":
        break
    elif len(mail) > 20:
        mail = mail[0:19]
    table = table + user + "\t" + pwd + "\t" + mail + "\n"

print(table.expandtabs(20))
```

