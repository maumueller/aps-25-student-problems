n = int(input())

numbs = []

for _ in range(n):
	numbs.append(list(map(int, input().split())))

sum = numbs[0][0] # first one always
index = 0

for i in range(1, n):
    search = numbs[i]

    left, right = search[index], search[index + 1]

    if left > right:
         sum += right
         index += 1
    else:
         sum += left

print(sum)