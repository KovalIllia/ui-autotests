from utils.data_generators import generate_mobile_number
from utils.logger import Logger


def test_register_user(driver, fake, password, get_register_page):
    Logger.info("Starting user registration test")
    register_page=get_register_page

    register_page.choose_gender_button()
    register_page.fill_password(password)
    register_page.select_random_day()
    register_page.select_random_month()
    register_page.select_random_year()

    register_page.fill_first_name(fake.first_name())
    register_page.fill_last_name(fake.last_name())
    register_page.fill_company(fake.company())
    register_page.fill_address(fake.address())
    register_page.fill_secondary_address(fake.address())
    register_page.select_random_country()
    register_page.fill_city(fake.city())
    register_page.fill_state(fake.state())
    register_page.fill_zipcode(fake.zipcode())
    mobile_number = generate_mobile_number()
    register_page.fill_mobile_number(mobile_number)
    register_page.create_account_button()
    register_page.create_account_banner_is_visiable()

    assert register_page.create_account_banner_is_visiable(), "Account Created banner not visible"
    Logger.info("User registration test finished successfully.")