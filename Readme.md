��Һã�����̷�塣

���ڵ�unittestԭ�������������û�У�û��ϵ�����ڣ�������ҵĽŲ���ͨ��д����ĵ�һ���Զ�������������������Ϥ��Ϥ��

## ��һ������

�鿴���ӿڻ���������Ŀ�ĵ������Զ�����������.xlsx����д���Ϊtest_add_department_001��test_add_department_002��������

![image-20210530202340614](http://pic.testtalking.com/testtalking/image-20210530202340614.png)

![image-20210528160434346](http://pic.testtalking.com/testtalking/20210528160434.png)

�½�һ��testcase�ļ��У�����һ��AddDepartment.py�ļ���

![image-20210603200147351](http://pic.testtalking.com/testtalking/20210603200147.png)

д������ģ��������Զ�������������

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
import unittest
import json
import requests


class AddDepartment(unittest.TestCase):

    def setUp(self):
        print("{0} ִ��ǰ��������ݿ�".format(self._testMethodName))

    def tearDown(self):
        print("{0} ִ�к�������ݿ�".format(self._testMethodName))

    def test_add_department_001(self):
        """����T01ѧԺ"""
        result = requests.post(url='http://127.0.0.1:8099/api/departments/',
                               headers={"Content-Type": "application/json",
                                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"},
                               data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]})
                            )
        # �鿴����Ľ��
        print(result.status_code,result.text)


    def test_add_department_002(self):
        """�ظ�����T01ѧԺ"""
        result = requests.post(url='http://127.0.0.1:8099/api/departments/',
                               headers={"Content-Type": "application/json",
                                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"},
                               data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]})
                            )
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

## �������

������һ�ڵ�֪ʶ�㣬һһ��Ȿ��������

### ����������case��TestCase��

��������������TestCase�У��У�

- setUp����ִ�в�������֮ǰ����ʼ�����ݿ⣨��������ʵ�֣�

  ![image-20210529205053853](http://pic.testtalking.com/testtalking/20210529205053.png)

- test_add_department_001���Զ�����������

  ![image-20210529205136221](http://pic.testtalking.com/testtalking/20210529205136.png)

- tearDown����ִ�в�������֮�󣬻ָ����ݿ⣨��������ʵ�֣�

  ![image-20210529205117076](http://pic.testtalking.com/testtalking/20210529205117.png)

### �����������֮һ��suite��TestSuite��

��д������ѧԺ���ظ�����ѧԺ��������������������Ҫ���ϵ�����ģ���У��γ�һ������suite�����ϣ���

���õ�unittest�ϣ�ʹ��TestSuite����������

![image-20210525232236209](http://pic.testtalking.com/testtalking/20210525232236.png)

### �����������֮����loader��TestLoader��

�˵���δ�漰�����ڻ�˵��

### ִ�в���������runner��

![image-20210525232259750](http://pic.testtalking.com/testtalking/20210525232259.png)

TextTestRunnerͨ��run ����ִ�в���������

������ǿ�������̨�������

![image-20210529211957834](http://pic.testtalking.com/testtalking/image-20210529211957834.png)

STEP 01����һ������ǰ��������ݿ�

STEP 02����һ�����������������ɹ������ظ�results��

STEP 03����һ��������������ݿ�

STEP 04���ڶ�������ǰ��������ݿ�

STEP 05���ڶ�����������������ʧ�ܣ����ظ�results��

STEP 06���ڶ���������������ݿ�

## ����

���ǣ���д������ִ�������Ĺ����У����Ƿ�������Щ���⣿

### 01 ����δ��װ

URL��Headers�������壬ȫ�������㡣����������ʱ��������Ķ��Եͣ��Һ���ά����

![image-20210525232509162](http://pic.testtalking.com/testtalking/20210525232509.png)

### 02 ��Ҫ��ȫ������ݿ�ķ���

![image-20210529212030296](http://pic.testtalking.com/testtalking/image-20210529212030296.png)

### 03 �ڶ�������������һ������

������һ����������ִ�гɹ���

���⣬�ڶ������������ܳ�ʼ�����ݿ⣨����ζ�����ݶ�ʧ����

![image-20210529211957834](http://pic.testtalking.com/testtalking/image-20210529211957834.png)

### 04 ������ȱ��ͳһ����͵���

���ڵ������������ļ�ִ�У����鷳������ѯ���޸ġ�ɾ��ģ�鶼���Ӻ���Ҫ��һ���ط�ͳһ������Щģ������С�

![image-20210525232520431](http://pic.testtalking.com/testtalking/20210525232520.png)

�����ĸ����⣬���ڣ���һ������

## һ������������ܽ�

**01 ���ⲻֹ�ڴˣ��������⣬�һ���ں�����������֮ǰ����������룬������Щ���⡣**

**02 һ��Ҫ����ʵ�١�**

