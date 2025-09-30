import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import fake, password
from utils.data_generators import generate_mobile_number
from utils.form_helper import FormHelper
from selenium.webdriver.remote.webelement import WebElement


class TestLogin:

    def test_register_user(self, driver, fake, password):
        driver.get("http://automationexercise.com")
        assert driver.title == "Automation Exercise"
        assert "automationexercise" in driver.current_url

        main_page_login_button = driver.find_element(By.XPATH, "//a[@href='/login']").click()
        signup_text : WebElement= WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'New User Signup!')]"))
        )

        assert signup_text.is_displayed()

        signup_login_field = driver.find_element(By.XPATH,
                                                 "//input[@type='text' and @data-qa='signup-name' and @required]")
        signup_login_field.send_keys(fake.first_name())

        signup_mail_field = driver.find_element(By.XPATH, "//input[@data-qa='signup-email' and @type='email']")
        signup_mail_field.send_keys(f"testuser{random.randint(1, 1000)}@gmail.com")

        signup_button = driver.find_element(By.XPATH, "//button[@type='submit'][@data-qa='signup-button']").click()

        new_user_signup_baner = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Enter Account Information')]")))
        assert new_user_signup_baner.is_displayed()

        tittle_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='Mr']").click()
        password_field = driver.find_element(By.XPATH, "//input[@type='password' and @data-qa='password']")
        password_field.send_keys(password)

        form = FormHelper(driver)
        form.select_random_day()
        form.select_random_moth()
        form.select_random_year()

        newsletter_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='newsletter']").click()
        special_offers_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='optin']").click()

        """Address Information"""
        first_name = driver.find_element(By.XPATH, "//input[@data-qa='first_name' and @name='first_name']")
        first_name.send_keys(fake.first_name())

        last_name = driver.find_element(By.XPATH, "//input[@data-qa='last_name' and @name='last_name']")
        last_name.send_keys(fake.last_name())

        company_field = driver.find_element(By.XPATH, "//input[@data-qa='company' and @name='company']")
        company_field.send_keys(fake.company())

        address_first_field = driver.find_element(By.XPATH, "//input[@data-qa='address' and @id='address1']")
        company_field.send_keys(fake.address())

        address_second_field = driver.find_element(By.XPATH, "//input[@data-qa='address2' and @id='address2']")
        address_second_field.send_keys(fake.address())

        form.select_random_country()

        state_field = driver.find_element(By.XPATH, "//input[@data-qa='state' and @id='state']")
        state_field.send_keys(fake.state())

        city_field = driver.find_element(By.XPATH, "//input[@data-qa='city' and @id='city']")
        city_field.send_keys(fake.city())

        zipcode_field = driver.find_element(By.XPATH, "//input[@data-qa='zipcode' and @id='zipcode']")
        zipcode_field.send_keys(fake.zipcode())

        mobile_number_field = driver.find_element(By.XPATH, "//input[@data-qa='mobile_number' and @id='mobile_number']")
        mobile_number_field.send_keys(generate_mobile_number())

        create_account_button = driver.find_element(By.XPATH,
                                                    "//button[@data-qa='create-account' and @class='btn btn-default']").click()
        # time.sleep(1000)

        create_account_visible : WebElement= WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[@class='title text-center']//b[contains(text(), 'Account Created!')]")))

        assert create_account_visible.is_displayed()
        assert create_account_visible.text.strip()=='ACCOUNT CREATED!'

        continue_button=driver.find_element(By.XPATH,"//a[@data-qa='continue-button' or text()='Continue' or @class='btn btn-primary']")
        continue_button.click()

        time.sleep(1000)