"""
    具体用例，调用一系列的页面对象（pom），实现测试行为
"""
import unittest


from ddt import file_data, ddt
from selenium import webdriver

from test_framework.page_object.login_page import LoginPage


@ddt
class case1(unittest.TestCase):
    @file_data('../testdata/login.yaml')
    def test_01(self, name, pwd):
        driver = webdriver.Chrome()
        lp = LoginPage(driver)
        lp.login(name, pwd)


if __name__ == '__main__':
    unittest.main()
