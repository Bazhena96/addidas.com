from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

from TestSuite.Utils import find_and_click, input_and_click, input_text

class LogIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds
        # navigate to the home page
        self.driver.get("https://www.adidas.com")

    def

