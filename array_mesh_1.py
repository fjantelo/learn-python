# Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

# Input: ["a", "b", "c"], ["d", "e", "f", "g"]
# Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]

def array_mesh(array1, array2):
    output = []
    for i in range(0, len(array1)):
        for j in range(0, len(array2)):
            output.append(array1[i] + array2[j])
    return output


print(array_mesh(["a", "b", "c"], ["d", "e", "f", "g"]))
