#!/usr/bin/env python3
import sys
import re

def parse_ints(line):
    parts = line.strip().split()
    for i in parts:
        if not re.fullmatch(r"(0|[1-9][0-9]*)", i):
            print(f"Non integer found", i)
            sys.exit(43)
    return list(map(int, parts))

def validate():
    try:
        # first line  n m k
        line1 = sys.stdin.readline()
        # print(f"Hm... {line1}", file=sys.stderr)
        n, m, k = parse_ints(line1)

        if not (1 <= n <= 500):
            print(f"Invalid n: {n}", file=sys.stderr)
            sys.exit(43)
        if not (0 <= m <= 16):
            print(f"Invalid m: {m}", file=sys.stderr)
            sys.exit(43)
        if not (0 <= k <= 10000):
            print(f"Invalid k: {k}", file=sys.stderr)
            sys.exit(43)

        line2 = sys.stdin.readline()
        # print(f"Hm... {line2}", file=sys.stderr)
        r0, c0 = parse_ints(line2)
        if not (0 <= r0 < n and 0 <= c0 < n):
            print(f"Knight position out of bounds: ({r0},{c0})", file=sys.stderr)
            sys.exit(43)

        seen_positions = set()
        seen_positions.add((r0, c0))
        
        for i in range(m):
            line = sys.stdin.readline()
            if not line:
                print(f"Missing enemy line {i+1}", file=sys.stderr)
                sys.exit(43)

            v, r, c = parse_ints(line)
            if not (1 <= v <= 10000):
                print(f"Invalid value {v}", file=sys.stderr)
                sys.exit(43)
            
            if not (0 <= r < n and 0 <= c < n):
                print(f"Enemy position out of bounds: ({r},{c})", file=sys.stderr)
                sys.exit(43)

            if (r, c) in seen_positions:
                print(f"Duplicate enemy position: ({r},{c})", file=sys.stderr)
                sys.exit(43)
            seen_positions.add((r, c))

        remaining = sys.stdin.read().strip()
        if remaining:
            print("Extra data at the end", file=sys.stderr)
            sys.exit(43)

    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        sys.exit(43)

if __name__ == "__main__":
    validate()
    sys.exit(42)