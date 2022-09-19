import pytest

from page_objects.page import MainPage


@pytest.fixture(scope='function')
def page(driver):
    page = MainPage(driver)

    page.open()

    return page
