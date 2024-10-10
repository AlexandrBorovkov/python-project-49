import random
import prompt
from brain_games.games.core import greeting, cycle


def create_question():
    number = random.randint(1, 999)
    return number


def get_user_response():
    return prompt.string("Your answer: ")


def get_right_answer(question):
    result = len([x for x in range(1, question // 2 + 1) if question % x == 0])
    if result == 1:
        return "yes"
    return "no"


def start_game():
    INDEX_LIST_QUESTIONS = 3
    username = greeting(INDEX_LIST_QUESTIONS)
    cycle(username, create_question, get_user_response, get_right_answer)
