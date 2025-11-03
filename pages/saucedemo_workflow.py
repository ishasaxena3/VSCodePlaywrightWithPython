from .saucedemo_tests import SauceDemo

class SauceDemoWorkflow:
    def __init__(self, sauce_demo: SauceDemo):
        self.pom = sauce_demo  # store the POM instance

    def enter_username(self, username):
        self.pom.username.fill(username)

    def enter_password(self, password):
        self.pom.password.fill(password)

    def click_login(self):
        self.pom.login_button.click()

    def dropdown_option(self):
        self.pom.dropdown.select_option("lohi")

    def click_add1(self):
        self.pom.add_to_cart1.click()

    def click_add2(self):
        self.pom.add_to_cart2.click()

    def click_add3(self):
        self.pom.add_to_cart3.click()

    def click_add4(self):
        self.pom.add_to_cart4.click()

    def click_remove1(self):
        self.pom.remove_from_cart5.click()

    def click_add5(self):
        self.pom.add_to_cart5.click()

    def click_remove2(self):
        self.pom.remove_from_cart2.click()

    def click_shopping_cart(self):
        self.pom.shopping_cart.click()

    def click_checkout(self):
        self.pom.checkout.click()

    def enter_fst_name(self, first_name):
        self.pom.first_name.fill(first_name)

    def enter_lst_name(self, last_name):
        self.pom.last_name.fill(last_name)

    def enter_postal_code(self, postal_code):
        self.pom.postal_code.fill(postal_code)

    def click_continue_button(self):
        self.pom.continue_button.click()

    def click_finish_button(self):
        self.pom.finish_button.click()

    def click_back_to_products(self):
        self.pom.back_to_products.click()