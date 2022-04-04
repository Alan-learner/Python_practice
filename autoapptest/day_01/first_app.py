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
