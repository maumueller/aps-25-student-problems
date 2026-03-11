import math
from sys import stdin

class IntervalDS:
    """A generic class that implements interval queries."""
    def __init__(self, n):
        """Initialize data structure to handle interval queries
           on n elements"""
        raise NotImplementedError()

    def update(self, i, k):
        """Set i-th element to k"""
        raise NotImplementedError()

    def get(self, i):
        """value of element position i"""
        raise NotImplementedError()

    def query(self, i, j):
        """Return sum of elements from i-th to j-th elements"""
        raise NotImplementedError()

class SQ(IntervalDS):
    """An implementation of the square-root algorithm."""
    def __init__(self, n):
        self.blocks = math.ceil(n**.5) + 1
        self.block_size = math.ceil(n**.5)
        self.A = [0 for _ in range(n + 1)]
        self.B = [0 for _ in range(self.blocks)]

    def update(self, i, k):
        block = i // self.block_size
        self.B[block] -= self.A[i]
        self.B[block] += k
        self.A[i] = k 
    
    def get(self, i):
        return self.A[i]

    def add(self, i, k):
        tmp = self.get(i)
        self.update(i, tmp + k)

    def query(self, i, j):
        first_i = (i // self.block_size) * self.block_size
        last_j = (j // self.block_size) * self.block_size + self.block_size - 1
        s = sum(self.B[i // self.block_size : j // self.block_size + 1])
        s -= sum(self.A[first_i : i])
        s -= sum(self.A[j + 1 : last_j + 1])
        return s


input = lambda: stdin.readline().strip()

N, M = map(int, input().split())


sq = SQ(N) #Maybe add 1
m = {}
arr = []

for i in range(N):
    inp = input().split()
    amount = int(inp[0])
    task = " ".join(inp[1:])
    m[task] = i 
    sq.add(i, amount)
for _ in range(M):
    inp = input()
    if inp == "calculate":
        fst = m[input()]
        snd = m[input()]
        answer = sq.query(fst, snd)
        arr.append(answer) # make faster print
    else:
        inp = input().split()
        n = int(inp[0])
        task = " ".join(inp[1:])
        sq.add(m[task], n)

for element in arr:
    print(element)
