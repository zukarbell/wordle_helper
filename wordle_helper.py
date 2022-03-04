import time


def creat_list_from_txt(file_path):
    with open(file_path) as all_words:
        final_list = []
        for word in all_words:
            final_list.append(word.strip())

        return final_list


def input_cur_word():
    word = []
    for i in range(5):
        cur = input("type letter in location " + str(i+1) + " it don't know, do enter")
        if cur:
            word.append(cur)
        else:
            word.append(None)
    print_rel("the word you typed is ", word)
    return word


def print_rel(message, list_chars):
    word = ""
    for char in list_chars:
        if char:
            word += char
        else:
            word += "_"
    print(message + word)


def filter_func_correct_chars(ref_word):
    """
    :param ref_word: as list
    :return:
    """

    def inner(cur_word):
        flag = True
        for i in range(5):
            if ref_word[i] and ref_word[i] != cur_word[i]:
                flag = False
        return flag

    return inner


if __name__ == '__main__':
    all_words = creat_list_from_txt("words_list.txt")
    cur_word = input_cur_word()
    cur_filter = filter_func_correct_chars(cur_word)
    new_list = filter(cur_filter, all_words)
    print("possible words", list(new_list))
    time.sleep(15)