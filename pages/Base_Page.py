from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __int__(self, browser):
        self.browser = browser

    def wait_for_element_to_be_displayed(self, locator):
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        return element

    def wait_for_element_to_disappear(self, locator):
        element = WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(locator))
        return element


