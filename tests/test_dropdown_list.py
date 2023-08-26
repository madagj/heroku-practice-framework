from pages.Heroku_Page import HerokuPage


def test_click_option_1_2(browser):
    '''
    Open the Heroku website / Heroku website is opened
    1. Click on dropdown page / Drop Down page is opened
    2. Click drop down / Drop down options are displayed
    3. Click option 1 in drop down / Option 1 is displayed
    4. Click drop down / Drop down options are displayed
    5. Click option 2 in drop down / Option 2 is displayed
    6. Click drop down / Drop down options are displayed
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    dropdown_page = heroku_page.go_to_dropdown_page()
    dropdown_page.click_drop_down()
    dropdown_page.click_option_1()
    assert dropdown_page.is_option_1_displayed(), "Option 1 is not displayed"
    dropdown_page.click_drop_down()
    dropdown_page.click_option_2()
    assert dropdown_page.is_option_2_displayed(), "Option 2 is not displayed"
    dropdown_page.click_drop_down()
    assert dropdown_page.is_option_1_displayed(), "Both options are displayed"
    assert dropdown_page.is_option_2_displayed(), "Both options are displayed"
