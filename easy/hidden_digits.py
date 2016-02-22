"""
CHALLENGE HIDDEN DIGITS
In this challenge you're given a random string containing hidden and visible digits. The digits are hidden
behind lower case latin letters as follows: 0 is behind 'a', 1 is behind ' b ' etc., 9 is behind 'j'.
Any other symbol in the string means nothing and has to be ignored. So the challenge is to find all visible
and hidden digits in the string and print them out in order of their appearance.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line in this file contains a
string. You may assume that there will be no white spaces inside the string. E.g.

    abcdefghik
    Xa,}A#5N}{xOBwYBHIlH,#W
    (ABW>'yy^'M{X-K}q,
    6240488

OUTPUT SAMPLE:
For each test case print out all visible and hidden digits in order of their appearance. Print out NONE in
case there is no digits in the string. E.g.

    012345678
    05
    NONE
    6240488
"""


def get_characters(chain):
    return list(chain)


def is_text_case(case):
    text_cases = 'abcdefghij'
    if case in text_cases:
        return True
    return False


def is_number_case(case):
    number_cases = '0123456789'
    if case in number_cases:
        return True
    return False


def get_special_characters(test):
    specials = []
    for case in test:
        if is_text_case(case):
            specials.append(case)
        elif is_number_case(case):
            specials.append(int(case))
    return(specials)


def get_hidden_values(specials):
    hidden_values = []
    text_cases = 'abcdefghij'

    for element in specials:
        if type(element) == int:
            hidden_values.append(element)
        else:
            hidden_values.append(text_cases.index(element))
    return ''.join(str(hidden) for hidden in hidden_values)

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:

    specials = get_special_characters(test)
    hidden_values = get_hidden_values(specials)

    if len(hidden_values) == 0:
        print('NONE')
    else:
        print(hidden_values)

test_cases.close()
