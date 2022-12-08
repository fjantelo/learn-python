# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

def map_double(input):
    output = []
    for number in input:
        output.append(number * 2)
    return output


print(map_double([4, 2, 5, 99, -4]))
