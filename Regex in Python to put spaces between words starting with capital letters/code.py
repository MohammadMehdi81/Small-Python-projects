# import Modules
import re


def putSpace(input):
    # regex [A-Z][a-z]* means any string starting
    # with capital character followed by many
    # lowercase letters
    words = re.findall('[A-Z][a-z]*', input)

    # case
    print(' '.join(words))


# Driver program
input = 'BruceWayneIsBatman'
putSpace(input)