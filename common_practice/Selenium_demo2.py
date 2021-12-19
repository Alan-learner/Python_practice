from time import sleep

from selenium.webdriver import Chrome

web = Chrome()
web.execute('get', {'url': 'http://www.baidu.com'})
web.find_element('name', 'wd').send_keys('iphone')
web.find_element('id', 'su').click()
# web.find_element('name', 'q')._execute("sendKeysToElement",
#                                        {'text': "",
#                                         'value': ""})
sleep(5)
web.quit()
