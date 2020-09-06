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

    def test_log_in(self):
        find_and_click(self.driver, ".inner___1T3DW > a:nth-child(12)")
        input_text(self.driver, "#login-email", "bazhenkak@gmail.com")
        input_text(self.driver, "#login-password", "change1313")
        find_and_click(self.driver, "div.gl-vspace-bpall-small:nth-child(6) > button:nth-child(1)")

    def test_forgot_password(self):
        find_and_click(self.driver, ".inner___1T3DW > a:nth-child(12)")
        find_and_click(self.driver, "div.col-l-10:nth-child(1) > form:nth-child(2) > a:nth-child(1)")
        input_text(self.driver, ".field__input___3eT4b", "bazhenkak@gmail.com")
        find_and_click(self.driver, "div.gl-vspace-bpall-medium:nth-child(1) > button:nth-child(1)")

    def test_join_club(self):
        find_and_click(self.driver, ".inner___1T3DW > div:nth-child(8) > em:nth-child(1) > a:nth-child(1)")
        input_text(self.driver, "#registration-email-field", "bazhenkak@gmail.com")
        input_text(self.driver, "#registration-password-field", "change1313")
        find_and_click(self.driver, ".gl-form-item--inline")
        find_and_click(self.driver, "button.gl-cta:nth-child(8)")

    def tearDown(self):
        self.driver.quit()









