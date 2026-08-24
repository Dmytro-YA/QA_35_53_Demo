from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.practice_form_page import PracticeFormPage

class FormsPage(BasePage):
    PRACTICE_FORM_LINK = (By.XPATH, "//span[text()='Practice Form']")

    def open_forms(self) -> PracticeFormPage:
        self.find(self.PRACTICE_FORM_LINK)
        return PracticeFormPage(self.driver)

    def open_practice_form(self):
        self.click(self.PRACTICE_FORM_LINK)
        return PracticeFormPage(self.driver)