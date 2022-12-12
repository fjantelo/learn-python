# Given two sorted arrays, merge the second array into the first array while ensuring that the first array remains sorted. Do not use any built-in sort methods.

# Input :
# A : [1, 5, 8]
# B : [6, 9]

# Modified A : [1, 5, 6, 8, 9]

def merge_sorted_arrays(array1, array2):
    output = []
    index1 = index2 = 0
    while index1 < len(array1) or index2 < len(array2):
        if index1 == len(array1) or array1[index1] > array2[index2]:
            output.append(array2[index2])
            index2 += 1
        elif index2 == len(array2) or array2[index2] > array1[index1]:
            output.append(array1[index1])
            index1 += 1
        elif array1[index1] == array2[index2]:
            output.append(array1[index1])
            output.append(array2[index2])
            index1 += 1
            index2 += 1
    return output


print(merge_sorted_arrays([1, 5, 8], [6, 9]))
