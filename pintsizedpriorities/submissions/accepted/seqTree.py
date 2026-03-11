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

class SegmentTree(IntervalDS):
    """A segment tree implementation."""
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N *= 2
        self.A = [0 for _ in range(2 * self.N)]

    def get(self, i):
        return self.A[self.N + i]
    
    def update(self, i, k):
        p = self.N + i
        self.A[p] = k
        p //= 2
        while p > 0:
            self.A[p] = self.A[2 * p] + self.A[2 * p + 1]
            p //= 2

    def add(self, i, k):
        tmp = self.get(i)
        self.update(i, tmp + k)
    
    def query(self, i, j):
        #return self.__top_down_range_sum(1, 0, self.N, i, j + 1)
        return self.__bottom_up_range_sum(i, j)


    def __bottom_up_range_sum(self, i, j):
        i += self.N
        j += self.N

        s = 0
        while i <= j:
            if i % 2 == 1:
                s += self.A[i]
                i += 1
            if j % 2 == 0:
                s += self.A[j]
                j -= 1
            i //= 2
            j //= 2
        return s

    def __top_down_range_sum(self, p, start, span, i, j):
        if start + span <= i or j <= start:
            return 0
        if i <= start and start + span <= j:
            return self.A[p]
        left = self.__top_down_range_sum(2 * p, start, span // 2, i, j)
        right = self.__top_down_range_sum(2*p + 1, start + span // 2, span // 2, i, j)
        return left + right



input = lambda: stdin.readline().strip()

N, M = map(int, input().split())


sq = SegmentTree(N) #Maybe add 1
m = {}
arr = []

for i in range(0, N):
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
