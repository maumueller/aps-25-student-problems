import sys
import re

lines = sys.stdin.readlines()

# there's no tree
if len(lines) < 2:
	sys.exit(43)

# number denoting amount of inputs, aka how many "layers" the triangle / mountain  has
line = lines[0]

try:
	x = int(line)
except:
	sys.exit(43)

# check if the input actually has n following lines of input, based on the first line of input (n)
if len(lines)-1 != x:
	print("hit 1", len(lines)-1, x)
	sys.exit(43)

if not re.match(r"^([1-9][0-9]*( [1-9][0-9]*)*)(\n|\r)", line):
	print("hit 2")
	sys.exit(43)

# checks if n is actually a valid number (the triangle needs at least 1 "layer", in case of 1 it's just the top)

if not 1 <= x <= 1000:
	print("hit 3")
	sys.exit(43)

sys.exit(42)