# !/usr/bin/python
# -*- coding:utf-8 -*-+
"""
Author：公众号：测试奇谭
"""
import unittest
from config.ProjectConfig import ETConfig
from day10.easytest.common.HttpReq import ETReq
from day10.easytest.common.wrapers import skip_related_case, write_case_log
from day10.easytest.testcase.data.DepartmentData import QUERY_DATA
from ddt import ddt, data, unpack
import json

@ddt
class QueryDepartment(unittest.TestCase):

    @data(QUERY_DATA['test_query_department_001'])
    @unpack
    @write_case_log()
    def test_query_department_001(self, res_key, res_value):
        """查询所有学院"""
        result = ETReq.get(url=ETConfig.URL)
        result = json.loads(result.text)
        self.assertNotEqual(result[res_key], res_value)


    @data(QUERY_DATA['test_query_department_002'])
    @unpack
    @skip_related_case('test_add_department_001')
    @write_case_log()
    def test_query_department_002(self, res_key, res_value):
        """查询T01学院（存在）"""
        result = ETReq.get(url=ETConfig.URL + 'T01')
        # 查看请求的结果
        result = json.loads(result.text)
        self.assertEqual(result[res_key], res_value)


if __name__ == '__main__':
    # 构造测试
    suite = unittest.TestSuite()
    suite.addTest(QueryDepartment("test_query_department_001"))
    suite.addTest(QueryDepartment("test_query_department_002"))
    # 本地测试用，可以在控制台看到日志
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)