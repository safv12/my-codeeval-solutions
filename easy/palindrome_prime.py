"""
CHALLENGE PALINDROME PRIME
Write a program which determines the largest prime palindrome less than 1000.

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print to stdout the largest prime palindrome less than 1000.

    929
"""

def is_prime(number):

    if number <= 3:
        return number >= 2

    if number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, int(number ** 0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


prime_numbers = []
for current_number in xrange(1,1001):

    if is_prime(current_number):
        prime_numbers.append(current_number)


palindromes = []
for prime_number in prime_numbers:
    if str(prime_number)[::-1] == str(prime_number):
        palindromes.append(int(prime_number))

print(max(palindromes))
