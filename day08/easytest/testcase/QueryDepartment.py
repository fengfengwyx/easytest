# !/usr/bin/python
# -*- coding:utf-8 -*-+
"""
Author：公众号：测试奇谭
"""
import unittest
from config.ProjectConfig import ETConfig
from day08.easytest.common.HttpReq import ETReq


class QueryDepartment(unittest.TestCase):

    def test_query_department_001(self):
        """查询所有学院"""
        result = ETReq.get(url=ETConfig.URL)
        # 查看请求的结果
        print(result.status_code,result.text)


    def test_query_department_002(self):
        """查询T01学院（存在）"""
        result = ETReq.get(url=ETConfig.URL + 'T01')
        # 查看请求的结果
        print(result.status_code,result.text)


if __name__ == '__main__':
    # 构造测试
    suite = unittest.TestSuite()
    suite.addTest(QueryDepartment("test_query_department_001"))
    suite.addTest(QueryDepartment("test_query_department_002"))
    # 本地测试用，可以在控制台看到日志
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)