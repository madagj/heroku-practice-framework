from pages.Heroku_Page import HerokuPage
import time


def test_example_1(browser):
    '''
     Open the Heroku website / Heroku website is opened
     1. Click on Dynamic Loading / Dynamic Loading page is opened
     2. New page is open, click on start button / Start button clicked
     3. Check if text loading is displayed / Text loading is displayed
     4. Check if loading imagine is displayed / Imagine is displayed
     5. Check finish message appear / Finish message appear
     6. Check if finish message match / Finish message match
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dynamic_loading = heroku_page.go_to_dynamic_loading()
    dynamic_loading.click_example_1()
    dynamic_loading.get_url()
    dynamic_loading.click_start_button()
    assert dynamic_loading.is_text_loading_displayed(), "Text loading message is not displayed"
    assert dynamic_loading.is_loading_image_displayed(), " No image displayed"
    assert dynamic_loading.is_finish_text_displayed(), "No message appear"
    assert dynamic_loading.get_finish_text() == "Hello World!"


def test_example_2(browser):
    '''
     Open the Heroku website / Heroku website is opened
     1. Click on Dynamic Loading / Dynamic Loading page is opened
     2. New page is open, click on start button / Start button clicked
     3. Check if text loading is displayed / Text loading is displayed
     4. Check if loading imagine is displayed / Imagine is displayed
     5. Check finish message appear / Finish message appear
     6. Check if finish message match / Finish message match
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dynamic_loading = heroku_page.go_to_dynamic_loading()
    dynamic_loading.click_example_2()
    dynamic_loading.click_start_button()
    assert dynamic_loading.is_text_loading_displayed(), " Text loading message is not displayed"
    assert dynamic_loading.is_loading_image_displayed(), " No image displayed"
    assert dynamic_loading.is_finish_text_displayed(), "Success message missing"
    assert dynamic_loading.get_finish_text() == "Hello World!"
