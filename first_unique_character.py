# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Examples:

# s = "leetcode"
# return 0.
# (The "l" is the first character that only appears once in the string, and appears at index 0.)

# s = "loveleetcode",
# return 2.
# (The "l" and "o" are repeated, so the first non-repeating character is the "v", which is at index 2.)

# Note: You may assume the string contain only lowercase letters.

def unique_character(input):
    characters = {}
    output = -1
    index = 0
    for letter in input:
        if letter in characters.keys():
            characters[letter] = ""
        else:
            characters[letter] = index
        index += 1
    for v in characters.values():
        if type(v) == int:
            output = v
            break
    return output


print(unique_character("leetcode"))
print(unique_character("loveleetcode"))
