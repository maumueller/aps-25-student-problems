from collections import defaultdict
from queue import Queue

N, M = map(int, input().split())

G: defaultdict[str, set[str]] = defaultdict(set)
for _ in range(M):
    person_a, person_b = input().split()
    G[person_a].add(person_b)
    G[person_b].add(person_a)

start_a, start_b = input().split()
word = input().strip()

# edge case of 1 key
if N == 1:
    print("A" * len(word))
    print(len(word))
    exit()


def bfs(a: str, b: str, visited: set[str], G: defaultdict[str, set[str]]) -> float:
    if a == b:
        return len(visited)

    next = G[a] - visited
    return min([bfs(x, b, visited | {a}, G) for x in next] + [float("inf")])


paths: dict[tuple[str, str], float] = dict()
for person_a in G:
    for person_b in G:
        if (person_a, person_b) in paths:
            continue

        shortest_path = bfs(person_a, person_b, set(), G)

        paths[(person_a, person_b)] = shortest_path
        paths[(person_b, person_a)] = shortest_path

STEP = tuple[str, str, int]
dp: defaultdict[STEP, float] = defaultdict(lambda: float("inf"))
queue: Queue[STEP] = Queue()

dp[start_a, start_b, -1] = 0
queue.put((start_a, start_b, -1))

step_information: dict[STEP, STEP] = {}

while not queue.empty():
    person_a, person_b, step = queue.get()

    step += 1

    if step == len(word):
        break

    persons = [person_a, person_b]
    states = [(word[step], person_b, step), (person_a, word[step], step)]
    for active_person, new_state in zip(persons, states):
        cost = paths[(active_person, word[step])] + dp[person_a, person_b, step - 1]
        if dp[new_state] > cost:
            dp[new_state] = cost
            queue.put(new_state)
            step_information[new_state] = (person_a, person_b, step - 1)

path = [sorted([x for x in dp if x[2] == (len(word) - 1)], key=lambda x: dp[x])[0]]

for step in range(len(word) - 1, -1, -1):
    path.append(step_information[path[-1]])
path = path[::-1]

# Check which person is on the current char
output = "".join([["A", "B"][step.index(char)] for char, step in zip(word, path[1:])])
print(output)
print(dp[path[-1]] + len(word))


# import networkx as nx
# import matplotlib.pyplot as plt
# nx.draw(G, pos=pos, with_labels=True)
# plt.title("Sample Input Connections")
# plt.tight_layout()
# plt.savefig("G.png")
