"""
CHALLENGE REAL FAKE

The police caught a swindler with a big pile of credit cards. Some of them are
stolen and some are fake. It would take too much time to determine which ones
are real and which are fake, so you need to write a program to check credit
cards.

To determine which credit cards are real, double every third number starting
from the first one, add them together, and then add them to those figures that
were not doubled. If the total sum of all numbers is divisible by 10 without
remainder, then this credit card is real.


INPUT SAMPLE:
The first argument is a path to a file. Each row includes a test case with a credit card number that you need to check.

    9999 9999 9999 9999
    9999 9999 9999 9993

OUTPUT SAMPLE:
If a credit card is fake – print Fake, if it’s real – print Real.

    Fake
    Real

CONSTRAINTS:
    The credit card number is 16 digits in length.
    The number of test cases is 40.
"""
import sys

def sum_of_segments_digits(segments):
    duplicated_digits = 0
    for segment in segments:
        first_digit = segment[0:1]
        third_digit = segment[2:3]
        duplicated_digits += (int(first_digit) * 2) + (int(third_digit) * 2)

    other_digits = 0
    for segment in segments:
        second_digit = segment[1:2]
        fourth_digit = segment[3:5]
        other_digits += int(second_digit) + int(fourth_digit)

    return duplicated_digits + other_digits

def validate_creditcard(creditcard):
    segments = creditcard.split()
    sum = sum_of_segments_digits(segments)

    if (sum % 10 != 0):
        return 'Fake'
    return 'Real'




creditcards = open(sys.argv[1], 'r')
for credicard in creditcards:

    print(validate_creditcard(credicard))

creditcards.close()
