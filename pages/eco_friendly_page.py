from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_text(self, locator, text):
        expected_element = self.page.locator(locator).first
        expect(expected_element).to_have_text(text)

    def change_button(self):
        button_to_change_table = self.page.locator(eco_friendly_locators.button_to_change_table).first
        button_to_change_table.click()

    def add_to_card(self):
        first_element = self.page.locator(eco_friendly_locators.list_of_elements).first
        first_element.click()

    def shopping_cart(self):
        shopping_cart = self.page.locator(eco_friendly_locators.shopping_cart)
        shopping_cart.click()
