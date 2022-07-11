from selenium.webdriver.chrome import webdriver
import time

driver = webdriver.WebDriver(executable_path='./chromedriver')

driver.get('https://habr.com')

time.sleep(5)

driver.quit()
