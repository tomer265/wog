from services.currency import get_conversion_rate
from common import try_parse
from random import randint


def get_money_interval(difficulty_level: int, random_usd_value: int) -> []:
    print('Please wait. Comparing your answer with the current USD/NIS exchange rate...')
    exchange_rate = get_conversion_rate('USD', 'ILS')
    accepted_interval = 10 - difficulty_level
    nis_value = random_usd_value * exchange_rate
    max_value = nis_value + accepted_interval
    min_value = nis_value - accepted_interval
    return {'max_value': max_value, 'min_value': min_value}


def get_guess_from_user() -> tuple[float, int]:
    random_usd_value = randint(1, 100)
    user_input = input(f"Can you guess the NIS value of {random_usd_value} USD? ")
    while not try_parse(user_input.strip(), True):
        user_input = input("Please insert a numeric value: ")
    return float(user_input), random_usd_value


def compare_results(difficulty_level: int, random_usd_value: int, user_input: float):
    min_max_values = get_money_interval(difficulty_level, random_usd_value)
    if min_max_values['min_value'] <= user_input <= min_max_values['max_value']:
        return True
    return False


def play(difficulty_level: int):
    user_guess = get_guess_from_user()
    return compare_results(difficulty_level, user_guess[1], user_guess[0])

