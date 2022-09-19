from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import *


class HabrBase:
    url = 'https://habr.com'

    def __init__(self, webdriver: WebDriver):
        self.webdriver: WebDriver = webdriver

    @property
    def last_page_number(self):
        return self.webdriver.find_element(*last_page_locator)

    def count_pages_number(self):
        return int(self.last_page_number.text)

    def go_to_last_page(self):
        self.last_page_number.click()

    @property
    def articles(self):
        return self.webdriver.find_elements(*article_locator)

    def count_articles_number(self):
        return len(self.articles)

    @property
    def current_url(self):
        return self.webdriver.current_url

    def open(self):
        self.webdriver.get(self.url)

    def focus_on_new_tab(self):
        driver = self.webdriver

        tabs = driver.window_handles

        current_tab = driver.current_window_handle

        new_index = tabs.index(current_tab) + 1

        driver.switch_to.window(tabs[new_index])


class MainPage(HabrBase):
    url = 'https://habr.com'

    # services list
    HABR = 0
    QNA = 1
    CAREER = 2
    FL = 3

    @property
    def search_button(self):
        return self.webdriver.find_element(*search_button_locator)

    @property
    def services(self):
        return self.webdriver.find_elements(*services_dropdown_element)

    def click_search(self):
        self.search_button.click()

        page = SearchPage(self.webdriver)
        page.wait_full_page()

        return page

    def wait_full_page(self):
        wait = WebDriverWait(self.webdriver, 5)

        wait.until(
            presence_of_all_elements_located(article_locator)
        )

    def open(self):
        super().open()
        self.wait_full_page()

    def click_services_dropdown(self):
        element = self.webdriver.find_element(*services_dropdown_button)
        element.click()

    def click_external_service(self, service_index):
        assert service_index in (self.HABR, self.QNA, self.CAREER, self.FL)

        element = self.services[service_index]
        element.click()

        self.focus_on_new_tab()

        return CareerPage(self.webdriver)


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


class CareerPage(HabrBase):
    url = 'https://career.habr.com/'
