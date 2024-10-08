import prompt
import random


def start_game():
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
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
        len_list = random.randint(5, 10)
        start = random.randint(11, 99)
        step = random.randint(2, 9)
        stop = (len_list - 1) * step + start + 1
        index = random.randint(0, len_list - 1)
        result_list = [str(x) for x in range(start, stop, step)]
        right_answer = result_list[index]
        result_list[index] = ".."
        print(f"Question: {" ".join(result_list)}")
        user_response = prompt.string("Your answer: ")
        if user_response == right_answer:
            print("Correct!")
            counter -= 1
        else:
            output_wrong_answer(user_response, right_answer, username)
            return
    print(f"Congratulations, {username}!")
