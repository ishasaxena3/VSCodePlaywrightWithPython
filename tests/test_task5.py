import re
from playwright.sync_api import Page, expect

def test_dropdown(page: Page):
    dropdown_locator=page.locator('#dropdown')
    page.goto("https://the-internet.herokuapp.com/dropdown")
    
    dropdown_locator.select_option(index=1)
    expect(dropdown_locator).to_have_value("1")
    
    dropdown_locator.select_option(label="Option 2")
    expect(dropdown_locator).to_have_value("2")
    expect(page.locator("#dropdown")).to_have_value("2")
