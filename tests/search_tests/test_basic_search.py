from page_objects.page import *


def test_articles_number_on_page(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    page.search('Selenium')

    assert page.count_articles_number() == 20


def test_pages_number_on_page(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    page.search('Selenium')

    assert page.count_pages_number() == 50
