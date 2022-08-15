from selenium.webdriver.common.by import By

last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
article_locator = By.TAG_NAME, 'article'
search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
search_button_locator = By.XPATH, '//*[@data-test-id="search-button"]'
empty_res_locator = By.XPATH, '//*[@data-test-id="empty-placeholder-text"]'
