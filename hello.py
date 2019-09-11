# 导包
from time import sleep

from selenium import webdriver

# 创建浏览器对象
driver = webdriver.Chrome()
# 打开网页
driver.get("http://www.baidu.com/")
# 窗口最大化
driver.maximize_window()
sleep(3)
# 关闭浏览器
driver.quit()
