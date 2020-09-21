[TOC]



# Python全栈学习（26）re模块

## 初识正则

```python
正则就是用一些具有特殊含义的符号组合到一起（称为正则表达式）来描述字符或者字符串的方法。或者说：正则就是用来描述一类事物的规则。（在Python中）它内嵌在Python中，并通过 re 模块实现。正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。

# 能做什么
    # 1.检测一个输入的字符串是否合法  -- web开发项目 表单验证
        # 用户输入一个内容的时候,我们要提前做检测
        # 能够提高程序的效率并且减轻服务器的压力
    # 2.从一个大文件中找到所有符合规则的内容 -- 日志分析\爬虫
        # 能够高效的从一大段文字中快速找到符合规则的内容
```

## 正则表达式

### 字符组

```python
在同一个位置可能出现的各种字符组成了一个字符组，在正则表达式中用[]表示，字符分为很多类，比如数字、字母、标点等等。
#比如：你现在要求一个位置"只能出现一个数字",那么这个位置上的字符只能是0、1、2...9这10个数之一
```

| `正则`         | `待匹配字符` | `匹配结果` | `说明`                                                       |
| -------------- | ------------ | ---------- | ------------------------------------------------------------ |
| `[0123456789]` | `8`          | `True`     | `在一个字符组里枚举合法的所有字符，字符组里的任意一个字符和"待匹配字符"相同都视为可以匹配` |
| `[0123456789]` | `a`          | `False`    | `由于字符组中没有"a"字符，所以不能匹配`                      |
| `[0-9]`        | `7`          | `True`     | `也可以用-表示范围,[0-9]就和[0123456789]是一个意思`          |
| `[a-z]`        | `s`          | `True`     | `同样的如果要匹配所有的小写字母，直接用[a-z]就可以表示`      |
| `[A-Z]`        | `B`          | `True`     | `[A-Z]就表示所有的大写字母`                                  |
| `[0-9a-fA-F]`  | `e`          | `True`     | `可以匹配数字，大小写形式的a～f，用来验证十六进制字符`       |

### 元字符

```python
元字符使正则表达式具有处理能力
```

| `元字符` | `匹配内容`                                                   |
| -------- | ------------------------------------------------------------ |
| .        | 匹配除换行符以外的任意字符                                   |
| \w       | 匹配字母或数字或下划线                                       |
| \s       | 匹配任意的空白符                                             |
| \d       | 匹配数字                                                     |
| \n       | 匹配一个换行符                                               |
| \t       | 匹配一个制表符                                               |
| \b       | 匹配一个单词的边界：o\b匹配以o为结尾的单词                   |
| ^        | 匹配字符串的开始                                             |
| $        | 匹配字符串的结尾                                             |
| \W       | `匹配非字母或数字或下划线`                                   |
| \D       | `匹配非数字`                                                 |
| \S       | `匹配非空白符`                                               |
| a\|b     | `匹配字符a或字符b`，如果两个规则有重叠部分,总是把长的放在左侧 |
| ()       | `匹配括号内的表达式，也表示一个组`                           |
| [...]    | `匹配字符组中的字符`                                         |
| [^...]   | `匹配除了字符组中字符的所有字符`                             |

### 量词

| `量词` | `用法说明`       |
| ------ | ---------------- |
| {n}    | 重复n次          |
| {n,}   | 重复n次或更多次  |
| {n,m}  | 重复n到m次       |
| ?      | 重复零次或一次   |
| +      | 重复一次或更多次 |
| *      | 重复零次或更多次 |

```c++
   // 整数 \d+
   // 小数 \d+\.\d+
   // 分组的作用 : \d+(\.\d+)?
```

```python
#匹配手机号
# 判断用户输入的内容是否合法,如果用户输入的对就能查到结果,如果输入的不对就不能查到结果
    ^1[3-9]\d{9}$
# 从一个大文件中找到所有符合规则的内容
    1[3-9]\d{9}
```

### 贪婪匹配机制

```python
#贪婪匹配：在满足匹配时，匹配尽可能长的字符串，默认情况下，采用贪婪匹配
例如：
.*X 表示匹配任意字符，任意多次数，遇到最后一个x为止
```

### 惰性匹配

```python
#在量词范围允许的情况下, 尽量少匹配内容
'''
*? 重复任意次，但尽可能少重复
+? 重复1次或更多次，但尽可能少重复
?? 重复0次或1次，但尽可能少重复
{n,m}? 重复n到m次，但尽可能少重复
{n,}? 重复n次以上，但尽可能少重复
'''
#.*?x
表示取前面任意长度的字符，直到第一个x出现
```

### 转义符

```python
取消一个元字符的特殊意义有两种方法：
  # 在这个元字符前面加 "\"
  # 对一部分字符生效,把这个特殊意义字符放在字符组 "[]" 里
    比如：[.()+?*]
```

### 练习

```python
# 18/15位的身份证号
'''
^([1-9]\d{16}[0-9x]|[1-9]\d{14})$
[1-9]\d{14}(\d{2}[\dx])?
'''

#IP匹配
1. 本文匹配为(1-255).(0-255).(0-255).(1-254)
ip_match = r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9]|0?[1-9]0)\.)(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(?:25[0-4]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9]|0?[1-9]0)$"

2. 本文匹配为 (不以0开头的多位整数 0-255).(0-255).(0-255).(0-255)
ret = re.search(r'^(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])$',ip)
print(ret)

ret2 = re.findall(r'^(?:(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])$', '10.199.200.11')
print(ret2)

```

## re模块

### 常用方法

#### findall

```python
#findall
'''
获取所有符合条件的,优先显示分组中的内容
'''
import re
ret = re.findall('9\d\d','19740ash93010uru')
print(ret) #['974', '930']

ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['oldboy']  这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,使用 ?: 取消分组优先权限

ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['www.oldboy.com']


#练习：
import re
with open('content','r',encoding='utf8') as f1:
    c1 = f1.read()
    ret = re.findall('<span class="title">(.*)</span>\s*(?:<span class="title">.*</span>)?', c1)
    print(ret,len(ret)) #?: 取消分组优先权限
或
import re
with open('content','r',encoding='utf8') as f1:
    c1 = f1.read()
    ret = re.findall('<span class="title">(\w+)</span>', c1)
    print(ret,len(ret)) # \w :不匹配非word字符

    
'''
['肖申克的救赎', '霸王别姬', '阿甘正传', '这个杀手不太冷', '泰坦尼克号', '美丽人生', '千与千寻', '辛德勒的名单', '盗梦空间', '忠犬八公的故事', '海上钢琴师', '星际穿越', '楚门的世界', '三傻大闹宝莱坞', '机器人总动员', '放牛班的春天', '大话西游之大圣娶亲', '熔炉', '疯狂动物城', '无间道', '龙猫', '教父', '当幸福来敲门', '怦然心动', '触不可及'] 25
'''
PS:
    '''
    # 如果查找的内容在一个复杂的环境中
	# 要查的内容并没有一个突出的 与众不同的特点 甚至会和不需要的杂乱的数据混合在一起
	# 这个时候我们就需要把所有的数据都统计出来,然后对这个数据进行筛选,把需要的数据对应的正则表达式用 () 标记出来
    '''
```

#### search

```python
'''
search 只取第一个符合条件的,没有优先显示
    得到的结果是一个变量
        变量.group() 的结果 完全和 变量.group(0)的结果一致
        变量.group(n) 的形式来指定获取第n个分组中匹配到的内容
'''
ret = re.search('9(\d)(\d)','19740ash93010uru')
print(ret)  
if ret:
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))
'''
974
7
4
'''

#利用group分组得到理想结果
#例子：

exp = '2-3*(5+6)'
res = re.search(r'\d+[+]\d',exp)
a,b = res.group().split('+')
print(int(a)+int(b))
或
exp = '2-3*(5+6)'
ret = re.search('(\d+)[+](\d+)',exp)
print(int(ret.group(1))+int(ret.group(2)))

```

#### split

```python
import re
res=re.split('\d+','boo2233sage')
print(res)
ret = re.split('\d(\d)(\d)', 'amy123sage')
print(ret)
#没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项
'''
['boo', 'sage']
['amy', '2', '3', 'sage']
'''
```

#### sub subn

```python
import re
ret = re.sub('\d+','H','1ello 2ex',1)
print(ret)
print(re.sub(r'([a-zA-Z]+)(\s+)([a-zA-Z]+)(\s+)([a-zA-Z]+)', r'\5\2\3\4\1', 'amy is good'))
#"r'\5\2\3\4\1'"  repl可以是字符串，也可以是函数
例：
import re
 
def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456"
 
	def _add111(matched):
    	intStr = matched.group("number")     #123
    	intValue = int(intStr)
    	addedValue = intValue + 111          #234
    	addedValueStr = str(addedValue)
   		return addedValueStr
     
	replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr)
	print("replacedStr=",replacedStr)       #hello 234 world 567

==================================================================================
ret2 = re.subn('\d+','a','123Amy234')
print(ret2)

'''
Hello 2ex
good is amy 
('aAmya', 2)
'''
```

#### match

```python
import re
ret = re.match('SA','SAGE')
ret2 = re.match('SA','1SAGE')
print(ret.group(),ret,ret2)

'''
SA  <_sre.SRE_Match object; span=(0, 2), match='SA'>  None
'''
# 同search,不过在字符串开始处进行匹配，完全可以用search+^代替match
```

#### compile

```python
#预先编译正则表达式，减少多次解析同一个正则表达式的时间

import re
ip_cmpl = re.compile('^(?:(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])$')
ret = re.findall(ip_cmpl,'10.68.200.89')
ret2 = re.findall(ip_cmpl,'10.68.90.89')
print(ret,ret2)
'''
['10.68.200.89'] ['10.68.90.89']
'''
或
ip_comp = re.compile('^(?:(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])$')
ip1 = '10.68.200.89'
ip2 = '100.88.1.99'

print(ip_comp.search(ip1).group())
print(ip_comp.search(ip2).group())
'''
10.68.200.89
100.88.1.99
'''
```

#### finditer

```python
#finditer返回一个存放匹配结果的迭代器
import re

res = re.finditer('\d', '1S2g4amy12boo13')
print(res)
print(next(res))
print(next(res).group())
print([i.group() for i in res])
'''
<callable_iterator object at 0x00000194DCC6ADA0> 
<_sre.SRE_Match object; span=(0, 1), match='1'>
2
['4', '1', '2', '1', '3']
'''
```

### 分组命名

```python
# 分组命名 (?P<组名>正则) (?P=组名)
例：
import re
ret = re.search(r"<(?P<name>\w+)>.*<(?P=name)>","<Sage>&&&helloAMY}}}}<Sage>")
print(ret)
print(ret.group('name'))

'''
<_sre.SRE_Match object; span=(0, 27), match='<Sage>&&&helloAMY}}}}<Sage>'>
Sage
'''
```

### flag

```python
re.I
    IGNORECASE
    忽略字母大小写

re.L
    LOCALE
    影响 “w, “W, “b, 和 “B，这取决于当前的本地化设置。

re.M
    MULTILINE
    使用本标志后，‘^’和‘$’匹配行首和行尾时，会增加换行符之前和之后的位置。

re.S
    DOTALL
    使 “.” 特殊字符完全匹配任何字符，包括换行；没有这个标志， “.” 匹配除了换行符外的任何字符。

re.X
    VERBOSE
    当该标志被指定时，在 RE 字符串中的空白符被忽略，除非该空白符在字符类中或在反斜杠之后。
    它也可以允许你将注释写入 RE，这些注释会被引擎忽略；
    注释用 “#”号 来标识，不过该符号不能在字符串或反斜杠之后。

```

## 练习：计算器

```python
#!-*- coding:utf-8 -*-
#__anthor__:"Klay Zhu"
#date: 2018/7/13
import re
PREC = '{:+.5f}'#计算精度 5代表5位小数
obj_mul = re.compile(r"(-?\d+\.?\d*)\*(-?\d+\.?\d*)") # 乘法
obj_div = re.compile(r"(-?\d+\.?\d*)/(-?\d+\.?\d*)")  # 除法
obj_add = re.compile(r"(-?\d+\.?\d*)\+(-?\d+\.?\d*)") # 加法
obj_sub = re.compile(r"(-?\d+\.?\d*)-(-?\d+\.?\d*)")  # 减法
obj_f   = re.compile(r"\(?\+?-?\d+\)?")               # 检查括号内是否运算完毕规则
obj_k   = re.compile(r"\([^()]+\)")                   # 寻找最内层括号规则
obj_che = re.compile(r"[^0-9+\-*/()\s.]")             # 匹配输入非法字符

def rm_SP(string):
    """
    去除符号
    :param str:
    :return:
    """
    string = re.sub('\+\+','+',string)
    string = re.sub('--', '+', string)
    string = re.sub('\+-', '-', string)
    string = re.sub('-\+', '-', string)
    string = re.sub('/\+', '/', string)
    string = re.sub('\*\+', '*', string)
    string = re.sub('^\+', '', string)
    return string

def count(string):
    """
    计算没有括号的式子
    :param string:
    :return:
    """
    string = rm_SP(string)
    while True:
        if obj_div.search(string) :# 除法(必须先判断)
            exp = re.split(r'/',obj_div.search(string).group())
            answer = float(exp[0]) / float(exp[1])
            string = obj_div.sub(PREC.format(answer),string,1)
        elif obj_mul.search(string) :# 乘法
            exp = re.split(r'\*', obj_mul.search(string).group())
            answer = float(exp[0]) * float(exp[1])
            string = obj_mul.sub(PREC.format(answer), string,1)
        elif obj_add.search(string) :# 加法
            exp = re.split(r'\+', obj_add.search(string).group())
            answer = float(exp[0]) + float(exp[1])
            string = obj_add.sub(PREC.format(answer), string,1)
        elif obj_sub.search(string) :# 减法
            exp = re.split(r'-', obj_sub.search(string).group())
            if exp[0] =="":#前面有负号的时候
                answer = 0-float(exp[1]) - float(exp[2])
                string = obj_sub.sub(PREC.format(answer), string, 1)
            else:
                answer = float(exp[0]) - float(exp[1])
                string = obj_sub.sub(PREC.format(answer), string,1)
        elif obj_f.search(string):# 结束循环
            string = re.sub('\(|\)|', '', string)
            return string
        string = rm_SP(string) #去除多余的符号


def rm_PAR(string):
    """
    计算括号里
    :param string:
    :return:
    """
    string = rm_SP(string)
    list_m = obj_k.findall(string)
    list_map= map(count,list_m)
    ##map处理所有列表
    
    for i in range(len(list_m)):
        string = string.replace(list_m[i],list_map.__next__(),1)    
    return string

def checkout(string):
    """
    校验输入是否合法
    :param string:
    :return:
    """
    if len(re.findall('\(',string)) != len(re.findall('\)',string)):
        print("括号不成对")
        exit()
    elif obj_che.findall(string) != [] :
        print(obj_che.findall(string))
        print("输入中有非法字符")
        exit()

def main(string):
    """
    主函数，循环计算
    :param string:
    :return:
    """
    checkout(string)
    string = re.sub('\s', '', string) #去掉空格
    while True:
        if obj_k.search(string):#是否还存在括号
            string = rm_PAR(string)
            continue
        answer = count(string)
        return answer



if __name__ == '__main__':
    string = r'2 * 60/17 - 30 + (-40.0/5) * (9-2*5/2+9/-3*10/4*2+10*5/5 -(-4*3)) -(-4*3)/(16-3*2)'#-236.80000
    # string = input("请输入需要计算的式子：")
    answer = main(string)
    print("最后答案：", answer)



```

