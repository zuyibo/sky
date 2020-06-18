from selenium import webdriver
import unittest
from time import sleep


class Case03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(15 * '=' + '开始' + 15 * '=')

    @classmethod
    def tearDownClass(cls):
        print(15 * '=' + '结束' + 15 * '=')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        sleep(2)

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_search1(self):
        self.driver.find_element_by_id("kw").send_keys(u"腾讯视频")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.assertEqual(u"腾讯视频_百度搜索", self.driver.title)

    def test_search2(self):
        self.driver.find_element_by_id("kw").send_keys(u"S9")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.assertEqual(u"S9_百度搜索", self.driver.title)

    def test_search3(self):
        self.driver.find_element_by_id("kw").send_keys(u"英雄联盟")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.assertEqual(u"英雄联盟_百度搜索", self.driver.title)

    def test_search4(self):
        self.driver.find_element_by_id("kw").send_keys(u"iphone11")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.assertEqual(u"iphone11_百度搜索", self.driver.title)
