import time

from pages.Heroku_Page import HerokuPage


def test_displayed(browser):
      '''
    Open the Heroku website / Heroku website is opened
    1. Click on drag and drop/ Drag and drop page is opened
    2. Check if column A and column B are displayed/ Both are displayed
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    drag_and_drop_page = heroku_page.go_to_drag_and_drop()
    assert drag_and_drop_page.is_a_column_displayed()
    assert drag_and_drop_page.is_b_column_displayed()





