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

    timestamp = int(segments[0])

    if timestamp in timestamps:
        sys.exit(43)

    timestamps.add(timestamp)

sys.exit(42)
