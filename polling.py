responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Would you like the event to continue?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} voted: {response}.")       