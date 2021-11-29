from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWeiXinXiaoChengXu:
    def setup(self):
        caps = {
            "platformName":"android",
            "deviceName":"127.0.0.1:7555",
            "appPackage":"com.tencent.mm",
            "appActivity":"com.tencent.mm.ui.LauncherUI",
            "noReset":True,
            "unicodeKeyboard": True,
            "resetKeyboard":True,

            # 第一步：设置正确的chromedriver
            "chromedriverExecutable":"G:/lxj/chromedriver.exe",
            # 第二步：设置chromeoption传递给chromedriver,把小程序的进程名传递进去
            #"androidProcess":"com.tencent.mm:appbrand0",
            "goog:chromeOptions":{"androidProcess":"com.tencent.mm:appbrand0"},
            "adbPort":5038

        }

        '''
        caps["platformName"] = "android",
        #caps["deviceName"] = "测试人社区 ceshiren.com"
        caps["deviceName"] = "127.0.0.1:7555",
        caps["appPackage"] = "com.tencent.mm",
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI",
        caps["noReset"] = True,
        caps["unicodeKeyboard"] = True,
        caps["resetKeyboard"] = True,

        # 第一步：设置正确的chromedriver
        caps["chromedriverExecutable"] = "G:/lxj/chromedriver.exe",

        # 因为小程序的进程名跟包名不一样，需要加上这个参数
        #ChromeOptions chromeOptions = new ChromeOptions(),
        #chromeOptions.setExperimentalOption(name: "androidProcess", value: "com.tencent.mm:appbrand0"),
        #desiredCapabilities.setCapability("goog:chromeOptions", chromeOptions),

        # 第二步：设置chromeoption传递给chromedriver,把小程序的进程名传递进去
        caps["chromeOptions"] = {"androidProcess":"com.tencent.mm:appbrand0"},

        # 第三步：使用adb proxy,fix chromedriver的BUG
        # desiredCapabilities.setCapability(capabilityName:"adbPort",value:"5038"),
        caps["adbPort"] = 5038,
        '''
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH,"//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_search(self):
        #原生程序自动化
        size = self.driver.get_window_size()
        self.driver.swipe(size['width']*0.5,size['height']*0.4,size['width']*0.5,size['height']*0.4)
        self.driver.find_element(By.CLASS_NAME,'android.widget.EditText').click()
        self.driver.find_element(By.XPATH,"//*[@text='取消']")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(By.XPATH,"//*[@text='自选']")
        print(self.driver.contexts)

        #进入webview
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.implicitly_wait(10)
        self.find_top_window()

        #css定位
        self.driver.find_element(By.CSS_SELECTOR,"[src*=stock_add]").click()
        #等待新窗口
        WebDriverWait(self.driver,30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR,"._input").click()
        #输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys('alibaba').perform()
        #点击
        self.driver.switch_to.context("WEBVIEW_xweb")
        self.driver.find_element(By.CSS_SELECTOR,".stock_item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock_item").click()

    #微信小程序，打开一个新的小程序后，新的小程序就是顶层窗口，且是VISIBLE状态，其他页面就是INVISIBLE状态
    #只需要找到状态为VISIBLE的页面，就能找到新打开的小程序
    #找顶层可见窗口
    def find_top_window(self):
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print("find 小程序啦")
                print(self.driver.title)
                #return True
            else:
                self.driver.switch_to.window(window)
        #return False
