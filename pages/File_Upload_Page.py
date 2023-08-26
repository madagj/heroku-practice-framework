from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from pages.Base_Page import BasePage


class FileUploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"
    DRAG_BUTTON = (By.XPATH, '//div[@id="drag-drop-upload"]')
    UPLOAD_BUTTON = (By.XPATH, '//input[@id="file-submit"]')
    FILE_UPLOAD_MESSAGE = (By.XPATH, 'h3')
    FILE_NAME_MESSAGE = (By.XPATH, '//div[@id="uploaded-files"]')
    UPLOAD_FILES_NAME = (By.XPATH, '//div[@id="uploaded-files"]')
    CHOOSE_FILE_BUTTON = (By.NAME, 'file')
    ERROR_MESSAGE = (By.XPATH, '/html/body/h1')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_drag_file(self):
        self.browser.find_element(*self.DRAG_BUTTON).click()

    def click_choose_file(self):
        #self.browser.find_element(*self.CHOOSE_FILE_BUTTON).click()
        self.wait_for_element_to_be_displayed(self.CHOOSE_FILE_BUTTON).click()

    def click_upload_button(self):
        self.browser.find_element(*self.UPLOAD_BUTTON).click()

    def is_file_upload_message_displayed(self):
        return self.browser.find_element(*self.FILE_UPLOAD_MESSAGE).is_displayed()

    def get_file_upload_message(self):
        return self.browser.find_element(*self.FILE_UPLOAD_MESSAGE).text

    def get_name_of_file(self):
        return self.browser.find_element(*self.UPLOAD_FILES_NAME).text

    def get_error_message(self):
        return self.browser.find_element(*self.ERROR_MESSAGE).text

    def is_error_message_displayed(self):
        return self.browser.find_element(*self.ERROR_MESSAGE).is_displayed()

    def use_file(self):
        Keyboard = Controller()
        Keyboard.type("C:\\Users\\ceafa\\Downloads\\Example.txt")
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)





