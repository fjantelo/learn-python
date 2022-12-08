# Given a string of words, write a function that returns a new string that contains the words in reverse order.

# Input: “popcorn is so cool isn’t it yeah i thought so”
# Output: “so thought i yeah it isn’t cool so is popcorn”

def reverse_words(input):
    output = ""
    words = input.split()
    index = len(words) - 1
    while index >= 0:
        if index != 0:
            output += words[index] + " "
        else:
            output += words[index]
        index -= 1
    return output


print(reverse_words("popcorn is so cool isn’t it yeah i thought so"))
