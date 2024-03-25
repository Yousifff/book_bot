from collections import Counter

def read_file(fname):
    with open(fname,'r') as readFile:
        for line in readFile:
            yield line


def count_words(text):
    total = 0
    for line in text:
        total += len(line.split())
    return total


def count_letters(text):
    counter = {}
    for line in text:
        for letter in line:
            if letter.lower().isalpha():
                if letter.lower() not in counter:
                    counter[letter.lower()] = 1
                else:
                    counter[letter.lower()] += 1
    return counter
