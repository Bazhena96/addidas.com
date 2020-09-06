from selenium.webdriver.common.keys import Keys


def find_and_click(driver, css_selector):
    element = driver.find_element_by_css_selector(css_selector)
    element.click()


def input_text(driver, css_selector, text):
    element = driver.find_element_by_css_selector(css_selector)
    element.send_keys(text)


def input_and_click_enter(driver, css_selector, text):
    element = driver.find_element_by_css_selector(css_selector)
    element.send_keys(text)
    element.send_keys(Keys.ENTER)