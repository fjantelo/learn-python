# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

# Input: “abcdefghhijkkloooop”
# Output: “h”

def first_duplicate_character(input):
    count = {}
    output = ""
    for letter in input:
        if (letter in count):
            count[letter] += 1
        else:
            count[letter] = 1
        if count[letter] > 1:
            output = letter
            break
    return output


print(first_duplicate_character("abcdefghhijkkloooop"))
