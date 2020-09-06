from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

from TestSuite.Utils import find_and_click, input_and_click, input_text


class AddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds
        # navigate to the home page
        self.driver.get("https://www.adidas.com")

    def test_add_product(self):
        # add text into search box
        input_and_click(".searchinput___zXLAR", self.driver, "short")
        # open product link
        open_link = self.driver.find_element_by_css_selector("div.grid-item___3rAkS:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        open_link.send_keys(Keys.ENTER)
        # close alert
        find_and_click(".gl-modal__close > svg:nth-child(1)", self.driver)
        # choose size
        find_and_click("button.size___TqqSo:nth-child(1)", self.driver)
        # click add to card
        find_and_click(".add-to-bag___3wgQk > button:nth-child(1)", self.driver)
        # check the product cart and verify that product are added
        find_and_click("a.gl-cta:nth-child(7)", self.driver)

    def test_set_remainder(self):
        # click the release date button
        find_and_click("div.glass-navigation-flyout-white___20EjX:nth-child(8) > a:nth-child(1)", self.driver)
        # close alert
        find_and_click(".gl-modal__close > svg:nth-child(1)", self.driver)
        # choose the product to set the remainder
        find_and_click("div.plc-product-card___1kN_6:nth-child(2) > div:nth-child(1) > a:nth-child(1)", self.driver)
        # set a remainder
        find_and_click(".ctaButtonContainer___3a_3R > button:nth-child(1)", self.driver)
        # add to calendar and choose the date
        find_and_click(".gl-cta--secondary", self.driver)
        find_and_click("a.gl-cta--secondary:nth-child(1)", self.driver)

    def test_check_order(self):
        # click "check the order"
        find_and_click(".inner___1T3DW > a:nth-child(6)", self.driver)
        # input data
        input_text("div.field___22seD:nth-child(2) > input:nth-child(1)", self.driver, "AD012345678")
        input_text("div.field___22seD:nth-child(3) > input:nth-child(1)", self.driver, "bazhenkak@gmail.com")
        # find order
        find_and_click("button.gl-cta:nth-child(4)", self.driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
