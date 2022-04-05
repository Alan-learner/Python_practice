"""
    Appium自动化app uice测试
"""

from appium import webdriver

# step1.设置终端设备参数项
ue_conf = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "Xiaomi 9",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset": True
}
# step2.电脑启动appium server
# 127.0.0.1：4723（默认端口）

# step3.使用adb命令连接设备ip(让模拟器/真机能够被电脑识别)
# cmd: adb connect 127.0.0.1:62001(夜神端口)

# step4.配置ue_conf.appPackage,ue_conf.appActivity参数
# cmd:D:\Andriod_sdk\Andriod_SDK\build-tools\29.0.3>aapt dump badging "D:\AutoWork\DCA07D1BA344B81557143655D303C8B9.apk" | findstr package
# cmd:D:\Andriod_sdk\Andriod_SDK\build-tools\29.0.3>aapt dump badging "D:\AutoWork\DCA07D1BA344B81557143655D303C8B9.apk" | findstr launchable activity


# step4.发送指令给apium servr，SDK中转给安卓终端
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', ue_conf)

# step5.元素定位及操作
el_pwd = driver.find_element(by=AppiumBy.ID, value='id')
el_pwd.send_keys('pwd123')
# 隐式等待
driver.implicitly_wait(15)
# java 底层方法定位
el_usrname = driver.find_element_by_android_uiautomator('new Uiselector().text("请输入用户名")')
el_usrname.send_keys('name123')
# java 底层组合方法定位
el_login = driver.find_element_by_android_uiautomator('new Uiselector().text("登录").resourseId("id is here")')
el_login.click()
# 通过content-desc/description属性定位
el_qq_pwd = driver.find_element_by_accessibility_id('密码 安全（描述框）')
# 报错则卸载weditor默认安装的atx程序
# xpath定位，不稳定(页面一旦调整就会变更，需要不断维护)，优先使用weditor来定位
el_qq_usrname = driver.find_element_by_xpath('xpath')
el_qq_usrname.send_keys('usr123')

# step6.四大常见操作
el_pwd.click()
el_qq_pwd.send_keys()
print(el_qq_usrname.text)
el_login.get_attribute('description')

# step7.进阶操作
# 获取屏幕尺寸
screen_size = driver.get_window_size()
x = screen_size['width']
y = screen_size['height']
print('屏幕尺寸:', screen_size)
# 左滑两次
for k in range(2):
    driver.swipe(
        start_x=x * 0.9,
        start_y=y * 0.5,
        end_x=x * 0.5,
        end_y=y * 0.5,
        duration=1000
    )
