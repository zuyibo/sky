import unittest
from selenium import webdriver
from time import sleep


class Case05(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(9 * '=' + '开始' + 9 * '=')

    @classmethod
    def tearDownClass(cls):
        print(9 * '=' + '结束' + 9 * '=')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        sleep(2)

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_04(self):
        self.driver.find_element_by_id('kw').send_keys('你好')
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.assertEqual(u'你好_百度搜索', self.driver.title)


if __name__ == '__main__':
    unittest.main()
