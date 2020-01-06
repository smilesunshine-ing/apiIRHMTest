import pymysql

import app, json


# 编写断言代码函数
def assert_common(self, response, http_code, success, code, message):
    # 断言响应状态码
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get('success'))
    self.assertEqual(code, response.json().get('code'))
    self.assertIn(message, response.json().get('message'))


def read_login_data():
    data_path = app.BASE_DIR + '/data/logindata.json'
    with open(data_path, 'r', encoding='utf-8') as f:
        # 加载文件为json格式的数据
        jsondata = json.load(f)
        # 遍历文件取出其中数据并保存在列表中
        p_list = list()
        for data in jsondata:
            mobile = data.get('mobile')
            password = data.get('password')
            http_code = data.get('http_code')
            success = data.get('success')
            code = data.get('code')
            message = data.get('message')
            p_list.append((mobile, password,
                           http_code, success,
                           code, message))
        print(p_list)
        return p_list


def read_add_emp_data():
    path = app.BASE_DIR + '/data/employee.json'
    # 打开文件
    with open(path, 'r', encoding='utf-8') as f:
        jsondata = json.load(f)
        # 由于employee，json是一个字典数据，
        result_list = list()
        add_emp_data = jsondata.get('add_emp')
        username = add_emp_data.get('username')
        mobile = add_emp_data.get('mobile')
        success = add_emp_data.get('success')
        code = add_emp_data.get('code')
        message = add_emp_data.get('message')
        http_code = add_emp_data.get('http_code')
        result_list.append((username, mobile, success, code, message, http_code))
    print('读取添加员工数据', result_list)
    return result_list


def read_query_emp_data():
    path = app.BASE_DIR + '/data/employee.json'
    # 打开文件
    with open(path, 'r', encoding='utf-8') as f:
        jsondata = json.load(f)
        # 由于employee，json是一个字典数据，
        result_list = list()
        query_emp_data = jsondata.get('query_emp')
        success = query_emp_data.get('success')
        code = query_emp_data.get('code')
        message = query_emp_data.get('message')
        http_code = query_emp_data.get('http_code')
        result_list.append((success, code, message, http_code))
    print('查询添加员工数据', result_list)
    return result_list


def read_modify_emp_data():
    path = app.BASE_DIR + '/data/employee.json'
    # 打开文件
    with open(path, 'r', encoding='utf-8') as f:
        jsondata = json.load(f)
        # 由于employee，json是一个字典数据，
        result_list = list()
        modify_emp_data = jsondata.get('modify_emp')
        success = modify_emp_data.get('success')
        code = modify_emp_data.get('code')
        message = modify_emp_data.get('message')
        http_code = modify_emp_data.get('http_code')
        result_list.append((success, code, message, http_code))
    print('修改添加员工数据', result_list)
    return result_list


def read_delete_emp_data():
    path = app.BASE_DIR + '/data/employee.json'
    # 打开文件
    with open(path, 'r', encoding='utf-8') as f:
        jsondata = json.load(f)
        # 由于employee，json是一个字典数据，
        result_list = list()
        delete_emp_data = jsondata.get('delete_emp')
        success = delete_emp_data.get('success')
        code = delete_emp_data.get('code')
        message = delete_emp_data.get('message')
        http_code = delete_emp_data.get('http_code')
        result_list.append((success, code, message, http_code))
    print('删除添加员工数据', result_list)
    return result_list


class DBUtils:
    def __init__(self, host='182.92.81.159', user='readuser', password='iHRM_user_2019', database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # _-enter__和__exit__是一对魔法方法，主要和with结合使用，
    # 如：with DBUtils() as db:
    # 我们就可以在with的代码块中使用db 来执行sql 语句，这个db 就相当于cursor
    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


if __name__ == '__main__':
    # main函数的作用
    # 防止调用这个模块或者类时，自动执行代码
    # read_login_data()
    # read_add_emp_data() #读取添加员工信息
    read_delete_emp_data()  # 读取查询员工信息
