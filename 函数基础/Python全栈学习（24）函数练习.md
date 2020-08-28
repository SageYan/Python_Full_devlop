[TOC]



# Python全栈学习（24）函数练习

### 投票函数

```python
'''
lst = ['复仇者联盟4', '驯龙高手3', '金瓶梅', '老男孩', '大话西游']
由用户给每⼀个电影投票.最终将该⽤户投票信息公布出来。
要求：
用户可以持续投票，用户输入序号，进行投票。比如输入序号 1，给金瓶梅投票1。
每次投票成功，显示给哪部电影投票成功。
退出投票程序后，要显示最终每个电影的投票数。
建议最终投票的结果为这种形式：
{'⾦瓶梅': 0, '复仇者联盟4': 0, '驯龙高手3': , '老男孩': 0,'大话西游':0}
'''
lst = ['复仇者联盟4', '驯龙高手3', '金瓶梅', '老男孩', '大话西游']
dic = dict.fromkeys(lst, 0)

while 1:

    for idx, val in enumerate(lst):
        print('序号：{} 电影名称：{}'.format(idx + 1, val))
    num = input("请为您喜欢的电影输入对应序号投票：").strip()
    if num.isdecimal():
        num = int(num)
        if num > 0 and num <= len(lst):
            dic[lst[num - 1]] += 1
        else:
            print("超出范围，重新输入")
    elif num.upper() == "Q":
        print("投票成功，退出")
        break
    else:
        print("输入有误，请重新输入")

for name, vote in dic.items():
    print("电影：{}，得票数：{}\n".format(name, vote))
```

### 文件处理成所需数据类型

```python
'''
id,name,age,phone,job
1,alex,22,13651054608,IT
2,wusir,23,13304320533,Tearcher
3,taibai,18,1333235322,IT
4,cong,23,1333235312,DBA

[{'id': '1', 'job': 'IT', 'name': 'alex', 'phone': '13651054608', 'age': '22'}, {'id': '2', 'job': 'Tearcher', 'name': 'wusir', 'phone': '13304320533', 'age': '23'}, {'id': '3', 'job': 'IT', 'name': 'taibai', 'phone': '1333235322', 'age': '18'}, {'id': '4', 'job': 'DBA', 'name': 'cong', 'phone': '1333235312', 'age': '23'}]

'''

lst = []
with open('namelist','r',encoding='utf8') as f1:
    title = f1.__next__().strip().split(",")

    #print(dic)
    for line in f1:
        #dic = dict.fromkeys(title)
        dic = {}
        line_lst = line.strip().split(',')
        print(line_lst)
        for idx in range(len(line_lst)):
            dic[title[idx]] = line_lst[idx]

        lst.append(dic)
print(lst)
```

### 数据源构建成所需格式

```python
'''
list3 = [
    {"name": "alex", "hobby": "抽烟"},
    {"name": "alex", "hobby": "喝酒"},
    {"name": "alex", "hobby": "烫头"},
    {"name": "alex", "hobby": "Massage"},
    {"name": "wusir", "hobby": "喊麦"},
    {"name": "wusir", "hobby": "hiphop"},
    {"name": "wusir", "hobby": "出差"},
    {"name": "Sage", "hobby": "soccer"},
    {"name": "Sage", "hobby": "sleep"},
]

list4 = [
    {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
    {"name": "wusir", "hobby_list": ["喊麦", "街舞", "出差"]},
]

'''
#直接构建
l1 = []
for s_dic in list3:
    for t_dic in l1:
        if s_dic['name'] == t_dic['name']:
            t_dic['hobby_list'].append(s_dic['hobby'])
            break
    else:
        l1.append({'name':s_dic['name'],'hobby_list':[s_dic['hobby'], ]})
print(l1)

PS: for ... else ...
    #如果for循环正常结束，else中语句执行。如果有break的，则不执行else语句
    
#构建特殊的数据结构。
'''
dic = {'alex': {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
       "wusir": {"name": "wusir", "hobby_list": ["喊麦", "街舞", "出差"]}
       }
'''

print(list(dic.values()))
dic = {}
for i in list3:
    if i['name'] not in dic:
        dic[i['name']] = {'name': i['name'], 'hobby_list': [i['hobby'], ]}
    else:
        dic[i['name']]['hobby_list'].append(i['hobby'])
print(list(dic.values()))


```



