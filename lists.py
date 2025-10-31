names = [ 'Faasen', 'Alice', 'Bob', 'Charlie', 'james bond' ]
print(names)

print(names[0])

print(names[4].title())

print(names[-1].title())

print(names[-1].upper())

message = f"Hello, {names[0].title()}! Welcome back."
print(message)

names[2] = 'Steve'
print(names[2])

names.append('Diana')
print(names)

names.insert(0, 'Zara')
print(names)   

del names[4]    
print(names)

popped_name = names.pop(0)
print(f"The friend you have lost is {popped_name.title()}!")


names.sort()
print(names)

print(sorted(names, reverse=True))
print(names)

print(len(names))
