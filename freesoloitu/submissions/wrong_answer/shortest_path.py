import heapq

n = int(input())

if n == 1:
	print(input())
	exit(0)

edges = {
	(i, j) : [] 
	for i in range(0, n) 
	for j in range(i+1)
}


lines = []
for i in range(n):
	lines.append(list(map(int, input().split())))

lines.append([0])

for i in range(len(lines) - 1):
	vals = lines[i]
	for j in range(i+1):
		if i == n-1:
			edges[(i, j)].append(((i + 1, 0), vals[j]))
		else:
			edges[(i, j)].append(((i+1, j) ,vals[j]))
			edges[(i, j)].append(((i+1, j+1) ,vals[j]))

def dijkstra(start, edges):
	dist = {node: float('inf') for node in edges}
	dist[start] = 0
	pq = [(0, start)]

	while pq:
		current_dist, current_node = heapq.heappop(pq)

		if current_dist > dist[current_node]:
			continue
		
		if (current_node) == (n, 0):
			break

		for neighbor, weight in edges[current_node]:
			new_dist = current_dist + weight
			if new_dist < dist.get(neighbor, float('inf')):
				dist[neighbor] = new_dist
				heapq.heappush(pq, (new_dist, neighbor))

	return dist

distances = dijkstra((0, 0), edges)

print(distances[(n, 0)])
