class Node:
    def __init__(self, id):
        self.edges = []
        self.id = id

    def add_edge(self, node, cap):
        self.edges.append((node, cap, 0))

def maxFlow(source, sink, network):
    def bfs():
        visited = [-1] * len(network)
        queue = [source]
        visited[source] = source
        while queue:
            current = queue.pop(0)
            if current == sink:
                return visited
            for neighbor, capacity, currentflow in network[current].edges:
                if visited[neighbor.id] == -1 and capacity - currentflow > 0:
                    visited[neighbor.id] = current
                    queue.append(neighbor.id)
        return None

    max_flow = 0
    while True:
        path = bfs()
        if not path:
            break
        flow = float('Inf')
        current = sink
        while current != source:
            prev = path[current]
            for neighbor, capacity, currentflow in network[prev].edges:
                if neighbor.id == current:
                    flow = min(flow, capacity - currentflow)
                    break
            current = prev
        max_flow += flow
        current = sink
        while current != source:
            prev = path[current]
            for i, (neighbor, capacity, currentflow) in enumerate(network[prev].edges):
                if neighbor.id == current:
                    network[prev].edges[i] = (neighbor, capacity, currentflow + flow)
                    break
            for i, (neighbor, capacity, currentflow) in enumerate(network[current].edges):
                if neighbor.id == prev:
                    network[current].edges[i] = (neighbor, capacity, currentflow - flow)
                    break
            current = prev
    return max_flow, network

if __name__ == "__main__":
    C, P = map(int, input().split())
    T, N, R = map(int, input().split())

    endPoint = N + T + 1  # end point
    # Create a graph
    network = [-1]*(endPoint+1)

    network[0] = Node(0) # warehouse
    network[endPoint] = Node(endPoint)

    for i in range (T): #trading posts
        post = Node(i+1)
        network[i+1] = post

    for i in range (N): #cities
        cap = int(input())
        city = Node(T+i+1)
        city.add_edge(network[endPoint], cap)
        network[T+i+1] = city

    for i in range (R): # caravans
        start, end, cap = map(int, input().split())
        startNode = network[start]
        endNode = network[end]
        startNode.add_edge(endNode, cap)

    result = (maxFlow(0, endPoint, network))

    rMaxFlow = result[0]
    rNetwork = result[1]

    max_single_flow = 0
    for node in rNetwork:
        for edge in node.edges:
            if edge[0].id!=endPoint:
                max_single_flow = max(max_single_flow, edge[2])

    if (rMaxFlow*(P-C))-max_single_flow*P > 0:
        print(rMaxFlow-max_single_flow, (rMaxFlow*(P-C))-max_single_flow*P)
    else:
        print("Not worth")