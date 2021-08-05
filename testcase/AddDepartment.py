# !/usr/bin/python
# -*- coding:utf-8 -*-+
"""
Author：公众号：测试奇谭
"""

from config.ProjectConfig import ETConfig
from day07.easytest.common.db_funcs import init_db
from day07.easytest.common.HttpReq import ETReq
from day07.easytest.common.wrapers import skip_related_case
import unittest
import json


class AddDepartment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("{0} 执行前，清除数据库".format(cls.__name__))
        init_db()

    def test_add_department_001(self):
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # 判断请求结果
        result = json.loads(result.text)
        self.assertEqual(result['already_exist']['count'], 1) # 断言会失败

    @unittest.skip("强制跳过")
    def test_add_department_001_a(self):
        """@unittest.skip(reason) 强制跳过当前用例"""
        pass

    @unittest.skipIf(3 > 2, "condition为True，跳过")
    def test_add_department_001_b(self):
        """@unittest.skipIf(condition, reason)：condition为True的时候跳转"""
        pass

    @unittest.skipUnless(3 < 2, "condition为False，强制跳过")
    def test_add_department_001_c(self):
        """@unittest.skipUnless(condition, reason)：condition为False的时候跳转"""
        pass

    @unittest.expectedFailure
    def test_add_department_001_d(self):
        """@unittest.expectedFailure：如果test失败了，这个test不计入失败的case数目"""
        self.assertTrue(False)


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