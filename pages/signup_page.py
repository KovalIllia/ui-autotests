import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.basic_page import BasicPage
from pages.register_page import RegisterPage
from utils.logger import Logger


class SignupPage(BasicPage):
    SIGNUP_HEADER = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    ACCOUNT_INFO_BANNER = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")


    @allure.step("Verify that the title 'New User Signup!' is displayed.")
    def is_loaded(self):
        Logger.debug("Waiting for 'New User Signup!' header")
        return self.wait.until(
            EC.visibility_of_element_located((self.SIGNUP_HEADER))).is_displayed()

    @allure.step("Fill out the sing in form: name and email")
    def fill_form_for_signup_user(self, name, email):
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        Logger.info(f"Entered signup name: {name}")

        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        Logger.info(f"Entered email: {email}")

    @allure.step("Click on the 'Sign Up' button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BUTTON)).click()
        Logger.info("Clicked on 'Sign Up' button.")
        return RegisterPage(self.driver)

    @allure.step("Get current URL")
    def get_current_signup_url(self):
        return self.driver.current_url
