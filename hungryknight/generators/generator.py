#!/usr/bin/env python3
import random
import sys

def generate_small():

    n = random.randint(5, 10)
    m = random.randint(1, min(4, 16))
    k = random.randint(m*2, min(50, 10000))
    
    r0 = random.randint(0, n-1)
    c0 = random.randint(0, n-1)
    
    print(f"{n} {m} {k}")
    print(f"{r0} {c0}")
    
    used = {(r0, c0)}
    for i in range(m):
        while True:
            r = random.randint(0, n-1)
            c = random.randint(0, n-1)
            if (r, c) not in used:
                used.add((r, c))
                v = random.randint(1, 100)
                print(f"{v} {r} {c}")
                break

def generate_medium():

    n = random.randint(20, 100)
    m = random.randint(5, 12)
    k = random.randint(m*3, min(500, 10000))
    
    r0 = random.randint(0, n-1)
    c0 = random.randint(0, n-1)
    
    print(f"{n} {m} {k}")
    print(f"{r0} {c0}")
    
    used = {(r0, c0)}
    for i in range(m):
        while True:
            r = random.randint(0, n-1)
            c = random.randint(0, n-1)
            if (r, c) not in used:
                used.add((r, c))
                v = random.randint(10, 1000)
                print(f"{v} {r} {c}")
                break

def generate_large():

    n = random.randint(200, 500)
    m = random.randint(12, 16)
    k = random.randint(100, min(2000, 10000))
    
    r0 = random.randint(0, n-1)
    c0 = random.randint(0, n-1)
    
    print(f"{n} {m} {k}")
    print(f"{r0} {c0}")
    
    used = {(r0, c0)}
    for i in range(m):
        while True:
            r = random.randint(0, n-1)
            c = random.randint(0, n-1)
            if (r, c) not in used:
                used.add((r, c))
                v = random.randint(100, 1000)
                print(f"{v} {r} {c}")
                break

def generate_max():

    n = 500
    m = 16
    k = random.randint(1000, 10000)
    
    r0 = random.randint(0, n-1)
    c0 = random.randint(0, n-1)
    
    print(f"{n} {m} {k}")
    print(f"{r0} {c0}")
    
    used = {(r0, c0)}
    for i in range(m):
        while True:
            r = random.randint(0, n-1)
            c = random.randint(0, n-1)
            if (r, c) not in used:
                used.add((r, c))
                v = random.randint(100, 1000)
                print(f"{v} {r} {c}")
                break

def generate_edge_no_enemies():

    n = random.randint(10, 100)
    m = 0
    k = random.randint(10, 100)
    
    r0 = random.randint(0, n-1)
    c0 = random.randint(0, n-1)
    
    print(f"{n} {m} {k}")
    print(f"{r0} {c0}")

def generate_edge_no_moves():

    n = random.randint(10, 50)
    m = random.randint(1, 8)
    k = 0
    
    r0 = random.randint(0, n-1)
    c0 = random.randint(0, n-1)
    
    print(f"{n} {m} {k}")
    print(f"{r0} {c0}")
    
    used = {(r0, c0)}
    for i in range(m):
        while True:
            r = random.randint(0, n-1)
            c = random.randint(0, n-1)
            if (r, c) not in used:
                used.add((r, c))
                v = random.randint(1, 100)
                print(f"{v} {r} {c}")
                break

def generate_edge_unreachable():
    # hardcoded edge case where the knight cannot reach any enemies
    n = 20
    m = 2
    k = 5
    
    print(f"{n} {m} {k}")
    print("0 0")
    
    print("1000 19 19")
    print("500 10 15")

def generate_smallboard():

    n = random.randint(5, 8)
    m = random.randint(2, min(4, 16))
    k = random.randint(10, 50)
    
    r0 = random.randint(0, n-1)
    c0 = random.randint(0, n-1)
    
    print(f"{n} {m} {k}")
    print(f"{r0} {c0}")
    
    used = {(r0, c0)}
    for i in range(m):
        attempts = 0
        # don't want infinite loop
        while attempts < 100:
            r = random.randint(0, n-1)
            c = random.randint(0, n-1)
            if (r, c) not in used:
                used.add((r, c))
                v = random.randint(10, 200)
                print(f"{v} {r} {c}")
                break
            attempts += 1

def generate_worst():

    n = 50  # smallish board
    m = 16
    k = 200  # enough moves to reach all enemies
    
    # start in the center
    r0 = n // 2
    c0 = n // 2
    
    print(f"{n} {m} {k}")
    print(f"{r0} {c0}")
    
    # placing enemies in a circle around center
    import math
    used = {(r0, c0)}
    
    for i in range(m):
        angle = 2 * math.pi * i / m
        radius = 8
        r = int(r0 + radius * math.sin(angle))
        c = int(c0 + radius * math.cos(angle))
        
        r = max(0, min(n-1, r))
        c = max(0, min(n-1, c))
        
        attempts = 0
        while (r, c) in used and attempts < 20:
            r = (r + 1) % n
            c = (c + 1) % n
            attempts += 1
        
        used.add((r, c))
        v = 100 + random.randint(-10, 10) # small variation in value
        print(f"{v} {r} {c}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generator_type = sys.argv[1]
        
        generators = {
            "small": generate_small,
            "medium": generate_medium,
            "large": generate_large,
            "max": generate_max,
            "edge_no_enemies": generate_edge_no_enemies,
            "edge_no_moves": generate_edge_no_moves,
            "edge_unreachable": generate_edge_unreachable,
            "smallboard": generate_smallboard,
            "worst": generate_worst,
        }
        
        if generator_type in generators:
            generators[generator_type]()
        else:
            print(f"unknown generator type: {generator_type}", file=sys.stderr)
            sys.exit(1)
    else:
        random.choice([generate_small, generate_medium, generate_large])()