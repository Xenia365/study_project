from driver import WebDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from Logger import logger
from config import PAGE_LOAD_TIMEOUT, SCRIPT_TIMEOUT, IMPLICITLY_WAIT, BASE_URL


class Browser:

    driver = None

    @staticmethod
    def get_driver():
        Browser.driver = WebDriverManager.new_driver()
        logger.info('Got driver')

    @staticmethod
    def refresh_page():
        Browser.driver.navigate().refresh()
        logger.info('Page refreshed')

    @staticmethod
    def close():
        Browser.driver.close()
        logger.info('Page closed')

    @staticmethod
    def quit():
        Browser.driver.quit()
        logger.info('Browser closed')

    @staticmethod
    def go_to_page(URL):
        Browser.driver.navigate.to(URL)
        logger.info('Open another page')

    @staticmethod
    def forward():
        Browser.driver.navigate().forward()
        logger.info('Forward')

    @staticmethod
    def back():
        Browser.driver.navigate().back()
        logger.info('Back')

    @staticmethod
    def do_script(script):
        Browser.driver.execute_script(script)
        logger.info('Run script')

    @staticmethod
    def switch_to_frame(frame):
        Browser.driver.switch_to.frame(Browser.driver.frame)
        logger.info('Switch to frame')

    @staticmethod
    def switch_to_content():
        Browser.driver.switch_to.default_content()
        logger.info('Switch to content')

    @staticmethod
    def configurate():
        Browser.driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        Browser.driver.set_script_timeout(SCRIPT_TIMEOUT)
        Browser.driver.implicitly_wait(IMPLICITLY_WAIT)
        logger.info('Configurated')


