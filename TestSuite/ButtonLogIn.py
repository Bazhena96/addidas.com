import gmail as gmail
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest

from TestSuite.Utils import find_and_click, input_text, input_and_click_enter


class ButtonLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds
        # navigate to the home page
        self.driver.get("https://www.adidas.com")

    def test_facebook_logIn(self):
        find_and_click(self.driver, ".inner___1T3DW > a:nth-child(12)")
        facebook_button = self.driver.find_element_by_css_selector("button.gl-cta--secondary:nth-child(1)")
        if facebook_button.is_enabled():
            facebook_button.click()
        else:
            print("button not found")

    def test_google_logIn(self):
        find_and_click(self.driver, ".inner___1T3DW > a:nth-child(12)")
        google_button = self.driver.find_element_by_css_selector("button.gl-cta:nth-child(2)")
        if google_button.is_enabled():
            google_button.click()
        else:
            print("Button not found")

    def test_yahoo_logIn(self):
        find_and_click(self.driver, ".inner___1T3DW > a:nth-child(12)")
        yahoo_button = self.driver.find_element_by_css_selector("button.gl-cta:nth-child(3)")
        if yahoo_button.is_enabled():
            yahoo_button.click()
        else:
            print("Button not found")

    def tearDown(self):
        self.driver.quit()
