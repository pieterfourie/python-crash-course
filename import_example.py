import pet

# pet.describe_pet('name', 'type')

pet.my_pet('willie', 'dog')


# OR

from pet import my_pet as mp

mp('harry', 'hamster')

# OR

from pet import *

my_pet('whiskers', 'cat')