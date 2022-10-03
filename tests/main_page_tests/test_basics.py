def test_main_page_articles(page):
    assert page.count_articles_number() == 20


def test_main_page_pages_number(page):
    assert page.count_pages_number() == 50


def test_search_page_from_main(page):
    page = page.click_search()

    assert page.is_page_shown()


def test_click_external_service(page):
    page.click_services_dropdown()

    page = page.click_external_service(page.QNA)

    actual = page.current_url
    expected = page.url

    assert actual == expected


def test_list_of_other_services(page):
    page.click_services_dropdown()

    actual = len(page.services)
    expected = 4

    assert actual == expected
