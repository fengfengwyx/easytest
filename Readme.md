��Һã�����̷�塣

�����ص����������������⡪������õ����ж�������ִ�н����

��������˼·���������ܲ�����һ������������Ե�¼�ӿ�ʱ����ù۲��¼�ӿڷ��سɹ�����ʧ�ܣ����жϵ�¼�Ƿ�ɹ���

��ô�����Զ�������ʱ�������**�����ж�ִ�н���ǲ�������Ҫ��**��

## ���ж�

�޸�test_add_department_001��test_add_department_002����������if else���жϡ�

```python
    def test_add_department_001(self):
        """����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # �ж�������
        result = json.loads(result.text)
        if result['already_exist']['count'] == 0:
            print("{} ִ�гɹ�".format(self._testMethodName))
        else:
            print("{} ִ��ʧ��".format(self._testMethodName))


    def test_add_department_002(self):
        """�ظ�����T01ѧԺ"""
        # self.test_add_department_001() # ������һ������T01���������ETReq.post
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # �ж�������
        result = json.loads(result.text)
        if result['already_exist']['count'] == 1:
            print("{} ִ�гɹ�".format(self._testMethodName))
        else:
            print("{} ִ��ʧ��".format(self._testMethodName))
```

��������ɣ�

![image-20210530205113006](http://pic.testtalking.com/testtalking/image-20210530205113006.png)

���������Ǳ㹹����һ���򵥵�if else���Է�ʽ���ó������ж��߼���

�����������ʶ����ôд�����в��ס����������࣬����ά����

һ����˵�����ǻ�ʹ��unittest��assert������������⡣

## ʹ�ö���

unittest�ж�����Ҫ���������ͣ�

1���������ԡ�����Ҫô��ȷ��Ҫô����

2���Ƚ϶��ԡ�ͨ���Ƚ�����������ֵ�ó�����ֵ��Ҫô�Ƚ���ȷ��Ҫô�Ƚϴ���

3���������ԡ�������б�Ԫ��ȣ�ʹ���������

��ͼ��ʾ������assert���༭�����Զ��������еĶ��ԡ�

![image-20210603172038206](http://pic.testtalking.com/testtalking/20210603172038.png)

��Ա��νӿ��Զ�����Ŀ������ʹ�ü򵥵�assertEqual���Ƚ϶��ԣ����������Է�ʽ������Գ�ʱ���о��£���ȷ��⣬�����Լ�����Ŀ�����ʵ�ѡ��

���ȣ�ȥ��if else���жϲ��֡�

![image-20210603171708115](http://pic.testtalking.com/testtalking/20210603171708.png)

�����assertEqual��

```python
    def test_add_department_001(self):
        """����T01ѧԺ"""
        result = ETReq.post(url=ETConfig.URL,
                            data=json.dumps({"data":[{"dep_id":"T01","dep_name":"TestѧԺ","master_name":"Test-Master","slogan":"Here is Slogan"}]}))
        # �ж�������
        result = json.loads(result.text)
        # self.assertEqual(result['already_exist']['count'], 0) # ���Ի�ʧ��
        self.assertEqual(result['already_exist']['count'], 1) # ���Ի�ʧ��
```

![image-20210603172921091](http://pic.testtalking.com/testtalking/20210603172921.png)

�ڿ���̨�����ǿ��Կ������յĽ����������ʧ�ܡ�

![image-20210603173031667](http://pic.testtalking.com/testtalking/20210603173031.png)

## һ������������ܽ�

**�ӿڶ��ԣ������Ϻܼ򵥣���������ʵ�����£���ý������ӵ����ݽṹ���ø���ҵ�񳡾�ϸ�ֶ������࣬��ӿڶ��ԡ����ݿ���Եȵȣ���Щ�����Ѷȣ������ֺ��������ܺܿ����ա�**