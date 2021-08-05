# !/usr/bin/python
# -*- coding:utf-8 -*-+
"""
Author：公众号：测试奇谭
"""
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