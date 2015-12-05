__author__ = 'WhiteHaven'

from sys import argv

# take in dictionary file address
script, dictFileAddress = argv

targetWord = "donaldtrump"  # subsitute for input() something

visited_letters = []

# create visitedLetters with as many list components as letters in targetWord
for letters in targetWord:
    visited_letters.append(False)

dictionary = set()

with open(dictFileAddress, "r+") as dictFile:
    dictionary.update(dictFile.read().splitlines())

# build fast dictionary letters-at-position set (list of sets of letters)

letterTrees = []
for letter in targetWord:
    # build a temp set, add to list
    tempSet = set()
    letterTrees.append(tempSet)

for dword in dictionary:
    for letter in range(0, len(dword)):
        letterTrees[letter].add(dword[letter])


partialAnagrams = set()
completeAnagrams = set()

# V2 algorithm
"""
presupposes list of sets

current_word string
current_words tuple
partialAnagrams set of tuples

completeAnagrams set of tuples

isWord()
    if letter is a possible permutation (then we know a word could come of it)
        if letter completes a word
            push to this most recent word into this round's tuple of words
            push new tuple of words to partialAnagrams
            if letter was the last one (and they're all used)
                push new tuple of words to completeAnagrams
        either way, send isWord to all remaining letters
    else ( letter is not possible )
        return false ( unwind recursion )
"""

def isWord(word, index, word_so_far, visited_letters, words_so_far):
    if word[index] in letterTrees[len(word_so_far)]:
        # add letter onto new word (must create new one because strings are immutable)
        new_word_so_far = word_so_far + word[index]

        # make new visited letters list to support recursion
        new_visited_letters = list(visited_letters)
        # mark visited_letters
        new_visited_letters[index] = True

        if new_word_so_far in dictionary:
            # write (words so far & new word) to new words (tuple) so far to continue to next word
            new_words_so_far = words_so_far + (new_word_so_far,)
            # write (words so far (may be () ) and new word to anagrams)
            partialAnagrams.update({tuple(sorted(new_words_so_far))})

            # branch, assuming that first word, to view the next letter as part of the next word
            for index in range(0, len(new_visited_letters)):
                if new_visited_letters[index] == False:
                    isWord(word, index, "", new_visited_letters, new_words_so_far)

            # if there's no False record in visited_letters, we're at the end
            if not (False in new_visited_letters):
                completeAnagrams.update({tuple(sorted(new_words_so_far))})
        else:
            new_words_so_far = words_so_far

        for index in range(0, len(new_visited_letters)):
            if new_visited_letters[index] == False:  # if unvisited, send function there
                isWord(word, index, new_word_so_far, new_visited_letters, new_words_so_far)
    return False


# main algorithm
# for each starting letter
for letter in range(0, len(targetWord)):
    isWord(targetWord, letter, "", visited_letters, ())


# write output

print("Partial Anagrams:\t %d" % (len(partialAnagrams)))
if len(partialAnagrams) == 0:
    print("None")
else:
    for each_entry in partialAnagrams:
        for word in each_entry:
            print("%s" % (word))
        print()

print("Complete Anagrams:\t %d" % (len(completeAnagrams)))
if len(completeAnagrams) == 0:
    print("None")
else:
    for each_entry in completeAnagrams:
        for word in each_entry:
            print("%s" % (word))
        print()
