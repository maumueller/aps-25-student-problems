from sys import setrecursionlimit

setrecursionlimit(10_000)

n = int(input())
triangle = []

for i in range(n):
	triangle.append(list(map(int, input().split())))

def triangleSolution(i: int, j: int):
	if i == n - 1:
		return triangle[i][j]
	else:
		return triangle[i][j] + min(triangleSolution(i + 1, j), triangleSolution(i + 1, j + 1))

print(triangleSolution(0, 0))