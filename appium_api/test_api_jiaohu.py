from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestSearch:
    def setup(self):
        desired_cap = {
            "platformName": "android",
            "platformVersion": "5.0",
            #自动启动模拟器（只能启动android自带的模拟器）
            "avd": "AVD_23_6",
            "deviceName": "emulator-5554",
            "browserName":"Chrome",
            "noReset": True,
            "unicodeKeyBoard":True,
            "resetKeyBoard":True,

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)
    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        #开始录屏
        self.driver.start_recording_screen()

        self.driver.get("http://m.baidu.com")
        #模拟来电话
        self.driver.make_gsm_call('19912345678',GsmCallActions.CALL)
        #模拟来短信
        self.driver.send_sms('19912345688','hello appium api')
        #设置网络连接
        ''' 
        网络连接类型如下： 
        0 (None) 000
        1 (Airplane Mode) 001
        2 (Wifi only) 010    
        4 (Data only) 100   
        6 (All network on) 110
        '''
        self.driver.set_network_connection(1)
        sleep(3)

        #获取当前屏幕的截图,括号里是保存的路径(当前路径下的photos文件夹下，文件名为img.png)
        self.driver.get_screenshot_as_file('./photos/img.png')

        self.driver.set_network_connection(4)
        sleep(3)

        #结束录屏
        self.driver.stop_recording_screen()
