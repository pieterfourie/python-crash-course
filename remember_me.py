from pathlib import Path
import json

def greet_user():
    """Greet the user by name."""
    path = Path('text_files/username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
# Stores user info in a Json file for future use