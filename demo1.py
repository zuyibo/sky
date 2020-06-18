import requests
import unittest


class Case01(unittest.TestCase):
    def case_01(self):
        self.url = 'http://apis.juhe.cn/simpleWeather/query'
        self.payload = {"key": "d174def31d332aff7292020ea1ad60be",
                        "city": "北京"}
        r = requests.get(self.url, self.payload)
        result = r.json()
        self.assertEqual(result['result']['realtime']['info'], '阴')

    def case_03(self):
        self.url = 'http://apis.juhe.cn/simpleWeather/query'
        self.payload = {"key": "d174def31d332aff7292020ea1ad60be",
                        "city": "上海"}
        r = requests.get(self.url, self.payload)
        result = r.json()
        self.assertEqual(result['result']['realtime']['info'], '多云')
