import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 设置浏览器不关闭
options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)
edge = webdriver.Edge(options=options)

edge.get("https://baidu.com/")
# time.sleep(2)
# db = edge.find_element(By.XPATH, '//*[@id="header"]/div/div/img')
# db.screenshot('1.png')
# target = edge.find_element(By.XPATH, '//*[@id="baidu_translate_input"]')
# ActionChains(edge).drag_and_drop(db, target).perform()
time.sleep(1)
edge.find_element(By.LINK_TEXT, '新闻').click()
edge.find_element(By.LINK_TEXT, 'hao123').click()
time.sleep(1)
handles = edge.window_handles
print(handles)
print(edge.current_window_handle)
edge.switch_to.window(handles[2])
print(edge.current_window_handle)

edge.close()
print(handles)
print(edge.window_handles)

edge.quit()