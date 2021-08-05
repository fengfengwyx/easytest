��Һã�����̷�塣

���������һ�������ݡ������Խ����ͳ��չʾ��

ͳ��չʾ�ķ����ܶ࣬��ӿڼ�������ҳչʾ���ʼ�����ȡ�����Ŀ��easytest�����Ǳ�ʵ����򵥵�һ�֡���ͨ���ʼ�չʾ�Զ������ԵĽ����

### �ʼ�����

��QQ������Ϊʾ���������������аٶȣ�����ͼһ�����Բ�������ȡ��Ȩ�롣

![image-20210610161708199](http://pic.testtalking.com/testtalking/20210610161708.png)

�������˺ź���Ȩ��ŵ�ProjectConfig.py�ļ��ڡ�

![image-20210610162128145](http://pic.testtalking.com/testtalking/20210610162128.png)

### ���뱨���

��Ϊunittestû��ͳ�ơ�չʾ����Ĺ��ܣ���������������⡪��HTMLTestRunner��

����HTMLTestRunner����ͨ��pip��װ���ұ������commonĿ¼�£�����ȥ�������λ�����Ĺ���һ�棬����bug fix��

![image-20210610181423545](http://pic.testtalking.com/testtalking/20210610181423.png)

![image-20210610135024115](http://pic.testtalking.com/testtalking/20210610182502.png)

��ʵ��HTMLTestRunner�޷����㲿��ͳ�Ƴ������Ҹ�����Ŀ�������ο���������Щ�������ò��ţ��Ͳ��ų����ˣ����ң�HTR����ͳ��չʾ�����Ѿ���ʱ����Ҳ�������á�������������˵��HTMLTestRunner�򵥡����ã��ǳ�ֵ�����֡�

�����Զ������Ա�����˵���ҵĹ۵���**���þ���**��

Ҫ֪����**�����治���ص㣬�ص���Ƿ�����֮ǰ�Ĳ���**��

### ��ǹ����

��main�ļ����µ�run_case�����޸�ΪRunCase�࣬�����������޸ģ�

1�����в����������������Խ������Ϊhtml�ļ�

2����ȡhtml�ļ������ʼ�����ʽ���Ͳ��Ա���

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-
from day10.easytest.common.HTMLTestRunnerCNs import HTMLTestRunner
from day10.easytest.common.logger import write_log
from config.ProjectConfig import ETConfig
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import platform
import unittest
import os.path
import time

class RunCase(object):

    def __init__(self):
        # ������Ϣ
        self.smtpserver = ETConfig.EMAIL_CONFIG['EMAIL_SERVER']
        self.user = ETConfig.EMAIL_CONFIG['EMAIL_USER']
        self.password = ETConfig.EMAIL_CONFIG['EMAIL_PWD']
        self.sender = ETConfig.EMAIL_CONFIG['EMAIL_SENDER']
        self.receiver = ETConfig.EMAIL_CONFIG['EMAIL_RECEIVER']
        self.cc = ETConfig.EMAIL_CONFIG['EMAIL_CC']
        # html����·��
        self.report_dir = "{}report".format(ETConfig.TEST_DIR)

    def run_case(self):
        # ���report�ļ��в����ڣ������ļ���
        if "report" not in os.listdir(ETConfig.TEST_DIR):
            os.mkdir(self.report_dir)

        # ���в���������д��html�ļ�
        with open('{}\\et_result.html'.format(self.report_dir), 'wb') as fp:
            # ����./·���µ�TEST.py�ļ������Լ�������޸�·��
            try:
                write_log.info("RunCaseִ������--��ʼ")
                suite = unittest.TestSuite()
                tests = unittest.defaultTestLoader.discover('..\\testcase', pattern='*Department.py')
                suite.addTest(tests)
                runner = HTMLTestRunner(stream=fp, title=u'�Զ������Ա���', description=u'���л�����{}'.format(platform.platform()), tester="������̷")
                runner.run(suite)
                write_log.info("RunCaseִ������--����")
            except Exception as e:
                write_log.error("RunCaseִ�����������ɱ���ʧ�ܣ�{}".format(e))


    def send_mail(self):
        """
        �����ʼ�
        :return:
        """
        # �򿪱����ļ�
        with open('{}\\et_result.html'.format(self.report_dir), 'rb') as f:
            mail_body = str(f.read(), encoding="utf-8")

        msg = MIMEMultipart('mixed')
        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)
        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)

        msg['Subject'] = u'��easytest���Զ������Ա��� {}'.format(time.strftime("%Y-%m-%d", time.localtime()))
        msg['From'] = u'AutoTest <%s>' % self.sender
        msg['To'] = self.receiver
        msg['Cc'] = self.cc

        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.user, self.password)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
            smtp.quit()
            write_log.info("�����ʼ��ɹ���")
        except Exception as e:
            write_log.error("�����ʼ�ʧ�ܣ�{}".format(e))


if __name__ == '__main__':
    test = RunCase()
    test.run_case()
    test.send_mail()
```

���г��򣬸㶨��

![image-20210611134155373](http://pic.testtalking.com/testtalking/20210611134155.png)

### һ������������ܽ�

**01 �Լ����֣��������˽�����ܵĽ��չʾ���ƣ�ѡ����ʵġ����õı��С�**

**02 ����Ҫ���ĳ�����ϻ㱨��Ŀ�ģ�����ɵû�����˼���Զ������ԵĽ��չʾ���档**