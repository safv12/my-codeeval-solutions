"""
CHALLENGE REMOVE CHARACTERS
Write a program which removes specific characters from a string.

INPUT SAMPLE:
The first argument is a path to a file. The file contains the source strings and the
characters that need to be scrubbed. Each source string and characters you need to
scrub are delimited by comma.

For example:

    how are you, abc
    hello world, def

OUTPUT SAMPLE:
Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing
empty spaces on each line you print.

For example:

    how re you
    hllo worl

"""

def get_characters_to_remove(text):
    if type(text) == str:
        array_text = text.split(", ")
        characters_to_remove = array_text[1].strip()
        return list(characters_to_remove)
    return False


def get_original_text(text):
    if type(text) == str:
        array_text = text.split(", ")
        return array_text[0].strip()
    return False


def remove_characters(text, characters_to_remove):
    if len(characters_to_remove) >= 1:
        for character in characters_to_remove:
            text = text.replace(character, "")
    return text




import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    characters_to_remove = get_characters_to_remove(test)
    original_text = get_original_text(test);
    output = remove_characters(original_text, characters_to_remove)

    print(output)

test_cases.close()
