import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import fake, password
from utils.form_helper import FormHelper


class TestLogin:

    def test_register_user(self, driver, fake,password):
        driver.get("http://automationexercise.com")
        assert driver.title == "Automation Exercise"
        assert "automationexercise" in driver.current_url

        main_page_login_button = driver.find_element(By.XPATH, "//a[@href='/login']").click()
        signup_text = WebDriverWait(driver, 5).until(
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

        tittle_button=driver.find_element(By.XPATH,"//input[@type='radio' and @value='Mr']").click()
        password_field=driver.find_element(By.XPATH,"//input[@type='password' and @data-qa='password']")
        password_field.send_keys(password)

        form=FormHelper(driver)
        form.select_random_day()
        form.select_random_moth()
        form.select_random_year()

        newsletter_checkbox=driver.find_element(By.XPATH,"//input[@type='checkbox' and @name='newsletter']").click()
        special_offers_checkbox=driver.find_element(By.XPATH,"//input[@type='checkbox' and @name='optin']").click()

        """Address Information"""
        first_name=driver.find_element(By.XPATH,"//input[@data-qa='first_name' and @name='first_name']")
        first_name.send_keys(fake.first_name())

        last_name=driver.find_element(By.XPATH,"//input[@data-qa='last_name' and @name='last_name']")
        last_name.send_keys(fake.last_name())

