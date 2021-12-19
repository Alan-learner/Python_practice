"""
    BssePage:基类，封装常用的操作行为，便于后续流程调用
"""
from time import sleep

from selenium import webdriver


class BasePage:
    # 临时driver对象
    # driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 元素定位
    # def locator(self,type,value):
    #     return self.driver.find_element(type,value)
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 等待
    def wait(self, time):
        sleep(time)

    # 退出
    def quit(self):
        self.driver.quit()