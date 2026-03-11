from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def dfs(graph,u,dest,seen):
    if u in seen:
        return (False,seen)
    seen.add(u)
    for v,cap in graph[u].items():
        if cap > 0:
            if v == dest:
                return (True,[(u,v)])
            suc, p = dfs(graph,v,dest,seen)
            if suc:
                p.append((u,v))
                return (True,p)
    return (False,seen)


def flow(orggraph, src,dest):
    graph = defaultdict(lambda: defaultdict(int))
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c

    current_flow = 0
    while True:
        ispath, p_or_seen = dfs(graph,src,dest, set())
        if not ispath:
            return graph
        p = p_or_seen
        saturation = min( graph[u][v] for u,v in p )
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation

def find_portal_incoming_flow(graph, portal):
    max_flow = 0
    for _, connections in graph.items():
        max_flow += connections.get(portal, 0)
    return max_flow

if __name__ == "__main__":
    n, e, p = map(int, input().split())
    graph = defaultdict(lambda: defaultdict(int))
    portals = list(map(int, input().split()))
    for _ in range(e):
        u, v, c = map(int, input().split())
        graph[u][v] = c
    
    portals_incoming_flow = list(map(lambda portal: find_portal_incoming_flow(graph,portal),portals))
    portals_with_flow = list(zip(portals, portals_incoming_flow))
    portals_with_flow.sort(key=lambda k: k[1])
    
    residual = graph
    for portal in portals_with_flow:
        residual = flow(residual, 0, portal[0])

    open_portals = 0
    for portal in portals:
        if residual[portal]:
            open_portals += 1
    
    print(open_portals)