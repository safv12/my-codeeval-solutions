"""
CHALLENGE FILE SIZE

Print the size of a file in bytes.

INPUT:
The first argument to your program has the path to the file you need to
check the size of.

OUTPUT SAMPLE:
Print the size of the file in bytes. E.g.

    55
"""

import sys
import os

file = sys.argv[1]
print os.path.getsize(file);
