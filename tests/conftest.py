import os
import random

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from utils.data_generators import generate_password
from utils.logger import Logger
from faker import Faker


@pytest.fixture(scope="function")
def faker():
    return Faker()

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.binary_location = "/usr/bin/google-chrome"

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def fake():
    return Faker()


@pytest.fixture(scope="function")
def password() -> str:
    return generate_password()


def pytest_runtest_setup(item):
    nodeId=item.nodeid
    Logger.start_test(nodeId)
    Logger.info(f"Starting setup for test: {nodeId}")

# @pytest.fixture(autouse=True)
# def test_logger(request):
#     nodeid = request.node.nodeid
#     os.environ["PYTEST_CURRENT_TEST"] = nodeid
#     Logger.start_test(nodeid)
#     Logger.info(f"Starting test: {nodeid}")
#     yield


def pytest_runtest_makereport(item, call):
    from utils.logger import Logger
    if call.when == "call":
        outcome = "PASSED" if call.excinfo is None else "FAILED"
        Logger.info(f"Test {item.nodeid} finished: {outcome}")
        if call.excinfo is not None:
            Logger.error(f"Failure in test {item.nodeid}: {call.excinfo}")

def pytest_runtest_teardown(item, nextitem):
    Logger.file_name = None


@pytest.fixture(scope="function")
def get_home_page(driver):
    # Logger.info("Navigating to home page")
    home_page = HomePage(driver)
    home_page.open()

    assert home_page.is_loaded(), "Home page did not load properly"
    assert home_page.has_expected_url(), "URL is incorrect"

    return home_page


@pytest.fixture(scope="function")
def get_signup_page(get_home_page):
    signup_page = get_home_page.click_signup_login()
    assert signup_page.is_loaded(), "Signup page did not load"
    return signup_page


@pytest.fixture(scope="function")
def get_register_page(get_signup_page, fake,generated_signup_data):
    name = generated_signup_data["name"]
    email = generated_signup_data["email"]

    signup_page = get_signup_page
    signup_page.fill_form_for_signup_user(name, email)

    register_page = signup_page.click_submit_button()
    Logger.info(f"User signed up with name: {name}, email: {email}")

    assert register_page.is_loaded(), "Account info banner not visible"
    return register_page,generated_signup_data


@pytest.fixture(scope="function")
def generated_signup_data(fake):
    name = fake.first_name()
    email = f"testuser{random.randint(1, 1000)}@gmail.com"
    signup_data = {"name": name,
                   "email": email}
    Logger.info(f"Generated signup data: Name:{name}, email:{email}")
    return signup_data
