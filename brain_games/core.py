import prompt


def greeting(instruction):
    username = prompt.string("Welcome to the Brain Games!\n"
                             "May I have your name? ")
    print(f"Hello, {username}!")
    print(instruction)
    return username


def output_wrong_answer(user_response, right_answer, username):
    print(
        f"'{user_response}' is wrong answer ;(.",
        f"Correct answer was '{right_answer}'.",
        f"\nLet's try again, {username}!",
        sep=" "
    )


def get_user_response_integer():
    return prompt.integer("Your answer: ")


def get_user_response_string():
    return prompt.string("Your answer: ")


def cycle(create_question, instruction):
    username = greeting(instruction)
    counter = 3
    while counter > 0:
        question, right_answer = create_question()
        print(f"Question: {question}")
        if isinstance(right_answer, int):
            user_response = get_user_response_integer()
        else:
            user_response = get_user_response_string()
        if user_response == right_answer:
            print("Correct!")
            counter -= 1
        else:
            output_wrong_answer(user_response, right_answer, username)
            return
    print(f"Congratulations, {username}!")
