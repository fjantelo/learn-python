# Given two arrays, determine whether one is a subset of the other. It is considered a subset if all the values in one array are contained within the other.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 2]
# Output: true

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 7]
# Output: false

def array_subset(array1, array2):
    number_dictionary = {}
    if len(array1) > len(array2):
        long_array = array1
        short_array = array2
    else:
        long_array = array2
        short_array = array1
    output = True
    for number in long_array:
        number_dictionary[number] = True
    for number in short_array:
        if not (number in number_dictionary.keys()):
            output = False
    return output


print(array_subset([1, 2, 3, 4, 5, 6], [6, 3, 2]))
print(array_subset([1, 2, 3, 4, 5, 6], [6, 3, 7]))
