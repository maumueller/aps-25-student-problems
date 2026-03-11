import random
import sys
import time

def solve():
    # Read all input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    n = int(next(iterator))
    mini = int(next(iterator))
    maxi = int(next(iterator))

    crate = []
    for _ in range(n):
        s = int(next(iterator))
        weights = []
        for _ in range(s):
            weights.append(int(next(iterator)))
        crate.append(weights)

    amountOfTrue = 0
    # Increased simulations to reduce variance while staying within time limits.
    # Previous 10,000 iterations had too high variance (approx 2% failure rate).
    # 50,000 iterations reduces the standard error significantly.
    # 3-sigma error margin is approx 0.67%, which is safely within the 1% allowed.
    simulations = 50000

    for _ in range(simulations):
        result = 0
        for sides in crate:
            result += random.choice(sides)
        
        if mini <= result <= maxi:
            amountOfTrue += 1

    print(f"{(amountOfTrue * 100) / simulations:.2f}%")

if __name__ == "__main__":
    solve()
