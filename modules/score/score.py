from modules.score.utils import SCORES_FILE_NAME_WRITE_CONTEXT
from common import try_parse


def add_score(difficulty: int) -> None:
    points_of_winning = None
    # check if file exists
    try:
        # read current points value from file
        with open(SCORES_FILE_NAME_WRITE_CONTEXT, 'r') as file:
            file_value = file.read()
            if try_parse(file_value):
                # if the file is valid and can be parsed into an int, assign it to the variable
                points_of_winning = int(file_value)
    # if the file does not exist, create it with the initial 0 value
    except FileNotFoundError:
        write_points_to_file('0')

    # if the reading from the file or the casting to int has failed,
    # resulting in POINTS_OF_WINNING to still be None,
    # preform a "reset" to the score value represented
    # in the file
    if points_of_winning is None:
        write_points_to_file('0')

    # calculate the new score based on the difficulty
    else:
        points_of_winning += (difficulty * 3) + 5
        write_points_to_file(str(points_of_winning))


def write_points_to_file(num_str: str) -> None:
    print(f'inserted is {num_str}')
    with open(SCORES_FILE_NAME_WRITE_CONTEXT, 'w') as file:
        file.write(num_str)
