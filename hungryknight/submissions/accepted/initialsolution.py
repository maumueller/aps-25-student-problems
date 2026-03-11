#!/usr/bin/env python3

import sys
from collections import deque

# all pairs shortest path problem 

# function for running the BFS algo from the starting pos of the knight amd each piece to get the distances, 
# that returns the distances to each piece or -1 if unreachable m
def bfs(n, start, targets):

    dist = [[-1]*n for _ in range(n)]
    qr, qc = start
    dist[qr][qc] = 0
    dq = deque([(qr, qc)])
    moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    while dq:
        r, c = dq.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c +dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                dq.append((nr,nc))
    return [dist[r][c] for (r,c) in targets]

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n, m, k = map(int, (next(it), next(it), next(it)))
    r0, c0 = map(lambda x: int(x)-1, (next(it), next(it)))
    positions = []
    points = []
    for _ in range(m):
        p = int(next(it))
        r = int(next(it)) - 1
        c = int(next(it)) - 1
        points.append(p)
        positions.append((r,c))

    # get the distance from knight to each piece
    dist0 = bfs(n, (r0,c0), positions)

    # calc distances between all opponents pieces
    dist_mat = [[-1] * m for _ in range(m)]
    for i in range(m):
        row = bfs(n, positions[i], positions)
        for j in range(m):
            dist_mat[i][j] = row[j]

    # dp[mask][last] = min moves to visit mask ending at last
    INF = 10 ** 9
    maxmask = 1<<m
    dp = [[INF]* m for _ in range(maxmask)]

    # go from start directly to each piece i
    for i in range(m):
        d = dist0[i]
        if d != -1 and d <= k:
            dp[1<<i][i] = d

    # build masks
    for mask in range(maxmask):
        for last in range(m):
            if not (mask & (1<<last)): 
                continue
            dcur = dp[mask][last]
            if dcur > k: 
                continue
            for nxt in range(m):
                if mask & (1<<nxt): 
                    continue
                dstep = dist_mat[last][nxt]
                if dstep == -1: 
                    continue
                nd = dcur + dstep
                newmask = mask | (1<<nxt)
                if nd < dp[newmask][nxt]:
                    dp[newmask][nxt] = nd

    # finding the best total points for all masks with dp ≤ k
    best = 0
    for mask in range(maxmask):
        for last in range(m):
            if dp[mask][last] <= k:
                s = 0
                for i in range(m):
                    if mask & (1<<i):
                        s += points[i]
                best = max(best, s)

    print(best)

if __name__ == "__main__":
    main()
