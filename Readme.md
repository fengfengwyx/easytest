��Һã�����̷�塣

���ڣ�����һ��[����Զ������Ե���Ŀ����](http://mp.weixin.qq.com/s?__biz=MzI0ODUyMDA2MQ==&mid=2247486690&idx=1&sn=dcc6b30079cf436a01b88aed3c084427&chksm=e99ec0f0dee949e6daa46dad408657311217973f8af46dc556bad834933431955a1718ed0a32#rd)��

���ڣ���ʼ��ԭ����**�㶮ԭ���㽫�����ɵĳ�͸�Զ�������**��

> tips�����̺�github�����������˳��ͬ�����´��롣
>
> ![image-20210603110511351](http://pic.testtalking.com/testtalking/20210603110633.png)

## ����ʶunittest

����һ��test.py�ļ�������unittest��

```import unittest
import unittest
```

![image-20210508165035063](http://pic.testtalking.com/testtalking/20210508165035.png)

����ctrl+���������룬�ɻ�ȡ��unittest��һЩ��Ϣ��

1. unittest���
2. **unittest�ķ���������test��ͷ**������ذ��£�
3. �ٷ��ĵ����ӣ�֧�����ģ�
4. һ���򵥵�demo���ӣ�����ճ���������У�

<img src="http://pic.testtalking.com/testtalking/20210508165458.png" alt="image-20210508165458661" style="zoom: 67%;" />

## unittestԭ��

һ˵��ԭ�����֣��ܶ��˶پ��Կ�ʹ��

���ģ��Ҳ������Ľ�ԭ��

��һ��ͼ�����ַ�ʽ���㽲���ס�



<img src="http://pic.testtalking.com/testtalking/20210508170212.png" alt="image-20210508170212506"  />



��������ƽʱ�Ĺ���������

���쵽��һ�ݹ��ܲ������񣬿�ʼ��

### д����������case��TestCase��

![image-20210508172155917](http://pic.testtalking.com/testtalking/20210508172155.png)

д�����������ÿ���һЩ��������ɡ�

�ٸ����ӣ�һЩ������Ҫ������������ִ�У�������ò��Ի�����setUp����Ȼ��ִ�в���������run����ִ�����Ϊ�˲�Ӱ����������ִ�У���ûָ����Ի�����tearDown����

so�����õ�unittest�ϣ�TestCase�����ñ�����ˣ��������������

- setUp����ִ�в�������֮ǰ����ʼ������

- run��ִ�в�������

- tearDown����ִ�в�������֮�󣬻�ԭ����

### �����������֮һ��suite��TestSuite��

![image-20210508173524213](http://pic.testtalking.com/testtalking/20210508173524.png)

����д���������Ĺ����У��ǰ���ģ��д�İɡ�

�ٸ����ӣ���ע����˵����д������ע���������쳣ע��������������������Ҫ���ϵ�ע��ģ���У��γ�һ��ע��suite�����ϣ���

![image-20210508173312909](http://pic.testtalking.com/testtalking/20210508173312.png)

���õ�¼��˵����д��������¼�������쳣��¼������������������Ҫ���ϵ���¼ģ���У��γ�һ����¼suite�����ϣ���

��ע��suite�͵�¼suite���ֿ��������һ��������û���Ȩ��sutie���׼�����

so�����õ�unittest�ϣ�TestSuite�����ñ�����ˡ�������������

### �����������֮����loader��TestLoader��

![image-20210508173538890](http://pic.testtalking.com/testtalking/20210508173538.png)

����д����ʱ������дһ��������ȥִ��һ������������д��ÿһ��ģ����������ŵ����������棬�ȵ�ִ�С�

TestLoader�����ñ��Ǽ��� testcase������������ �� testsuite�������������� �У����Ժ���ִ�С�

### ִ�в���������runner��

![image-20210508173818943](http://pic.testtalking.com/testtalking/20210508173818.png)

����һ�������Ŵ������㣬���������Ҿ���˵���˰ɡ�

TextTestRunnerִ�в���������run �������������Խ�������� TextTestResult �С�

### �ܽ����������Ĳ��ߣ�

1. ��д��������TestCase������������test��ͷ��
2. TestLoader��TestCase���ص�TestSuite��
3. TextTestRunner���в��Լ���TestSuite
4. ���еĽ���ᱣ����TextTestResult��

�������룬ԭ������

���ڣ�����һ��д����һ���Զ�������������

## һ������������ܽ�

**01 ������Python��unittest��pytest������Java��JUnit��TestNG���㰴��ƽʱ�����ܲ��Ե�˼άȥ����ܣ�һ��Ҳ�����ӣ�**

**02 ÿһ���ܶ����������ԣ�����������ǵ������������Զ������Թ�����������ѧϰ���������Ǻ��ȥ˼����̽���ġ�**

