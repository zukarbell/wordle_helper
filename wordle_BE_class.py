from wordle_helper import creat_list_from_txt
import random
import os


class WordleBrain:
    def __init__(self, list_all_words):
        self.all_words = list_all_words
        self.grey_letters = set()
        self.cur_word = [None, None, None, None, None]
        self.yellow_letters = set()

    def input_letter_green(self, given_str):
        # 0 - letter, 1- location
        self.cur_word[int(given_str[1]) - 1] = given_str[0]

    def input_letter_grey(self, iter_of_grey):
        for char in iter_of_grey:
            self.grey_letters.add(char)

    def input_letters_yellow(self, yellow_iter):
        for char in yellow_iter:
            self.yellow_letters.add(char)

    def filter(self):
        filter_green = WordleBrain.bool_green(self.cur_word)
        filter_grey = WordleBrain.bool_grey(self.grey_letters)
        filter_yel = WordleBrain.bool_yellow(self.yellow_letters)
        iter_all_green = filter(filter_green, self.all_words)
        no_grey_with_green = list(filter(filter_grey, list(iter_all_green)))
        no_yel = list(filter(filter_yel, no_grey_with_green))
        self.all_words = no_yel

    def get_rel_words(self):
        return self.all_words

    def get_suggestion(self):
        return random.choice(self.all_words)

    def get_cur_wordle(self):
        wordle = ""
        for char in self.cur_word:
            if char:
                wordle += char
            else:
                wordle += "_"

        return wordle

    @staticmethod
    def bool_green(cur_wordle):
        """
        used as function for filter method. creat an instance with the letters you are sure at the moment and then use the instance in the filter method
        :param cur_wordle: cur word as list - must be in length 5 and letters tou are not sure of should be None
        :return: True if the letters are same, False - if there is a letter the is not correctly placed
        """
        def inner(word_from_all):
            for i in range(5):
                if cur_wordle[i] and cur_wordle[i] != word_from_all[i]:
                    return False
            return True

        return inner

    @staticmethod
    def bool_grey(set_of_greys):
        """
        used to creat a function to use in filter method. the instace should be given an iterable of all the letters that are for sure not in the word
        :param set_of_greys: iterable of all the letters that not in the word
        :return: True - if none of the letters is in the word, False - if one of them is in it
        """
        def inner(word_from_bank):
            for letter in set_of_greys:
                if letter in word_from_bank:
                    return False
            return True

        return inner

    @staticmethod
    def bool_yellow(set_of_yellow):
        """
        check if a given set of yellow letters is in the word
        :param set_of_yellow: set of all the yellow chars
        :return: False - if one of the letters is not in the given word, True - if all the letters are in the word
        """
        def inner(word_from_bank):
            for letter in set_of_yellow:
                if letter not in word_from_bank:
                    return False
            return True

        return inner


def input_green():
    not_finished = True
    list_input = []
    while not_finished:
        cur_input = input("Please enter a green letter and it's location (between 1-5).\n"
          "After finishing, or if you don't have words, type in !\n")
        if cur_input and cur_input != "!" and check_single_green(cur_input):
            list_input.append(cur_input)
        elif cur_input == "!" or len(list_input) == 5:
            print("great, you've finished the input\n\n")
            not_finished = False
        elif not check_single_green(cur_input):
            print("that's not a legal input, do a correct one")
        elif cur_input is None:
            print("you haven't typed anything, if finished type !")

    os.system('cls')
    return list_input


def check_single_green(in_str):
    if len(in_str) == 2:
        letter: str = in_str[:1]
        location: str = in_str[1:]
        if letter.isalpha() and location.isnumeric() and int(location) in range(1, 6):
            return True

    return False


def put_green_to_wordle(list_green, wordle: WordleBrain):
    for element in list_green:
        wordle.input_letter_green(element)


def input_grey_set():
    not_finished = True
    while not_finished:
        cur_input = input("enter a string of all the letters that are grey\n"
                          "if you'll type something that is not a letter, we will ignore it\n"
                          "if you don't know any grey letters, type !")
        if cur_input:
            if cur_input == "!":
                os.system('cls')
                return set()

            set_input = {char for char in cur_input if char.isalpha()}
            os.system('cls')
            return set_input
        else:
            print("you haven't typed anything, try again\n")


def input_yellow_set():
    not_finished = True
    while not_finished:
        cur_input = input("enter a string of all the letters that are yellow\n"
                          "if you'll type something that is not a letter, we will ignore it\n"
                          "if you don't know any yellow letters, type !")
        if cur_input:
            if cur_input == "!":
                os.system('cls')
                return set()

            set_input = {char for char in cur_input if char.isalpha()}
            os.system('cls')
            return set_input
        else:
            print("you haven't typed anything, try again\n")



if __name__ == '__main__':
    all_words = creat_list_from_txt("words_list.txt")  # list of all 5 letters words
    the_helper = WordleBrain(all_words)  # creat an instance of the brain
    list_greens = input_green()  # get all known greens
    put_green_to_wordle(list_greens, the_helper)

    not_finished = True
    while not_finished:
        grey_set = input_grey_set()
        yel_set = input_yellow_set()
        the_helper.input_letter_grey(grey_set)
        the_helper.input_letters_yellow(yel_set)
        # if not grey_set:
        #     break

        the_helper.filter()
        print("try these words:", the_helper.get_rel_words(), "\n")
