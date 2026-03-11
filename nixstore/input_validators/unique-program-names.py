#!/usr/bin/env python3

import sys

try:
    n = int(sys.stdin.readline())
except ValueError:
    sys.exit(43)

programNames = set()

for _ in range(n):
    line = sys.stdin.readline()
    if not line:
        sys.exit(43)

    segments = line.strip().split()

    if segments[1] == "remove":
        programNames.remove(segments[2])
    elif segments[1] == "add":
        programName = segments[2]

        if programName in programNames:
            sys.exit(43)

        programNames.add(programName)

sys.exit(42)
