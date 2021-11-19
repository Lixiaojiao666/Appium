from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".common.MainActivity",
  #第一次点击app后，将后台更新的按钮关掉，然后将 "noRest"设置为 True，
  # 意思是：不要对后台的更新进行初始化，保持为不更新的状态,不清除缓存信息
  "noRest": True,
  #首次启动的时候，不停止app,这样每次运行测试用例的时候，就不用每次都重启app
  "dontStopAppOnReset":True,
  #跳过一些初始化等前置操作
  "skipDeviceInitialization":True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
#添加隐式等待（全局性，每次find_element都会触发隐式等待）,增强测试稳定性
driver.implicitly_wait(10)
driver.find_element(By.ID,"com.xueqiu.android:id/tv_search").click()
driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text").send_keys('alibaba')

#返回上一个页面，恢复初始页面，下次再运行测试用例不会报错
driver.back()
driver.back()

driver.quit()

