from pages.home_page import HomePage
from tests.conftest import fake
from utils.logger import Logger


def test_home_page(driver, fake):
    Logger.info("Opening Home Page")
    login_page = HomePage(driver)
    login_page.open()

    actual_title = driver.title
    assert login_page.has_expected_title(), f"expected title: 'Automation Exercise', but got: {actual_title}"

    actual_url = driver.current_url
    assert login_page.has_expected_url(), f"URL is incorrect.expected url: 'automationexercise', but got: {actual_url} "

    Logger.info("Clicking SignUp/Login")
    login_page.click_signup_login()
