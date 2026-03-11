
n = 5 * 10**5 
m = n

domain = [f"{n} {m}"]

for i in range(n):
    domain.append(f"1 {i}")

print("\n".join(domain))

calc = []
for i in range(m-1):
    calc.append("add")
    calc.append(f"{i-1000000} {i}")

calc.append("calculate")
calc.append(str(0))
calc.append(str(m-1))

print("\n".join(calc))
    


