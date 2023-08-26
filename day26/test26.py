import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://www.baidu.com"
edge = None


@pytest.fixture(scope="class", autouse=True)
def get_driver():
    print('setup class')
    global edge
    edge = webdriver.Edge()
    yield
    print('teardown class')
    edge.quit()


@pytest.fixture(scope="function", autouse=True)
def get_page(request):
    print('setup')
    edge.get(url)
    time.sleep(1)



class TestBaidu:
    @pytest.mark.parametrize("data", [111, 222, 333], ids=['第一个','第二个','第三个'])
    def test_send(self, data):
        edge.find_element(By.ID, "kw").send_keys(data)
        time.sleep(2)
        edge.find_element(By.ID, "su").click()
        time.sleep(2)

    @pytest.mark.parametrize("data", ['新闻', 'hao123', '地图'], ids=['第四个','第五个','第六个'])
    def test_send2(self, data):
        edge.find_element(By.LINK_TEXT, data).click()
        time.sleep(2)


if __name__ == '__main__':
    pytest.main(["test26.py", "-s"])
