# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
Author：公众号：测试奇谭
"""
import requests
from day10.easytest.common.logger import write_log

class HttpReq(object):

    def __init__(self):
        self.headers = {"Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
                        }

    # GET 请求
    def get(self, url='', data='', cookies=None):
        try:
            response = requests.get(url=url, data=data, headers=self.headers, cookies=cookies)
            return response
        except Exception as e:
            write_log.error("GET请求失败：{}".format(e))

    # POST 请求
    def post(self, url='', data='', cookies=None):
        try:
            response = requests.post(url=url, data=data, headers=self.headers, cookies=cookies)
            return response
        except Exception as e:
            write_log.error("POST请求失败：{}".format(e))

    # PUT 请求
    def put(self, url='', params='', data='', cookies=None):
        try:
            response = requests.put(url=url, params=params, data=data, headers=self.headers, cookies=cookies)
            return response
        except Exception as e:
            write_log.error("PUT请求失败：{}".format(e))

    # DELETE 请求
    def delete(self, url='', data='', cookies=None):
        try:
            response = requests.delete(url=url, data=data, headers=self.headers, cookies=cookies)
            return response
        except Exception as e:
            write_log.error("DELETE请求失败：{}".format(e))

# ET = easytest
ETReq = HttpReq()