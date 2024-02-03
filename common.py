# could not find a built-in tryparse function, and did not want to install outer modules so that
# the project won't get heavy
def try_parse(user_input: str, accept_float=False) -> bool:
    if not accept_float and user_input.isnumeric():
        return True
    elif accept_float:
        # the simple check of str.isdecimal() did not work well
        user_input_to_validate = user_input.replace('.', '')
        if user_input_to_validate.isnumeric():
            return True
        else:
            return False
    else:
        return False


# a reusable selection within range validator that can be called when a user input is not numeric / out of range
def is_option_within_range(selected, start_index, end_index) -> bool:
    if not start_index <= selected <= end_index:
        print(f'Selected option is invalid. '
              f'Please insert a valid numeric value between '
              f'{start_index} and {end_index}')
        return False
    return True
