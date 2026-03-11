#!/usr/bin/env python3
import sys

n = int(sys.stdin.readline())
currentStorage = 0
installed = {}

for _ in range(n):
    parts = sys.stdin.readline().split()
    t, command = int(parts[0]), parts[1]

    if command == "add":
        name, size = parts[2], int(parts[3])
        installed[name] = size
        currentStorage += size

    elif command == "remove":
        name = parts[2]
        currentStorage -= installed[name]
        del installed[name]

    elif command == "query":
        print(currentStorage)