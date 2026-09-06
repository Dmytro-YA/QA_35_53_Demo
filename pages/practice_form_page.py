import platform
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from models.student import Student
from models.enums import Gender, Hobbies
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
    MODEL_TITLE = (By.ID, "example-modal-sizes-title-lg")

    def  fill_and_submit(self, student: Student) -> None:
        self.fill(self.FIRST_NAME, student.first_name)
        self.fill(self.LAST_NAME, student.last_name )
        self.fill(self.EMAIL, student.email)
        self._choose_gender(student.gender)

        self.fill(self.MOBILE, student.mobile)
        self._set_date_of_birth(student.date_of_birth)
        self._add_subjects(student.subject)
        self._choose_hobbies(student.hobbies)
        self.fill(self.CURRENT_ADDRESS, student.current_address)
        self.scroll_down()
        self._set_state_city(student.state, student.city)
        time.sleep(2)



        self.click(self.SUBMIT_BTN)
        time.sleep(2)
    def check_message(self) -> str:
        return self.get_text(self.MODEL_TITLE)


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

    def _choose_hobbies(self, hobbies: list[Hobbies]) -> None:

        for hobby in hobbies:
            self.driver.find_element(By.ID, hobby.locator).click()


    def _set_state_city(self, state: str, city: str) -> None:
        # field_state = self.find(self.STATE)
        self.find(self.STATE).send_keys(state, Keys.ENTER)
        self.find(self.CITY).send_keys(city, Keys.ENTER)

