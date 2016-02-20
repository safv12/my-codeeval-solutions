"""
CHALLENGE LOWEST UNIQUE NUMBER
There is a game where each player picks a number from 1 to 9, writes it on a paper and gives to a guide.
A player wins if his number is the lowest unique. We may have 10-20 players in our game.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename.
You're a guide and you're given a set of numbers from players for the round of game.
E.g. 2 rounds of the game look this way:

    3 3 9 1 6 5 8 1 5 3
    9 2 9 9 1 8 8 8 2 1 1

OUTPUT SAMPLE:
Print a winner's position or 0 in case there is no winner. In the first line of input sample
the lowest unique number is 6. So player 5 wins.

    5
    0
"""

def get_elements(test):
    test = test.split(' ')
    elements = []

    for element in test:
        elements.append(element.strip())
    return elements


def get_winner(uniques, original_elements):
    print(uniques)
    print(original_elements)


def print_winner(elements, uniques, not_uniques, original_elements):
    if len(uniques) == 0:
        uniques = []
    if len(not_uniques) == 0:
        not_uniques = []

    if len(elements) > 0:
        current = elements.pop(0)
        if current in not_uniques or current in elements:
            not_uniques.append(current)
        else:
            uniques.append(current)
        print_winner(elements, uniques, not_uniques, original_elements)
    else:
        get_winner(uniques, original_elements)

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    test = get_elements(test)
    print_winner(test, [], [], test)

test_cases.close()
