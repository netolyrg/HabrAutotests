def test_empty_search(page):
    page.search('asdfasdfasdfasdf')

    assert page.count_articles_number() == 0


def test_empty_search_text(page):
    page.search('asdfasdfasdfasdf')

    assert len(page.get_empty_page_text()) > 0
