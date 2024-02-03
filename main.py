from app import start_play, welcome
from modules.score.score import add_score

welcome()
user_score_to_add = start_play()

if user_score_to_add > 0:
    add_score(user_score_to_add)
