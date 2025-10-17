from pages.home_page import HomePage
from pages.signup_page import SignupPage
from tests.conftest import fake
from utils.logger import Logger


def test_navigate_to_signup_page(driver, fake):
    Logger.info("Starting navigation test: Home -> Signup/Login")
    home_page = HomePage(driver)
    home_page.open()

    assert home_page.is_loaded(), "Home page failed to load"
    Logger.info("Home page loaded successfully")

    Logger.info("Clicking SignUp/Login button")
    signup_page = home_page.click_signup_login()

    actual_signup_url = driver.current_url
    expected_signup_url = "/login"

    assert isinstance(
        signup_page, SignupPage
    ), "click_signup_login did not return a SignupPage object."
    assert (
        expected_signup_url in actual_signup_url
    ), f"Wrong target URL. Expected path '{expected_signup_url}' not in '{actual_signup_url}'"
