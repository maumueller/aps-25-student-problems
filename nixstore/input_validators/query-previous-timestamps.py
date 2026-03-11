#!/usr/bin/env python3

import sys

try:
    n = int(sys.stdin.readline())
except ValueError:
    sys.exit(43)

timestamps = set()

for _ in range(n):
    line = sys.stdin.readline()
    if not line:
        sys.exit(43)

    segments = line.strip().split()

    timestamps.add(segments[0])

    if segments[1] == "query":
        start = segments[2]
        end = segments[3]

        if start not in timestamps or end not in timestamps:
            sys.exit(43)

sys.exit(42)
