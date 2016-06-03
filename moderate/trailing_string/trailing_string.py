"""
CHALLENGE TRAILING STRING
There are two strings: A and B. Print 1 if string B occurs at the end of string A. Otherwise, print 0.

INPUT SAMPLE:
The first argument is a path to the input filename containing two comma-delimited strings, one per line.
Ignore all empty lines in the input file.

    Hello World,World
    Hello CodeEval,CodeEval
    San Francisco,San Jose

OUTPUT SAMPLE:
Print 1 if the second string occurs at the end of the first string. Otherwise, print 0.

    1
    1
    0
"""
import sys

def get_key_word(test_case):
    if type(test_case) == str:
        test_case_len = len(test_case)
        comma_index = test_case.index(",") + 1
        return test_case[comma_index : test_case_len].strip()


def get_test_text(test_case):
    if type(test_case) == str:
        comma_index = test_case.index(",")
        return test_case[0 : comma_index].strip()


def get_last_word(word, key_word):
    if type(word) == str:
        key_word_len = len(key_word) * -1
        return word[key_word_len:]



test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    key_word = get_key_word(test)
    test_text = get_test_text(test)
    last_word = get_last_word(test_text, key_word)

    if (last_word == key_word):
        print(1)
    else:
        print(0)

test_cases.close()
