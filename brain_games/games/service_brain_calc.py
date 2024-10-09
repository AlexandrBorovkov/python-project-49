import random
import prompt
from simpleeval import simple_eval
from brain_games.games.core import greeting, cycle


def create_question():
    number_1 = random.randint(1, 99)
    number_2 = random.randint(1, 99)
    char = random.choice(["+", "-", "*"])
    return f"{number_1} {char} {number_2}"


def get_user_response():
    return prompt.integer("Your answer: ")


def get_right_answer(question):
    return simple_eval(question)


def start_game():
    INDEX_LIST_QUESTIONS = 0
    username = greeting(INDEX_LIST_QUESTIONS)
    cycle(username, create_question, get_user_response, get_right_answer)
