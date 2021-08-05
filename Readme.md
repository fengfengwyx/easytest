��Һã�����̷�塣

����������ѧϰ�����Ƿ��Ѹе�ƣ����

����ǣ�̷�彨������Ϣһ�죬���Ķ�һ��01-06��ʵ�ٶ�����ϰ�¡�

���ڣ�̷�彲���������򵥣���ʵҲ����ô�򵥵����ݡ�����������ִ�С�

��ʵ�ʵĽӿڲ����У����ĳ����������ִ����������������ִ�������ٸ����ӣ�A������B����ʱ������������B����������A����ִ�гɹ�������A����ִ��ʧ�ܺ�B����ִ��Ҳ��ʧ�ܣ�������Ϊ����ʧ�ܣ�������ΪA���µģ���

���ǣ������յ�����ִ��ͳ���У�B��ͳ�Ƴ�ʧ��������Ȼ��ȴ������������

��������������unittest�У������ʹ��skip����ִ�С�

## ��������

unittestĬ�ϵ�������������ʽ����װ����ʵ�֣���

skip��ʹ�úܼ򵥣���ͼ��ʾ��������Ҳ��������Ŀ�У������ִ����һ�ԣ����skipװ�������÷���

![image-20210603201414069](http://pic.testtalking.com/testtalking/20210603201414.png)

�ص�֮ǰ��ʵ���У������ǲ������������ֳ�����

���test_add_department_001����������T01ѧԺ��ִ��ʧ�ܣ�test_add_department_002���ظ�����T01ѧԺ��û��Ҫ��ִ�С�

��ʱ��������Ҫ����test_add_department_002��

���ǣ�unittest��������skip��ʽ�޷��������ǵ�������Ϊskip�޷���������Ϊ��Ρ�

����ô�죿

## ��װ����

��common�ļ����£��½�һ��wrapers.py�ļ���������װ����������

![image-20210603201430204](http://pic.testtalking.com/testtalking/20210603201430.png)

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from functools import wraps

def skip_related_case(related_case_name=''):
    """
    AB��������
    ���A��������ִ�С�ִ�б�������ʧ�ܣ���B������ִ��
    :param related_case_name: ��������A������
    :return:
    """
    def wraper_func(func):
        @wraps(func)
        def inner_func(*args, **kwargs):
            fail_cases = str([fail[0] for fail in args[0]._outcome.result.failures])
            error_cases = str([error[0] for error in args[0]._outcome.result.errors])
            skip_cases = str([error[0] for error in args[0]._outcome.result.skipped])
            if (related_case_name in fail_cases):
                reson = "{}����ʧ�ܣ�����ִ��{}����".format(related_case_name, func.__name__)
                test = unittest.skipIf(True, reson)(func(*args, **kwargs))
            elif (related_case_name in error_cases):
                reson = "{}ִ�б�������ִ��{}����".format(related_case_name, func.__name__)
                test = unittest.skipIf(True, reson)(func(*args, **kwargs))
            elif (related_case_name in skip_cases):
                reson = "{}����δִ�У�����ִ��{}����".format(related_case_name, func.__name__)
                test = unittest.skipIf(True, reson)(func(*args, **kwargs))
            else:
                test = func
            return test(*args, **kwargs)
        return inner_func
    return wraper_func
```

�ص������࣬���Ը�test_add_department_002װ�������Ǹոմ�����skip_related_case������

```python
    @skip_related_case('test_add_department_001')
    def test_add_department_002(self):
        """�ظ�����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # �ж�������
        result = json.loads(result.text)
        self.assertEqual(result['already_exist']['count'], 1)
```

���������������ǿ����ڿ���̨������

��Ϊtest_add_department_001����ʧ�ܣ���test_add_department_002������������ִ�У���������ǵ�Ŀ�ġ�

![image-20210603195105597](http://pic.testtalking.com/testtalking/20210603195105.png)

## һ������������ܽ�

**unittest��python�Ļ����⣬�������������Զ������ԵĴ󲿷ֳ����������Ծ��кܶೡ���޷��������ǵ���������Ҫ���������unittest�����л��ƣ�����װ������ѡ��������ܣ�һ���Զ���ʡ�Ĵﵽ����Ŀ��Ϊ׼��**