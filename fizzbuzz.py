# Write a function that prints out every number from 1 to N, with the following exceptions:

# If the number is divisible by 3, print out "FIZZ".
# If the number is divisible by 5, print out "BUZZ".
# If the number is divisible by both 3 and 5, print out "FIZZBUZZ".

def fizzbuzz(input):
    for i in range(1, input + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZBUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(i)


fizzbuzz(30)
