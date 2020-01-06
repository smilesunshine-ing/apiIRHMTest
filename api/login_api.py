import requests
import app


class LoginApi:
    def __init__(self):
        self.login_url = app.HOST + '/api/sys/login'
        self.headers = app.HEADERS

    # 从外面接受mobile 和password
    # 为什么这样写？
    # 字典数据的话，后续进行参数化时，会很不方便，所以改成接收两个变量
    def login(self, mobile, password):
        # 使用data来接受外面传入的的数据，拼接成要发送的数据
        data = {"mobile": mobile,
                "password": password}

        # 发送登录接口请求
        response = requests.post(self.login_url,
                                 json=data,
                                 headers=self.headers)

        # 返回响应数据
        return response

