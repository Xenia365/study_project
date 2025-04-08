from selenium.webdriver.support.expected_conditions import presence_of_element_located

from Browser.driver import WebDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from Logger import logger
from config import PAGE_LOAD_TIMEOUT, SCRIPT_TIMEOUT, IMPLICITLY_WAIT, EXPLICITLY_WAIT
from selenium.webdriver.common.by import By
from Browser.browser import Browser


class BaseElement:

    driver = None

    def __init__(self, locator, condition):
        self.locator = locator
        self.condition = condition
        self.element = None

    @staticmethod
    def take_driver():
        BaseElement.driver = Browser.driver

    def find_element(self):
        self.element = WebDriverWait(BaseElement.driver, EXPLICITLY_WAIT).until(EC.presence_of_element_located((self.condition, self.locator)))
        return self.element

    def find_elements(self):
        self.element = WebDriverWait(BaseElement.driver, EXPLICITLY_WAIT).until(EC.presence_of_all_elements_located((self.condition, self.locator)))
        return self.element

    def to_click_all(self):
        for element in self.element:
            element.click()

    def to_click(self):
        self.element.click()

    def send_keys(self, key):
        self.element.send_keys(key)

    def submit(self):
        self.element.submit()

