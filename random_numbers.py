# Create function that generates list of lists with random numbers, half of them should be integers and half floats
# numbers should be in range (0,100>
# each sublist should contain at least 10 numbers
import random


def generate_numbers():
    list_of_lists = []
    random_integers = []
    random_floats = []
    for i in range(0, 10):
        random_integers.append(random.randint(0, 100))
    for x in range(0, 10):
        random_floats.append(random.uniform(0, 100))
    list_of_lists = random_floats + random_integers
    return list_of_lists


generate_numbers()
