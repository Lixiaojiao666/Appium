from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        desired_cap = {
            "platformName": "android",
            #"platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "noReset":True,
            "browserName":"Chrome",
            "autoGrantPermissions":True
            #"chromedriverExecutable":"G:/lxj"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element(By.ID,"index-kw").click()
        self.driver.find_element(By.ID,"index-kw").send_keys("appium")
        search_locator = self.driver.find_element(By.ID,"index-bn")
        #添加显式等待
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locator))
        #find_element(*变量) 括号里不放xpath，放变量的话，要在变量前面加*
        self.driver.find_element(*search_locator).click()
        sleep(3)