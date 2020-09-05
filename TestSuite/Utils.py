def find_and_click(css_selector, driver):
    element = driver.find_element_by_css_selector(css_selector)
    element.click()


def input_text(css_selector, driver, text):
    element = driver.find_element_by_css_selector(css_selector)
    element.send_keys(text)



