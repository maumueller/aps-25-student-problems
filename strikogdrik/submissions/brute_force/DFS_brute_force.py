from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(1_000_000)

input = sys.stdin.read
data = input().splitlines()

tp = data[0]
n, m = map(int, data[1].split())

blanket = defaultdict(list)
patterns = {}
found = False

for line in data[2:]:
    a, b, p = line.split()
    blanket[a].append(b)
    patterns[(a, b)] = p

def dfs(u, prev_pattern, curr_pattern):
    global found
    for v in blanket[u]:
        new_pattern = patterns[(u,v)]
        if new_pattern == ("DrunkKnitting", prev_pattern):
            continue
        route = curr_pattern + [new_pattern]
        if new_pattern == tp:
            print("-".join(route))
            found = True
            exit(0)
        dfs(v,new_pattern, route)


dfs("1",None,[])

if not found:
    print("Unravel it all :c")
        