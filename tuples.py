field_dimentions = (100, 50)
print("Field length:", field_dimentions[0])
print("\nField width:", field_dimentions[1])  

#Values in a tuple cannot be changed
#field_dimentions[0] = 120  # This will raise an error


print("\nOriginal field dimensions:")
for dimension in field_dimentions:
    print(dimension)

field_dimentions = (120, 60)
print("\nModified field dimensions:")
for dimension in field_dimentions:
    print(dimension)    