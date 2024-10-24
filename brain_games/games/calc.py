from random import choice
from brain_games.constants import CALC_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def create_question():
    number_1 = get_random_number(1, 99)
    number_2 = get_random_number(1, 99)
    char = choice(["+", "-", "*"])
    question = f"{number_1} {char} {number_2}"
    right_answer = str(eval(question))
    return question, right_answer


def start_game():
    run_game(create_question,
             CALC_INSTRUCTION
             )
