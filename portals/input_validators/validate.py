import sys
import re
# not done, still needs to verify that the final graph is valid
# the input is
# n
# s1 s2 s3 ...
# t1 t2 t3 ...
# <n lines of edges of format v w weight>

# someone should probably figure out a better format of giving the graph
# and someone should probably figure out if the the "only sinks should have outdegree 0 and only sources should have indegree 0" requirement is desirable, and figure out of other things are desirable

four_int_pattern = re.compile('^([1-9]\\d* ){2}0 [1-9]\\d*$')
multiple_int_pattern = re.compile('^([1-9]\\d* )+[1-9]\\d*$')
three_int_pattern = re.compile('^\\d+ [1-9]\\d* [1-9]\\d*$')

# deal with first line ´´n_nodes n_edges wizard_start n_portals´´ 
try:
    line = sys.stdin.readline()
except EOFError:
    print('No input given.')
    sys.exit(1)

if three_int_pattern.match(line):
    n_nodes,n_edges,n_portals = map(int,line.split())
else:
    print(f'The first line of input must consist of 3 positive integers. Not {line}.')
    sys.exit(1)

# deal with second line portal1 , portal2 , portal3 ...
try:
    line = sys.stdin.readline()
except EOFError:
    print('Only one line of input given.')
    sys.exit(1)

if not multiple_int_pattern.match(line):
    print(f'The second line of input must consist of only positive integers. Not {line}.')
    sys.exit(1)
portals = list(map(int,line.split()))
if len(portals) != n_portals:
    print(f'Wrong number of portals given. Promised {n_portals} and gave {len(portals)}.')
    sys.exit(1)

# deal with edges
edges = []
for _ in range(n_edges):
    try:
        line = sys.stdin.readline()
    except EOFError:
        print(f'Not enough edges given. Expected {n_edges} and got only {len(edges)}.')
        sys.exit(1)
    if not three_int_pattern.match(line):
        print(f'Edges must consist of a non-negative integer followed by 2 positive integers. Not {line}.')
        sys.exit(1)
    v,w,weight = map(int,line.split())
    edges.append((v,w,weight))
if sys.stdin.readline() != "":
    print('Too many edges given.')
    sys.exit(1)

# decide if graph is acyclic with only sources having indegree 0 and only sinks having outdegree 0
edges_with_positive_indegree = set()
edges_with_positive_outdegree = set()
greatest_node = 0
for v,w,weight in edges:
    edges_with_positive_outdegree.add(v)
    edges_with_positive_indegree.add(w)
    greatest_node = max(greatest_node , w)

if 0 in edges_with_positive_indegree:
    print('The source node should have indegree 0.')    
    sys.exit(1)
if 0 not in edges_with_positive_outdegree:
    print('The source should have positive outdegree.')
    sys.exit(1)
for portal in portals:
    if portal in edges_with_positive_outdegree:
        print('A sink should have outdegree 0.')
    if portal not in edges_with_positive_indegree:
        print('A sink should have positive indegree.')
        sys.exit(1)

if greatest_node != n_nodes - 1:
    print(f'Got the wrong number of nodes. Was promised {n_nodes} but received {greatest_node+1}.')

print('The input is valid!')
sys.exit(42)
