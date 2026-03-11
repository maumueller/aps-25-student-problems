import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    v = [0] * (n + 2)
    bit = [0] * (n + 2)

    # Read first permutation and store positions
    tokens = []
    while len(tokens) < n:
        tokens += list(map(int, input().split()))
    for i, x in enumerate(tokens, 1):
        v[x] = i

    # Fenwick Tree functions (1-based)
    def update(i):
        while i <= n:
            bit[i] += 1
            i += i & -i

    def query(i):
        res = 0
        while i:
            res += bit[i]
            i -= i & -i
        return res

    # Read second permutation and compute answer
    ans = n * (n - 1) // 2
    tokens = []
    while len(tokens) < n:
        tokens += list(map(int, input().split()))
    for x in tokens:
        ans -= query(v[x])
        update(v[x])

    print(ans)

if __name__ == '__main__':
    main()


#CPU time: 1.078 seconds
#Peak memory usage: 145.97 MiB