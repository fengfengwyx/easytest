大家好，我是谭叔。

经历过几期学习，你是否已感到疲惫？

如果是，谭叔建议你休息一天，再阅读一遍01-06，实操动手练习下。

本期，谭叔讲个看起来简单，其实也不那么简单的内容——跳过用例执行。

在实际的接口测试中，如果某条用例不满执行条件，我们无需执行它。举个例子，A用例和B用例时依赖用例，即B用例依赖于A用例执行成功，而当A用例执行失败后，B用例执行也会失败（不是因为本身失败，而是因为A导致的）。

于是，在最终的用例执行统计中，B被统计成失败用例，然而却并不是这样。

针对这种情况，在unittest中，你可以使用skip跳过执行。

## 基础跳过

unittest默认的有四种跳过方式（以装饰器实现）。

skip的使用很简单，如图所示。代码我也贴在了项目中，你可以执行试一试，理解skip装饰器的用法。

![image-20210603201414069](http://pic.testtalking.com/testtalking/20210603201414.png)

回到之前的实操中，我们是不是遇到过这种场景：

如果test_add_department_001用例（新增T01学院）执行失败，test_add_department_002（重复新增T01学院）没必要再执行。

此时，我们需要跳过test_add_department_002。

但是，unittest的这四种skip方式无法满足我们的需求，因为skip无法以用例作为入参。

该怎么办？

## 封装跳过

在common文件夹下，新建一个wrapers.py文件，用来封装跳过方法。

![image-20210603201430204](http://pic.testtalking.com/testtalking/20210603201430.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from functools import wraps

def skip_related_case(related_case_name=''):
    """
    AB关联用例
    如果A用例跳过执行、执行报错、断言失败，则B用例不执行
    :param related_case_name: 关联用例A的名字
    :return:
    """
    def wraper_func(func):
        @wraps(func)
        def inner_func(*args, **kwargs):
            fail_cases = str([fail[0] for fail in args[0]._outcome.result.failures])
            error_cases = str([error[0] for error in args[0]._outcome.result.errors])
            skip_cases = str([error[0] for error in args[0]._outcome.result.skipped])
            if (related_case_name in fail_cases):
                reson = "{}断言失败，跳过执行{}用例".format(related_case_name, func.__name__)
                test = unittest.skipIf(True, reson)(func(*args, **kwargs))
            elif (related_case_name in error_cases):
                reson = "{}执行报错，跳过执行{}用例".format(related_case_name, func.__name__)
                test = unittest.skipIf(True, reson)(func(*args, **kwargs))
            elif (related_case_name in skip_cases):
                reson = "{}跳过未执行，跳过执行{}用例".format(related_case_name, func.__name__)
                test = unittest.skipIf(True, reson)(func(*args, **kwargs))
            else:
                test = func
            return test(*args, **kwargs)
        return inner_func
    return wraper_func
```

回到用例类，尝试给test_add_department_002装饰上我们刚刚创建的skip_related_case方法。

```python
    @skip_related_case('test_add_department_001')
    def test_add_department_002(self):
        """重复新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 判断请求结果
        result = json.loads(result.text)
        self.assertEqual(result['already_exist']['count'], 1)
```

运行用例集，我们可以在控制台看到：

因为test_add_department_001断言失败，故test_add_department_002被跳过，无需执行，达成了我们的目的。

![image-20210603195105597](http://pic.testtalking.com/testtalking/20210603195105.png)

## 一如既往，做个总结

**unittest是python的基础库，能满足我们做自动化测试的大部分场景，但，仍旧有很多场景无法满足我们的需求。我们要做的是理解unittest的运行机制，做封装，或者选择其他框架，一切以多快好省的达到测试目的为准则。**