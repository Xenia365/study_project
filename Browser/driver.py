from selenium import webdriver
from config import BROWSER

class WebDriverManager:

    driver = None

    @staticmethod
    def new_driver():
        if BROWSER == 'chrome':
            driver = webdriver.Chrome()
            driver.maximize_window()
            return driver