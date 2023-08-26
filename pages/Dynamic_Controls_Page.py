from selenium.webdriver.common.by import By
from pages.Base_Page import BasePage


class DynamicControlsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_controls"
    ADD_REMOVE_BUTTON = (By.XPATH, '//button[@onclick = "swapCheckbox()"]')
    ENABLE_DISABLE_BUTTON = (By.XPATH, '//button[@onclick = "swapInput()"]')
    CHECK_BOX = (By.XPATH, '//input[@type="checkbox"]')
    MESSAGE_CLICK = (By.XPATH, '//*[@id="message"]')
    LOADING_MESSAGE = (By.XPATH, '//*[@id="loading"]')
    IMAGE_LOADING = (By.XPATH, '//*[@id="loading"]/img')
    INPUT_TEXT = (By.XPATH, '//input[@type = "text"]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def is_add_remove_button_displayed(self):
        return self.browser.find_element(*self.ADD_REMOVE_BUTTON).is_displayed()

    def is_enable_disable_button_displayed(self):
        return self.browser.find_element(*self.ENABLE_DISABLE_BUTTON).is_displayed()

    def is_checkbox_displayed(self):
        return self.browser.find_element(*self.CHECK_BOX).is_displayed()

    def click_add_remove_button(self):
        self.browser.find_element(*self.ADD_REMOVE_BUTTON).click()

    def click_enable_disable_button(self):
        self.browser.find_element(*self.ENABLE_DISABLE_BUTTON).click()

    def is_loading_message_displayed(self):
        return self.browser.find_element(*self.LOADING_MESSAGE).is_displayed()

    def is_image_displayed(self):
        return self.wait_for_element_to_be_displayed(self.IMAGE_LOADING).is_displayed()

    def is_wait_message_displyaed(self):
        return self.browser.find_element(*self.MESSAGE_CLICK).is_displayed()

    def input_text(self):
        self.browser.find_element(*self.INPUT_TEXT).send_keys("Test123")

    def get_loading_message(self):
        return self.browser.find_element(*self.LOADING_MESSAGE).text

    def get_wait_message(self):
        return self.browser.find_element(*self.MESSAGE_CLICK).text

    def is_message_click_displayed(self):
        return self.wait_for_element_to_be_displayed(self.MESSAGE_CLICK).is_displayed()








