from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser (headless=False to see it)
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()
        
    # Step 1: Navigate to site
    page.goto("https://www.google.com/")
       
    #Step 2: Validate title and URL
    assert page.title() == "Google", "Title does not match!"
    print("✅ Title matches successfully!")
    print("The URL of the page is: ", page.url)
    
    # Step 3: Search for a term
    page.click("//textarea[@id='APjFqb']")
    page.fill("//textarea[@id='APjFqb']", "Playwright Python")
    page.press("//textarea[@id='APjFqb']", "Enter")
    page.wait_for_load_state('networkidle') 

    # Step 4: Validate search results
    page.wait_for_selector("div#search") 
    assert "Playwright Python" in page.title(), "Search term not found in title!"
    print("✅ Search term found in title successfully!")