from playwright.sync_api import Page

class SauceDemo:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.dropdown = page.locator("[data-test='product-sort-container']")
        self.add_to_cart1 = page.locator("[data-test='add-to-cart-sauce-labs-onesie']")
        self.add_to_cart2 = page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.add_to_cart3 = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.add_to_cart4 = page.locator("[data-test='add-to-cart-sauce-labs-fleece-jacket']")
        self.remove_from_cart5 = page.locator("[data-test='remove-sauce-labs-bolt-t-shirt']")
        self.add_to_cart5 = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.remove_from_cart2 = page.locator("[data-test='remove-sauce-labs-onesie']")
        self.shopping_cart = page.locator("[data-test='shopping-cart-link']")
        self.checkout = page.locator("[data-test='checkout']")
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.back_to_products = page.locator("[data-test='back-to-products']")
        self.is_title_visible = page.locator("[data-test='primary-header']")
