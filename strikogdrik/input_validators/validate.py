import sys
import re

#Read line by line and add to array
lines = []
for line in sys.stdin:
    if line.strip(): 
        lines.append(line.strip())
if len(lines) < 2: 
    sys.exit("Invalid input")

#First line: target pattern. Check for letters only
target_pattern = lines[0]
if not re.fullmatch(r"[A-Za-z]+", target_pattern):
    sys.exit("Invalid target pattern")

#Second line: n = number of stitches & m = number of edges
try: 
    if not re.match(r"(0|([1-9][0-9]*)) (0|([1-9][0-9]*))$", lines[1]):
        sys.exit("Invalid integer") 
    n, m = map(int, lines[1].split())
    if not 2 <= n <= 1_00_000: 
        sys.exit("Invalid amount of nodes")
    if not 1 <= m <= n*(n-1)//2:
        sys.exit("Invalid amount of edges")
except ValueError:
    sys.exit("Invalid integer")

#Check we get the right amount of edges. m+2 = length of total lines read.
if len(lines) != m + 2:
    sys.exit("Invalid number of edges")
edge_pattern = re.compile(r"^(0|[1-9][0-9]*) (0|[1-9][0-9]*) ([A-Za-z]+)$")
for i in range(2, 2+m):
    matching_edge = edge_pattern.fullmatch(lines[i])
    if not matching_edge:
        sys.exit("Invalid edge")
    u, v = int(matching_edge.group(1)), int(matching_edge.group(2))
    if not (0 < u <= n-1 and u < v <= n):
        sys.exit("Invalid edge value")
sys.exit(42)