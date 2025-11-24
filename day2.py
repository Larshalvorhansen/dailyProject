# [x] Create a program that analyzes text files to find word frequency distributions
# [x] and export results to CSV.
# [ ] Include functionality to find the most common words and basic statistics.

import csv


def makeOccuranceDict(text):
    text = text.lower()
    words = text.split()
    occuranceDict = {}
    # print(words)
    for word in words:
        instance = words.count(word)
        occuranceDict[word] = instance
    return occuranceDict


def dict2csv(dict):
    with open("occs.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for x, y in dict.items():
            # print(x, y)
            writer.writerow([x, y])
    return 0


def countWords(text):
    text = text.lower()
    words = text.split()
    return len(words)


def getMostCommonWord(text):
    occDict = makeOccuranceDict(text)
    largestOcc = 0
    word = "none"
    for x, y in occDict.items():
        if y > largestOcc:
            largestOcc = y
            word = x
    return (word, largestOcc)


text = "Hei hvordan går det med deg hei hei ;)"
print(makeOccuranceDict(text))
dict2csv(makeOccuranceDict(text))
print(countWords(text))
print(getMostCommonWord(text))
