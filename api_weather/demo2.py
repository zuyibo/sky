import requests
import unittest


class Case02(unittest.TestCase):
    def case_02(self):
        self.url = 'http://japi.juhe.cn/charconvert/change.from'
        self.payload = {"key": "7d9e7ceb9b3432c4bd8d1ad663dbd1c9",
                        "text": "龙",
                        "type": "1"}
        r = requests.get(self.url, self.payload)
        result = r.json()
        self.assertEqual(result['outstr'], '龍')
