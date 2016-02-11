"""
CHALLENGE SUM OF DIGITS
Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:
The first argument will be a path to a filename containing positive integers,
one per line. E.g.

    23
    496

OUTPUT SAMPLE:
Print to stdout, the sum of the numbers that make up the integer, one per
line. E.g.

    5
    19

"""

import sys
test_cases = open(sys.argv[1], 'r') # permite leer un archivo recibido a traves de un parametro
for test_case in test_cases:

    total = 0
    test_case = str(test_case)
    while len(str(test_case)) > 1:
        total += int(test_case[0:1])
        test_case = test_case[1:len(test_case)]

    print(total)

test_cases.close()
