from brain_games.constants import EVEN_INSTRUCTION
from brain_games.core import run_game
from brain_games.utils import get_random_number


def get_right_answer(question):
    return "yes" if question % 2 == 0 else "no"


def create_question():
    question = get_random_number(1, 999)
    right_answer = get_right_answer(question)
    return question, right_answer


def start_game():
    run_game(create_question,
             EVEN_INSTRUCTION
             )
