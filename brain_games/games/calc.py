from random import choice
from brain_games.core import greeting, cycle, get_user_response_integer
from brain_games.utils import get_random_number


def create_question():
    number_1 = get_random_number(1, 99)
    number_2 = get_random_number(1, 99)
    char = choice(["+", "-", "*"])
    return f"{number_1} {char} {number_2}"


def get_right_answer(question):
    return eval(question)


def start_game():
    INDEX_LIST_QUESTIONS = 0
    username = greeting(INDEX_LIST_QUESTIONS)
    cycle(username,
          create_question,
          get_user_response_integer,
          get_right_answer
          )
