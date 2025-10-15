import random

import allure

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.logger import Logger
from utils.data_generators import generate_mobile_number
from pages.register_page import RegisterPage

def test_register_user(driver,fake,password):
    Logger.info("Navigating to home page")
    home_page=HomePage(driver)
    home_page.open()

    assert home_page.has_expected_url(), "URL is incorrect"

    Logger.info("Clicking on Signup/Login button")

    # home_page.click_signup_login()
    # signup_page=SignupPage(driver)
    signup_page = home_page.click_signup_login()


    assert signup_page.is_loaded(),"Signup page did not load"

    name = fake.first_name()
    email = f"testuser{random.randint(1, 1000)}@gmail.com"
    signup_page.fill_form_for_signup_user(name,email)
    signup_page.click_submit_button()
    Logger.info(f"User signed up with name: {name}, email: {email}")


    assert signup_page.is_account_info_banner_is_visiable(), "Account info banner not visible"

    """Register"""
    register_page=RegisterPage(driver)
    assert register_page.is_account_info_banner_is_visiable(), "Register page did not load"

    register_page.choose_gender_button()
    register_page.fill_password(password)
    register_page.select_random_day()
    register_page.select_random_month()
    register_page.select_random_year()

    register_page.fill_first_name(fake.first_name())
    register_page.fill_last_name(fake.last_name())
    register_page.fill_company(fake.company())
    register_page.fill_address(fake.address())
    register_page.fill_secondary_address(fake.address())
    register_page.select_random_country()
    register_page.fill_city(fake.city())
    register_page.fill_state(fake.state())
    register_page.fill_zipcode(fake.zipcode())
    mobile_number=generate_mobile_number()
    register_page.fill_mobile_number(mobile_number)
    register_page.create_account_button()
    register_page.create_account_banner_is_visiable()


    assert register_page.create_account_banner_is_visiable(), "Account Created banner not visible"


