from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BUTTON = (By.ID, '//*[@id="login"]/button/i')
    LOG_OUT = (By.XPATH, '//i[@class="icon-2x icon-signout"]')
    INVALID_PASSWORD = (By.ID, "flash-messages")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def type_username(self):
        self.browser.find_element(*self.USERNAME).send_keys("tomsmith")

    def type_password(self):
        self.browser.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")

    def click_button(self):
        self.browser.find_element(*self.BUTTON).click()

    def click_logout(self):
        self.browser.find_element(*self.LOG_OUT).click()

    def is_logout_button_displayed(self):
        return self.browser.find_element(*self.LOG_OUT).is_displayed()

    def wrong_password(self):
        self.browser.find_element(*self.USERNAME).send_keys("tomsmith")
        self.browser.find_element(*self.PASSWORD).send_keys("wrong_password")
        self.browser.find_element(*self.PASSWORD).send_keys(Keys.TAB)
        self.browser.find_element(*self.PASSWORD).send_keys(Keys.ENTER)

    def is_invalid_login_displayed(self):
        return self.browser.find_element(*self.INVALID_PASSWORD).is_displayed()

    def get_invalid_message(self):
        return self.browser.find_element(*self.INVALID_PASSWORD).text

    def wrong_username(self):
        self.browser.find_element(*self.USERNAME).send_keys("Test123")
        self.browser.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        self.browser.find_element(*self.PASSWORD).send_keys(Keys.TAB)
        self.browser.find_element(*self.PASSWORD).send_keys(Keys.ENTER)

    def alternative_login_button(self):
        self.browser.find_element(*self.USERNAME).send_keys("tomsmith")
        self.browser.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        self.browser.find_element(*self.PASSWORD).send_keys(Keys.TAB)
        self.browser.find_element(*self.PASSWORD).send_keys(Keys.ENTER)






