# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: “silent”, “listen”
# Output: true

# Input: “frog”, “bear”
# Output: false

def anagrams(word1, word2):
    count1 = {}
    count2 = {}
    for letter in word1:
        if (letter in count1):
            count1[letter] += 1
        else:
            count1[letter] = 1
    for letter in word2:
        if (letter in count2):
            count2[letter] += 1
        else:
            count2[letter] = 1
    if count1 == count2:
        return True
    else:
        return False


print(anagrams("silent", "listen"))
print(anagrams("frog", "bear"))
