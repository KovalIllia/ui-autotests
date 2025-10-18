from pages.register_page import RegisterPage
from utils.data_generators import generate_mobile_number
from utils.logger import Logger
from utils.user_data import UserData


def test_register_user(driver,fake,password,get_register_page):
    Logger.info("Starting user registration test")
    register_page = get_register_page

    user = UserData()
    register_page.fill_user_data_form(user)
    register_page.create_account_button()

    assert (
        register_page.create_account_banner_is_visiable()
    ), "Account Created banner not visible! The registration final banner was not displayed."
    Logger.info("User registration test finished successfully.")