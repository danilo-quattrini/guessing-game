import random

def define_random_number(min_limiter: int, max_limiter: int) -> int:
    """
        Function that takes two integers, we generate
        with the module randint a random number within the
        numbers from the min_limite to the max_limiter.
    :param min_limiter:
    :param max_limiter:
    :return: random number
    """
    return random.randint(min_limiter, max_limiter)

def guess_game(number_to_guess: int):
    """
        Function that takes a random number and with the
        user input it's going to show if the user it's near
        to guess the number or not.

        If the user write a number that's greater than the
        number_to_guest, it'll print that the number is "Too high",
        on the other and "Too low".

        The game will reach an end only if the user guess the number
        and print the numbers of time he tried to guess the number.
    :param number_to_guess:
    :return: None
    """
    chosen_number: int = 0
    guess_counter: int = 0
    while chosen_number != number_to_guess:
        chosen_number = int(input("Guess a number ==> "))
        if chosen_number > number_to_guess: print("Too high")
        elif chosen_number < number_to_guess: print("Too low")
        guess_counter += 1
        if chosen_number == number_to_guess:
            print(f"You Win!!!\nTotal guess: {guess_counter}")
            break

min_range, max_range = int(input("Define the min range\n==>")), int(input("Define the max range\n==>"))
guess_game(define_random_number(min_range, max_range))