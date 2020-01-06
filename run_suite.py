import os
import time
import unittest
import app
from tools.HTMLTestRunner import HTMLTestRunner
# 1.初始化suite
from script.login import Login
from script.test_emp import TestIHRMEmp


suite = unittest.TestSuite()
# 2.将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))
# suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 3.使用HTMLRunner 执行测试套件，生成测试报告
report_path = app.BASE_DIR + '/report/ihrm{}.html'.format(time.strftime('%Y%m%d-%H%M%S'))
with open(report_path, 'wb') as f:
    # 初始化HTMLRunner
    runner = HTMLTestRunner(f, verbosity=1, title='IHRM人力资源接口测试', description='v1.0.0')
    # 使用runner运行测试套件
    runner.run(suite)
