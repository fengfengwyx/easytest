��Һã�����̷�塣

�Զ���������Ŀʵս���ѽӽ�β����������һ����꿽�ʣ�**��ǰ������������Σ�������������**

��������Ѻ����⣬�������������ġ�

���ڣ���������������

## ʲô������������

���ȣ�����������һ������ϸ��������Ӧ���ġ���ʲô���Զ������Ե�����������

ͬ�����Ǵӹ��ܲ�����⡣

��д���ܲ�������ʱ�����Ƿ�Ὣ������������������ֿ���

�ٸ����ӣ���¼����һ���Ϊ�����û������������롢�����¼��ť�����������û�����������������ȴ�кܶ��֡�

�����У�ǰ���ǲ��������������ǲ������ݡ������������ܲ��Ի��������Իع飬ֻ��Ҫ�޸Ĳ������ݣ��û�������������ݣ����������޸Ĳ�������������¼�����̣���

�ۼ���������������Լ򵥵����Ϊ��**��ͬ�Ĳ���������ÿ��ʹ�ò�ͬ�Ĳ�������**��

��������������������ֿ������Խ��Ͳ���������ά���ɱ����ر����ڽӿڲ����У�����Խ�������Ϣ�������롢�����Ԥ�ڽ���������ʵ�����ʽ��¼Ϊ���ݼ���ִ�в���ʱ��ֻ��Ҫ�޸����ݼ����������޸Ĳ���������

�Ա��Զ���ʵս��ĿΪ�����򿪽ӿ��Զ�������������

![image-20210607170402940](http://pic.testtalking.com/testtalking/20210607170403.png)

test_add_department_003��test_add_department_004��test_add_department_005�����������ֶο�ֵУ�顣

���ೡ�����ʺ�ʹ������������

## ���ʵ������������

unittest��֧������������һ����Ҫ����������ddt��ʵ�֡�

### һ����װddt

```
pip3 install ddt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

### �����������ݼ�

��testcaseĿ¼�£��½�һ��dataĿ¼���ٴ���DepartmentData.py�ļ������ڴ�Ų������ݡ�

![image-20210607170200993](http://pic.testtalking.com/testtalking/20210607170201.png)

Ϊͳһά�������ǽ�����ѧԺ�����е�����ȫ������������γ�ADD_DATA���ݼ���

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-

# res_keyδʵ��JSON�ּ����������������Լ�����ʵ��
ADD_DATA = {
    "test_add_department_001": {
        "req_data": {"data": [{"dep_id": "T01", "dep_name": "TestѧԺ", "master_name": "Test-Master", "slogan": "Here is Slogan"}]},
        "res_key": "already_exist",
        "res_value": 0},

    "test_add_department_002": {
        "req_data": {"data": [{"dep_id": "T01", "dep_name": "TestѧԺ", "master_name": "Test-Master", "slogan": "Here is Slogan"}]},
        "res_key": "already_exist",
        "res_value": 1},

    "test_add_department_003": {
        "req_data": {"data": [{"dep_id": "", "dep_name": "dep_idΪ��ѧԺ", "master_name": "dep_idΪ��Master", "slogan": "Here is dep_idΪ��"}]},
        "res_key": "dep_id",
        "res_value": "���ֶβ���Ϊ�ա�"},

    "test_add_department_004": {
        "req_data": {"data": [{"dep_id": "T02", "dep_name": "", "master_name": "dep_nameΪ��Master", "slogan": "Here is dep_nameΪ��"}]},
        "res_key": "dep_name",
        "res_value": "���ֶβ���Ϊ�ա�"},

    "test_add_department_005": {
        "req_data": {"data": [{"dep_id": "T02", "dep_name": "T02ѧԺ", "master_name": "", "slogan": "Here is master_nameΪ��"}]},
        "res_key": "master_name",
        "res_value": "���ֶβ���Ϊ�ա�"},

    "test_add_department_006": {
        "req_data": {"data": [{"dep_id": "T02", "dep_name": "T02ѧԺ", "master_name": "T02Master", "slogan": ""}]},
        "res_key": "already_exist",
        "res_value": 0},
}
```

### �����޸�����

�޸�test_add_department_001������

1. װ��ddt��data��unpack
2. �������
3. �޸���������
4. �޸���Ӧ�ж�

> tips��ddt���Լ����б��ֵ䡢Ԫ���python���ݸ�ʽ��Ҳ����ͨ��file_data����json/txt/yaml�������ļ���
>
> ��ƪ���ü����ֵ�ķ�ʽʵ�֡�

```python
from testcase.data.DepartmentData import ADD_DATA
from ddt import ddt, data, unpack

...
    @data(ADD_DATA['test_add_department_001'])
    @unpack
    @write_case_log()
    def test_add_department_001(self, req_data, res_key, res_value):
        """����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)
...
```

![image-20210607171120405](http://pic.testtalking.com/testtalking/20210607171120.png)

���ϣ���һ���򵥵Ĳ�������ģ�͡�

### �ġ���������

���Զ�������������������dep_id/dep_name/master_name������������test_add_department_001������

![image-20210607170402940](http://pic.testtalking.com/testtalking/20210607171538.png)

```python
...
	@data(ADD_DATA['test_add_department_003'], ADD_DATA['test_add_department_004'], ADD_DATA['test_add_department_005'])
    @unpack
    @write_case_log()
    def test_add_department_003(self, req_data, res_key, res_value):
        """Ϊ��У��-dep_id/dep_name/master_nameΪ��У��"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        # �ж�������
        result = json.loads(result.text)
        self.assertEqual(result[res_key][0], res_value)
...
```

![image-20210607171813004](http://pic.testtalking.com/testtalking/20210607171813.png)

�����������£�

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-+
from config.ProjectConfig import ETConfig
from common.db_funcs import init_db
from common.HttpReq import ETReq
from common.wrapers import skip_related_case,write_case_log
from testcase.data.DepartmentData import ADD_DATA
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
        """����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)  # res_keyδʵ��JSON�ּ����������������Լ�����ʵ��


    @data(ADD_DATA['test_add_department_002'])
    @unpack
    @write_case_log()
    @skip_related_case('test_add_department_001')
    def test_add_department_002(self, req_data, res_key, res_value):
        """�ظ�����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        # �ж�������
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)


    @data(ADD_DATA['test_add_department_003'], ADD_DATA['test_add_department_004'], ADD_DATA['test_add_department_005'])
    @unpack
    @write_case_log()
    def test_add_department_003(self, req_data, res_key, res_value):
        """Ϊ��У��-dep_id/dep_name/master_nameΪ��У��"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        # �ж�������
        result = json.loads(result.text)
        self.assertEqual(result[res_key][0], res_value)


    @data(ADD_DATA['test_add_department_006'])
    @unpack
    @write_case_log()
    def test_add_department_006(self, req_data, res_key, res_value):
        """Ϊ��У��-sloganΪ��У��"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)


if __name__ == '__main__':
    # �������
    suite = unittest.TestSuite()
    suite.addTest(AddDepartment("test_add_department_001"))
    suite.addTest(AddDepartment("test_add_department_002"))
    suite.addTest(AddDepartment("test_add_department_003"))
    suite.addTest(AddDepartment("test_add_department_006"))
    # ���ز����ã������ڿ���̨������־
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)
```

�������AddDepartment�����࣬�ڿ���̨���Կ���һ��ִ����6��������

![image-20210607173644062](http://pic.testtalking.com/testtalking/20210607173644.png)

��ȥ�����־��test_add_department_003ִ�������Σ��ﵽ������������Ŀ�ġ��������������Ͳ������ݷ��뿪��ִ�в���ʱ��ֻ��Ҫ�޸����ݼ����������޸Ĳ���������

![image-20210607173746547](http://pic.testtalking.com/testtalking/20210607173746.png)

## һ������������ܽ�

**01 ��ƪֻ�Ǵ������ţ������������������ɲ��ǳ�Ϧ֮��Ĺ���**

**02 ����������������Խ����Ĺ�ע�����ݲ��棬���磬��ο����������ݡ���θ��Ǹ���У�鳡������μ����������ݡ����ģ��������ʵ���ݵ������ϡ�**

