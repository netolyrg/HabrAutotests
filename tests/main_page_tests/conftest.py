import pytest

from page_objects.main_page import MainPage


@pytest.fixture(scope='function')
def page(driver):
    page = MainPage(driver)

    page.open()

    yield page

    tabs = page.webdriver.window_handles
    if len(tabs) > 1:
        for tab in tabs[:0:-1]:
            driver.switch_to.window(tab)
            driver.close()

    driver.switch_to.window(tabs[0])
