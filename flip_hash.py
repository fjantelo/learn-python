# Given a hash, create a new hash that has the keys and values switched.

# Input: {"a" => 1, "b" => 2, "c" => 3}
# Output: {1 => "a", 2 => "b", 3 => "c"}

def flip_hash(input):
    output = {}
    for k, v in input.items():
        output[v] = k
    return output


print(flip_hash({"a": 1, "b": 2, "c": 3}))
