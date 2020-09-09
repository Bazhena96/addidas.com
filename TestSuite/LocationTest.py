from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.common.exceptions import NoSuchElementException


from TestSuite.Utils import find_and_click


class ChangeLocation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds
        # navigate to the home page
        self.driver.get("https://www.adidas.com")

    def test_change_location(self):
        find_and_click(self.driver, ".country_selector_text___yovMX")
        find_and_click(self.driver, "#europe")
        # change location to Poland
        find_and_click(self.driver, "div.country-group:nth-child(4) > ul:nth-child(3) > li:nth-child(3) > a:nth-child(1)")
        try:
            text = self.driver.find_element_by_id("POBIERZ, ZAREJESTRUJ SIĘ, WEŹ UDZIAŁ")
            return True
        except NoSuchElementException:
            print('Zero element')
            return False

    def tearDown(self):
        self.driver.quit()
