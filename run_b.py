import unittest
import yagmail
import test_screenshot_selenium
from demo3 import Case03


suite = unittest.TestSuite()
suite.addTest(Case03('test_search1'))
suite.addTest(Case03('test_search2'))
suite.addTest(Case03('test_search3'))
suite.addTest(Case03('test_search4'))
st = open('./report1.html', 'wb')
test_screenshot_selenium.HTMLTestRunner(stream=st, title=u'ui自动化测试').run(suite)

yag = yagmail.SMTP(user="168504524@qq.com",
                   password="vvswzjbmiwgbbjca",
                   host='smtp.qq.com',
                   port='465')
contents = ['尊敬的某某领导：',
            '接口自动化已执行已完成，请查收附件']
yag.send(to='168504524@qq.com',
         cc='188368844@qq.com',
         subject='市南项目报告',
         contents=contents,
         attachments=r'./report1.html')
