# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

def array_mesh(input):
    output = []
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            if i != j:
                output.append(input[i] + input[j])
    return output


print(array_mesh(["a", "b", "c", "d"]))
