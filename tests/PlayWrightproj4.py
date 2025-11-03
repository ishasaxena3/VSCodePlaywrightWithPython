from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser (headless=False to see it)
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()
        
    # Step 1: Navigate to site
    page.goto("https://www.saucedemo.com/")
    print("The URL of the page is: ", page.url)
    page.wait_for_load_state('networkidle') 
    print("✅ Title matches successfully!")
    
    # Step 2: Login
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')                  
    page.wait_for_load_state('networkidle')
    print("✅ Logged in successfully!")
    # Step 3: Logout
    page.click('button[id="react-burger-menu-btn"]')
    page.click('a[id="logout_sidebar_link"]')
    page.wait_for_load_state('networkidle')
    print("✅ Logged out successfully!")