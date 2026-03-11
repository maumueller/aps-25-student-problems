#!/usr/bin/env python3

import sys
from collections import deque


# return full distance matrix instead of just distances to targets
def bfs(n, start):
    dist = [[-1]*n for _ in range(n)]
    qr, qc = start
    dist[qr][qc] = 0
    dq = deque([(qr, qc)])
    moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    while dq:
        r, c = dq.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                dq.append((nr,nc))
    # returning entire matrix instead of specific targeets
    return dist

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n, m, k = map(int, (next(it), next(it), next(it)))
    # doesn't subtract 1 from coordinates (0-indexed vs 1-indexed issue)
    r0, c0 = map(int, (next(it), next(it)))
    enemies = []
    for _ in range(m):
        v = int(next(it))
        r = int(next(it))
        c = int(next(it))
        # storing as tuple with all info instead of separate lists
        enemies.append((v, r, c))

    if m == 0:
        print(0)
        return

    # get the distance from knight to all positions
    dist_from_start = bfs(n, (r0,c0))
    
    # calc distances from all enemy positions
    dist_from_enemy = []
    for i in range(m):
        _, r, c = enemies[i]
        # full matrix for each enemy
        dist_from_enemy.append(bfs(n, (r, c)))

    # DP with bad memoization
    memo = {}
    
    def dp(mask, pos_r, pos_c, moves_left):
        # memoization key includes exact position (pos_r, pos_c)
        # creating n*n states per mask instead of just m states
        key = (mask, pos_r, pos_c, moves_left)
        
        if key in memo:
            return memo[key]

        current_value = 0
        for i in range(m):
            if mask & (1 << i):
                current_value += enemies[i][0]
        
        best_value = current_value
        
        for next_enemy in range(m):
            if mask & (1 << next_enemy):
                continue
            
            enemy_r, enemy_c = enemies[next_enemy][1], enemies[next_enemy][2]
            
            # manhattan distance for no reason :D
            dist = abs(pos_r - enemy_r) + abs(pos_c - enemy_c)
            
            # determining the actual distance based on current position
            actual_dist = None
            if pos_r == r0 and pos_c == c0:
                actual_dist = dist_from_start[enemy_r][enemy_c]
            else:
                # searching through all enemies to find current position
                for i in range(m):
                    if enemies[i][1] == pos_r and enemies[i][2] == pos_c:
                        actual_dist = dist_from_enemy[i][enemy_r][enemy_c]
                        break
                
                # recalculating BFS if not at an enemy position
                if actual_dist is None:
                    temp_dist = bfs(n, (pos_r, pos_c))
                    actual_dist = temp_dist[enemy_r][enemy_c]
            
            if actual_dist != -1 and actual_dist <= moves_left:
                new_mask = mask | (1 << next_enemy)
                # recursion instead of iterative DP
                value = dp(new_mask, enemy_r, enemy_c, moves_left - actual_dist)
                best_value = max(best_value, value)
        
        memo[key] = best_value
        return best_value
    
    max_value = 0
    
    # start from initial position
    max_value = max(max_value, dp(0, r0, c0, k))
    
    # tries starting from positions within 3 moves, multiplyingh the work 
    if k >= 3:
        visited = set()
        queue = deque([(r0, c0, 0)])
        visited.add((r0, c0))
        
        while queue:
            r, c, moves = queue.popleft()
            
            if moves > 0 and moves <= 3:
                # calling DP from many different starting positions
                value = dp(0, r, c, k - moves)
                max_value = max(max_value, value)
            
            if moves < 3:
                for dr, dc in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, moves + 1))
    
    print(max_value)

if __name__ == "__main__":
    main()