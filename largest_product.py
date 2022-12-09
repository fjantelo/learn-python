# Find the largest product of any two numbers within a given array.

# Input: [5, -2, 1, -9, -7, 2, 6]
# Output: 63 (-9 * -7)

def largest_product(input):
    output = 0
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            product = input[i] * input[j]
            if i != j and product > output:
                output = product
    return output


print(largest_product([5, -2, 1, -9, -7, 2, 6]))
