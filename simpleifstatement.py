# Simple if statement examples

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Example of case-insensitive comparison
name = 'Faasen'

if name.lower() == 'faasen':
    print("Hello, Faasen! Welcome back.")

# Example of checking age for alcohol purchase    

alcohol_age = 18  # Set the age limit for alcohol purchase

age = int(input("Enter your age: "))  # Check age

if age >= alcohol_age:
    print("You are old enough to buy alcohol.")
else:
    print("You are not old enough to buy alcohol.")