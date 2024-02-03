from common import try_parse
from random import randint


def generate_number(difficulty: int):
    secret_number = randint(1, difficulty)
    return secret_number


def get_guess_from_user() -> int:
    entered_number = input("Guess the number!\nEnter your guess: ")
    while not try_parse(entered_number.strip()):
        entered_number = input("Please insert a numeric value: ")
    return int(entered_number.strip())


def compare_results(secret_number) -> bool:
    if secret_number == get_guess_from_user():
        return True
    return False


def play(difficulty: int):
    secret_number = generate_number(difficulty)
    return compare_results(secret_number)
