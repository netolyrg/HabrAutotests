from page_objects.page import *


def test_empty_search(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    page.search('asdfasdfasdfasdf')

    assert page.count_articles_number() == 0

    assert len(page.get_empty_page_text()) > 0
