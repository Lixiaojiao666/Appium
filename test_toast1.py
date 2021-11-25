from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

class TestToast:
    def setup(self):
        desired_cap = {
            "platformName": "android",
            #设备名字可以是任意的，不能确定是哪个设备，只有udid可以唯一确定启用哪个设备
            "deviceName": "127.0.0.1:7555",
            # 设备唯一标识，设置后，将启动设置的设备而不是默认设备。
            "udid": "127.0.0.1:7555",
            "appPackage": "io.appium.android.apis",
            "appActivity": ".view.PopupMenu1",
            #定义工作引擎为uiautomator2，android默认工作引擎就是uiautomator2
            "automationName":"uiautomator2"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass

    def test_toast(self):
        #MobileBy才有ACCESSIBILITY_ID属性，By没有这个属性
        #ACCESSIBILITY_ID属性 就是content-desc
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Make a Popup!').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Search"]').click()
        #通过text，定位toast
        #toast_text=self.driver.find_element(MobileBy.XPATH,'//*[@text="Clicked popup menu item Search"]').text
        # 通过text,contains包含了部分文本 ，定位toast
        toast_text = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked popup")]').text
        #通过class，定位toast
        #toast_text = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        print(toast_text)