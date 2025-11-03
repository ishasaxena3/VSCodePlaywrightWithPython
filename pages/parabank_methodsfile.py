from playwright.sync_api import Page,expect

class Parabank_methods:
    def __init__(self, page: Page,parabank_cls):
        self.page = page
        self.locators = parabank_cls
    
    def enter_username(self,username):
        self.locators.username.fill(username)
        
    def enter_password(self,password):
        self.locators.password.fill(password)
        
    def click_login(self):
        self.locators.enter_button.click()
        
    def is_welcome_message_visible(self, expected_text):
        expect(self.locators.welcome_message).to_contain_text(expected_text)
      
    def click_accountnumber_link(self):
        self.locators.accountnumber_link.click()
        
    def click_homelink(self):
        self.locators.homepage_link.click()
        
    def click_logout(self):
        self.locators.logout.click()