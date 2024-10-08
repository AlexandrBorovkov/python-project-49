import prompt
import random


def start_game():
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return username


def output_wrong_answer(user_response, right_answer, username):
    print(
        f"'{user_response}' is wrong answer ;(.",
        f"Correct answer was '{right_answer}'.",
        f"\nLet's try again, {username}!",
        sep=" "
    )


def check_number(num):
    result = len([x for x in range(1, num // 2 + 1) if num % x == 0])
    if result == 1:
        return "yes"
    return "no"


def answer_processing(username):
    counter = 3
    while counter > 0:
        number = random.randint(1, 99)
        print(f"Question: {number}")
        user_response = prompt.string("Your answer: ")
        right_answer = check_number(number)
        if user_response == right_answer:
            print("Correct!")
            counter -= 1
        else:
            output_wrong_answer(user_response, right_answer, username)
            return
    print(f"Congratulations, {username}!")
