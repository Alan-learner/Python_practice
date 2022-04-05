import logging

from appium import webdriver

from autoapptest.app_test_pom.testaw.read_yaml import PathCfg, ReadYaml


class BasePage(object):
    def __init__(self, relative_data_path='app_cfg.yaml'):
        """
        :param relative_data_path: 对于testdata的路径
        """
        data_path = PathCfg(file_name=relative_data_path)
        app_conf = ReadYaml(data_path)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', app_conf)

    def locator(self, loc_info):
        # loc_info = (MobileBy.ID, "RescourseId值")
        return self.driver.find_element(*loc_info)

    def input(self, loc_info, msg):
        self.locator(loc_info).send_keys(msg)

    def click(self, loc_info):
        self.locator(loc_info).click()

    def get_screen_size(self):
        size_dict = self.driver.get_window_size()
        width, height = size_dict.values()
        logging.info(f'屏幕尺寸为：长 {height}，宽 {width}')
        return width, height

    def swap_left(self, num=1, duration=1000):
        x, y = self.get_screen_size()
        for k in range(num):
            self.driver.swipe(
                start_x=x * 0.8,
                start_y=y * 0.5,
                end_x=x * 0.5,
                end_y=y * 0.5,
                duration=duration
            )

    def swap_right(self, num=1, duration=1000):
        x, y = self.get_screen_size()
        for k in range(num):
            self.driver.swipe(
                start_x=x * 0.2,
                start_y=y * 0.5,
                end_x=x * 0.5,
                end_y=y * 0.5,
                duration=duration
            )

    def swap_up(self, num=1, duration=1000):
        x, y = self.get_screen_size()
        for k in range(num):
            self.driver.swipe(
                start_x=x * 0.5,
                start_y=y * 0.8,
                end_x=x * 0.5,
                end_y=y * 0.5,
                duration=duration
            )

    def swap_down(self, num=1, duration=1000):
        x, y = self.get_screen_size()
        for k in range(num):
            self.driver.swipe(
                start_x=x * 0.5,
                start_y=y * 0.2,
                end_x=x * 0.5,
                end_y=y * 0.5,
                duration=duration
            )
