import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.register_page import RegisterPage
from utils.logger import Logger


class SignupPage:
    SIGNUP_HEADER = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ACCOUNT_INFO_BANNER = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Verify that the title 'New User Signup!' is displayed.")
    def is_loaded(self):
        Logger.debug("Waiting for 'New User Signup!' header")
        return self.wait.until(
            EC.visibility_of_element_located((self.SIGNUP_HEADER))).is_displayed()

    @allure.step("Fill out the sing in form: name and email")
    def fill_form_for_signup_user(self, name, email):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        Logger.info(f"Entered signup name: {name}")
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        Logger.info(f"Entered email: {email}")

    @allure.step("Click on the 'Sign Up' button")
    def click_submit_button(self):
        signup_button = self.driver.find_element(*self.SIGNUP_BUTTON).click()
        return RegisterPage(self.driver)

    # @allure.step("Check that the 'Enter Account Information' banner is displayed")
    # def is_account_info_banner_is_visiable(self):
    #     return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_INFO_BANNER)).is_displayed()
