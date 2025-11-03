import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://books-pwakit.appspot.com/")
    page.locator("#input").fill("Playwright")
    page.locator("#input").press("Enter")
    expect(page.get_by_role("link", name="The Playwright's Process")).to_be_visible()