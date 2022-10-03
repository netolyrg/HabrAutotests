from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import search_button_locator, services_dropdown_element, article_locator, \
    services_dropdown_button
from page_objects.base_page import HabrBase
from page_objects.search_page import SearchPage


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

    def click_services_dropdown(self):
        element = self.webdriver.find_element(*services_dropdown_button)
        element.click()

    def click_external_service(self, service_index):
        assert service_index in (self.HABR, self.QNA, self.CAREER, self.FL)

        service_pages_map = {
            self.HABR: MainPage,
            self.QNA: QNAPage,
            self.CAREER: CareerPage,
            self.FL: FLPage,
        }

        element = self.services[service_index]
        element.click()

        self.focus_on_new_tab()

        page_class = service_pages_map.get(service_index)

        return page_class(self.webdriver)


class CareerPage(HabrBase):
    url = 'https://career.habr.com/'


class QNAPage(HabrBase):
    url = 'https://qna.habr.com/'


class FLPage(HabrBase):
    url = 'https://freelance.habr.com/'