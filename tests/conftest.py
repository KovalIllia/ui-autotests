import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.data_generators import generate_password


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def fake():
    return Faker()

@pytest.fixture(scope="function")
def password()->str:
    return generate_password()