# tests/saucedemo_workflow_testing_with_methods.py
from playwright.sync_api import Page, expect
from pages.saucedemo_tests import SauceDemo
from pages.saucedemo_workflow import SauceDemoWorkflow

def test_sauceDemo(page: Page):
    page.goto("https://www.saucedemo.com/")

    # initialize POM
    sauce_demo = SauceDemo(page)
    workflow = SauceDemoWorkflow(sauce_demo)

    # login
    workflow.enter_username("standard_user")
    workflow.enter_password("secret_sauce")
    workflow.click_login()
    expect(sauce_demo.is_title_visible).to_contain_text("Swag Labs")

    # sort and add items
    workflow.dropdown_option()
    workflow.click_add1()
    workflow.click_add2()
    workflow.click_add3()
    workflow.click_add4()
    workflow.click_remove1()
    workflow.click_add5()
    workflow.click_remove2()

    # checkout process
    workflow.click_shopping_cart()
    workflow.click_checkout()
    workflow.enter_fst_name("Isha")
    workflow.enter_lst_name("S")
    workflow.enter_postal_code("V9A5J1")
    workflow.click_continue_button()
    workflow.click_finish_button()

    # verify order complete
    expect(page.locator("[data-test='complete-header']")).to_be_visible()
    expect(page.locator("[data-test='complete-header']")).to_contain_text("Thank you for your order!")

    # back to products
    workflow.click_back_to_products()