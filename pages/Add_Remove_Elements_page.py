from selenium.webdriver.common.by import By
from pages.Base_Page import BasePage


class AddRemoveElementsPage(BasePage):

    TITLE_TEXT = (By.CSS_SELECTOR, "div h3")
    ADD_ELEMENT_BUTTON = (By.XPATH, "//*[@id='content']/div/button")
    DELETE_BUTTON = (By.XPATH, "//*[@id='elements']/button")
    URL = 'https://the-internet.herokuapp.com/add_remove_elements/'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_add_button(self):
        self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()

    def click_delete_button(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def get_title_page(self):
        return self.browser.find_element(*self.TITLE_TEXT).text()

    def is_delete_button_displayed(self):
        return self.wait_for_element_to_be_displayed(*self.DELETE_BUTTON).is_displayed()

    def get_number_of_delete_button(self):
        return len(self.browser.find_elements(*self.DELETE_BUTTON))







