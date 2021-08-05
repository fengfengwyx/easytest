# !/usr/bin/python
# -*- coding:utf-8 -*-+
"""
Author：公众号：测试奇谭
"""
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