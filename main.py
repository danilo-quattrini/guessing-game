import random

def define_random_number(min_limiter: int, max_limiter: int) -> int:
    return random.randint(min_limiter, max_limiter)

def guess_game(number_to_guess: int):
    chosen_number: int = 0
    guess_counter: int = 0
    while chosen_number != number_to_guess:
        chosen_number = int(input("Guess a number ==> "))
        if chosen_number > number_to_guess: print("Too high")
        else: print("Too low")
        guess_counter += 1
    print(f"You Win!!!\nTotal guess: {guess_counter}")

min_range, max_range = int(input("Define the min range\n==>")), int(input("Define the max range\n==>"))
guess_game(define_random_number(min_range, max_range))