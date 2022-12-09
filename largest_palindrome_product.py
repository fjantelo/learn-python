# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from reverse_string import reverse_string


def palindrome_product():
    output = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            x = str(i * j)
            if x == reverse_string(x) and i * j > output:
                output = i * j
    return output


print(palindrome_product())
