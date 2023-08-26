from pages.Heroku_Page import HerokuPage


def test_click_checkboxes(browser):
    '''
   Open the Heroku website / Heroku website is opened
   1. Click on Checkbox / Checkbox page is opened
   2. In Checkbox page Checkbox 2 is already clicked
   3. Click on checkbox1 / Checkbox 1 is clicked
   4. Check if both checkbox are clicked / Both checkbox are clicked
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    checkbox_page = heroku_page.go_to_checkboxes_page()
    checkbox_page.click_checkbox1()
    assert checkbox_page.is_checkbox1_clicked() == True
    assert checkbox_page.is_checkbox2_clicked() == True



def test_checkbox2_is_clicked(browser):
    '''
     Open the Heroku website / Heroku website is opened
   1. Click on Checkbox / Checkbox page is opened
   2. Check if checkbox 2 is clicked / Checkbox 2 is clicked
    '''
    heroku_page = HerokuPage(browser)
    heroku_page.go_to_heroku_page()
    checkbox_page = heroku_page.go_to_checkboxes_page()
    assert checkbox_page.is_checkbox2_clicked() == True








