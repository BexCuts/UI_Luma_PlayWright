from playwright.sync_api import Page
from pages.locators import sale_locators
from pages.sale_page import SalePage


def test_women_sale(page: Page):
    sale_page = SalePage(page)
    sale_page.open_page()
    sale_page.more_button_click()
    sale_page.check_text(sale_locators.title, 'Women Sale')


def test_check_title(page: Page):
    sale_page = SalePage(page)
    sale_page.open_page()
    sale_page.check_title('Sale')


def test_go_to_logo(page: Page):
    sale_page = SalePage(page)
    sale_page.open_page()
    sale_page.click_on_logo()
    sale_page.check_to_be_visible(sale_locators.bg_white)
