import requests
import logging
import app


class EmpApi:
    def __init__(self):
        self.emp_url = app.HOST + '/api/sys/user'
        # 注意：如果调用员工管理模块的相关接口时，先调用login。py接口，
        # 那么获取到的app.HEADERS是{“Content-Type”：“application”，“Authorization”：“Bearer ;xx-xx-xx-”}
        self.headers = app.HEADERS
        pass

    def add_emp(self, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-07",
            "formOfEmployment": 1,
            "workNumber": "1267378",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2020-02-04T16:00:00.000Z"
        }
        # 发送添加员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        return response

    def query_emp(self):
        # 查询员工
        url = self.emp_url + '/' + app.EMP_ID
        return requests.get(url, headers=self.headers)

    def modify_emp(self, username):
        # 修改员工信息
        url = self.emp_url + '/' + app.EMP_ID
        # 从外部接收到的数据，拼接成json数据
        data = {
            "username": username
        }
        # 返回查询结果
        return requests.put(url, json=data, headers=self.headers)

    def delete_emp(self):
        # 删除员工信息
        url = self.emp_url + '/' + app.EMP_ID
        # 返回调用删除的接口并返回响应数据
        return requests.delete(url, headers=self.headers)
