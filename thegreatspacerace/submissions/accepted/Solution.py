import time


value = int(input())
m = list(map(int, input().split()))

t = time.time()

s = list(m)
list.sort(s, reverse = True)

cap = min((value - 1) + s[0], max((value - 1) * 2, s[0]))
if s[0] > value: cap = s[0]
sumvalues = [None] * (cap + 1)
sumvalues[0] = [0, {}]

done = False

for el in s:
    for x in range(cap + 1):
        if sumvalues[x] is None: 
            continue
        y = x + el
        if y > cap: 
            continue
        if sumvalues[y] is None or not sumvalues[y][0] <= sumvalues[x][0] + 1: 
            temp = [sumvalues[x][0] + 1, dict(sumvalues[x][1])]
            temp[1][el] = temp[1].get(el, 0) + 1
            sumvalues[y] = temp
        if y == value: 
            done = True
            break
        if y > value: 
            break
    if done: break

#print(time.time() - t)

result = None
for x in range (value, cap + 1): 
    if sumvalues[x] is not None: 
        result = sumvalues[x]
        break

for i in range(len(m)):
    print (result[1].get(m[i], 0), m[i])

#print(time.time() - t)
