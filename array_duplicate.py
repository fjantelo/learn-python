# A given array has one pair of duplicate values. Return the first duplicate value.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [5, 2, 9, 7, 2, 6]
# Output: 2

def array_duplicate(array):
    count = {}
    for number in array:
        if number in count.keys():
            count[number] += 1
        else:
            count[number] = 1
        if count[number] > 1:
            return number


print(array_duplicate([5, 2, 9, 7, 2, 6]))
