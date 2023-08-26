import time

from pages.Heroku_Page import HerokuPage


def test_upload_file_without_upload_file(browser):
    '''
      Open the Heroku website / Heroku website is opened
   1. Click Upload Files / Upload Files is opened
   2. Click on Upload Button without upload a file / Upload Button clicked
   3. Check if an error message is displayed / Error message is displayed
   4. Check if an error message match / Error message match
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    file_upload_page = heroku_page.go_to_file_upload()
    file_upload_page.click_upload_button()
    assert file_upload_page.is_error_message_displayed()
    assert file_upload_page.get_error_message() == "Internal Server Error"









