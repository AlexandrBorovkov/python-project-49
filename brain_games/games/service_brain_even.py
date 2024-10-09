import random
import prompt
from brain_games.games.core import greeting, cycle


def create_question():
    number = random.randint(1, 999)
    return number


def get_user_response():
    return prompt.string("Your answer: ")


def get_right_answer(question):
    return ["yes", "no"][question % 2]


def start_game():
    INDEX_LIST_QUESTIONS = 1
    username = greeting(INDEX_LIST_QUESTIONS)
    cycle(username, create_question, get_user_response, get_right_answer)
