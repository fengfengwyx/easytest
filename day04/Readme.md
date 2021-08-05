大家好，我是谭叔。

上期的unittest原理掌握了吗？如果没有，没关系，本期，请跟随我的脚步，通过写出你的第一个自动化测试用例，再来熟悉熟悉。

## 第一条用例

查看【接口环境】【项目文档】【自动化测试用例.xlsx】，写编号为test_add_department_001和test_add_department_002的用例。

![image-20210530202340614](http://pic.testtalking.com/testtalking/image-20210530202340614.png)

![image-20210528160434346](http://pic.testtalking.com/testtalking/20210528160434.png)

新建一个testcase文件夹，创建一个AddDepartment.py文件。

![image-20210603200147351](http://pic.testtalking.com/testtalking/20210603200147.png)

写出新增模块的两条自动化测试用例：

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
import unittest
import json
import requests


class AddDepartment(unittest.TestCase):

    def setUp(self):
        print("{0} 执行前，清除数据库".format(self._testMethodName))

    def tearDown(self):
        print("{0} 执行后，清除数据库".format(self._testMethodName))

    def test_add_department_001(self):
        """新增T01学院"""
        result = requests.post(url='http://127.0.0.1:8099/api/departments/',
                               headers={"Content-Type": "application/json",
                                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"},
                               data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]})
                            )
        # 查看请求的结果
        print(result.status_code,result.text)


    def test_add_department_002(self):
        """重复新增T01学院"""
        result = requests.post(url='http://127.0.0.1:8099/api/departments/',
                               headers={"Content-Type": "application/json",
                                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"},
                               data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]})
                            )
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

## 拆解用例

根据上一期的知识点，一一拆解本条用例。

### 测试用例（case：TestCase）

在这条测试用例TestCase中，有：

- setUp：在执行测试用例之前，初始化数据库（方法下期实现）

  ![image-20210529205053853](http://pic.testtalking.com/testtalking/20210529205053.png)

- test_add_department_001：自动化测试用例

  ![image-20210529205136221](http://pic.testtalking.com/testtalking/20210529205136.png)

- tearDown：在执行测试用例之后，恢复数据库（方法下期实现）

  ![image-20210529205117076](http://pic.testtalking.com/testtalking/20210529205117.png)

### 整理测试用例之一（suite：TestSuite）

你写了新增学院、重复新增学院的用例，这两条用例需要集合到新增模块中，形成一个新增suite（集合）；

套用到unittest上，使用TestSuite集合用例。

![image-20210525232236209](http://pic.testtalking.com/testtalking/20210525232236.png)

### 整理测试用例之二（loader：TestLoader）

此点暂未涉及，下期会说。

### 执行测试用例（runner）

![image-20210525232259750](http://pic.testtalking.com/testtalking/20210525232259.png)

TextTestRunner通过run 方法执行测试用例。

最后，我们看看控制台的输出：

![image-20210529211957834](http://pic.testtalking.com/testtalking/image-20210529211957834.png)

STEP 01：第一次新增前，清除数据库

STEP 02：第一次新增，返回新增成功（无重复results）

STEP 03：第一次新增后，清除数据库

STEP 04：第二次新增前，清除数据库

STEP 05：第二次新增，返回新增失败（有重复results）

STEP 06：第二次新增后，清除数据库

## 问题

但是，在写用例和执行用例的过程中，你是否发现了这些问题？

### 01 请求未封装

URL、Headers、请求体，全在用例层。当用例过多时，代码可阅读性低，且很难维护。

![image-20210525232509162](http://pic.testtalking.com/testtalking/20210525232509.png)

### 02 需要补全清除数据库的方法

![image-20210529212030296](http://pic.testtalking.com/testtalking/image-20210529212030296.png)

### 03 第二条用例依赖第一条用例

即，第一条用例必须执行成功。

此外，第二条用例，不能初始化数据库（这意味着数据丢失）。

![image-20210529211957834](http://pic.testtalking.com/testtalking/image-20210529211957834.png)

### 04 用例集缺乏统一管理和调度

现在的用例集在类文件执行，很麻烦。当查询、修改、删除模块都增加后，需要有一个地方统一控制这些模块的运行。

![image-20210525232520431](http://pic.testtalking.com/testtalking/20210525232520.png)

以上四个问题，下期，咱一起解决。

## 一如既往，做个总结

**01 问题不止于此，部分问题，我会放在后面解决。在这之前，你可以想想，还有哪些问题。**

**02 一定要上手实操。**

