import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import password
from utils.form_helper import FormHelper
from utils.logger import Logger
from utils.user_data import UserData


class RegisterPage:
    ACCOUNT_INFO_BANNER = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
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
    MOBILE_NUMBER = (By.XPATH, "//input[@data-qa='mobile_number' and @id='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH,
                             "//button[@data-qa='create-account' and @class='btn btn-default']")

    ACCOUNT_CREATED_BANNER = (
        By.XPATH, "//h2[@class='title text-center']//b[contains(text(), 'Account Created!')]"
    )

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.form = FormHelper(driver)

    # def is_account_info_banner_is_visiable(self):
    #     with allure.step("expected banner: 'Enter Account Information'"):
    #         Logger.debug("Waiting for 'Enter Account Information' header")
    #         return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_INFO_BANNER)).is_displayed()

    def fill_user_data_form(self, user: UserData):
        self.driver.find_element(*self.GENDER_RADIO_BUTTON).click()

        self.driver.find_element(*self.PASSWORD).send_keys(user.password)

        self.form.select_random_day()
        self.form.select_random_month()
        self.form.select_random_year()

        self.driver.find_element(*self.NEWSLETTER_CHECKBOX).click()
        self.driver.find_element(*self.SPECIAL_OFFERS_CHECKBOX).click()

        self.driver.find_element(*self.FIRST_NAME).send_keys(user.first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(user.last_name)
        self.driver.find_element(*self.COMPANY).send_keys(user.company)
        self.driver.find_element(*self.ADDRESS).send_keys(user.address)
        self.driver.find_element(*self.SECONDARY_ADDRESS).send_keys(user.secondary_address)
        self.form.select_random_country()
        self.driver.find_element(*self.STATE).send_keys(user.state)
        self.driver.find_element(*self.CITY).send_keys(user.city)
        self.driver.find_element(*self.ZIPCODE).send_keys(user.zipcode)
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys(user.mobile)

    def create_account_button(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON).click()

    @allure.step("Check the message about successful registration")
    def create_account_banner_is_visiable(self):
        Logger.debug("Waiting for 'Account Created!' header")
        return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_CREATED_BANNER)).is_displayed()
