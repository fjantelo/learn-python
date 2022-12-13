# Given a hash, return a flat array containing all the hash’s keys and values.

# Input: {“a” => 1, “b” => 2, “c” => 3, “d” => 4}
# Output: [“a”, 1, “b”, 2, “c”, 3, “d”, 4]

def flatten_hash(input):
    output = []
    keys = list(input.keys())
    values = list(input.values())
    for i in range(0, len(keys)):
        output.append(keys[i])
        output.append(values[i])
    return output


print(flatten_hash({"a": 1, "b": 2, "c": 3, "d": 4}))
