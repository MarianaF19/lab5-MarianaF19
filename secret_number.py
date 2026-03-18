import random

def seed_secret_numbers(seed):
    return random.seed(seed)

def generate_secret_numbers(star=1, end=100):
    return random.randint(start,end)