n = int(input())

numbs = []

for _ in range(n):
	numbs.append(list(map(int, input().split())))
	
dp = [[0] * (i + 1) for i in range(n)]

for i in range(n-1, -1, -1):
	for j in range(i + 1):
		if i == n - 1:
			dp[i][j] = numbs[i][j]
		else:
			dp[i][j] = numbs[i][j] + min(
				dp[i + 1][j], 
				dp[i + 1][j + 1]
            )

print(dp[0][0])