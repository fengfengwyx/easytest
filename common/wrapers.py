# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
Author：公众号：测试奇谭
"""
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