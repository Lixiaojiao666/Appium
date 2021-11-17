from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".common.MainActivity",
  #第一次点击app后，将后台更新的按钮关掉，然后将 "noRest"设置为 True，意思是：不要对后台的更新进行初始化，保持为不更新的状态
  "noRest": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
driver.implicitly_wait(10)
el1 = driver.find_element(By.ID,"com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element(By.ID,"com.xueqiu.android:id/action_close")
el2.click()
el3 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[2]/android.widget.ImageView")
el3.click()
el4 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[1]/android.widget.ImageView")
el4.click()
