from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class AddToCart(unittest.TestCase):
    def SetUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)  # seconds
        self.driver.maximize_window()
        # navigate to the home page
        self.driver.get("https://www.adidas.com")

    def test_add_product_to_cart(self):
        self.driver = webdriver.Firefox()
        # add text into search box
        input_field = self.driver.find_element_by_css_selector(".searchinput-wrapper___18TsX > form:nth-child(2)")
        input_field.send_keys("short")
        input_field.send_keys(Keys.ENTER)
        titles = self.driver.find_elements_by_class_name("gl-product-card__details-main")
        for title in titles:
            assert "short" in title.text()
        # open product link
        product_link = self.driver.find_element_by_css_selector("div.grid-item___3rAkS:nth-child(1) > div:nth-child("
                                                                "1) > div:nth-child(1) > div:nth-child(1) > "
                                                                "div:nth-child(1)")
        product_link.send_keys(Keys.ENTER)
        # close alert
        close_alert = self.driver.find_element_by_css_selector(".gl-modal__close > svg:nth-child(1)")
        close_alert.click()
        # choose size
        choose_size = self.driver.find_element_by_css_selector("button.size___TqqSo:nth-child(1)")
        choose_size.click()
        # click add to card
        add_to_cart = self.driver.find_element_by_css_selector(".add-to-bag___3wgQk > button:nth-child(1)")
        add_to_cart.click()
        # check the product cart and verify that product are added
        check_cart = self.driver.find_element_by_css_selector("a.gl-cta:nth-child(7)")
        check_cart.submit()
        check_cart.click()

    def TearDown(self):
        self.driver = webdriver.Firefox()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

