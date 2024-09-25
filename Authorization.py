# Mock user database for demo purposes
# This is a dictionary where keys are usernames and values are their respective tokens
user_database = {
    'user1': 'token123',      # 'user1' has 'token123' as their token
    'user2': 'token456',      # 'user2' has 'token456' as their token
    'admin': 'supersecret'    # 'admin' has 'supersecret' as their token
}

def is_authorized(username, token):
    """
    Checks if the given username and token match the user database.
    
    :param username: Username to check
    :param token: Token or password associated with the user
    :return: True if authorized, False otherwise
    """
    
    # Check if the username exists in the user database
    if username in user_database:
        
        # Check if the provided token matches the stored token for the user
        if user_database[username] == token:
            return True  # Authorization successful
        else:
            # If token doesn't match, print a message and return False
            print("Invalid token.")
            return False
    else:
        # If username not found in the database, print a message and return False
        print("Username not found.")
        return False

def main():
    """
    Main function to simulate user input and check authorization.
    """
    
    # Prompt the user to enter their username
    username = input("Enter your username: ")
    
    # Prompt the user to enter their token
    token = input("Enter your token: ")
    
    # Call the is_authorized function with the input username and token
    if is_authorized(username, token):
        # If authorized, print a success message
        print(f"User '{username}' is authorized!")
    else:
        # If not authorized, print a failure message
        print(f"User '{username}' is not authorized.")

# This ensures the script runs only when executed directly (not when imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to execute the authorization process
