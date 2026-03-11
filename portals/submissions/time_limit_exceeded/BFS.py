from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

# all graphs are (default) dictionaries
# vertex -> (vertex -> capacity), by default capacity is 0
def bfs(graph,src,dest): # returns path to dest or reachable set
    parent = {src:src}
    layer = [src]
    while layer:
        nextlayer = []
        for u in layer:
            for v,cap in graph[u].items():
                if cap > 0 and v not in parent:
                    parent[v] = u
                    nextlayer.append(v)
                    if v == dest:
                        p =  []
                        current_vertex = dest
                        while src != current_vertex:
                            p.append((parent[current_vertex],current_vertex))
                            current_vertex = parent[current_vertex]
                        return (True,p)
        layer = nextlayer
    return (False,set(parent))

def flow(orggraph, src,dest):
    graph = defaultdict(lambda: defaultdict(int))
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c

    current_flow = 0
    while True:
        ispath, p_or_seen = bfs(graph,src,dest)
        if not ispath:
            return (current_flow,
                    { a:{b:c-graph[a][b] for b,c in d.items() if graph[a][b]<c} 
                        for a,d in orggraph.items() },
                    p_or_seen)
        p = p_or_seen
        saturation = min( graph[u][v] for u,v in p )
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation


if __name__ == "__main__":
    n, e, p = map(int, input().split())
    graph = defaultdict(lambda: defaultdict(int))
    supersink = n + 1
    portals = list(map(int, input().split()))
    for portal in portals:
        graph[portal][supersink] = 1
    for _ in range(e):
        u, v, c = map(int, input().split())
        graph[u][v] = c

    flow_value, _, _ = flow(graph, 0, supersink)
    print(flow_value)