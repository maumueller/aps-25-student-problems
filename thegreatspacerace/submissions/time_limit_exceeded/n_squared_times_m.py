value = int(input())
m = list(map(int, input().split()))

s = list(m)
list.sort(s, reverse = True)
cap = max((value-1)*2, s[0])
uses = [int(cap/el) if el > 0 else 0 for el in s]
maxUses = [[0, 0] for _ in uses]
for x in range(len(s)): maxUses[x] = [s[x], uses[x]]
sumvalues = [[float('inf') if x > 0 else [0, {}] for x in range (cap+1)] for _ in range (sum(uses)+1)]


progress = 0
for el in maxUses:
    for i in range(el[1]):
        placement = progress + i
        for x in range(cap + 1):
            y = x + el[0]
            if y > cap: 
                if sumvalues[placement][x] != float('inf') and sumvalues[placement+1][x] == float('inf'):
                    sumvalues[placement+1][x] = sumvalues[placement][x]
                continue
            if sumvalues[placement][x] == float('inf'): continue
            if sumvalues[placement][y] == float('inf') or sumvalues[placement][y][0] > sumvalues[placement][x][0] + 1: 
                sumvalues[placement+1][y] = [sumvalues[placement][x][0] + 1, dict(sumvalues[placement][x][1])]
                sumvalues[placement+1][y][1][el[0]] = sumvalues[placement+1][y][1].get(el[0], 0) + 1
            if sumvalues[placement][x] != float('inf') and sumvalues[placement+1][x] == float('inf'):
                sumvalues[placement+1][x] = sumvalues[placement][x]
        # print (i, el[1], el[0], placement + 1, sumvalues[placement + 1])
    progress += el[1]
        
result = float('inf')
for x in range (value, cap + 1): 
    if sumvalues[-1][x] != float('inf'): 
        result = sumvalues[-1][x]
        break

for i in range(len(m)):
    print (result[1].get(m[i], 0), m[i])
