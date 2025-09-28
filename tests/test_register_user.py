import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestLogin:

    def test_register_user(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("http://automationexercise.com")
        # потрібно створити даний степ --- Verify that home page is visible successfully


        signup_button = driver.find_element(By.XPATH, "//a[@href='/login']")
        signup_button.click()






# registration
# @pytest.mark.positive
#     @pytest.mark.parametrize("new_user_data",
#                              TestDataProvider.generate_user_reg_data(save_user=True))
#     def test_registration_success_scenario(self, app, new_user_data):
#         # TestDataProvider.save_created_account(new_user_data["email"], new_user_data["password"])
#         app.home_page.open_homepage()
#         app.home_page.click_sign_in()
#         app.authentication_page.create_account_section.input_email_address(new_user_data["email"])
#         app.authentication_page.create_account_section.click_button_create_account()
#         actual = app.authentication_page.get_page_h1_heading_text()
#         pytest.assume("CREATE AN ACCOUNT" == actual, "Actual:{} ,Expected: {}".format(actual, "CREATE AN ACCOUNT"))
#         actual = app.authentication_page.personal_info_section.get_section_heading()
#         pytest.assume("YOUR PERSONAL INFORMATION" == actual,
#                       "Actual:{} ,Expected: {}".format(actual, "YOUR PERSONAL INFORMATION"))
#
#         app.authentication_page.personal_info_section.input_personal_info(new_user_data)
#         app.authentication_page.personal_info_section.click_button_register()
#         title = app.authentication_page.get_title()
#         expected_title = "My account - My Store"
#         pytest.assume(title == expected_title, "Actual:{} ,Expected: {}".format(title, expected_title))
#         full_name = app.myaccount_page.get_logged_in_full_name()
#         expected_full_name = new_user_data["first_name"] + " " + new_user_data["last_name"]
#         pytest.assume(full_name == expected_full_name.lower(),
#                       "Actual:{} ,Expected: {}".format(full_name, expected_full_name))


#
# login
# @pytest.mark.positive
#     def test_open_homepage(self,app):
#         app.home_page.open_homepage()
#         assert("My Store" == app.home_page.get_title())
#
#
#     @pytest.mark.positive
#     @pytest.mark.parametrize("user_creds,page_title",
#                              [({"username": "autopracuser1@mailnesia.com", "password": "autoprac1234"},
#                                "My account - My Store")])
#     def test_login_success(self, app, user_creds, page_title):
#         app.home_page.open_homepage()
#         app.home_page.click_sign_in()
#         app.authentication_page.login_section.perform_login(user_creds["username"], user_creds["password"])
#         assert (page_title == app.authentication_page.get_title())