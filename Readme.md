��Һã�����̷�塣

���ڽ���֮ǰ��̷����꿽��һ�£�**��һ�ڵ����ݣ���ʵ������**

���û�У������ʵ�٣�����У��ɼ�����

���������������©���ĸ����⡣

## �����һ�����⣺��װ

### ��װ����

ΪʲôҪ��ô����

**�ñ�ǧ��ǧ�棬�Ҳ����㣬�㲻���ҡ�**�ҵ���������ĵ����ϲ����ã�����������ҵĵ����ϲ����á�

��װ���ú󣬿��Ը����������Զ���������Ŀ��

#### ʵ��

��easytest��Ŀ¼�£�����һ��config�ļ��У��ٴ���һ��ProjectConfig.py�ļ������ڱ�����Զ���������Ŀ���������ݣ�����汾�š������URL���ӿ���Ŀ��ַ�ȡ�

> ע�⣺PROJECT_DIR��TEST_DIR�����滻Ϊ�㱾���Ľӿ���Ŀ·�����Զ�����Ŀ·��

![image-20210603225920672](http://pic.testtalking.com/testtalking/20210603225920.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-
class ProjectConfig(object):
    VERSION = "v1.0"
    # �滻Ϊ�㱾�ص�url��ַ
    URL = "http://127.0.0.1:8099/api/departments/"
    # �滻Ϊ�㱾�صĽӿ���Ŀ·����ע�ⲻ���Զ�����Ŀ·����
    PROJECT_DIR = "C:\\Users\\010702\\PycharmProjects\\easytest\\�ӿڻ���\\"
    # �Զ���������ĿĿ¼
    TEST_DIR = "C:\\Users\\010702\\PycharmProjects\\easytest\\"

ETConfig = ProjectConfig()
```

> tips���򱾽ӿ��Զ�����Ŀ����Լ򵥣��ʲ���py�ļ��������á�
>
> ���ҽ�����������˾��Ŀ���Զ�������ʱ�������ñ�����ini��yaml���ļ��У�������.gitignore��Ҳ���Բ����������ķ����Ա��ڲ�ͬ��������������Զ�����Ŀ��

### ��װ����

ΪʲôҪ��ô����

**�ô������࣬�����пɶ��ԣ����Ҹ���ά����**

#### ʵ��

����common�ļ��У����½�һ��py�ļ�HttpReq��

![image-20210604161947533](http://pic.testtalking.com/testtalking/20210604161947.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-

import requests

class HttpReq(object):

    def __init__(self):
        self.headers = {"Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
                        }

    # GET ����
    def get(self, url='', data='', cookies=None):
        response = requests.get(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

    # POST ����
    def post(self, url='', data='', cookies=None):
        response = requests.post(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

    # PUT ����
    def put(self, url='', params='', data='', cookies=None):
        response = requests.put(url=url, params=params, data=data, headers=self.headers, cookies=cookies)
        return response

    # DELETE ����
    def delete(self, url='', data='', cookies=None):
        response = requests.delete(url=url, data=data, headers=self.headers, cookies=cookies)
        return response

ETReq = HttpReq()
```

## ����ڶ������⣺��ȫ���ݿⷽ��

��commonĿ¼�£����½�һ��db_funcs.py�ļ������ڹ������ݿ���صķ�����

![image-20210604162023809](http://pic.testtalking.com/testtalking/20210604162023.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3
from config.ProjectConfig import ETConfig

def execute_db(sql):
    """
    ���ӽӿ���Ŀsqlite���ݿ⣬��ִ��sql���
    :param sql: sql���
    :return:
    """
    # �����ݿ�����
    conn = sqlite3.connect("{0}\\studentManagementSystem\\db.sqlite3".format(ETConfig.PROJECT_DIR))
    # �½��α�
    cursor = conn.cursor()
    # ִ��sql
    cursor.execute(sql)
    # ��ȡִ�н��
    result = cursor.fetchall()
    # �ر��αꡢ�ύ���ӡ��ر�����
    cursor.close()
    conn.commit()
    conn.close()
    return result


def init_db():
    """
    ��ʼ�����ݿ⣬ɾ����departments����������
    :return:
    """
    execute_db("delete from departments;")

if __name__ == '__main__':
    init_db()
```

## �޸�����

���ɣ�������������ݣ����ǽ����ڵ������������޸ġ�

![image-20210603201236866](http://pic.testtalking.com/testtalking/20210603201236.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
import unittest
import json
from config.ProjectConfig import ETConfig
from day05.easytest.common.db_funcs import init_db
from day05.easytest.common.HttpReq import ETReq

class AddDepartment(unittest.TestCase):

    def setUp(self):
        init_db()

    def tearDown(self):
        init_db()

    def test_add_department_001(self):
        """����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # �鿴����Ľ��
        print(result.status_code,result.text)


    def test_add_department_002(self):
        """�ظ�����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # �鿴����Ľ��
        print(result.status_code,result.text)


if __name__ == '__main__':
    # �������
    suite = unittest.TestSuite()
    suite.addTest(AddDepartment("test_add_department_001"))
    suite.addTest(AddDepartment("test_add_department_002"))
    # ���ز����ã������ڿ���̨������־
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)
```

���֮ǰ���ǲ��Ǽ�����ࣿ

## ������������⣺����

��Ϊ�����г��ʵĽӿ��Զ����������⣬��������кܶ��֡�

��Ե�ǰ�Զ���ʵս�����������⣬���ǿɲ��ã�

### ����һ

��test_add_department_002�����������ǰ����ִ��һ��test_add_department_001��׼����ǰ�����ݡ�

![image-20210529214327964](http://pic.testtalking.com/testtalking/image-20210529214327964.png)

���к�test_add_department_002ȷʵ�õ���Ԥ�ڽ����

![image-20210529214412470](http://pic.testtalking.com/testtalking/image-20210529214412470.png)

### ������

����unittest�Ŀ�����ԣ���setUp��tearDown����Ϊ�༶��ģ�setUpClass��tearDownClass��������ִ��AddDepartment��������ࣨ����ģ�飩֮ǰ��֮�󣬷ֱ�������������������ÿһ������������ǰ������⡣

![image-20210529215526865](http://pic.testtalking.com/testtalking/image-20210529215526865.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
import unittest
import json
from config.ProjectConfig import ETConfig
from day05.easytest.common.db_funcs import init_db
from day05.easytest.common.HttpReq import ETReq


class AddDepartment(unittest.TestCase):

    # def setUp(self):
    #     init_db()
    #
    # def tearDown(self):
    #     init_db()

    @classmethod
    def setUpClass(cls):
        print("{0} ִ��ǰ��������ݿ�".format(cls.__name__))
        init_db()

    @classmethod
    def tearDownClass(cls):
        print("{0} ִ�к�������ݿ�".format(cls.__name__))
        init_db()

    def test_add_department_001(self):
        """����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # �鿴����Ľ��
        print(result.status_code, result.text)


    def test_add_department_002(self):
        """�ظ�����T01ѧԺ"""
        # self.test_add_department_001() # ������һ������T01���������ETReq.post
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # �鿴����Ľ��
        print(result.status_code,result.text)


if __name__ == '__main__':
    # �������
    suite = unittest.TestSuite()
    suite.addTest(AddDepartment("test_add_department_001"))
    suite.addTest(AddDepartment("test_add_department_002"))
    # ���ز����ã������ڿ���̨������־
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)
```

����Ч����

![image-20210529215556800](http://pic.testtalking.com/testtalking/image-20210529215556800.png)

STEP 01��ִ������caseǰ��������ݿ�

STEP 02��ִ�е�һ��case�����������ɹ������ظ�results��

STEP 03��ִ�еڶ���case����������ʧ�ܣ����ظ�results��

STEP 04��ִ������case��������ݿ�

> tips��ʵ�ʹ����е��������⣬û���򵥡�

## ������ĸ����⣺����

������excel����������������������ѯ��case��

![image-20210529220115378](http://pic.testtalking.com/testtalking/image-20210529220115378.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
import unittest
from config.ProjectConfig import ETConfig
from day05.easytest.common.HttpReq import ETReq


class QueryDepartment(unittest.TestCase):
    def test_query_department_001(self):
        """��ѯ����ѧԺ"""
        result = ETReq.get(url=ETConfig.URL)
        # �鿴����Ľ��
        print(result.status_code,result.text)


    def test_query_department_002(self):
        """��ѯT01ѧԺ�����ڣ�"""
        result = ETReq.get(url=ETConfig.URL + 'T01')
        # �鿴����Ľ��
        print(result.status_code,result.text)


if __name__ == '__main__':
    # �������
    suite = unittest.TestSuite()
    suite.addTest(QueryDepartment("test_query_department_001"))
    suite.addTest(QueryDepartment("test_query_department_002"))
    # ���ز����ã������ڿ���̨������־
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)
```

���ǵ���һ�ڣ��������������ڣ���©��TestLoader��

![image-20210530202119488](http://pic.testtalking.com/testtalking/image-20210530202119488.png)

���ڣ����Ǳ���õ���������unittest����У�ʹ��TestLoader�򵥵��Ȳ���������ִ�С�

�½�main�ļ��в�����run_case��py�ļ���

![image-20210603201317931](http://pic.testtalking.com/testtalking/20210603201317.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-
import unittest

# �������Լ���
suite = unittest.TestSuite()

# ʶ������Department��β��py�ļ�Ϊ��������
tests = unittest.defaultTestLoader.discover('..\\testcase', pattern='*Department.py')

# ���в�������
suite.addTest(tests)
runner = unittest.TextTestRunner()
test_result = runner.run(suite)
```

����run_case.py��TestLoader����� testcase������������ �� testsuite�������������� �У������в���������

�ڿ���̨�鿴������ﵽ�����ǵ�Ԥ��Ч����

![image-20210530203539272](http://pic.testtalking.com/testtalking/image-20210530203539272.png)

> tips��TestLoader���кܶ������÷�������ʹ�ã������аٶȣ�unittest TestLoader��ʹ�÷�����

## ����

������������

ÿһ������ִ�к�������Ҫ����ȥ�ж�������ִ�н������Υ�����Զ������Եĳ��ԡ�

��ν���أ����������ټ���

## һ������������ܽ�

**01 ʵ�ʹ����еĽӿ����󣬻���Session��Cookies��Token��Ȩ���ȸ���Ŀ���ӣ���˼·�����ࡣ**

**02 ������һ�Σ�ʵ�٣�ʵ�٣�ʵ�١�** 

