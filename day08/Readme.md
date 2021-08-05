大家好，我是谭叔。

本期，中场休息，讲一点简单的内容——记录日志。

因为接口自动化测试的特殊性，写完自动化脚本后，我们一般会将脚本放在服务器上执行。执行成功还好，但执行失败，或者执行异常，该怎么办呢？

举个实际的例子，在AddDepartment新增模块中，以下三步都可能导致执行异常：

- 初始化数据库可能失败

- 发送post请求可能失败

- 解析响应可能失败

  ![image-20210603195712767](http://pic.testtalking.com/testtalking/20210603195712.png)

我们不知道执行哪一条用例失败，也不知道哪一步失败，显得特被动。

因此，根据需要记录合理的日志，显得很有必要。

## 封装日志

在common文件夹下创建一个logger.py文件。

![image-20210603205137780](http://pic.testtalking.com/testtalking/20210603205137.png)

手撸一个简单的日志方法：

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
from logging import handlers
from config.ProjectConfig import ETConfig

def logger():
    os.makedirs("{}logs".format(ETConfig.TEST_DIR), exist_ok=True)
    log = logging.getLogger("{}logs/et.log".format(ETConfig.TEST_DIR))
    format_str = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s', '%Y-%m-%d %H:%M:%S')
    # 按天录入日志，最多保存7天的日志
    handler = handlers.TimedRotatingFileHandler(filename=("{}logs/et.log".format(ETConfig.TEST_DIR)), when='D', backupCount=7, encoding='utf-8')
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    handler.setFormatter(format_str)
    return log

write_log = logger()
```

## 记录日志

接下来，记录下日志吧。

### db_funcs.py

![image-20210605222649381](http://pic.testtalking.com/testtalking/image-20210605222649381.png)

### HttpReq.py

![image-20210604145839778](http://pic.testtalking.com/testtalking/20210604145839.png)

### 用例层

为方便统一管理和维护，我们在wrapers.py下新建了一个write_case_log的装饰方法。

![image-20210605221006837](http://pic.testtalking.com/testtalking/image-20210605221006837.png)

```python
def write_case_log():
    """
    记录用例运行日志
    :return:
    """
    def wraper_func(func):
        @wraps(func)
        def inner_func(*args, **kwargs):
            write_log.info('{}开始执行'.format(func.__name__))
            func(*args, **kwargs)
            write_log.info('{}执行中'.format(args))
            write_log.info('{}结束执行'.format(func.__name__))
        return inner_func
    return wraper_func
```

然后给用例套个头：

![image-20210605221131801](http://pic.testtalking.com/testtalking/image-20210605221131801.png)

这样，我们便能通过日志查看用例的执行情况了。

![image-20210607173107463](http://pic.testtalking.com/testtalking/20210607173107.png)

当中止接口项目服务后，再执行用例，因接口请求失败，我们可以在日志中看到HttpReq的失败记录。

![image-20210607173202031](http://pic.testtalking.com/testtalking/20210607173202.png)

## 一如既往，做个总结

**日志记录很容易实现，但又不容易做好。总的思路是在合适的位置加合适的日志，遇到问题能快速定位。**