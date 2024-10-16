import random
import math
from brain_games.core import greeting, cycle, get_user_response_integer


def create_question():
    number_1 = random.randint(1, 99)
    number_2 = random.randint(1, 99)
    return f"{number_1} {number_2}"


def get_right_answer(question):
    number_1, number_2 = [int(x) for x in question.split()]
    return math.gcd(number_1, number_2)


def start_game():
    INDEX_LIST_QUESTIONS = 2
    username = greeting(INDEX_LIST_QUESTIONS)
    cycle(username,
          create_question,
          get_user_response_integer,
          get_right_answer
          )
