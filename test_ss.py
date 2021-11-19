from appium import webdriver
from selenium.webdriver.common.by import By

# 今日头条app测试
desired_cap = {
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.ss.android.article.news",
  "appActivity": ".activity.MainActivity",
  #第一次点击app后，将后台更新的按钮关掉，然后将 "noRest"设置为 True，意思是：不要对后台的更新进行初始化，保持为不更新的状态
  "noRest": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
driver.implicitly_wait(10)

el3 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="小视频"]').click()