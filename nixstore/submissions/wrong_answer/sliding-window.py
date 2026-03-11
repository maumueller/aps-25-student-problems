#!/usr/bin/env python3
import sys

n = int(sys.stdin.readline())
events = []
pointerL = 0
pointerR = 0
windowSum = 0

for _ in range(n):
    parts = sys.stdin.readline().split()
    t, cmd = int(parts[0]), parts[1]

    if cmd == "add":
        name, size = parts[2], int(parts[3])
        events.append((t, size))

    elif cmd == "query":
        t1, t2 = int(parts[2]), int(parts[3])

        while pointerR < len(events) and events[pointerR][0] <= t2:
            windowSum += events[pointerR][1]
            pointerR += 1

        while pointerL < len(events) and events[pointerL][0] < t1:
            windowSum -= events[pointerL][1]
            pointerL += 1

        print(windowSum)
