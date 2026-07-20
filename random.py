import random

def random_pop(data):
    number = random.randint(0, len(data-1))
    return data.pop(number)
    