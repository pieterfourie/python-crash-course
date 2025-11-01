users = {
    "faasen": "1234",
    "steven": "abcd",
    "alice": "qwerty"
}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ") 

if username_input in users and users[username_input] == password_input:
    print(f"Access granted for {username_input}.")
else:
    print("Access denied.")

