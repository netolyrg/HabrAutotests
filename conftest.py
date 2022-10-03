import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


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


@pytest.fixture(scope='session')
def session_driver():
    obj = setup()

    yield obj

    tear_down(obj)


@pytest.fixture(scope='function')
def driver(session_driver):
    yield session_driver

    tabs = session_driver.window_handles
    if len(tabs) > 1:
        for tab in tabs[:0:-1]:
            session_driver.switch_to.window(tab)
            session_driver.close()

    session_driver.switch_to.window(tabs[0])
