import unittest, logging

from api.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized import parameterized


class TestIHRMLogin(unittest.TestCase):
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


    def test01_login_success(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('登录成功返回的数据为：{}'.format(jsonData))

        # # 断言方法一
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsonData.get('success'))  # 断言success的值
        # self.assertEqual(10000, jsonData.get('code'))  # 断言code
        # self.assertIn('操作成功', jsonData.get('message'))  # 断言message

        # 断言方法二
        assert_common(self, response, 200, True, 10000, '操作成功')

    def test02_username_is_not_exist(self):
        # 调用封装的登录接口
        response = self.login_api.login('13900000002', '123456')
        # 接收返回的json数据
        jsondata = response.json()
        # 输出
        logging.info('账号不存在时返回的结果为{}'.format(jsondata))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test03_pwd_is_error(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', 'error')
        # 接收返回的json 数据
        jsondata = response.json()
        # 输出
        logging.info('密码错误时返回的结果是{}'.format(jsondata))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test04_username_have_special_char(self):
        # 调用封装的登录接口
        response = self.login_api.login('13@#0000002', '123456')
        # 接收返回的json 数据
        jsondata = response.json()
        # 输出
        logging.info('用户名包含特殊字符时时返回的数据结果是{}'.format(jsondata))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test05_username_is_null(self):
        # 调用封装的登录接口
        response = self.login_api.login('', '123456')
        # 接收返回的json 数据
        jsondata = response.json()
        # 输出
        logging.info('用户名为空时返回的结果是{}'.format(jsondata))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test06_pwd_is_null(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '')
        # 接收返回的json 数据
        jsondata = response.json()
        # 输出
        logging.info('密码为空时返回的结果是{}'.format(jsondata))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test07_username_have_chinese(self):
        # 调用封装的登录接口
        response = self.login_api.login('138中0000002', '123456')
        # 接收返回的json 数据
        jsondata = response.json()
        # 输出
        logging.info('账号中有中文时返回的结果是{}'.format(jsondata))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test08_username_middler_have_space(self):
        # 调用封装的登录接口
        response = self.login_api.login('1380 000002', '123456')
        # 接收返回的json 数据
        jsondata = response.json()
        # 输出
        logging.info('账号中有空格时返回的结果是{}'.format(jsondata))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')
