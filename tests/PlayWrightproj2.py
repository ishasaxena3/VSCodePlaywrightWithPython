from playwright.sync_api import sync_playwright

with sync_playwright() as p:
        # Launch browser (headless=False to see it)
        browser = p.chromium.launch(headless=False, channel="chrome")
        page = browser.new_page()
        
        # Step 1: Navigate to site
        page.goto("https://www.saucedemo.com/")
        assert page.title() == "Swag Labs", "Title does not match!"
        print("✅ Title matches successfully!")

        # Step 2: Login
        page.fill('input[name="user-name"]', 'standard_user')
        page.fill('input[name="password"]', 'secret_sauce')
        page.click('#login-button')
        page.wait_for_load_state('networkidle')
        print("✅ Logged in successfully!")

        # Step 3: Add products to cart
        page.click('#add-to-cart-sauce-labs-backpack')
        page.click('button#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)')
        print("✅ Added items to cart!")

        # Step 4: Checkout
        page.click('.shopping_cart_link')
        page.click('#checkout')
        page.fill('#first-name', "Isha")
        page.fill('#last-name', "Kailashii")
        page.fill('#postal-code', "12345")
        page.click('#continue')
        page.click('#finish')

        # Step 5: Validate success message
        assert "Thank you for your order!" in page.text_content("body"), "Order confirmation missing!"
        print("✅ Checkout completed successfully!")

        browser.close()