大家好，我是谭叔。

自动化测试项目实战，已接近尾声，我再来一次灵魂拷问：**先前的内容练得如何？有遇到困难吗？**

如果有困难和问题，可在留言区聊聊。

本期，聊聊数据驱动。

## 什么是数据驱动？

首先，数据驱动是一个大概念。细分下来，应该聊——什么是自动化测试的数据驱动。

同理，我们从功能测试理解。

在写功能测试用例时，你是否会将测试数据与测试用例分开？

举个例子，登录操作一般分为输入用户名、输入密码、点击登录按钮三步，但是用户名和密码的数据组合却有很多种。

该例中，前者是测试用例，后者是测试数据——不管做功能测试还是做测试回归，只需要修改测试数据（用户名和密码的数据），而无需修改测试用例本身（登录的流程）。

论及数据驱动，你可以简单的理解为：**相同的测试用例，每次使用不同的测试数据**。

将测试数据与测试用例分开，可以降低测试用例的维护成本，特别是在接口测试中，你可以将所有信息，如输入、输出、预期结果，都以适当的形式记录为数据集，执行测试时，只需要修改数据集，而无需修改测试用例。

以本自动化实战项目为例，打开接口自动化测试用例：

![image-20210607170402940](http://pic.testtalking.com/testtalking/20210607170403.png)

test_add_department_003、test_add_department_004、test_add_department_005用例，均是字段空值校验。

这类场景，适合使用数据驱动。

## 如何实现数据驱动？

unittest不支持数据驱动，一般需要借助第三方ddt库实现。

### 一、安装ddt

```
pip3 install ddt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

### 二、创建数据集

在testcase目录下，新建一个data目录，再创建DepartmentData.py文件，用于存放测试数据。

![image-20210607170200993](http://pic.testtalking.com/testtalking/20210607170201.png)

为统一维护，我们将新增学院用例中的数据全部抽离出来，形成ADD_DATA数据集。

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-

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
```

### 三、修改用例

修改test_add_department_001用例：

1. 装饰ddt的data和unpack
2. 增加入参
3. 修改请求数据
4. 修改响应判断

> tips：ddt可以加载列表，字典、元组等python数据格式，也可以通过file_data加载json/txt/yaml等数据文件。
>
> 本篇采用加载字典的方式实现。

```python
from testcase.data.DepartmentData import ADD_DATA
from ddt import ddt, data, unpack

...
    @data(ADD_DATA['test_add_department_001'])
    @unpack
    @write_case_log()
    def test_add_department_001(self, req_data, res_key, res_value):
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)
...
```

![image-20210607171120405](http://pic.testtalking.com/testtalking/20210607171120.png)

如上，是一个简单的测试驱动模型。

### 四、新增用例

打开自动化测试用例，尝试用dep_id/dep_name/master_name三条数据驱动test_add_department_001用例。

![image-20210607170402940](http://pic.testtalking.com/testtalking/20210607171538.png)

```python
...
	@data(ADD_DATA['test_add_department_003'], ADD_DATA['test_add_department_004'], ADD_DATA['test_add_department_005'])
    @unpack
    @write_case_log()
    def test_add_department_003(self, req_data, res_key, res_value):
        """为空校验-dep_id/dep_name/master_name为空校验"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        # 判断请求结果
        result = json.loads(result.text)
        self.assertEqual(result[res_key][0], res_value)
...
```

![image-20210607171813004](http://pic.testtalking.com/testtalking/20210607171813.png)

完整代码如下：

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
        """新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)  # res_key未实现JSON分级分类解析，你可以自己尝试实现


    @data(ADD_DATA['test_add_department_002'])
    @unpack
    @write_case_log()
    @skip_related_case('test_add_department_001')
    def test_add_department_002(self, req_data, res_key, res_value):
        """重复新增T01学院"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        # 判断请求结果
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)


    @data(ADD_DATA['test_add_department_003'], ADD_DATA['test_add_department_004'], ADD_DATA['test_add_department_005'])
    @unpack
    @write_case_log()
    def test_add_department_003(self, req_data, res_key, res_value):
        """为空校验-dep_id/dep_name/master_name为空校验"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        # 判断请求结果
        result = json.loads(result.text)
        self.assertEqual(result[res_key][0], res_value)


    @data(ADD_DATA['test_add_department_006'])
    @unpack
    @write_case_log()
    def test_add_department_006(self, req_data, res_key, res_value):
        """为空校验-slogan为空校验"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps(req_data))
        result = json.loads(result.text)
        self.assertEqual(result[res_key]['count'], res_value)


if __name__ == '__main__':
    # 构造测试
    suite = unittest.TestSuite()
    suite.addTest(AddDepartment("test_add_department_001"))
    suite.addTest(AddDepartment("test_add_department_002"))
    suite.addTest(AddDepartment("test_add_department_003"))
    suite.addTest(AddDepartment("test_add_department_006"))
    # 本地测试用，可以在控制台看到日志
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)
```

最后，运行AddDepartment用例类，在控制台可以看到一共执行了6条用例。

![image-20210607173644062](http://pic.testtalking.com/testtalking/20210607173644.png)

再去查查日志，test_add_department_003执行了三次，达到了数据驱动的目的——将测试用例和测试数据分离开，执行测试时，只需要修改数据集，而无需修改测试用例。

![image-20210607173746547](http://pic.testtalking.com/testtalking/20210607173746.png)

## 一如既往，做个总结

**01 本篇只是带你入门，想做好数据驱动，可不是朝夕之间的功夫。**

**02 做数据驱动后，你可以将重心关注在数据层面，比如，如何快速生成数据、如何覆盖更多校验场景、如何减少冗杂数据、如何模拟线上真实数据等问题上。**

