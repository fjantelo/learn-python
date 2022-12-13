# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

def longest_common_prefix(input):
    common_prefix_array = []
    output = ""
    i = 1
    while i < len(input):
        letters = ""
        j = 0
        while j < len(input[i]):
            if input[i][j] == input[i - 1][j]:
                letters = letters + input[i][j]
            else:
                break
            j += 1
        common_prefix_array.append(letters)
        i += 1
    i = 1
    output = common_prefix_array[0]
    while i < len(common_prefix_array):
        if len(common_prefix_array[i]) < len(output):
            output = common_prefix_array[i]
        i += 1
    return output


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
