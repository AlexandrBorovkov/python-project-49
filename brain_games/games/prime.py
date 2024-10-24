from brain_games.constants import PRIME_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def get_right_answer(question):
    result = len([x for x in range(1, int(question ** 0.5 + 1))
                  if question % x == 0])
    if result == 1:
        return "yes"
    return "no"


def create_question():
    question = get_random_number(1, 99)
    right_answer = get_right_answer(question)
    return question, right_answer


def start_game():
    run_game(create_question,
             PRIME_INSTRUCTION
             )
