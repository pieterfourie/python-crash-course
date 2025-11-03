# Make an emp

aliens = []

# Make 30 green aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change the first 3 aliens to yellow
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'    

# Show the first 5 aliens

for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created

print(f"Total number of aliens: {len(aliens)}")


print("\n")

# Lets store a list in a dictionary

Sandwitch = {
    'bread': 'wheat',
    'exrtras': ['lettuce', 'tomato', 'bacon'],
}

# Summarize the order
print(f"You ordered a {Sandwitch['bread']} bread sandwitch with the following extras:\n")
for extra in Sandwitch['exrtras']:
    print(f"- {extra}")
    print("\n")


# A dictionary in a dictionary

users = {
    'cronaldo': {
        'first': 'cristiano',
        'last': 'ronaldo',
        'location': 'madrid',
    },

    'flampard': {
        'first': 'frank',
        'last': 'lampard',
        'location': 'chelsea',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print("\n")

