import random
import string

def generate_random_name(legth=6):
    character = string.ascii_letters
    random_name = ''.join(random.choice(character) for _ in range(legth))
    return random_name

random_name = generate_random_name(10)
print("Generated random name: {}".format(random_name))