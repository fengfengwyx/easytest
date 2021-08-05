# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
Author：公众号：测试奇谭
"""

# res_key未实现JSON分级分类解析，你可以自己尝试实现
ADD_DATA = {
    "test_add_department_001": {
        "req_data": {"data": [{"dep_id": "T01", "dep_name": "Test学院", "master_name": "Test-Master", "slogan": "Here is Slogan"}]},
        "res_key": "already_exist",
        "res_value": 0},

    "test_add_department_002": {
        "req_data": {"data": [{"dep_id": "T01", "dep_name": "Test学院", "master_name": "Test-Master", "slogan": "Here is Slogan"}]},
        "res_key": "already_exist",
        "res_value": 1},

    "test_add_department_003": {
        "req_data": {"data": [{"dep_id": "", "dep_name": "dep_id为空学院", "master_name": "dep_id为空Master", "slogan": "Here is dep_id为空"}]},
        "res_key": "dep_id",
        "res_value": "该字段不能为空。"},

    "test_add_department_004": {
        "req_data": {"data": [{"dep_id": "T02", "dep_name": "", "master_name": "dep_name为空Master", "slogan": "Here is dep_name为空"}]},
        "res_key": "dep_name",
        "res_value": "该字段不能为空。"},

    "test_add_department_005": {
        "req_data": {"data": [{"dep_id": "T02", "dep_name": "T02学院", "master_name": "", "slogan": "Here is master_name为空"}]},
        "res_key": "master_name",
        "res_value": "该字段不能为空。"},

    "test_add_department_006": {
        "req_data": {"data": [{"dep_id": "T02", "dep_name": "T02学院", "master_name": "T02Master", "slogan": ""}]},
        "res_key": "already_exist",
        "res_value": 0},
}


QUERY_DATA = {
    "test_query_department_001": {
        "res_key": "results",
        "res_value": []},
    "test_query_department_002": {
        "res_key": "dep_id",
        "res_value": "T01"}
}