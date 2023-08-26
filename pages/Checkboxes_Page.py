from selenium.webdriver.common.by import By


class CheckboxesPage:

    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOX1 = (By.XPATH, '//input[1]')
    CHECKBOX2 = (By.XPATH, '//input[2]')
    CHECKBOX1CLICKED = (By.XPATH, '//input[1][@checked]')
    CHECKBOX2CLICKED = (By.XPATH, '//input[2][@checked]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_checkbox1(self):
        self.browser.find_element(*self.CHECKBOX1).click()

    def click_checkbox2(self):
        self.browser.find_element(*self.CHECKBOX2).click()

    def is_checkbox1_clicked(self):
        return self.browser.find_element(*self.CHECKBOX1CLICKED).is_displayed()

    def is_checkbox2_clicked(self):
        return self.browser.find_element(*self.CHECKBOX2CLICKED).is_displayed()










