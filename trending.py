"""
CSCI-141 Project

File name: trending.py

Author: Sophia Le
"""
import wordData

def trending(words, year1, year2):
    """
    computes the top and bottom trending words between a given start and
    end year
    :param words: a dictionary mapping words to dictionaries with years and
    counts
    :param year1: an integer representing the starting year
    :param year2: an integer representing the end year
    :return: a list containing a tuple (word, trend) entry for each word for
    which qualifying data exists; the list is sorted in decreasing trend value
    """
    lst = []
    for word in words:
        if year1 in words[word] and year2 in words[word]:
            start = words[word][year1]
            end = words[word][year2]
            if start >= 1000 and end >= 1000:
                trend = float(end / start)
                lst.append((word, trend))
    trends = sorted(lst, key=lambda x:x[1], reverse=True)
    return trends

def main():
    """
    prompts the user for an input data file, then prompts the user for a
    start and end year, then outputs the top and bottom 10 trending words
    in that timespan
    """
    file = input('enter a file: ')
    words = wordData.readWordFile(file)
    s = int(input('enter a start year: '))
    e = int(input('enter an end year: '))
    trends = trending(words, s, e)
    top = []
    for item in trends:
        top.append(item[0])
    print('The top 10 trending words from ' + str(s) + ' to ' + str(e) + ' :')
    for i in top[0:10]:
        print(i)
    print()
    print('The bottom 10 trending words from ' + str(s) + ' to ' + str(e) + ' :')
    for j in top[len(top):-11:-1]:
        print(j)

if __name__ == '__main__':
    # run main() only when directly invoking this module
    main()
# end of program file