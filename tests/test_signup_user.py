import random

from pages.register_page import RegisterPage
from pages.signup_page import SignupPage
from utils.logger import Logger


def test_signup_user(driver, fake, get_home_page):
    Logger.info("Navigating to home page")
    home_page = get_home_page

    signup_page = home_page.click_signup_login()
    actual_signup_header = driver.find_element(*SignupPage.SIGNUP_HEADER).text
    assert (
        signup_page.is_loaded()
    ), f"Signup page did not load. Expected header: 'New User Signup!', but got : {actual_signup_header}"

    name = fake.first_name()
    email = f"testuser{random.randint(1, 1000)}@gmail.com"
    signup_page.fill_form_for_signup_user(name, email)

    register_page=signup_page.click_submit_button()
    Logger.info(f"User signed up with name: {name}")
    Logger.info(f"User signed up with email: {email}")

    actual_info_banner = driver.find_element(*RegisterPage.ACCOUNT_INFO_BANNER).text
    assert (
        register_page.is_account_info_banner_is_visiable()
    ), f"Account info banner not visible. Expected banner: 'Enter Account Information', but got: {actual_info_banner}"

