prompt = "\nPlease enter your name or end to exit: "

while True:
    name = input(prompt)
    if name.lower() == 'end':
        break
    print(f"Hello, {name}!")