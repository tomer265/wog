import services.games_configs_getters as games_service
import common
from modules.games import currency_roulette_game, guess_game, memory_game


def option_not_in_range(to_option: int):
    return input(f'\nPlease insert a numeric option between 1 and {to_option}: ')


def welcome(message='Hello player, please insert your name: '):
    username = input(message)
    while not username.strip():
        username = input('Please insert your name: ')
    username = username.strip()
    print(f'Hi {username} and welcome to the World of Game: The Epic Journey. ')


def start_play() -> int:
    # Game selection section
    print('Please choose a game to play:')
    # gets available games
    available_games = games_service.get_available_games()
    if len(available_games) <= 0:
        print('No games found.')
        return 0

    # lists the available games in the console
    for index, available_game in enumerate(available_games):
        print(f'\t{index+1}.\t{available_game}')

    # gets the user's GAME selection and validate that the input is an int and within range
    user_game_selection = input()
    while (not common.try_parse(user_game_selection)
           or not common.is_option_within_range(int(user_game_selection), 1, len(available_games))):
        user_game_selection = option_not_in_range(len(available_games))

    # re-assigning the selected game to an int type variable
    user_game_selection = int(user_game_selection)
    user_game_selection_name = available_games[user_game_selection-1]

    # Difficulty selection section
    game_difficulties = games_service.get_game_difficulties()
    # sets a default difficulty
    default_game_difficulty = 1
    if len(game_difficulties) <= 0:
        print(f'No levels available. Selecting the default level {default_game_difficulty}')
    else:
        print('\nPlease choose a game difficulty:')
        # lists the available difficulties in the console
        for available_difficulty in game_difficulties:
            print(f'\t{available_difficulty}')

        # gets the user's GAME selection and validate that the input is an int and within range
        user_difficulty_selection = input()
        while (not common.try_parse(user_difficulty_selection)
               or not common.is_option_within_range(int(user_difficulty_selection), 1, len(game_difficulties))):
            user_difficulty_selection = option_not_in_range(len(game_difficulties))

        user_difficulty_selection = game_difficulties[int(user_difficulty_selection)-1]
        # prints the final result of the user's selection
        print(f'You have selected the game "{user_game_selection_name}"'
              f'\nSelected difficulty level is {user_difficulty_selection}.\n\nGood luck!')

        game_to_start = None
        match user_game_selection:
            case 1:
                game_to_start = memory_game
            case 2:
                game_to_start = guess_game
            case 3:
                game_to_start = currency_roulette_game

        game_result = game_to_start.play(user_difficulty_selection)
        if game_result:
            print('You have won!')
            return user_difficulty_selection
        else:
            print('You have lost.')
            return 0

        