import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.basic_page import BasicPage
from utils.logger import Logger
from utils.user_data import UserData


class RegisterPage(BasicPage):
    ACCOUNT_INFO_BANNER = (
        By.XPATH,
        "//b[contains(text(),'Enter Account Information')]",
    )
    GENDER_RADIO_BUTTON = (By.XPATH, "//input[@type='radio' and @value='Mr']")
    PASSWORD = (By.XPATH, "//input[@type='password' and @data-qa='password']")
    NEWSLETTER_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @name='newsletter']")
    SPECIAL_OFFERS_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @name='optin']")
    FIRST_NAME = (By.XPATH, "//input[@data-qa='first_name' and @name='first_name']")
    LAST_NAME = (By.XPATH, "//input[@data-qa='last_name' and @name='last_name']")
    COMPANY = (By.XPATH, "//input[@data-qa='company' and @name='company']")
    ADDRESS = (By.XPATH, "//input[@data-qa='address' and @id='address1']")
    SECONDARY_ADDRESS = (By.XPATH, "//input[@data-qa='address2' and @id='address2']")
    STATE = (By.XPATH, "//input[@data-qa='state' and @id='state']")
    CITY = (By.XPATH, "//input[@data-qa='city' and @id='city']")
    ZIPCODE = (By.XPATH, "//input[@data-qa='zipcode' and @id='zipcode']")
    MOBILE_NUMBER = (
        By.XPATH,
        "//input[@data-qa='mobile_number' and @id='mobile_number']",
    )
    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[@data-qa='create-account' and @class='btn btn-default']",
    )

    ACCOUNT_CREATED_BANNER = (
        By.XPATH,
        "//h2[@class='title text-center']//b[contains(text(), 'Account Created!')]",
    )

    @allure.step("expected banner: 'Enter Account Information'")
    def is_loaded(self) -> bool:
        Logger.debug("Waiting for 'Enter Account Information' header")
        try:
            banner = self.wait.until(
                EC.visibility_of_element_located(self.ACCOUNT_INFO_BANNER)
            )
            return banner.is_displayed()
        except Exception as e:
            Logger.error(f"RegisterPage not loaded: {e}")
            return False

    def fill_user_data_form(self, user: UserData):
        Logger.info(f"Filling out registration form for user: {user.first_name}")
        self.wait.until(EC.element_to_be_clickable(self.GENDER_RADIO_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(
            user.password
        )

        self.form.select_random_day()
        self.form.select_random_month()
        self.form.select_random_year()

        self.wait.until(EC.element_to_be_clickable(self.NEWSLETTER_CHECKBOX)).click()
        self.wait.until(
            EC.element_to_be_clickable(self.SPECIAL_OFFERS_CHECKBOX)
        ).click()
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(
            user.first_name
        )
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(
            user.last_name
        )
        self.wait.until(EC.visibility_of_element_located(self.COMPANY)).send_keys(
            user.company
        )
        self.wait.until(EC.visibility_of_element_located(self.ADDRESS)).send_keys(
            user.address
        )
        self.wait.until(
            EC.visibility_of_element_located(self.SECONDARY_ADDRESS)
        ).send_keys(user.secondary_address)
        self.form.select_random_country()
        self.wait.until(EC.visibility_of_element_located(self.STATE)).send_keys(
            user.state
        )
        self.wait.until(EC.visibility_of_element_located(self.CITY)).send_keys(
            user.city
        )
        self.wait.until(EC.visibility_of_element_located(self.ZIPCODE)).send_keys(
            user.zipcode
        )
        self.wait.until(EC.visibility_of_element_located(self.MOBILE_NUMBER)).send_keys(
            user.mobile
        )
        Logger.info(
            f"Data used: Name={user.first_name}, "
            f"last_name: {user.last_name}, "
            f"Pass={user.password}, "
            f"City={user.city}, "
            f"Address={user.address[:20]}, "
            f"secondary_adress: {user.secondary_address[:30]}, "
            f"state: {user.state}, "
            f"zipcode: {user.zipcode}, "
            f"mobile_number: {user.mobile}"
        )

    def create_account_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_BUTTON)).click()
        Logger.info("Clicked 'Create Account' button.")

    @allure.step("Check the message about successful registration")
    def create_account_banner_is_visiable(self):
        Logger.debug("Waiting for 'Account Created!' header")
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_CREATED_BANNER)
        ).is_displayed()
