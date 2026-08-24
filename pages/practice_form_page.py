from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from models.student import Student

class PracticeFormPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@placeholder = 'First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder = 'Last Name']")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    MOBILE = (By.ID, 'userNumber')
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput' or @class='form-control react-datepicker-ignore-onclickoutside']")
    SUBJECTS = (By.CSS_SELECTOR, "input#subjectsInput.subjects-auto-complete__input")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@placeholder='Current Address']")
    STATE  = (By.ID, "react-select-3-input")
    CITY = (By.ID, "react-select-4-input")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Submit']")

    def  fill_and_submit(self, student: Student) -> None:
        self.fill(self.FIRST_NAME, student.first_name)
        self.fill(self.LAST_NAME, student.last_name )
        self.fill(self.EMAIL, student.email)
        self.fill(self.MOBILE, student.mobile)

        self.click(self.SUBMIT_BTN)



