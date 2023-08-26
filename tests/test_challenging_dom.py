from pages.Heroku_Page import HerokuPage


def test_click_all_3_buttons(browser):
    '''
       Open the Heroku website / Heroku website is opened
    1. Click on Challenging DOM / Challenging DOM page is opened
    2. Check the message on Green Button / Green button message check
    3. Check if click on Blue Button the message on Green Button change / Green Button message change
    4. Check if click on Green Button the message on Green Button change / Green Button message change
    5. Check if click on Red Button the message on Green Button change / Green Button message change
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dom_page = heroku_page.go_to_challenging_dom_page()
    first_message = dom_page.get_green_button_text
    dom_page.click_blue_button()
    second_message = dom_page.get_green_button_text
    assert first_message is not second_message, "Display the same message"
    dom_page.click_green_button()
    third_message = dom_page.get_green_button_text
    assert second_message is not third_message, "Display the same message"
    last_message = dom_page.get_green_button_text
    assert third_message is not last_message, "Display the same message"


def test_all_elements_in_page(browser):
    '''
    Open the Heroku website / Heroku website is opened
    1. Click on Challenging DOM / Challenging DOM page is opened
    2. Check if Blue Button is displayed on page / Blue Button is displayed
    3. Check if Red Button is displayed on page / Red Button is displayed
    4. Check if Green Button is displayed on page / Green Button is displayed
    5. Check if Answer message is displayed / Answer message is displayed
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dom_page = heroku_page.go_to_challenging_dom_page()
    assert dom_page.is_blue_button_displayed()
    assert dom_page.is_red_button_displayed()
    assert dom_page.is_green_button_displayed()
    assert dom_page.is_answer_displayed()


