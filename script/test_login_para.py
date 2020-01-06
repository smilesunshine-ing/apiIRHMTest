import unittest, logging

from api.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized import parameterized


class TestIHRMLoginPara(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.login_api = LoginApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(read_login_data)
    def test_login(self, mobile, password, http_code, success, code, message):
        # 调用封装的登录接口
        response = self.login_api.login(mobile, password)
        # 接收返回的json数据
        jsondata = response.json()
        # 输出
        logging.info('登录返回的结果为{}'.format(jsondata))
        # 断言
        assert_common(self, response, http_code, success, code, message)
