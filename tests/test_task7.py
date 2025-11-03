import re
from playwright.sync_api import Page, expect

def test_file_upload(page: Page):
    
    page.goto("https://the-internet.herokuapp.com/upload")
    #page.get_by_role("button", name="Choose File").click()
    page.get_by_role("button", name="Choose File").set_input_files("C:\\Users\\ishas\\TestingWorkSpace\\VCCodePlaywrightWithPython\\testData\\file_for_upload.txt")
    page.get_by_role("button", name="Upload").click()
    expect(page.get_by_text("file_for_upload.txt")).to_be_visible()
