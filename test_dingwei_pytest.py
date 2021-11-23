
from time import sleep

import pytest as pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestDingWei():
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
            #"dontStopAppOnReset": True,
            # 跳过一些初始化等前置操作
            "skipDeviceInitialization": True,
            #修改语言为汉语
            "unicodeKeyBoard":True,
            #重置语言
            "resetKeyBoard":True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)
    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        '''
        1.打开 雪球 app
        2.点击搜索输入框
        3.向搜索输入框里面输入“阿里巴巴”
        4.在搜索结果里面选择‘阿里巴巴’，然后进行点击
        5.获取这只 阿里巴巴 的股价，并判断 这只股价的价格<200
        '''
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        sleep(3)
        #self.driver.find_element(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        #price=float(self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/current_price' and @text='阿里巴巴']").text)
        #获取元素的文本信息，就是价格，然后转化为float
        price=float(self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]').text)
        #断言股价小于200
        print(price)
        assert price<200

    def test_attribute(self):
        '''
        1.打开 雪球 app首页
        2.定位首页搜索框
        3.判断搜索框是否可用，并查看搜索框name属性值
        4.打印搜索框这个元素的左上角坐标和它的宽高
        5.向搜索框输入：alibaba
        6.判断 [阿里巴巴]是否可见
        7.如果可见，打印“搜索成功”，如果不可见，打印‘搜索失败’
        '''
        ele1=self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search")
        #打印搜索框name属性值
        print(ele1.text)
        #打印它的左上角坐标
        print(ele1.location)
        #打印它的宽高
        print(ele1.size)
        search_enabled=ele1.is_enabled()
        if search_enabled == True:
            ele1.click()
            self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys('alibaba')
            ele2=self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']")
            ele2_displayed=ele2.get_attribute("displayed")
            if ele2_displayed == 'true':
                print("搜索成功")
            else:
                print("搜索失败")


    def test_touchaction(self):
        action = TouchAction(self.driver)
        #按住一个点(x=500,y=850)，等待200毫秒，移动到另外一个点(x=500,y=50)，然后释放，执行这个操作
        #action.press(x=500, y=850).wait(200).move_to(x=500, y=50).release().perform()
        #一般不建议使用坐标，因为如果设备改变，就要重新修改坐标
        #可以采用获取屏幕分辨率
        window_size=self.driver.get_window_rect()
        #获取屏幕宽度，赋值给变量width
        width=window_size['width']
        #获取屏幕高度，赋值给变量width
        height=window_size['height']
        #x1坐标取屏幕宽度的一半
        x1=int(width/2)
        #y1坐标取屏幕高度的4/5
        y1=int(height*4/5)
        # y1坐标取屏幕高度的1/5
        y2=int(height*1/5)
        action.press(x=x1,y=y1).wait(300).move_to(x=x1,y=y2).release().perform()

    def test_get_current(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        #获取股票代码为09988的股票的股价
        current_price=self.driver.find_element(By.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前股票代码为09988的股票的股价为：{current_price}")
        assert float(current_price)<200

    def test_myinfo(self):
        '''
        1. 点击我的，进入到个人信息页面
        2. 点击登录，进入到登录页面
        3. 输入用户名，输入密码
        4. 点击登录
        :return:
        '''
        #使用text定位 “我的”
        #self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        #使用组合定位“我的”：id 和 text
        #self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        #使用组合定位“我的”：class 和 text
        #self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("我的")').click()
        #使用父子关系定位“我的”
        #self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.RelativeLayout").childSelector(text("我的"))').click()
        # 使用兄弟关系定位“我的”
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_icon").fromParent(text("我的"))').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()

    def test_scroll_find_element(self):

        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_text").text("关注")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/empty_button").text("去看看")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("薪者").instance(0))').click()
        sleep(3)


if __name__ == '__main__':
    pytest.main()