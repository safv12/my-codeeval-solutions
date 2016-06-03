"""
CHALLENGE FIRST NON-REPEATED CHARACTER

Write a program which finds the first non-repeated character in a string.

INPUT SAMPLE:
The first argument is a path to a file. The file contains strings.

For example:
    yellow
    tooth


OUTPUT SAMPLE:
Print to stdout the first non-repeated character, one per line.

For example:
    y
    h
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    word = test
    unrepeated = ''

    while len(word) >= 1:
        character = word[0:1]
        word = word[1:len(word)]

        if test.count(character) == 1:
            unrepeated = character
            break

    print(unrepeated)

test_cases.close()
