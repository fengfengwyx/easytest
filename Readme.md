大家好，我是谭叔。

本期讲解之前，谭叔灵魂拷问一下：**上一期的内容，你实操了吗？**

如果没有，请回退实操，如果有，可继续。

我们来解决上期遗漏的四个问题。

## 解决第一个问题：封装

### 封装配置

为什么要这么做？

**好比千人千面，我不是你，你不是我。**我的配置在你的电脑上不能用，你的配置在我的电脑上不能用。

封装配置后，可以更灵活的运行自动化测试项目。

#### 实操

在easytest主目录下，创建一个config文件夹，再创建一个ProjectConfig.py文件，用于保存该自动化测试项目的配置数据，比如版本号、请求的URL、接口项目地址等。

> 注意：PROJECT_DIR和TEST_DIR，请替换为你本机的接口项目路径和自动化项目路径

![image-20210603225920672](http://pic.testtalking.com/testtalking/20210603225920.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-
class ProjectConfig(object):
    VERSION = "v1.0"
    # 替换为你本地的url地址
    URL = "http://127.0.0.1:8099/api/departments/"
    # 替换为你本地的接口项目路径（注意不是自动化项目路径）
    PROJECT_DIR = "C:\\Users\\010702\\PycharmProjects\\easytest\\接口环境\\"
    # 自动化测试项目目录
    TEST_DIR = "C:\\Users\\010702\\PycharmProjects\\easytest\\"

ETConfig = ProjectConfig()
```

> tips：因本接口自动化项目，相对简单，故采用py文件保存配置。
>
> 但我建议你在做公司项目的自动化测试时，将配置保存在ini、yaml等文件中，并设置.gitignore。也可以部署配置中心服务，以便在不同机器上灵活运行自动化项目。

### 封装请求

为什么要这么做？

**让代码更简洁，更具有可读性，并且更好维护。**

#### 实操

创建common文件夹，并新建一个py文件HttpReq。

![image-20210604161947533](http://pic.testtalking.com/testtalking/20210604161947.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-

import requests

class HttpReq(object):

    def __init__(self):
        self.headers = {"Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
                        }

    # GET 请求
    def get(self, url='', data='', cookies=None):
        response = requests.get(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

    # POST 请求
    def post(self, url='', data='', cookies=None):
        response = requests.post(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

    # PUT 请求
    def put(self, url='', params='', data='', cookies=None):
        response = requests.put(url=url, params=params, data=data, headers=self.headers, cookies=cookies)
        return response

    # DELETE 请求
    def delete(self, url='', data='', cookies=None):
        response = requests.delete(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

ETReq = HttpReq()
```

## 解决第二个问题：补全数据库方法

在common目录下，再新建一个db_funcs.py文件，用于构造数据库相关的方法。

![image-20210604162023809](http://pic.testtalking.com/testtalking/20210604162023.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3
from config.ProjectConfig import ETConfig

def execute_db(sql):
    """
    连接接口项目sqlite数据库，并执行sql语句
    :param sql: sql语句
    :return:
    """
    # 打开数据库连接
    conn = sqlite3.connect("{0}\\studentManagementSystem\\db.sqlite3".format(ETConfig.PROJECT_DIR))
    # 新建游标
    cursor = conn.cursor()
    # 执行sql
    cursor.execute(sql)
    # 获取执行结果
    result = cursor.fetchall()
    # 关闭游标、提交连接、关闭连接
    cursor.close()
    conn.commit()
    conn.close()
    return result


def init_db():
    """
    初始化数据库，删除掉departments的所有数据
    :return:
    """
    execute_db("delete from departments;")

if __name__ == '__main__':
    init_db()
```

## 修改用例

来吧，根据上面的内容，我们将上期的用例，稍作修改。

![image-20210603201236866](http://pic.testtalking.com/testtalking/20210603201236.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
import unittest
import json
from config.ProjectConfig import ETConfig
from day05.easytest.common.db_funcs import init_db
from day05.easytest.common.HttpReq import ETReq

class AddDepartment(unittest.TestCase):

    def setUp(self):
        init_db()

    def tearDown(self):
        init_db()

    def test_add_department_001(self):
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 查看请求的结果
        print(result.status_code,result.text)


    def test_add_department_002(self):
        """重复新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 查看请求的结果
        print(result.status_code,result.text)


if __name__ == '__main__':
    # 构造测试
    suite = unittest.TestSuite()
    suite.addTest(AddDepartment("test_add_department_001"))
    suite.addTest(AddDepartment("test_add_department_002"))
    # 本地测试用，可以在控制台看到日志
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)
```

相较之前，是不是简化了许多？

## 解决第三个问题：依赖

作为面试中常问的接口自动化依赖问题，解决方法有很多种。

针对当前自动化实战中遇到的问题，我们可采用：

### 方法一

在test_add_department_002运行请求代码前，先执行一次test_add_department_001，准备好前置数据。

![image-20210529214327964](http://pic.testtalking.com/testtalking/image-20210529214327964.png)

运行后，test_add_department_002确实拿到了预期结果。

![image-20210529214412470](http://pic.testtalking.com/testtalking/image-20210529214412470.png)

### 方法二

基于unittest的框架特性，将setUp和tearDown更换为类级别的，setUpClass、tearDownClass。即，在执行AddDepartment这个用例类（新增模块）之前和之后，分别做清库操作，而不是在每一个测试用例的前后做清库。

![image-20210529215526865](http://pic.testtalking.com/testtalking/image-20210529215526865.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
import unittest
import json
from config.ProjectConfig import ETConfig
from day05.easytest.common.db_funcs import init_db
from day05.easytest.common.HttpReq import ETReq


class AddDepartment(unittest.TestCase):

    # def setUp(self):
    #     init_db()
    #
    # def tearDown(self):
    #     init_db()

    @classmethod
    def setUpClass(cls):
        print("{0} 执行前，清除数据库".format(cls.__name__))
        init_db()

    @classmethod
    def tearDownClass(cls):
        print("{0} 执行后，清除数据库".format(cls.__name__))
        init_db()

    def test_add_department_001(self):
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 查看请求的结果
        print(result.status_code, result.text)


    def test_add_department_002(self):
        """重复新增T01学院"""
        # self.test_add_department_001() # 或者贴一段新增T01的请求代码ETReq.post
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 查看请求的结果
        print(result.status_code,result.text)


if __name__ == '__main__':
    # 构造测试
    suite = unittest.TestSuite()
    suite.addTest(AddDepartment("test_add_department_001"))
    suite.addTest(AddDepartment("test_add_department_002"))
    # 本地测试用，可以在控制台看到日志
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)
```

看看效果：

![image-20210529215556800](http://pic.testtalking.com/testtalking/image-20210529215556800.png)

STEP 01：执行所有case前，清除数据库

STEP 02：执行第一条case，返回新增成功（无重复results）

STEP 03：执行第二条case，返回新增失败（有重复results）

STEP 04：执行所有case后，清除数据库

> tips：实际工作中的依赖问题，没这般简单。

## 解决第四个问题：调度

打开用例excel，根据用例，新增两条查询的case。

![image-20210529220115378](http://pic.testtalking.com/testtalking/image-20210529220115378.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
import unittest
from config.ProjectConfig import ETConfig
from day05.easytest.common.HttpReq import ETReq


class QueryDepartment(unittest.TestCase):
    def test_query_department_001(self):
        """查询所有学院"""
        result = ETReq.get(url=ETConfig.URL)
        # 查看请求的结果
        print(result.status_code,result.text)


    def test_query_department_002(self):
        """查询T01学院（存在）"""
        result = ETReq.get(url=ETConfig.URL + 'T01')
        # 查看请求的结果
        print(result.status_code,result.text)


if __name__ == '__main__':
    # 构造测试
    suite = unittest.TestSuite()
    suite.addTest(QueryDepartment("test_query_department_001"))
    suite.addTest(QueryDepartment("test_query_department_002"))
    # 本地测试用，可以在控制台看到日志
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)
```

还记得上一期，讲整理用例环节，遗漏的TestLoader吗？

![image-20210530202119488](http://pic.testtalking.com/testtalking/image-20210530202119488.png)

本期，我们便会用到它——在unittest框架中，使用TestLoader简单调度测试用例的执行。

新建main文件夹并创建run_case的py文件。

![image-20210603201317931](http://pic.testtalking.com/testtalking/20210603201317.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-
import unittest

# 创建测试集合
suite = unittest.TestSuite()

# 识别所有Department结尾的py文件为测试用例
tests = unittest.defaultTestLoader.discover('..\\testcase', pattern='*Department.py')

# 运行测试用例
suite.addTest(tests)
runner = unittest.TextTestRunner()
test_result = runner.run(suite)
```

运行run_case.py后，TestLoader会加载 testcase（测试用例） 到 testsuite（测试用例集） 中，再运行测试用例。

在控制台查看结果，达到了我们的预期效果。

![image-20210530203539272](http://pic.testtalking.com/testtalking/image-20210530203539272.png)

> tips：TestLoader还有很多其他用法，具体使用，可自行百度：unittest TestLoader的使用方法。

## 问题

问题接踵而至。

每一次用例执行后，我们需要人肉去判定用例的执行结果，这违背了自动化测试的初衷。

如何解决呢？我们下期再见。

## 一如既往，做个总结

**01 实际工作中的接口请求，还有Session、Cookies、Token鉴权，比该项目复杂，但思路大体差不多。**

**02 再提醒一次：实操，实操，实操。** 

