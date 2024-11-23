"""
CSCI-141 Project

File name: wordData.py

Author: Sophia Le
"""


def readWordFile(filename):
    """
    reads a file from the data directory and returns a dictionary of words
    that each contain years as keys and counts as values
    :param filename: a string giving the name of a unigram data file, assumes
    that the provided filename belongs to a file in the data directory
    :return: a dictionary mapping words to dictionaries; the inner dictionary
    associated with each word will use years as keys and counts as values
    """
    dictionary = dict()
    with open('data/' + filename) as file:
        for line in file:
            word = line.strip().split(',')
            if len(word) == 1:
                new_word = word[0]
                dictionary[new_word] = {}
                for year in range(1900, 2009):
                    dictionary[new_word][year] = 0
            elif len(word) == 2:
                year = int(word[0])
                dictionary[new_word][year] = int(word[1])
    return dictionary


def totalOccurrences(word, words):
    """
    computes the amount of times a word has appeared in print across all
    years
    :param word: a string representing the word for which to calculate
    the count, not guaranteed to exist in words
    :param words: a dictionary mapping words to dictionaries with years and
    counts
    :return: an integer representing the total number of times the given
    word has appeared in print
    """
    count = 0
    for year in words[word]:
        count += words[word][year]
    return count


def main():
    """
    prompts the user for an input data file, then prompts for a word to count
    and outputs the total occurrences of that word in the user-given data file
    """
    file = input('enter a file: ')
    words = readWordFile(file)
    word = input('enter a word to count: ')
    count = totalOccurrences(word, words)
    print('total occurrences of ' + word + ': ' + str(count))


if __name__ == '__main__':
    # run main() only when directly invoking this module
    main()
# end of program file
