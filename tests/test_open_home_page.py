import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from tests.conftest import fake, password
from utils.data_generators import generate_mobile_number
from utils.form_helper import FormHelper
from utils.logger import Logger


def test_home_page(driver, fake):
    Logger.info("Opening Home Page")
    login_page=HomePage(driver)
    login_page.open()

    assert login_page.has_expected_title(),"Home page did not load correctly"
    assert login_page.has_expected_url(), "URL is incorrect"

    Logger.info("Clicking SignUp/Login")
    login_page.click_signup_login()
