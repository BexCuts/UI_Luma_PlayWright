from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import create_customer_locators
import random
import string


def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(10))
    domain = random.choice(domains)
    return f'{username}@{domain}'


class CreateCustomerPage(BasePage):
    page_url = '/customer/account/create/'

    def check_text(self, locator, text):
        expected_element = self.page.locator(locator)
        expect(expected_element).to_have_text(text)

    def fill_first_name(self):
        first_name = self.page.locator(create_customer_locators.first_name_input_locator)
        first_name.fill('Some')

    def fill_last_name(self):
        first_last = self.page.locator(create_customer_locators.last_name_input_locator)
        first_last.fill('Some')

    def fill_email(self):
        email = self.page.locator(create_customer_locators.email_input_locator)
        random_email = generate_random_email()
        email.fill(random_email)

    def fill_password(self):
        password = self.page.locator(create_customer_locators.password_input_locator)
        password.fill('SomePass123')

    def fill_confirm_password(self):
        confirm_password = self.page.locator(create_customer_locators.confirm_password_input_locator)
        confirm_password.fill('SomePass123')

    def create_button_click(self):
        create_button = self.page.locator(create_customer_locators.create_button_locator)
        create_button.click()

    def fill_password_invalid(self):
        password = self.page.locator(create_customer_locators.password_input_locator)
        password.fill('123')

    def full_fill(self):
        first_name = self.page.locator(create_customer_locators.first_name_input_locator)
        first_name.fill('Some')
        first_last = self.page.locator(create_customer_locators.last_name_input_locator)
        first_last.fill('Some')
        email = self.page.locator(create_customer_locators.email_input_locator)
        random_email = generate_random_email()
        email.fill(random_email)
        password = self.page.locator(create_customer_locators.password_input_locator)
        password.fill('SomePass123')
        confirm_password = self.page.locator(create_customer_locators.confirm_password_input_locator)
        confirm_password.fill('SomePass123')
