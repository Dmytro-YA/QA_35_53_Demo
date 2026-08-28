import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import wait

from models.enums import Gender
from models.student import Student
from faker import Faker

fake = Faker()

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait.WebDriverWait(driver, 10)

    yield driver
    time.sleep(2)
    driver.quit()

@pytest.fixture
def student(driver) -> Student:
    return Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        gender=Gender.FEMALE,
        mobile=fake.numerify("058##########"),
        date_of_birth="12 Feb 1999",
        subject="Math,English,History",
        hobbies="sports",
        picture="",
        current_address="123 Main St, City, State, Country",
        state="NCR",
        city="Delhi"
    )

