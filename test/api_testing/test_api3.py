from playwright.sync_api import expect
import pytest

def test_get_user(playwright):
    # Create a new API request context
    request_context = playwright.request.new_context()

    # Send GET request
    response = request_context.get("https://reqres.in/api/users/2")

    # Assertions
    assert response.ok, f"Request failed with status {response.status}"
    #assert response.status == 200

    data = response.json()
    assert data["data"]["first_name"] == "Janet"

    # Dispose context to clean up
    request_context.dispose()