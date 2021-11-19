import pytest as pytest
from appium import webdriver
from selenium.webdriver.common.by import By


class TestDingWei():
    def setup(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            # 第一次点击app后，将后台更新的按钮关掉，然后将 "noRest"设置为 True，
            # 意思是：不要对后台的更新进行初始化，保持为不更新的状态,不清除缓存信息
            "noRest": True,
            # 首次启动的时候，不停止app,这样每次运行测试用例的时候，就不用每次都重启app
            "dontStopAppOnReset": True,
            # 跳过一些初始化等前置操作
            "skipDeviceInitialization": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_search(self):
        print("搜索测试用例")
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys('alibaba')

if __name__ == '__main__':
    pytest.main()