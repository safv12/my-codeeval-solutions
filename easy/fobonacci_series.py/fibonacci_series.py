"""
CHALLENGE - FIBONACCI SERIES

The Fibonacci series is defined as:
F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1.
Given an integer n≥0, print out the F(n).

INPUT SAMPLE:
The first argument will be a path to a filename containing integer numbers,
one per line. E.g.
 5
 12

OUTPUT SAMPLE:
Print to stdout, the fibonacci number, F(n). E.g.
 5
 144
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    current = 0
    backup = 0
    previous = 0

    for x in range(1, int(test) + 1):
        if current == 0:
            current += 1
        else:
            backup = current
            current = current + previous
            previous = backup

    print(current)

test_cases.close()
