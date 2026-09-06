
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
locator = tuple[str, str] #(By.ID, "email")
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator: locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        time.sleep(2)

    def fill(self, locator: locator, text: str) -> None:
        self.find(locator).send_keys(text)
        time.sleep(2)

    def get_text(self, locator: locator) -> str:
        return self.find(locator).text

    def scroll_down(self, pixels=500):
        ActionChains(self.driver).scroll_by_amount(0, pixels).perform()
