from selenium.webdriver.remote.webdriver import WebDriver

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
