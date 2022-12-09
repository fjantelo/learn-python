# Write a function that gives the Nth number of the Fibonacci Sequence. The Fibonacci sequence begins with 0 and 1, and every number thereafter is the sum of the previous two numbers. So the sequence goes like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on until infinity...

# Input: 9
# Output: 21 (as this is the 9th number of the Fibonacci Sequence)

def fibonacci(input):
    numbers = [0, 1]
    if input < 2:
        return 0
    else:
        for i in range(2, input):
            numbers.append(numbers[i-2] + numbers[i-1])
        return numbers[input - 1]


print(fibonacci(9))
