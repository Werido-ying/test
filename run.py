from selenium import webdriver
from Python_class import method
from test_data import data
driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = data.url["url"]
name = data.login_data["username"]
pwd = data.login_data["password"]
value = data.in_value["in_value"]
result = method.opera(driver,url,name,pwd,value)
if "9255" in result:
    print("验证成功，结果正确")
else:
    print("结果错误，不通过")