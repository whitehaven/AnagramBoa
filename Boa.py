__author__ = 'WhiteHaven'

targetWord = "lormncae"  # subsitute for input() something

visitedLetters = []

# create visitedLetters
for letters in targetWord:
    visitedLetters.append(False)

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
