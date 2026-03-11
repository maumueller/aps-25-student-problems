import bisect


class SegmentTree:
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

    def query(self, i, j):
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


# This shows an error that can occur if it is assumed that query/remove timestamps can just point to the previous add timestamp.
# This is not the case since a query can also query timestamps where nothing was added ie only query/remove happened

cur_index = 0
ts_to_index = {}
prog_to_index = {}

n = int(input())
tree = SegmentTree(n)

for _ in range(n):
    req = input().split()
    if req[1] == "add":
        ts, _, prog, size = req

        ts_to_index[int(ts)] = cur_index
        tree.update(cur_index, int(size))
        prog_to_index[prog] = cur_index
        cur_index += 1
    elif req[1] == "remove":
        ts, _, prog = req
        ts_to_index[int(ts)] = max(cur_index - 1, 0)
        tree.update(prog_to_index[prog], 0)


    elif req[1] == "query":
        ts, _, t1, t2 = req
        ts_to_index[int(ts)] = max(cur_index - 1, 0)

        i1 = ts_to_index[int(t1)]
        i2 = ts_to_index[int(t2)]
        print(tree.query(i1, i2))
    else:
        print("Error in input")
