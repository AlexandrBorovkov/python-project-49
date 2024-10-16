import math
from brain_games.constants import GCD_INSTRUCTION
from brain_games.core import cycle
from brain_games.utils import get_random_number


def create_question():
    number_1 = get_random_number(1, 99)
    number_2 = get_random_number(1, 99)
    question = f"{number_1} {number_2}"
    right_answer = math.gcd(number_1, number_2)
    return question, right_answer


def start_game():
    cycle(create_question,
          GCD_INSTRUCTION
          )
