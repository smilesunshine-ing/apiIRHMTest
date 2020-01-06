import unittest, logging

import app
from api.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized import parameterized


class Login(unittest.TestCase):
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

    def test_login(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('登录成功返回的数据为：{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, True, 10000, '操作成功')
        # 获取令牌，并拼接成以bearer开头的令牌字符串
        token = jsonData.get('data')
        # 保存令牌到全局变量
        app.HEADERS['Authorization'] = 'Bearer ' + token
        logging.info('保存的令牌是{}'.format(app.HEADERS))

