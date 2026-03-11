n = int(input())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

ans = 0
for i in range(n): # for each i, place w[i] in position i of v
    j = i # find v[i] in w at index j
    while w[j] != v[i]:
        j += 1

    while j > i: # swap it repeatedly to its right place
        (w[j], w[j - 1]) = (w[j - 1], w[j])
        j -= 1
        ans += 1

print(ans)