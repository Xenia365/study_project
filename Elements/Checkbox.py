from Browser.driver import WebDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from Logger import logger
from config import PAGE_LOAD_TIMEOUT, SCRIPT_TIMEOUT, IMPLICITLY_WAIT, EXPLICITLY_WAIT
from selenium.webdriver.common.by import By
import Browser
from Base_element import BaseElement


class Checkbox(BaseElement):

    def __init__(self, locator, condition):
        super().__init__(locator, condition)

    def select_all(self):
        Checkbox.find_elements(self).to_click_all()

    def select_one(self):
        Checkbox.find_element(self).to_click()


