__author__ = 'WhiteHaven'

from sys import argv

# take in dictionary file address
script, dictFileAddress = argv

targetWord = "lormncae"  # subsitute for input() something

visited_letters = []

# create visitedLetters with as many list componenets as letters in targetWord
for letters in targetWord:
    visited_letters.append(False)

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

partialAnagrams = []
completeAnagrams = []


# TODO write recursive isWord() function
#   is word(word, index, visitedLetters, visited_letters, wordsSoFar)
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

def isWord(word, index, word_so_far, visited_letters, words_so_far):
    if word[index] in letterTrees[index]:
        # add letter onto new word (must create new one because strings are immutable)
        new_word_so_far = word_so_far + word[index]

        # mark visited_letters
        visited_letters[index] = True

        if new_word_so_far in dictionary:
            words_so_far.append(new_word_so_far)
            partialAnagrams.append(new_word_so_far)

            # if there's no False record in visited_letters, we're at the end
            if not (False in visited_letters):
                completeAnagrams.append(words_so_far)
        for letter in visited_letters:
            if letter == True:
                isWord(word, index + 1, new_word_so_far, visited_letters, words_so_far)
    return False


# TODO main algorithm
# for each starting letter
for letter in range(0, len(targetWord) - 1):
    isWord(targetWord, letter, "", visited_letters, [])
