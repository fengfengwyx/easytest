��Һã�����̷�塣

���ڣ��г���Ϣ����һ��򵥵����ݡ�����¼��־��

��Ϊ�ӿ��Զ������Ե������ԣ�д���Զ����ű�������һ��Ὣ�ű����ڷ�������ִ�С�ִ�гɹ����ã���ִ��ʧ�ܣ�����ִ���쳣������ô���أ�

�ٸ�ʵ�ʵ����ӣ���AddDepartment����ģ���У��������������ܵ���ִ���쳣��

- ��ʼ�����ݿ����ʧ��

- ����post�������ʧ��

- ������Ӧ����ʧ��

  ![image-20210603195712767](http://pic.testtalking.com/testtalking/20210603195712.png)

���ǲ�֪��ִ����һ������ʧ�ܣ�Ҳ��֪����һ��ʧ�ܣ��Ե��ر�����

��ˣ�������Ҫ��¼�������־���Եú��б�Ҫ��

## ��װ��־

��common�ļ����´���һ��logger.py�ļ���

![image-20210603205137780](http://pic.testtalking.com/testtalking/20210603205137.png)

��ߣһ���򵥵���־������

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
    # ����¼����־����ౣ��7�����־
    handler = handlers.TimedRotatingFileHandler(filename=("{}logs/et.log".format(ETConfig.TEST_DIR)), when='D', backupCount=7, encoding='utf-8')
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    handler.setFormatter(format_str)
    return log

write_log = logger()
```

## ��¼��־

����������¼����־�ɡ�

### db_funcs.py

![image-20210605222649381](http://pic.testtalking.com/testtalking/image-20210605222649381.png)

### HttpReq.py

![image-20210604145839778](http://pic.testtalking.com/testtalking/20210604145839.png)

### ������

Ϊ����ͳһ�����ά����������wrapers.py���½���һ��write_case_log��װ�η�����

![image-20210605221006837](http://pic.testtalking.com/testtalking/image-20210605221006837.png)

```python
def write_case_log():
    """
    ��¼����������־
    :return:
    """
    def wraper_func(func):
        @wraps(func)
        def inner_func(*args, **kwargs):
            write_log.info('{}��ʼִ��'.format(func.__name__))
            func(*args, **kwargs)
            write_log.info('{}ִ����'.format(args))
            write_log.info('{}����ִ��'.format(func.__name__))
        return inner_func
    return wraper_func
```

Ȼ��������׸�ͷ��

![image-20210605221131801](http://pic.testtalking.com/testtalking/image-20210605221131801.png)

���������Ǳ���ͨ����־�鿴������ִ������ˡ�

![image-20210607173107463](http://pic.testtalking.com/testtalking/20210607173107.png)

����ֹ�ӿ���Ŀ�������ִ����������ӿ�����ʧ�ܣ����ǿ�������־�п���HttpReq��ʧ�ܼ�¼��

![image-20210607173202031](http://pic.testtalking.com/testtalking/20210607173202.png)

## һ������������ܽ�

**��־��¼������ʵ�֣����ֲ��������á��ܵ�˼·���ں��ʵ�λ�üӺ��ʵ���־�����������ܿ��ٶ�λ��**