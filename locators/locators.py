from selenium.webdriver.common.by import By

# Common locators
last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
article_locator = By.XPATH, '//*[@data-test-id="articleTitle"]/../..'
search_button_locator = By.XPATH, '//*[@data-test-id="search-button"]'

# Main Page
services_dropdown_button = By.CLASS_NAME, 'tm-header__dropdown-toggle'
services_dropdown_element = By.CLASS_NAME, 'tm-our-projects__item'

# Search Page
search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
empty_res_locator = By.XPATH, '//*[@data-test-id="empty-placeholder-text"]'
