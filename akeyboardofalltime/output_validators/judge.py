from collections import defaultdict
from queue import Queue
import sys
import traceback

sys.setrecursionlimit(10**5)


def bfs(a: str, b: str, visited: set[str], G: defaultdict[str, set[str]]) -> float:
    if a == b:
        return len(visited)

    next = G[a] - visited
    return min([bfs(x, b, visited | {a}, G) for x in next] + [float("inf")])


def get_path(
    cost: float,
    a: str,
    b: str,
    i: int,
    word: str,
    output_path: str,
    paths: dict[tuple[str, str], float],
) -> tuple[float, str]:
    if i == len(word):
        return (cost + len(word), output_path)

    if output_path[i] == "A":
        return get_path(
            cost + paths[(a, word[i])],
            word[i],
            b,
            i + 1,
            word,
            output_path + "A",
            paths,
        )
    assert output_path[i] == "B"
    return get_path(
        cost + paths[(b, word[i])], a, word[i], i + 1, word, output_path + "B", paths
    )


STEP = tuple[str, str, int]


def correct_solution(start_a: str, start_b: str, word: str) -> tuple[float, str]:
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

    output = "".join(
        [["A", "B"][step.index(char)] for char, step in zip(word, path[1:])]
    )
    return (dp[path[-1]] + len(word), output)


try:
    testcase_path = sys.argv[1]

    G: defaultdict[str, set[str]] = defaultdict(set)
    with open(testcase_path, "r") as f:
        N, M = map(int, f.readline().split())

        for _ in range(M):
            person_a, person_b = f.readline().split()
            G[person_a].add(person_b)
            G[person_b].add(person_a)

        start_a, start_b = f.readline().split()
        word = f.readline().strip()

        if start_a == start_b:
            if start_b not in G[start_a]:
                G[start_a].add(start_b)
            if start_a not in G[start_b]:
                G[start_b].add(start_a)

    path_ans = input().strip()
    cost_ans = int(input().strip())

    paths: dict[tuple[str, str], float] = dict()
    for person_a in G:
        for person_b in G:
            if (person_a, person_b) in paths:
                continue

            shortest_path = bfs(person_a, person_b, set(), G)

            paths[(person_a, person_b)] = shortest_path
            paths[(person_b, person_a)] = shortest_path

    # print(f"Validating path for {word=}, {start_a=}, {start_b=}, {answer=}")
    cost_ans_calc, path_ans_calc = get_path(
        0, start_a, start_b, 0, word, path_ans, paths
    )
    assert (
        cost_ans_calc == cost_ans
    ), f"Judge failed to recreate cost: {cost_ans_calc} != {cost_ans}"
    cost_true, path_true = correct_solution(start_a, start_b, word)
    # print(answer)
    # print(path)
    # print(cost + len(word))
    assert cost_ans == cost_true, f"Cost mismatch: {cost_ans} != {cost_true}"
    print("AC")
    exit(42)
except Exception as e:
    traceback.print_exception(type(e), e, e.__traceback__, file=sys.stderr)
    print("WA")
    exit(43)
