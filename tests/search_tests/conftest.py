import pytest

from page_objects.page import SearchPage


@pytest.fixture(scope='function')
def page(driver):
    page = SearchPage(driver)

    page.open()

    return page
