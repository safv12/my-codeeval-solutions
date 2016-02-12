"""
CHALLENGE REVERSE WORDS
Write a program which reverses the words in an input sentence.

INPUT SAMPLE:
The first argument is a file that contains multiple sentences, one per line.
Empty lines are also possible.

    Hello World
    Hello CodeEval

OUTPUT SAMPLE:
Print to stdout each sentence with the reversed words in it, one per line.
Empty lines in the input should be ignored. Ensure that there are no trailing
empty spaces in each line you print.

    World Hello
    CodeEval Hello
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    words = []
    while len(test) >= 1:
        if test.find(' ') == -1:
            words.append(test[0 : len(test) - 1])
            test = ''
        else:
            words.append(test[0 : test.find(' ')])
            test = test[test.find(' ') + 1 : len(test)]

    output = ''
    for word in words[::-1]:
        output += word + ' '

    print(output)

test_cases.close()
