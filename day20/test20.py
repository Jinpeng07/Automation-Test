import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 设置浏览器不关闭
options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)
edge = webdriver.Edge(options=options)

edge.get("https://www.baidu.com/")
time.sleep(2)
kw = edge.find_element(By.ID, 'kw')
kw.screenshot('1.png')
time.sleep(2)

edge.quit()