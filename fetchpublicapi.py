import requests

def fetch_user_data():
    """
    Fetch user data from the JSONPlaceholder API and display specific information.
    """
    try:
        # Fetch data from the API
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON data
        users = response.json()

        # Display specific information about each user
        print("User Details:")
        for user in users:
            print(f"Name: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print("Error fetching data from the API:", e)

def main():
    print("Fetching data from JSONPlaceholder API...\n")
    fetch_user_data()

if _name_ == "main":
    main()
