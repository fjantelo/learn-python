# Given two strings of equal length, write a function that returns the number of characters that are different between the two strings.

# Input: "ABCDEFG", "ABCXEOG"
# Output: 2

# Explanation: While the A, B, C, E, and G are in the same place for both strings, they have different characters in the other spaces. Since there are 2 such spaces that are different (the D and F in the first string), we return 2.

# Input: "ABCDEFG", "ABCDEFG",
# Output: 0

def hamming(string1, string2):
    output = 0
    index = 0
    for letter in string1:
        if letter != string2[index]:
            output += 1
        index += 1
    return output


print(hamming("ABCDEFG", "ABCXEOG"))

print(hamming("ABCDEFG", "ABCDEFG"))
