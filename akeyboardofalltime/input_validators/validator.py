from collections import defaultdict
import traceback
import sys


def bfs(a: str, visited: set[str], G: defaultdict[str, set[str]]) -> set[str]:
    if a in visited:
        return set()

    adj = G[a] - visited
    visited.add(a)
    reachable = {a}

    for x in adj:
        reachable.update(bfs(x, visited, G))
    return reachable


def inp():
    val = input()
    if "\r" in val:
        raise ValueError("Input contains carriage return characters")
    return val


try:
    N, M = map(int, inp().split())

    G: defaultdict[str, set[str]] = defaultdict(set)
    for _ in range(M):
        letter_a, letter_b = inp().split()
        G[letter_a].add(letter_b)
        G[letter_b].add(letter_a)

    start_a, start_b = inp().split()
    word = inp().strip()

    if start_a == start_b:
        if not start_b in G[start_a]:
            G[start_a].add(start_b)
        if not start_a in G[start_b]:
            G[start_b].add(start_a)

    # Verify that the set of nodes reachable from either start_a or start_b
    # include the word
    reachable_from_a = bfs(start_a, set(), G)
    reachable_from_b = bfs(start_b, set(), G)
    reachable = reachable_from_a.union(reachable_from_b)
    assert all(char in reachable for char in word), (
        "Not all characters in the word are reachable from the starting positions."
    )

    print("AC")
    exit(42)
except Exception as e:
    traceback.print_exception(type(e), e, e.__traceback__, file=sys.stderr)
    print("WA")
    exit(43)
