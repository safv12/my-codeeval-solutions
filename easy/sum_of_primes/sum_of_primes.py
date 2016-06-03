"""
CHALLENGE SUM OF PRIMES
Write a program which determines the sum of the first 1000 prime numbers.

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print to stdout the sum of the first 1000 prime numbers.
    3682913
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


total = 0
n_primes = 1
number = 0
while n_primes <= 1000:
    if is_prime(number):
        total += number
        n_primes += 1
    number += 1

print(total)
