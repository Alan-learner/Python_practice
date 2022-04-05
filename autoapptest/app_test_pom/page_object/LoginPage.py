from appium.webdriver.common.mobileby import MobileBy

from autoapptest.app_test_pom.base_page.BasePage import BasePage


class LoginPage(BasePage):
    el_cancle = (MobileBy.ID, 'id')
    el_tiyan = (MobileBy.ID, '')
    el_username = ''
    el_pwd = ''
    el_login = ''

    def login(self, username, password):
        self.click(self.el_cancle)
        self.swap_left(num=2)
        self.click(self.el_tiyan)
        self.input(self.el_username, username)
        self.input(self.el_pwd, password)
        self.click(self.login())
