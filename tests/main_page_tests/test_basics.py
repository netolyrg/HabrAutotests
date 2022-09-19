def test_main_page_articles(page):
    assert page.count_articles_number() == 20


def test_main_page_pages_number(page):
    assert page.count_pages_number() == 50


def test_search_page_from_main(page):
    page = page.click_search()

    assert page.is_page_shown()


def test_click_external_service(page):
    page.click_services_dropdown()

    page.click_external_service(page.CAREER)

    driver = page.webdriver
    tabs = driver.window_handles
    current_tab = driver.current_window_handle
    new_index = tabs.index(current_tab) + 1
    driver.switch_to.window(tabs[new_index])

    actual = page.current_url
    expected = 'https://career.habr.com/'

    assert actual == expected


def test_list_of_other_services(page):
    page.click_services_dropdown()

    actual = len(page.services)
    expected = 4

    assert actual == expected
