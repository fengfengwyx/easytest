# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
Author：公众号：测试奇谭
"""

import requests

class HttpReq(object):

    def __init__(self):
        self.headers = {"Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
                        }

    # GET 请求
    def get(self, url='', data='', cookies=None):
        response = requests.get(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

    # POST 请求
    def post(self, url='', data='', cookies=None):
        response = requests.post(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

    # PUT 请求
    def put(self, url='', params='', data='', cookies=None):
        response = requests.put(url=url, params=params, data=data, headers=self.headers, cookies=cookies)
        return response

    # DELETE 请求
    def delete(self, url='', data='', cookies=None):
        response = requests.delete(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

# ET = easytest
ETReq = HttpReq()