import re
from playwright.sync_api import Page

from pages.parabank_classfile import Parabankvariables
from pages.parabank_methodsfile import Parabank_methods

def test_parabank(page: Page):
    
    #Goto URL
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    
    #Intitialize the class and method files
    parabank_cls = Parabankvariables(page)
    parabank_method = Parabank_methods(page, parabank_cls)
    
    #Enter Login, password and hit enter
    parabank_method.enter_username("TestUser")
    parabank_method.enter_password("TestUser123")
    parabank_method.click_login()
    
    #Check if welcome message is visible
 #   parabank_method.is_welcome_message_visible("Welcome TestUser123 Uss")
    
    #Click Account number, home and last logout
    parabank_method.click_accountnumber_link()
    parabank_method.click_homelink()
    parabank_method.click_logout()
