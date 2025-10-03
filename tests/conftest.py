import os

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from utils.data_generators import generate_password
from utils.logger import Logger


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
def password()->str:
    return generate_password()


@pytest.fixture(autouse=True)
def test_logger(request):
    nodeid=request.node.nodeid
    os.environ["PYTEST_CURRENT_TEST"]=nodeid
    Logger.start_test(nodeid)
    Logger.info(f"Starting test: {nodeid}")
    yield

def pytest_runtest_makereport(item, call):
    from utils.logger import Logger
    if call.when == "call":
        outcome = "PASSED" if call.excinfo is None else "FAILED"
        Logger.info(f"Test {item.nodeid} finished: {outcome}")
        if call.excinfo is not None:
            Logger.error(f"Failure in test {item.nodeid}: {call.excinfo}")