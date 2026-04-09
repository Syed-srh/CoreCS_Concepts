# 2: Login Validation System
# Design a login system with proper validation.

# Features to be implemented
# Define username and password
# Accept user input
# Create custom exception:
# InvalidCredentialsError
# Add functionality:
# Raise exception if credentials do not match
# Print appropriate message
# Additional Requirements
# Allow maximum 3 login attempts
# Stop after 3 failed attempts

class InvalidCredentialsError(Exception):
    pass

def login(username, password):
    # Define valid credentials
    valid_username = "admin"
    valid_password = "password"

    if username == valid_username and password == valid_password:
        print("Login successful.")
    else:
        raise InvalidCredentialsError("Invalid username or password.")

# Example usage:
if __name__ == "__main__":
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
            break
        except InvalidCredentialsError as e:
            print(e)
            attempts += 1
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break

    if attempts == max_attempts:
        print("Too many failed login attempts. Program terminated.")

# This program implements a simple login validation system that checks user credentials against predefined values. It allows up to three attempts for the user to enter the correct username and password, and it raises a custom exception if the credentials are invalid.

