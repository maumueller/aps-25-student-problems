from collections import deque
from collections import defaultdict
import sys

# Read input
input = sys.stdin.read
data = input().splitlines()

# Target pattern to find
tp = data[0]

# Amount of nodes and edges
n, m = map(int, data[1].split())

# Graph representation
# - Blanket: adjacency list of nodes and their respective neighbors
# - pattern: maps the node connection to their pattern (edge)
blanket = defaultdict(list)
patterns = {}
for line in data[2:]:
    a, b, p = line.split()
    a = int(a)
    b = int(b)
    if p == "DrunkKnitting":
        continue # Skip irrelevant input
    blanket[a].append(b)
    patterns[(a, b)] = p

# Breath-first search to find the shortest legal patteren path to tp
def bfs(u):
    queue = deque([(u,(),None)]) # Queue holds tuples: (current node, tuple of patterns so far, previous pattern)
    visited = set() # Tracks previously visited pairs (node, pattern) to avoid recomputation

    while queue: 
        u,curr_pattern, prev_pattern = queue.popleft() # removing the first element in the deque

        for v in blanket[u]: # exploring each neighbouring node in the blanket
            new_pattern = patterns[(u,v)]

            # if this pattern is the same as the previous pattern or if we have already investigated this node and pattern pair, ignore it 
            if new_pattern ==  prev_pattern  or (v,new_pattern) in visited: 
                continue 

            route = curr_pattern + (new_pattern,)
            
            # If we found tp, print the path to get there and exit BFS
            if new_pattern == tp:
                sys.stdout.write("-".join(route) + "\n")
                return
            
            # If we did not, add the next node to visited and the queue
            visited.add((v,new_pattern))
            queue.append((v, route, new_pattern))

    print("Unravel it all :c") # Printed if we do not find tp

# Start BFS from node 1
bfs(1)

