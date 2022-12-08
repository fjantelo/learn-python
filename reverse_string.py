# Write a function that returns the reverse of a given string.

# Input: “abcde”
# Output: “edcba”

def reverse_string(input):
    output = ""
    index = len(input) - 1
    while index >= 0:
        output = output + input[index]
        index -= 1
    return output


print(reverse_string("abcde"))
