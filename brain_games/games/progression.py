from brain_games.constants import PROGRESSION_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def create_question():
    len_list = get_random_number(5, 10)
    index = get_random_number(0, len_list - 1)
    start = get_random_number(11, 99)
    step = get_random_number(2, 9)
    question = " ".join([".." if i == index else str(step * i + start)
                         for i in range(len_list)
                         ])
    right_answer = str(step * index + start)
    return question, right_answer


def start_game():
    run_game(create_question,
             PROGRESSION_INSTRUCTION
             )
