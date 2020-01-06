import app
import logging

# 初始化日志
# 为什么在api__init__.py中初始化日志？
# 这是因为。我们后面进行接口测试时，都会调用封装的API接口，调用时，都会自动运行__init__.py
# 从而实现自动初始化日志的功能
app.init__logging()
logging.info('test日志器能不能正常工作')
