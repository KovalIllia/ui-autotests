import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.data_generators import generate_password,generate_mobile_number


@pytest.fixture(scope="function")
def driver():
    options=webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def fake():
    return Faker()

@pytest.fixture(scope="function")
def password()->str:
    return generate_password()