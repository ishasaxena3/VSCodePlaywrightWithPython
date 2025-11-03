from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser (headless=False to see it)
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()
    
    #Steps to navigate to the site and login
    page.goto("https://dd-demo-tau.vercel.app/web_elements.html")
    page.click("a[href='#7-dropdown']")
    page.wait_for_load_state('networkidle')
    page.select_option("#dropdownField", label="Tesla")
    assert "Selected Car: Tesla" in page.text_content("#dropdownMsg"), "Dropdown message missing!"
    print("✅ Dropdown selection successful!")