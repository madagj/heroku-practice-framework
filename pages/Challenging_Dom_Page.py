from selenium.webdriver.common.by import By


class ChalLengingDomPage:

    URL = "https://the-internet.herokuapp.com/challenging_dom"
    BLUE_BUTTON = (By.XPATH, '//a[@class="button"]')
    RED_BUTTON = (By.XPATH, '//a[@class="button alert"]')
    GREEN_BUTTON = (By.XPATH, '//a[@class="button success"]')
    ANSWER_MESSAGE = (By.ID, "canvas")
    GREEN_BUTTON_TEXT = (By.XPATH, '//a[@class="button success"]/text()')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_blue_button(self):
        self.browser.find_element(*self.BLUE_BUTTON).click()

    def click_red_button(self):
        self.browser.find_element(*self.RED_BUTTON).click()

    def click_green_button(self):
        self.browser.find_element(*self.GREEN_BUTTON).click()

    def is_red_button_displayed(self):
        return self.browser.find_element(*self.RED_BUTTON).is_displayed()

    def is_blue_button_displayed(self):
        return self.browser.find_element(*self.BLUE_BUTTON).is_displayed()

    def is_green_button_displayed(self):
        return self.browser.find_element(*self.GREEN_BUTTON).is_displayed()

    def is_answer_displayed(self):
        return self.browser.find_element(*self.ANSWER_MESSAGE).is_displayed()

    def get_green_button_text(self):
        return self.browser.find_element(*self.GREEN_BUTTON_TEXT).text









