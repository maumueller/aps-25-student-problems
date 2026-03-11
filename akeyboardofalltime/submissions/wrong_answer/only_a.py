from collections import defaultdict
import sys

sys.setrecursionlimit(10**5)

N, M = map(int, input().split())

G: defaultdict[str, set[str]] = defaultdict(set)
for _ in range(M):
    person_a, person_b = input().split()
    G[person_a].add(person_b)
    G[person_b].add(person_a)

start_a, start_b = input().split()
word = input().strip()


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


def get_path(
    cost: float, a: str, b: str, i: int, word: str, path: str
) -> tuple[float, str]:
    if i == len(word):
        return (cost, path)

    a_move = get_path(cost + paths[(a, word[i])], word[i], b, i + 1, word, path + "A")
    return min([a_move])


cost, path = get_path(0, start_a, start_b, 0, word, "")
print(path)
print(cost + len(word))
