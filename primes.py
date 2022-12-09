# Write a function that returns whether a given number is a prime number.
# First prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

def primes(input):
    index = 2
    output = True
    while index < input:
        if input % index == 0:
            output = False
            break
        index += 1
    return output


print("The following should be true (prime)")
print(primes(2))
print(primes(3))
print(primes(5))
print(primes(7))
print(primes(11))
print(primes(13))
print(primes(17))
print(primes(19))
print(primes(23))
print(primes(29))
print("The following should be false (not prime)")
print(primes(4))
print(primes(6))
print(primes(10))
print(primes(21))
