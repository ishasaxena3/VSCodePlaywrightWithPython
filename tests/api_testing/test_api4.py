import pytest
from playwright.sync_api import APIRequestContext

@pytest.fixture(scope="session")
def api_context(playwright):
    # Create one API context for the session
    request_context = playwright.request.new_context(base_url="https://reqres.in")
    yield request_context
    request_context.dispose()

def test_create_user(api_context: APIRequestContext):
    payload = {
        "name": "Ankisha",
        "job": "QA Specialist"
    }

    response = api_context.post("/api/users", data=payload)

    # Assertions
    assert response.ok, f"Request failed with status {response.status}"
    assert response.status == 201

    data = response.json()
    assert data["name"] == "Ankisha"
    assert data["job"] == "QA Specialist"
    assert "id" in data