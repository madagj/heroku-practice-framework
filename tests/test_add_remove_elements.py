import random
import time
from pages.Heroku_Page import HerokuPage


def test_delete_button_is_displayed(browser):
    '''
     Open the Heroku website / Heroku website is opened
    1. Click on Add Remove Elements / Add/Remove Elements page is opened
    2. Click on Add Element button / Delete button is displayed
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    add_element_page = heroku_page.go_to_add_remove_elements_page()
    add_element_page.click_add_button()
    assert add_element_page.delete_button(), "Delete button is not displayed"


def test_add_remove_delete_button(browser):
    '''
     Open the Heroku website / Heroku website is opened
    1. Click on Add Remove Elements / Add/Remove Elements page is opened
    2. Click on Add Element button random times /  Delete buttons are displayed
    3. Click random numbers of times / 0 Delete buttons is displayed
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    add_remove_element_page = heroku_page.go_to_add_remove_elements_page()
    add_remove_element_page.click_add_button()
    no_max = random.randint(1, 200)
    i = 1
    while i < no_max:
        add_remove_element_page.click_add_button()
        i += 1
    assert add_remove_element_page.get_number_of_delete_button() == no_max
    for a in range(add_remove_element_page.get_number_of_delete_button()):
        add_remove_element_page.click_delete_button()
    assert add_remove_element_page.get_number_of_delete_button() == 0


def test_message_displayed(browser):
    '''
    Open the Heroku website / Heroku website is opened
    1. Click on Add Remove Elements / Add/Remove Elements page is opened
    2. Check if the text is displayed on the page
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    add_element_page = heroku_page.go_to_add_remove_elements_page()
    assert add_element_page.get_title_page() == "Add/Remove Elements", "Message is not displayed"







