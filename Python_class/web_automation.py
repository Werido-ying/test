# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# str1 = driver.capabilities['browserVersion']  # 查看chrome版本
# str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]  # 查看python下的chromedriver版本
# print(str1)
# print(str2)
import time

# from selenium import webdriver
# import time
# driver = webdriver.Chrome()      #指定浏览器，初始化driver
# driver.get("https://www.csdn.net/")     #跳转到url
# driver.maximize_window()     #最大化窗口
# time.sleep(2)
# driver.get("https://tieba.baidu.com/")
# time.sleep(2)
# driver.back()     #后退
# time.sleep(2)
# driver.forward()     #前进
# time.sleep(2)
# driver.refresh()     #刷新
# #退出
# driver.quit()
# #driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://erp.lemfix.com/login.html")
# time.sleep(1)
# text1 = driver.find_element(By.XPATH,"//div[@class='login-logo']//b").text  #xpath的层级定位
# print(text1)
# time.sleep(1)
# driver.find_element(By.ID,"username").send_keys("test123")
# # driver.find_element("id","username").send_keys("test123")
# time.sleep(1)
# driver.find_element(By.ID,"password").send_keys("123456")
# time.sleep(1)
# driver.find_element(By.ID,"btnSubmit").click()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.bilibili.com/")
# time.sleep(1)
#相对路径
# driver.find_element(By.XPATH,"//div[@class='header-login-entry']").click()

# driver.find_element(By.CLASS_NAME,"nav-search-input").send_keys("辩论精彩发言")
# driver.find_element(By.XPATH,"//div[@class='nav-search-btn']").click()

#层级定位 （上面）

#文本属性定位
# driver.find_element(By.XPATH,"//span[text()='历史']").click()
# driver.find_element(By.XPATH,"//a[text()='番剧']").click()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("http://erp.lemfix.com/login.html")
# driver.find_element(By.ID,"username").send_keys("test123")
# driver.find_element(By.ID,"password").send_keys("123456")
# driver.find_element(By.ID,"btnSubmit").click()
#
# driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
# driver.find_element(By.XPATH,"//a[@data-code=210]//span").click()
#1、通过id切换frame
# father_id = driver.find_element(By.XPATH,"//li[@class='active']").get_attribute("id")
# frame_id = father_id+"-frame"
# driver.switch_to.frame(frame_id)
#2、通过元素定位切换frame
#先定位切换目标frame
# frame_biu = driver.find_element(By.XPATH,"//iframe[@id='{}']".format(frame_id))
# driver.switch_to.frame(frame_biu)
#3、通过frame下标切换
# driver.switch_to.frame(1)

# driver.find_element(By.XPATH,"//input[@id='searchNumber']").send_keys("9255")
# driver.find_element(By.XPATH,"//span[@class='l-btn-text icon-search l-btn-icon-left']").click()
# time.sleep(1)
#层级定位
# num = driver.find_element(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text
# print(num)
# if "9255" in num:
#     print("验证通过")
# else:
#     print("内容不一致")