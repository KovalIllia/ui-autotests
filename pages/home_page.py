from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver


class HomePage:
    URL = "http://automationexercise.com"
    SIGNUP_LOGIN_BUTTON=(By.XPATH, "//a[@href='/login']")


    def __init__(self, driver=WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def has_expected_title(self)->bool:
        return (self.driver.title=="Automation Exercise")

    def has_expected_url(self)->bool:
        return "automationexercise" in self.driver.current_url

    def is_loaded(self)-> bool:
        return self.driver.title=="Automation Exercise"


    def click_signup_login(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_LOGIN_BUTTON)).click()
