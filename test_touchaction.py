from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.MainActivity",
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


    # 解锁手势密码
    def test_touchaction_unclock(self):
        print("解锁手势密码")
        action = TouchAction(self.driver)
        action.press(x=243,y=395).wait(150).move_to(x=721,y=378).wait(150).move_to(x=1190,y=364)\
            .wait(150).move_to(x=1202,y=859).wait(150).move_to(x=1195,y=1339).release().perform()
