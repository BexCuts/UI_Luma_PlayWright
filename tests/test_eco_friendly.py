from playwright.sync_api import Page
from pages.eco_friendly_page import EcoFriendlyPage
from pages.locators import eco_friendly_locators


def test_change_table(page: Page):
    eco_page = EcoFriendlyPage(page)
    eco_page.open_page()
    eco_page.change_button()
    eco_page.check_text(eco_friendly_locators.after_change, 'Learn More')


def test_add_to_card(page: Page):
    eco_page = EcoFriendlyPage(page)
    eco_page.open_page()
    eco_page.add_to_card()
    eco_page.check_text(eco_friendly_locators.button_add_to_card, 'Add to Cart')


def test_empty_shopping_cart(page: Page):
    eco_page = EcoFriendlyPage(page)
    eco_page.open_page()
    eco_page.shopping_cart()
    eco_page.check_text(eco_friendly_locators.empty_message, 'You have no items in your shopping cart.')
