import unittest
import yagmail
import HTMLTestRunner_cn
from demo1 import Case01
from demo2 import Case02


suite = unittest.TestSuite()
suite.addTest(Case01('case_01'))
suite.addTest(Case01('case_03'))
suite.addTest(Case02('case_02'))
st = open('./report.html', 'wb')
HTMLTestRunner_cn.HTMLTestRunner(stream=st, title=u'接口自动化测试').run(suite)

yag = yagmail.SMTP(
    user="168504524@qq.com",
    password="vvswzjbmiwgbbjca",
    host='smtp.qq.com',
    port='465')
contents = ['尊敬的某某领导：',
            '接口自动化已执行已完成，请查收附件']

yag.send(to='168504524@qq.com',
         cc='188368844@qq.com',
         subject='市南项目报告',
         contents=contents,
         attachments=r'./report.html')