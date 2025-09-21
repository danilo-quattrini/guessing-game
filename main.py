import random


def define_random_number(min_limiter: int, max_limiter: int) -> int:
    return random.randrange(min_limiter, max_limiter)

min_range, max_range= int(input("Define the min range\n==>")), int(input("Define the max range\n==>"))
define_random_number(min_range, max_range)