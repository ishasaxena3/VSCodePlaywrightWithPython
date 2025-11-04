import json
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser (headless=False to see it)
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()
    
    with open("testdata/products.json") as f:
        products = json.load(f)
        
    
    #Steps to navigate to the site and login
    page.goto(" https://www.saucedemo.com/")
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')                  
    page.wait_for_load_state('networkidle')
    
    # #Steps to add product to the cart
    # page.click("#add-to-cart-sauce-labs-backpack")
    # page.click("#add-to-cart-sauce-labs-fleece-jacket")
    # page.wait_for_load_state('networkidle') 
    # page.click(".shopping_cart_link")
    
    #Steps to add product to the card via external file
    for product in products:
        product_name=product["name"]
        product_id = product["id"]
        product_price = product["price"]
        # Check if the product name is visible in the cart page
        print(f"Adding {product_name} to cart...")
        page.click(f"#{product_id}")  # temporary placeholder
        page.wait_for_timeout(500)
    
    #Remove the product from the cart
    page.click(".shopping_cart_link")
    
    #Veify if all the products are available and added in the cart
    for product in products:
        product_name=product["name"]
        product_price=product["price"]
        assert page.is_visible(f"text={product_name}"), f"❌ {product_name} not found in cart!"
        print(f"✅ Verified {product_name} in cart")
        
    page.wait_for_load_state('networkidle') 
    #page.wait_for_selector("#remove-sauce-labs-backpack", state="visible")
    page.click("#remove-sauce-labs-backpack")
    
    #Complete the checkout process
    page.click("#checkout")
    page.wait_for_load_state('networkidle') 
    page.fill("#first-name",'Isha')
    page.fill("#last-name", 'Sena')
    page.fill("#postal-code",'123456')
    page.click("#continue")
    page.click("#finish")
    assert "Thank you for your order!" in page.text_content("body"), "Order confirmation missing!"
    print("✅ Checkout completed successfully!")
    Screenshot = page.screenshot(path="screenshot.png")
    print("✅ Screenshot taken successfully!")  
