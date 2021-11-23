from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebDriverWait:
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

    def test_webdirver_wait(self):

        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        sleep(3)
        locator = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]')
        #WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))

        #使用lambda表达式
        ele = WebDriverWait(self.driver,10).until(lambda x:x.find_element(*locator))
        print(ele.text)
        price = float(ele.text)

        # 获取元素的文本信息，就是价格，然后转化为float
        #price = float(self.driver.find_element(*locator).text)
        # 断言股价小于200
        print(price)
        assert price < 200