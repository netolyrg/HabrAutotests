import pytest

from selenium.webdriver.chrome import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options


def setup():
    lang = 'ru'

    options = Options()
    options.add_argument(f'--lang={lang}')
    options.add_experimental_option('prefs', {'intl.accept_languages': f'{lang}'})

    service = Service(
        executable_path='./chromedriver'
    )

    driver = webdriver.WebDriver(service=service, options=options)

    return driver


def tear_down(driver):
    driver.quit()


@pytest.fixture
def driver():
    obj = setup()

    yield obj

    tear_down(obj)
