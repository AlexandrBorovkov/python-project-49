from brain_games.constants import PRIME_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_problem_number_and_answer():
    problem_num = get_random_number(1, 99)
    answer = "yes" if is_prime(problem_num) else "no"
    return problem_num, answer


def start_game():
    run_game(get_problem_number_and_answer,
             PRIME_INSTRUCTION
             )
