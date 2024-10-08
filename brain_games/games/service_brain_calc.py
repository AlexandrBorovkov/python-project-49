import prompt
import random

from simpleeval import simple_eval


def start_game():
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")
    print("What is the result of the expression?")
    return username


def output_wrong_answer(user_response, right_answer, username):
    print(
        f"'{user_response}' is wrong answer ;(.",
        f"Correct answer was '{right_answer}'.",
        f"\nLet's try again, {username}!",
        sep=" "
    )


def answer_processing(username):
    counter = 3
    while counter > 0:
        number_1 = random.randint(1, 99)
        number_2 = random.randint(1, 99)
        char = random.choice(["+", "-", "*"])
        expression = f"{number_1} {char} {number_2}"
        print(f"Question: {expression}")
        user_response = prompt.string("Your answer: ")
        right_answer = simple_eval(expression)
        try:
            user_response = int(user_response)
        except ValueError:
            output_wrong_answer(user_response, right_answer, username)
            return
        if user_response == right_answer:
            print("Correct!")
            counter -= 1
        else:
            output_wrong_answer(user_response, right_answer, username)
            return
    print(f"Congratulations, {username}!")
