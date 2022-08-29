from page_objects.page import *


def test_main_page(driver):
    page = MainPage(driver)
    page.open()

    assert page.count_articles_number() == 20
    assert page.count_pages_number() == 50


def test_search_page_from_main(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    assert page.is_page_shown()
