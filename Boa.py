__author__ = 'WhiteHaven'

from sys import argv

# take in dictionary file address
script, dictFileAddress = argv

targetWord = "cormnlae"  # subsitute for input() something

visited_letters = []

# create visitedLetters with as many list componenets as letters in targetWord
for letters in targetWord:
    visited_letters.append(False)

# TODO rebuild dictionary set to evade \n issue
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
    if word[index] in letterTrees[len(word_so_far)]:
        # add letter onto new word (must create new one because strings are immutable)
        new_word_so_far = word_so_far + word[index]

        # make new visited letters list to support recursion
        new_visited_letters = list(visited_letters)
        # mark visited_letters
        new_visited_letters[index] = True

        if new_word_so_far in dictionary:
            new_words_so_far = list(words_so_far)
            new_words_so_far.append(new_word_so_far)
            partialAnagrams.append(new_word_so_far)

            # if there's no False record in visited_letters, we're at the end
            if not (False in new_visited_letters):
                completeAnagrams.append(new_words_so_far)
        for index in range(0, len(new_visited_letters)):
            if new_visited_letters[index] == False:  # if unvisited, send function there
                isWord(word, index, new_word_so_far, new_visited_letters, words_so_far)
    return False


# TODO main algorithm
# for each starting letter
for letter in range(0, len(targetWord)):
    isWord(targetWord, letter, "", visited_letters, [])


# write output

print("Partial Anagrams:\t %d" % (len(partialAnagrams)))
if len(partialAnagrams) == 0:
    print("None")
else:
    for element in range(0, len(partialAnagrams)):
        print("%d\t%s" % (element + 1, partialAnagrams[element]))

print("Complete Anagrams:\t %d" % (len(completeAnagrams)))
if len(completeAnagrams) == 0:
    print("None")
else:
    for element in range(0, len(completeAnagrams)):
        print("%d\t%s" % (element + 1, completeAnagrams[element]))
