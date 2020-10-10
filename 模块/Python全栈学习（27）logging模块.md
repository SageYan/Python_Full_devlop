[TOC]



# Python全栈学习（26）logging模块

## logging使用场景

```python
 1.用来记录用户的行为 - 数据分析
 2.用来记录用户的行为 - 操作审计
 3.排查代码中的错误
```

## 简单配置

### 日志级别

```python
import logging
logging.debug('debug message')          # 调试
logging.info('info message')            # 信息
logging.warning('warning message')      # 警告
logging.error('error message')          # 错误
logging.critical('critical message')    # 严重

'''
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message
'''
PS:
    默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）。
    默认的日志格式为日志级别：  Logger名称：用户输出消息
```

### 基本类

```python
Loggers ：日志器，负责开放接口来调用功能，比如它负责添加Handlers和Filters 
Handlers  ：负责日志记录的传输目的地，比如有FileHandler(写入目标为文件)和StreamHandler（写入目标为流，默认为标准输出流）
Filters ：负责过滤哪些日志是要输出的 
Formatters ：负责对日志输出格式的格式化
```

#### logger对象的基本配置

```python

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

