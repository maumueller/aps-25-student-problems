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
visited = set()
found = False

for line in data[2:]:
    a, b, p = line.split()
    blanket[a].append(b)
    patterns[(a, b)] = p

def dfs(u, prev_pattern, curr_pattern):
    global found
    for v in blanket[u]:
        new_pattern = patterns[(u,v)]
        if new_pattern == "DrunkKnitting" or new_pattern == prev_pattern:
            continue
        if (v, new_pattern) not in visited:
            visited.add((v, new_pattern))
            route = curr_pattern + [new_pattern]
            if new_pattern == tp:
                print("-".join(route))
                found = True
                return True
            if dfs(v, new_pattern, route):
                return True
    return False

if not dfs("1",None,[]):
     print("Unravel it all :c")
   
        