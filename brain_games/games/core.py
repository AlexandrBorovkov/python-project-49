import prompt


def greeting(index):
    list_questions = ["What is the result of the expression?"]
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")
    print(list_questions[index])
    return username


def output_wrong_answer(user_response, right_answer, username):
    print(
        f"'{user_response}' is wrong answer ;(.",
        f"Correct answer was '{right_answer}'.",
        f"\nLet's try again, {username}!",
        sep=" "
    )



def cycle(username, create_question, get_user_response, get_right_answer):
    counter = 3
    while counter > 0:
        question = create_question()
        print(f"Question: {question}")
        user_response = get_user_response()
        right_answer = get_right_answer(question)
        
        if user_response == right_answer:
            print("Correct!")
            counter -= 1
        else:
            output_wrong_answer(user_response, right_answer, username)
            return
    print(f"Congratulations, {username}!")
