import random

from utils.logger import Logger


def test_signup_user(driver, fake, get_home_page):
    Logger.info("Navigating to home page")
    home_page = get_home_page
    Logger.info("Home Page is loaded via fixture")

    signup_page = home_page.click_signup_login()
    assert signup_page.is_loaded(), "Signup page did not load or header is incorrect."

    name = fake.first_name()
    email = f"testuser{random.randint(1, 1000)}@gmail.com"
    signup_page.fill_form_for_signup_user(name, email)

    register_page = signup_page.click_submit_button()
    assert register_page.is_loaded(), "Register Page (Enter Account Information) failed to load."

    Logger.info("Successfully navigated to Register Page after initial signup.")
    # assert (
    #     register_page.create_account_banner_is_visiable()
    # ), "Account Created! banner not visible after successful submission."
