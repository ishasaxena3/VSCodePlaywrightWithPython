from playwright.sync_api import Page, expect

def test_basic_auth(page: Page) -> None:
    # 1. Define the correct URL format including the credentials (admin:admin)
    AUTH_URL = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
    
    # 2. Navigate to the authenticated URL
    page.goto(AUTH_URL)
    
    # 3. Assert that the successful login message is visible
    SUCCESS_MESSAGE = "Congratulations! You must have the proper credentials."
    expect(page.get_by_text(SUCCESS_MESSAGE)).to_be_visible()