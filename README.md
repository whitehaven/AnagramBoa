# AnagramBoa
Anagram finder/solver using recursion and cool tree data structures.

One innovation here is that I'm making a set of possibilities for each word in a list indexed by letter position.
    Observe the difference:
        Linear:
            try every word from a set made from a dictionary at position ( O(n) for every one! ) ( O(n*m) total )
        
        Tree:
            find in a set[index] ( O(logn) for each one ) ( O(m*logn) total )