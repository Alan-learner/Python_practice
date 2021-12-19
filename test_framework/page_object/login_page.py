"""
    登录页，实现系统的登录流程
"""
from selenium import webdriver

from test_framework.base.base_page import BasePage


class LoginPage(BasePage):
    # 页面url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    # 页面操作元素
    name = ('name', 'accounts')
    pwd = ('name', 'pwd')
    button = ('xpath', '//button[text()="登录"]')

    # 登录操作流程
    def login(self, account, password):
        self.open(self.url)
        self.input(self.name, account)
        self.input(self.pwd, password)
        self.click(self.button)
        self.wait(10)
        self.quit()



