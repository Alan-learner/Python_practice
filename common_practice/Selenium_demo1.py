from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
# 使用驱动，启动浏览器
driver.get('http://www.baidu.com')
# 配置访问网址地址栏属性
driver.find_element_by_name('wd').send_keys('肖申克的救赎')
# 在搜索框内输入关键字    find_element一定是查找有对应属性的元素
driver.find_element_by_id('su').click()
# 点击搜索按钮
sleep(5)
driver.quit()
# 关闭浏览器并释放资源
