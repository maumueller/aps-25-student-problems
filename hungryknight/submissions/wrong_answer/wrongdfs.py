knight_moves = [(2,1), (2, -1), (1, 2), (1,-2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]

def dfs(board_size, pos, enemies, moves_left, captured):
    if moves_left == 0:
        return 0

    max_value = 0
    for kx, ky in knight_moves:
        mx, my = pos[0] + kx, pos[1] + ky
        if 0 <= mx < board_size and 0 <= my < board_size:
            new_pos = (mx, my)
            value = 0
            new_captured = captured
            if new_pos in enemies:
                value = enemies[new_pos]
                new_captured = tuple(sorted(set(captured) | {new_pos}))
            max_value = max(max_value, value + dfs(board_size, new_pos, enemies, moves_left-1, new_captured))
    return max_value



n, m, k = map(int, input().split())
x, y = map(int, input().split())
pos = (x,y)
enemies = {}
for _ in range(m):
    v, x, y = map(int, input().split())
    enemies[x,y] = v

print(dfs(n, pos, enemies, k, tuple()))
