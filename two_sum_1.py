# Given an array of numbers, return a new array containing just two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Specifically use nested loops to solve this exercise even though there are other approaches as well.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

def two_sum(input):
    output = []
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            if i != j and input[i] + input[j] == 10:
                output = [input[i], input[j]]
                break
    if len(output) == 0:
        return False
    else:
        return output


print(two_sum([2, 5, 3, 1, 0, 7, 11]))
print(two_sum([1, 2, 3, 4, 5]))
