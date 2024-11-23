"""
CSCI-141 Project

File name: printedWords.py

Author: Sophia Le
"""
import wordData
import matplotlib.pyplot as plt


def printedWords(words):
    """
    computes the total number of printed words for each year
    :param words: a dictionary mapping words to dictionaries with years
    and counts
    :return: a list, sorted in ascending order of years, containing
    tuples (year, count_total_words) for each year for which data exists
    """
    counts = {}
    for word in words:
        for year in words[word]:
            if year not in counts:
                counts[year] = 0
            counts[year] += words[word][year]
    lst = sorted(counts.items(), key=lambda x: x[0], reverse=False)
    return lst


def wordsForYear(year, yearList):
    """
    Computes the total amount of printed words for a specified year
    :param year: an integer representing the year being queried
    :param yearList: a list, sorted in ascending order of years, containing
    tuples (year, count_total_words) for each year for which data exists
    :return: an integer representing the total number of printed words
    for that year; if there is no entry in yearList for the requested
    year, the function returns 0
    """
    count = 0
    for item in yearList:
        if item[0] == year:
            count += item[1]
    return count


def main():
    """
    prompts the user for an input data file, prompts the user for a year
    to count, outputs the total number of printed words in that year, and
    plots the distribution of total printed words across all years
    """
    file = input('enter a file: ')
    words = wordData.readWordFile(file)
    years_list = printedWords(words)
    year = int(input('enter a year: '))
    count = wordsForYear(year, years_list)
    print('total printed words in ' + str(year) + ': ' + str(count))
    y = []
    c = []
    for i in range(len(years_list)):
        y.append(years_list[i][0])
    for j in range(len(years_list)):
        c.append(years_list[j][1])
    plt.plot(y, c)
    plt.show()


if __name__ == '__main__':
    # run main() only when directly invoking this module
    main()
# end of program file
