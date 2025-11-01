# check multiple conditions with lists

username = ['faasen', 'steven', 'alice']
secret = ['1234']

username_input = input("Enter your username: ")
password_input = input("Enter your secret: ")

if username_input in username and password_input in secret:
    print(f"Access granted for {username_input}.")
else:
    print("Access denied.")