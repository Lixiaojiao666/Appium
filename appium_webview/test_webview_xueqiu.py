from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "noReset":True,
            "skipServerInstallation":True,
            #"browserName":"Chrome",
            "autoGrantPermissions":True,
            #单个chromedriver路径
            #"chromedriverExecutable":"D:/chromedriver/chromedriver2.39-66.exe",
            #如果有多个版本的chromedriver需要使用，可以设置如下：
            "chromedriverExecutableDir":"D:/chromedriver/all",
            "chromedriverChromeMappingFile":"C:/Users/李晓娇/PycharmProjects/Appium/appium_webview/mapping.json"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass

    def test_webview_xueqiu(self):
        '''
        打开应用
        点击“交易”
        点击“A股开户”
        输入用户名和密码
        点击“立即开户”
        退出应用
        :return:
        '''
        #自己写的

        print(self.driver.contexts)
        #print(self.driver.window_handles)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("交易")').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="去开户"]').click()
        print(self.driver.contexts)
        #print(self.driver.window_handles)
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="phone-number"]').send_keys("15588886666")
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="code"]').send_keys("123456")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="立即开户"]').click()
        '''

        #奇怪，我写的好像没用到嵌入的webview页面，不需要切换上下文，不需要切换windows，也成功了
        #老师写的,在我这里通不过

        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()
        A_locator = (MobileBy.XPATH,'//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        #print(self.driver.window_handles)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        #kaihu_window = self.driver.window_handles[-1]
        #self.driver.switch_to.window(kaihu_window)

        phonenumber_locator=(MobileBy.ID,'phone-number')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(phonenumber_locator))
        self.driver.find_element(*phonenumber_locator).send_keys("13810100202")
        self.driver.find_element(MobileBy.ID,'code').send_keys("1234")
        self.driver.find_element(MobileBy.CSS_SELECTOR,'body > div > div > div.form-wrap > div > div.btn-submit').click()
        '''
