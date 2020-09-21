[TOC]

# Python全栈学习（10）字符串格式化

## %字符串格式化

```python
#%格式化字符串
msg='i am %s my hobby is %s' % ('lhf','alex')
print(msg)

msg='i am %s my hobby is %s' % ('lhf',1)
msg='i am %s my hobby is %s' % ('lhf',[1,2])
print(msg)
name='lhf'
age=19
msg='i am %s my hobby is %s' % (name,age)
print(msg)

#打印浮点数
tpl = "percent %.2f" % 99.976234444444444444
print(tpl)

#打印百分比
tpl = 'percent %.2f %%' % 99.976234444444444444
print(tpl)

#字典传参
tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
print(tpl)

msg='i am %(name)+60s my hobby is alex' %{'name':'lhf'}
print(msg)

#颜色
msg='i am \033[43;1m%(name)+60s\033[0m my hobby is alex' %{'name':'lhf'}
print(msg)

#分隔符格式化
print('root','x','0','0',sep=':')
# print('root'+':'+'x'+':'+'0','0')
```

## format字符串格式化

```python
#format字符串格式化
tp1 = "I am {},I am {} old,I like {}!".format("sage",18,"reading")
print(tp1)

tp2 = "I am {0},I am {1} old,I like {0}!".format("sage",18,"reading")
print(tp2)

tp1 = "I am {name},I am {age} old,I like {name}!".format(name="sage",age=18)
print(tp1)

tp1 = "I am {name},I am {age} old,I like {name}!".format(**{"name":"job","age":14})
print(tp1)

tp1 = "I am {:s},I am {:d} old".format(*["kaer",15])
print(tp1)

#数字格式化
#二进制，八进制，整形，十六进制，百分比
tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%},{:+.5f}".format(15, 15, 15, 15, 15, 15.87623, 2.012123131)
print(tpl)
'''
numbers: 1111,17,15,f,F, 1587.623000%,+2.01212
'''
```

