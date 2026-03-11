from sys import stdin

class FenwickTree():

    def __init__(self, n):
        self.A = [0 for _ in range(n + 1)]

    def get(self, i):
        return self.prefix_sum(i) - self.prefix_sum(i - 1)

    def update(self, i, k):
        self.add(i, k - self.get(i))
        
    def add(self, i, k):
        while i < len(self.A):
            self.A[i] += k
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.A[i]
            i -= i & -i
        return s

    def query(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

def input():
    return stdin.readline().strip()


N, M = map(int, input().split()) 

sq = FenwickTree(N) #Maybe add 1
m = {}
arr = []

for i in range(1, N + 1):
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
