# Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.

# Input: [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]

def select_less_than_100(input):
    output = []
    for number in input:
        if number < 100:
            output.append(number)
    return output


print(select_less_than_100([99, 101, 88, 4, 2000, 50]))
