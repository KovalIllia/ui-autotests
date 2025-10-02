import random

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import fake
from utils.logger import Logger


class SignupPage:
    SIGNUP_HEADER = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ACCOUNT_INFO_BANNER = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")

    def __init__(self, driver=WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        Logger.debug("Waiting for 'New User Signup!' header")
        return self.wait.until(
            EC.visibility_of_element_located((self.SIGNUP_HEADER))).is_displayed()



    def fill_form_for_signup_user(self,name,email):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        Logger.info(f"Entered signup name: {name}")
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        Logger.info(f"Entered email: {email}")


    def click_submit_button(self):
        signup_button = self.driver.find_element(*self.SIGNUP_BUTTON).click()


    def is_account_info_banner_is_visiable(self):
        return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_INFO_BANNER)).is_displayed()

