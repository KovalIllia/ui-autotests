from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import password
from utils.form_helper import FormHelper
from utils.logger import Logger


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
        self.wait = WebDriverWait(driver, 20)
        self.form = FormHelper(driver)

    def is_account_info_banner_is_visiable(self):
        Logger.debug("Waiting for 'Enter Account Information' header")
        return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_INFO_BANNER)).is_displayed()

    def choose_gender_button(self):
        gender_button = self.driver.find_element(*self.GENDER_RADIO_BUTTON).click()

    def fill_password(self, password):
        password = self.driver.find_element(*self.PASSWORD).send_keys(password)

    def select_random_day(self):
        return self.form.select_random_day()

    def select_random_month(self):
        return self.form.select_random_moth()

    def select_random_year(self):
        return self.form.select_random_year()

    def newsletter_checkbox(self):
        newsletter_checkbox = self.driver.find_element(*self.NEWSLETTER_CHECKBOX).click()

    def special_offers_checkbox(self):
        special_offers_checkbox = self.driver.find_element(*self.SPECIAL_OFFERS_CHECKBOX).click()

    def fill_first_name(self, first_name: str):
        first_name = self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def fill_last_name(self, last_name: str):
        last_name = self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def fill_company(self, company: str):
        company = self.driver.find_element(*self.COMPANY).send_keys(company)

    def fill_address(self, address: str):
        address = self.driver.find_element(*self.ADDRESS).send_keys(address)

    def fill_secondary_address(self, address: str):
        secondary_address = self.driver.find_element(*self.SECONDARY_ADDRESS).send_keys(address)

    def select_random_country(self):
        return self.form.select_random_country()

    def fill_state(self, state: str):
        state = self.driver.find_element(*self.STATE).send_keys(state)

    def fill_city(self, city: str):
        city = self.driver.find_element(*self.CITY).send_keys(city)

    def fill_zipcode(self, zipcode: str):
        zipcode = self.driver.find_element(*self.ZIPCODE).send_keys(zipcode)

    def fill_mobile_number(self, mobile_number: str):
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys(mobile_number)

    def create_account_button(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON).click()

    def create_account_banner_is_visiable(self):
        Logger.debug("Waiting for 'Account Created!' header")
        return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_CREATED_BANNER)).is_displayed()
