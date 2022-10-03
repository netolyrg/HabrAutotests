import pytest


@pytest.fixture(scope='function')
def feedback_page(driver):
    page = FeedbackPage(driver)

    page.open()

    return page
