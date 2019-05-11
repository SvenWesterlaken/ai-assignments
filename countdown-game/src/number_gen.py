import random

def generate_numbers(n=6, max_big=100):

    small_numbers = list(range(1, 10))
    big_numbers = list(range(25, max_big+1, 25))

    return random.sample(small_numbers + big_numbers, n)

def generate_goal_number(max=999): return random.randint(100, max)
