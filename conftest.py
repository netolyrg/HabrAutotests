import time

import pytest

from selenium.webdriver.chrome import webdriver


def setup():
    print('set up')
    driver = webdriver.WebDriver(executable_path='./chromedriver')

    driver.get('https://habr.com')

    time.sleep(1)

    return driver


def tear_down(driver):
    print('tear down')
    driver.quit()


@pytest.fixture
def driver():
    obj = setup()

    yield obj

    tear_down(obj)
