from pages.Heroku_Page import HerokuPage
import time


def test_display_on_page(browser):
    '''
     Open the Heroku website / Heroku website is opened
     1. Click on Dynamic Control / Dynamic Control page is opened
     2. Check if Add/Remove Button is displayed / Add/Remove Button is displayed
     3. Check if Checkbox is displayed / Checkbox is displayed
     4. Check if Enable/Disable Button is displayed / Enable/Disable Button is displayed
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dynamic_control_page = heroku_page.go_to_dynamic_control()
    assert dynamic_control_page.is_add_remove_button_displayed()
    assert dynamic_control_page.is_checkbox_displayed()
    assert dynamic_control_page.is_enable_disable_button_displayed()


def test_click_on_add_remove_button(browser):
    '''
      Open the Heroku website / Heroku website is opened
     1. Click on Dynamic Control / Dynamic Control page is opened
     2. Click Add Remove Button / Add Remove Button clicked
     3. Check if message text match on click Add Remove Button / Text message match
     4. Check if functionality of Add Remove Button is done / A success message appear
     5. Check if Success message match / Success message match
     6. Click on Add/Remove Button / Add/Remove button clicked
     7. Check if message text match on click Add Remove Button / Text message match
     8. Check if Success message match / Success message match
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dynamic_control_page = heroku_page.go_to_dynamic_control()
    dynamic_control_page.click_add_remove_button()
    assert dynamic_control_page.get_loading_message() == "Wait for it...", "No loading message appear"
    assert dynamic_control_page.is_message_click_displayed() == True
    assert dynamic_control_page.get_wait_message() == "It's gone!", "Wrong message appear"
    dynamic_control_page.click_add_remove_button()
    assert dynamic_control_page.get_loading_message() == "Wait for it...", "No loading message appear"
    assert dynamic_control_page.is_message_click_displayed() == True
    assert dynamic_control_page.get_wait_message() == "It's back!", "Wrong message appear"


def test_enable_disable_button(browser):
    '''
      Open the Heroku website / Heroku website is opened
     1. Click on Dynamic Control / Dynamic Control page is opened
     2. Click on Enable/Disable Button / Enable/Disable Button clicked
     3. Check if a success message appear and match / Success message appear and match
     4. Write a message into input box in this test in "Test123" / "Test123" is written in the input box
     5. Check if a success message appear and match / Success message appear and match
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dynamic_control_page = heroku_page.go_to_dynamic_control()
    dynamic_control_page.click_enable_disable_button()
    time.sleep(3)
    assert dynamic_control_page.get_wait_message() == "It's enabled!"
    dynamic_control_page.input_text()
    dynamic_control_page.click_enable_disable_button()
    time.sleep(5)
    assert dynamic_control_page.get_wait_message() == "It's disabled!"









