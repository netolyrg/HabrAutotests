import pytest

from page_objects.search_page import SearchPage


@pytest.fixture(scope='function')
def page(driver):
    page = SearchPage(driver)

    page.open()

    return page
