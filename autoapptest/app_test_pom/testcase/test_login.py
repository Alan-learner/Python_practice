import pytest

from autoapptest.app_test_pom.page_object.LoginPage import LoginPage


class TestLogin:
    def setup(self):
        self.login = LoginPage(relative_data_path="app_cfg.yaml")

    # 装饰器数据驱动测试，也可以从文件读取
    @pytest.mark.parametrize("username,password", [('user123', 'pwd123'), ('user234', 'pwd234')])

    def test_login(self, username, password):
        self.login.login(username, password)


if __name__ == '__main__':
    pytest.main()
