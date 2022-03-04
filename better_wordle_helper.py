from wordle_helper import *


def change_input_to_list(given_str):
    word = []
    if not given_str:
        return [None] * 5
    for char in given_str:
        if char == " ":
            word.append(None)
        else:
            word.append(char)

    return word


def check_input(given_list):
    print("you typed", given_list)
    desicion = input("if correct, press y, else press something else")
    if desicion == "y":
        return False
    else:
        return True


def filter_func_not_in_word(letters_not):
    """
    :param ref_word: as list
    :return:
    """

    def inner(cur_word):
        for char in letters_not:
            if char in cur_word:
                return False
        return True

    return inner




if __name__ == '__main__':
    all_words = creat_list_from_txt("words_list.txt")

    # input sequence
    no_input = True
    while no_input:
        start = input("type what you got")
        input_list = change_input_to_list(start)
        while len(input_list) < 5:
            input_list.append(None)
        no_input = check_input(input_list)

    cur_filter = filter_func_correct_chars(input_list)
    new_list_of_words = list(filter(cur_filter, all_words))
    print("possible words", new_list_of_words)



    while True:
        letters_not_str = input("type the letters that are for sure not in the word")
        letters_not_lst = change_input_to_list(letters_not_str)
        new_filter = filter_func_not_in_word(letters_not_lst)
        latest_lst = list(filter(new_filter, new_list_of_words))
        print("possible words", latest_lst)
        new_list_of_words = latest_lst
    # print(all_words)