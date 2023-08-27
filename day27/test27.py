import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.testcase("baidu")
@allure.feature("搜索")
@pytest.mark.parametrize("data", ['a', 'b', 'c'])
def test01(data):
    with allure.step("打开网页"):
        driver = webdriver.Edge()
        driver.get("http://www.baidu.com")
        driver.maximize_window()
        time.sleep(1)
    with allure.step(f'搜索{data}'):
        driver.find_element(By.ID,"kw").send_keys(data)
        time.sleep(1)
        driver.find_element(By.ID, 'su').click()
        time.sleep(1)
    with allure.step("保存图片"):
        filename = 'test' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.png'
        driver.save_screenshot(filename)
        allure.attach.file(filename, attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()
