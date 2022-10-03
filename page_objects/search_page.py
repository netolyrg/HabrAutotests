from selenium.webdriver.support.expected_conditions import any_of, presence_of_element_located, \
    visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import search_input_locator, search_icon_locator, article_locator, empty_res_locator
from page_objects.base_page import HabrBase


class SearchPage(HabrBase):
    url = 'https://habr.com/ru/search'

    @property
    def search_input(self):
        return self.webdriver.find_element(*search_input_locator)

    @property
    def search_button(self):
        return self.webdriver.find_element(*search_icon_locator)

    def search(self, search_text):
        self.search_input.send_keys(search_text)
        self.search_button.click()

        self.wait_results_or_empty()

    def wait_results_or_empty(self):
        # нужно ждать либо хотя бы одну статью, либо текст "результатов нет"
        wait = WebDriverWait(self.webdriver, 2, poll_frequency=0.1)
        wait.until(
            any_of(
                presence_of_element_located(article_locator),
                presence_of_element_located(empty_res_locator)
            ))

    @property
    def empty_result_banner(self):
        return self.webdriver.find_element(*empty_res_locator)

    def get_empty_page_text(self):
        return self.empty_result_banner.text

    def wait_full_page(self):
        wait = WebDriverWait(self.webdriver, 5)

        wait.until(
            visibility_of_element_located(search_input_locator)
        )

    def open(self):
        super().open()
        self.wait_full_page()

    def is_page_shown(self):
        return self.search_input.is_displayed()