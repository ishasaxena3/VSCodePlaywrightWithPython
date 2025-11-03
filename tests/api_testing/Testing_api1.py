from playwright.sync_api import sync_playwright

def test_firstapi():
    with sync_playwright() as playwright:
        request = playwright.request.new_context()
        response = request.get("https://jsonplaceholder.typicode.com/posts/1")

        # ✅ assert syntax correction
        assert response.status == 200

        # ✅ fixed typo (.joson -> .json)
        json_data = response.json()
        print(json_data)

        # ✅ assert syntax correction
        assert json_data["id"] == 1
        request.dispose()
