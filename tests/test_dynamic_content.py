from pages.Heroku_Page import HerokuPage


def test_click_message(browser):
    '''
    Open the Heroku website / Heroku website is opened
    1. Click on Dynamic content/ Dynamic content page is opened
    2. Check message on the tird image in webpage / Message check
    3. Click on "click here" and check if the message change / Message has been changed
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dynamic_page = heroku_page.go_to_dynamic_content()
    first_message = dynamic_page.get_message_text
    dynamic_page.click_button()
    second_message = dynamic_page.get_message_text
    assert first_message is not second_message, "Message are similar"
