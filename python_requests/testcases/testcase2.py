# coding:utf-8
from python_requests.common.http_request import HttpRequest
import unittest


class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.get_method = "get"
        cls.post_method = "post"
        cls.url = ""
        cls.http_request = HttpRequest()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test1(self):
        params = {"key1": "value1",
                  "key2": "value2"
                  }
        headers = {"key1": "value1",
                   "key2": "value2"
                   }
        res = self.http_request.http_request(method=self.get_method, url=self.url, params=params, headers=headers)

    def test2(self):
        data = {"key1": "value1",
                "key2": "value2"
                }
        json = {"key1": "value1",
                "key2": "value2"
                }
        headers = {"key1": "value1",
                   "key2": "value2"
                   }
        res = self.http_request.http_request(method=self.post_method, url=self.url, data=data, json=json,
                                             headers=headers)
