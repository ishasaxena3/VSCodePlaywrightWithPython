import re
from playwright.sync_api import expect

def test_google_search(page):
    # Optional short wait to let context load
    page.wait_for_timeout(1000)

    # Go to Google
    page.goto("https://www.google.com/ncr")

    # Handle cookie popup if present
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No popup to accept, proceeding with the test execution")

    # Search for 'Playwright Python'
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")

    # Validate title
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))