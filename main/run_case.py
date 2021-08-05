# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
Author：公众号：测试奇谭
"""

import unittest

# 创建测试集合
suite = unittest.TestSuite()

# 识别所有Department结尾的py文件为测试用例
tests = unittest.defaultTestLoader.discover('..\\testcase', pattern='*Department.py')

# 运行测试用例
suite.addTest(tests)
runner = unittest.TextTestRunner()
test_result = runner.run(suite)