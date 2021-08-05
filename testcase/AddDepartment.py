# !/usr/bin/python
# -*- coding:utf-8 -*-+
"""
Author：公众号：测试奇谭
"""
from config.ProjectConfig import ETConfig
from day10.easytest.common.db_funcs import init_db
from day10.easytest.common.HttpReq import ETReq
from day10.easytest.common.wrapers import skip_related_case,write_case_log
from day10.easytest.testcase.data.DepartmentData import ADD_DATA
from ddt import ddt, data, unpack
import unittest
import json


@ddt
class AddDepartment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()


    @data(ADD_DATA['test_add_department_001'])
    @unpack
    @write_case_log()
    def test_add_department_001(self, req_data, res_key, res_value):
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)  # res_key未实现JSON分级分类解析，你可以自己尝试实现


    @data(ADD_DATA['test_add_department_002'])
    @unpack
    @write_case_log()
    @skip_related_case('test_add_department_001')
    def test_add_department_002(self, req_data, res_key, res_value):
        """重复新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        # 判断请求结果
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)


    @data(ADD_DATA['test_add_department_003'], ADD_DATA['test_add_department_004'], ADD_DATA['test_add_department_005'])
    @unpack
    @write_case_log()
    def test_add_department_003(self, req_data, res_key, res_value):
        """为空校验-dep_id/dep_name/master_name为空校验"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        # 判断请求结果
        result = json.loads(result.text)
        self.assertEqual(result[res_key][0], res_value)


    @data(ADD_DATA['test_add_department_006'])
    @unpack
    @write_case_log()
    def test_add_department_006(self, req_data, res_key, res_value):
        """为空校验-slogan为空校验"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)


if __name__ == '__main__':
    # 构造测试
    suite = unittest.TestSuite()
    suite.addTest(AddDepartment("test_add_department_001"))
    suite.addTest(AddDepartment("test_add_department_002"))
    suite.addTest(AddDepartment("test_add_department_003"))
    suite.addTest(AddDepartment("test_add_department_006"))
    # 本地测试用，可以在控制台看到日志
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)