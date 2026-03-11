import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    v = [0] * (n + 2)
    bit = [0] * (n + 2)

    idx = 1
    for i in range(1, n + 1):
        x = int(data[idx])
        v[x] = i
        idx += 1

    ans = n * (n - 1) // 2

    for i in range(n):
        x = int(data[idx])
        idx += 1
        pos = v[x]
        # query
        res = 0
        j = pos
        while j:
            res += bit[j]
            j -= j & -j
        ans -= res
        # update
        j = pos
        while j <= n:
            bit[j] += 1
            j += j & -j

    print(ans)

if __name__ == '__main__':
    main()

#CPU time: 0.969 seconds
#Peak memory usage: 165.02 MiB