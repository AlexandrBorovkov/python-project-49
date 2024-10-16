from brain_games.core import greeting, cycle, get_user_response_string
from brain_games.utils import get_random_number


def create_question():
    number = get_random_number(1, 99)
    return number


def get_right_answer(question):
    result = len([x for x in range(1, int(question ** 0.5 + 1)) if question % x == 0])
    if result == 1:
        return "yes"
    return "no"


def start_game():
    INDEX_LIST_QUESTIONS = 3
    username = greeting(INDEX_LIST_QUESTIONS)
    cycle(username,
          create_question,
          get_user_response_string,
          get_right_answer
          )
