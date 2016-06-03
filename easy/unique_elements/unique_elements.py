"""
CHALLENGE UNIQUE ELEMENTS
You are given a sorted list of numbers with duplicates. Print out the
sorted list with duplicates removed.

INPUT SAMPLE:
File containing a list of sorted integers, comma delimited, one per line.
    1,1,1,2,2,3,3,4,4
    2,3,4,5,5


OUTPUT SAMPLE:
Print out the sorted list with duplicates removed, one per line.
    1,2,3,4
    2,3,4,5
"""

import sys

test_cases = open(sys.argv[1], 'r')


def get_next_element(line):
    return str(line[0:line.find(',')])

def remove_current_element(line):
    return line[line.find(',') + 1:len(line)]


for test_case in test_cases:

    output = ''
    unique_elements = []

    while len(test_case) >= 1:
        current_element = ''

        if test_case.find(',') == -1:
            current_element = get_next_element(test_case)
            test_case = ''
        else:
            current_element = get_next_element(test_case)
            test_case = remove_current_element(test_case)

        if not int(current_element) in unique_elements:
            unique_elements.append(int(current_element.replace(',','')))
            output += current_element + ','

    print(output[0:-1])

test_cases.close()
