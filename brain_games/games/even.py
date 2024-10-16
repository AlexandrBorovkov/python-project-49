from brain_games.core import greeting, cycle, get_user_response_string
from brain_games.utils import get_random_number


def create_question():
    number = get_random_number(1, 999)
    return number


def get_right_answer(question):
    return ["yes", "no"][question % 2]


def start_game():
    INDEX_LIST_QUESTIONS = 1
    username = greeting(INDEX_LIST_QUESTIONS)
    cycle(username,
          create_question,
          get_user_response_string,
          get_right_answer
          )
