# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    word1 = sorted(word1)
    word2 = sorted(word2)
    check = word1 == word2
    return (check)

