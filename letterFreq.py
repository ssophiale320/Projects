"""
CSCI-141 Project

File name: letterFreq.py

Author: Sophia Le
"""
import wordData
import matplotlib.pyplot as plt


def letterFreq(words):
    """
    Computes the relative letter frequency of all 26 English letters across
    all the word data provided
    :param words: a dictionary mapping words to dictionaries with years and
    counts
    :return: a string containing the 26 lowercase letters of the English
    alphabet, sorted in decreasing order of frequency of occurrence of
    each character
    """
    letters = dict()
    lst = []
    result = ''
    for word in words:
        for l in word:
            if l not in letters:
                letters[l] = 0
            letters[l] += wordData.totalOccurrences(word, words)
    for key in letters:
        lst.append((key, letters[key]))
    lst2 = sorted(lst, key=lambda x: x[1], reverse=True)
    for m in range(len(lst2)):
        result += lst2[m][0]
    return result


def data(words):
    """
    builds a dictionary containing all 26 letters of the English alphabet
    (lowercase) as well as the counts of each letter across all years
    :param words: a dictionary mapping words to dictionaries with years
    and counts
    :return: a dictionary containing 26 letters of the English alphabet
    as keys and the total amount of times each letter has appeared in
    print as values
    """
    count = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        count[letter] = 0
    for word in words:
        for letter in word:
            count[letter] += wordData.totalOccurrences(word, words)
    return count


def main():
    """
    prompts the user for an input data file, prints a string
    containing 26 lowercase English letters ranked by decreasing order
    of frequency, and plots the counts' distribution
    """
    file = input('enter a file: ')
    words = wordData.readWordFile(file)
    frequency = letterFreq(words)
    print('letters sorted by decreasing frequency: ' + frequency)
    counts = data(words)
    plt.bar(list(counts.keys()), list(counts.values()), color='skyblue')
    plt.show()


if __name__ == '__main__':
    # run main() only when directly invoking this module
    main()
# end of program file
