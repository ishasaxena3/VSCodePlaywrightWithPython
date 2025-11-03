def test_ap(playwright):
    request=playwright.request.new_context()
    response=request.get("https://reqres.in/api/users/2")
    print(response.status)
    json_data=response.json()
    print(json_data)
    request.dispose()
    print("Done")
    
    