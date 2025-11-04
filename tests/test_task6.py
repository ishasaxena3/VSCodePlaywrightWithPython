import re
from playwright.sync_api import expect, Page

def test_dialogBox(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")    
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.get_by_text("You clicked: Ok")).to_be_visible()
