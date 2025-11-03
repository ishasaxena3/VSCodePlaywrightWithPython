from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch Chrome browser (set headless=True to run in background)
    browser = p.chromium.launch(headless=False)
    
    # Open a new browser page
    page = browser.new_page()
    
    # Navigate to Google
    page.goto("https://www.google.com")
    
    # Print the page title
    print("Page title:", page.title())
    
    # Close the browser
    browser.close()
