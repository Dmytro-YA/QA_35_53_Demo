import time

from pages.home_page import HomePage

class TestFormPage:
    def test_open_practice_form(self, driver, student ):
        practice_forms_page = HomePage(driver).open().open_forms().open_practice_form()
        time.sleep(2)
        practice_forms_page.fill_and_submit(student)
        assert practice_forms_page.check_message() == "Thanks for submitting the form"



