# Write a function that returns the greatest value from an array of numbers.

# Input: [5, 17, -4, 20, 12]
# Output: 20

def array_max(input):
    output = input[0]
    for number in input:
        if number > output:
            output = number
    return output


print(array_max([5, 17, -4, 20, 12]))
