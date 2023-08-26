from selenium.webdriver.common.by import By
from pages.Base_Page import BasePage


class DynamicLoadingPage(BasePage):

    URL = "https://the-internet.herokuapp.com/dynamic_loading"
    EXAMPLE_1 = (By.XPATH, '//a[@href = "/dynamic_loading/1"]')
    EXAMPLE_2 = (By.XPATH, '//a[@href = "/dynamic_loading/2"]')
    BUTTON_START = (By.XPATH, '//button')
    TEXT_LOADING = (By.XPATH, '//div[@id="loading"]')
    IMAGE_LOADING = (By.XPATH, '//img[@src="/img/ajax-loader.gif"]')
    FINISH_TEXT = (By.XPATH, '//div[@id="finish"]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_example_1(self):
        self.browser.find_element(*self.EXAMPLE_1).click()

    def click_example_2(self):
        self.browser.find_element(*self.EXAMPLE_2).click()

    def click_start_button(self):
        self.browser.find_element(*self.BUTTON_START).click()

    def is_text_loading_displayed(self):
        return self.wait_for_element_to_disappear(self.TEXT_LOADING)

    def get_loading_text(self):
        return self.browser.find_element(*self.TEXT_LOADING).text

    def is_loading_image_displayed(self):
        return self.wait_for_element_to_disappear(self.IMAGE_LOADING)

    def is_finish_text_displayed(self):
        return self.wait_for_element_to_be_displayed(self.FINISH_TEXT)

    def get_finish_text(self):
        return self.wait_for_element_to_be_displayed(self.FINISH_TEXT).text


    def get_url(self):
        new_url = self.browser.current_url
        return new_url





