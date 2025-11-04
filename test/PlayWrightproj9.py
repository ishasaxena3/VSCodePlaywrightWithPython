def test_invalid_login(page):  # <- page fixture comes from pytest-playwright
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.fill("input[name='username']", "wronguser")
    page.fill("input[name='password']", "wrongpass")
    page.click("button[type='submit']")
    page.wait_for_timeout(2000)
    assert "Dashboard" in page.title()
