import sys
import re

line = sys.stdin.readline()
print(f"Hm... {line}", file = sys.stderr)

if not re.match(r"(0|([1-9][0-9]*))\n", line):
    sys.exit(43)
try:
    x = int(line)
    if not 0 <= x <= 100000:
        sys.exit(43)
except ValueError:
    sys.exit(43)

line = sys.stdin.readline()
print(f"Hm... {line}", file = sys.stderr)
values = line.split(" ")
if not 1 <= len(values) <= 50:
    sys.exit(43)
for el in values:
    if not re.match(r"(0|([1-9][0-9]*))", el):
        sys.exit(43)
    
    if el == values[-1] and not re.match(r"(0|([1-9][0-9]*)\n)", el):
        sys.exit(43)
    try:
        x = int(el)
        if not 0 <= x <= 100000:
            sys.exit(43)
    except ValueError:
        sys.exit(43)

if sys.stdin.readline() != "":
    sys.exit(43)

print(f"Input validated", file = sys.stderr)
sys.exit(42)