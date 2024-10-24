import prompt
from brain_games.constants import NUMBER_OF_ITERATIONS


def run_game(create_question, instruction):
    username = prompt.string("Welcome to the Brain Games!\n"
                             "May I have your name? ")
    print(f"Hello, {username}!")
    print(instruction)
    for _ in range(NUMBER_OF_ITERATIONS):
        question, right_answer = create_question()
        print(f"Question: {question}")
        user_response = prompt.string("Your answer: ")
        if user_response == right_answer:
            print("Correct!")
        else:
            print(
                f"'{user_response}' is wrong answer ;(.",
                f"Correct answer was '{right_answer}'.",
                f"\nLet's try again, {username}!"
            )
            return
    print(f"Congratulations, {username}!")
