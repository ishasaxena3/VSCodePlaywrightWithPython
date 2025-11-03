from playwright.sync_api import Page

class Parabankvariables:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("input[name=\"username\"]")
        self.password =  page.locator("input[name=\"password\"]")
        self.enter_button = page.get_by_role("button", name="Log In")
        self.welcome_message = page.locator("smallText")
        self.accountnumber_link = page.get_by_role("link", name="15231")
        self.homepage_link = page.get_by_role("link", name="home")
        self.logout = page.get_by_role("link", name="Log Out")