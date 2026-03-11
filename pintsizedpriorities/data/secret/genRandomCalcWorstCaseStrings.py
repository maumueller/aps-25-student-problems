import random

n = 5 * 10**5
m = n


domain = [f"{n} {m}"]

for i in range(n):
    domain.append(f"1 {i:050}")

print("\n".join(domain))

calc = []
for _ in range(m):
    calc.append("calculate")
    first = random.randint(0, m-1)
    second = random.randint(0, m-1)
    if first > second:
        first, second = second, first
    calc.append(f"{first:050}")
    calc.append(f"{second:050}")

print("\n".join(calc))
    



