from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.webdriver.common.by import By


class TestParam:
    def setup(self):
        desired_cap = {
            "platformName": "android",
            #设备名字可以是任意的，不能确定是哪个设备，只有udid可以唯一确定启用哪个设备
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
            "resetKeyBoard": True,
            #两次请求的间隔时间，即超时时间（默认60秒），如果网络不好，或者上传文件，可以设置的超时时间长点，这样就不会总是报错
            "newCommandTimeout":300,
            #设备唯一标识，设置后，将启动设置的设备而不是默认设备。
            "udid":"127.0.0.1:7555",
            #首次启动app的时候，一般会有弹窗提示获取位置权限，录音权限，获取通讯录权限等弹窗
            #该参数设置为true，可以自动接受弹窗提示
            #特别注意：如果noReset为true，那么这个参数就不生效
            "autoGrantPermissions":True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass
        #self.driver.quit()

    @pytest.mark.parametrize('searchkey,type,expect_price',[
        ('alibaba','BABA',130.00),
        ('xiaomi','40209',100.00)
    ])
    def test_param(self,searchkey,type,expect_price):
        '''
        1.打开雪球应用
        2.点击 搜索框
        3.输入 搜索词 阿里巴巴 或 小米
        4.点击第一个搜索结果
        5.判断股票价格
        :return:
        '''
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        sleep(3)
        current_price=self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert_that(float(current_price),close_to(expect_price,expect_price*0.1))


