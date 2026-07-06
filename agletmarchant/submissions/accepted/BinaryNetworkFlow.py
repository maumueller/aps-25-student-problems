class Node:
    def __init__(self, id):
        self.edges = []
        self.id = id

    def add_edge(self, node, cap):
        self.edges.append((node, cap, 0, cap))

def maxFlow(source, sink, network, flowLimit):
    for node in network:
        for i, (neighbor, capacity, currentflow, tempCap) in enumerate(node.edges):
            if neighbor.id != sink:
                node.edges[i] = (neighbor, capacity, 0, min(capacity, flowLimit))
            else:
                node.edges[i] = (neighbor, capacity, 0, capacity)

    def bfs():
        visited = [-1] * len(network)
        queue = [source]
        visited[source] = source
        while queue:
            current = queue.pop(0)
            if current == sink:
                return visited
            for neighbor, capacity, currentflow, tempCap in network[current].edges:
                if visited[neighbor.id] == -1 and tempCap - currentflow > 0:
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
            for neighbor, capacity, currentflow, tempCap in network[prev].edges:
                if neighbor.id == current:
                    flow = min(flow, tempCap - currentflow)
                    break
            current = prev
        max_flow += flow
        current = sink

        while current != source:
            prev = path[current]
            for i, (neighbor, capacity, currentflow, tempCap) in enumerate(network[prev].edges):
                if neighbor.id == current:
                    network[prev].edges[i] = (neighbor, capacity, currentflow + flow, tempCap)
                    break
            for i, (neighbor, capacity, currentflow, tempCap) in enumerate(network[current].edges):
                if neighbor.id == prev:
                    network[current].edges[i] = (neighbor, capacity, currentflow - flow, tempCap)
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

    originalMaxFlow = (maxFlow(0, endPoint, network, float('inf')))[0]

    low, high = 0, originalMaxFlow
    currentLimit = high
    resultFLow = 0
    resultLimit = 0

    while low <= high:
        mid = (low + high) // 2
        temp_result = maxFlow(0, endPoint, network, mid)

        flow = temp_result[0]

        if flow == originalMaxFlow:
            resultFLow = flow
            resultLimit = mid
            currentLimit = mid
            high = mid - 1  # Try for a lower limit
        else:
            low = mid + 1  # Increase the limit to meet the flow requirement

    if (resultFLow * (P - C))-resultLimit*P > 0:
        print(resultFLow - resultLimit, (resultFLow * (P - C)) - resultLimit * P)
    else:
        print("Not worth")