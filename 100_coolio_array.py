# Given an array of numbers, return true if the array is a "100 Coolio Array", or false if it is not.

# A "100 Coolio Array" meets the following criteria:

# Its first and last numbers add up to 100,
# Its second and second-to-last numbers add up to 100,
# Its third and third-to-last numbers add up to 100,
# and so on and so forth.

# Here are examples of 100 Coolio Arrays:

# [1, 2, 3, 97, 98, 99]
# [90, 20, 70, 100, 30, 80, 10]

def coolio_array(input):
    if len(input) < 2:
        output = False
    else:
        output = True
    for i in range(0, int(len(input) / 2)):
        if input[i] + input[len(input) - 1 - i] != 100:
            output = False
            break
    return output


print(coolio_array([1, 2, 3, 97, 98, 99]))
print(coolio_array([90, 20, 70, 100, 30, 80, 10]))
print(coolio_array([1, 2, 3, 5, 7]))
print(coolio_array([100]))
