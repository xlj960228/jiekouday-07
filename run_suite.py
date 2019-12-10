import unittest


# 定义测试套件
from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts")
# 获取文件存储文件流 并实例化HtmlTestRunner  调用run
with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)