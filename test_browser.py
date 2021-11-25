from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

class TestBrowser:
    def setup(self):
        desired_cap = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "noReset":True,
            "browserName":"Chrome",
            #"chromedriverExecutable":"G:/lxj"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(3)