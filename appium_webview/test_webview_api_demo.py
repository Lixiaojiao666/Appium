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
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.ApiDemos",
            "noReset":True,
            #"browserName":"Chrome",
            "autoGrantPermissions":True,
            #"chromedriverExecutable":"D:/chromedriver"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass

    def test_webdriver(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        #打印上下文：在打开web页面之前，只有一个：['NATIVE_APP']
        print(self.driver.contexts)

        #页面向下滑动到底部，然后找到 WebView ，并且点击它
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0))').click()
        # 打印上下文：在打开web页面之后，有两个：['NATIVE_APP', 'WEBVIEW_io.appium.android.apis']
        print(self.driver.contexts[-1])
        #此时就需要切换一下上下文,之前在app上，现在要切换到web页面上
        self.driver.switch_to.context(self.driver.contexts[-1])

        #原生应用内如果有web页面，原生应用会将web页面渲染为的原生组件内容，不同的手机对web页面的渲染效果是不一样的，这样就造成了不同的手机的元素属性可能不同，换个手机就会定位不准
        #比较准的定位方式是使用chrome://inspector来直接定位web页面的元素，而不是渲染后的组件
        #self.driver.find_element(By.XPATH,"//*[@resource-id='i_am_a_textbox']").send_keys("123456")
        #sleep(3)
        #self.driver.find_element(By.XPATH, "//*[@resource-id='i am a link']").click()

        #使用chrome://inspector来定位元素
        self.driver.find_element(By.ID,'i_am_a_textbox').send_keys("123456")
        sleep(3)
        self.driver.find_element(By.ID,'i am a link').click()
        print(self.driver.page_source)


