import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FormHelper():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_random_day(self):
        desired_day = random.randint(1, 30)
        option = self.driver.find_element(By.XPATH,
                                          f"//select[@data-qa='days' and @name='days']/option[@value='{desired_day}']")
        option.click()
        return desired_day

    def select_random_moth(self):
        desired_month = random.randint(1, 12)
        option = self.driver.find_element(By.XPATH,
                                          f"//select[@data-qa='months' and @name='months']/option[@value='{desired_month}']")
        option.click()
        return desired_month

    def select_random_year(self, min_year=1900, max_year=2021):
        desired_year = random.randint(min_year, max_year)
        option = self.driver.find_element(By.XPATH,
                                          f"//select[@data-qa='years' and @name='years']/option[@value='{desired_year}']")
        option.click()
        return desired_year

    def select_random_country(self) -> str:
        list_of_countries = ["India", "United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore"]
        desired_country = random.choice(list_of_countries)
        option = self.driver.find_element(By.XPATH,
                                          f"//select[@data-qa='country' and @name='country']/option[@value='{desired_country}']")
        option.click()
        return list_of_countries
