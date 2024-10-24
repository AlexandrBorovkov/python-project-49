from brain_games.constants import EVEN_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def is_even(number):
    return number % 2 == 0


def get_problem_number_and_answer():
    problem_num = get_random_number(1, 999)
    answer = "yes" if is_even(problem_num) else "no"
    return problem_num, answer


def start_game():
    run_game(get_problem_number_and_answer,
             EVEN_INSTRUCTION
             )
