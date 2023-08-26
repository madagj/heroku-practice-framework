from selenium.webdriver.common.by import By

class DropdownListPage:

    URL = "https://the-internet.herokuapp.com/dropdown"
    OPTION_1 =(By.XPATH, '//option[@value="1"]')
    OPTION_2 = (By.XPATH, '//option[@value="2"]')
    DROP_DOWN = (By.ID, "dropdown")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_drop_down(self):
        self.browser.find_element(*self.DROP_DOWN).click()

    def click_option_1(self):
        self.browser.find_element(*self.OPTION_1).click()

    def click_option_2(self):
        self.browser.find_element(*self.OPTION_2).click()

    def is_option_1_displayed(self):
        return self.browser.find_element(*self.OPTION_1).is_displayed()

    def is_option_2_displayed(self):
        return self.browser.find_element(*self.OPTION_2).is_displayed()