import random

import allure

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.logger import Logger
from utils.data_generators import generate_mobile_number
from pages.alternative_register_page import RegisterPage
from utils.user_data import UserData


def test_register_user(driver,fake,password):
    Logger.info("Navigating to home page")
    home_page=HomePage(driver)
    home_page.open()

    assert home_page.has_expected_url(), "URL is incorrect"

    Logger.info("Clicking on Signup/Login button")
    home_page.click_signup_login()


    signup_page=SignupPage(driver)
    assert signup_page.is_loaded(),"Signup page did not load"

    name = fake.first_name()
    email = f"testuser{random.randint(1, 1000)}@gmail.com"
    signup_page.fill_form_for_signup_user(name,email)
    signup_page.click_submit_button()
    Logger.info(f"User signed up with name: {name}, email: {email}")


    assert signup_page.is_account_info_banner_is_visiable(), "Account info banner not visible"

    """Register"""

    register_page=RegisterPage(driver)
    user = UserData()
    assert register_page.is_account_info_banner_is_visiable(), "Register page did not load"

    register_page.fill_user_data_form(user)

    register_page.create_account_button()

    assert register_page.create_account_banner_is_visiable(), "Account Created banner not visible"


