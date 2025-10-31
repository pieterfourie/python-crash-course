players = ['alice', 'bob', 'charlie', 'david', 'eve', 'frank', 'grace', 'heidi']
print(players[0:3])      # First three players

print(players[:4])       # First four players

print(players[3:])       # Players from the 4th to the end

print(players[-3:])      # Last three players

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    