import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
  
    #Go to URL and save this URL for future assertions
    page.goto("https://duckduckgo.com/")
    initial_url = page.url
    
    #Search for a keyword
    page.get_by_role("combobox", name="Search with DuckDuckGo").fill("google.com")
    page.get_by_role("button", name="Search", exact=True).click()
    
    #Click on specific link that you want to open
    page.get_by_role("link", name="Google", exact=True).click()
    
    #Go back to the intitial IRL
    page.go_back()
    page.go_back()
    expect(page).to_have_url(initial_url)
    page.screenshot()
    expect(page.get_by_role("link", name="Learn about DuckDuckGo")).to_be_visible()
