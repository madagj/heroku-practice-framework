import time

from pages.Heroku_Page import HerokuPage


def test_displayed(browser):
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    drag_and_drop_page = heroku_page.go_to_drag_and_drop()
    assert drag_and_drop_page.is_a_column_displayed()
    assert drag_and_drop_page.is_b_column_displayed()


def test_move_columns(browser):
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    drag_and_drop_page = heroku_page.go_to_drag_and_drop()
    drag_and_drop_page.column_a_move_to_b()



