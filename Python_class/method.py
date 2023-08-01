import time
from selenium.webdriver.common.by import By
#封装打开网页方法
def open_site(driver,url):
    driver.maximize_window()
    driver.get(url)
#封装登录
def login(driver,username,password):
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"btnSubmit").click()
#封装搜索
def opera(driver,url,username,password,in_value):
    open_site(driver,url)
    login(driver,username,password)
    driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
    father_id = driver.find_element(By.XPATH,"//li[@class='active']").get_attribute("id")
    frame_id = father_id + "-frame"
    driver.switch_to.frame(frame_id)
    driver.find_element(By.XPATH,"//input[@id='searchNumber']").send_keys(in_value)
    driver.find_element(By.XPATH,"//span[@class='l-btn-text icon-search l-btn-icon-left']").click()
    time.sleep(2)
    num = driver.find_element(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text
    return num
