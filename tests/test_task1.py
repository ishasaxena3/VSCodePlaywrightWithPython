import re
from playwright.sync_api import Page, expect

def test_duckduckgo(page: Page):
    
    #Navigate to the page
    page.goto("https://duckduckgo.com/")
    
    #Seach for the Playwright with pythin keyword and hit enter
    page.get_by_role("combobox", name="Search with DuckDuckGo").fill("Playwright with python")
    page.get_by_role("button", name="Search", exact=True).click()
    
    #Assert for the URL
    print(f"Current URL: {page.url}")
    expect(page).to_have_url(re.compile(r"q=Playwright\+with\+python"))
    
    # You could also assert the search box element is still present and visible
    expect(page.get_by_role("combobox", name="search")).to_be_visible()

    # 4. Click the link to the Playwright documentation
    # We use part of the text for a link locator for reliability.
    page.get_by_role("link", name="Getting started - Library |").click()
    
    # 5. Assertion 2: Verify the final destination
    # The most important check is that the click worked and we landed on the correct page.
    #expect(page).to_have_url("https://playwright.dev/python/docs/intro")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()