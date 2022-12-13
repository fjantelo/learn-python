# Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# Output: {"Dewey" => 6, "Truman" => 5}

# Explanation: "Dewey" occurs 6 times in the array, while "Truman" occurs 5 times.

def count_votes(input):
    votes = {}
    for name in input:
        if (name in votes):
            votes[name] += 1
        else:
            votes[name] = 1
    return votes


print(count_votes(["Dewey", "Truman", "Dewey", "Dewey", "Truman",
      "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]))
