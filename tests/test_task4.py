import re
from playwright.sync_api import Page, expect

def test_herokuapp(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    initial_URL=page.url
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=" Login").click()
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Welcome to the Secure Area.")).to_be_visible()
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url(initial_URL)