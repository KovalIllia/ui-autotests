import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver  # ✅ Виправлений імпорт
from selenium.webdriver.support import expected_conditions as EC

from pages.basic_page import BasicPage
from pages.signup_page import SignupPage
from utils.logger import Logger


class HomePage(BasicPage):

    @allure.step("Verify home page is loaded")
    def is_loaded(self) -> bool:
        return (
            self.has_expected_title()
            and self.logo_is_visible()
            and self.is_navigation_bar_fully_visible()
        )

    Logger.info("Checking Home Page specific load conditions.")

    @allure.step("Click on 'Signup/Login' button")
    def click_signup_login(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_LOGIN_BUTTON)).click()
        Logger.info("Clicked on Signup/Login button")
        return SignupPage(self.driver)

    @allure.step("Get current URL")
    def get_current_login_url(self):
        return self.driver.current_url
