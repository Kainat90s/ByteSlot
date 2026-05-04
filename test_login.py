import requests

def test_login(username, password):
    url = "http://localhost:8000/api/accounts/login/"
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Testing with known users from DB
    test_login("Lukmaan", "testpassword123") # Assuming a default password or common one
