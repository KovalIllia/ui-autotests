import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver  # Виправлено: використовуємо загальний тип WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.form_helper import FormHelper
from utils.logger import Logger



class BasicPage:
    URL = "https://automationexercise.com/"

    EXPECTED_LOGO = (By.XPATH, "//img[@src='/static/images/home/logo.png']")
    HOME_BUTTON = (By.XPATH, "//a[i[@class='fa fa-home']]")
    PRODUCTS_BUTTON = (By.XPATH, "//a[i[@class='material-icons card_travel'] and contains(text(), 'Products')]")
    CART_BUTTON = (By.XPATH, "//a[i[@class='fa fa-shopping-cart']and contains(text(), 'Cart')]")
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[i[@class='fa fa-lock']and contains(text(), ' Signup / Login')]")
    TEST_CASES_BUTTON = (By.XPATH, "//a[i[@class='fa fa-list']and contains(text(), ' Test Cases')]")
    API_TESTING_BUTTON = (By.XPATH, "//a[i[@class='fa fa-list']and contains(text(), ' API Testing')]")
    VIDEO_TUTORIALS_BUTTON = (By.XPATH, "//a[i[@class='fa fa-youtube-play']and contains(text(), ' Video Tutorials')]")
    CONTACT_US_BUTTON = (By.XPATH, "//a[i[@class='fa fa-envelope']and contains(text(), ' Contact us')]")
    FOOTER = (By.XPATH, "//footer[@id='footer']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
        self.form = FormHelper(driver)

    @allure.step("Opening the start page (URL)")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Checking the correctness of the page title: 'Automation Exercise'")
    def has_expected_title(self) -> bool:
        return self.driver.title == "Automation Exercise"

    @allure.step("Checking the URL: must have 'automationexercise'")
    def has_expected_url(self) -> bool:
        return "automationexercise" in self.driver.current_url

    @allure.step("Checking if the page is loaded (using Title)")
    def is_loaded(self) -> bool:
        return self.wait.until(EC.title_is("Automation Exercise"))

    @allure.step("Checking visibility of logo")
    def logo_is_visible(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.EXPECTED_LOGO)).is_displayed()

    def _get_navigation_element_locators(self):
        return [
            self.HOME_BUTTON,
            self.PRODUCTS_BUTTON,
            self.CART_BUTTON,
            self.SIGNUP_LOGIN_BUTTON,
            self.TEST_CASES_BUTTON,
            self.API_TESTING_BUTTON,
            self.VIDEO_TUTORIALS_BUTTON,
            self.CONTACT_US_BUTTON
        ]

    @allure.step("Checking the visibility of all navigation bar elements")
    def is_navigation_bar_fully_visible(self) -> bool:
        Logger.info("Checking visibility of all elements in the navigation bar.")

        """We use a helper method to get locators"""
        locators = self._get_navigation_element_locators()

        for locator in locators:
            try:
                self.wait.until(EC.visibility_of_element_located(locator))
            except:
                Logger.error(f"Navigation element with locator {locator} is NOT visible.")
                return False

        Logger.info("All navigation elements are visible.")
        return True


    @allure.step("Checking visibility of Footer")
    def is_footer_present(self) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(self.FOOTER))
            return True
        except:
            return False