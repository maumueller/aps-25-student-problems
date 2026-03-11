#This solution is provided by chatgpt. It claims to check for the answer within some positions within a cone, as a circular grid (i think).

import sys
import math

def read_input():
    data = sys.stdin.read().split()
    N = int(data[0])
    coords = []
    idx = 1
    for _ in range(N):
        x = float(data[idx])
        y = float(data[idx+1])
        z = float(data[idx+2])
        coords.append((x, y, z))
        idx += 3
    return coords

def norm(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def normalize(v):
    length = norm(v)
    return (v[0]/length, v[1]/length, v[2]/length)

def generate_unit_sphere_points(num_theta=100, num_phi=200):
    directions = []
    for i in range(1, num_theta):  # avoid poles
        theta = math.pi * i / num_theta
        for j in range(num_phi):
            phi = 2 * math.pi * j / num_phi
            x = math.sin(theta) * math.cos(phi)
            y = math.sin(theta) * math.sin(phi)
            z = math.cos(theta)
            directions.append((x, y, z))
    return directions

def solve(stations):
    sample_dirs = generate_unit_sphere_points()
    counts = [0 for _ in sample_dirs]

    for px, py, pz in stations:
        p_vec = (px, py, pz)
        dist = norm(p_vec)
        if dist <= 1.0:
            # Covers the whole sphere — too close to origin
            continue
        theta = math.asin(1.0 / dist)
        p_unit = normalize(p_vec)

        for i, dir_vec in enumerate(sample_dirs):
            # angle between vectors = arccos(dot)
            dp = dot(p_unit, dir_vec)
            if dp >= math.cos(theta):  # angle ≤ θ
                counts[i] += 1

    print(max(counts))

stations = read_input()
solve(stations)
