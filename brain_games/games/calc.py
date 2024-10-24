from random import choice
from brain_games.constants import CALC_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def choice_math_operations(number_1, number_2):
    math_operations = [
        ("+", number_1 + number_2),
        ("-", number_1 - number_2),
        ("*", number_1 * number_2)
    ]
    return choice(math_operations)


def create_question():
    number_1, number_2 = get_random_number(1, 99), get_random_number(1, 99)
    math_operation = choice_math_operations(number_1, number_2)
    question = f"{number_1} {math_operation[0]} {number_2}"
    right_answer = str(math_operation[1])
    return question, right_answer


def start_game():
    run_game(create_question,
             CALC_INSTRUCTION
             )
