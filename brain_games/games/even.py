from brain_games.constants import EVEN_INSTRUCTION
from brain_games.core import cycle
from brain_games.utils import get_random_number


def create_question():
    question = get_random_number(1, 999)
    right_answer = ["yes", "no"][question % 2]
    return question, right_answer


def start_game():
    cycle(create_question,
          EVEN_INSTRUCTION
          )
