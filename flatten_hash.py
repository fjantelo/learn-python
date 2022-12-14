# Given a hash, return a flat array containing all the hash’s keys and values.

# Input: {“a” => 1, “b” => 2, “c” => 3, “d” => 4}
# Output: [“a”, 1, “b”, 2, “c”, 3, “d”, 4]

def flatten_hash(input):
    output = []
    for k, v in input.items():
        output.append(k)
        output.append(v)
    return output


print(flatten_hash({"a": 1, "b": 2, "c": 3, "d": 4}))
