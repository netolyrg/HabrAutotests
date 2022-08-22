from page import *


def test_main_page(driver):
    page = MainPage(driver)
    page.open()

    assert page.count_articles_number() == 19
    assert page.count_pages_number() == 50
