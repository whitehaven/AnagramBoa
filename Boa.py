__author__ = 'WhiteHaven'

from sys import argv

# take in dictionary file address
script, dictFileAddress = argv

targetWord = "lormncae"  # subsitute for input() something

visitedLetters = []

# create visitedLetters with as many list componenets as letters in targetWord
for letters in targetWord:
    visitedLetters.append(False)

# build dictionary set
dictFile = open(dictFileAddress)
dictionary = set()

tempEntry = dictFile.readline()
while tempEntry != "":
    dictionary.add(tempEntry)
    tempEntry = dictFile.readline()

# build fast dictionary letters-at-position set (list of sets of letters)

# build a temp set, add to list
letterTrees = []
for letter in targetWord:
    tempSet = set()
    letterTrees.append(tempSet)

for dword in dictionary:
    for letter in range(0, len(dword) - 1):
        letterTrees[letter].add(dword[letter])


# TODO main algorithm
# for each starting letter
#   is word(word, index, visitedLetters, wordsSoFar)
#       if letter in dictionary(char)
#           if complete word
#               write to fragment anagrams
#               update to wordsSoFar
#               if on complete word (we know that) and we're out of letters
#                   write to complete anagrams list
#               for all un-visitedLetters
#                   return is word(word, index+1, visitedLetters, wordsSoFar)
#       elif (letters aren't in dictionary)
#           return false
