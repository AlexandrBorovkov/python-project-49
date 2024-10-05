import prompt


def welcome_user():
    print("brain-games", "Welcome to the Brain Games!", sep="\n")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")



