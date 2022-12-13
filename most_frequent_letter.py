# Given a string, find the most commonly occurring letter.

# Input: “peter piper picked a peck of pickled peppers”
# Output: “p”

def most_frequent_letter(input):
    letter_count = {}
    for letter in input:
        if (letter in letter_count):
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return max(letter_count, key=letter_count.get)


print(most_frequent_letter("peter piper picked a peck of pickled peppers"))
