"""
CSCI-141 Project

File name: wordSimilarity.py

Author: Sophia Le
"""
import math
import wordData

def topSimilar(words, target_word):
    """
    finds the top 5 most similar words for a given target word across
    all words
    :param words: a dictionary mapping words to dictionaries with years and
    counts
    :param target_word: a string representing a word used to find similar
    words
    :return: a list of the top five words including the input word in
    descending order of similarity
    """
    new_words = {}
    for word in words:
        years = words[word]
        counts = []
        sums = 0
        for i in words[word]:
            sums += words[word][i] ** 2
        norm = math.sqrt(sums)
        for j in words[word]:
            words[word][j] = float(words[word][j] / norm)
        for year in years:
            counts.append(years[year])
        new_words[word] = counts
    target_vector = new_words[target_word]
    similarities = []
    for w in new_words:
        compare_vector = new_words[w]
        dot_product = 0
        for i in range(len(target_vector)):
            dot_product += target_vector[i] * compare_vector[i]
        similarities.append((w, dot_product))
    sim = sorted(similarities, key=lambda x:x[1], reverse=True)
    final_list = []
    for s in sim[0:5]:
        final_list.append(s[0])
    return final_list


def main():
    """
    prompts the user for a filename and a word, then calculates the top
    5 most similar words to the user-given word and outputs them to the
    terminal
    """
    file = input('enter a file: ')
    words = wordData.readWordFile(file)
    word = input('enter a word: ')
    similarity = topSimilar(words, word)
    print('The most similar words are: ')
    print(similarity)


if __name__ == '__main__':
    # run main() only when directly invoking this module
    main()
# end of program file
