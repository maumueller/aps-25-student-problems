#This is a solution provided by chatGPT. It only checks paths through the centre of a space station, which is wrong

import math
import sys

def read_input():
    N = int(sys.stdin.readline())
    stations = []
    for _ in range(N):
        x, y, z = map(float, sys.stdin.readline().split())
        stations.append((x, y, z))
    return stations

def norm(v):
    return math.sqrt(sum(x*x for x in v))

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def projection_distance(p, dir_unit):
    # Project point p onto dir_unit
    dot_prod = dot(p, dir_unit)
    proj = tuple(dot_prod * x for x in dir_unit)
    diff = tuple(px - qx for px, qx in zip(p, proj))
    return norm(diff)

def solve(stations):
    max_count = 0
    for vx, vy, vz in stations:
        v_len = math.sqrt(vx*vx + vy*vy + vz*vz)
        dir_unit = (vx/v_len, vy/v_len, vz/v_len)
        count = 0
        for sx, sy, sz in stations:
            d = projection_distance((sx, sy, sz), dir_unit)
            if d <= 1 + 1e-3:  # small epsilon margin
                count += 1
        max_count = max(max_count, count)
    print(max_count)

if __name__ == "__main__":
    stations = read_input()
    solve(stations)
