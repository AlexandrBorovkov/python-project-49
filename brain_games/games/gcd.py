import math
from brain_games.constants import GCD_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def get_numbers_to_find_gcd_and_answer():
    number_1, number_2 = get_random_number(1, 99), get_random_number(1, 99)
    problem_nums = f"{number_1} {number_2}"
    answer = str(math.gcd(number_1, number_2))
    return problem_nums, answer


def start_game():
    run_game(get_numbers_to_find_gcd_and_answer,
             GCD_INSTRUCTION
             )
