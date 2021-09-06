# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
Author：公众号：测试奇谭
"""

class ProjectConfig(object):
    VERSION = "v1.0"
    # 替换为你本地的url地址
    URL = "http://127.0.0.1:8099/api/departments/"
    # 替换为你本地的接口项目路径（注意不是自动化项目路径）
    PROJECT_DIR = "C:\\Users\\010702\\PycharmProjects\\easytest\\接口环境\\"
    # 自动化测试项目目录
    TEST_DIR = "C:\\Users\\010702\\PycharmProjects\\easytest\\"

    # 邮件配置信息
    EMAIL_CONFIG = {"EMAIL_SERVER":"smtp.qq.com", # 服务器
                    "EMAIL_USER":"aaaa@qq.com", # 账号
                    "EMAIL_PWD":"xxxxxx", # 密码（授权码）
                    "EMAIL_SENDER":"aaaa@qq.com", # 发件人（同账号）
                    "EMAIL_RECEIVER":"bbbb@qq.com", # 收件人（多个用,隔开）
                    "EMAIL_CC":"cccc@qq.com"} # 抄送人（多个用,隔开）

ETConfig = ProjectConfig()