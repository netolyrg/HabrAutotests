import pytest

from page_objects.feedback_page import FeedbackPage


@pytest.fixture(scope='function')
def feedback_page(driver):
    page = FeedbackPage(driver)

    page.open()

    return page
