from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.read
data = input().splitlines()

tp = data[0]
n, m = map(int, data[1].split())

blanket = defaultdict(list)
patterns = {}
for line in data[2:]:
    a, b, p = line.split()
    blanket[a].append(b)
    patterns[(a, b)] = p

def bfs(u):
    queue = deque([(u,[],None)])
    visited = set()
    result = ""
    while queue:
        u,curr_pattern, prev_pattern = queue.popleft()

        for v in blanket[u]:
            new_pattern = patterns[(u,v)]

            if new_pattern == ("DrunkKnitting", prev_pattern)  or (v,new_pattern) in visited:
                continue

            route = curr_pattern + [new_pattern]
            
            if new_pattern == tp:
                for path in route:
                    print(path + "-", end="")
                exit()
                    
            visited.add((v,new_pattern))
            queue.append((v, route, new_pattern))
    print("Unravel it all :c")

bfs("1")
