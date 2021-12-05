"""
    selenium框架常用操作函数封装
"""
from time import sleep

from selenium import webdriver


def open_browser(type):
    # if type == 'Chrome':
    #     driver = webdriver.Chrome()
    # elif type == 'Ie':
    #     driver = webdriver.Ie()
    # else:
    #     driver = webdriver.Firefox()
    try:
        # 基于python的反射机制实现
        driver = getattr(webdriver, type)()
        # 从webdriver(类)中获取一个type属性，加()代表是函数
    except Exception as e:
        # 报错则默认用Chrome浏览器
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:
    # 创建临时的driver对象啊
    # driver = webdriver.Chrome()

    def __init__(self, type):
        self.driver = open_browser(type)

    # 访问url
    def open_url(self, url):
        self.driver.get(url)

    # 查找元素：以一定方法，根据指定内容查找
    def locater(self, method, txt):
        return self.driver.find_element(method, txt)

    # 输入内容
    def input_txt(self, method, txt, ctxt):
        self.locater(method, txt).send_keys(ctxt)

    # 点击
    def clicker(self, method, txt):
        self.locater(method, txt).click()

    # 等待
    def wait(self, time):
        sleep(time)

    # 关闭
    def quit(self):
        self.driver.quit()
