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
        input_and_click(self.driver, ".searchinput___zXLAR", "short")
        # open product link
        open_link = self.driver.find_element_by_css_selector("div.grid-item___3rAkS:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        open_link.send_keys(Keys.ENTER)
        # close alert
        find_and_click(self.driver, ".gl-modal__close > svg:nth-child(1)")
        # choose size
        find_and_click(self.driver, "button.size___TqqSo:nth-child(1)")
        # click add to card
        find_and_click(self.driver, ".add-to-bag___3wgQk > button:nth-child(1)")
        # check the product cart and verify that product are added
        find_and_click(self.driver, "a.gl-cta:nth-child(7)")

    def test_set_remainder(self):
        # click the release date button
        find_and_click(self.driver, "div.glass-navigation-flyout-white___20EjX:nth-child(8) > a:nth-child(1)")
        # close alert
        find_and_click(self.driver, ".gl-modal__close > svg:nth-child(1)")
        # choose the product to set the remainder
        find_and_click(self.driver, "div.plc-product-card___1kN_6:nth-child(2) > div:nth-child(1) > a:nth-child(1)")
        # set a remainder
        find_and_click(self.driver, ".ctaButtonContainer___3a_3R > button:nth-child(1)")
        # add to calendar and choose the date
        find_and_click(self.driver, ".gl-cta--secondary")
        find_and_click(self.driver, "a.gl-cta--secondary:nth-child(1)")

    def test_check_order(self):
        # click "check the order"
        find_and_click(self.driver, ".inner___1T3DW > a:nth-child(6)")
        # input data
        input_text(self.driver, "div.field___22seD:nth-child(2) > input:nth-child(1)", "AD012345678")
        input_text(self.driver, "div.field___22seD:nth-child(3) > input:nth-child(1)", "bazhenkak@gmail.com")
        # find order
        find_and_click(self.driver, "button.gl-cta:nth-child(4)")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
