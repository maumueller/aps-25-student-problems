import random

n = 5 * 10**5
m = n

domain = [f"{n} {m}"]

for i in range(n):
    domain.append(f"1 {i}")

print("\n".join(domain))

calc = []
for _ in range(m-1):
    calc.append("add")
    first = random.randint(0, 2**31-1)
    name = random.randint(0, m-1)
    calc.append(f"{first} {name}")


calc.append("calculate")
calc.append(str(0))
calc.append(str(m-1))

print("\n".join(calc))
    


