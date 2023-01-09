# Ans1.
import os
path = os.path.dirname(__file__)
path = path + '/'
# file = open(path + 'abc.txt', 'r')
# print(file.read())
# data = file.readlines()
# print(len(data))
# print(data[0], data[1])

def firstLinesFromAFile(file, nlines):
    data = file.readlines()
    print(data[:nlines])

def lastLinesFromAFile(file, nlines):
    data = file.readlines()
    lenght = len(data)
    # print(data[lenght-nlines::])

    for i in range(lenght-nlines,lenght):
        print(data[i])

def longestWordsInAFile(file):
    long = 0
    longest_word = []
    data = file.readlines()
    lenght = len(data)
    for i in range(lenght):
        line = data[i].split(" ")
        # print(line)
        for j in range(len(line)):
            if long < len(line[j]):
                long = len(line[j])
                longest_word.clear()
                longest_word.append(line[j])
            elif long == len(line[j]):
                longest_word.append(line[j])
    
    print(longest_word)

file = open(path + 'abc.txt', 'r')
longestWordsInAFile(file)