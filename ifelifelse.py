
# Role-based login system with password check

# Define users and their passwords

users = {
    "faasen": "1234",
    "admin": "admin",
    "viewer": "viewonly",
    "editor": "editpass"
}

# Ask for login credentials
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if username exists
if username in users:
    # Check if password matches
    if username == "admin" and password == users[username]:
        print("Welcome, Admin! You have full access.")
    elif username == "viewer" and password == users[username]:
        print("Welcome, Viewer! You have read-only access.")
    elif username == "editor" and password == users[username]:
        print("Welcome, Editor! You can edit content.")
    elif username == "faasen" and password == users[username]:
        print("Welcome back boss! You have full access.")
    else: 
        print("Access denied.")