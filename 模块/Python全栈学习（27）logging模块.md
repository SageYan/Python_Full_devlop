[TOC]



# Python全栈学习（26）logging模块

## logging使用场景

```python
 1.用来记录用户的行为 - 数据分析
 2.用来记录用户的行为 - 操作审计
 3.排查代码中的错误
```

## logging模块简介

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

### logging模块的使用方式介绍

#### 使用logging提供的模块级别的函数

```python
logging所提供的模块级别的日志记录函数也是对logging日志系统相关类的封装而已。
其中logging.basicConfig(**kwargs)函数用于指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信息，其他几个都是用于记录各个级别日志的函数。
```



| 函数                                   | 说明                                 |
| -------------------------------------- | ------------------------------------ |
| logging.debug(msg, *args, **kwargs)    | 创建一条严重级别为DEBUG的日志记录    |
| logging.info(msg, *args, **kwargs)     | 创建一条严重级别为INFO的日志记录     |
| logging.warning(msg, *args, **kwargs)  | 创建一条严重级别为WARNING的日志记录  |
| logging.error(msg, *args, **kwargs)    | 创建一条严重级别为ERROR的日志记录    |
| logging.critical(msg, *args, **kwargs) | 创建一条严重级别为CRITICAL的日志记录 |
| logging.log(level, *args, **kwargs)    | 创建一条严重级别为level的日志记录    |
| logging.basicConfig(**kwargs)          | 对root logger进行一次性配置          |



#### logging模块的四大组件

| 组件       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| loggers    | 提供应用程序代码直接使用的接口                               |
| handlers   | 用于将日志记录发送到指定的目的位置                           |
| filters    | 提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略） |
| formatters | 用于控制日志信息的最终输出格式                               |

```python
说明： logging模块提供的模块级别的那些函数实际上也是通过这几个组件的相关实现类来记录日志的，只是在创建这些类的实例时设置了一些默认值。
```

## 使用logging提供的模块级别的函数记录日志

```python
logging.basicConfig(level=logging.DEBUG,filename='loginfo',
                    format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

'''
2020-10-14 14:56:11 PM - root - DEBUG[line :15]-log2:  This is a debug log.
2020-10-14 14:56:11 PM - root - INFO[line :16]-log2:  This is a info log.
2020-10-14 14:56:11 PM - root - WARNING[line :17]-log2:  This is a warning log.
2020-10-14 14:56:11 PM - root - ERROR[line :18]-log2:  This is a error log.
2020-10-14 14:56:11 PM - root - CRITICAL[line :19]-log2:  This is a critical log.
'''
```

## logging模块日志流处理流程

### 1.  组件之间的关系描述

```python
1 日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；
2 不同的处理器（handler）可以将日志输出到不同的位置；
3 日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
4 每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
5 每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。

简单点说就是：日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。
```

### 2.  logging日志模块相关类使用方法举例

```python
需求：
1）要求将所有级别的所有日志都写入磁盘文件中
2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
4）要求all.log在每天凌晨进行日志切割

实现
import logging
import logging.handlers
import datetime

#logging.getLogger()方法创建logger对象
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)
#设置handler对象
#TimedRotatingFileHandler 按照时间切分日志
all_handler = logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',backupCount=7,encoding='utf-8',atTime=datetime.time(0,0,0,0))
all_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
#RotatingFileHandler 按照大小切割日志
err_handler = logging.handlers.RotatingFileHandler('err.log',maxBytes=1024,backupCount=5)
err_handler.setLevel(logging.ERROR)
err_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s'))
#增加屏幕输出handler
s_handler = logging.StreamHandler()

#为该logger对象添加 handler对象
logger.addHandler(all_handler)
logger.addHandler(err_handler)
logger.addHandler(s_handler)
#测试
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
```
