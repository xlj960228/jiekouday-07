import unittest

import requests
from parameterized import parameterized

from api.api_login import ApiLogin
from tools.read_json import read_json


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取session对象
        cls.session = requests.session()
        # 获取ApiLogin对象
        cls.login = ApiLogin(cls.session)

    # 结束
    @classmethod
    def tearDownClass(cls):
        # 关闭session对象
        cls.session.close()



    # 测试方法
    @parameterized.expand(read_json("login.json"))
    def test_login(self, username, password, verify_code, expect):
        # 调用获取验证码
        self.login.api_verify_code()
        # 调用登录
        r = self.login.api_login(username, password, verify_code)
        # 断言
        self.assertEqual(expect,r.json().get("status"))
