from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import *
from page_objects.base_page import HabrBase


class FeedbackPage(HabrBase):
    url = 'https://habr.com/ru/feedback/'

    @property
    def submit_button(self):
        return self.webdriver.find_element(*submit_button)

    @property
    def email_error_message(self):
        return self.webdriver.find_element(*email_error)

    @property
    def message_error_message(self):
        return self.webdriver.find_element(*message_error)

    @property
    def personal_agreement_error_message(self):
        return self.webdriver.find_element(*agreement_error)

    @property
    def subject(self):
        return Select(self.webdriver.find_element(*subject))

    def count_subjects(self):
        elements = self.subject.options

        return len(elements)

    def change_subject_by_index(self, index=1):
        self.subject.select_by_index(index)

    def wait_full_page(self):
        wait = WebDriverWait(self.webdriver, 5)

        wait.until(
            presence_of_all_elements_located(subject)
        )
