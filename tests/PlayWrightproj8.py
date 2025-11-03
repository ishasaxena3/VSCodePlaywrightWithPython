def test_dashboard_page_title(logged_in_page):
    assert "Dashboard" in logged_in_page.title()
