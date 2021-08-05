# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
Author：公众号：测试奇谭
"""
from common.HTMLTestRunnerCNs import HTMLTestRunner
from common.logger import write_log
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
