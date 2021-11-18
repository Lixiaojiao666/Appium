from appium import webdriver

# desired_caps是字典型的对象，里面有一些连接需要的参数
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='com.xueqiu.android.common.MainActivity'
#创建和server的连接，传入desired_caps
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.quit()