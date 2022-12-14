# Write a function that returns the sum of all numbers in a given array.

# NOTE: Do not use any built-in language functions that do this automatically for you.

# Input: [1, 2, 3, 4]
# Output: 10

# Explanation: (1 + 2 + 3 + 4) = 10


def reduce_sum(input):
    output = 0
    for number in input:
        output += number
    return output


print(reduce_sum([1, 2, 3, 4]))
