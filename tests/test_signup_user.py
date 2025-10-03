import random
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.logger import Logger


def test_signup_user(driver,fake):
    Logger.info("Navigating to home page")
    home_page=HomePage(driver)
    home_page.open()

    assert home_page.has_expected_url(), "URL is incorrect"
    assert home_page.has_expected_url(), "URL is incorrect"

    Logger.info("Clicking on Signup/Login button")
    home_page.click_signup_login()

    signup_page=SignupPage(driver)
    assert signup_page.is_loaded(),"Signup page did not load"

    name = fake.first_name()
    email = f"testuser{random.randint(1, 1000)}@gmail.com"
    signup_page.fill_form_for_signup_user(name,email)
    signup_page.click_submit_button()
    Logger.info(f"User signed up with name: {name}")
    Logger.info(f"User signed up with name: {email}")

    assert signup_page.is_account_info_banner_is_visiable(), "Account info banner not visible"
