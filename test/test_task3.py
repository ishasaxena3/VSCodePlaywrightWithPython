import os
from pathlib import Path
from playwright.sync_api import Page, expect

def test_capture_screenshot(page: Page) -> None:
    # 1. Navigate to the page
    page.goto("https://playwright.dev/python/")
    
    # 2. Define the path where the screenshot will be saved
    
    # Define a base directory relative to the current working directory
    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(exist_ok=True)
    
    # Define the full file path using pathlib.Path (this handles separators correctly)
    # The Path object is necessary for the .exists() check later!
    file_path = screenshot_dir / "test_task3.png" # Creates a Path object like 'screenshots/test_task3.png'

    # 3. Capture the screenshot (Key Skill: the 'full_page=True' argument)
    print(f"Capturing full-page screenshot to: {file_path.resolve()}") # Use .resolve() to show the full path
    
    # Playwright accepts both Path objects and strings for the path argument
    page.screenshot(path=file_path, full_page=True)

    # 4. Assertion (Ensure the file exists as proof of the task completion)
    # This works because file_path is now a pathlib.Path object.
    assert file_path.exists(), f"Screenshot file was not found at {file_path}"

    print("Task 3 completed: Screenshot successfully captured and verified.")
