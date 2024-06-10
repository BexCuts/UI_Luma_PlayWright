from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import sale_locators


class SalePage(BasePage):
    page_url = '/sale.html'

    def more_button_click(self):
        more_button = self.page.locator(sale_locators.more_button)
        more_button.click()

    def check_text(self, locator, text):
        expected_element = self.page.locator(locator)
        expect(expected_element).to_have_text(text)

    def check_title(self, text):
        title = self.page.locator(sale_locators.title)
        expect(title).to_have_text(text)

    def click_on_logo(self):
        logo = self.page.locator(sale_locators.logo)
        logo.click()

    def check_to_be_visible(self, locator):
        expected_element = self.page.locator(locator).first
        expect(expected_element).to_be_visible()
