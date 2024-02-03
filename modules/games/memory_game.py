import time
from random import randint
import common


def generate_sequence(game_difficulty) -> list[int]:
    numbers_sequence = []
    for num in range(game_difficulty):
        random_number = randint(0, 100)
        numbers_sequence.append(random_number)
    print(f'The numbers are {numbers_sequence}', end='')
    time.sleep(0.7)
    print('\r ')
    return numbers_sequence


def get_list_from_user() -> tuple[bool,list[str]]:
    user_input = input('Do you remember the numbers you have seen? type them separated by a comma: ')
    user_input_list = user_input.split(',')
    for num in user_input_list:
        num = num.strip()
        if not common.try_parse(num):
            print(f'{num} is not a valid number. Please type your guess again and make sure to type only numbers.')
            user_input_list = []
            return False,user_input_list
    return True,user_input_list


def is_list_equal(user_input_list: list[str], numbers_sequence: list[int]) -> bool:
    for num in user_input_list:
        if int(num) not in numbers_sequence:
            return False
    return True


def play(difficulty: int) -> bool:
    numbers_sequence = generate_sequence(difficulty)
    user_input_result = get_list_from_user()
    is_user_input_valid = user_input_result[0]
    while not is_user_input_valid:
        user_input_result = get_list_from_user()
        is_user_input_valid = user_input_result[0]
    return is_list_equal(user_input_result[1], numbers_sequence)
