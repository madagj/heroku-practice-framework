from selenium.webdriver.common.by import By


class DynamicContentPage:

    URL= "https://the-internet.herokuapp.com/dynamic_content?with_content=static"
    CLICK_BUTTON = (By.XPATH, '//a[@href="/dynamic_content?with_content=static"]')
    MESSAGE = (By.XPATH, '//*[@id="content"]/div[3]/div[2]')

    def __init__(self,browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_button(self):
        self.browser.find_element(*self.CLICK_BUTTON).click()

    def get_message_text(self):
        return self.browser.find_element(*self.MESSAGE).text

