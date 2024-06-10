from playwright.sync_api import Page
from pages.locators import create_customer_locators
from pages.create_customer_page import CreateCustomerPage


def test_create_customer(page: Page):
    create_page = CreateCustomerPage(page)
    create_page.open_page()
    create_page.full_fill()
    create_page.create_button_click()
    create_page.check_text(create_customer_locators.my_account, 'My Account')


def test_password_count_of_num_validation(page: Page):
    create_page = CreateCustomerPage(page)
    create_page.open_page()
    create_page.fill_first_name()
    create_page.fill_last_name()
    create_page.fill_email()
    create_page.fill_password_invalid()
    create_page.create_button_click()
    create_page.check_text(create_customer_locators.weak_pass, 'Minimum length of this field must be '
                           'equal or greater than 8 symbols. Leading and trailing spaces will be ignored.')


def test_create_without_email(page: Page):
    create_page = CreateCustomerPage(page)
    create_page.open_page()
    create_page.fill_first_name()
    create_page.fill_last_name()
    create_page.fill_password()
    create_page.fill_confirm_password()
    create_page.create_button_click()
    create_page.check_text(create_customer_locators.email_empty, 'This is a required field.')
