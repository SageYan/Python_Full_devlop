[TOC]



# Python全栈学习（28）内置模块练习

## 算法练习：二分查找

```python
'''
从有序列表中找到一个值索引位置的位置
'''

def dichotomy(num, lst):
    pos = round(len(lst) / 2)
    while True:
        if num < lst[pos]:
            pos = round(pos / 2)
        elif num > lst[pos]:
            pos = round((len(lst) - pos - 1) / 2 + pos)
        else:
            return pos


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 36, 46, 58, 69]
print(dichotomy(58, lst))
print(lst.index(58))
```

## sys.argv模块练习

```python
'''
写一个python脚本,在cmd里执行,实现：
python xxx.py 用户名 密码 cp 文件路径 目的地址
python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
python xxx.py alex sb rm D:\python_22\day22
python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23
'''

import os
import sys
import shutil


def os_cmd():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':

        print('''
        脚本使用方法如下：
        python xxx.py 用户名 密码 命令 原文件路径 目的地址

        其中命令支持：
        [cp 复制，rename 重命名，rm 删除， mkdir 创建目录]

        ''')
    elif len(sys.argv) >= 5:
        if sys.argv[1] == 'alex' and sys.argv[2] == 'sb':
            if len(sys.argv) == 6 and sys.argv[3] == 'cp':
                if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
                    filename = os.path.basename(sys.argv[4])
                    newpath = os.path.join(sys.argv[5], filename)
                    shutil.copy2(sys.argv[4], newpath)
                    print("复制到{}命令执行成功".format(newpath))
                else:
                    print("输入路径有误！")
            elif len(sys.argv) == 6 and sys.argv[3] == 'rename':
                if os.path.exists(sys.argv[4]) and os.path.exists(os.path.dirname(sys.argv[5])):
                    os.rename(sys.argv[4], sys.argv[5])

    else:
        print("您输入的命令内容有误！")


os_cmd()
```
