import gmail as gmail
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest

from TestSuite.Utils import find_and_click, input_text, input_and_click_enter

correctLoginIncorrectPassword = {"login": "bazhenkak@gmail.com", "password": 5645677,
                                 "error_message": "Incorrect email/password – please check and retry"}
incorrectLoginCorrectPassword = {"login": "gogogogo@gmail.com", "password": 7789938,
                                 "error_message": "Incorrect email/password – please check and retry"}
incorrectLoginIncorrectPassword = {'login': "goofojir@gmail.com", "password": 333333,
                                   "error_message": "Incorrect email / password – please check and retry"}

scenarios = (correctLoginIncorrectPassword, incorrectLoginCorrectPassword, incorrectLoginIncorrectPassword)


class InvalidLoginScenarios(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds
        # navigate to the home page
        self.driver.get("https://www.adidas.com")

    def test_login_scenario(self):
        for scenario in scenarios:
            find_and_click(self.driver, ".inner___1T3DW > a:nth-child(12)")
            email = self.driver.find_element_by_css_selector("#login-email").clear()
            input_text(self.driver, "#login-email", scenario['login'])
            password = self.driver.find_element_by_css_selector('#login-password').clear()
            input_text(self.driver, "#login-password", scenario['password'])
            find_and_click(self.driver, "div.gl-vspace-bpall-small:nth-child(6) > button:nth-child(1)")
            self.assertIn(scenario['error_message'], self.driver.page_source)

    def tearDown(self):
        self.driver.quit()
