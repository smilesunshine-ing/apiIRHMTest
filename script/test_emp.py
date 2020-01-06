import logging
import unittest

import pymysql

import app
from api.emp_api import EmpApi
from api.login_api import LoginApi
from utils import assert_common, read_add_emp_data, read_query_emp_data, read_modify_emp_data, read_delete_emp_data, \
    DBUtils
from parameterized import parameterized


class TestIHRMEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化员工类
        cls.emp_api = EmpApi()
        cls.login_api = LoginApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # def test01_login(self):
    #     # 调用封装的登录接口
    #     response = self.login_api.login('13800000002', '123456')
    #     # 接收返回的json数据
    #     jsonData = response.json()
    #     # 调试输出登录接口返回的数据
    #     logging.info('登录成功返回的数据为：{}'.format(jsonData))
    #     # 断言
    #     assert_common(self, response, 200, True, 10000, '操作成功')
    #     # 获取令牌，并拼接成以bearer开头的令牌字符串
    #     token = jsonData.get('data')
    #     # 保存令牌到全局变量
    #     app.HEADERS['Authorization'] = 'Bearer ' + token
    #     logging.info('保存的令牌是{}'.format(app.HEADERS))

    @parameterized.expand(read_add_emp_data)
    def test02_add_emp(self, username, mobile, success, code, message, http_code):
        # 调用添加员工接口
        response = self.emp_api.add_emp(username, mobile)
        # 获取添加员工接口的json数据
        jsondata = response.json()
        # 输出json 数据
        logging.info('添加员工接口返回数据为：{}'.format(jsondata))
        # 断言
        assert_common(self, response, http_code, success, code, message)
        logging.info(11)
        # 获取员工ID保存到全局变量
        app.EMP_ID = jsondata.get('data').get('id')
        # 打印获取到的员工ID
        logging.info('添加员工ID为：', app.EMP_ID)

    # def test02_add_emp(self):
    #     # 调用添加员工接口
    #     response = self.emp_api.add_emp('4340833212', '42104739835965327563212')
    #     # 获取添加员工接口的json数据
    #     jsondata = response.json()
    #     # 输出json 数据
    #     logging.info('添加员工接口返回数据为：{}'.format(jsondata))
    #     # 断言
    #     assert_common(self, response, 200, True, 10000, '操作成功')
    #
    #     # 获取员工ID保存到全局变量
    #     app.EMP_ID = jsondata.get('data').get('id')
    #     # 打印获取到的员工ID
    #     logging.info('添加员工ID为：', app.EMP_ID)

    @parameterized.expand(read_query_emp_data)
    def test03_query_emp(self, success, code, message, http_code):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 获取查询员工接口的返回json数据
        jsondata = response.json()
        # 输出数据
        logging.info('查询员工接口返回的数据为：{}'.format(jsondata))

        # 断言
        assert_common(self, response, http_code, success, code, message)

    # def test03_query_emp(self):
    #     # 调用查询员工接口
    #     response = self.emp_api.query_emp()
    #     # 获取查询员工接口的返回json数据
    #     jsondata = response.json()
    #     # 输出数据
    #     logging.info('查询员工接口返回的数据为：{}'.format(jsondata))
    #     # 断言
    #     assert_common(self, response, 200, True, 10000, '操作成功', )

    @parameterized.expand(read_modify_emp_data)
    def test04_modify_emp(self,username,success, code, message, http_code):
        # 调用修改员工数据
        response = self.emp_api.modify_emp('3254大脸猫哈哈哈')
        # 获取修改员工接口返回的的json数据
        jsondata = response.json()
        # 输出json数据
        logging.info('修改员工信息接口返回的的json数据为{}'.format(jsondata))

        with DBUtils as db_utils:
            #执行查询语句，查询添加的员工的username是不是修改的username
            sql = 'select username from bs_user where id ={}'.format(app.EMP_ID)
            db_utils.execute(sql)
            #获取执行结果
            result = db_utils.fetchone()[0]
            logging.info('从数据库中查询出的员工的用户名为：{}'.format(result))
            self.assertEqual(username,result)


        # 断言
        assert_common(self, response, http_code, success, code, message)

    # def test04_modify_emp(self):
    #     # 调用修改员工数据
    #     response = self.emp_api.modify_emp('3254大脸猫哈哈哈')
    #     # 获取修改员工接口返回的的json数据
    #     jsondata = response.json()
    #     # 输出json数据
    #     logging.info('修改员工信息接口返回的的json数据为{}'.format(jsondata))
    #     # 断言
    #     assert_common(self, response, 200, True, 10000, '操作成功')

    @parameterized.expand(read_delete_emp_data)
    def test05_delete_emp(self,success, code, message, http_code):
        # 删除员工数据
        response = self.emp_api.delete_emp()
        # 获取删除员工接口返回的数据
        jsondata = response.json()
        # 输出数据
        logging.info('删除员工之后返回的的josn数据为{}'.format(jsondata))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    # def test05_delete_emp(self):
    #     # 删除员工数据
    #     response = self.emp_api.delete_emp()
    #     # 获取删除员工接口返回的数据
    #     jsondata = response.json()
    #     # 输出数据
    #     logging.info('删除员工之后返回的的josn数据为{}'.format(jsondata))
    #     # 断言
    #     assert_common(self, response, 200, True, 10000, '操作成功')
