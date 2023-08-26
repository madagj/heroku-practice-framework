from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DragAndDropPage:

    A_COLUMN = (By.ID, "column-a")
    B_COLUMN = (By.ID, "column-b")
    URL = "https://the-internet.herokuapp.com/drag_and_drop"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def is_a_column_displayed(self):
        return self.browser.find_element(*self.A_COLUMN).is_displayed()

    def is_b_column_displayed(self):
        return self.browser.find_element(*self.B_COLUMN).is_displayed()

    def column_a_move_to_b(self):
        action = ActionChains(self.browser)
        source = self.browser.find_element(*self.A_COLUMN)
        target = self.browser.find_element(*self.B_COLUMN)
        action.drag_and_drop(source, target).perform()
        #action.click_and_hold(source).move_to_element(target).perform()

    def is_column_a_moved_to_column_b(self):
        action = ActionChains(self.browser)
        source = self.browser.find_element(*self.A_COLUMN)
        target = self.browser.find_element(*self.B_COLUMN)
        return action.drag_and_drop(source, target).perform()
        # action.click_and_hold(source).move_to_element(target).perform()
        # return action.click_and_hold(source).move_to_element(target).perform()







