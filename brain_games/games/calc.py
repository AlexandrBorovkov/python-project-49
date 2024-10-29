from random import choice
from brain_games.constants import CALC_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def choice_math_operations(number_1, number_2):
    return choice([
        ("+", number_1 + number_2),
        ("-", number_1 - number_2),
        ("*", number_1 * number_2)
    ])


def get_an_example_and_answer():
    number_1, number_2 = get_random_number(1, 99), get_random_number(1, 99)
    math_operation = choice_math_operations(number_1, number_2)
    return f"{number_1} {math_operation[0]} {number_2}", str(math_operation[1])


def start_game():
    run_game(get_an_example_and_answer,
             CALC_INSTRUCTION
             )
