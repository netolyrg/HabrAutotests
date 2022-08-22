from page import *


def test_pagination_to_last_page(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    page.search('Selenium')

    page.go_to_last_page()

    expected = 'https://habr.com/ru/search/page50/?q=Selenium&target_type=posts&order=relevance'
    actual = page.current_url

    assert actual == expected
