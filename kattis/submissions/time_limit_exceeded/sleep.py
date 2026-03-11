import sys
from collections import defaultdict

def calculate_success_probability(n, min_val, max_val, dice):
    dp = defaultdict(float)
    dp[0] = 1.0  # probability of sum 0 at the start

    for die in dice:
        new_dp = defaultdict(float)
        for total_weight, prob in dp.items():
            for component in die:
                new_dp[total_weight + component] += prob / len(die)
        dp = new_dp

    # Sum probabilities for weights in [min_val, max_val]
    result = sum(prob for weight, prob in dp.items() if min_val <= weight <= max_val)
    return result


n, min_val, max_val = map(int, sys.stdin.readline().split())
dice = []
for _ in range(n):
    parts = list(map(int, sys.stdin.readline().split()))
    dice.append(parts[1:])  # skip the count, use weights

probability = calculate_success_probability(n, min_val, max_val, dice)
probability = probability*100
print(f"{probability:.2f}"+"%")

