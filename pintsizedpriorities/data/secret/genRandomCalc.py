import random

n = 5 * 10**5
m = n

domain = [f"{n} {m}"]

for i in range(n):
    domain.append(f"1 {i}")

print("\n".join(domain))

calc = []
for _ in range(m):
    calc.append("calculate")
    first = random.randint(0, m-1)
    second = random.randint(0, m-1)
    if first > second:
        first, second = second, first
    calc.append(str(first))
    calc.append(str(second))

print("\n".join(calc))
    


