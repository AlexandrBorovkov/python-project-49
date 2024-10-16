from brain_games.core import greeting, cycle, get_user_response_integer
from brain_games.utils import get_random_number


def create_question():
    len_list = get_random_number(5, 10)
    start = get_random_number(11, 99)
    step = get_random_number(2, 9)
    stop = (len_list - 1) * step + start + 1
    index = get_random_number(0, len_list - 1)
    result_list = [str(x) for x in range(start, stop, step)]
    result_list[index] = ".."
    return " ".join(result_list)


def get_right_answer(question):
    lst_nums = [x if x == ".." else int(x) for x in question.split()]
    index_char = lst_nums.index("..")
    if index_char == 0:
        return lst_nums[index_char + 1] - \
            (lst_nums[index_char + 2] - lst_nums[index_char + 1])
    if index_char == len(lst_nums) - 1:
        return lst_nums[index_char - 1] + \
            (lst_nums[index_char - 1] - lst_nums[index_char - 2])
    if 0 < index_char < len(lst_nums) - 1:
        return lst_nums[index_char - 1] + \
            (lst_nums[index_char + 1] - lst_nums[index_char - 1]) // 2


def start_game():
    INDEX_LIST_QUESTIONS = 4
    username = greeting(INDEX_LIST_QUESTIONS)
    cycle(username,
          create_question,
          get_user_response_integer,
          get_right_answer
          )
