def test_main_page_articles(page):
    assert page.count_articles_number() == 20


def test_main_page_pages_number(page):
    assert page.count_pages_number() == 50


def test_search_page_from_main(page):
    page = page.click_search()

    assert page.is_page_shown()
