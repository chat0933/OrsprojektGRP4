def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        print("Login successful!")
        # Add code here to proceed to the next page or perform additional actions
    else:
        print("Invalid username or password. Please try again.")

# Main program
print("Welcome to the Login Page!")
login()