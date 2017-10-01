# -----------------------------------------------------------------------------
# Name:    wordstats
#
# Author:  Pavlos P
# Date:    10/25/2016
# -----------------------------------------------------------------------------
"""
The program computes some language statistics based on the contents of a file

It searches for the longest word used in the file.
The five most common words in the file with the number of times they appear
The word count of all the words in the file, sorted alphabetically
And the output of the words writen in a new file
"""

import string
import tkinter
import tkinter.font
import random
import os.path


def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
    minimum length of the words that will appear
    in the cloud representation
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """

    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    my_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=my_row % 5, column=my_row // 5)
        my_row += 1
    root.mainloop()


def find_longest_word(words):
    """
    this function finds and prints the longest words in the dictionary

    :param words:(dictionary)
    """

    longest_word = max(words, key=len)
    all_long_words = []

    max_length = len(longest_word)
    for word in words:

        if len(word) == max_length:
            all_long_words.append("The longest word is:  " + word)

    print("\n\nor:\n\n".join(all_long_words))


def count_words(filename):
    """
    this function builds and returns a dictionary for a given filename

    :param filename:(string)
    :return: word_count (the dictionary for the given filename)
    """

    word_count = {}
    with open(filename, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            words = line.split()
            for word in words:

                word = word.strip(string.punctuation + string.digits).lower()

                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1

    return word_count


def find_common_words(frequency_list, word_count, TARGET):
    """
    this function finds the five most common with the times they appear in the file

    :param frequency_list:(dictionary)
    :param word_count:(dictionary)
    :param TARGET:(integer)
    """

    counter = 0

    for letter in frequency_list:
        counter += 1
        if counter <= TARGET:
            print(letter + ':', word_count[letter])


def report(word_count):
    """"
     this function reports various statistics based on the given word count dictionary

     :param word_count(dictionary)
     """

    find_longest_word(word_count)

    frequency_list = sorted(word_count, key=word_count.get, reverse=True)

    TARGET = 5
    print("The 5 most common words are:")
    find_common_words(frequency_list, word_count, TARGET)


def write_to_file(words, file_name):
    """
    this function writes alphabetically all the words in a file

    :param words(dictionary)
    :param filename(string)
    """
    with open(file_name, 'w') as new_file:
        for key, value in sorted(words.items()):
            new_file.write('%s:%s\n' % (key, value))


def get_input(prompt):
    """
    this function asks the user for a file name that exists

    it gives the user three times to repeat, in case they typed wrong file name
    then fourth time the user types a wrong entry, the program exits

    :param :prompt(string)
    :return:the file name(string)
    """

    reenter = True
    chances = 0
    while reenter:

        file_name = input(prompt)
        if os.path.exists(file_name):
            reenter = False
            return file_name
        elif chances == 2:
            print("\t\tOne more try")

        if chances == 3:
            reenter = False
            exit(0)
        else:
            chances += 1
            print("This file does not exist...")


def main():
    prompt = "Please enter the file name :"
    file_name = get_input(prompt)
    word_count = count_words(file_name)
    report(word_count)

    file_name = input("Now write data to a file\n" + prompt)
    write_to_file(word_count, file_name)
    # draw_cloud(word_count)


if __name__ == '__main__':
    main()
