# Given an array, write a function that returns an array that contains the original array’s values in reverse.

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

def reverse_array(input):
    output = []
    for number in input:
        output.insert(0, number)
    return output


print(reverse_array([1, 2, 3, 4, 5]))
