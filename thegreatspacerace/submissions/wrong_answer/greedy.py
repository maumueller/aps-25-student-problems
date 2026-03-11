import math

value = int(input())
m = list(map(int, input().split()))

s = list(m)
list.sort(s, reverse = True)
for i in range(len(s)): s[i] = [s[i], 0]
sum = 0

for el in s:
    if el[0] == 0: continue
    val = math.floor((value - sum) / el[0])
    el[1] = val
    sum += val * el[0]

    if (el == s[-1] and sum < value) or (el == s[-2] and sum < value and s[-1][0] == 0):
        val = math.ceil((value - sum) / el[0]) 
        el[1] += val
        sum += val * el[0]

result = {}
for el in s: result[el[0]] = el[1]

for i in range(len(m)):
    print (result[m[i]], m[i])