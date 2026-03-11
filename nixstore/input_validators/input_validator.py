#!/usr/bin/env python3

import sys
import re

try:
    n = int(sys.stdin.readline())
except ValueError:
    sys.exit(43)

if n < 1 or n > 10**5:
    sys.exit(43)

leading_numbers = []

for _ in range(n):
    line = sys.stdin.readline()
    if not line:
        sys.exit(43)
    line = line.strip()
    if re.match(r"^\d{1,10} add [a-zA-Z0-9_]+ \d+$", line):
        pass
    elif re.match(r"^\d{1,10} remove [a-zA-Z]+$", line):
        pass
    elif re.match(r"^\d{1,10} query \d{1,10} \d{1,10}$", line):
        pass
    else:
        sys.exit(43)

    leading_match = re.match(r"^(\d{1,10})", line)
    if not leading_match:
        sys.exit(43)

    leading_number = int(leading_match.group(1))
    leading_numbers.append(leading_number)

if sys.stdin.readline().strip() != "":
    sys.exit(43)

if leading_numbers != sorted(leading_numbers):
    sys.exit(43)

sys.exit(42)

#TODO: Needs to check if remove and query only reference things that have been added
