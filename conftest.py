import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import wait

from models.enums import Gender, Hobbies, StateCity
from models.student import Student
from faker import Faker

fake = Faker()

@pytest.fixture
def driver():
    options = Options()
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
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
        hobbies=[Hobbies.SPORTS, Hobbies.READING, Hobbies.MUSIC],
        picture="",
        current_address="123 Main St, City, State, Country",
        state=StateCity.RAJASTHAN.state,
        city=StateCity.RAJASTHAN.cities[0],
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
