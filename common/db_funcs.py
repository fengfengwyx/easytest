# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
Author：公众号：测试奇谭
"""

import sqlite3
from config.ProjectConfig import ETConfig
from day08.easytest.common.logger import write_log

def execute_db(sql):
    """
    连接接口项目sqlite数据库，并执行sql语句
    :param sql: sql语句
    :return:
    """
    try:
        # 打开数据库连接
        conn = sqlite3.connect("{0}\\studentManagementSystem\\db.sqlite3".format(ETConfig.PROJECT_DIR))
        # 新建游标
        cursor = conn.cursor()
        # 执行sql
        cursor.execute(sql)
        # 获取执行结果
        result = cursor.fetchall()
        # 关闭游标、提交连接、关闭连接
        cursor.close()
        conn.commit()
        conn.close()
        return result
    except sqlite3.OperationalError as e:
        write_log.error("数据库连接，执行失败：{}".format(e))


def init_db():
    """
    初始化数据库，删除掉departments的所有数据
    :return:
    """
    execute_db("delete from departments;")

if __name__ == '__main__':
    init_db()