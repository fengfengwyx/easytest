# !/usr/bin/python
# -*- coding:utf-8 -*-+
"""
Author：公众号：测试奇谭
"""
from config.ProjectConfig import ETConfig
from day08.easytest.common.db_funcs import init_db
from day08.easytest.common.HttpReq import ETReq
from day08.easytest.common.wrapers import skip_related_case,write_case_log
import unittest
import json


class AddDepartment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()


    @write_case_log()
    def test_add_department_001(self):
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        result = json.loads(result.text)
        self.assertEqual(result['already_exist']['count'], 0)

    @write_case_log()
    @skip_related_case('test_add_department_001')
    def test_add_department_002(self):
        """重复新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 判断请求结果
        result = json.loads(result.text)
        self.assertEqual(result['already_exist']['count'], 1)


if __name__ == '__main__':
    # 构造测试
    suite = unittest.TestSuite()
    suite.addTest(AddDepartment("test_add_department_001"))
    suite.addTest(AddDepartment("test_add_department_002"))
    # 本地测试用，可以在控制台看到日志
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)