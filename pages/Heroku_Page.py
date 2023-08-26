from selenium.webdriver.common.by import By
from pages.Add_Remove_Elements_page import AddRemoveElementsPage
from pages.Challenging_Dom_Page import ChalLengingDomPage
from pages.Checkboxes_Page import CheckboxesPage
from pages.Drag_And_Drop_Page import DragAndDropPage
from pages.Dropdown_List_Page import DropdownListPage
from pages.Dynamic_Content_Page import DynamicContentPage
from pages.Dynamic_Controls_Page import DynamicControlsPage
from pages.Dynamic_Loading_Page import DynamicLoadingPage
from pages.File_Upload_Page import FileUploadPage
from pages.login_page import LoginPage


class HerokuPage:

    ADD_REMOVE_ELEMENTS = (By.XPATH, "//a[contains(text(), 'Add/Remove')]")
    DOM = (By.XPATH, '//*[@id="content"]/ul/li[5]/a')
    CHECKBOXES = (By.XPATH, '//a[@href = "/checkboxes"]')
    DRAG_AND_DROP = (By.XPATH, "//a[@href='/drag_and_drop']")
    DROPDOWN = (By.XPATH, "//a[@href='/dropdown']")
    DYNAMIC_CONTENT = (By.XPATH, "//a[@href='/dynamic_content']")
    DYNAMIC_CONTROLS = (By.XPATH, "//a[@href='/dynamic_controls']")
    DYNAMIC_LOADING = (By.XPATH, '//a[@href="/dynamic_loading"]')
    FILE_UPLOAD = (By.XPATH, '//a[@href="/upload"]')
    LOGIN = (By.XPATH, '//a[@href="/login"]')
    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, browser):
        self.browser = browser

    def go_to_heroku_page(self):
        self.browser.get(self.URL)

    def go_to_add_remove_elements_page(self):
        self.browser.find_element(*self.ADD_REMOVE_ELEMENTS).click()
        return AddRemoveElementsPage(self.browser)

    def go_to_challenging_dom_page(self):
        self.browser.find_element(*self.DOM).click()
        return ChalLengingDomPage(self.browser)

    def go_to_checkboxes_page(self):
        self.browser.find_element(*self.CHECKBOXES).click()
        return CheckboxesPage(self.browser)

    def go_to_drag_and_drop(self):
        self.browser.find_element(*self.DRAG_AND_DROP).click()
        return DragAndDropPage(self.browser)

    def go_to_dropdown_page(self):
        self.browser.find_element(*self.DROPDOWN).click()
        return DropdownListPage(self.browser)

    def go_to_dynamic_content(self):
        self.browser.find_element(*self.DYNAMIC_CONTENT).click()
        return DynamicContentPage(self.browser)

    def go_to_dynamic_control(self):
        self.browser.find_element(*self.DYNAMIC_CONTROLS).click()
        return DynamicControlsPage(self.browser)

    def go_to_dynamic_loading(self):
        self.browser.find_element(*self.DYNAMIC_LOADING).click()
        return DynamicLoadingPage(self.browser)

    def go_to_file_upload(self):
        self.browser.find_element(*self.FILE_UPLOAD).click()
        return FileUploadPage(self.browser)

    def go_to_login(self):
        self.browser.find_element(*self.LOGIN).click()
        return LoginPage(self.browser)

