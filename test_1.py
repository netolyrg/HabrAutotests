from page import *


def test_basic_search(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    page.search('Selenium')

    assert page.count_articles_number() == 20
    assert page.count_pages_number() == 50
