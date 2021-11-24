from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestGetAttribute:
    def setup(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            # 第一次点击app后，将后台更新的按 v   z钮关掉，然后将 "noRest"设置为 True，
            # 意思是：不要对后台的更新进行初始化，保持为不更新的状态,不清除缓存信息
            "noRest": True,
            # 首次启动的时候，不停止app,这样每次运行测试用例的时候，就不用每次都重启app
            # "dontStopAppOnReset": True,
            # 跳过一些初始化等前置操作
            "skipDeviceInitialization": True,
            # 修改语言为汉语
            "unicodeKeyBoard": True,
            # 重置语言
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_get_attribute(self):
        search_ele = self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
        assert 'search' in search_ele.get_attribute("enabled")

    def test_hamcrest(self):
        #equal_to:等于
        assert_that(10,equal_to(10))
        #close_to：10上下浮动2
        assert_that(12,close_to(10,2))
        #contains_string:包含字符串
        assert_that("contains some string",contains_string("string"))


