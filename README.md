# AnagramBoa
Anagram finder/solver using recursion and cool tree data structures.

python Boa.py DICTIONARY

---

commit |16176b10658de325aee3fd11ee731fa6a977bdfe
|---| --- |
Author:| whitehaven <accrist@gmail.com>
Date:  | Thu Sep 10 19:49:59 2015 -0600

I've realized I need to convert all lists to tuples for their hashability. Yikes, it's hard to find all the places I used the lists.


---
commit |bda7bd51a545ace58676e20740deda69a5487a42
|---| --- |
Author:| whitehaven <accrist@gmail.com>
Date:  | Thu Sep 10 18:57:01 2015 -0600

One innovation here is that I'm making a set of possibilities for each word in a list indexed by letter position.
    Observe the difference:
        
    Linear:
        try every word from a set made from a dictionary at position ( O(n) for every one! ) ( O(n*m) total )
    
    Tree:
        find in a set[index] ( O(logn) for each one ) ( O(m*logn) total )
            
Anagrams will probably not be permuted in order unless I decide to do that later.