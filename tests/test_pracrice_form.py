import time
from tabnanny import check
import pytest_check as check
import allure
from models import student
from pages.home_page import HomePage
from selenium.webdriver.common.by import By


FIRST_NAME = (By.XPATH, "//tbody/tr[1]/td[2]")
TEXT_FORM = "Thanks for submitting the form"

@allure.epic("DemoQA")
@allure.feature("Practice Form")

class TestFormPage:
    @allure.story("Fill and submit the form")
    @allure.title("Test Fill and submit the form")
    @allure.description("Test Fill and submit the form")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_practice_form(self, driver, student ):
        practice_forms_page = HomePage(driver).open().open_forms().open_practice_form()
        time.sleep(2)
        practice_forms_page.fill_and_submit(student)
        with allure.step("Check message"):
            assert practice_forms_page.check_message() == TEXT_FORM

    @allure.story("Fill and submit the form")
    @allure.title("Test Fill and submit the form")
    @allure.description("Test Fill and submit the form")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_submit_check_data_in_table(self, driver, student ):
        allure.attach(
            str(student),
            name = "student",
            attachment_type=allure.attachment_type.TEXT
        )
        practice_forms_page = HomePage(driver).open().open_forms().open_practice_form()
        time.sleep(2)
        practice_forms_page.fill_and_submit(student)

        check.equal(practice_forms_page.check_message(), TEXT_FORM)
        check.is_in(student.first_name, driver.find_element(*FIRST_NAME).text)
        # check.equal(practice_forms_page.check_message(), "TEXT_FORM")
        print("test is working")
        check.is_in(student.last_name, driver.find_element(*FIRST_NAME).text)








