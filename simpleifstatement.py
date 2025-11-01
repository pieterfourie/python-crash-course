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
    