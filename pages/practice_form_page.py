import platform
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from models.student import Student
from models.enums import Gender
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
        self._choose_gender(student.gender)

        self.fill(self.MOBILE, student.mobile)
        self._set_date_of_birth(student.date_of_birth)
        self._add_subjects(student.subject)
        time.sleep(2)



        # self.click(self.SUBMIT_BTN)


    def _choose_gender(self, gender: Gender) -> None:
        self.driver.find_element(By.ID, gender.locator).click()

    def _set_date_of_birth(self, date_of_birth: str) -> None:
        field_date = self.find(self.DATE_OF_BIRTH)
        field_date.click()
        select_all = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL
        field_date.send_keys(select_all + "a")
        field_date.send_keys(date_of_birth + Keys.ENTER)

    def _add_subjects(self, subjects: str) -> None:
        field_sub = self.find(self.SUBJECTS)
        field_sub.click()
        for subject in subjects.split(","):
            field_sub.send_keys(subject)
            time.sleep(0.3)
            field_sub.send_keys(Keys.ENTER)

