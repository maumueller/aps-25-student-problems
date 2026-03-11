# Fenwick Tree
from typing import Dict

# Fenwick tree to handle the size of the programs
class FenwickTree:
    def __init__(self, n: int):
        self.A = [0 for _ in range(n + 1)]

    def get(self, i: int) -> int:
        return self.prefix_sum(i) - self.prefix_sum(i - 1)

    def set(self, i: int, k: int) -> None:
        s = 0
        while i < len(self.A):
            self.A[i] += k
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.A[i]
            i -= i & -i
        return s

    def query(self, i: int, j: int) -> int:
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

n = int(input())

# Holds the installed programs, their sizes and the time they were installed.
installedPrograms: Dict[str, Dict[str, int]] = {}
# Holds the time mapping from statement timestamp to the Fenwick Tree index.
timeMapping: Dict[int, int] = {}
fenwickTree = FenwickTree(10**6)

# Statement handlers
def add_program(time: int, name: str, size: int):
    global installedPrograms
    global timeMapping
    global fenwickTree

    installedPrograms[name] = { "size": size, "time": time }

    fenwickTree.set(timeMapping[time], size)

def remove_program(name: str):
    global installedPrograms
    global timeMapping
    global fenwickTree

    program = installedPrograms[name]
    time = program["time"]
    size = program["size"]

    fenwickTree.set(timeMapping[time], -size)

    del installedPrograms[name]

def query_programs(time1: int, time2: int) -> int:
    global timeMapping
    global fenwickTree

    # Get the Fenwick Tree index for the time range
    rangeStart = timeMapping.get(time1, 0)
    rangeEnd = timeMapping.get(time2, 0)

    return fenwickTree.query(rangeStart, rangeEnd)

# Handle input
for _ in range(n):
    line = input().split()

    time = int(line[0])
    command = line[1]

    timeMapping[time] = len(timeMapping) + 1

    if command =="add":
        name = line[2]
        size = int(line[3])
        add_program(time, name, size)
    elif command =="remove":
        name = line[2]
        remove_program(name)
    elif command =="query":
        time1 = int(line[2])
        time2 = int(line[3])
        result = query_programs(time1, time2)
        print(result)
