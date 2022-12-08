# Write a function that accepts an array of numbers and returns the product of all the numbers.

# Input: [1, 2, 3, 4]
# Output: 24

# Explanation: (1 x 2 x 3 x 4) = 24

def reduce_product(input):
    output = 1
    for number in input:
        output *= number
    return output


print(reduce_product([1, 2, 3, 4]))
