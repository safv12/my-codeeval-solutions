"""
Write a program which finds the next-to-last word in a string.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

    some line with text
    another line

Each line has more than one word.

OUTPUT SAMPLE:

Print the next-to-last word in the following way.

    with
    another
"""

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    words = test.split(' ')
    print(words[len(words) - 2])

test_cases.close()
