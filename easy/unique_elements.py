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
for line in test_cases:

    unique_elements = ''
    a = []

    while len(line) >= 1:
        element = ''

        if line.find(',') == -1:
            element = str(line[0:len(line)])
            line = ''
        else:
            element = str(test[0:line.find(',')]) + ','
            line = line[line.find(',')+1:len(line)]

        if not int(element.replace(',','')) in a:
            a.append(int(element.replace(',','')))
            unique_elements += element

    print(unique_elements[0:-1])

test_cases.close()
