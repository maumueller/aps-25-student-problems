import sys
import re

f = open(sys.argv[2], "rt")

goal = 0
inputCount = 0
for l in f:
    arr = list(map(int, l.split()))
    goal += arr[0] * arr[1]
    inputCount += 1

total = 0
try:
    for _ in range (inputCount):
        line = sys.stdin.readline()
        print(f"Hm... {line}", file = sys.stderr)
        try:
            arr = list(map(int, line.split()))
            total += arr[0] * arr[1]
        except:
            sys.exit(43)
except:
    sys.exit(43)

print(f"total: {total} == goal: {goal} -> {total == goal}")

if total == goal:
    sys.exit(42)
sys.exit(43)