大家好，我是谭叔。

本期是最后一部分内容——测试结果的统计展示。

统计展示的方法很多，如接口计数、网页展示、邮件报告等。本项目叫easytest，我们便实现最简单的一种——通过邮件展示自动化测试的结果。

### 邮件配置

以QQ邮箱作为示例（其他邮箱自行百度），如图一顿无脑操作，获取授权码。

![image-20210610161708199](http://pic.testtalking.com/testtalking/20210610161708.png)

将邮箱账号和授权码放到ProjectConfig.py文件内。

![image-20210610162128145](http://pic.testtalking.com/testtalking/20210610162128.png)

### 引入报告库

因为unittest没有统计、展示结果的功能，故需引入第三方库——HTMLTestRunner。

又因HTMLTestRunner不能通过pip安装，我便放在了common目录下，是我去年基于两位博主改过的一版，做了bug fix。

![image-20210610181423545](http://pic.testtalking.com/testtalking/20210610181423.png)

![image-20210610135024115](http://pic.testtalking.com/testtalking/20210610182502.png)

其实，HTMLTestRunner无法满足部分统计场景，我根据项目做过二次开发，但这些东西你用不着，就不放出来了，并且，HTR这套统计展示机制已经过时，我也基本弃用。但，于新人来说，HTMLTestRunner简单、易用，非常值得入手。

对于自动化测试报告来说，我的观点是**够用就行**。

要知道，**发报告不是重点，重点的是发报告之前的操作**。

### 鸟枪换炮

将main文件夹下的run_case方法修改为RunCase类，做以下两步修改：

1、运行测试用例，并将测试结果汇总为html文件

2、读取html文件，以邮件的形式发送测试报告

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
        # 邮箱信息
        self.smtpserver = ETConfig.EMAIL_CONFIG['EMAIL_SERVER']
        self.user = ETConfig.EMAIL_CONFIG['EMAIL_USER']
        self.password = ETConfig.EMAIL_CONFIG['EMAIL_PWD']
        self.sender = ETConfig.EMAIL_CONFIG['EMAIL_SENDER']
        self.receiver = ETConfig.EMAIL_CONFIG['EMAIL_RECEIVER']
        self.cc = ETConfig.EMAIL_CONFIG['EMAIL_CC']
        # html报告路径
        self.report_dir = "{}report".format(ETConfig.TEST_DIR)

    def run_case(self):
        # 如果report文件夹不存在，创建文件夹
        if "report" not in os.listdir(ETConfig.TEST_DIR):
            os.mkdir(self.report_dir)

        # 运行测试用例并写入html文件
        with open('{}\\et_result.html'.format(self.report_dir), 'wb') as fp:
            # 运行./路径下的TEST.py文件，视自己的情况修改路径
            try:
                write_log.info("RunCase执行用例--开始")
                suite = unittest.TestSuite()
                tests = unittest.defaultTestLoader.discover('..\\testcase', pattern='*Department.py')
                suite.addTest(tests)
                runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'运行环境：{}'.format(platform.platform()), tester="测试奇谭")
                runner.run(suite)
                write_log.info("RunCase执行用例--结束")
            except Exception as e:
                write_log.error("RunCase执行用例，生成报告失败：{}".format(e))


    def send_mail(self):
        """
        发送邮件
        :return:
        """
        # 打开报告文件
        with open('{}\\et_result.html'.format(self.report_dir), 'rb') as f:
            mail_body = str(f.read(), encoding="utf-8")

        msg = MIMEMultipart('mixed')
        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)
        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)

        msg['Subject'] = u'【easytest】自动化测试报告 {}'.format(time.strftime("%Y-%m-%d", time.localtime()))
        msg['From'] = u'AutoTest <%s>' % self.sender
        msg['To'] = self.receiver
        msg['Cc'] = self.cc

        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.user, self.password)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
            smtp.quit()
            write_log.info("发送邮件成功！")
        except Exception as e:
            write_log.error("发送邮件失败：{}".format(e))


if __name__ == '__main__':
    test = RunCase()
    test.run_case()
    test.send_mail()
```

运行程序，搞定！

![image-20210611134155373](http://pic.testtalking.com/testtalking/20210611134155.png)

### 一如既往，做个总结

**01 自简单上手，再深入了解各类框架的结果展示机制，选择合适的、够用的便行。**

**02 若你要达成某种向上汇报的目的，那你可得花点心思在自动化测试的结果展示上面。**