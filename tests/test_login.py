from pages.Heroku_Page import HerokuPage


def test_success_login(browser):
    '''
    Open the Heroku website / Heroku website is opened
    1. Click From Authentication / Login page is opened
    2. Write correct username, password and click login button / Successfully login into the page
    3. Check if logout button is displayed/ Logout Button is displayed
    4. Click logout button/ Successfully logout

    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    login_page = heroku_page.go_to_login()
    login_page.alternative_login_button()
    assert login_page.is_logout_button_displayed()
    login_page.click_logout()


def test_wrong_password(browser):
    '''
     Open the Heroku website / Heroku website is opened
    1. Click From Authentication / Login page is opened
    2. Write correct username but wrong password
    3. Check if is an error message displayed/ Error message is displayed
    4. Check if the message match/ Message match
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    login_page = heroku_page.go_to_login()
    login_page.wrong_password()
    assert login_page.is_invalid_login_displayed(), "Logout button is displayed"
    assert login_page.get_invalid_message() == 'Your password is invalid!\n×', "No message appear"


def test_wrong_username(browser):
    '''
      Open the Heroku website / Heroku website is opened
     1. Click From Authentication / Login page is opened
     2. Write correct password but wrong username
     3. Check if is an error message displayed/ Error message is displayed
     4. Check if the message match/ Message match
     '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    login_page = heroku_page.go_to_login()
    login_page.wrong_username()
    assert login_page.is_invalid_login_displayed(), "Logout button is displayed"
    assert login_page.get_invalid_message() == 'Your username is invalid!\n×', "No message appear"


