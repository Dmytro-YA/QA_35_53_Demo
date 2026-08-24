import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import wait

from models.student import Student


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait.WebDriverWait(driver, 10)

    yield driver

    driver.quit()

@pytest.fixture
def student(driver) -> Student:
    return Student(
        first_name="John",
        last_name="Doe",
        email="anna@gmail.com",
        gender="Female",
        mobile="1234567890",
        date_of_birth="10 Nov 2000",
        subject="Math,English,History",
        hobbies="sports",
        picture="",
        current_address="123 Main St, City, State, Country",
        state="NCR",
        city="Delhi"
    )

