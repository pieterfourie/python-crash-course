car_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}

print(car_0['color'])
print(car_0['speed'])

car_0['x_position'] = 0
car_0['y_position'] = 25
print(car_0)

print(f"Original position: {car_0['x_position']}")

if car_0['speed'] == 'slow':
    x_increment = 1
elif car_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

car_0['x_position'] = car_0['x_position'] + x_increment

print(f"New position: {car_0['x_position']}")

del car_0['points']
print(car_0)

point_values = car_0.get('points', 'No point value assigned.')
print(point_values)