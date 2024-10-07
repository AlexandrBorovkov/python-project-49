import prompt
import random


def start_game():
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return username


def answer_processing(username):
    counter = 3
    while counter > 0:
        number = random.randint(1, 999)
        print(f"Question: {number}")
        user_response = prompt.string("Your answer: ")
        right_answer = ["yes", "no"][number % 2]
        if user_response == right_answer:
            print("Correct!")
            counter -= 1
        else:
            print(
                f"'{user_response}' is wrong answer ;(.",
                f"Correct answer was '{right_answer}'.",
                f"\nLet's try again, {username}!",
                sep=" "
            )
            return
    print(f"Congratulations, {username}!")
